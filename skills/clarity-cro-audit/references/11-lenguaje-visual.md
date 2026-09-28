# Lenguaje visual del entregable

Quien lee esto es un CRO manager con veinte pestañas abiertas. **Si tiene que leer un párrafo
para entender un hallazgo, el hallazgo no está bien presentado.** La regla operativa: cada
sección tiene que poder entenderse mirando, y el texto solo confirma.

---

## Regla de proporción

Por sección: **un elemento visual dominante, tres o cuatro líneas de texto como máximo.** Si
hace falta más texto, el hallazgo va dentro de un ticket plegado, no en el cuerpo.

Prohibido: párrafos de más de tres líneas en el cuerpo, tablas de más de seis columnas, listas
de más de cinco puntos fuera de un ticket.

---

## Los once componentes

**1 · Fila de KPI.** Cuatro números arriba del todo con su fuente etiquetada. Es lo único que
mucha gente va a leer.

**2 · Embudo de barras.** Un paso por fila: etiqueta y tasa arriba, barra abajo dividida en
«avanza» (color de dato) y «se pierde» (color de pérdida, con el número en el extremo derecho).
Nunca un embudo en forma de cono: las áreas engañan y no se pueden comparar entre pasos.

**3 · Comparación pareada.** Para móvil vs desktop, o antes vs después. Dos barras por métrica,
normalizadas al mayor del par, con leyenda. Un solo vistazo tiene que bastar para ver quién
gana en cada paso.

**4 · Pequeños múltiplos.** Cuando hay dos series de escalas distintas — tráfico y pedidos —
son **dos gráficos**, nunca dos ejes. Mismo ancho, mismas etiquetas de tiempo, un mes destacado
en color de alerta si ahí está la historia.

**5 · Tarjeta de fuga.** Icono, número grande, título de tres palabras, una línea de contexto.
Sirve para el resumen; nunca para el detalle.

**6 · Tarjeta de urgencia numerada.** Para el bloque de apertura y para el orden de ataque.
Rango grande arriba a la izquierda, icono, número dominante, título de una línea, y al pie la
línea de arreglo con su tiempo. **Reemplaza a la matriz impacto/esfuerzo:** tener una matriz de
puntos *y* una lista de tickets es decir lo mismo dos veces, y el lector no sabe cuál manda. Un
único orden, visible, numerado.

**7 · Mockup antes / después.** Dos marcos de teléfono a la misma escala, con la foto y los
precios reales, una línea punteada en el fin de la primera pantalla, y bajo cada uno el dato:
píxeles, porcentaje de página, porcentaje de gente que llega.

**8 · Tarjeta de ticket plegable.** Cerrada muestra: código, título, chips de dueño, tiempo y
riesgo, y la ganancia esperada a la derecha. Abierta muestra el antes/después en dos cajas y
cuatro recuadros: qué hago yo · qué necesito de ustedes · riesgo · cómo se sabe si funcionó.

**9 · Calendario de impacto acumulado.** Cuatro columnas semanales con barras acumuladas en
color de «bien», cada una rotulada con los tickets que entraron en producción esa semana. Bajo
las barras, dos recuadros de rango: mes 1 y mes 2, en pedidos y en dinero. Nunca fechas reales.

**10 · Panel nativo de la plataforma.** Para la proyección. Se dibuja con la estética de la
plataforma auditada — en Shopify: verde `#008060`, fondo `#f6f6f7`, bordes `#e1e3e5`, tipografía
de sistema, filas de tabla con hoy → proyectado. **Estático por definición:** ni un campo
editable, ni un deslizador. Es una lectura, no una calculadora.

**11 · Bloque de código.** Para las piezas estándar ausentes y para las herramientas. Fondo
oscuro fijo (no cambia con el tema), monoespaciada de 11 a 12 px, resaltado por roles —
etiqueta, atributo, valor, comentario, palabra clave — y un encabezado con el nombre del
archivo y un verbo: «pegar en `snippets/`». El código **sustituye a la imagen** en estos
bloques: se lee más rápido cuando lo que se entrega es «pega esto». Siempre dentro de un
contenedor con desplazamiento horizontal propio.

---

## Color

Solo cuatro roles, y ninguno decorativo:

| Rol | Uso |
|---|---|
| **Dato** | Barras, valores, todo lo neutro |
| **Pérdida** | Lo que se cae, lo que está roto, el estado «hoy» |
| **Bien** | Lo que funciona, el estado «propuesto», las ganancias |
| **Atención** | Riesgo medio, advertencias |

El color de acento de la marca del cliente puede reemplazar al de dato. Los otros tres son
semánticos y no se tocan.

Validar siempre el par dato/pérdida con el validador de paletas antes de publicar, en claro y
en oscuro. Los rangos de luminosidad son distintos por modo.

---

## Chips de dueño

Tres, siempre los mismos, siempre con el mismo color:

- 🟣 **Lo hago yo** — análisis, código listo para pegar, especificaciones, configuración.
- 🔵 **Necesita acceso al tema** — publicar, QA. Muchas veces es solo arrastrar bloques en el
  editor de temas, y conviene decirlo porque baja la barrera.
- 🟡 **Decisión de negocio** — precios, márgenes, riesgo asumido. No lo decide CRO.

## Chips de riesgo

- **Sin riesgo / bajo** — reversible en minutos, no toca el flujo de compra.
- **Medio** — cambio visible en una página que vende, o que puede regalar margen si se
  configura mal.
- **Alto** — toca precio o toca SEO. Va al final y con aprobación explícita.

Cada ticket declara además **tiempo** en días u horas. Ningún ticket pasa de 3 días; si pasa,
se parte.

---

## Responsive

Se lee tanto en un teléfono a las once de la noche como en un monitor. No es opcional:

- Un solo contenedor con ancho máximo y padding que se reduce en móvil.
- Todo lo que sea grilla usa `repeat(auto-fit, minmax(…))`, nunca columnas fijas.
- Los mockups antes/después se apilan y la flecha rota 90°.
- Las tarjetas de ticket reordenan la ganancia debajo del título.
- Cualquier tabla ancha va dentro de un contenedor con desplazamiento horizontal propio; el
  cuerpo de la página **nunca** se desplaza en horizontal.
- Tipografía con `clamp()` en títulos.

Verificar renderizando a 390 px y a 1120 px, en claro y en oscuro, antes de publicar.

---

## Escritura

- Titular que nombre el hallazgo, no el tema. «El 82% del tráfico convierte la mitad», no
  «Análisis por dispositivo».
- Cada número lleva su fuente visible.
- Verbos concretos. Nada de «optimizar», «potenciar», «mejorar la experiencia».
- Si una lectura anterior estaba equivocada, se corrige en un recuadro visible.
- Español neutro.
