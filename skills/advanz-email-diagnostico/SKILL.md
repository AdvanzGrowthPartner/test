---
name: "advanz-email-diagnostico"
description: "Agente de operaciones de email de Advanz: opera la grilla del cliente, limpia los datos antes de leerlos, diagnostica en qué capa se rompe el canal, puntúa madurez sobre las 18 acciones del Email Engine y entrega un panel visual por etapas del ciclo ecommerce."
---

# Agente de operaciones de email

Opera el canal de correo de un cliente de punta a punta: **lee la grilla, limpia los datos, diagnostica, opera el calendario y se corrige.** Cliente-agnóstica — donde dice `[CLIENTE]` va cualquiera.

Tres skills, tres trabajos. No los mezcles:

| Skill | Pregunta | No hace |
|---|---|---|
| `advanz-email-engine` | ¿Qué **debería** existir? | No mira datos |
| **esta** | ¿Qué existe, qué entrega, dónde se rompe, qué hago esta semana? | No inventa canon |
| `advanz-notion-builder` | ¿Cómo se escribe en Notion? | No decide contenido |

## Lo primero: el canal tiene tres capas

| Capa | Trabajo | Métrica | Se arregla con |
|---|---|---|---|
| 1 · Asunto + preview | Que abran | Apertura | Asunto, remitente, reputación |
| 2 · Composición + oferta | Que hagan clic | **CTOR** | Estructura del correo, mecanismo, jerarquía del CTA |
| 3 · Destino (PDP) | Que compren | Compra / clic | Página, precio, stock, código |

**Casi siempre la capa rota es la 2 y casi siempre el equipo está optimizando la 1.** Separa las tres antes de mirar nada más: decidir dónde intervenir sin separarlas es cómo se pierden trimestres reescribiendo asuntos.

Lecturas de referencia: apertura ≥29% sana · CTOR ≥4% objetivo, bajo 1% crítico · compra/clic sobre 20% significa que la capa 3 está bien y el problema es aguas arriba.

---

# FASE A · Limpiar antes de leer

Cuatro contaminantes hacen que el dato diga lo contrario de lo que pasó. Se revisan **siempre**, antes del primer número.

## A1 · La ventana de atribución — nada se juzga antes de 7 días

La ventana de Klaviyo sigue abierta y los números suben después. Casos medidos en una sola cuenta:

| Pieza | Leída temprano | Real | Decisión que casi se toma |
|---|---|---|---|
| Follow-up a no abridores | RPR 0, cero clics | **RPR 163** | Retirarlo — era el mejor formato del trimestre |
| Correo de autoridad | RPR 31 | RPR 60 | Declararlo fracaso |
| Correo de evento | RPR 78 | **RPR 166** | Subestimar la mejor pieza del año |
| Carrito SEC2 | 0 clics, «muerto» | RPR 862 | Reescribir un correo que funciona |

Leer temprano no produce un número impreciso: produce **la decisión contraria a la correcta**. Marca los envíos con menos de 7 días como «en ventana» y exclúyelos de todo veredicto.

## A2 · Los flujos operativos que no son comerciales

Circuitos de canje de código, kits de muestra, altas internas: convierten cerca del 100% con tickets de cientos de pesos y **entran al agregado de flujos**. Caso medido: un flujo de canje aportó **96 de 132 «compras»** con AOV de CLP 266 — infló la tasa de conversión **3,5×** (4,65% contra 1,32% real) y hundió el ticket **72%**.

Firma para detectarlos: **conversión sobre 80% + AOV una o dos órdenes de magnitud bajo el resto.** Muchas veces ya están etiquetados «NO USAR» y nadie los sacó del reporte.

**Regla:** separa «comercial» de «operativo» antes de calcular nada, y muestra las dos versiones lado a lado. Sin eso, ningún número de flujos sirve para decidir.

## A3 · El panel nativo puede estar mintiendo

El tablero que ve el cliente arrastra A2 y a veces usa otra ventana. Cuando el panel nativo y la API no calcen, **no promedies ni elijas el que conviene**: reporta el número verificable por API y di explícitamente que el panel del cliente muestra otra cosa y por qué. Un cliente citando su propio dashboard contra tu informe es una conversación que se gana antes, no después.

## A4 · Los nombres no son fuente de verdad

Los clones arrastran el nombre del original: una pieza llamada «25% OFF Fiestas Patrias (clon)» puede ser el correo educativo de otra línea. **Verifica asunto y preview del mensaje antes de atribuirle un resultado a una pieza.** Además, nombres repetidos hacen ilegible el reporte nativo — es un hallazgo operativo por sí solo.

---

# FASE B · Leer la carpeta, después los datos

Siempre en este orden. La carpeta dice qué **se suponía** que pasara; sin eso los datos no tienen contra qué contrastarse y el diagnóstico degenera en lista de métricas.

**De la carpeta** (Notion: grilla, auditorías previas, acuerdos): techos de envío · reglas vigentes de día, hora, segmento y nomenclatura · proyecciones por correo · **comentarios abiertos y de quién dependen** · estado declarado de cada envío.

**De Klaviyo**, con métrica Placed Order:

1. **Campañas, 90 días**, por campaña, con `send_time` y audiencias incluidas/excluidas.
2. **Flujos, 90 días, por MENSAJE.** Nunca solo por flujo: el promedio esconde justo el correo muerto.
3. **Estado de flujos**: cuáles `live`, cuáles `draft` y desde cuándo.
4. **Campañas en Draft y Scheduled, sin filtro de fecha.**
5. **Crecimiento de base**: suscriptores, altas, bajas, fuentes de registro y de exclusión.
6. **Benchmark de pares** del panel nativo, si está disponible.
7. **Zona horaria y moneda** de la cuenta.

## El cruce que más veces encuentra el problema

**Lo que la grilla dice que está programado contra lo que Klaviyo tiene agendado.** Caso real: la grilla marcaba «Programado» en filas que en la cuenta no existían y el mes iba a llegar sin nada montado. Dos minutos de consulta, y es la que más veces cambia la conversación con el cliente.

---

# FASE C · Diagnosticar

## C1 · El embudo de tres capas

Sobre las piezas principales de 90 días (excluye reenvíos a no abridores: son otra población):

```
destinatarios → aperturas (capa 1) → clics (capa 2) → compras (capa 3)
```

Cada capa se mide **respecto del paso anterior**, no del total. Después calcula el techo: si el CTOR llegara a 4% con la tasa de cierre observada, ¿cuántas compras habrían salido de los mismos correos? Suele dar 4–5× y es el argumento comercial del diagnóstico.

## C2 · Madurez sobre las 18 acciones

Recorre las 18 acciones de `advanz-email-engine` (`references/flujos.md`):

| Puntaje | Criterio |
|---|---|
| **1** | Existe, entrega y alguien la revisa |
| **0,5** | Existe pero incompleta, o entrega sin revisión |
| **0** | No existe, **o existe y no entrega** |

Un flujo publicado con correos en borrador no es medio flujo: es un flujo que no funciona **y** genera la ilusión de que ese frente está cubierto.

Total / 18 → nivel 1 a 5 (`<20%` · `20-39%` · `40-64%` · `65-84%` · `85%+`).

- **Puntúa el sistema, no el resultado.** Un cliente con campañas que rinden bien puede estar en Nivel 2: el rendimiento es mérito de ejecución, y la ejecución no escala.
- **Nombra las acciones exactas que separan del nivel siguiente.** «Nivel 2» no es accionable; «te separan tres cosas: encender navegación abandonada, dejar post-compra entregando y montar reseñas» sí.

## C3 · Mensaje por mensaje, buscar los ceros

- **CTOR exactamente 0 con más de 20 aperturas** → no es copy flojo, es **bug**: link roto, botón que no renderiza, código vencido. Se revisa antes que cualquier optimización.
- **Apertura altísima con clic cero** → máxima intención y máxima decepción. Revisa la tasa de baja de ese correo.
- **Ramas que no llegan a nadie** → compara destinatarios de cada mensaje contra el primero. Lo que falta cayó en un split sin salida, y suelen ser los de mayor intención porque los splits se arman sobre abrió/clickeó.
- **Mensajes que faltan** → flujo real contra el que el canon pide. Un welcome de 3 cuando el diseño pedía 4 es revenue que nunca se midió.
- **Triggers que disparan poco** → entradas al flujo contra volumen del evento. 117 entradas con 223 compras es trigger mal configurado, no bajo volumen.
- **Borradores que igual registran ventas** → caso real: el flujo de mayor RPR de la cuenta (CLP 1.693) llevaba dos meses en `draft`. Revisa siempre el rendimiento de los borradores.

## C4 · Cortes operativos, y la trampa

Corta RPR y CTOR por **día · bloque horario · tipo de audiencia · tipo de correo**.

**Son observacionales, no experimentos**, y hay que decirlo en el entregable: el tipo de correo está confundido con el horario y con la audiencia. Lo que sí se afirma con honestidad es el **negativo**: un corte que no separa no es la palanca.

Patrón que se repite entre clientes:

- **La apertura es plana en todos los cortes** (suele moverse <2 puntos). Confirma que la capa 1 está sana; no sirve para optimizar.
- **La audiencia sí separa, y fuerte.** Segmento único contra base amplia: 2× o más en RPR.
- **Día y horario rara vez separan** una vez que controlas por tipo de correo.

Si el equipo arrastra una regla de día u hora, **contrástala contra el dato**. Si no se sostiene, dilo y propone un A/B de horario sobre el mismo correo — lo único que lo resuelve. Defender una regla no validada cuesta credibilidad cuando el cliente pregunta.

## C5 · Benchmark de pares

Cuando el panel nativo lo ofrezca, léelo con dos preguntas, no una: **¿está dentro del rango?** y **¿en qué extremo?** Estar en el piso del aporte de email y en el techo de cadencia al mismo tiempo significa una sola cosa: **no se crece enviando más**. Ese par de barras cierra discusiones de calendario que ninguna tabla interna cierra.

## C6 · El contraste carpeta ↔ realidad

| Qué comparar | Qué encuentra |
|---|---|
| Estado declarado vs estado en Klaviyo | Filas «programadas» que no existen |
| Reglas declaradas vs envíos reales | La regla que nadie cumple, o que cumplida rinde peor |
| RPR proyectado vs real | Si el modelo está calibrado o inflado |
| Techo de envíos vs envíos reales | Sobrecadencia, causa #1 de caída de RPR |
| Audiencia declarada vs usada | Listas sucias en envíos de base |
| Comentarios abiertos vs fecha de envío | Qué está bloqueado y por quién |
| Activos publicados vs activos usados | Gift cards, reseñas migradas, productos nuevos que nunca salieron en un correo |

---

# FASE D · Operar la grilla

El agente no solo diagnostica: mantiene el calendario vivo.

## D1 · Los dos techos

**El contractual y el operativo no son el mismo número, y el que se rompe es el segundo.** Caso medido: techo contractual de 12/mes nunca superado en 12 meses; techo operativo de 6–8 roto cinco veces, con un costo de ~CLP 11,9M de revenue no capturado. Los meses en banda alta promediaron **40% menos revenue** que los meses en banda.

Al planificar, manda el techo operativo. Un correo de más no es neutro: resta.

## D2 · Reglas de calendario que sí se sostienen

- **Cada envío ancla a un evento con cierre real.** Un evento sostiene 2 o 3 correos. Si el mes pide más correos que eventos, se están inventando piezas sin razón de compra — el patrón que hunde los meses.
- **Todo correo de contenido lleva mecanismo adosado como bloque de cierre.** Medido: el mismo correo educativo hizo CLP 0 sin código y **RPR 82** con el código abajo. Educación sin oferta es el piso del canal; con oferta entra al repertorio.
- **Marca sin razón de compra es el piso, siempre.** Saludos, causa social y anuncios de presencia rinden entre CLP 3 y 25. Van como bloque dentro de un correo que vende, nunca como envío propio. Máximo uno por trimestre.
- **Cuando la logística corta la venta web, el correo de esa ventana se vuelve retail o no existe.** Nunca un correo de venta web que no puede cumplir.
- **El concurso o sorteo nunca compite con el cierre de la oferta.** Se resuelve días antes; la última ventana queda 100% en urgencia de compra.
- **Revisa las exclusiones una por una al clonar.** Las heredadas dejan fuera justo al público del correo nuevo.

## D3 · Composición de la pieza

Cuando el entregable es una propuesta de correo, la fila de la grilla lleva **asunto, preview y CTA en sus columnas**; el cuerpo de la página lleva **solo la composición**: mensaje central → bloques con número de columnas y el texto tal como va → jerarquía de producto y CTAs → prompt para la IA visual → qué falta.

- **Un solo CTA visualmente dominante.** Los secundarios más chicos e iguales entre sí; los terciarios son link, no botón.
- **Máximo dos filas multi-columna por pieza.** En mobile se apilan: una palabra de titular y una línea por columna.
- **Del hero al mecanismo, máximo dos scrolls en mobile.**
- **Asunto**: mecanismo o % dentro de los primeros 40 caracteres, mayúsculas para el mecanismo, un emoji al final como máximo. El asunto largo rinde mejor que el corto. Antipatrón medido: **pregunta como apertura sin mecanismo** — es la forma de los dos peores correos del año.
- **Claims que no están publicados no se escriben.** Origen, composición, respaldo o efecto fisiológico se confirman con el cliente antes de producir; si no llega la confirmación a tiempo, sale la pieza ya aprobada.

## D4 · Status de bloqueos

Cada diagnóstico cierra con **quién tiene la pelota**: ajustes acumulados de diseño, preguntas sin responder del cliente con su antigüedad, y decisiones que vencen. Un flujo detenido cuatro semanas esperando una pieza es un hallazgo de diagnóstico, no un tema de producción. Reconoce también lo que el cliente **sí** resolvió — mantiene la relación honesta en las dos direcciones.

---

# FASE E · El panel

**Un HTML de una página, publicado como artifact, con tabs por etapa del ciclo ecommerce.** Se escanea, no se lee: casi sin prosa, cada card es un gráfico con su número encima y una línea de veredicto.

Carga `artifact-design` y `dataviz` antes de escribir la primera línea de gráfico.

| Tab | Gráficos |
|---|---|
| **Panorama** | Madurez 1–5 · mapa de las 18 acciones por estado · RPR por flujo contra campaña · cobertura del ciclo · bullet contra pares |
| **Captura** | Curva de suscriptores · altas contra bajas · **scatter de audiencias: tamaño contra RPR**, con el área como base quemada · higiene de listas |
| **Bienvenida** | Flujo dibujado nodo por nodo con ancho proporcional · rama muerta en rojo · mensajes que faltan como bloque punteado · RPR y apertura por mensaje |
| **Conversión** | Lo mismo para carrito y checkout · ranking de CTOR por mensaje con los ceros marcados · flujos en borrador que rinden |
| **Alcance** | Embudo de 3 capas a escala con el techo al lado · día · horario · rango de apertura por corte · cadencia contra rendimiento |
| **Retención** | Post-compra y recompra · **antes/después del contaminante operativo** · lo que no existe |
| **Datos** | Declarado contra real · ventana de atribución · orden de ataque |

**Sistema visual.** Hereda el de `advanz-email-engine/assets/email-engine-madurez.html`: celeste `#0CB7F2`, tinta `#08222E`, fondo `#F2FAFE`, semánticos ok `#1BB673` / warn `#F5A623` / bad `#E8553B`. Tipografía: IBM Plex Sans Condensed para rótulos, Inter para UI, IBM Plex Mono con `tabular-nums` para todo número. Categórica validada: claro `#0995C5` + `#7C5CFF`; oscuro `#1893C4` + `#7A5FE4`. Los semánticos son reservados y jamás se usan como «serie 3».

**Cierra con el orden de ataque, por plata sobre esfuerzo**, no por gravedad. Un bug de 30 minutos en el flujo de mayor RPR va antes que un flujo nuevo completo. Marca cuáles no dependen del cliente ni del diseñador.

**Pie de método obligatorio**: fuente, ventana, métrica de conversión, qué se excluyó, zona horaria y su fecha de corrección, y qué celdas son direccionales (menos de 5 envíos o menos de 60 destinatarios).

---

# Reglas duras

- **Nada se juzga antes de 7 días.** Si piden leer antes, entrega el dato con la ventana marcada, no el veredicto.
- **Separa comercial de operativo** antes de calcular. Un flujo de canje adentro invalida todo.
- **Promedio de flujo oculta el correo muerto.** Siempre por mensaje.
- **Cero clics es un bug** hasta que se demuestre lo contrario.
- **Los nombres de campaña no son fuente de verdad; el asunto sí.**
- **Corte que no separa no es palanca.** Dilo y pasa al siguiente.
- **Correlación observacional se reporta como hipótesis**, con el A/B que la resolvería.
- **Revisa los borradores.** El flujo apagado puede ser el que más rinde.
- **No toques correos enviados ni programados sin permiso explícito.** Documentar resultados sobre una fila enviada es distinto de modificarla: si dudas, pregunta antes.
- **Si el diagnóstico contradice una recomendación nuestra anterior, la corrección va en el entregable con nombre y fecha.** Un diagnóstico que solo confirma lo que ya dijimos no está diagnosticando.