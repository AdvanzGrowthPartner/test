# Detection Patterns — Cómo detectar apps por CATEGORÍA, no por marca

Esta referencia define **patrones genéricos de detección por categoría funcional**. El catálogo vivo de apps específicas (URLs, precios, replicabilidad) está en Notion `Shopify Tools Library` (`13ce4773-1586-4c99-8bec-ebae6dd77bff`).

**Por qué este enfoque**: las apps cambian de nombre, vendor o desaparecen. Los patrones de detección por capa funcional son estables.

---

## 6 capas de detección (orden de ejecución)

### Layer 1 — App blocks embebidos en el theme
Más confiable. Buscar:
```bash
grep -oE 'shopify://apps/[a-z0-9\-]+' home.html | sort -u
```
Esto devuelve el slug oficial del app embed. Si aparece `shopify://apps/recharge-subscriptions` la confianza es 100%.

**Limitación**: solo detecta apps con app embed activado. Apps que solo cargan JS via script tag no aparecen acá.

### Layer 2 — Selling plan groups (subscription engine)
Endpoint: `/products/<handle>.js` campo `selling_plan_groups`.

| app_id en selling plan | Engine |
|---|---|
| `294517` | Recharge |
| `SKIO` (string) | Skio |
| numérico ≠ 294517 | Smartrr / Loop / app custom |
| Vacío pero `requires_selling_plan:false` | Native Shopify Subscriptions o no usado |
| Array vacío `[]` | Sin suscripciones |

### Layer 3 — Dominios externos (CDN signatures)
Catálogo de dominios estable por categoría (no por app):

| Categoría | Dominios típicos a buscar |
|---|---|
| Reviews | `.judge.me`, `loox.io/widget`, `okendo.io`, `yotpo.com`, `stamped.io`, `reviews.io`, `junip.co` |
| Subscriptions | `rechargecdn.com`, `rechargeapps.com`, `cdn.skio.com`, `smartrr.com` |
| Email | `klaviyo.com`, `mailmunch`, `omnisend.com`, `mailerlite.com` |
| SMS | `attn.tv` (Attentive), `postscript.io`, `klaviyo.com/sms`, `manychat.com` |
| Upsell/Bundles | `rebuyengine.com`, `aftersell.app`, `reconvert.io`, `upcart` paths |
| Page builder | `pagefly.io`, `gempages.net`, `replo.app`, `shogun.com` |
| Loyalty | `loyaltylion.net`, `smile.io`, `yotpo.com/loyalty`, `referralcandy.com` |
| Analytics | `clarity.ms`, `static.hotjar.com`, `triplewhale.com`, `northbeam.io` |
| GDPR | `consentmo.com`, `enzuzo.com`, `cookiebot.com`, `iubenda.com` |
| Chat | `gorgias.io`, `tidio.co`, `reamaze.com`, `crisp.chat`, `zendesk.com` |
| Attribution | `getelevar.com`, `littledata.io`, `segment.com` |
| Affiliate | `goaffpro.com`, `impact.com`, `uppromote.com`, `refersion.com` |
| Video commerce | `videowise.com`, `tolstoy.app`, `firework.com` |
| Search | `boost-pfs`, `searchanise.io`, `klevu.com`, `algolia.com` |

```bash
grep -oE 'https://[a-zA-Z0-9.-]+\.[a-z]+' home.html \
  | sed -E 's|^https://||' \
  | sort -u \
  | grep -vE "^(www\.)?(shopify|shopifycdn|cdn\.shopify|facebook|google|youtube|fonts|instagram)" 
```

### Layer 4 — JS object/global signatures
Variables window-scope que las apps inyectan:

| Variable global | App engine |
|---|---|
| `window._learnq` | Klaviyo |
| `window.SmileUI` o `smile-ui` | Smile.io |
| `window.LoyaltyLion` | LoyaltyLion |
| `window.easybundles_ext_data` | easyBundles |
| `window.Rebuy` | Rebuy |
| `window.Recharge` | Recharge |
| `window.Skio` | Skio |
| `window.dataLayer` con eventos `dl_*` | Elevar |
| `attentive` o `__attentive` | Attentive |
| `fbq` | Meta Pixel |
| `ttq` | TikTok Pixel |
| `clarity` función | Microsoft Clarity |
| `hj` o `window.hj` | Hotjar |
| `gtag` | GA4/GTM |
| `pintrk` | Pinterest Pixel |
| `snaptr` | Snapchat Pixel |
| `rdt` | Reddit Pixel |
| `analytics.track` con `Segment` | Segment CDP |

```bash
grep -oE 'window\.[A-Z][a-zA-Z]+|(\bfbq\b|\bttq\b|\b_learnq\b|\brdt\b|\bsnaptr\b|\bpintrk\b)' home.html | sort -u
```

### Layer 5 — Custom elements del theme (apps reemplazadas por Liquid)
Custom HTML elements con guión indican que el theme implementó la feature nativamente en lugar de instalar app:

```bash
grep -oE '<[a-z\-]+-[a-z\-]+' home.html | sort -u
```

Patrones típicos y la app que reemplazan:

| Custom element pattern | App que reemplaza |
|---|---|
| `<ticker-bar>`, `<announcement-bar>` | Hextom announcement (~$10/mo) |
| `<flavor-swatch>`, `<*-swatch>` | Globo Product Options (~$15/mo) |
| `<quick-add-product>`, `<quick-view>` | Quick View apps |
| `<ugc-carousel>`, `<*-carousel>` | Foursixty (~$50/mo) |
| `<cart-drawer>`, `<cart-popup>` | UpCart / Slide Cart apps |
| `<sticky-add>`, `<sticky-atc>` | Sticky ATC apps |

**Implicancia diagnóstica**: si una tienda tiene MUCHOS custom elements y POCOS app blocks, está reemplazando apps con Liquid nativo → stack barato y mantenible.

### Layer 6 — Active shadow buyer (validación de configuración real)
No basta con detectar el app instalado. Hay que validar si está **activamente generando conversión**:

```bash
# Add to cart
curl -X POST "$SHOP/cart/add.js" -d "{\"id\":VARIANT,\"quantity\":1}"

# Cart state
curl "$SHOP/cart.js"
# Check: data.attributes (residue de apps), data.items[].properties

# Checkout redirect
curl -I "$SHOP/checkout"
# Follow location → ver métodos de pago, BNPL, accelerated checkout

# Selling plans
curl "$SHOP/products/<handle>.js" | jq .selling_plan_groups
```

Información valiosa del shadow buyer:
- Cart attributes inyectados → confirma qué apps están activas
- Item properties → confirma upsells/bundles activos
- Payment methods en checkout → revela stack pagos (LATAM-specific, BNPL)
- Selling plans con plans listados → suscripciones realmente vendidas
- Discounts auto-aplicados → motor de descuentos activo

---

## False positives frecuentes — siempre verificar contexto

Algunos términos aparecen en HTML sin que la app esté instalada. Antes de declarar detección, verificar **contexto** con grep de ±30 chars:

```bash
grep -oE '.{30}APPNAME.{30}' home.html | head -3
```

Casos típicos de false positives:

- **Okendo, Yotpo, Loox menciones cruzadas**: aparecen en código de migración cuando la tienda cambió de vendor. Si hay `okendoProductReview*` JS pero NO hay `okendo.io` en dominios externos → probable false positive.
- **Recharge legacy**: una tienda migrada de Recharge a Skio puede dejar URLs `rechargecdn.com` aunque el engine activo sea Skio. Validar con selling_plan_groups → `app_id=SKIO` confirma migración.
- **Selling plans presente, pero `requires_selling_plan:false`**: la suscripción está instalada en backend pero NO ofrecida en PDP. No cuenta como "en uso".
- **Judge.me con `data-number-of-reviews='0'`**: instalado pero no usado. Reportar como "instalado, sin uso".

---

## Cómo agregar una app nueva al catálogo

**No editar este archivo**. El catálogo vivo de apps está en Notion (`Shopify Tools Library`). Cuando detectes una app no listada acá:

1. Identificá la **categoría funcional** (Reviews, Subs, Bundles, etc.)
2. Identificá los **3 signatures más fuertes**: HTML pattern, dominio externo, variable global
3. Agregalos a la tabla de la categoría correspondiente en este archivo (solo si el patrón es genérico y replicable)
4. Crear entrada en Notion con detalle de la app específica, costo, URL App Store, tienda donde fue detectada

Si el patrón de detección es **único de la app** (ej. dominio `cdn.skio.com` solo Skio lo usa), va a Notion. Si el patrón es **genérico de la categoría** (ej. todas las apps de Reviews terminan en `.io/widget/` o tienen JSON-LD AggregateRating), va acá.
