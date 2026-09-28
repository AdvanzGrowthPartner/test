# El entregable

Un reporte de CRO se juzga por una sola cosa: si alguien puede ejecutarlo sin volver a
preguntar. Esta es la estructura que lo consigue, en orden.

---

## Estructura obligatoria

Doce secciones, en este orden. **El orden es por urgencia, no por método:** el lector abre el
documento y lo primero que ve es qué hacer esta semana, no cómo se hizo el análisis.

| # | Sección | Qué contesta |
|---|---|---|
| 01 | **Los cinco de esta semana** | ¿Qué hago el lunes? Cinco tarjetas numeradas por urgencia |
| 02 | **Dónde se cae la gente** | El embudo real, con la fuga mayor destacada |
| 03 | **El mismo sitio, tres negocios distintos** | El corte por dispositivo y por canal |
| 04 | **La ficha pesa lo que no debe** | F13: peso, dimensiones, prioridad, scripts |
| 05 | **Lo que hay hoy y lo que debería haber** | Mockups actual vs propuesto, a escala |
| 06 | **Orden de ataque** | Todos los tickets, ordenados por urgencia, en un solo bloque |
| 07 | **Las piezas que el resto de Shopify ya usa** | Las ausencias, ilustradas con código |
| 08 | **Qué se despliega y qué se acumula** | Calendario de 30 días con impacto acumulado |
| 09 | **Lo que se recupera** | Proyección estática, con la estética de la plataforma |
| 10 | **Con qué se hace** | Herramientas y fragmentos para copiar y pegar |
| 11 | **Lo que se puede romper** | Las dos listas de `13-no-tocar.md` |
| 12 | **Cómo se replica** | El catálogo de fugas como sistema |

### Reglas de orden

- **Un solo bloque de prioridad.** El error más común es tener una matriz impacto/esfuerzo *y*
  una lista de tickets: dicen lo mismo dos veces y el lector no sabe cuál manda. Se fusionan en
  la sección 06, con las tarjetas ordenadas por urgencia y agrupadas en «esta semana»,
  «semanas 2 y 3» y «después de medir».
- **La urgencia manda sobre el esfuerzo.** Primero lo que pierde dinero ahora mismo y se
  arregla en horas; después lo grande; al final lo que necesita un experimento.
- **Cada sección abre con su número, no con su método.** «8,45 MB en una imagen», no «análisis
  de rendimiento de assets».

## Formato de item

```
Bloque X · Nombre
  Item X1 · Qué resuelve · Días · Ticket asociado
```

Ningún item pasa de 3 días. Si pasa, no es un item: es un proyecto y hay que partirlo. Los
bloques agrupan por superficie del sitio, no por disciplina, porque así se asignan a una
persona.

## Formato de ticket

Cerrado, en una línea escaneable:

```
T<n> · <Título afirmativo>
  [chip dueño] [chip dueño] [tiempo] [riesgo]              [ganancia esperada]
```

Abierto:

```
  HOY → DESPUÉS        dos cajas enfrentadas, tres líneas cada una
  Qué hago yo          lo que se entrega sin que nadie haga nada
  Qué necesita de ustedes   acceso, decisiones, QA — y cuánto tiempo suyo
  Riesgo               nivel + el cuidado concreto
  Cómo se sabe         la métrica exacta con su valor de hoy y el plazo de lectura
```

**Los tres chips de dueño** son siempre los mismos: lo hago yo · necesita acceso al tema ·
decisión de negocio. Distinguirlos es lo que hace que el plan arranque: sin eso, el cliente
asume que todo depende de él y no empieza nada.

**El riesgo se declara siempre**, incluso cuando es nulo. Un ticket sin riesgo declarado se lee
como un ticket con riesgo desconocido.

«El cambio» tiene que incluir números: alturas en píxeles, breakpoints, nombres de eventos,
umbrales. Un ticket que dice «mejorar la jerarquía» no es un ticket.

## Mockups actual vs. propuesto

Dos marcos de teléfono lado a lado, a la misma escala, con:

- La foto y los precios reales del producto (se bajan del `products.json`).
- Una línea punteada donde termina la primera pantalla.
- Bajo cada marco, una línea con el dato: píxeles hasta el CTA, porcentaje de página, y
  porcentaje de visitantes que llega.
- Un pie de figura que enumere qué cambió, en orden.

Si no se puede capturar el sitio, se reconstruye a escala y se dice en el pie. Un mockup
anotado comunica más que una captura sin anotar, porque muestra el estado propuesto que una
captura no puede mostrar.

## El calendario de 30 días

No es un cronograma de tareas: es **impacto esperado acumulado cruzado con el tiempo de
ejecución.** Un diagrama de barras semanales donde cada barra suma lo que ya está desplegado.

```
Semana 1   ██                        +6 pedidos     T0, T7, T8 desplegados
Semana 2   ██████                   +29 pedidos     + T1, T10
Semana 3   ███████████              +68 pedidos     + T2, T3
Semana 4   ████████████████        +105 pedidos     + T6, primeras lecturas
```

Reglas:

- La barra es **acumulada**, no semanal. Lo que se quiere comunicar es la curva, no el pico.
- Cada semana nombra los tickets que **entraron en producción**, no los que se trabajaron.
- Debajo, dos rangos: mes 1 y mes 2, cada uno en pedidos **y** en dinero, con los dos extremos
  explicados.
- Se distinguen dos clases de señal: lo que se ve en días (peso, clics, avance de paso) y lo
  que necesita volumen para leerse (conversión, ticket promedio).
- Nunca fechas de calendario reales. Semanas relativas: el plan arranca cuando arranque.

## La proyección

Va después del calendario y **no tiene nada movible**. Es una lectura, no una calculadora.

- **Sin campos editables, sin deslizadores, sin supuestos que el lector pueda cambiar.** Si el
  lector puede mover un número, deja de ser una proyección y pasa a ser un juguete; y el
  primero que lo mueva va a llegar a una cifra que nadie puede defender.
- Sale **enteramente de los datos de la conexión**: sesiones, tasa por paso, pedidos y ventas
  reales de los últimos 90 días, y como techo la brecha del propio sitio entre móvil y desktop.
- Se presenta **con la estética de la plataforma auditada**. Si es una auditoría de Shopify,
  el panel se ve como el panel de Shopify: mismo verde, mismos grises de tabla, mismos nombres
  de métrica. El lector reconoce la pantalla y no tiene que aprender a leerla.
- Cada fila muestra hoy → proyectado, y la última fila declara **qué porcentaje de la brecha
  con desktop se está cerrando**. Ese es el supuesto real, y va visible.
- Nada de costos ni de honorarios. Pedidos, ventas y margen.

## Reglas de escritura

- Cada afirmación lleva su número y su ruta de verificación.
- Los rangos siempre con los dos extremos explicados.
- Si una lectura anterior estaba equivocada, se corrige en un recuadro visible. La credibilidad
  del documento sube, no baja.
- Nada de «optimizar», «potenciar», «mejorar la experiencia». Verbos concretos.
- Español neutro.

## Comprobación final

Antes de entregar, responde estas cinco en una línea cada una. Si alguna no se puede:

1. ¿Cuál es la fuga más grande, en sesiones?
2. ¿Qué se hace el lunes?
3. ¿Cuántos días de desarrollo es el camino crítico?
4. ¿Cuándo se ve la primera señal?
5. ¿Cuánto margen recupera y con qué supuestos?
