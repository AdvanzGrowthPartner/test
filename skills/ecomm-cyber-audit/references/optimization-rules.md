# Optimization Rules — qué mover, cuándo, cuánto

Reglas por canal, consistentes con el stack de paid de Advanz (regla del 20% para escalar, 3x kill rule, 70/20/10, fatiga por frequency). Todas se aplican **solo a la restricción diagnosticada** — no se corren todas a la vez.

---

## Gate 0 — Integridad de data (correr SIEMPRE antes de optimizar)

Si cualquiera de estas falla, la acción #1 es arreglar tracking, no mover presupuesto:

- **Cuadre grosero Shopify vs plataformas:** las purchases reportadas por Meta+Dashbo no deberían exceder absurdamente las órdenes reales de Shopify. Si Meta reporta 200 compras y Shopify muestra 60 órdenes totales, hay doble conteo o atribución inflada → no escalar sobre ese ROAS.
- **Pixel / CAPI vivo:** si Meta marca eventos faltantes o el match quality cayó, el algoritmo está optimizando a ciegas.
- **UTMs de email:** si en la atribución de Shopify no aparece `email` como fuente, Klaviyo no está marcando y el % owned está subestimado.
- **GA4 / conversiones:** caída brusca de conversiones registradas sin caída de ventas reales = tracking roto, no performance.

> En cyber, el costo de optimizar sobre data mala es máximo: se escala lo que parece ganar y se mata lo que parece perder, ambos al revés.

---

## Adquisición sub-invertida (ROAS/MER alto + pacing bajo)

La restricción más común y más rentable de relevar en peak: hay demanda rentable y no se está comprando suficiente.

- **Escalar ganadores +20% por movida.** Subir presupuesto en saltos de ~20% para no resetear el learning. Repetir cada pocas horas mientras el ROAS aguante por encima del target. (Subidas bruscas de 2x sí resetean aprendizaje y matan el momentum.)
- **Subir caps** de las campañas/adsets ganadores si están topando presupuesto.
- **Abrir presupuesto a campañas con ROAS sobre target** que estén limitadas.
- En Meta: priorizar Advantage+ Shopping con el catálogo de cyber. En Google: subir el cap de tROAS en PMax y branded search. En TikTok: empujar Spark Ads / Smart+ con el creativo de oferta.
- **Regla de stop:** dejar de escalar una campaña cuando su ROAS marginal cae bajo el target o cuando el SKU que empuja se acerca a OOS.

---

## Tienda / Oferta (tráfico OK pero CVR colapsó)

Está entrando tráfico pero no convierte. Escalar ads acá es echar agua a un balde con hoyo.

- **Velocidad de sitio bajo carga:** en peak, apps pesadas y scripts de terceros tumban el CVR móvil. Diferir/pausar apps no críticas. (El móvil es la mayoría del tráfico cyber en Chile.)
- **Claridad de la oferta:** ¿el descuento se entiende en 3 segundos en el PDP y en el home? Si el usuario tiene que calcular, se va.
- **Fricción de checkout:** revisar `sessions_that_reached_checkout` vs `completed_checkout`. Si la caída está en el checkout, el problema es pago/envío/costos sorpresa, no el ad.
- **Match mensaje-creativo-landing:** el creativo promete X, la landing debe mostrar X arriba del fold. Desalineación = bounce.
- **No escalar adquisición hasta tapar el hoyo.** Primero CVR, después volumen.

---

## Canasta (CVR OK pero AOV bajo)

Convierte bien pero cada compra vale poco. Palanca de revenue sin gastar un peso más en ads.

- **Umbral de envío gratis** un poco sobre el AOV actual (ej. AOV $25.000 → envío gratis desde $30.000). En Chile el despacho gratis mueve más que un % extra de descuento.
- **Bundles / packs de cyber** de los SKUs ganadores.
- **Upsell post-compra** (one-click) en el thank-you page.
- **Cross-sell** de complementos del top-SKU en el PDP/carrito.
- Mensaje de "te faltan $X para envío gratis" en el carrito.

---

## Owned / Retención (adquisición al tope + ROAS cayendo)

La adquisición paga ya rinde decreciente. El revenue marginal más barato está en el canal propio.

- **Exprimir la lista:** cadencia de campañas email/SMS más agresiva durante el evento — teaser → "estamos en vivo" → midpoint → last-chance / "extendido". Ver cadencia en `cyber-playbook.md`.
- **Retargeting caliente:** audiencias de add-to-cart e initiate-checkout de las últimas 72h, con presupuesto propio.
- **Segmentar:** VIPs / repeat buyers reciben early access u oferta diferenciada; no-compradores reciben más empuje.
- **Flows tensados:** acortar el delay del carrito abandonado durante cyber (la ventana de decisión es más corta). Browse abandonment activo.
- (Setup fino de flows en Klaviyo → `advanz-ecomm-intelligence`.)

---

## Inventario / Margen (todo verde)

Cuando los 4 signos están sanos, la restricción se vuelve física: stock y margen.

- **Proteger stock de SKUs ganadores:** monitorear inventario de los top-SKUs (ver `data-sources.md`). Cuando uno se acerca a OOS, **bajar el spend que lo empuja** y redirigir a otro SKU con stock y buen margen.
- **No quemar ads en SKUs sin stock.** Es la fuga más invisible: parece que la campaña gana, pero las órdenes se caen o se reembolsan.
- **Cuidar margen:** si para sostener ROAS hay que profundizar el descuento, chequear que el margen unitario siga positivo. Vender a pérdida a escala en cyber es la trampa clásica.
- **Capturar el cohorte:** todo comprador de cyber entra a un flow de retención (ver Post en `cyber-playbook.md`). Acá se gana el LTV, no en el evento.

---

## Fatiga creativa (transversal, vigilar en peak)

- **Frequency > 3.5** en peak + **CTR cayendo** + **CPM subiendo** = fatiga. Rotar creativo, no subir presupuesto (subir presupuesto a un creativo fatigado acelera la quema).
- Tener un banco de 3-5 variantes de creativo de cyber listas desde la fase Pre para rotar sin frenar.
- CPM subiendo **con CVR estable** ≠ fatiga: es competencia de subasta (todos pujan en cyber). Ahí se aguanta o se mueve a retargeting más barato, no se rota creativo.

---

## Cómo rankear las acciones (leverage)

Ordenar por: **impacto esperado × reversibilidad ÷ esfuerzo.**
- Alta reversibilidad (subir presupuesto, pausar un adset) → barato de probar, va arriba.
- Baja reversibilidad (cambiar precio de catálogo, rehacer PDP) → más caro de revertir, exige más certeza.
La acción #1 siempre es la que mueve la restricción diagnosticada. El resto, en orden de leverage.
