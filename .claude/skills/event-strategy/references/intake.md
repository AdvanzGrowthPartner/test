# Fase 0 — Preparación / Intake (antes de tocar data)

**Regla dura: el skill pregunta ANTES de traer data o construir nada.** Traer la data por MCP y proyectar es caro (llamadas, tiempo, "avería" tipo API/Python). Primero se cierra el encargo con el cliente/consultor para que tenga certeza de qué se requiere; recién con eso se sale a buscar la información y se levanta el brief.

Nunca asumir la marca, el evento ni el alcance. Nunca abrir con Shopify. Se abre con preguntas.

---

## El orden

```
Intake (preguntas) → Confirmar evento por WEB → Inventariar conectores MCP
   → recién ahí: Gate 0 + pull de data → clasificación → leverage → BRIEF + predicción visual
```

Las preguntas son baratas y le dan certeza al cliente. El pull es caro y va después.

---

## Las 8 preguntas de pre-config (canónicas)

**El intake son SIEMPRE estas 8 preguntas, en este orden.** Se hacen agrupadas (idealmente en una sola tanda), no de a una. Si el usuario ya respondió alguna en su mensaje, no repreguntarla — confirmarla. Si no la define ("aún no sé"), se sigue con default declarado y el brief lo cubre con escenarios. **Primero estas 8; recién después el pull y el output visual.**

1. **Sitio / marca / URL.** ¿Qué tienda? Es lo único sin lo cual no hay radar. Si hay una sola tienda conectada, proponerla como default y confirmar. El skill es reutilizable: sirve para esta o cualquier tienda.
2. **Evento objetivo.** ¿Cuál trabajamos? El skill **identifica el más cercano a la fecha de hoy y además lista los próximos eventos y sus diferencias** (fechas, duración, mecánica, vertical que más tracciona) desde `event-calendar.md`, todo **confirmado por web** (ver abajo). Devuelve: *"El más cercano es [evento] (del X al Y, ~N días). Después vienen [B] y [C]. ¿Vamos con el más cercano?"*. Si es evento propio, pedir fechas y duración.
3. **Vertical / categoría.** ¿Moda, consumible, skincare, otro? Define mecánica, lead-time y qué no puede fallar (`product-classification.md`). Se autodetecta del catálogo y se confirma.
4. **Ambición / objetivo.** ¿Volumen, margen, captar cohorte nuevo, o liquidar stock? ¿Qué tan fuerte jugarla? (Pregunta base — puede quedar "por definir" → el brief va con escenarios.)
5. **Presupuesto de inversión aprox.** ¿Cuánto invertir en el evento (paid + producción)? Un rango basta. (Puede quedar "por definir".)
6. **Productos a trabajar.** ¿Los tienes declarados o los detecto del catálogo y te los propongo para validar? (`product-classification.md`.)
7. **Capacidad de ejecución.** ¿Qué palancas existen: enviar correos (email/SMS) · generar/mover anuncios (paid) · mover el sitio (CRO/ficha) · producir creativos · asegurar stock? El brief solo apalanca lo que existe — no recomendar paid si no hay quién lo prenda.
8. **Meta de resultado / proyección esperada.** ¿Hay una meta de ventas/ROAS para el evento, o proyecto yo desde tu histórico? Esto ata la predicción del output.

> **Conectores MCP (no es pregunta, lo inventaría el skill):** en paralelo revisar qué hay conectado (Shopify, Meta, Google, Klaviyo, TikTok/Dashbo, Ahrefs/Semrush) y usar **lo que haya** para las previsiones de búsqueda y de producto. Lo que falte se declara como gap, no se inventa. Sin Shopify se exige conectarlo (Gate 0).

---

## Variables analizadas — batería FIJA por tipo de negocio

Las 8 preguntas cierran el encargo; con el OK, el skill sale a analizar una **batería fija de variables** que depende del tipo de negocio. Es fija (siempre las mismas) para que el análisis sea comparable entre clientes y el cliente sepa de antemano qué se va a mirar.

**Ecommerce DTC (batería estándar) — se leen del MCP, no se preguntan:**
1. **Facturación / baseline** (run-rate diario, tendencia)
2. **Ticket medio (AOV)** y su comportamiento en evento
3. **Zonas de mayor venta** (región/ciudad — dónde concentra el revenue)
4. **Avatar / recurrencia** (nuevo vs recurrente, returning rate, dispositivo)
5. **Colecciones y valores** (catálogo, rango de precios, packs)
6. **Comportamiento de producto** (ganador/sidekick/fantasma/zombie)
7. **Canales rentables** (fuentes de tráfico, mix del evento pasado)
8. **Envío / despacho** (deadline logístico, cobertura, umbral de envío gratis)
9. **Estacionalidad / tendencia** (ola de búsquedas + curva del evento pasado)
10. **Oportunidad, gap de mercado y zona gris** (síntesis: dónde hay leverage, qué no está capturando, qué es incierto)

**Otro tipo de negocio (ej. SaaS):** la batería cambia — serían ~10 preguntas/variables fijas propias de ese modelo (activación, MRR, churn, expansión, ciclos de renovación, etc.). Este skill es SOLO ecommerce DTC; si algún día se extiende, cada vertical de negocio trae su propia batería fija.

Todo lo que no se pueda leer del MCP se declara como **gap** en el output (no se inventa). Estas variables son exactamente las que el output visual muestra arriba en "Análisis de marca → [URL] · variables analizadas".

---

## Confirmar el evento por WEB (parte del Bloque A)

Las fechas de los eventos cambian cada año — **nunca asumirlas de memoria.** Apenas se nombra el evento, hacer una búsqueda web para confirmar:
- Nombre oficial y organizador (ej. CyberDay/CyberMonday los organiza la CCS; Black Friday es el último viernes de noviembre).
- **Fechas exactas y duración** del año en curso.
- Devolverlo al usuario para que confirme antes de seguir: *"Verifiqué: [evento] es del [fecha] al [fecha], ~[N] días. ¿Trabajamos sobre eso?"*
- Si la búsqueda contradice lo que dijo el usuario (ej. cree que es a fin de mes y en realidad es el 5 de octubre), **decirlo explícito** — es parte del valor.

Cruzar la fecha confirmada con `event-calendar.md`: posición en el mes vs ciclo de pago, estacionalidad de la categoría, y la ventana de lead-time de la vertical → esto da el veredicto del reloj (holgado / justo / tarde).

---

## Salida del intake (antes del pull)

Cerrar la Fase 0 con un mini‑resumen de una pantalla, para que el cliente confirme antes de gastar en el pull:

```
Encargo confirmado:
- Sitio: [marca / URL]
- Evento: [nombre] · [fechas] · ~[N] días · reloj [🟢/🟡/🔴 T-N]
- Ambición: [objetivo] · presupuesto aprox [rango]
- Productos: [declarados por el cliente / a detectar del catálogo]
- Palancas disponibles: [email · paid · sitio · creativo · stock]
- Conectores MCP: [los que hay] · gaps: [los que faltan]

→ Con esto salgo a traer la data y levanto el brief + predicción. ¿Confirmas?
```

Solo tras el OK (o si el usuario ya dio todo y pidió avanzar) se corre Gate 0 y el pull (`data-pull.md`). **Este resumen es el checkpoint que le da certeza al del otro lado antes de la avería de data.**

---

## Excepciones (cuándo acortar el intake)

- Si el usuario **ya entregó** sitio + evento + ambición en su mensaje, no repreguntar: confirmar en una línea y avanzar.
- Si hay **una sola tienda conectada** y el usuario claramente se refiere a ella, proponerla como default y confirmar, no preguntar en abstracto.
- Si el usuario dice explícito "no preguntes, avanza con lo que haya", correr con defaults sensatos declarados y marcar los supuestos. Pero por defecto: **preguntar primero.**
