# Amazing Care · Command Center — Build & Deploy brief (para Claude Code)

> **Objetivo.** Un dashboard permanente por canal (Rentabilidad · Campañas · CRO · SEO/GEO ·
> Email), embebible en Notion, que trae **datos en vivo** de Meta Ads + Google Ads + Klaviyo
> (+ Shopify a futuro) y acumula histórico. Se hostea en **Cloudflare Pages** (un solo deploy):
> la página sirve en `/` y su API en `/api/*` (mismo origen → sin CORS, sin el CSP que bloquea
> a los artifacts de claude.ai).
>
> Ejecutá este brief en Claude Code donde tengas los accesos (Cloudflare, Meta, Google Ads,
> Klaviyo). La API es **solo lectura**.

---

## 0. Estado actual (qué ya está hecho)

- **Front del command center** ya construido: `amazing-command-center.html` (o `public/index.html`
  dentro de `command-center-cf.zip`). 5 tabs + Histórico, score % por canal, simulador de
  rentabilidad, y **Email/SEO con el reporte completo embebido**. Ya incluye el script de
  hidratación en vivo (§4).
- **Meta Ads**: ya validado por MCP (datos reales de agosto, §5).
- **Klaviyo**: ya validado por MCP (agosto, §5).
- **Google Ads**: NO hay MCP → lo llama la Function `google.js` con la API directa (§3, §8).
- **Ahrefs**: descartado (plan pago). SEO se arma con **Shopify (canal orgánico) + grilla de
  Search Console en Notion** (§9).

---

## 1. Arquitectura

```
Cloudflare Pages (proyecto: amazing-command-center)
├── /                 public/index.html      (dashboard; fetch a /api/all al abrir)
├── /api/all          functions/api/all.js   (Meta + Google + Klaviyo agregados)
├── /api/meta         functions/api/meta.js
├── /api/google       functions/api/google.js
├── /api/klaviyo      functions/api/klaviyo.js
└── /api/_middleware  functions/api/_middleware.js  (CORS + key opcional + helper json())
```

Por qué Cloudflare y no un artifact: el sandbox de los artifacts de claude.ai **bloquea todo
`fetch` a orígenes externos**. Sirviendo dashboard + API desde el mismo Pages, el fetch es
mismo-origen y no hay CORS ni CSP. Alternativa equivalente: Vercel (mismo patrón con
`api/*.js`).

---

## 2. Estructura de archivos

```
command-center-cf/
├── public/
│   └── index.html            # el dashboard (viene en el zip; ver §4)
├── functions/
│   └── api/
│       ├── _middleware.js
│       ├── meta.js
│       ├── google.js
│       ├── klaviyo.js
│       └── all.js
├── wrangler.toml
├── package.json
└── .gitignore
```

---

## 3. Código completo de la API (Pages Functions)

### functions/api/_middleware.js
```js
// CORS + gate opcional por key para /api/*. Same-origin no necesita key.
export async function onRequest(context) {
  const { request, env, next } = context;
  const origin = request.headers.get("Origin") || "*";
  const cors = {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "GET,OPTIONS",
    "Access-Control-Allow-Headers": "content-type,x-cc-key",
    "Access-Control-Max-Age": "86400",
  };
  if (request.method === "OPTIONS") return new Response(null, { headers: cors });
  if (env.CC_API_KEY) {
    const key = request.headers.get("x-cc-key") || new URL(request.url).searchParams.get("key");
    if (key !== env.CC_API_KEY) return json({ ok: false, error: "unauthorized" }, 401, cors);
  }
  const res = await next();
  const out = new Response(res.body, res);
  for (const [k, v] of Object.entries(cors)) out.headers.set(k, v);
  return out;
}
export function json(obj, status = 200, extra = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...extra },
  });
}
```

### functions/api/meta.js
```js
// Meta Ads — insights a nivel cuenta para un mes. Secrets: META_TOKEN, META_ACCOUNT, FX_CLP_PER_USD.
const GRAPH = "https://graph.facebook.com/v21.0";
function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  const since = `${y}-${String(mo).padStart(2, "0")}-01`;
  const until = new Date(y, mo, 0).toISOString().slice(0, 10);
  return { since, until };
}
export async function metaInsights(env, account, month) {
  if (!env.META_TOKEN || !account) return { error: "meta not configured" };
  const { since, until } = monthRange(month);
  const fields = "spend,purchase_roas,actions,impressions,reach,ctr,cpm,inline_link_clicks";
  const url = `${GRAPH}/act_${account}/insights?level=account&fields=${fields}` +
    `&time_range=${encodeURIComponent(JSON.stringify({ since, until }))}&access_token=${env.META_TOKEN}`;
  const r = await fetch(url); const j = await r.json();
  if (j.error) return { error: j.error.message };
  const row = (j.data && j.data[0]) || {};
  const fx = Number(env.FX_CLP_PER_USD || 950);
  const spend = Number(row.spend || 0);
  const roas = Number((row.purchase_roas || []).find(x => x.action_type === "omni_purchase")?.value ||
    (row.purchase_roas || [])[0]?.value || 0);
  const purchases = Number((row.actions || []).find(x => x.action_type === "omni_purchase")?.value || 0);
  return {
    account, currency: "USD", fx,
    spend_usd: spend, spend_clp: Math.round(spend * fx), roas, purchases,
    cpa_usd: purchases ? +(spend / purchases).toFixed(2) : null,
    sales_clp: Math.round(spend * roas * fx),
    impressions: Number(row.impressions || 0), reach: Number(row.reach || 0),
    ctr: row.ctr ? +Number(row.ctr).toFixed(2) : null,
    cpm_usd: row.cpm ? +Number(row.cpm).toFixed(2) : null,
    link_clicks: Number(row.inline_link_clicks || 0),
  };
}
export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const p = new URL(request.url).searchParams;
  const month = p.get("month") || new Date().toISOString().slice(0, 7);
  const acc = p.get("account") || env.META_ACCOUNT;
  const data = await metaInsights(env, acc, month);
  return json({ ok: !data.error, month, meta: data });
}
```

### functions/api/klaviyo.js
```js
// Klaviyo — campañas + flujos (email) de un mes. Secrets: KLAVIYO_KEY, KLAVIYO_CONV_METRIC(=RP5iQ9).
const BASE = "https://a.klaviyo.com/api";
const REV = "2024-10-15";
function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  return { start: new Date(Date.UTC(y, mo - 1, 1)).toISOString(), end: new Date(Date.UTC(y, mo, 1)).toISOString() };
}
async function report(kind, env, month) {
  const { start, end } = monthRange(month);
  const body = { data: { type: `${kind}-values-report`, attributes: {
    statistics: ["recipients", "conversions"], timeframe: { start, end },
    conversion_metric_id: env.KLAVIYO_CONV_METRIC || "RP5iQ9",
    filter: `equals(send_channel,"email")` } } };
  const r = await fetch(`${BASE}/${kind}-values-reports/`, { method: "POST", headers: {
    Authorization: `Klaviyo-API-Key ${env.KLAVIYO_KEY}`, "content-type": "application/json",
    accept: "application/json", revision: REV }, body: JSON.stringify(body) });
  const j = await r.json();
  if (j.errors) return { error: j.errors[0]?.detail || "klaviyo error" };
  const results = j?.data?.attributes?.results || [];
  let rev = 0, conv = 0;
  for (const row of results) {
    const tag = (row.groupings && row.groupings.flow_name) || "";
    if (/NUTRI|NO USAR|Nutrikit/i.test(tag)) continue;       // excluir circuito de códigos
    rev += Number(row.statistics?.conversion_value || 0);
    conv += Number(row.statistics?.conversions || 0);
  }
  return { revenue_clp: Math.round(rev), conversions: conv };
}
export async function klaviyo(env, month) {
  if (!env.KLAVIYO_KEY) return { error: "klaviyo not configured" };
  const [camp, flow] = await Promise.all([report("campaign", env, month), report("flow", env, month)]);
  if (camp.error) return camp; if (flow.error) return flow;
  const total = camp.revenue_clp + flow.revenue_clp;
  return { campaigns_clp: camp.revenue_clp, flows_clp: flow.revenue_clp, total_clp: total,
    flow_share: total ? +(flow.revenue_clp / total).toFixed(3) : 0 };
}
export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  const d = await klaviyo(env, month);
  return json({ ok: !d.error, month, klaviyo: d });
}
```

### functions/api/google.js
```js
// Google Ads — spend/conversions/value a nivel cuenta para un mes (sin MCP).
// Secrets: GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
//          GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID, GOOGLE_ADS_LOGIN_CUSTOMER_ID,
//          GOOGLE_ADS_CURRENCY(CLP|USD), FX_CLP_PER_USD.
const API = "https://googleads.googleapis.com/v17";
function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  return { since: `${y}-${String(mo).padStart(2, "0")}-01`, until: new Date(y, mo, 0).toISOString().slice(0, 10) };
}
async function accessToken(env) {
  const r = await fetch("https://oauth2.googleapis.com/token", { method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ client_id: env.GOOGLE_ADS_CLIENT_ID, client_secret: env.GOOGLE_ADS_CLIENT_SECRET,
      refresh_token: env.GOOGLE_ADS_REFRESH_TOKEN, grant_type: "refresh_token" }) });
  const j = await r.json(); if (!j.access_token) throw new Error(j.error_description || "oauth failed");
  return j.access_token;
}
export async function googleAds(env, month) {
  if (!env.GOOGLE_ADS_REFRESH_TOKEN || !env.GOOGLE_ADS_CUSTOMER_ID) return { error: "google ads not configured" };
  const { since, until } = monthRange(month);
  const cid = env.GOOGLE_ADS_CUSTOMER_ID.replace(/-/g, "");
  const token = await accessToken(env);
  const query = `SELECT metrics.cost_micros, metrics.conversions, metrics.conversions_value, ` +
    `metrics.impressions, metrics.clicks FROM customer WHERE segments.date BETWEEN '${since}' AND '${until}'`;
  const r = await fetch(`${API}/customers/${cid}/googleAds:searchStream`, { method: "POST", headers: {
    Authorization: `Bearer ${token}`, "developer-token": env.GOOGLE_ADS_DEVELOPER_TOKEN,
    "login-customer-id": (env.GOOGLE_ADS_LOGIN_CUSTOMER_ID || cid).replace(/-/g, ""),
    "content-type": "application/json" }, body: JSON.stringify({ query }) });
  const j = await r.json();
  if (j.error || (Array.isArray(j) && j[0]?.error)) return { error: (j.error || j[0].error)?.message || "google ads error" };
  let costMicros = 0, conv = 0, value = 0, impr = 0, clicks = 0;
  for (const c of (Array.isArray(j) ? j : [j])) for (const row of (c.results || [])) {
    costMicros += Number(row.metrics?.costMicros || 0); conv += Number(row.metrics?.conversions || 0);
    value += Number(row.metrics?.conversionsValue || 0); impr += Number(row.metrics?.impressions || 0);
    clicks += Number(row.metrics?.clicks || 0);
  }
  const fx = Number(env.FX_CLP_PER_USD || 950);
  const usd = String(env.GOOGLE_ADS_CURRENCY || "CLP").toUpperCase() === "USD";
  const cost = costMicros / 1e6, toClp = n => Math.round(usd ? n * fx : n);
  return { spend_clp: toClp(cost), conversions: +conv.toFixed(1), sales_clp: toClp(value),
    roas: cost ? +(value / cost).toFixed(2) : null, impressions: impr, clicks };
}
export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  try { const d = await googleAds(env, month); return json({ ok: !d.error, month, google: d }); }
  catch (e) { return json({ ok: false, month, google: { error: String(e.message || e) } }); }
}
```

### functions/api/all.js
```js
import { metaInsights } from "./meta.js";
import { googleAds } from "./google.js";
import { klaviyo } from "./klaviyo.js";
export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  const [meta, google, kl] = await Promise.allSettled([
    metaInsights(env, env.META_ACCOUNT, month),
    googleAds(env, month).catch(e => ({ error: String(e.message || e) })),
    klaviyo(env, month),
  ]);
  const val = r => (r.status === "fulfilled" ? r.value : { error: String(r.reason) });
  const m = val(meta), g = val(google), k = val(kl);
  const paidSpend = (m.spend_clp || 0) + (g.spend_clp || 0);
  const paidSales = (m.sales_clp || 0) + (g.sales_clp || 0);
  return json({ ok: true, month, generated_at: new Date().toISOString(),
    meta: m, google: g, klaviyo: k,
    paid: { spend_clp: paidSpend || null, sales_clp: paidSales || null,
      roas_blended: paidSpend ? +(paidSales / paidSpend).toFixed(2) : null } });
}
```

### wrangler.toml
```toml
name = "amazing-command-center"
pages_build_output_dir = "public"
compatibility_date = "2024-11-01"
[vars]
FX_CLP_PER_USD = "950"
GOOGLE_ADS_CURRENCY = "CLP"
```

### package.json
```json
{
  "name": "amazing-command-center",
  "private": true,
  "scripts": {
    "dev": "wrangler pages dev public",
    "deploy": "wrangler pages deploy public --project-name amazing-command-center"
  },
  "devDependencies": { "wrangler": "^3.80.0" }
}
```

### .gitignore
```
node_modules/
.wrangler/
.dev.vars
*.log
```

---

## 4. El front (public/index.html)

El dashboard ya está construido y es grande (~150 KB con los reportes de Email y SEO
embebidos). **Usá el `public/index.html` que viene en `command-center-cf.zip`** (o el
`amazing-command-center.html` enviado). Ya trae inyectado el script de hidratación:

```html
<script>
/* LIVE HYDRATION — pisa el snapshot con Meta+Google+Klaviyo reales; si no hay API, deja el snapshot */
(function(){
 var BASE=(window.CC_API||'');
 var clp=function(n){return '$'+(Math.round(n/1e6*10)/10)+'M';};
 var nf=function(n){return Number(n).toLocaleString('es-CL');};
 async function hydrate(){
  try{
   var r=await fetch(BASE+'/api/all?month='+encodeURIComponent(CC.current)); if(!r.ok)return;
   var d=await r.json(); if(!d||!d.ok)return; var md=CC.data[CC.current]; if(!md)return;
   if(d.meta&&!d.meta.error){var m=d.meta; md.campanas.kpis=[
     {l:'Inversión (Meta)',v:clp(m.spend_clp),s:'US$'+nf(Math.round(m.spend_usd))+' · en vivo',d:'nt'},
     {l:'Purchase ROAS',v:(m.roas||0).toFixed(2)+'x',s:'sobre breakeven',d:'up'},
     {l:'Compras',v:nf(m.purchases),s:'costo US$'+(m.cpa_usd||'—'),d:'nt'},
     {l:'Alcance',v:nf(m.reach),s:nf(m.impressions)+' impresiones',d:'nt'},
     {l:'CTR',v:(m.ctr||'—')+'%',s:'CPM US$'+(m.cpm_usd||'—'),d:'nt'},
     {l:'Ventas (in-platform)',v:clp(m.sales_clp),s:'ROAS × inversión',d:'up'}];}
   if(d.google&&!d.google.error){md.campanas.google=false;
     md.campanas.kpis.push({l:'Google Ads',v:clp(d.google.spend_clp),s:'ROAS '+(d.google.roas||'—')+'x · en vivo',d:'up'});}
   if(d.klaviyo&&!d.klaviyo.error){var k=d.klaviyo;
     md.email.kpis[0]={l:'Ventas atribuidas',v:clp(k.total_clp),s:'Klaviyo en vivo',d:'up'};
     md.email.kpis[1]={l:'Campañas',v:clp(k.campaigns_clp),s:'en vivo',d:'nt'};
     md.email.kpis[2]={l:'Flujos',v:clp(k.flows_clp),s:((k.flow_share||0)*100).toFixed(0)+'% del canal',d:'up'};}
   if(d.paid&&d.paid.roas_blended){var rk=md.resumen.kpis;
     rk[rk.length-1]={l:'MER paid (Meta+Google)',v:d.paid.roas_blended.toFixed(2)+'x',s:'en vivo',d:'up'};}
   var up=document.querySelector('.perlab'); if(up) up.innerHTML='Cierre <b>'+CC.mlabel[CC.current]+' 2026</b> · datos en vivo';
   if(typeof render==='function') render();
  }catch(e){}
 }
 hydrate();
})();
</script>
```

> El dashboard pinta desde un objeto `CC_DATA` (snapshot) y esta función lo **hidrata** con lo
> real. Si necesitás regenerar el front desde cero, el schema de `CC_DATA` está en el HTML
> (comentado): `months[]`, `mlabel`, `trends`, `scores{canal:{s,dims,fix}}`, `coverage`,
> `sessions[]` (histórico), `data[YYYY-MM]{resumen,campanas,cro,seo,email}`.

---

## 5. Snapshot de datos reales (validados por MCP) — para el fallback

### Meta Ads — agosto 2026 · cuenta DTC `2911300959169889` (USD, FX≈950)
| Métrica | Valor |
|---|---|
| Inversión | US$2.790,49 (≈ $2,65M CLP) |
| Purchase ROAS | 3,40x |
| Compras | 212 · costo US$13,16 |
| Impresiones / Alcance | 1.126.529 / 287.285 |
| CTR / CPM | 1,11% / US$2,48 |
| Link clicks | 8.482 |
| Ventas in-platform | ≈ $9,0M CLP (ROAS × inversión) |

### Klaviyo — agosto 2026 (email)
- **Campañas** (10 envíos, 57.711 destinatarios): total ≈ **$2.832.768** (Fibra enviada 3× → 3er envío RPR $3; Fiestas Patrias 25% = $725.234; Retail Jumbo $97.521).
- **Flujos** (excluye Nutrikit tag NO USAR): **$554.113** → Welcome_AON $133.414 (RPR $270), Carritos_AON $281.661 ($1.002/contacto), Flash (draft) $139.038, Postcompra $0 (43% apertura), Recompra sin actividad.
- **Total email ≈ $3,39M**.

### Account map — Amazing Care
```
Meta Ads:  DTC 2911300959169889 (USD) · Mayorista 3131920510317594 (CLP) · Business 454429699764155
Klaviyo:   Placed Order RP5iQ9 · Viewed Form SQLn6z · Submitted Form WrC97x · Subscribed Email QYLKnd
           Flujos: Welcome_AON S8bwJx · Carritos_AON RCsVZf · Postcompra QQjgEa · Recompra_AON VNCVuB
                   Flash TXdmwz · Nutrikit SrbL9b [NO USAR]
           (la cuenta tiene métricas de WhatsApp → sirve para el módulo de recuperación)
Google Ads: cuenta de Amazing bajo el MCC de Advanz  (conseguir customer_id + login_customer_id)
Shopify:    amazingcare.cl (CLP)  — pendiente Admin API para rentabilidad
CRO (90d):  42.983 sesiones (82% móvil) · CVR 3,32% · 1.441 pedidos · ticket $33.785
SEO (ago):  1.875 sesiones orgánicas (+76%) · 78 ventas (CVR 4,16%) · 54.500 impresiones/90d
```

---

## 6. Deploy (Cloudflare Pages)

```bash
cd command-center-cf
npm install
npx wrangler login
npx wrangler pages project create amazing-command-center   # si no existe
npm run deploy                                             # → https://amazing-command-center.pages.dev
```

## 7. Secrets — `wrangler pages secret put <NOMBRE>`

| Secret | Valor / de dónde |
|---|---|
| `META_TOKEN` | System User token (business.facebook.com → Usuarios del sistema, permiso `ads_read`) |
| `META_ACCOUNT` | `2911300959169889` (DTC, sin `act_`) |
| `KLAVIYO_KEY` | Private API key `pk_...` (scope reporting) |
| `KLAVIYO_CONV_METRIC` | `RP5iQ9` (opcional; es el default) |
| `GOOGLE_ADS_DEVELOPER_TOKEN` | API Center del MCC |
| `GOOGLE_ADS_CLIENT_ID` / `GOOGLE_ADS_CLIENT_SECRET` | OAuth client (Google Cloud Console) |
| `GOOGLE_ADS_REFRESH_TOKEN` | ver §8 |
| `GOOGLE_ADS_CUSTOMER_ID` | cuenta de Amazing (solo dígitos) |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | MCC de Advanz (solo dígitos) |
| `CC_API_KEY` | opcional, sólo si exponés la API a otros orígenes |

`FX_CLP_PER_USD` y `GOOGLE_ADS_CURRENCY` ya están en `wrangler.toml`.

---

## 8. Google Ads — obtener el `refresh_token` (paso manual, 1 vez)

1. En **Google Cloud Console** → APIs & Services → Credentials → crear **OAuth client** tipo
   *Desktop app*. Guardá `client_id` y `client_secret`.
2. En **Google Ads (MCC)** → API Center → pedí/copiá el **developer token**.
3. Conseguí el refresh token (una vez), scope `https://www.googleapis.com/auth/adwords`:
   - Con el **OAuth Playground** (rueda dentada → usar tu client_id/secret → autorizar scope
     adwords → intercambiar por tokens), **o**
   - Con un script node local:
     ```bash
     npx google-ads-api-refresh-token   # o el flujo oauth2 estándar con googleapis
     ```
4. Cargá los 6 secrets `GOOGLE_ADS_*`. Probá: `GET /api/google?month=2026-08`.

---

## 9. Estado de fuentes y pendientes

| Canal | Fuente | Estado |
|---|---|---|
| Email | Klaviyo API | ✅ listo (function `klaviyo.js`) |
| Campañas Meta | Graph API | ✅ listo (`meta.js`) — falta galería de creativos (1 endpoint más) |
| Campañas Google | Google Ads API | 🟡 listo el código; falta cargar secrets (§8) |
| CRO | Shopify + Clarity | 🟡 snapshot; sumar Admin API para funnel por mes |
| SEO | **Shopify (orgánico) + grilla GSC en Notion** (NO Ahrefs) | 🟡 semi-manual |
| Rentabilidad | Shopify Admin API | ⬜ por sumar (ventas totales → MER blended real) |
| WhatsApp recovery | Klaviyo (métricas WhatsApp existen) | ⬜ por medir (hoy es simulación) |

**Próximas Functions sugeridas:** `shopify.js` (Admin GraphQL: ventas/pedidos/funnel del mes) y
`meta-creatives.js` (thumbnails + ROAS/CTR por anuncio). Mismo patrón que las de arriba.

---

## 10. Actualizar con un prompt / automatización
- En vivo: `/api/all?month=YYYY-MM` resuelve el mes pedido; el dashboard ya llama al mes actual.
- Histórico: para “cerrar” un mes, escribir su nodo en `CC_DATA` (snapshot) desde la respuesta de
  `/api/all` y redeployar. Se puede envolver en la skill `advanz-reporting` como comando
  “actualiza el command center con <mes>”.
- Cron opcional: Cloudflare Cron Trigger que pega `/api/all` y persiste el snapshot mensual.

## 11. Embeber en Notion
Bloque `/embed` con la URL `*.pages.dev` (o dominio propio). Mismo origen → carga sin trabas.

## 12. Seguridad
- Cero tokens en el repo: todos son **Secrets de Cloudflare**.
- API **solo lectura** (insights/reportes) — no crea ni modifica campañas ni envía correos.
- `.dev.vars` (local) y `node_modules/` en `.gitignore`.
- Si publicás la API a otros orígenes, activá `CC_API_KEY` y mandá `x-cc-key`.

---

*Entregables relacionados:* `command-center-cf.zip` (este proyecto con el `public/index.html` ya
armado) y `amazing-command-center.html` (el dashboard suelto). Generado por Advanz + Claude.

---

## 13. Functions extra — Shopify (rentabilidad + productos) y Creativos (Meta)

`all.js` ahora **también llama a Shopify** (para MER real + top productos). Los **creativos** van
en su propio endpoint on-demand (`/api/meta-creatives`), que el tab Campañas pide al abrirse.
El front (`public/index.html`) ya renderiza: **"🛒 Qué se vendió — top productos"** en Rentabilidad
y **"🖼️ Creativos por rendimiento"** en Campañas (galería con thumbnails).

### Secrets adicionales
| Secret | Valor / de dónde |
|---|---|
| `SHOPIFY_SHOP` | subdominio `*.myshopify` de Amazing (ej `25trtw-d5`) |
| `SHOPIFY_TOKEN` | Admin API access token (scopes `read_reports`, `read_products`, `read_orders`) |
| `SHOPIFY_API_VERSION` | opcional, default `2024-10` |

> Los creativos reutilizan `META_TOKEN` + `META_ACCOUNT` (ya cargados). Endpoints de prueba:
> `GET /api/shopify?month=2026-08` y `GET /api/meta-creatives?month=2026-08`.

### functions/api/shopify.js
```js
// Shopify — rentabilidad del mes (ventas, pedidos, ticket) + top productos vía ShopifyQL (Admin GraphQL).
function monthRange(m){const[y,mo]=m.split("-").map(Number);return{since:`${y}-${String(mo).padStart(2,"0")}-01`,until:new Date(y,mo,0).toISOString().slice(0,10)};}
async function gql(env,query){const ver=env.SHOPIFY_API_VERSION||"2024-10";
  const r=await fetch(`https://${env.SHOPIFY_SHOP}.myshopify.com/admin/api/${ver}/graphql.json`,{method:"POST",
    headers:{"X-Shopify-Access-Token":env.SHOPIFY_TOKEN,"content-type":"application/json"},body:JSON.stringify({query})});return r.json();}
function parseTable(resp){const t=resp?.data?.shopifyqlQuery?.tableData;if(!t)return{cols:[],rows:[]};
  return{cols:(t.columns||[]).map(c=>c.name),rows:t.rowData||[]};}
async function shopifyql(env,ql){const query=`{ shopifyqlQuery(query: ${JSON.stringify(ql)}) { __typename ... on TableResponse { tableData { columns { name dataType } rowData } } parseErrors { code message } } }`;
  const resp=await gql(env,query);if(resp.errors)return{error:resp.errors[0]?.message||"shopify graphql error"};
  const pe=resp?.data?.shopifyqlQuery?.parseErrors;if(pe&&pe.length)return{error:pe[0].message};return parseTable(resp);}
export async function shopify(env,month){
  if(!env.SHOPIFY_SHOP||!env.SHOPIFY_TOKEN)return{error:"shopify not configured"};
  const{since,until}=monthRange(month);
  const totals=await shopifyql(env,`FROM sales SHOW total_sales, orders, average_order_value SINCE ${since} UNTIL ${until}`);
  if(totals.error)return totals;
  const row=totals.rows[0]||[],idx=n=>totals.cols.indexOf(n),num=v=>Number(String(v??"0").replace(/[^\d.-]/g,""))||0;
  const sales=num(row[idx("total_sales")]),orders=num(row[idx("orders")]),aov=num(row[idx("average_order_value")]);
  const prod=await shopifyql(env,`FROM sales SHOW total_sales, net_items_sold GROUP BY product_title SINCE ${since} UNTIL ${until} ORDER BY total_sales DESC LIMIT 8`);
  let products=[];
  if(!prod.error){const ti=prod.cols.indexOf("product_title"),si=prod.cols.indexOf("total_sales"),ui=prod.cols.indexOf("net_items_sold");
    products=prod.rows.map(r=>({title:String(r[ti]),sales_clp:num(r[si]),units:num(r[ui])}));}
  try{const img=await gql(env,`{ products(first: 60, sortKey: BEST_SELLING) { edges { node { title featuredImage { url } } } } }`);
    const map={};for(const e of (img?.data?.products?.edges||[]))map[e.node.title]=e.node.featuredImage?.url||null;
    products=products.map(p=>({...p,image:map[p.title]||null}));}catch(e){}
  return{sales_clp:Math.round(sales),orders,aov_clp:Math.round(aov),products};
}
export async function onRequestGet({request,env}){const{json}=await import("./_middleware.js");
  const month=new URL(request.url).searchParams.get("month")||new Date().toISOString().slice(0,7);
  const d=await shopify(env,month);return json({ok:!d.error,month,shopify:d});}
```

### functions/api/meta-creatives.js  (ruta `/api/meta-creatives`)
```js
// Meta — galería de creativos por rendimiento del mes (thumbnail + ROAS/CTR/gasto por anuncio).
const GRAPH="https://graph.facebook.com/v21.0";
function monthRange(m){const[y,mo]=m.split("-").map(Number);return{since:`${y}-${String(mo).padStart(2,"0")}-01`,until:new Date(y,mo,0).toISOString().slice(0,10)};}
export async function creatives(env,account,month,limit=9){
  if(!env.META_TOKEN||!account)return{error:"meta not configured"};
  const{since,until}=monthRange(month);
  const fields=`name,effective_status,creative{thumbnail_url,image_url},insights.time_range(${JSON.stringify({since,until})}){spend,purchase_roas,ctr,impressions,actions}`;
  const url=`${GRAPH}/act_${account}/ads?fields=${encodeURIComponent(fields)}&limit=200&access_token=${env.META_TOKEN}`;
  const r=await fetch(url),j=await r.json();if(j.error)return{error:j.error.message};
  const fx=Number(env.FX_CLP_PER_USD||950),rows=[];
  for(const ad of (j.data||[])){const ins=ad.insights?.data?.[0];if(!ins)continue;
    const spend=Number(ins.spend||0);if(spend<=0)continue;
    const roas=Number((ins.purchase_roas||[]).find(x=>x.action_type==="omni_purchase")?.value||(ins.purchase_roas||[])[0]?.value||0);
    const purchases=Number((ins.actions||[]).find(x=>x.action_type==="omni_purchase")?.value||0);
    rows.push({name:ad.name,thumb:ad.creative?.image_url||ad.creative?.thumbnail_url||null,
      spend_usd:+spend.toFixed(0),spend_clp:Math.round(spend*fx),roas:roas?+roas.toFixed(2):null,
      ctr:ins.ctr?+Number(ins.ctr).toFixed(2):null,purchases});}
  rows.sort((a,b)=>b.spend_usd-a.spend_usd);return{creatives:rows.slice(0,limit)};
}
export async function onRequestGet({request,env}){const{json}=await import("./_middleware.js");
  const p=new URL(request.url).searchParams,month=p.get("month")||new Date().toISOString().slice(0,7);
  const d=await creatives(env,p.get("account")||env.META_ACCOUNT,month);
  return json({ok:!d.error,month,creatives:d.creatives||[],error:d.error});}
```

### all.js — actualizado (ahora incluye Shopify + MER real)
> Reemplazá el `all.js` de §3 por: importa `shopify` de `./shopify.js`, lo agrega al
> `Promise.allSettled`, devuelve `shopify` en el JSON, y calcula `paid.mer_real =
> shopify.sales_clp / (meta+google spend)`. (Ya viene así en `command-center-cf.zip`.)
