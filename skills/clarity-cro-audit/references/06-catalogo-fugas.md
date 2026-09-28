# Catálogo de puntos de fuga

Doce patrones que se repiten en casi cualquier ecommerce. Cada uno trae: cómo se detecta sin
opinar, el umbral que lo marca como problema, el arreglo estándar y el efecto esperado.

Recórrelos en orden. Los seis primeros son los que concentran el impacto.

---

## F1 · El CTA está bajo el pliegue

**Detección** `getBoundingClientRect().top` del botón de compra ÷ `scrollHeight`, en viewport
móvil. Cruzar con el mapa de desplazamiento para saber cuánta gente llega a esa altura.

**Umbral** Botón por debajo del 15% de la página, o retención menor al 50% a esa altura.

**Arreglo** Barra de compra fija en móvil, disparada por `IntersectionObserver` sobre el botón
original. 1 día de trabajo.

**Efecto esperado** La exposición al CTA sube del X% al ~90%. Con un supuesto conservador de
que los nuevos expuestos convierten a un sexto de la tasa de quien llega por scroll, la tasa de
agregado al carro sube entre 1,5 y 3 puntos.

**Por qué es el primero** Es el único hallazgo del catálogo que se arregla en un día y toca a
todo el tráfico de la plantilla más visitada.

---

## F2 · Acantilado de scroll

**Detección** Mapa de desplazamiento: buscar la banda de 5% con mayor caída porcentual.

**Umbral** Más de 20 puntos de audiencia perdidos en una sola banda del 5%.

**Diagnóstico** Cruzar la banda con la anatomía del DOM: qué bloque empieza exactamente ahí.
Casi siempre es el precio, un selector obligatorio, o un bloque promocional interpuesto.

**Arreglo** Reordenar: lo que sostiene la decisión sube, lo que la interrumpe baja del botón.
Preseleccionar variantes. Comprimir la galería a un máximo del 42% de la altura del viewport.

**Efecto esperado** Retención en esa banda de X% a X+20 puntos. Tasa de agregado al carro +1 a
+2 puntos.

---

## F3 · Checkout ciego

**Detección** Filtro `Ruta → URL visitada → contiene → checkout`.

**Umbral** 0 sesiones.

**Arreglo** En Shopify, instalar la herramienta como Web Pixel en Customer Events. En otras
plataformas, verificar que el script corra en el dominio del pago.

**Efecto esperado** Ninguno directo. Bloquea la validación de todo lo demás, así que va primero
en el cronograma aunque vaya último en impacto.

---

## F4 · Información escondida

**Detección** Ranking de clics de la ficha: sumar clics en acordeones, pestañas y flechas de
carrusel; comparar con los clics en el botón de compra.

**Umbral** Los clics de exploración superan a los de compra.

**Lectura** No es curiosidad: es gente buscando la respuesta que le falta para decidir. El
contenido de los dos o tres elementos más clicados es exactamente el que debe subir.

**Arreglo** Sacar tres datos decisivos del acordeón y ponerlos como bullets junto al precio.
Poner primero la imagen que explica, no el packshot.

**Efecto esperado** +0,5 a +1 punto de agregado al carro. Los clics en acordeones deben bajar.

---

## F5 · Escalera de precios plana

**Detección** `/products.json` → precio ÷ unidades por SKU. Construir la tabla de precio
unitario por formato.

**Umbral** Menos del 10% de ahorro unitario al subir un escalón de formato. Bandera roja si
algún formato mayor es más caro por unidad que uno menor.

**Arreglo** Rediseñar la escalera (referencia: base · −15% · −25% · −35%) y mostrar el precio
por unidad en la card y en el selector de formato.

**Efecto esperado** No mueve la tasa: mueve el ticket. Si el 25% de los pedidos sube un
escalón, el ticket promedio sube alrededor de un 8%.

**Cuidado** Requiere decisión comercial, no solo desarrollo. Nunca lo decide el equipo de CRO
solo.

---

## F6 · Cupón mostrado sin aplicar

**Detección** Abrir el carrito con productos y comparar el total mostrado con el descuento que
promete la comunicación.

**Umbral** El total no incluye el descuento prometido.

**Arreglo** Enlace de descuento en campañas para que quede aplicado en la sesión, y línea de
descuento aplicada en el carrito en vez del bloque con el código.

**Efecto esperado** El paso carro → inicio de checkout sube entre 3 y 6 puntos.

---

## F7 · Ausencia de precio unitario en la grilla

**Detección** Inspeccionar la card de colección: ¿aparece precio por unidad, por dosis, por
mes?

**Umbral** No aparece y el catálogo tiene más de dos formatos del mismo producto.

**Arreglo** Línea de precio unitario bajo el precio, en color secundario.

**Efecto esperado** Mezcla de formatos hacia arriba. Se mide en el ticket promedio.

---

## F8 · Quick-add canibalizando la ficha

**Detección** Clics de quick-add ÷ clics en el nombre del producto, en el mapa de calor de la
colección.

**Umbral** Relación mayor a 2:1.

**Lectura importante** Esto **no** es necesariamente un problema: significa que la gente compra
desde la grilla. Lo que sí es un problema es leer el embudo «colección → ficha» como fuga
cuando en realidad es un atajo. Corregir la lectura antes de proponer nada.

**Arreglo** Si el quick-add domina, la card tiene que cargar la información que la ficha daría:
precio unitario, reseñas, badge. Y un acceso explícito «Ver detalle» para quien sí quiere leer.

---

## F9 · Navegación por menú en vez de por página

**Detección** Ranking de clics de la colección: comparar hamburguesa + enlaces del menú contra
los productos individuales.

**Umbral** El menú supera a cualquier producto individual.

**Lectura** La página no está haciendo su trabajo de merchandising: el usuario se va a buscar
otra parte del catálogo.

**Arreglo** Revisar arquitectura. Si N SKUs son en realidad un producto con variantes,
consolidarlos. Ojo: es el único arreglo del catálogo con impacto en SEO.

---

## F10 · Errores del tema

**Detección** Tarjeta de errores de JavaScript. Separar errores del navegador o de apps
embebidas (`_autofillcallbackhandler`, `window.webkit.messagehandlers`, `script error.`
genérico) de errores del tema (selectores nulos, `addEventListener` sobre elementos
inexistentes).

**Umbral** Más del 5% de grabaciones con error de selector nulo.

**Arreglo** Reproducir en las plantillas con más tráfico y en navegador in-app. Guardas de
nulidad.

**Efecto esperado** Desconocido hasta verificar. Por eso se verifica primero: cuesta dos horas
y si es real es el arreglo más barato del proyecto.

---

## F11 · Navegador in-app

**Detección** Tarjeta de exploradores: sumar InstagramApp, FacebookApp, TikTok y equivalentes.

**Umbral** Más del 25% del tráfico.

**Lectura** Es un contexto distinto: webview más lenta, sin autocompletado, con salida a un
toque. No se puede comparar su rendimiento con el de un navegador normal, y el INP pesa el
doble.

**Arreglo** No hay uno solo. Sí obliga a: probar todo en ese contexto, vigilar INP, y no usar
flujos que dependan de autocompletado o de múltiples pestañas.

---

## F12 · Eventos duplicados o sesgados

**Detección** Cruzar pares de eventos dentro de un mismo segmento. Y comparar el evento contra
el volumen de la URL equivalente, separando sesiones que aterrizan de sesiones que navegan.

**Umbral** Dos eventos con más del 90% de coincidencia, o un evento que dispara en menos del
30% de las sesiones que aterrizan en su página.

**Arreglo** No usar ese evento como paso de embudo. Definir eventos propios.

---

---

## F13 · Peso y prioridad de las imágenes

La fuga que no se ve en ningún mapa de calor, porque la gente que la sufre se va antes de
generar un solo evento. Es casi siempre el ticket número uno por relación impacto / esfuerzo.

**Detección** Sobre el HTML de la ficha más visitada, sin abrir el navegador:

```bash
curl -s https://<tienda>/products/<handle> > pdp.html
# 1. Imágenes servidas sin parámetro de ancho: Shopify entrega el archivo original
grep -oP 'cdn\.shopify\.com[^"\047 ]+\.(png|jpe?g|webp)[^"\047 ]*' pdp.html \
  | grep -v 'width=' | sort -u
# 2. Peso real de cada una
for u in $(cat urls.txt); do echo -n "$u "; curl -sI "$u" | grep -i content-length; done
# 3. ¿Hay prioridad declarada en la primera imagen?
grep -c 'fetchpriority' pdp.html
# 4. Preconexiones a los CDNs que sirven el LCP
grep -oP '<link[^>]+rel="(preconnect|dns-prefetch)"[^>]*>' pdp.html
# 5. Scripts de terceros
grep -oP '<script[^>]+src="[^"]+"' pdp.html | wc -l
# 6. Peso del propio HTML
wc -c pdp.html
```

**Umbrales**

| Señal | Umbral | Gravedad |
|---|---|---|
| Una sola imagen | > 300 KB en móvil | Alta |
| Suma de imágenes de la primera pantalla | > 1 MB | Alta |
| Dimensión del archivo | > 2× el ancho del contenedor | Media |
| `fetchpriority="high"` en la imagen principal | ausente | Media |
| `preconnect` al CDN de imágenes | ausente | Media |
| HTML de la ficha | > 300 KB | Media |
| Scripts externos | > 25 | Media |
| Apps de reseñas instaladas | más de una | Alta |

**Por qué importa en pesos, no en milisegundos** El tráfico social entra por 4G y sale antes de
que pinte la imagen. Cuando el corte por canal muestra que el canal social convierte a un
tercio del directo y además es el que aterriza directo en la ficha, el peso de la ficha explica
buena parte de esa brecha. Ese cruce — canal × CVR × peso de la ficha — es el que convierte un
hallazgo técnico en un ticket de negocio.

**Arreglo** Es de los pocos que se resuelven en horas y sin riesgo:

```liquid
{%- comment -%} Antes: {{ product.featured_image | image_url }} sirve el original {%- endcomment -%}
<img
  src="{{ product.featured_image | image_url: width: 800 }}"
  srcset="{{ product.featured_image | image_url: width: 480 }} 480w,
          {{ product.featured_image | image_url: width: 800 }} 800w,
          {{ product.featured_image | image_url: width: 1200 }} 1200w"
  sizes="(max-width: 767px) 100vw, 640px"
  width="800" height="800"
  fetchpriority="high" decoding="async"
  alt="{{ product.featured_image.alt | escape }}">
```

Y en `theme.liquid`, dentro de `<head>`, antes de cualquier script:

```liquid
<link rel="preconnect" href="https://cdn.shopify.com" crossorigin>
<link rel="preconnect" href="https://fonts.shopifycdn.com" crossorigin>
```

Toda imagen que no sea la principal lleva `loading="lazy"`. La principal **nunca**: `lazy` en
el LCP lo empeora.

**Riesgo** Bajo. Es reversible en minutos y no toca el flujo de compra. La única precaución es
no bajar de 800 px de ancho en la imagen principal si el sitio tiene zoom.

## Cómo se convierte el catálogo en el reporte

1. Corre F13 antes que nada: es una descarga y seis comandos, y suele dar el ticket cero.
2. Corre F3 y F12: definen el margen de error de todo lo demás.
3. Corre F1, F2, F4 sobre la plantilla de producto más visitada.
4. Corre F7, F8, F9 sobre la colección más visitada.
5. Corre F5 sobre el `products.json` completo.
6. Corre F6 abriendo el carrito.
7. Corre F10 y F11 sobre el proyecto entero.
8. Ordena por **urgencia**: sesiones afectadas ÷ días de trabajo, y lo irreversible antes que lo cosmético.
9. Agrupa en bloques: Medición · Ficha · Colección y catálogo · Carrito y cierre.
10. Contrasta contra `12-piezas-estandar.md`: lo que la tienda **no tiene** y el resto de Shopify sí.
