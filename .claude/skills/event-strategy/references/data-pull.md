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
- **ROAS/MER de equilibrio:** el mínimo para no perder margen con el descuento del evento → define cuánto se puede escalar sin quemar caja.
- **Capacidad de despacho:** pedidos/día que aguanta la operación sin romper la promesa de envío (un peak de 108→300 órdenes/día puede reventar fulfillment).
- **Techo de stock por SKU → techo de venta:** cuánto revenue máximo soporta el inventario antes del quiebre del ganador.
- **Ventana de aprendizaje de plataformas:** días de warm-up que necesita cada campaña para entrar al peak con learning resuelto, no en frío.
- **Tramos de descuento vs margen:** simular 20/30/40% y ver dónde se cae el margen (define la profundidad de la oferta).
- **LTV del cohorte del evento:** % de compradores nuevos recomprable post-evento → el cyber no es solo la venta del día, es adquisición de base.

### Inversión, ROAS e histórico de eventos → el Notion del cliente
La data de **inversión en pauta, ROAS/MER y aprendizajes de eventos pasados** normalmente NO está en Shopify — vive en los **reportes del cliente en Notion** (ej. "Reportes Mensuales" → año → mes, con el reporte del evento como "Octubre (Cyber)"). Leerla **dato a dato** con el MCP de Notion antes de dejar nada "por validar":
- Inversión real por plataforma (Meta / Google), CPA/CPC, campañas ganadoras.
- Revenue del evento (puede diferir del corte de Shopify por ventana distinta — usar el número del reporte como oficial y decir la ventana).
- Aprendizajes: mejores horarios de email, flujos que rindieron, % de carrito abandonado, base de datos, regiones rentables vs no.
**Cuidado con la cifra que se lee:** un reporte puede mostrar una "inversión inicial" que NO es el total del evento (ej. Amazing Care: el reporte de octubre abría con $384K, pero el reporte de Paid Media confirmó **$3,27M totales** con **ROAS 7,9×**). Leer SIEMPRE el reporte de cierre / Paid Media completo (inversión total, ROAS por canal, campañas ganadoras), no la primera cifra. Y contrastar revenue del reporte con Shopify (ventanas distintas dan números distintos).

### Imágenes de producto y creativos (feature + limitación de entorno)
**Traerlas SIEMPRE** — es parte del output. Query MCP Shopify: `search_products` / `get-product` devuelve `featuredMedia.preview.image.url` (URL del CDN), precio, stock y estado por SKU. Con eso se arma un **catálogo en JS** dentro del artifact y se renderiza galería de producto, vista previa de anuncio (1:1 / 4:5 / 9:16) y miniaturas del carrito (ver `artifact-spec.md`).

**Patrón que sí funciona:** `<img src="{url CDN}" onerror="this.remove()">` **encima de un tile/fondo de marca por sabor o tipo**. Así:
- Donde el CDN es alcanzable (Claude Code local, HTML descargado y abierto en el navegador, sitio del cliente) → se ven las **fotos reales**.
- Donde el visor de claude.ai aplica CSP (bloquea hosts externos) → cae al **tile de marca** y no se ve roto.

**Limitación DURA del entorno (confirmada, no teórica):** el egress bloquea `cdn.shopify.com` con **403 por policy en TODOS los entornos probados** — el remoto normal y también una sesión Cowork en "red de confianza" (se lanzó `create_session` y las descargas cayeron 403 igual). O sea: **no se pueden bajar los bytes** para embeberlos como data URI desde ningún entorno de agente, y la CSP del Artifact tampoco deja hotlinkear hosts externos. Consecuencia: dentro del **preview de claude.ai** se ve el fallback de marca, no la foto. **No prometer fotos reales en el preview** sin resolver una de las dos vías reales:
1. **Allowlistear `cdn.shopify.com`** en la política de egress del entorno (única vía para que el agente baje los bytes → data URI).
2. **El usuario pega las fotos en el chat** → aterrizan en disco (`/tmp/.../images/*.png`) y se embeben como data URI (esto **sí** evade el egress porque el byte ya está local). Es el camino más rápido cuando no se puede tocar el allowlist.

Mientras tanto: **entregar también el archivo HTML** (`SendUserFile`), que el usuario abre en su navegador donde el CDN sí carga por hotlink; y decir el estado con todas sus letras. No inventar que las fotos "ya cargan".

Todo lo que no se pueda leer se declara como gap en el output.

---

## 3. Meta Ads — comportamiento paga pasado (si está)

Para saber qué canal/creativo rindió en eventos anteriores y cómo proyectar el paid.
- `ads_get_ad_accounts` → resolver la cuenta del cliente.
- `ads_get_ad_entities` / insights con date range del evento pasado → ROAS, spend, campañas ganadoras, fatiga.

Si Meta no está conectado: proyectar el paid sobre supuestos declarados (spend plan × ROAS histórico de Shopify por canal) y marcarlo.

### Radar de competencia — `ads_library_search` (ranking real, no impresión)
El bloque de competidores del artifact NO se rellena "a ojo". Se rankea con conteo real de anuncios activos:
- `mcp__Meta_MCP__ads_library_search` con `search_terms` = marca del competidor, `countries=["CL"]`, `ad_active_status="ACTIVE"` (y un `client_conversation_id` de 20 chars). Repetir por cada competidor.
- **Métricas que sí se pueden afirmar:** nº de anuncios activos, cuánto tiempo llevan corriendo (recencia / fecha de inicio), ángulos y ofertas visibles en los creativos, y el link directo a la Ad Library de cada uno (para que el consultor verifique).
- **Ranking = quién es más agresivo** (más anuncios activos + más recientes). Ese es el orden del bloque. Complementar con seguidores/alcance solo si hay fuente (Ahrefs social, o dato manual) — si no, decir "alcance/seguidores pendiente", no inventar.
- Cruce útil: "qué hizo el competidor el evento pasado" (creativos que ya no corren) vs "qué corre ahora" → anticipa su jugada.

---

## 3b. Klaviyo — el funnel owned fino (captura, carro, venta)

Shopify aproxima el email por `order_referrer_source='email'`, pero el **funnel de captura y recuperación** —que es donde suele estar la fuga más grande y barata de tapar— vive en Klaviyo. Si el connector está, sacarlo; es lo que hace el bloque de "captura vs add-to-cart vs recuperación vs venta".

**Resolver IDs primero** (no hardcodear los de otro cliente): `get_metrics` lista las métricas con su ID; `get_lists` / `get_flows` dan listas y flujos. Las métricas núcleo a ubicar por nombre:
- **Viewed Form** y **Submitted Form** → el funnel del popup de captura.
- **Added to Cart** (o **Checkout Started**) → intención.
- **Placed Order** → venta.

**a) Funnel de captura del popup** (¿cuántos ven el form vs cuántos dejan el correo?):
```
query_metric_aggregates:
  metric_id = <Viewed Form>   → volumen de vistas del popup
  metric_id = <Submitted Form> → volumen de submits (correos capturados)
  measurement = count, interval = day, rango = últimos 30-90d
```
La **tasa view→submit** es el KPI. Si es baja (form pesado, oferta débil, timing malo), es leverage barato pre-evento: más capturas = más base a la que dispararle el evento. Segmentar por device si el schema deja (`session_device_type` en Shopify, o el breakdown de Klaviyo) — el form suele rendir distinto en mobile vs desktop.

**b) Recuperación de carro — normal vs evento** (`get_flow_report`):
```
get_flow_report:
  flow_id = <flujo de carro abandonado>
  conversion_metric_id = <Placed Order>
  rango normal (baseline)  vs  rango del evento pasado
```
Muestra cuánto revenue **recupera** el flujo y cuánto queda en la mesa. En evento el volumen de carros abandonados se dispara → si el flujo no está afinado (timing, nº de toques, oferta de rescate), la fuga crece. El brief compara **carro normal vs carro en evento** para dimensionar esa fuga.

**c) Salud de la lista y flows activos:** `get_lists` (tamaño), `get_flows` (qué está prendido: welcome, carro, post-compra, winback). Un flujo apagado en evento es dinero regalado.

**Lectura para el brief:** el funnel completo se dibuja horizontal — **vistas de form → correos capturados → add-to-cart → carros recuperados → venta** — con la tasa de caída en cada paso y la comparación normal vs evento. Ahí se ve la fuga barata de tapar antes del peak. Si Klaviyo no conecta: aproximar por `order_referrer_source='email'` de Shopify y **declarar** que el funnel fino de captura/carro queda pendiente. Nunca inventar sends/opens/recuperación.

---

## Orden de llamada recomendado

1. `get-shop-info` (Gate 0).
2. Shopify: baseline (b) → peak anterior (a) → tráfico (c) → producto+stock+imágenes (d).
3. Volumen de búsquedas (ola) — Ahrefs/Semrush/Google Trends.
4. Meta (paid pasado + `ads_library_search` para el radar de competencia) si está.
5. Klaviyo (funnel de captura + recuperación de carro, §3b) si conecta.
6. Notion del cliente (inversión/ROAS/aprendizajes de eventos pasados) — dato a dato.
7. Recién ahí: clasificar (`product-classification.md`), puntuar leverage (`leverage-scoring.md`), construir el artifact (`artifact-spec.md`).

**Regla de honestidad:** cada fuente que no respondió o no está conectada se declara en el output ("Meta no conectado — el paid va proyectado sobre spend plan × ROAS histórico"). Un consultor que sabe qué falta decide mejor que uno que confía en un número inventado.
