---
name: ecomm-event-radar
description: "Radar de anticipación y previsualización de campañas para eventos comerciales de ecommerce DTC — CyberDay, CyberMonday, Black Friday, Hot Sale, Navidad, Día de la Madre/Padre, San Valentín, 18/Fiestas Patrias, liquidaciones y eventos propios. ARRANCA preguntando (sitio/marca, qué evento, ambición, presupuesto, productos y capacidad de ejecución) y confirma la fecha y duración del evento por web ANTES de traer data. Recién ahí se conecta por MCP (Shopify + volumen de búsquedas + Meta), lee peaks pasados, fuentes de tráfico y comportamiento de productos, clasifica el catálogo (ganador/acompañamiento/fantasma/zombie) y la vertical (moda/consumible/skincare), fija fechas y cuánto tiempo de anticipación queda, distingue venta estacional (descuento, urgencia, remate) de always-on, detecta la oportunidad y el mayor leverage, y arma un ARTIFACT visual que previsualiza la campaña y proyecta el resultado vs el último evento. NO ejecuta — previsualiza y entrega una primera estrategia para que el consultor la apruebe. Usa SIEMPRE que digan: 'prepara el cyber/black/navidad de [cliente]', 'qué evento se viene', 'nos alcanza el tiempo', 'cuánto me queda para [evento]', 'previsualiza la campaña', 'arma la estrategia de [evento]', 'proyecta el [evento] vs el año pasado', 'qué productos meto', 'qué canales muevo', 'dónde está la oportunidad', 'hay leverage para [evento]', 'me conviene entrar', o cuando peguen una URL de tienda y pidan planear un evento. Entra ANTES del evento; la ejecución EN VIVO durante el evento → ecomm-cyber-audit. SOLO ecommerce DTC/B2C — NO B2B, SaaS ni lead gen."
---

# Ecomm Event Radar

## Propósito

Esta skill es la **capa de anticipación y previsualización** de campañas para eventos comerciales de un ecommerce DTC. Su trabajo es *adelantarse*: leer el growth engine del cliente por MCP **antes** del evento, detectar dónde está la oportunidad y el mayor leverage, y devolver un **preview visual** de cómo se vería la campaña más una **proyección basada en el último evento** — para que el consultor decida si va o no.

No es solo "cyber". Entiende **el año completo de eventos** y cómo se comporta cada uno según su fecha, su estacionalidad y su posición dentro del mes.

### La división de trabajo (no confundir con `ecomm-cyber-audit`)

| | **`ecomm-event-radar`** (este skill) | **`ecomm-cyber-audit`** |
|---|---|---|
| Momento | ANTES del evento (T-60 a T-1) | DURANTE el evento (peak, cada 3-6h) |
| Pregunta | ¿Me conviene? ¿Con qué? ¿Cuánto tiempo me queda? ¿Cómo se vería? | ¿Qué muevo AHORA? |
| Output | **Artifact visual de preview + proyección + primera estrategia** | Decisión táctica en texto (Cyber Pulse) |
| Naturaleza | Estratégica, anticipatoria, visual | Ejecutora, en vivo, sin gráficos |

**Este skill produce el plan y el preview. Cuando arranca el evento, la ejecución pasa a `ecomm-cyber-audit`.** Dilo explícitamente al cerrar: "esto es el preview; cuando arranque, lo optimizamos en vivo con el otro motor".

### La tesis

El cliente promedio decide un evento a último minuto, mete el catálogo entero con el mismo descuento, y prende ads sin saber si hay oportunidad real. Eso quema margen y tiempo.

El leverage no está en "hacer la campaña". Está en **entender, antes de moverse, si hay una ola que surfear** — cuándo llega el peak de demanda de esa categoría, qué producto la traccciona, qué canal la convierte rentable, y cuánto tiempo de producción queda — y **previsualizar** esa campaña para que el consultor la apruebe con criterio, no con fe.

**El output central de este skill es un artifact visual donde cualquiera ve, en 60 segundos, dónde está la oportunidad y en qué enfocarse con mayor leverage.**

### Qué NO hace (límites duros)

- **NO ejecuta.** No crea campañas, no manda correos, no aprueba presupuesto, no crea descuentos en Shopify. Solo previsualiza, proyecta y sugiere.
- **NO reemplaza al humano.** El consultor lidera con el cliente hasta validar. Este skill entrega la **primera estrategia base**; el sí/no y el cierre humano son del consultor.
- **NO inventa data.** Si una fuente no está conectada o no responde, lo dice y guía cómo conectarla. Nunca proyecta sobre números inventados.
- **NO es para B2B / SaaS / lead gen.** Solo ecommerce DTC/B2C.

---

## Fase 0 — Preparación / Intake (SIEMPRE lo primero, antes de tocar data)

**El skill pregunta antes de traer data o construir nada.** Nunca asume la marca, el evento ni el alcance; nunca abre con Shopify. Traer la data por MCP y proyectar es caro — primero se cierra el encargo con el cliente/consultor para que tenga certeza de qué se requiere, y recién con eso se sale a buscar la información y se levanta el brief.

Preguntar (agrupado, no de a una) los 4 bloques del intake:
- **A · Qué y dónde:** ¿qué sitio/marca/URL? ¿qué evento (Cyber, Black, Hot Sale, Navidad, propio…)? → apenas se nombra el evento, **confirmarlo por web** (nombre oficial, fechas y duración aproximada) y devolverlo: *"se viene [evento], ~N días, del X al Y — ¿es este?"*.
- **B · Ambición:** ¿con cuánto quieres participar / cuál es la proyección u objetivo? ¿presupuesto aprox a invertir?
- **C · Munición:** ¿tienes los productos declarados o los detecto del catálogo? ¿qué capacidad de ejecución hay (enviar correos, mover anuncios, mover el sitio, creativos, stock)?
- **D · Conexiones:** inventariar qué conectores MCP hay (Shopify, Meta, Google, Klaviyo, Ahrefs/Semrush…) y usar lo que haya; lo que falte se declara como gap.

Cerrar la Fase 0 con un **mini‑resumen del encargo** para que el cliente confirme *antes* de gastar en el pull. Solo tras el OK (o si el usuario ya dio todo y pidió avanzar) se corre el Gate 0 y el pull.

**El detalle de las preguntas, cómo confirmar el evento por web y el formato del resumen → `references/intake.md`.**

---

## Gate 0 — Conexión MCP (tras el intake, exigente pero guiando)

Este skill vive de la data viva. Sin al menos Shopify conectado, es opinión, no radar.

1. **Verificar conexión Shopify:** llamar `mcp__Shopify__get-shop-info`. Si responde → tienda conectada, seguir. Si falla → **no es un alto seco, pero se exige**: decir en una línea "necesito la tienda del cliente conectada por MCP para leer sus peaks y su catálogo real; conéctala (o pásame la URL + acceso) y seguimos" y guiar el paso. No inventar el análisis sin ella.
2. **Fuentes complementarias (mejoran la lectura, no bloquean):** volumen de búsquedas (Ahrefs / Semrush) para anticipar el peak de demanda de la categoría; Meta Ads para el comportamiento paga pasado. Si no están, seguir con Shopify y marcar el gap.

**Detalle de qué llamar, en qué orden y con qué query → `references/data-pull.md`.**

---

## Reference Files — leer según la tarea

| Tarea | Archivo |
|-------|---------|
| Preguntas del intake, cómo confirmar el evento por web, formato del resumen del encargo | `references/intake.md` |
| Calendario anual de eventos, fechas, estacionalidad, cómo la posición-en-el-mes cambia el comportamiento, mecánica y ventana de lead-time por evento | `references/event-calendar.md` |
| Qué llamar en cada MCP (Shopify, Ahrefs/Semrush volumen, Meta), en qué orden, con qué query; chequeo de conexión | `references/data-pull.md` |
| Clasificación de productos (ganador / acompañamiento / fantasma / zombie) y de vertical (moda / consumible / skincare / otros), con cómo calcularla | `references/product-classification.md` |
| Cómo puntuar oportunidad y leverage; estacional vs always-on; regla "siempre propone algo"; preguntas de discovery al consultor | `references/leverage-scoring.md` |
| Especificación del artifact visual de preview + cómo construirlo | `references/artifact-spec.md` |

**Para previsualizar/planear un evento (flujo completo):** leer los 5.
**Para solo entender qué evento se viene y si hay ola:** `event-calendar.md` + `leverage-scoring.md`.
**Para solo clasificar el catálogo:** `data-pull.md` + `product-classification.md`.

---

## El flujo de trabajo

### 0. Intake — preguntar antes de traer data
Correr la Fase 0 (arriba / `intake.md`): sitio, evento (+confirmación web de fechas y duración), ambición, presupuesto, productos, capacidad de ejecución y conectores disponibles. Cerrar con el resumen del encargo y confirmar. **No pasar a traer data sin esto.**

### 1. Resolver evento, cliente y reloj
- Con el evento confirmado por web, **calcular el reloj:** días hasta el evento (T-N) y contrastar con la ventana de lead-time mínima de la vertical (`event-calendar.md`). Define si se llega holgado, justo o tarde — y el flujo de producción posible.
- Resolver la tienda por MCP (Gate 0).

### 2. Leer la historia por MCP
- **Shopify (la verdad):** peaks pasados del mismo evento (curva hora/día), ventas, AOV, CVR, fuentes de tráfico (`order_referrer_source`), catálogo y comportamiento de cada SKU. → `data-pull.md`.
- **Volumen de búsquedas (la ola que viene):** cuándo sube la demanda de la categoría cada año — para saber con cuánto tiempo adelantarse. → `data-pull.md`.
- **Meta (comportamiento paga pasado):** qué campañas/creativos rindieron en eventos previos, si está conectado.

### 3. Clasificar catálogo y vertical
- Definir la vertical (moda / consumible / skincare / otros) — cambia la mecánica, el lead-time y qué no puede fallar. → `product-classification.md`.
- Clasificar cada producto: **ganador** (tracciona, con stock y margen), **acompañamiento** (sube AOV / bundle), **fantasma** (vistas sin venta — problema de oferta/ficha), **zombie** (ni vistas ni ventas — no gastar en él). → `product-classification.md`.

### 4. Detectar oportunidad y leverage
- ¿Hay ola de demanda? ¿Hay producto ganador con stock y margen para descontar? ¿Hay canal rentable para empujarlo? ¿Alcanza el tiempo?
- Puntuar el leverage (impacto × probabilidad ÷ esfuerzo/tiempo). Distinguir mecánica **estacional** (descuento profundo, urgencia, remate) vs **always-on** (precio plano). → `leverage-scoring.md`.
- **Regla dura: siempre proponer un movimiento.** Aunque la oportunidad sea débil, entregar un plan mínimo viable (p. ej. always-on reforzado o entrada acotada a un solo ganador) y **marcar el riesgo explícito**. Nunca devolver un no-go seco — sí devolver "entrada chica + por qué" cuando no hay ola.

### 5. Hacer las preguntas de discovery al consultor
Antes de cerrar la estrategia, preguntar lo que la data no dice (ver lista en `leverage-scoring.md`): qué se vendió la vez pasada y qué campaña funcionó, si hay presupuesto aprobado y de cuánto, qué stock real se puede comprometer, qué margen tolera descuento, qué no se puede repetir del evento anterior.

### 6. Entregar el preview
- Construir el **artifact visual** (`artifact-spec.md`): reloj/lead-time, semáforo de "qué no puede fallar", matriz de productos, mix de canales rentables, mecánica de oferta, y **proyección vs último evento** (rango conservador/esperado/stretch, con nivel de confianza).
- Cerrar con la **primera estrategia en una línea** + los 3 movimientos de mayor leverage, y el handoff: el consultor valida con el cliente; la ejecución en vivo la toma `ecomm-cyber-audit`.

---

## Cómo proyectar (lo más delicado)

Extrapolar lineal está mal — las ventas de evento no son uniformes.

- **Mejor insumo:** la curva del **propio cliente en el mismo evento del año/edición anterior** (Shopify histórico). Si existe, usarla.
- **Si no hay histórico propio:** usar la curva direccional del evento (`event-calendar.md`) y **declararla como direccional**.
- **Ajustar por la ola de búsquedas** y por la fecha dentro del mes (posición vs ciclo de pago — ver `event-calendar.md`).
- **Siempre entregar rango** (conservador / esperado / stretch) + **nivel de confianza**, nunca un número puntual. Proyectar **por canal** distinto: paid escala con el spend que se *va* a desplegar; owned (email/SMS) es pulsado por envío; orgánico surfea la ola.

Método y reglas completas → `references/artifact-spec.md` (sección Proyección) y el patrón heredado de `ecomm-cyber-audit/owner-view.md`.

---

## Handoffs (este skill no ejecuta — deriva)

| Necesidad | A dónde |
|-----------|---------|
| Ejecutar/optimizar el evento EN VIVO | `ecomm-cyber-audit` |
| Producir la cadencia de email/SMS del evento | `advanz-email-engine` |
| Diagnóstico estratégico integral del engine | `advanz-growth-engine` |
| Decidir leverage macro (construir vs invertir, esperar vs actuar) | `leverage-decision-engine` |
| Dejar el plan como página editable para el equipo | `advanz-notion-builder` |
| Construir el artifact HTML con solidez | `web-artifacts-builder` / `diagram-engine` |

---

## Principios operativos

1. **Preguntar antes de traer data.** Primero el intake (Fase 0): sitio, evento, ambición, presupuesto, productos, capacidad, conectores. El pull por MCP es caro y va después del OK del encargo. Nunca abrir con Shopify ni construir el artifact sin intake.
2. **Adelantarse es el producto.** El valor está en leer la ola antes de que llegue, no en reaccionar. Si el skill entra tarde, decirlo con todas sus letras (el reloj manda).
3. **Previsualizar, no ejecutar.** Este skill nunca aprieta un botón. Entrega un preview y una proyección; el humano cierra.
4. **Siempre proponer un movimiento.** Aunque la ola sea débil: entrada chica + riesgo marcado. Nunca un no-go seco.
5. **Tosco con el margen y el tiempo.** No romantizar. Si un producto es zombie, no entra. Si no hay stock, no se empuja. Si no hay margen para descuento, no se descuenta — se hace always-on.
6. **Baseline propio, no benchmark de industria.** El evento se proyecta como lift sobre el propio histórico del cliente.
7. **La fecha importa tanto como el evento.** Un evento a fin de mes (post-sueldo) no se comporta como uno a mediados. Ajustar mecánica y proyección por eso.
8. **Vertical primero.** Moda, consumible y skincare tienen lead-times, mecánicas y "qué no puede fallar" distintos. Definir la vertical antes de sugerir nada.
9. **El artifact se entiende solo.** Cualquiera debe ver dónde está la oportunidad y el foco de mayor leverage sin explicación.
10. **La data manda; el gap se declara.** Si falta una fuente, se dice y se guía a conectarla. Nunca proyectar sobre inventos.

---

## Anti-patrones a evitar

- **NO construir el brief/artifact ni traer data antes del intake.** Preguntar primero (Fase 0); el pull va después del OK del encargo.
- **NO asumir la marca ni las fechas del evento.** Confirmar el evento por web siempre.
- **NO ejecutar nada** (crear campañas, correos, descuentos, aprobar budget). Solo preview.
- **NO meter el catálogo entero al evento.** Entran ganadores + acompañamiento; fantasmas se arreglan o quedan fuera; zombies nunca.
- **NO proyectar lineal** ni entregar número puntual sin rango y sin confianza.
- **NO inventar números** de una fuente no conectada. Declarar el gap y guiar.
- **NO inflar precios antes del evento** para fingir descuento (riesgo Sernac + comparadores Knasta/SoloTodo). El descuento es real o no es.
- **NO tratar todos los eventos igual.** Ajustar por fecha, estacionalidad y posición en el mes.
- **NO devolver un no-go seco.** Siempre hay un movimiento mínimo; marcar su riesgo.
- **NO usar este skill EN VIVO durante el evento** → ese es `ecomm-cyber-audit`.
- **NO usarlo para B2B / SaaS / lead gen.**

---

**Este skill es el radar de Advanz: se adelanta al evento, lee el engine del cliente por MCP, encuentra la ola y el leverage, y devuelve un preview visual + una proyección para que el consultor decida. Prepara y previsualiza — no ejecuta.**
