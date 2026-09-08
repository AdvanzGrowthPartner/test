# Data Pull — qué llamar en cada MCP, en qué orden

El radar cruza 3 tipos de señal antes de opinar:

1. **La verdad del negocio** → Shopify (peaks pasados, ventas, tráfico, comportamiento de SKU).
2. **La ola que viene** → volumen de búsquedas (Ahrefs / Semrush): cuándo sube la demanda de la categoría.
3. **El comportamiento paga pasado** → Meta Ads (qué rindió en eventos previos).

Shopify es obligatorio (Gate 0). Los otros dos mejoran la lectura pero no bloquean — si faltan, se declara el gap.

---

## Gate 0 — Chequeo de conexión (siempre primero)

```
mcp__Shopify__get-shop-info
```
- **Responde** → tienda conectada. Anotar moneda, dominio y zona horaria (importa para leer la curva horaria del peak).
- **Falla** → exigir sin frenar: "necesito la tienda del cliente conectada por MCP para leer sus peaks y catálogo real. Conéctala en la sesión (o pásame la URL + acceso) y seguimos. Sin eso, esto es opinión, no radar." Guiar y esperar. No inventar el análisis.

Si hay varias tiendas: `mcp__Shopify__switch-shop` para apuntar a la del cliente correcto.

---

## 1. Shopify — la verdad del negocio

Herramientas principales: `run-analytics-query` (ShopifyQL), `list-orders`, `get-product`, `search_products`, `get-inventory-levels`, y `graphql_query` para lo que no cubre un tool directo.

### a) El peak del mismo evento, año/edición anterior (curva)
Sacar ventas por día/hora del rango del evento pasado — es el mejor insumo de proyección.
```
run-analytics-query:
  "SHOW total_sales, orders, average_order_value
   BY day
   FROM sales
   SINCE <inicio_evento_anterior> UNTIL <fin_evento_anterior>"
```
Para la curva **horaria** del Día 1 (patrón de compra real del cliente), bajar a `BY hour` en ese día. Esa curva alimenta la proyección (`artifact-spec.md`).

### b) Baseline pre-evento (últimos 30 días normales)
El evento se juzga como **lift sobre esto**, no contra industria.
```
run-analytics-query:
  "SHOW total_sales, orders, average_order_value, sessions, conversion_rate
   BY day FROM sales SINCE -30d UNTIL today"
```
(Si `sessions`/`conversion_rate` no salen por ShopifyQL en esa tienda, sacarlos por GA4/analytics del cliente o pedirlos; marcar la fuente.)

### c) Fuentes de tráfico (de dónde entró la venta)
Para saber qué canal es rentable y cuál trae volumen.
```
run-analytics-query:
  "SHOW total_sales, orders BY referrer_source, referrer_name
   FROM sales SINCE <rango> UNTIL <rango>"
```
`order_referrer_source = 'email'` aproxima el revenue owned (email/SMS) cuando no hay MCP de Klaviyo directo. **Decirlo:** para data fina de email (sends/opens/flows) usar el connector de Klaviyo si está, o pedir el paste del dashboard. No inventar números de email.

### d) Comportamiento de producto (para clasificar el catálogo)
Ventas + vistas + inventario por SKU. Cruzar:
- Ventas por producto: `run-analytics-query: "SHOW total_sales, units_sold, view_sessions BY product_title FROM sales SINCE -90d"` (o `products` dataset según la tienda).
- Vistas sin venta (fantasmas) requieren dato de vistas — de ShopifyQL `view_sessions` / GA4 si está.
- Stock: `get-inventory-levels` para los candidatos a ganador (no se empuja lo que no se puede surtir).
- Catálogo: `search_products` / `get-product` para atributos, precio, márgen si está en metafields.

→ Cómo se traduce esto en ganador/acompañamiento/fantasma/zombie: `product-classification.md`.

### e) Lo que no cubre un tool directo
`graphql_query` para metafields (márgenes, costos), colecciones, descuentos históricos, etc. Ejemplo: leer `variants { inventoryQuantity price compareAtPrice }` para ver si ya hubo descuento y de cuánto.

---

## 2. Volumen de búsquedas — la ola que viene (Ahrefs / Semrush)

Esto es lo que hace al skill *adelantarse*: ver cuándo despierta la demanda de la categoría **antes** de que se traduzca en venta.

**Ahrefs** (llamar `doc` antes del primer uso de un tool):
- `keywords-explorer-volume-history` — histórico mensual de volumen de las keywords de la categoría → revela el mes en que empieza a subir la ola cada año.
- `keywords-explorer-volume-by-country` — filtrar a Chile (`cl`).
- `keywords-explorer-overview` / `matching-terms` — dimensionar la categoría y términos asociados al evento ("cyber [categoría]", "regalo día de la madre", etc.).
- Valores monetarios de Ahrefs vienen en **centavos USD** (dividir por 100). Si un resultado trae `render_with`, usar el render tool indicado.

**Semrush** (alternativa/confirmación): `keyword_research` + `get_report_schema` → `execute_report`; `database = "cl"` para Chile. Útil para tendencia estacional y términos de competencia.

**Lectura:** identificar el mes/semana en que la búsqueda de la categoría empieza a subir → eso define con cuánto tiempo hay que tener la campaña lista (cruzar con las ventanas de lead-time de `event-calendar.md`). Si estas fuentes no están conectadas, seguir con Shopify + el calendario direccional, y marcar el gap.

### Fuentes PÚBLICAS de previsión de búsqueda (cuando no hay Ahrefs/Semrush)
Para la previsión de demanda del evento hay alternativas gratuitas — declararlas como la vía cuando el MCP de SEO no está o el plan es insuficiente:

| Fuente | Qué da | Cómo usarla para el evento |
|--------|--------|-----------------------------|
| **Google Trends** (gratis, sin login) | Interés relativo (0–100) por término, país y tiempo | La mejor para **estacionalidad**: ver la curva anual de "electrolitos"/"cyber [categoría]" en Chile y confirmar cuándo despega la ola. Comparar términos y años. |
| **Google Keyword Planner** (gratis con cuenta Google Ads) | Volumen mensual aprox + pujas | Dimensionar demanda absoluta y costo esperado del search paga para el evento. |
| **Google Search Console** (gratis, del propio sitio) | Queries reales que ya traen tráfico al cliente | Ver qué términos propios crecen pre-evento y priorizar SEO/PMax sobre ellos. |
| **Ubersuggest / Trends de marketplaces** | Volumen y términos relacionados | Complemento rápido si no hay lo anterior. |

**Regla:** si no hay MCP de SEO ni acceso a estas fuentes en la sesión, decir explícitamente "previsión de búsqueda pendiente (falta Google Trends / Keyword Planner)" y proyectar solo desde el histórico propio. Nunca inventar volúmenes.

---

## 4. Qué más cruzar (checklist de fuentes complementarias)

Más allá de las 3 señales núcleo, cruzar lo que haya disponible — cada cruce cierra un gap del brief:

- **Peaks de tráfico de años anteriores (multi-año, no solo el último):** traer la curva del mismo evento en 2-3 ediciones pasadas (Shopify `sessions`/`sales` por día en cada ventana histórica) → confirma que el patrón se repite, mide el crecimiento YoY real y hace la proyección más sólida que un solo año.
- **Relevancia de producto entre eventos:** qué SKUs fueron ganadores en varios eventos (no solo el último) → los "ganadores recurrentes" son la apuesta más segura; los que ganaron una vez y no repitieron, mirarlos con cuidado. Cruzar top-productos de cada evento pasado.
- **Competencia:** Meta Ad Library (`ads_library_search`) + Semrush shopping/paid → qué ofertas y ángulos corren los competidores en el evento, y cuándo entran.
- **Google Trends / Keyword Planner:** estacionalidad y volumen (arriba) → la previsión de la ola.
- **Klaviyo (si conecta):** tamaño y salud de la lista, flows activos, revenue owned fino (hoy se aproxima por `order_referrer_source='email'`).
- **Logística / despacho:** deadline de envío pre-evento, cobertura por región (cruzar con `billing_region` de Shopify), quiebres históricos.
- **Márgenes / costos:** metafields de costo por SKU (`graphql_query`) → qué tolera descuento real (define estacional vs always-on).
- **Reviews / UGC / prueba social:** para la ficha y los creativos del evento.
- **Calendario competitivo:** cuándo entran otros al mismo evento (Cyber.cl, retailers) → ventana de anticipo.
- **Clima / estacionalidad física** (si aplica a la categoría, ej. hidratación en verano): refuerza o modera la proyección.

Todo lo que no se pueda leer se declara como gap en el output.

---

## 3. Meta Ads — comportamiento paga pasado (si está)

Para saber qué canal/creativo rindió en eventos anteriores y cómo proyectar el paid.
- `ads_get_ad_accounts` → resolver la cuenta del cliente.
- `ads_get_ad_entities` / insights con date range del evento pasado → ROAS, spend, campañas ganadoras, fatiga.
- `ads_library_search` → qué está corriendo la competencia para el evento (ángulos, ofertas).

Si Meta no está conectado: proyectar el paid sobre supuestos declarados (spend plan × ROAS histórico de Shopify por canal) y marcarlo.

---

## Orden de llamada recomendado

1. `get-shop-info` (Gate 0).
2. Shopify: baseline (b) → peak anterior (a) → tráfico (c) → producto+stock (d).
3. Volumen de búsquedas (ola) — Ahrefs/Semrush.
4. Meta (paid pasado) si está.
5. Recién ahí: clasificar (`product-classification.md`), puntuar leverage (`leverage-scoring.md`), construir el artifact (`artifact-spec.md`).

**Regla de honestidad:** cada fuente que no respondió o no está conectada se declara en el output ("Meta no conectado — el paid va proyectado sobre spend plan × ROAS histórico"). Un consultor que sabe qué falta decide mejor que uno que confía en un número inventado.
