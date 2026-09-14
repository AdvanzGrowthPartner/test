# Fase 1 — Playbooks por superficie

Para cada superficie: **qué revisar**, cómo se ve **"bien"** en DTC, los **límites** (plataforma/plan/theme), y a qué **archivo/sección** del Blueprint pertenece. No inventes tasas — la medición de embudo y fugas se rutea a `clarity-cro-audit` (ShopifyQL + Clarity). Los benchmarks numéricos ("debería ser X%") salen de `advanz-ecomm-intelligence`.

Etiqueta cada hallazgo: `superficie · severidad · archivo/sección · ¿zona frágil del Blueprint?`.

---

## 1. PDP / ficha de producto  → `templates/product.json`, `sections/main-product.*`
La superficie de mayor apalancamiento. Revisar:
- **Above the fold**: título, precio (y precio unitario si aplica en Chile), variantes claras, CTA add-to-cart visible sin scroll, imagen/galería con zoom.
- **Propuesta de valor y prueba**: bullets de beneficio, reviews visibles (rating + conteo), UGC/fotos reales, badges de confianza (envío, devolución, pago).
- **Contenido de decisión**: ingredientes/modo de uso/FAQ — normalmente vienen de **metafields** (ver Blueprint); si el bloque existe, no lo rompas.
- **Urgencia/escasez honesta**, cross-sell/bundle, suscripción si hay selling plan.
- **Velocidad y mobile**: peso de la galería, LCP, sticky ATC en mobile.
"Bien": el usuario entiende qué es, por qué le sirve y confía, sin salir de la pantalla; ATC siempre alcanzable.
Límite: apps de reviews/bundles inyectan bloques propios — edítalos vía su app, no hardcodeando.

## 2. Carrito (drawer o página)  → `templates/cart.json`, `sections/cart-*`, snippets de drawer
Revisar:
- Claridad de line items, edición de cantidad sin recargar, subtotal y **umbral de envío gratis** con barra de progreso.
- **Cross-sell / order bumps** en el carrito (AOV) — sin fricción.
- Cupón: no pedir código de forma prominente si dispara "voy a buscar un cupón" (fuga F6 de clarity).
- CTA de checkout inequívoco; métodos de pago express visibles.
- Estados vacíos con ruta de vuelta a colecciones.
"Bien": subir AOV y llevar a checkout sin distraer. Ojo: en amazingcare esta superficie ya tuvo un "Pre Fix Carrito [Backup]" → zona sensible, QA extra.
Límite: si el drawer es de una app, los cambios van por la app; si es del theme, por la sección.

## 3. Checkout  → acotado por plan
- **Sin Plus**: el checkout es casi intocable por código. Foco en lo editable desde el editor de checkout (branding, mensajes de confianza) y en **upsell post-compra** si hay app compatible; y en que el carrito no meta fricción antes.
- **Con Plus**: Checkout Extensibility (UI extensions, Functions) — trust, campos, envíos, descuentos. Aun así aplica toda la disciplina de la Fase 3.
"Bien": mínimos pasos, pagos express arriba, cero sorpresas de costo. No prometas cambios de checkout que el plan no permite (confírmalo en el Blueprint).

## 4. Colecciones / PLP  → `templates/collection.json`, colecciones smart vs custom
Dos frentes: **la página de colección** y **la construcción de la colección**.
- Página: filtros útiles (no genéricos), orden con sentido comercial (no solo "destacados" fijo), tarjetas con precio/rating/quick-add, precio unitario (F7/F8 de clarity), jerarquía de banners.
- Construcción: ¿smart (reglas) o custom (curado)? Para lanzamientos/estacionales, curado; para catálogo grande, smart. Revisa colecciones huérfanas o vacías, y que las de navegación existan (best sellers, novedades, por beneficio/ocasión).
- Merchandising: orden de productos dentro de la colección (sort manual vs. automático), destacar hero/best sellers arriba.
"Bien": el usuario llega a una lista relevante, filtra rápido y encuentra el producto correcto. Herramientas MCP útiles: `search_collections`, `get-collection`, `create-collection`, `update-collection`, `add-to-collection`.

## 5. Home / merchandising  → `templates/index.json`
El hueco que ninguna skill cubría. Revisar:
- **Hero**: promesa clara + CTA único a una ruta de compra (no 5 CTAs compitiendo).
- **Ruta a colección/PDP** en 1-2 clics; secciones que empujan al catálogo, no solo branding.
- **Prueba social temprana** (reviews, medios, nº de clientes), propuesta de valor (envío, garantía).
- Orden de secciones: lo que vende arriba; branding y "nuestra historia" abajo.
- Coherencia mobile del orden de secciones.
"Bien": en 5 segundos se entiende qué se vende, a quién y por qué confiar, con un camino obvio a comprar.

---

## Salida de la Fase 1
Lista de hallazgos etiquetados por superficie/severidad/archivo, lista para alimentar la priorización de la Fase 2. Marca en rojo los que caen en zonas frágiles del Blueprint (secciones custom, bloques de app, carrito ya intervenido): esos exigen más QA y aprobación explícita en Fase 3.
