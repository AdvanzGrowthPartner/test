# Data Sources — qué llamar, en qué orden, con qué query

Todas estas tools son deferred: hacer `tool_search` para cargarlas antes de usarlas. Los nombres de parámetros se confirman con `tool_search`, no se adivinan.

**Orden de lectura recomendado:** Shopify primero (la verdad del negocio) → Dashbo (TikTok/Google) → Meta → email (vía Shopify). Shopify ancla todo; las plataformas de ads explican el *por qué*.

---

## 1. Shopify (la verdad del negocio) — SIEMPRE

Tool principal: `Shopify:run-analytics-query` (ShopifyQL). Es la fuente de CVR, AOV, ventas reales, sesiones y atribución por canal. Sintaxis `FROM ... SHOW ... TIMESERIES/GROUP BY`.

**Pulso de ventas del evento (peak):**
```
FROM sales SHOW orders, gross_sales, net_sales, total_sales, average_order_value TIMESERIES hour SINCE -1d UNTIL today
```

**Ventas vs baseline (comparar contra periodo previo):**
```
FROM sales SHOW total_sales, orders, average_order_value TIMESERIES day SINCE -3d UNTIL today COMPARE TO previous_period
```

**Conversión y embudo de sesión (¿se convierte el tráfico?):**
```
FROM sessions SHOW sessions, sessions_with_cart_additions, sessions_that_reached_checkout, sessions_that_completed_checkout, conversion_rate TIMESERIES hour SINCE -1d UNTIL today
```

**Atribución por canal — incluye email/SMS (cubre el gap de Klaviyo):**
```
FROM sales SHOW orders, total_sales GROUP BY order_referrer_source, order_referrer_name SINCE -1d UNTIL today
```
> De acá sale el `% revenue owned` (filas con `order_referrer_source = 'email'` o el nombre de Klaviyo). Si no aparece email, el tracking de UTM de Klaviyo no está pasando — anotarlo como hallazgo.

**Top SKUs del evento (qué escalar / qué proteger):**
```
FROM sales SHOW gross_sales, net_sales, orders GROUP BY product_title ORDER BY gross_sales DESC LIMIT 15
```

**Inventario de los SKUs ganadores (stock-aware bidding):**
- `Shopify:search_products` para resolver el GID del SKU ganador → `Shopify:get-inventory-levels` con ese productId.
- Regla: si un top-SKU está cerca de OOS, **no escalar ads que lo empujen**. Ver `optimization-rules.md`.

**Contexto de tienda:** `Shopify:get-shop-info` (moneda, plan, timezone — clave para interpretar las horas del peak en horario Chile).

---

## 2. Dashbo (TikTok + Google — el data moat)

El MCP unificado de paid. Concentra TikTok y Google (y más) en una sola lectura.

**Resolver el cliente:**
- `dashbo_list_clients` → obtener el client_id.
- IDs conocidos: **Amazing Care = 4606**, **Grupo Insurex = 5991**. Para el resto, listar y resolver por nombre.
- `dashbo_list_business_units` → las líneas de control (BU) del cliente.
- `dashbo_list_client_available_fields` → métricas y dimensiones disponibles para ese cliente (no asumir; varían).

**Forma rápida (lenguaje natural → data en un paso):**
- `dashbo_parse_query_get_data` con algo como:
  - "ROAS y spend por campaña de TikTok y Google, últimas 24 horas, comparado con los 7 días previos"
  - "CPA y conversiones por campaña hoy vs ayer"
- Si se necesita control fino de campos/filtros: `dashbo_query_data` (estructurado).

**Indicadores precalculados (alertas, progreso de objetivos):**
- `dashbo_get_business_unit_indicators` → trae alertas y progreso ya calculados por BU. Útil para un pulse ultra-rápido sin armar query.

**Qué leer del resultado:** spend, ROAS/CPA por campaña, tendencia vs periodo previo. Identificar campañas ganadoras (escalar) y perdedoras (matar/pausar) según `optimization-rules.md`.

---

## 3. Meta Ads (FB / IG)

Tools (Meta MCP):
- `ads_get_ad_accounts` → resolver el ad account del cliente.
- `ads_get_ad_entities` → insights a nivel campaña / adset / ad (spend, ROAS/purchases, frequency, CTR, CPM). Esta es la lectura base.
- `ads_get_errors` → errores de entrega que estén capando campañas (rechazos, learning limited, presupuesto agotado). **Correr siempre en peak**: una campaña ganadora frenada por un error es plata dejada en la mesa.
- `ads_insights_performance_trend` → dirección de las métricas en el tiempo (detecta fatiga y caídas).
- `ads_insights_anomaly_signal` → desviaciones raras (spikes de CPM, caídas de CVR) que merecen revisión.
- `ads_get_opportunity_score` → recomendaciones accionables de Meta (tomar con criterio, no seguir ciego).
- `ads_get_ad_preview` → para validar que un creativo de cyber está sirviendo bien.

**Para ejecutar cambios** (si Patricio lo pide explícitamente, no por default):
- `ads_update_entity` → cambiar presupuesto, pausar.
- `ads_activate_entity` → reactivar.
> Por default el skill **recomienda**, no ejecuta. Solo ejecutar cambios en Meta si Patricio lo pide con claridad ("hazlo", "sube el presupuesto de X a $Y").

**Señales clave a extraer:** frequency (fatiga > 3.5 en peak), CTR trend, CPM trend, ROAS por campaña/adset. Reglas en `optimization-rules.md`.

---

## 4. Klaviyo / Email (canal propio)

**No hay MCP de Klaviyo conectado hoy.** Dos caminos:

1. **MVP (default):** sacar el revenue atribuido a email/SMS desde Shopify (`order_referrer_source`, ver query arriba). Da el `% revenue owned`, que es el número que importa para el árbol de restricción.
2. **Data de flow-level** (sends, open rate, click rate, revenue por flow, crecimiento de lista): pedirle a Patricio que pegue los números del dashboard de Klaviyo. Procesar el paste, no inventar.

**Qué se quiere saber del canal propio en cyber:**
- % del revenue total que viene de owned (email/SMS). En cyber sano suele ser una porción relevante; si es bajo, hay palanca sin explotar.
- Estado de los flows críticos: carrito abandonado, browse abandonment, post-compra. (Setup/ajuste fino → `advanz-ecomm-intelligence`.)
- Cadencia de campañas: ¿ya salió el teaser, el "estamos en vivo", el midpoint, el last-chance?

---

## Cálculos derivados (hacer siempre)

- **MER (blended) = revenue total Shopify ÷ spend total (Meta + Dashbo).** Es el número rey. El ROAS por plataforma se solapa por atribución; el MER no.
- **% revenue owned = revenue email/SMS ÷ revenue total.**
- **Pacing = spend acumulado ÷ presupuesto planificado para la fase.** ¿Sub o sobre-invertido?
- **Lift vs baseline = métrica del evento ÷ misma métrica en los 30 días previos.** Ver `benchmarks-cyber.md`.

Si alguna fuente no responde o devuelve vacío: decirlo en la lectura ("Meta no devolvió data — revisar conexión"), no rellenar con supuestos.
