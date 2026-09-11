// Google Search Console — orgánico real (SEO + fichas Merchant + blogs), sin MCP.
// Secrets (propios de GSC; NO se comparten con Google Ads porque el scope es distinto):
//   GSC_CLIENT_ID, GSC_CLIENT_SECRET, GSC_REFRESH_TOKEN  (OAuth con scope
//     https://www.googleapis.com/auth/webmasters.readonly)
//   GSC_SITE_URL  → la propiedad. Dominio: "sc-domain:amazingcare.cl"
//                   (o prefijo URL: "https://amazingcare.cl/")
// Si autorizaste UN solo cliente OAuth para Ads + Search Console (ambos scopes),
// podés no setear los GSC_* y caerá a los GOOGLE_ADS_* como respaldo.
const SC = "https://searchconsole.googleapis.com/webmasters/v3/sites";

function cred(env) {
  return {
    client_id: env.GSC_CLIENT_ID || env.GOOGLE_ADS_CLIENT_ID,
    client_secret: env.GSC_CLIENT_SECRET || env.GOOGLE_ADS_CLIENT_SECRET,
    refresh_token: env.GSC_REFRESH_TOKEN || env.GOOGLE_ADS_REFRESH_TOKEN,
    site: env.GSC_SITE_URL || "sc-domain:amazingcare.cl",
  };
}
function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  const since = `${y}-${String(mo).padStart(2, "0")}-01`;
  const until = new Date(y, mo, 0).toISOString().slice(0, 10);
  return { since, until };
}
async function accessToken(c) {
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: c.client_id, client_secret: c.client_secret,
      refresh_token: c.refresh_token, grant_type: "refresh_token",
    }),
  });
  const j = await r.json();
  if (!j.access_token) throw new Error(j.error_description || "oauth failed");
  return j.access_token;
}
async function query(token, site, body) {
  const url = `${SC}/${encodeURIComponent(site)}/searchAnalytics/query`;
  const r = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "content-type": "application/json" },
    body: JSON.stringify(body),
  });
  const j = await r.json();
  if (j.error) throw new Error(j.error.message || "gsc error");
  return j.rows || [];
}
const BRAND = /amaz|amiz|ameaz|amagaz|amaizi|qmazi|aazing|antartic/i;
const pct = (c, i) => (i ? +(c / i * 100).toFixed(2) : 0);
const round1 = n => +Number(n).toFixed(1);

export async function gsc(env, month, opts = {}) {
  const c = cred(env);
  if (!c.refresh_token) return { error: "gsc not configured" };
  // Ventana: por defecto el mes pedido; opts.window="365" trae los últimos 12 meses.
  let since, until;
  if (opts.window === "365") {
    until = new Date(Date.now() - 2 * 864e5).toISOString().slice(0, 10); // GSC llega con ~2 días de rezago
    since = new Date(Date.now() - 367 * 864e5).toISOString().slice(0, 10);
  } else { ({ since, until } = monthRange(month)); }
  const token = await accessToken(c);
  const base = { startDate: since, endDate: until, type: "web", dataState: "all" };

  const [tot, dev, appr, queries, pages, byMonth] = await Promise.all([
    query(token, c.site, { ...base }),                                             // totales
    query(token, c.site, { ...base, dimensions: ["device"] }),                     // dispositivo
    query(token, c.site, { ...base, dimensions: ["searchAppearance"] }),           // Merchant / rich results
    query(token, c.site, { ...base, dimensions: ["query"], rowLimit: 25 }),        // top consultas
    query(token, c.site, { ...base, dimensions: ["page"], rowLimit: 100 }),        // páginas (fichas + blogs)
    query(token, c.site, { ...base, dimensions: ["date"], rowLimit: 500 }),        // serie temporal
  ]);

  const t = tot[0] || { clicks: 0, impressions: 0, ctr: 0, position: 0 };
  const totals = { clicks: t.clicks, impressions: t.impressions, ctr: +(t.ctr * 100).toFixed(2), position: round1(t.position) };

  const byDevice = dev.map(r => ({
    device: r.keys[0], clicks: r.clicks, impressions: r.impressions,
    ctr: +(r.ctr * 100).toFixed(2), position: round1(r.position),
  }));
  const byAppearance = appr.map(r => ({
    appearance: r.keys[0], clicks: r.clicks, impressions: r.impressions,
    ctr: +(r.ctr * 100).toFixed(2), position: round1(r.position),
  }));

  // marca vs genérico
  let bc = 0, bi = 0, nc = 0, ni = 0;
  for (const r of queries) {
    if (BRAND.test(r.keys[0])) { bc += r.clicks; bi += r.impressions; }
    else { nc += r.clicks; ni += r.impressions; }
  }
  const brand = {
    brand: { clicks: bc, impressions: bi, ctr: pct(bc, bi) },
    nonbrand: { clicks: nc, impressions: ni, ctr: pct(nc, ni) },
  };
  const topQueries = queries.slice(0, 15).map(r => ({
    q: r.keys[0], clicks: r.clicks, impressions: r.impressions,
    ctr: +(r.ctr * 100).toFixed(2), position: round1(r.position),
  }));

  // páginas → fichas de producto vs blogs vs resto
  const cls = u => u.includes("/products/") ? "product" : u.includes("/blogs/") ? "blog"
    : u.includes("/collections/") ? "collection" : /amazingcare\.cl\/?$/.test(u) ? "home" : "page";
  const norm = u => u.split("?")[0];
  const pMap = {};
  for (const r of pages) {
    const u = norm(r.keys[0]);
    const p = pMap[u] || (pMap[u] = { url: u, kind: cls(u), clicks: 0, impressions: 0, posSum: 0 });
    p.clicks += r.clicks; p.impressions += r.impressions; p.posSum += r.position * r.impressions;
  }
  const allPages = Object.values(pMap).map(p => ({
    url: p.url, kind: p.kind, clicks: p.clicks, impressions: p.impressions,
    ctr: pct(p.clicks, p.impressions), position: round1(p.impressions ? p.posSum / p.impressions : 0),
  }));
  const topProducts = allPages.filter(p => p.kind === "product").sort((a, b) => b.clicks - a.clicks).slice(0, 8);
  const topBlogs = allPages.filter(p => p.kind === "blog").sort((a, b) => b.clicks - a.clicks).slice(0, 10);

  // serie mensual
  const mo = {};
  for (const r of byMonth) {
    const k = r.keys[0].slice(0, 7);
    const d = mo[k] || (mo[k] = { clicks: 0, impressions: 0 });
    d.clicks += r.clicks; d.impressions += r.impressions;
  }
  const monthly = Object.entries(mo).sort().map(([m, v]) => ({ month: m, clicks: v.clicks, impressions: v.impressions }));

  return { site: c.site, since, until, totals, byDevice, byAppearance, brand, topQueries, topProducts, topBlogs, monthly };
}

export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const url = new URL(request.url);
  const month = url.searchParams.get("month") || new Date().toISOString().slice(0, 7);
  const window = url.searchParams.get("window") || "";
  try { const d = await gsc(env, month, { window }); return json({ ok: !d.error, month, gsc: d }); }
  catch (e) { return json({ ok: false, month, gsc: { error: String(e.message || e) } }); }
}
