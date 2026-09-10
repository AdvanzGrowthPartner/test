# Artifact Spec — el preview visual de la campaña

El output central del skill es un **artifact HTML self-contained** que previsualiza la campaña y proyecta el resultado. Regla de oro: **cualquiera lo entiende en 60 segundos y ve dónde está la oportunidad y el foco de mayor leverage.** No es un dashboard de data — es un *preview de decisión*.

**TODO es una declaración visual** (no párrafos): cada bloque se muestra como gráfico, timeline, matriz, barra o semáforo — texto solo para el veredicto y las etiquetas. El objetivo es dar claridad de "cómo se ve" ANTES de activar. Se construye **recién después de las 8 respuestas del intake** (`intake.md`), nunca antes.

Construir con `web-artifacts-builder` (o `diagram-engine` para las piezas de mapa/matriz). Cargar `artifact-design` antes de escribir. Un solo archivo, responsive, theme-aware, sin dependencias externas fuera del allowlist.

### Piezas visuales obligatorias
- **Header "Análisis de marca → [URL]"** con las **variables analizadas** como chips (las 10 de la batería ecommerce en `intake.md`): facturación, AOV, zonas de mayor venta, avatar/recurrencia, colecciones, producto, canales, envío, tendencia, oportunidad/gap.
- **Cronograma en GANTT** (barras por fase de producción sobre un eje de fechas T-N → evento → post), no una lista.
- **Matriz de producto visual** con los 4 roles etiquetados: 🟢 **ganador** · 🔵 **sidekick (acompañamiento)** · 🟠 **fantasma** · ⚫ **zombie**.
- **Tendencia** ("dónde se mueve la tendencia"): curva/heat del evento pasado + estacionalidad de demanda, marcando el peak y el valle.
- **Estructura de oferta y campaña**: visual (tarjetas/arco), qué pack ancla, qué sube AOV, qué comunica cada fase.
- **Tiempo de preparación**: legible del propio Gantt (semáforo 🟢/🟡/🔴 del reloj).
- **Proyección**: rango visual (conservador/esperado/stretch) + confianza.

### Módulos ampliados (war room de campaña)
El output evolucionó de "preview" a **war room**: además de lo anterior, incluir cuando la data lo permita —
- **Gráficos combinados reales** (usar Chart.js UMD desde cdnjs, pinneado; temear leyendo las CSS vars):
  - *Tendencia*: **barras sesiones + barras ventas + línea CR%** (diario del evento pasado). El insight suele ser que el CR sube y el tráfico es plano.
  - *A quién le vendes vs conversión*: **barras (sesiones/ventas) + línea CR%** por dispositivo / segmento / canal.
- **Oferta irresistible (visual):** el mix como stack **ancla (bundle) → upsell de carrito → crosssell**, + una **matriz de test** (variante × hipótesis × métrica × qué ganó) para ver cómo testear antes del peak.
- **Proyección interactiva:** slider de **inversión media** + split Meta/Google + ROAS editable → **calcula revenue por canal (Google y Meta) y MER en vivo** (JS vanilla). Declarar que el ROAS es supuesto de planificación.
- **Calculadora de volumen de creativos:** slider de inversión + mezcla video/estático → **# de conceptos, videos (UGC/creador) y estáticos recomendados**, con la lógica de *volumen mínimo para que la plataforma distribuya* ("con poca plata no dispersar; con mucha, necesitas volumen real").
- **Distribución por rendimiento:** cómo repartir budget por canal pre‑evento vs peak, y la regla viva (+20% al que supera ROAS objetivo, 3x kill, proteger lo que funciona) → deriva a `ecomm-cyber-audit`.
- **Salida orgánica + email + anuncios:** playbook visual (qué avisar/postear/links; secuencia teaser→live→last + flujos carrito/browse/post‑compra; estáticos vs video UGC según inversión).
- **Landing de campaña `/cyber` (o `/black`):** medir tráfico y CR de la URL del evento por fuente, aislado del resto del sitio; base de retarget.

### UX (no negociable) — estética Shopify / Polaris
- **Look & feel tipo admin de Shopify (Polaris):** ground gris claro, cards blancas con borde sutil y radio ~12–14, verde marca #008060, tipografía Inter + IBM Plex Mono para datos. Claro y aireado; dark = slate, nunca negro. Si el usuario ofrece pantallazos de su Shopify, pedirlos para calibrar.
- **Header STICKY que funciona de índice:** barra fija arriba con anclas a cada sección (`#s1`…`#sN`) + `scroll-behavior:smooth` y `scroll-margin-top`. Permite saltar directo a cualquier punto.
- **Cards siempre "normal vs cyber":** cada métrica clave se muestra comparada — día normal → día evento + el multiplicador (facturación, órdenes, CR, AOV). El evento no sube el ticket: multiplica volumen y conversión.
- **Canales reales, no lumps:** nunca escribir "owned+search". Desglosar los canales que corren de verdad (Google, Meta [IG+FB], Directo/Marca, Orgánico, Email/Owned) con su revenue real y estado (corriendo / por conectar). Email suele caer en "directo" por falta de UTM → marcarlo.
- **Proteger marcos y rangos:** nada se sale de su caja; ejes con min/max; overflow controlado. Fechas y badges grandes; leyendas **laterales**.
- **Días del evento separados** (ej. 5 · 6 · 7, no "5–7") con su % esperado de venta por día.
- **Gantt con "qué definir / qué comunicar / qué asegurar / qué calentar"** desglosado en boxes, no solo la barra. Incluir la fase de **comunicación** (teaser/anticipo) y la de **retención** post-evento.
- **Productos con imágenes reales** vía MCP (Shopify `featuredImage`) en tabs (Ganadores / Colecciones). Si el proxy bloquea el CDN de Shopify (no se pueden bajar para embeber como data URI), usar placeholders y **pedir pantallazos** al usuario para incrustarlas.
- **Oferta con la lógica del porqué** (por qué el GWP, por qué el upsell, por qué el crosssell), visual, con imágenes de producto.
- **Proyección:** escenario del evento **fijo/normalizado** (no movible) + un **planificador de pauta interactivo** aparte (slider de inversión con tope realista — p.ej. $10M en cyber — que alimenta a TODOS los outputs siguientes, incluida la calculadora de creativos, sin re-mover). Meta = azul, Google = amarillo. Incluir **MER explicado con fórmula**, **ROAS medio sin evento / en eventos** (por validar si no hay data de ads), e **histórico real de eventos** (año, inversión, revenue, MER).
- **Volumen de creativos:** slider **video↔estático** (el video convierte mejor) enganchado a la MISMA inversión; # conceptos escala con presupuesto (volumen mínimo para que la plataforma distribuya).
- **Distribución por rendimiento:** barras **verticales agrupadas** (fase × canal), no barras laterales.
- **Salida = comportamiento del evento en el tiempo:** un flujo temporal (teaser→VIP→live→proof→last→cola) + orgánico/email/anuncios.
- **Landing `/cyber`:** **emular visualmente la página** (mock con barra de URL, hero, productos) + qué medir y por qué.
- Todo interactivo es JS vanilla o Chart.js (UMD desde cdnjs, pinneado); sin dependencias fuera del allowlist del Artifact.

### Refinamientos de detalle (aprendidos en cliente)
- **Fondo con aura de marca:** base clara con auras radiales suaves de los colores de la marca (Advanz) detrás del contenido (`body::before`, opacidad baja). Nunca compite con la data.
- **Gantt con rol + qué verificar por etapa:** cada fila del Gantt lleva su **rol** y su **checklist de verificación** inline; sin chips decorativos sueltos debajo. Barras grandes.
- **Oferta = AHORRO primero:** el héroe del mensaje es el ahorro (en sticks, en producto y en envío), no el precio bajo. El **GWP (regalo) va SIEMPRE atado al pack, nunca suelto** (regalar suelto = regalar margen). El carrito muestra precio tachado + "ahorras $X".
- **Proyección:** los supuestos (inversión/ROAS por escenario) van en una **mini-tabla lateral** que acompaña las barras, no en texto chico. Escenario tope = "todo sale bien" (no inflar; respetar el ROAS techo histórico de la cuenta).
- **Distribución de inversión conectada al planificador:** las barras de $ por fase se recalculan con el slider de inversión y el split (no valores hardcodeados); mostrar la referencia del evento anterior.
- **Landing con 3 vistas (home · PDP · carrito), las 3 obligatorias**, con **marcadores numerados flotantes** en el mock conectados por número (01, 02…) a la checklist de must-haves. Envío gratis y countdown visibles en las 3.
- **Checklist por área + por etapa:** 6 áreas (Producto y stock · Web & CRO · Social Media · Campañas · Email · Revisor final), cada una verificable pre/durante/post. Ver `event-checklist.md`.

---

## Encabezado (lo primero que se ve)

```
[Cliente] · [Evento] · [fecha del evento]
Veredicto en una línea: [hay ola fuerte, entramos con X / oportunidad media, entrada acotada / sin ola, always-on reforzado]
```
El veredicto sale del scoring (`leverage-scoring.md`). Es honesto y tosco, no vendedor.

---

## Las 6 secciones del preview

### 1. El reloj ⏱️ — ¿cuánto tiempo queda y alcanza?
- Timeline horizontal de HOY → evento, con los hitos de producción (`event-calendar.md`: oferta, tracking, lista, creativos, audiencias, warm-up, email, sitio) ubicados en su T-N.
- Semáforo del reloj: 🟢 holgado / 🟡 justo / 🔴 tarde (contra el lead-time mínimo de la vertical).
- Si es 🔴: banner claro "se entra tarde — alcance acotado a [X]".

### 2. Qué NO puede fallar 🚦 — el checklist tosco
Semáforo de los no-negociables de la vertical (`product-classification.md` §B):
| Ítem | Estado | Nota |
|------|--------|------|
| Tracking (pixel/CAPI/GA4/UTMs) | 🟢🟡🔴 | |
| Stock del/los ganador(es) | 🟢🟡🔴 | |
| Oferta y margen definidos | 🟢🟡🔴 | |
| Sitio/velocidad para carga | 🟢🟡🔴 | |
| [Ítem propio de la vertical: tallas / sets / stock depth] | 🟢🟡🔴 | |
Rojo aquí = riesgo directo a la campaña. Es lo que el consultor tiene que resolver antes.

### 3. Matriz de productos 🎯 — qué entra y con qué rol
- Matriz 2×2 **vistas × ventas** con los SKU ubicados y coloreados: 🟢 ganador / 🔵 acompañamiento / 🟠 fantasma / ⚫ zombie.
- Al lado, la lectura en texto: cuál es el hero, cuál sube AOV, qué fantasma vale la pena arreglar, qué se ignora.
- Marcar stock/margen del ganador (si no hay stock, badge de alerta).

### 4. Mix de canales 📡 — dónde está la plata rentable
- Barras del revenue histórico por canal en ese evento (o baseline): paid (Meta/Google/TikTok), owned (email/SMS), orgánico/directo.
- Marcar el canal más rentable y el de más volumen (no siempre el mismo).
- La recomendación de dónde poner el peso, con el porqué.

### 5. Mecánica de oferta 🏷️ — estacional vs always-on
- Cuál mecánica se recomienda (del scoring) y por qué, en una tarjeta.
- Si estacional: el arco de comunicación (teaser → live → midpoint → last-chance) sobre un mini-timeline.
- Recordatorio de la trampa de precios (Sernac/Knasta): descuento real.

### 6. Proyección 📈 — cómo se vería vs el último evento
Ver método abajo. Mostrar:
- **Rango:** conservador — **esperado** — stretch (barras o bullet), nunca número puntual.
- **vs último evento:** lift esperado sobre el histórico propio.
- **Por canal:** cuánto aporta cada uno en el escenario esperado.
- **Nivel de confianza** declarado (alto si hay histórico propio del mismo evento; bajo si es direccional).
- Los **supuestos** en texto (spend plan, stock, margen) — la proyección es tan buena como ellos.

---

## Cierre del artifact (no es sección de gráfico, es la bajada)

- **Los 3 movimientos de mayor leverage** (del scoring), cada uno con: qué, por qué (dato), impacto esperado, dónde/quién, esfuerzo, y plazo dentro del reloj.
- **Riesgos y no-negociables** en una línea cada uno.
- **Handoff explícito:** "esto es el preview; el consultor valida con el cliente; la ejecución en vivo la toma `ecomm-cyber-audit`."

---

## Método de proyección (lo más delicado — no equivocarse)

Extrapolar lineal está **mal**: las ventas de evento no son uniformes.

**Fórmula (curva de pacing):**
`Total proyectado = ventas acumuladas ÷ % esperado acumulado a esa altura`

**Insumos, en orden de preferencia:**
1. **Curva del propio cliente en el mismo evento anterior** (Shopify, `data-pull.md` §1a) — lo único que captura su patrón real. Confianza alta.
2. **Curva direccional del evento** (`event-calendar.md`) si no hay histórico propio. Declararla como direccional. Confianza baja/media.

**Ajustes obligatorios:**
- **Ola de búsquedas:** si la demanda de la categoría viene fuerte/débil este año, ajustar el esperado.
- **Fecha dentro del mes:** evento post-sueldo → menos conservador; pre-sueldo → más conservador (`event-calendar.md`).
- **Por canal, distinto:** paid escala con el spend que se *va a desplegar* (no con el ritmo actual); owned (email/SMS) es pulsado — sube en cada envío (live/midpoint/last-chance); orgánico/directo surfea la ola.

**Reglas de honestidad:**
- Siempre **rango**, nunca número puntual. Error alto si el histórico es pobre (±25-35%).
- Declarar **confianza** y **supuestos**.
- Si falta una fuente, decirlo en la sección (“Meta no conectado — paid proyectado sobre spend plan × ROAS histórico”). No inventar.

*(Patrón heredado y ampliado de `ecomm-cyber-audit/references/owner-view.md`.)*

---

## Variante Notion (si el consultor la pide)

Si piden dejarlo como página editable para el equipo, volcar el mismo contenido con `advanz-notion-builder` (TL;DR → Mermaid horizontal → secciones escaneables → toggles). El artifact HTML es el preview visual; Notion es el registro editable. Ambos comen de la misma lectura.

---

## Qué NO hacer en el artifact
- No convertirlo en un dashboard de métricas sin bajada. Cada sección apunta a una decisión.
- No mostrar proyección puntual sin rango/confianza.
- No incluir SKU zombie como si fueran opción.
- No prometer ejecución — el artifact previsualiza, no ejecuta.
