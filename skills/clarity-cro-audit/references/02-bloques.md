# Los 6 bloques de extracción

Cada bloque: qué preguntar, cómo sacarlo de Clarity, y cómo leerlo. Ejecuta los tres rangos
(365d / 90d / 30d) al menos en los bloques 0, 2 y 5.

---

## Bloque 0 · Salud del tracking

**Pregunta:** ¿qué números de este proyecto me puedo creer?

| Qué mirar | Dónde | Lectura |
|---|---|---|
| ¿Se ve el checkout? | Filtro `Ruta → URL visitada → contiene → checkout` | 0 sesiones = ciclo cortado en el ATC. Es lo primero que se reporta |
| Cobertura del script | Compara páginas vistas por sección con el catálogo real | Faltan secciones = script no está en todas las plantillas |
| Fiabilidad por evento | Sesiones del evento vs páginas vistas equivalentes, y dentro del segmento "entra directo" | <30% de cobertura = evento no usable como paso |
| Eventos duplicados | Cruza pares de eventos | Dos eventos con casi el mismo conteo = están midiendo lo mismo |
| Tráfico de bots | Tarjeta *Tráfico de bots* | >10% obliga a filtrar bots antes de comparar periodos |
| Errores de JavaScript | Tarjeta *Errores de JavaScript* | Errores tipo `null is not an object (evaluating 'X.addEventListener')` son código propio roto: candidatos directos a fuga |

Distingue siempre errores del navegador o de apps embebidas (`_autofillcallbackhandler`,
`window.webkit.messagehandlers`, `script error.` genérico de scripts cross-origin) de errores
del tema (selectores nulos, `addEventListener` sobre elementos inexistentes). Los primeros son
ruido; los segundos rompen funcionalidad.

**Salida del bloque:** una lista de "esto sí se puede medir / esto no", que encabeza el reporte.

---

## Bloque 1 · Conversiones que importan

**Pregunta:** ¿cuál es el ciclo real de este negocio y qué proxy mide cada paso?

1. Escribe el ciclo tal como lo vive el cliente, no el genérico. Para ecommerce con carrito
   lateral: *entrada → descubrimiento (colección o PDP) → PDP → selección de variante → ATC →
   abrir carrito → ir a pagar → checkout → compra*.
2. Marca cada paso como **medible / proxy / ciego** según el Bloque 0.
3. Define la **conversión primaria medible**. Si no hay purchase, es el último paso visible
   (normalmente "inicio de checkout") y se dice explícitamente que no es una venta.
4. Define micro-conversiones secundarias que sí se miden: suscripción, uso del buscador,
   apertura de reseñas, contacto.

**Salida:** tabla de pasos con su proxy y su nivel de confianza. Sin esto, todo el resto del
reporte se malinterpreta.

---

## Bloque 2 · Navegación general

**Pregunta:** ¿el tráfico que llega tiene intención, y el sitio se la sostiene?

| Métrica | Dónde | Señal |
|---|---|---|
| Sesiones + tendencia | Tarjeta *Sesiones* → icono de tendencia | Quiebres = cambios de canal o de tracking |
| Páginas por sesión | Tarjeta | <1,5 = el sitio no consigue un segundo clic |
| Profundidad de scroll | Tarjeta | <30% = no llegan a los bloques de venta |
| Tiempo activo | Tarjeta | Es tiempo **activo**, no de sesión. <45s en ecommerce = lectura superficial |
| Nuevos vs recurrentes | Tarjeta *Información general de los usuarios* | >80% nuevos = negocio dependiente de tráfico pagado |
| Dispositivo / navegador | Tarjeta *Exploradores/Dispositivos* | Navegador in-app (InstagramApp, FacebookApp) es un contexto distinto: webview lenta, sin autofill, con cierre fácil |
| Canal / campaña / fuente | Tarjeta *Origen de referencia* (pestañas) | Clarity clasifica por referrer: el tráfico in-app suele caer en "Other". No confundir con directo |
| Rendimiento (LCP/INP/CLS) | Tarjeta *Rendimiento* | INP alto = la página responde tarde al toque: se siente rota en móvil |

Corre las mismas métricas dentro de los segmentos de fuga: la diferencia entre el promedio y
el segmento es el diagnóstico.

---

## Bloque 3 · Flujo entre URLs

**Pregunta:** ¿por dónde entran, por dónde pasan y en qué página se van?

Clarity no tiene reporte de rutas. Se reconstruye con tres piezas:

**(a) Entradas.** `Ruta → URL de entrada → contiene → /products/` (y `/collections/`, home).
Da el reparto real de aterrizajes. Es la corrección más importante frente a asumir que todos
entran por la home.

**(b) Tránsito.** Embudos de URL (embudos B y C). El paso a paso entre secciones te da la tasa
de avance entre plantillas, que es lo que ningún reporte de páginas vistas muestra.

**(c) Salidas.** `Ruta → URL de salida → contiene → <patrón>`. Repite para home, `/collections/`,
`/products/`, `/cart`, blog. Ordena por sesiones: esa es tu tabla de páginas de salida.

Cruce clave: **una página con muchas entradas y muchas salidas es una landing que no engancha;
una con pocas entradas y muchas salidas es un callejón sin salida de la navegación interna.**

Si el `/cart` casi no aparece ni en entradas ni en salidas, el sitio usa carrito lateral y hay
que medirlo con eventos, no con URLs.

---

## Bloque 4 · Puntos de fuga

**Pregunta:** ¿qué está deteniendo a la gente en cada punto?

Para cada fuga identificada en el bloque 5, aplica el segmento correspondiente y lee:

| Señal | Qué significa | Cómo confirmarla |
|---|---|---|
| Retrocesos rápidos altos | La página siguiente decepcionó y volvieron | Grabaciones del segmento, ver los 10 primeros segundos |
| Clics fallidos (dead clicks) | Tocan algo que parece interactivo y no lo es | Heatmap de clics de esa URL: busca clics sobre imágenes, precios, badges |
| Clics continuos (rage) | Algo no responde | Grabación + consola de errores JS |
| Desplazamiento excesivo | Buscan algo que no encuentran | Heatmap de scroll: ¿dónde está el contenido que buscan? |
| Scroll bajo con salida | No llegaron al bloque de venta | Heatmap de scroll y posición del CTA |
| Errores JS en el segmento | Funcionalidad rota | Tarjeta de errores filtrada por el segmento |

Cierra siempre con **grabaciones**: mínimo 10 por fuga, elegidas dentro del segmento. Una fuga
sin una grabación que la muestre es una teoría, no un hallazgo.

Heatmaps a revisar sí o sí: colección principal, PDP más vista, home. En mobile y desktop por
separado.

---

## Bloque 5 · Ciclo de venta

**Pregunta:** ¿cuánta gente y cuánto volumen se pierde en cada paso?

Lee los embudos A, B, C y D en 90 días y anota, por paso:

```
Paso · sesiones que llegan · % que avanza · sesiones perdidas
```

Y calcula:
- **Tasa de avance** de cada paso.
- **Volumen absoluto perdido** de cada paso ← esto ordena la prioridad.
- **Tiempo medio para convertir** (lo da la tarjeta): tiempos muy cortos en ecommerce de
  consideración media sugieren compra impulsiva; muy largos, duda no resuelta.

Compara los mismos embudos entre segmentos (móvil vs desktop, entrada directa a PDP vs
navegación desde colección, nuevos vs recurrentes). La brecha entre segmentos es la hipótesis.

---

## Bloque 6 · Lectura rápida (el entregable vivo)

No es análisis: es dejar el panel usable. Confirma que quedaron guardados los embudos A-D y
los segmentos 01-08, y anota en el reporte cómo se leen. El criterio es que alguien del equipo
abra Clarity un lunes, elija un segmento y entienda la fuga sin volver a configurar nada.
