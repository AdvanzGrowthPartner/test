# Las piezas que el resto de Shopify ya usa

Este bloque no busca fugas: busca **ausencias**. Son ocho piezas que se repiten en las tiendas
Shopify que convierten bien, que cuestan horas y no días, y que casi ninguna tienda mediana
tiene completas. Se revisan una por una sobre la ficha y la colección más visitadas, y las que
faltan entran al plan como items con su fragmento de código listo.

**Regla de presentación:** este bloque se ilustra **con código, no con imágenes**. Un bloque de
código con resaltado se lee más rápido que un mockup cuando lo que se entrega es «pega esto».

**Cómo se detecta cada ausencia** en una sola pasada sobre el HTML descargado:

```bash
curl -s https://<tienda>/products/<handle> > pdp.html
grep -c 'sticky\|is-stuck'           pdp.html   # 1 barra fija
grep -c 'width=' pdp.html; grep -c 'fetchpriority' pdp.html   # 2 imágenes
grep -c 'unit_price\|precio por'     pdp.html   # 3 precio unitario
grep -ci 'envío gratis\|free shipping' pdp.html # 4 barra de envío
grep -ci 'llega\|entrega\|despacho'  pdp.html   # 5 fecha de entrega
grep -ci 'quedan\|stock\|unidades'   pdp.html   # 6 escasez real
grep -ci 'loox\|judge\|okendo\|yotpo\|stamped' pdp.html | sort -u  # 8 apps de reseñas
```

---

## 1 · Barra fija de compra en móvil

**Por qué** Es el arreglo directo de F1. Sin ella, el porcentaje de visitantes que ve un botón
de compra es el porcentaje que llega al píxel donde está — típicamente entre un 20 y un 30%.
Con ella es el 100%.

```css
.sticky-atc{position:fixed;left:0;right:0;bottom:0;z-index:4;display:none;
  gap:10px;align-items:center;padding:10px 12px;background:#fff;
  padding-bottom:calc(10px + env(safe-area-inset-bottom));
  border-top:1px solid #e6e6e6;box-shadow:0 -6px 18px rgba(0,0,0,.08)}
.sticky-atc.is-on{display:flex}
@media (min-width:768px){.sticky-atc{display:none!important}}
```

```js
const cta = document.querySelector('form[action*="/cart/add"] [type="submit"]');
const bar = document.querySelector('.sticky-atc');
new IntersectionObserver(([e]) => bar.classList.toggle('is-on', !e.isIntersecting),
  {threshold: 0}).observe(cta);
```

`env(safe-area-inset-bottom)` no es opcional: sin eso la barra queda bajo la barra de gestos en
iPhone y el botón deja de ser tocable.

## 2 · Imágenes redimensionadas y priorizadas

Ver F13. Es la misma pieza vista desde el otro lado: no es solo que pesen, es que **no está
declarado cuál importa**.

```liquid
<img src="{{ product.featured_image | image_url: width: 800 }}"
     srcset="{{ product.featured_image | image_url: width: 480 }} 480w,
             {{ product.featured_image | image_url: width: 800 }} 800w"
     sizes="(max-width:767px) 100vw, 640px"
     width="800" height="800" fetchpriority="high" decoding="async">
```

## 3 · Precio por unidad visible

**Por qué** El comprador de consumo repetido compara por unidad, no por pack. Si el sitio no
hace la división, la hace él — y muchas veces mal, o no la hace y compra el formato chico.

```liquid
{%- assign uds = product.metafields.custom.unidades.value | default: 1 -%}
{%- assign unitario = variant.price | divided_by: uds -%}
<span class="unit">{{ unitario | money }} por unidad</span>
```

Si el tema ya usa `unit_price_measurement` de Shopify, se muestra el nativo y no se calcula
nada:

```liquid
{%- if variant.unit_price_measurement -%}
  <span class="unit">{{ variant.unit_price | money }} / {{ variant.unit_price_measurement.reference_unit }}</span>
{%- endif -%}
```

## 4 · Barra de progreso a envío gratis, en la ficha

**Por qué** Casi todas las tiendas la tienen en el carrito, donde ya es tarde para decidir el
formato. En la ficha cambia la variante que se elige.

```liquid
{%- assign umbral = 3990000 -%}{%- comment -%} en centavos {%- endcomment -%}
{%- assign falta = umbral | minus: cart.total_price -%}
<div class="ship">
  {%- if falta > 0 -%}Te faltan <b>{{ falta | money }}</b> para el envío gratis
  {%- else -%}✓ Tienes envío gratis{%- endif -%}
  <div class="bar"><i style="width:{{ cart.total_price | times: 100 | divided_by: umbral | at_most: 100 }}%"></i></div>
</div>
```

El umbral se lee de la configuración real de envíos, nunca se inventa.

## 5 · Fecha estimada de entrega

**Por qué** «Llega el jueves 4» responde la objeción que «despacho en 24-48 h hábiles» deja
abierta. Es texto, no requiere integración.

```liquid
{%- assign dias = 2 -%}
{%- assign fecha = 'now' | date: '%s' | plus: 86400 | times: dias | date: '%A %d de %B' -%}
<p class="eta">📦 Pídelo hoy y llega aproximadamente el <b>{{ fecha }}</b></p>
```

Si hay corte de same-day, se declara la hora: es el dato que mueve la compra de hoy.

## 6 · Aviso de stock, solo si es real

**Por qué** Funciona cuando es verdad y destruye confianza cuando no. Se ata al inventario, no
a un contador.

```liquid
{%- if variant.inventory_management == 'shopify'
   and variant.inventory_quantity > 0 and variant.inventory_quantity <= 12 -%}
  <p class="low">Quedan {{ variant.inventory_quantity }} unidades</p>
{%- endif -%}
```

Nunca un número fijo ni un temporizador. Riesgo alto de daño reputacional por una ganancia
marginal.

## 7 · Comparador de formatos

**Por qué** Es la contracara de F5. Si la escalera de precios premia el volumen, hay que
mostrarlo; si no lo premia, primero se arregla el precio y después se muestra.

```liquid
<table class="cmp">
  <tr><th>Formato</th><th>Precio</th><th>Por unidad</th><th>Ahorro</th></tr>
  {%- assign base = product.variants.first -%}
  {%- assign base_u = base.price | divided_by: base.metafields.custom.unidades.value -%}
  {%- for v in product.variants -%}
    {%- assign u = v.price | divided_by: v.metafields.custom.unidades.value -%}
    <tr{% if v.id == product.selected_or_first_available_variant.id %} class="on"{% endif %}>
      <td>{{ v.title }}</td><td>{{ v.price | money }}</td><td>{{ u | money }}</td>
      <td>{{ base_u | minus: u | times: 100 | divided_by: base_u }}%</td>
    </tr>
  {%- endfor -%}
</table>
```

Si la última columna da 4% o menos en el formato grande, el ticket no es de diseño: es de
precios, y el dueño es negocio.

## 8 · Una sola app de reseñas

**Por qué** Dos apps de reseñas instaladas es el patrón más común de peso muerto: dos bundles,
dos hojas de estilo, dos peticiones al inicio, y normalmente una de ellas sin reseñas visibles.

```bash
grep -oiP '(loox|judge\.me|okendo|yotpo|stamped|reviews\.io)' pdp.html | sort | uniq -c
```

Se decide cuál se queda por dónde están las reseñas reales, se migra si hace falta, y se
desinstala la otra **desde el panel de apps** — no basta con quitar el bloque del tema, porque
el script sigue inyectándose.

---

## Cómo entra este bloque al reporte

Como **items**, no como recomendaciones. Cada pieza ausente se convierte en una tarjeta con:

```
Pieza · Qué resuelve · Fragmento de código · Tiempo · Riesgo · Dueño
```

Las piezas presentes también se nombran, en una línea, para que el cliente vea que se revisaron
las ocho. Un bloque que solo lista carencias parece una venta; uno que declara lo que ya está
bien parece una auditoría.
