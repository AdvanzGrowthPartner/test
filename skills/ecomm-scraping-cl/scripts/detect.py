#!/usr/bin/env python3
"""
Ecomm Scraping (CL) — detector de plataforma y stack para prospección outbound.

Uso:
    python3 detect.py "https://marca1.cl" "https://marca2.cl" ...

Por cada URL imprime un bloque JSON con: plataforma, myshopify_domain (si aplica),
señales de stack (meta pixel, google tag, analytics, tiktok, klaviyo, clarity, reviews),
tamaño de catálogo, y contacto (whatsapp, instagram, correos).

Diseñado para correr desde un entorno con acceso a red. No requiere dependencias
externas más allá de la stdlib (usa urllib). Es tolerante a fallos: si una marca
está bloqueada por Cloudflare, cae al endpoint /meta.json (firma dura de Shopify).
"""

import json
import re
import ssl
import sys
import urllib.request
import urllib.error
from http.client import RemoteDisconnected

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

TIMEOUT = 15


def fetch(url, timeout=TIMEOUT):
    """Devuelve (status_code, body_text). status 0 = no resolvió / error de red."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "es-CL,es;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/json,*/*",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            raw = r.read()
            try:
                body = raw.decode("utf-8", errors="ignore")
            except Exception:
                body = str(raw)
            return r.status, body
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", errors="ignore")
        except Exception:
            body = ""
        return e.code, body
    except (urllib.error.URLError, RemoteDisconnected, TimeoutError, ssl.SSLError,
            ConnectionResetError, OSError):
        return 0, ""
    except Exception:
        return 0, ""


def norm(url):
    url = url.strip().rstrip("/")
    if not url.startswith("http"):
        url = "https://" + url
    return url


def detect_platform(html):
    h = html.lower()
    if re.search(r"cdn\.shopify|/cdn/shop/|myshopify|shopify\.shop", h):
        return "Shopify"
    if re.search(r"woocommerce|wp-content", h):
        return "WooCommerce"
    if "jumpseller" in h:
        return "Jumpseller"
    if re.search(r"wixstatic|x-wix", h):
        return "Wix"
    if re.search(r"tiendanube|mitiendanube", h):
        return "Tiendanube"
    if re.search(r"vtexassets|vtex\.com", h):
        return "VTEX"
    return None


def hard_shopify_signature(base):
    """Ante Cloudflare (429 + body diminuto), /meta.json revela el myshopify_domain."""
    status, body = fetch(base + "/meta.json")
    m = re.search(r'"myshopify_domain"\s*:\s*"([^"]+)"', body or "")
    if m:
        return m.group(1)
    return None


def extract_signals(html):
    h = html
    sig = {}
    sig["meta_pixel"] = bool(re.search(r"fbq\(|connect\.facebook\.net", h, re.I))
    sig["google_tag"] = bool(re.search(r"gtag\(|googletagmanager", h, re.I))
    sig["analytics"] = bool(re.search(r"gtag\(|google-analytics|G-[A-Z0-9]{8,}|googletagmanager", h, re.I))
    sig["tiktok"] = bool(re.search(r"ttq\.|analytics\.tiktok", h, re.I))
    sig["klaviyo"] = bool(re.search(r"klaviyo|_learnq", h, re.I))
    sig["clarity"] = bool(re.search(r"clarity\.ms", h, re.I))
    sig["google_ads"] = bool(re.search(r"googleadservices|AW-[0-9]{9,}|google_conversion", h, re.I))
    reviews = sorted(set(r.lower() for r in
                         re.findall(r"judge\.me|loox|okendo|yotpo|stamped|opinew", h, re.I)))
    sig["reviews"] = ",".join(reviews) if reviews else None
    sig["ads_activos"] = sig["meta_pixel"] or sig["google_ads"] or sig["tiktok"]
    return sig


def extract_contact(html):
    c = {}
    wa = re.search(r"(?:wa\.me/|api\.whatsapp\.com/send\?phone=)(\d{9,})", html, re.I)
    c["whatsapp"] = ("+" + wa.group(1)) if wa else None

    igs = re.findall(r"instagram\.com/([a-zA-Z0-9_.]+)", html, re.I)
    ig = None
    for cand in igs:
        if cand.lower() not in ("p", "reel", "reels", "explore", "accounts", ""):
            ig = cand
            break
    c["instagram"] = ("https://instagram.com/" + ig) if ig else None

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html)
    bad = ("sentry", "wixpress", "example", "schema", "googleapis", "gstatic",
           "cloudflare", "shopify", "jsdelivr", "googletagmanager", "facebook",
           "instagram", "yourstore", "email.com", "dominio.com", "sentry.io")
    clean = []
    for e in emails:
        el = e.lower()
        if any(b in el for b in bad):
            continue
        if re.search(r"\.(png|jpg|jpeg|gif|svg|css|js|webp|min)", el):
            continue
        clean.append(e)
    clean = list(dict.fromkeys(clean))  # dedup keep order
    c["correo_contacto"] = clean[0] if clean else None
    c["correo_secundario"] = clean[1] if len(clean) > 1 else None
    return c


def catalog_size(base, platform):
    """Devuelve bucket 1-3 / 3-10 / +10 / None."""
    n = 0
    if platform == "Shopify":
        status, body = fetch(base + "/products.json?limit=250")
        n = len(re.findall(r'"id"\s*:\s*\d+', body or ""))
    elif platform == "WooCommerce":
        for path in ("/product-sitemap.xml", "/wp-sitemap-posts-product-1.xml"):
            status, body = fetch(base + path)
            n = len(re.findall(r"<loc>", body or ""))
            if n:
                break
    if n == 0:
        return None
    if n <= 3:
        return "1-3"
    if n <= 10:
        return "3-10"
    return "+10"


def analyze(url):
    base = norm(url)
    out = {"url": base, "plataforma": None, "myshopify_domain": None,
           "bloqueado": False, "signals": {}, "contacto": {}, "cartera_productos": None}

    status, html = fetch(base + "/")
    blocked = (status == 429) or (status in (0, 403, 503)) or (len(html) < 500)

    platform = detect_platform(html) if html else None

    if platform is None:
        # Intento firma dura (Shopify tras Cloudflare)
        dom = hard_shopify_signature(base)
        if dom:
            platform = "Shopify"
            out["myshopify_domain"] = dom
            out["bloqueado"] = True

    if platform == "Shopify" and out["myshopify_domain"] is None:
        m = re.search(r'"myshopify_domain"\s*:\s*"([^"]+)"', html)
        if m:
            out["myshopify_domain"] = m.group(1)

    out["plataforma"] = platform or "Por confirmar"

    if html and len(html) >= 500 and not blocked:
        out["signals"] = extract_signals(html)
        out["contacto"] = extract_contact(html)
        out["cartera_productos"] = catalog_size(base, platform)
    else:
        out["bloqueado"] = True
        # señales "Por verificar" — el pipeline las cierra a mano
        out["signals"] = {k: "Por verificar" for k in
                          ("meta_pixel", "google_tag", "analytics", "tiktok",
                           "klaviyo", "clarity", "google_ads", "reviews", "ads_activos")}

    out["http_status"] = status
    return out


def main():
    urls = sys.argv[1:]
    if not urls:
        print("Uso: python3 detect.py <url1> <url2> ...", file=sys.stderr)
        sys.exit(1)
    results = []
    for u in urls:
        try:
            results.append(analyze(u))
        except Exception as e:
            results.append({"url": u, "error": str(e)})
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
