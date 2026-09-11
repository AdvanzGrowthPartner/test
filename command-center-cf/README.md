# Amazing Care · Command Center — Cloudflare (datos en vivo)

Un solo deploy en **Cloudflare Pages** que sirve el dashboard **y** su API. La API
(Pages Functions) llama a **Meta Ads, Google Ads y Klaviyo** directo — sin depender
de ningún MCP — y el dashboard se auto-actualiza al abrirlo. Embebible en Notion.

```
/            → public/index.html   (el command center; hace fetch a /api/all)
/api/all     → Meta + Google + Klaviyo agregados (mismo origen: sin CORS, sin CSP)
/api/meta    /api/google    /api/klaviyo   (endpoints individuales para debug)
```

Los tokens viven como **Secrets de Cloudflare**, nunca en el código ni en el repo.

---

## 1) Deploy (una vez)

```bash
npm install
npx wrangler login                      # abre el navegador, autoriza tu cuenta Cloudflare
npx wrangler pages project create amazing-command-center   # si no existe aún
npm run deploy                          # sube public/ + functions/
```
Te queda una URL tipo `https://amazing-command-center.pages.dev`.

## 2) Secrets (una vez) — `wrangler pages secret put <NOMBRE>`

**Meta Ads** (ya lo usamos por MCP; para el Worker necesitás un token propio):
```bash
npx wrangler pages secret put META_TOKEN     # System User token de Meta Business (largo)
npx wrangler pages secret put META_ACCOUNT   # 2911300959169889  (Amazing Care DTC, sin act_)
```
> El token se genera en **business.facebook.com → Configuración → Usuarios del sistema →
> generar token** con permisos `ads_read`. Usá un System User para que no expire.

**Klaviyo**:
```bash
npx wrangler pages secret put KLAVIYO_KEY          # Private API key (pk_...) con scope de reporting
# opcional: KLAVIYO_CONV_METRIC  (default RP5iQ9 = Placed Order de Amazing)
```

**Google Ads** (esto reemplaza al MCP que no existe):
```bash
npx wrangler pages secret put GOOGLE_ADS_DEVELOPER_TOKEN
npx wrangler pages secret put GOOGLE_ADS_CLIENT_ID
npx wrangler pages secret put GOOGLE_ADS_CLIENT_SECRET
npx wrangler pages secret put GOOGLE_ADS_REFRESH_TOKEN
npx wrangler pages secret put GOOGLE_ADS_CUSTOMER_ID        # la cuenta de Amazing (solo dígitos)
npx wrangler pages secret put GOOGLE_ADS_LOGIN_CUSTOMER_ID  # el MCC de Advanz (solo dígitos)
```
> El **developer token** se pide en la cuenta MCC (API Center). El **refresh token** se
> obtiene una vez con el OAuth Playground o un script (client_id/secret + scope
> `https://www.googleapis.com/auth/adwords`). Es el único paso manual de Google.

Variables no-secretas (`FX_CLP_PER_USD`, `GOOGLE_ADS_CURRENCY`) ya están en `wrangler.toml`.

## 3) Redeploy tras cambios
```bash
npm run deploy
```

---

## Cómo se ve en vivo
- Abrí la URL: el dashboard carga el snapshot embebido y **en ~1s lo reemplaza** con lo
  que devuelve `/api/all` (Meta ROAS real, Google si está configurado, Klaviyo campañas/flujos).
- Si una fuente no está configurada, esa parte queda con el snapshot y el resto sí va en vivo.
- **Embeber en Notion**: `/embed` con la URL `pages.dev` (o tu dominio propio).

## Actualizar el histórico
`/api/all?month=2026-09` trae septiembre. El botón/skill de "actualizar" puede escribir
el nodo del mes en el snapshot y redeployar, o simplemente dejar que el fetch en vivo
resuelva el mes actual.

## Seguridad
- Ningún token en el repo: todos son Secrets de Cloudflare.
- Opcional: `wrangler pages secret put CC_API_KEY` para exigir `?key=` en `/api/*` si vas
  a llamar la API desde otros orígenes. Para el dashboard mismo-origen no hace falta.
- La API es **solo lectura** (insights/reportes). No modifica campañas ni envía nada.

## Estado de fuentes
| Fuente | Endpoint | Qué necesita |
|---|---|---|
| Meta Ads | `/api/meta` | `META_TOKEN`, `META_ACCOUNT` |
| Klaviyo | `/api/klaviyo` | `KLAVIYO_KEY` |
| Google Ads | `/api/google` | los 6 secrets `GOOGLE_ADS_*` |
| Shopify (rentabilidad + top productos) | `/api/shopify` | `SHOPIFY_SHOP`, `SHOPIFY_TOKEN` (scopes read_reports/read_products) |
| Creativos Meta (galería) | `/api/meta-creatives` | reusa `META_TOKEN` + `META_ACCOUNT` |
| Search Console (SEO: consultas, fichas Merchant, blogs) | `/api/gsc` | `GSC_REFRESH_TOKEN`, `GSC_SITE_URL` (scope `webmasters.readonly`) |
