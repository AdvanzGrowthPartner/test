# Detección de plataforma y stack — detalle

El script `scripts/detect.py` automatiza todo esto. Este documento explica el porqué y cómo manejar los casos que el script marca como ambiguos, para poder cerrarlos a mano.

## Firmas de plataforma (en el HTML del home)

| Plataforma | Firma |
|---|---|
| Shopify | `cdn.shopify`, `/cdn/shop/`, `myshopify`, `Shopify.shop` |
| WooCommerce | `woocommerce`, `wp-content` |
| Jumpseller | `jumpseller` |
| Wix | `wixstatic`, `X-Wix` |
| Tiendanube | `tiendanube`, `mitiendanube` |
| VTEX | `vtexassets`, `vtex.com` |

## Firma dura ante Cloudflare (la técnica clave)

Muchas tiendas Shopify están detrás de Cloudflare, que bloquea IPs de datacenter: el home devuelve **HTTP 429 con un body de ~18 bytes**. En ese caso el scraping normal no sirve, pero Shopify expone endpoints públicos que Cloudflare no siempre ratelimitea igual:

- **`/meta.json`** → devuelve JSON con `id`, `name` y `myshopify_domain`. Si responde, es Shopify confirmado, aunque el home esté bloqueado. Esta es la firma dura.
- `/products.json` a veces también pasa (da el catálogo).

Cuando esto ocurre: plataforma = Shopify (confirmada), pero los **tags de apps quedan `Por verificar`** porque no se pudo leer el HTML del home. Es esperado — se cierran en la fase de calificación del pipeline. No es un fallo del proceso.

## Señales de stack (grep del HTML)

| Señal | Patrón |
|---|---|
| Meta Pixel | `fbq(`, `connect.facebook.net` |
| Google Tag (GTM/gtag) | `gtag(`, `googletagmanager` |
| Analytics (GA4) | `G-XXXXXXXX`, `google-analytics`, `gtag(` |
| Google Ads | `googleadservices`, `AW-XXXXXXXXX`, `google_conversion` |
| TikTok Pixel | `ttq.`, `analytics.tiktok` |
| Klaviyo | `klaviyo`, `_learnq` |
| Microsoft Clarity | `clarity.ms` |
| Reviews | `judge.me`, `loox`, `okendo`, `yotpo`, `stamped`, `opinew` |

Nota: `Google Tag` y `Analytics Tag` suelen ir juntos (cuando hay `gtag`/GTM, ambos = Sí). Si se quiere distinguir contenedor GTM vs GA4 directo, revisar manualmente el HTML — el script los reporta juntos por defecto.

## Tamaño de catálogo

- **Shopify**: `GET /products.json?limit=250` y contar objetos `"id":`. Incluye variantes, así que cientos de "productos" puede significar un catálogo mediano con muchas variantes — leerlo como señal de tamaño, no como conteo exacto de SKUs.
- **WooCommerce**: `GET /product-sitemap.xml` (o `/wp-sitemap-posts-product-1.xml`) y contar `<loc>`.
- Buckets: `1-3` / `3-10` / `+10`.

Catálogos de cientos (ej. 1300+) suelen indicar revendedores grandes o marcas muy establecidas — dato relevante para el score y la facturación.

## Casos borde

- **Home da 0 productos en sitemap pero el catálogo existe**: muchas tiendas cargan productos vía JS/colecciones. El conteo del home puede dar 0 aunque haya catálogo. Si el `products.json` responde, ese conteo manda.
- **Redirect por JavaScript / plataforma headless**: si el home hace un refresh JS y no expone `meta.json` ni `products.json`, la plataforma no es confirmable como Shopify estándar. Marcar `Por confirmar` y anotarlo. No asumir.
- **Dominio no resuelve (status 0)**: el dominio no existe con ese nombre o está caído. NO inventar variantes ni cargar. Buscar el dominio correcto de la marca por su nombre + "sitio oficial".
- **Anti-bot fuerte (status 999 / 403 persistente)**: algunas marcas grandes bloquean todo scraping. Si `meta.json` tampoco responde, cargar con plataforma `Por confirmar` y señales `Por verificar`, anotando que tiene anti-bot. El dato de que existe y es marca propia sigue siendo válido para el prospecto.
- **WhatsApp con prefijo extranjero (+34, +1, etc.)**: bandera — verificar si la marca realmente opera en Chile o es una marca extranjera con presencia. Anotarlo en la ficha.
- **Correo placeholder de theme** (`shop@yourstore.com`, `email@dominio.com`, `email@email.com`): el script los filtra, pero si alguno se cuela, descartarlo — no es un correo real.

## Flujo de correo (cuando no está en el home)

Si el home no expone correo, probar en orden: `/contacto`, `/contact`, `/pages/contacto`, `/pages/contact`, `/politica-de-privacidad`, `/terminos-y-condiciones`. Muchas tiendas esconden el correo tras formularios o Cloudflare email-protection — en ese caso queda para el setting del pipeline.
