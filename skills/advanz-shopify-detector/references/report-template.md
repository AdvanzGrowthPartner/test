# Report Template

This is the structure for every analysis output. Don't deviate without reason.

Use `##` headers (not `#`) since the report sits inside a chat reply with the chat title already at `#` level.

---

## 🎯 [Nombre del comercio] — Análisis Stack Shopify

**URL analizada**: `[full URL]`
**Fecha**: [today]
**Modo**: [Pasivo / Shadow buyer activo]
**Vertical**: [supplements / fashion / wellness / food / etc — inferred]
**Estimación de tamaño**: [solo si hay señales claras: tráfico estimado, # SKUs, # reviews]

---

## 🏗️ Stack base

| Capa | Detección | Confianza | Costo | Replicabilidad Advanz |
|---|---|---|---|---|
| Plataforma | Shopify (shop_id `[id]`) | 🟢 | base $39+/mo | N/A |
| Theme | [Nombre] ([Vendor]) | 🟢/🟡 | [precio] | [veredicto] |
| Personalización | [Vanilla / Moderate / Heavy] | — | — | — |

**Señales clave del theme**: [lista corta de 3-5 señales: footer attribution, class signatures, etc]

---

## 🧩 Apps detectadas

Una tabla por categoría. Solo incluir categorías con detecciones reales.

### Conversión (PDP, bundles, upsell, urgencia)

| App | Señal de detección | Confianza | Costo mensual | Funnel impact | Replicabilidad | Verdict |
|---|---|---|---|---|---|---|
| [App name] | [unique signal] | 🟢/🟡/🔴 | $X-Y | [stage] | [path] | [✅ copiar / ⚠️ evaluar / ❌ no copiar] |

### Marketing & captura (email, SMS, pop-ups, pixels)

[Same table structure]

### Operación (suscripciones, pagos, envíos, inventario)

[Same table structure]

### Theme/Customización (secciones custom, metafields, page builders)

[Same table structure]

### Soporte & comunicación (chat, WhatsApp, helpdesk)

[Same table structure]

---

## 🛒 Shadow buyer walkthrough

*(only include this section if mode was "activo")*

### Home (`/`)
- Tiempo aproximado de carga: [si se midió]
- Pop-ups que dispararon: [exit-intent? newsletter? quiz?]
- Hero pattern: [video / static / carrusel / split]
- Trust signals visibles: [reviews badge, certifications, payment logos]
- Notas relevantes: [...]

### Colección/categoría
- Filtros: [native / Boost / Searchanise]
- Sort options: [defaults / custom]
- Producto card pattern: [imagen + nombre + precio / + swatches / + quick-add]
- Quick-view: [sí/no]

### PDP
- Layout: [hero a la izquierda + info derecha / split / stack]
- Variant picker: [dropdown / botones / swatches con imágenes]
- Bundle/quantity selector: [presente, app detectada, o theme native]
- Reviews: [arriba del fold / debajo / pestaña]
- Sticky CTA: [sí/no, app o theme]
- Trust block: [íconos, certificaciones, garantías]
- Cross-sell / "frecuentemente comprado junto": [presente, app, posición]
- Schema JSON-LD: [Product / Review / FAQ / BreadcrumbList — lista lo encontrado]

### Carrito (después de add-to-cart real)
- Tipo: [drawer / página completa / mini-modal]
- Free shipping bar: [sí, app o native, threshold]
- Upsells en cart: [sí/no, qué se ofreció]
- Gift with purchase: [sí/no]
- Notas/instrucciones: [campo abierto presente?]
- Cart attributes detectados: [lista de claves no-default en /cart.js]

### Checkout (sin completar pago)
- Custom branding: [logo, colores, fonts custom]
- Métodos de pago: [Shop Pay, Mercado Pago, Fintoc, Webpay, Klarna, etc]
- Express checkout: [Shop Pay accelerated, Google Pay, Apple Pay]
- Custom fields: [RUT? mensaje? regalo?]
- Order bump pre-payment: [sí/no — algunos apps inyectan]

### Post-purchase indicadores
- *(no podemos completar compra, pero detectamos capacidad)*
- ReConvert / AfterSell instalados: [sí/no según signals]
- Klaviyo / Postscript capacidad email/SMS abandoned cart: [sí/no]

---

## 🎯 Funnel mapping (Growth Engine stages)

Mapea cada app encontrada a su etapa del Growth Engine:

| Stage | Apps que cubren esta etapa en [tienda] | Gap detectado |
|---|---|---|
| **Foundations** (theme, schema, pixels) | [...] | [...] |
| **Offer** (bundles, pricing tiers, GWP) | [...] | [...] |
| **Validation** (reviews, UGC, social proof) | [...] | [...] |
| **Acquisition** (pixels, attribution, ads infra) | [...] | [...] |
| **Workflows** (email, SMS, chat) | [...] | [...] |
| **Retention** (subscriptions, loyalty, referral) | [...] | [...] |
| **Feedback** (analytics, heatmaps, surveys) | [...] | [...] |
| **Systems** (automations, integrations) | [...] | [...] |

---

## 💎 Lo que vale la pena copiar

Prioritized list (top 3-5). Each entry follows this structure:

### 1. [Nombre del patrón/app]
- **Qué hace bien**: [observación concreta del UX/copy/posición]
- **Por qué funciona**: [hipótesis basada en principio de conversión]
- **Cómo replicarlo en Advanz**:
  - Path A — Instalar misma app: [costo, tiempo, cuándo conviene]
  - Path B — Native Liquid: [factibilidad, horas estimadas, archivos a tocar]
  - Path C — App alternativa más barata: [cuál, diferencias]
- **Cliente Advanz candidato**: [qué cliente actual podría usarlo: AmazingCare, Thonet, Obio, etc]

---

## 🚫 Anti-patterns detectados

Cosas que viste y NO recomendarías copiar, con razón:

- **[Pattern]**: [por qué no copiar — UX, performance, trust erosion, costo injustificado]

---

## 📊 Calidad UX — veredicto general

Una calificación rápida en 5 dimensiones (1-5):

| Dimensión | Score | Comentario corto |
|---|---|---|
| Velocidad percibida | [N]/5 | [...] |
| Claridad de oferta | [N]/5 | [...] |
| Trust signals | [N]/5 | [...] |
| Friction reduction (cart→checkout) | [N]/5 | [...] |
| Mobile UX (si se inspeccionó) | [N]/5 | [...] |

**Veredicto**: [Una frase resumen — ej: "Stack maduro para DTC LATAM mid-tier, replicable casi en su totalidad con 2-3 semanas de implementación"]

---

## 📚 Próximo paso: Notion sync

Esta análisis se va a guardar en la database **Shopify Tools Library** del workspace `advanzgrowthpartner`. Properties principales: tienda, vertical, theme, # apps detectadas, total monthly cost estimado, candidatos para replicar.

¿Confirmar sync? *(o si la database aún no existe, ofrecer crearla)*
