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

### UX (no negociable)
- **Tema claro y aireado**, legible en light y dark (dark = slate, no negro). **Proteger marcos y rangos**: nada se sale de su caja; ejes con min/max declarados; contenedores con overflow controlado. Fechas y badges grandes; leyendas **laterales**, no bajo el gráfico.
- Todo interactivo es JS vanilla (sliders/calculadoras) o Chart.js; sin dependencias fuera del allowlist del Artifact.

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
