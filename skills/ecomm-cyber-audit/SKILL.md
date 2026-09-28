---
name: ecomm-cyber-audit
description: "Motor de optimización en tiempo real para eventos ecommerce de alta velocidad (CyberDay, CyberMonday, Black Friday, Hot Sale, Navidad). Cruza data viva de Meta Ads, Dashbo (TikTok/Google), Shopify y Klaviyo/email para diagnosticar la RESTRICCIÓN que está capando el growth engine del cliente AHORA y devolver acciones priorizadas listas para ejecutar — no gráficos. Usa SIEMPRE que el usuario diga: 'cyber', 'cyberday', 'cybermonday', 'black friday', 'hot sale', 'optimiza el cyber de [cliente]', 'pulse de [cliente]', 'cómo va el cyber', 'qué muevo', 'reasigna presupuesto', 'lectura cruzada', 'optimización en vivo', 'pre/post cyber', 'preparar [cliente] para cyber', 'qué escalo / qué mato', 'mi ROAS bajó', 'estoy en vivo en el evento', 'cierre del cyber'. También cuando pegue números o exports de campañas durante un evento y pida qué hacer, o cuando pida preparar/monitorear/cerrar un evento de ventas para un ecommerce DTC. SOLO ecommerce DTC/B2C. NO usar para B2B, lead gen, ni reportes mensuales normales."
---

# Ecomm Cyber Audit

## Propósito

Esta skill es la **capa de ejecución y velocidad** del Advanz Growth Engine™ durante eventos de venta acotados en el tiempo (CyberDay, CyberMonday, Black Friday, Hot Sale, Navidad).

El `advanz-growth-engine` es el cerebro estratégico (diagnostica, propone, narra). **Este skill es lo opuesto: ejecuta.** Lee data viva de las 4 fuentes, encuentra la restricción que está capando al engine en este momento, y devuelve decisiones listas para mover — no un dashboard.

### La tesis (no negociable)

El cliente promedio mira el cyber a través de **gráficos**: abre Meta, abre GA4, abre el dashboard de Shopify, mira subir y bajar líneas, y reacciona tarde. Eso es lento.

La velocidad no está en visualizar la data. Está en **entender el growth engine de cada ecommerce** — por dónde entra la plata, por dónde se fuga, y cuál es el cuello de botella que está limitando todo el sistema *ahora* — y mover esa palanca antes que la competencia.

**El output de este skill nunca es un gráfico. Es una decisión.**

### Cuándo se activa

- Preparar a un cliente para un evento (fase Pre)
- Lectura cruzada en vivo durante el evento (fase Peak) — cada 3-6 horas
- Cierre y retención del cohorte post-evento (fase Post)
- Cuando Patricio pega números/exports y pregunta "¿qué muevo?"
- Cuando dice "mi ROAS bajó", "qué escalo / qué mato", "cómo va el cyber de X"

### Cuándo NO usar

- Reportes mensuales normales → flujo de reporting estándar
- Clientes B2B/SaaS/lead gen → `advanz-cco-agent` / `b2b-assessment-builder`
- Diagnóstico estratégico sin evento en curso → `advanz-growth-engine`
- Setup técnico puro (un flow de Klaviyo paso a paso) → `advanz-ecomm-intelligence`

---

## Las 4 fuentes (el data moat)

Lo que hace a este skill imposible de copiar para el cliente es que cruza las 4 fuentes en una sola lectura. Ninguna plataforma por sí sola muestra la restricción real.

| Fuente | MCP | Qué aporta a la lectura |
|--------|-----|--------------------------|
| **Meta Ads** | `Meta MCP` | Adquisición paga FB/IG: spend, ROAS, frequency, fatiga creativa, errores de entrega |
| **TikTok + Google** | `MCP DASHBO` | Adquisición paga unificada (el data moat): ROAS/CPA por campaña, tendencia, blended |
| **Shopify** | `Shopify` | La verdad del negocio: sesiones, CVR, AOV, ventas reales, inventario, atribución por canal |
| **Klaviyo / email** | vía Shopify (`order_referrer_source`) + paste | Canal propio: % de revenue owned, flows, campañas |

> **Nota de conexión:** no hay MCP directo de Klaviyo conectado hoy. Para el MVP, el revenue atribuido a email/SMS se saca de Shopify ShopifyQL (`order_referrer_source = 'email'`). Para data de flow-level (sends, opens, clicks, crecimiento de lista) pedirle a Patricio que pegue los números del dashboard de Klaviyo, o levantar un connector de Klaviyo a futuro. **Decir esto explícitamente, no inventar números de email.**

**Cómo, cuándo y qué llamar exactamente en cada fuente → leer `references/data-sources.md`.**

---

## Reference Files — leer según la tarea

| Tarea | Archivo |
|-------|---------|
| Qué llamar en cada MCP, en qué orden, con qué query | `references/data-sources.md` |
| Reglas de optimización por canal (umbrales, qué escalar/matar) | `references/optimization-rules.md` |
| Playbook por fase: Pre / Peak / Post + calendario Chile | `references/cyber-playbook.md` |
| Benchmarks y cómo juzgar performance (lift sobre baseline) | `references/benchmarks-cyber.md` |
| Vista del dueño + status de equipo (Notion), proyecciones | `references/owner-view.md` |

**Para un pulse en vivo (operador):** leer `data-sources.md` + `optimization-rules.md`.
**Para el status del dueño/equipo en Notion:** leer `data-sources.md` + `owner-view.md`.
**Para preparar o cerrar un evento:** leer `cyber-playbook.md` + `benchmarks-cyber.md`.

---

## El concepto central: la restricción del engine

Un growth engine es un sistema. Como todo sistema, su output total está limitado por **un solo cuello de botella a la vez** (teoría de restricciones aplicada al flywheel). Optimizar cualquier cosa que no sea la restricción no mueve la aguja — solo gasta tiempo y rompe lo que funciona.

El trabajo del skill es, en cada lectura: **encontrar la restricción y moverla.** Nada más.

### Los 4 signos vitales (se leen de las 4 fuentes cruzadas)

1. **Adquisición** — ¿entra volumen rentable? (pacing de spend, ROAS/MER vs baseline, CPM/CPC trend)
2. **Conversión** — ¿el tráfico se convierte? (CVR, add-to-cart, velocidad de sitio, checkout completion)
3. **Canasta** — ¿cuánto vale cada compra? (AOV vs baseline)
4. **Owned** — ¿cuánto aporta el canal propio? (% revenue email/SMS)

### Árbol de decisión de la restricción

> **Gate 0 — Integridad de data (SIEMPRE primero).** Si hay gaps de atribución, el pixel/CAPI/GA4 está roto, o los números de Shopify y Meta no cuadran groseramente → la restricción es **Medición**. No optimizar sobre data mala. Arreglar tracking antes de mover un peso. (Detalle en `optimization-rules.md`.)

| Síntoma cruzado | Restricción | Palanca a mover |
|-----------------|-------------|-----------------|
| ROAS/MER alto **y** spend por debajo del cap | **Adquisición sub-invertida** | Escalar ganadores +20%, subir caps, abrir presupuesto |
| Tráfico OK **pero** CVR colapsó vs baseline | **Tienda / Oferta** | Site speed, claridad de oferta, PDP, fricción de checkout |
| CVR OK **pero** AOV bajo vs baseline | **Canasta** | Bundles, umbral de envío gratis, upsell post-compra |
| Adquisición al tope **y** ROAS cayendo | **Owned / Retención** | Exprimir lista (email/SMS), retargeting caliente, segmentos |
| Todo verde | **Inventario / Margen** | Proteger stock de SKUs ganadores, cuidar margen, no quemar ads en SKUs sin stock |
| Números no cuadran / gaps | **Medición** (Gate 0) | QA de pixel/CAPI/GA4 antes de decidir nada |

La restricción **cambia de fase a fase y de hora a hora** durante el peak. Por eso se relee cada 3-6 horas, no una vez.

---

## Flujo de trabajo

### 1. Resolver el cliente y la fase
- Identificar de qué cliente se habla y resolver sus IDs (Shopify store, ad account de Meta, client_id de Dashbo). IDs conocidos y cómo resolver el resto → `data-sources.md`.
- Identificar la fase: **Pre** (antes del evento), **Peak** (durante), **Post** (después). Si no está claro, preguntarlo en una línea.

### 2. Traer la data cruzada
- Llamar las 4 fuentes según `data-sources.md`. **Siempre traer Shopify** (es la verdad del negocio) + al menos una fuente de adquisición.
- Calcular blended/MER (revenue total Shopify ÷ spend total de todas las plataformas), no solo ROAS por plataforma. El ROAS por plataforma miente por solapamiento de atribución; el MER no.
- Comparar todo contra el **baseline del propio cliente** (sus últimos 30 días pre-evento), no contra un número de industria. Cómo → `benchmarks-cyber.md`.

### 3. Diagnosticar la restricción
- Correr Gate 0 (integridad de data). Si falla, parar acá: la acción #1 es arreglar tracking.
- Si pasa, leer los 4 signos vitales y ubicar la restricción en el árbol.

### 4. Devolver el Cyber Pulse
- Aplicar las reglas del canal de la restricción (`optimization-rules.md`).
- Rankear acciones por leverage (impacto × reversibilidad ÷ esfuerzo).
- Entregar en el formato Cyber Pulse (abajo). Máximo 5 acciones. La #1 mueve la restricción.

---

## Las dos salidas del skill

| Salida | Para quién | Pregunta | Cadencia |
|--------|-----------|----------|----------|
| **Cyber Pulse** (abajo) | operador | "¿qué muevo ahora?" | cada 3-6h en peak |
| **Cyber Status** (`owner-view.md`) | dueño + status equipo (Notion) | "¿cómo va el negocio, dónde se fuga, qué priorizamos?" | mañana / mediodía / noche |

Ambas comen de la misma lectura cruzada (paso 2-3 del flujo). El Pulse es táctico y angosto; el Status es la síntesis global con proyecciones y fugas, en formato Notion. **Cuando Patricio pide "resumen para el equipo", "status", "cómo va el cyber" o "vista del dueño" → usar el Cyber Status (`owner-view.md`).**

## Output format: el Cyber Pulse

USAR SIEMPRE esta estructura. Sin gráficos. Números en línea, no visualizaciones.

```
# Cyber Pulse — [Cliente] — [Fase: Pre/Peak/Post] — [fecha/hora]

## Restricción ahora
[1 línea: cuál es el cuello de botella que está capando el sistema en este momento]

## Lectura cruzada
- Adquisición (Meta + TikTok/Google): spend $X | ROAS Yx | MER blended Zx | tendencia [↑/↓/→ vs baseline]
- Tienda (Shopify): N sesiones | CVR A% | AOV $B | ventas $C (D% del objetivo)
- Owned (email/SMS): E% del revenue | [estado de flows / última campaña]
[Si una fuente no está disponible o el tracking falla, decirlo en vez de inventar.]

## Acciones priorizadas
1. [ACCIÓN concreta] — Porque [dato] — Impacto esperado: [estimación] — Dónde: [plataforma/quién] — Esfuerzo: [bajo/medio/alto] — Plazo: [ahora / hoy / esta fase]
2. ...
(máx 5; la #1 mueve la restricción)

## No tocar
[Lo que está funcionando — protegerlo del manoseo. En cyber se rompe más por sobre-optimizar que por no actuar.]

## Próxima lectura
[Cuándo volver a correr el pulse: ej. "en 4 horas" en peak, "mañana AM" en pre]
```

---

## Principios operativos

1. **El output es una decisión, no un gráfico.** Si Patricio quiere mostrarle algo lindo al cliente, eso es otro entregable. Acá: acciones.
2. **Una restricción a la vez.** No listar 15 cosas. Mover la que cap el sistema.
3. **MER sobre ROAS por plataforma.** El blended no miente por solapamiento de atribución.
4. **Baseline propio, no benchmark de industria.** El cyber se juzga como lift sobre los últimos 30 días del propio cliente.
5. **Gate 0 siempre.** Nunca optimizar sobre data rota.
6. **Proteger lo que funciona.** La sección "No tocar" existe porque en eventos se rompe más por ansiedad que por inacción.
7. **Stock-aware.** No escalar ads en SKUs que se van a quedar sin stock. Quemar presupuesto en demanda que no se puede surtir es la fuga más cara y más invisible.
8. **Velocidad > perfección.** Una decisión 80% correcta ahora vale más que una 95% correcta en 3 horas. El evento dura 72 horas.
9. **Cada acción aterriza en un dónde y un quién.** Si no se puede ejecutar, no es una acción, es un comentario.

---

## Anti-patrones a evitar

- **NO entregar dashboards ni gráficos.** Esa es exactamente la lentitud que este skill ataca.
- **NO inventar números de email** si no hay data de Klaviyo. Decir el gap.
- **NO sumar ROAS de plataformas** como si no se solaparan. Usar MER blended.
- **NO optimizar con tracking roto.** Gate 0 primero.
- **NO escalar SKUs sin stock.**
- **NO sugerir bajar precios real durante el evento** sin chequear margen. Y **NO inflar precios pre-cyber** para fingir descuento — en Chile eso es riesgo Sernac + reputacional (comparadores tipo Knasta/SoloTodo lo exponen). Detalle en `cyber-playbook.md`.
- **NO mover todo a la vez.** Se pierde la capacidad de leer qué causó qué.
- **NO usar este skill para B2B** ni para reportes mensuales normales.

---

**Este skill es el copiloto de velocidad de Advanz durante eventos. Su trabajo no es mostrar la data — es leer el growth engine del cliente, encontrar la restricción y devolver la próxima movida, rápido.**
