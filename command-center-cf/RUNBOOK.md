# RUNBOOK — desplegar el Command Center en tu sesión (Cloudflare Pages)

Todo lo necesario para dejarlo **en vivo** desde tu Claude Code (donde tenés Cloudflare +
los tokens). El detalle técnico y el código están en `amazing-command-center-BUILD.md`
(en esta misma carpeta). Acá va el paso a paso operativo.

---

## Antes de empezar — credenciales a tener a mano

| Necesitás | Dónde se saca | Para qué |
|---|---|---|
| Cuenta **Cloudflare** | dash.cloudflare.com | hostear (Pages) |
| **META_TOKEN** | business.facebook.com → Configuración → **Usuarios del sistema** → generar token, permiso `ads_read` (usá System User para que no expire) | Campañas + creativos |
| **META_ACCOUNT** | `2911300959169889` (Amazing Care DTC, sin `act_`) | " |
| **KLAVIYO_KEY** | Klaviyo → Settings → API Keys → **Private key** (`pk_...`) con scope de reporting | Email |
| **SHOPIFY_SHOP** + **SHOPIFY_TOKEN** | Admin de la tienda → Apps → develop apps → Admin API token (scopes `read_reports`, `read_products`, `read_orders`); `SHOPIFY_SHOP` = subdominio `*.myshopify` | Rentabilidad + productos |
| **GOOGLE_ADS_*** (6) | ver Paso 3 | Campañas Google + Merchant |

> Requisitos locales: **Node 18+** y `npx`. No hace falta instalar wrangler global (viene por npx).

---

## Paso 0 — abrir el proyecto
```bash
cd command-center-cf
npm install
```

## Paso 1 — deploy inicial (sube el front; la API queda esperando secrets)
```bash
npx wrangler login                                   # abre el navegador, autorizá
npx wrangler pages project create amazing-command-center   # si no existe
npm run deploy                                        # → https://amazing-command-center.pages.dev
```
Ya podés abrir esa URL: muestra el snapshot; la data en vivo entra al cargar los secrets.

## Paso 2 — cargar los secrets (uno por uno; se pegan, no se guardan en archivos)
```bash
npx wrangler pages secret put META_TOKEN
npx wrangler pages secret put META_ACCOUNT       # 2911300959169889
npx wrangler pages secret put KLAVIYO_KEY
npx wrangler pages secret put SHOPIFY_SHOP        # ej: 25trtw-d5
npx wrangler pages secret put SHOPIFY_TOKEN
# Google Ads (después del Paso 3):
npx wrangler pages secret put GOOGLE_ADS_DEVELOPER_TOKEN
npx wrangler pages secret put GOOGLE_ADS_CLIENT_ID
npx wrangler pages secret put GOOGLE_ADS_CLIENT_SECRET
npx wrangler pages secret put GOOGLE_ADS_REFRESH_TOKEN
npx wrangler pages secret put GOOGLE_ADS_CUSTOMER_ID        # cuenta Amazing, solo dígitos
npx wrangler pages secret put GOOGLE_ADS_LOGIN_CUSTOMER_ID  # MCC de Advanz, solo dígitos
# Search Console (SEO orgánico real — reemplaza a Ahrefs):
npx wrangler pages secret put GSC_CLIENT_ID
npx wrangler pages secret put GSC_CLIENT_SECRET
npx wrangler pages secret put GSC_REFRESH_TOKEN   # scope webmasters.readonly
npx wrangler pages secret put GSC_SITE_URL        # sc-domain:amazingcare.cl
```
> **GSC refresh token:** mismo helper, con el scope de Search Console:
> ```bash
> SCOPE=https://www.googleapis.com/auth/webmasters.readonly \
>   GOOGLE_ADS_CLIENT_ID=xxx GOOGLE_ADS_CLIENT_SECRET=yyy node get-google-refresh-token.mjs
> ```
> Si autorizás Ads + Search Console en el mismo cliente OAuth (ambos scopes, separados por
> espacio), `gsc.js` reutiliza los `GOOGLE_ADS_*` y podés saltear los `GSC_*` (salvo `GSC_SITE_URL`).
> Tras cargar/actualizar secrets, redeployá para tomarlos: `npm run deploy`.

## Paso 3 — Google Ads: obtener el `refresh_token` (una vez)
1. **Google Cloud Console** → APIs & Services → Credentials → crear **OAuth client** tipo
   *Desktop app*. Copiá `client_id` y `client_secret`.
2. **Google Ads (MCC)** → API Center → copiá el **developer token**.
3. Corré el helper que viene en esta carpeta:
   ```bash
   GOOGLE_ADS_CLIENT_ID=xxx GOOGLE_ADS_CLIENT_SECRET=yyy node get-google-refresh-token.mjs
   ```
   Abre el navegador, autorizás la cuenta de Google que tiene acceso al MCC, y la terminal
   imprime tu **refresh_token**. Ese es el `GOOGLE_ADS_REFRESH_TOKEN`.

## Paso 4 — verificar
Abrí en el navegador (reemplazá el dominio):
```
https://amazing-command-center.pages.dev/api/all?month=2026-08
https://amazing-command-center.pages.dev/api/shopify?month=2026-08
https://amazing-command-center.pages.dev/api/meta-creatives?month=2026-08
https://amazing-command-center.pages.dev/api/google?month=2026-08
https://amazing-command-center.pages.dev/api/gsc?window=365   # SEO: 12 meses (fichas Merchant + blogs + consultas)
```
Cada uno debe devolver JSON con `ok:true`. Si una fuente dice `not configured`, falta su secret.

## Paso 5 — embeber en Notion
Bloque `/embed` con la URL `*.pages.dev` (o tu dominio propio conectado en Cloudflare Pages).

---

## Troubleshooting
- **`meta not configured` / `klaviyo not configured`** → falta el secret; cargalo y `npm run deploy`.
- **Meta error "(#100) ..."** → el token no tiene `ads_read` o la cuenta no es la del token.
- **Google `PERMISSION_DENIED`** → el `login-customer-id` (MCC) no coincide con la cuenta, o falta
  el developer token / refresh token.
- **Shopify `Access denied for shopifyqlQuery`** → faltan scopes `read_reports`/`read_products` en el token.
- **Imágenes de productos/creativos no cargan** → verificá que abriste la URL `pages.dev` (no el
  archivo local): sólo hosteado cargan los CDN de Shopify/Meta.
- **CTA rápida:** para actualizar otro mes, la API acepta `?month=YYYY-MM` en todos los endpoints.

## Seguridad
- Ningún token en el repo: todos son **Secrets de Cloudflare** (`wrangler pages secret put`).
- La API es **solo lectura** (insights/reportes). No crea ni modifica campañas ni envía correos.
- `node_modules/`, `.wrangler/`, `.dev.vars` ya están en `.gitignore`.
