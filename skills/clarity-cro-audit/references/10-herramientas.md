# Mapa de herramientas · 100% CRO

Este diagnóstico es **solo CRO**. Nada de medios, nada de SEO, nada de retención salvo cuando
son la única forma de leer una fuga del embudo. Todo lo que está acá tiene que poder copiarse y
pegarse el mismo día: el criterio es que **mañana el diagnóstico esté vivo**.

**La regla de oro: empezar por la plataforma de ecommerce, no por la herramienta de
comportamiento.**

```
1. Shopify   → el embudo real y el dinero        ¿CUÁNTO se pierde y DÓNDE?
2. DOM       → la posición de cada elemento      ¿EN QUÉ PÍXEL?
3. Clarity   → el comportamiento                 ¿POR QUÉ?
```

Invertir el orden es el error clásico. Clarity da una foto rica pero sesgada; Shopify da la
verdad en una consulta. En una auditoría real Clarity contaba 2.821 carros y Shopify 4.051: un
30% de subconteo. Con el diagnóstico construido solo sobre Clarity, todos los porcentajes del
reporte habrían estado mal.

---

## 1 · Shopify · MCP `run-analytics-query` · fuente de verdad

Todo número de dinero sale de acá. Las seis consultas del diagnóstico, para pegar tal cual:

```sql
-- A · El embudo. Es la consulta que abre cualquier auditoría.
FROM sessions SHOW sessions, sessions_with_cart_additions,
     sessions_that_reached_checkout, sessions_that_completed_checkout, conversion_rate
SINCE -90d UNTIL today

-- B · El corte que casi siempre revela el problema, y que fija el techo de la proyección
FROM sessions SHOW sessions, sessions_with_cart_additions, sessions_that_reached_checkout,
     sessions_that_completed_checkout, conversion_rate
GROUP BY session_device_type SINCE -90d UNTIL today

-- C · El canal: dónde entra el tráfico barato que no convierte
FROM sessions SHOW sessions, conversion_rate, sessions_that_completed_checkout
GROUP BY referrer_source ORDER BY sessions DESC SINCE -90d UNTIL today

-- D · Dinero y descuentos
FROM sales SHOW orders, gross_sales, discounts, net_sales, total_sales, average_order_value
SINCE -90d UNTIL today

-- E · Mezcla de producto: qué formato se vende de verdad
FROM sales SHOW orders, gross_sales GROUP BY product_title ORDER BY gross_sales DESC LIMIT 15

-- F · Historia: ¿el tráfico y las ventas van acopladas?
FROM sessions SHOW sessions, sessions_that_completed_checkout TIMESERIES month SINCE -365d
```

Con esas seis ya tienes el embudo, la brecha por dispositivo, el canal culpable, el ticket, lo
que se va en descuentos, la mezcla y el acople tráfico-ventas.

**Qué no da:** el porqué. No dice si la gente no agrega al carro porque el botón está escondido
o porque el precio no convence.

## 2 · DOM y HTML del sitio · sin acceso, sin permisos

Es el paso que convierte un diagnóstico en un ticket. Sin esto el reporte dice «la ficha
convierte poco»; con esto dice «el botón está a 1.645 px y solo el 26% llega ahí».

```bash
# Todo el material de F13 y del bloque de piezas estándar, en una descarga
curl -s https://<tienda>/products/<handle> > pdp.html
curl -s https://<tienda>/products.json?limit=250 > products.json
curl -s https://<tienda>/collections/<handle>/products.json?limit=250 > col.json
```

En la consola del navegador, en viewport móvil:

```js
// assets/medir-plantilla.js  → anatomía, píxeles del CTA, veredicto de F1
// assets/auditar-assets.js   → peso, dimensiones y prioridad de cada imagen
// assets/escalera-precios.js → veredicto de F5 sobre products.json
```

Los tres devuelven un objeto, no un texto: se pegan directo en el reporte.

## 3 · Microsoft Clarity · sin conector, se recorre por navegador

**Qué sí da y nadie más da:** mapas de desplazamiento, ranking de clics por elemento,
grabaciones, segmentos de comportamiento.

**Qué no da:** el checkout de Shopify (cero cobertura salvo instalación como Web Pixel) ni
números fiables — sus eventos automáticos son heurísticas del DOM.

**No existe MCP de Clarity** y su Data Export API devuelve solo 3 días, así que sirve para
monitoreo, no para histórico. **Regla: ninguna decisión del reporte puede depender solo de
Clarity.**

La configuración mínima para que mañana esté leyendo bien — se hace en 15 minutos y está
detallada en `01-setup.md`:

| Qué | Cómo |
|---|---|
| Segmento «con venta» | Evento de compra = existe |
| Segmento «sin venta» | Llegó al carro y no compró |
| Embudo de 4 pasos | Colección → Ficha → Carro → Checkout |
| Filtro de móvil | Dispositivo = Mobile, guardado como vista |

Y el Web Pixel que le da visión del checkout, en Shopify → Configuración → Eventos de cliente →
Agregar pixel personalizado:

```js
(function(c,l,a,r,i,t,y){
  c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
  t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
  y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window, document, "clarity", "script", "<PROJECT_ID>");
analytics.subscribe("checkout_started", e => window.clarity("set","paso","checkout_iniciado"));
analytics.subscribe("payment_info_submitted", e => window.clarity("set","paso","pago_enviado"));
analytics.subscribe("checkout_completed", e => window.clarity("set","paso","compra"));
```

Sin este pixel, el tramo más caro del embudo — el que ya tiene intención de pagar — es un punto
ciego para todo lo que no sea Shopify.

## 4 · Skills que se combinan con esta

| Skill | Para qué, dentro del diagnóstico |
|---|---|
| `dataviz` | Validar la paleta dato/pérdida en claro y oscuro antes de publicar |
| `artifacts-builder` / publicación | El entregable es una página autocontenida |
| `webapp-testing` | Renderizar el entregable a 390 y 1120 px y detectar desbordes |

---

## Tabla de decisión

| Pregunta | Fuente | Con qué |
|---|---|---|
| ¿Cuánto vendemos y con qué ticket? | Shopify | Consulta D |
| ¿Dónde se cae el embudo? | Shopify | Consulta A |
| ¿Móvil o desktop, y cuál es el techo? | Shopify | Consulta B |
| ¿Qué canal trae tráfico que no convierte? | Shopify | Consulta C |
| ¿En qué píxel está el botón? | DOM | `medir-plantilla.js` |
| ¿Cuánto pesa la ficha y qué imagen manda? | HTML | `auditar-assets.js` |
| ¿La escalera de precios premia el volumen? | `products.json` | `escalera-precios.js` |
| ¿Qué piezas estándar faltan? | HTML | `12-piezas-estandar.md` |
| ¿Hasta dónde scrollea la gente? | Clarity | Mapa de desplazamiento |
| ¿Qué tocan y qué ignoran? | Clarity | Ranking de clics |
| ¿Qué pasó en esa sesión? | Clarity | Grabaciones del segmento sin venta |

## Fuera de alcance en este diagnóstico

Meta Ads, Google Ads, Klaviyo, Ahrefs y Semrush **tienen conector y no se usan acá.** Aparecen
en una sola línea al final del entregable, como el paso siguiente, y solo cuando un ticket los
necesita: Ads para poner precio al tráfico que se está perdiendo, Klaviyo para recuperar el
abandono mientras se arregla la causa, Ahrefs o Semrush como seguro antes de tocar URLs. Nada
de eso entra en el diagnóstico de CRO ni en la proyección.

## Qué falta en el stack

Un conector de Clarity. No existe. Se compensa con Shopify como fuente de verdad y los scripts
de DOM. Si algún día aparece, ahorraría la parte manual de navegar mapas de calor — no
cambiaría ninguna conclusión.
