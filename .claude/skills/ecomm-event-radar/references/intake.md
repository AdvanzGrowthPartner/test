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

## Los 4 bloques del intake

Hacer las preguntas **agrupadas**, no de a una. Si el usuario ya respondió algo en su mensaje, no repreguntarlo — confirmarlo.

### Bloque A — Qué y dónde
1. **¿Qué sitio / marca / URL?** (la tienda del cliente). Sin esto no hay radar.
2. **¿Qué evento?** — Cyber, CyberDay, CyberMonday, Black Friday/Black Week, Hot Sale, Navidad, Día de la Madre/Padre, San Valentín, 18/Fiestas Patrias, liquidación, o **evento propio de marca**.
   → Apenas se nombra el evento, el skill **lo confirma por web** (ver abajo): nombre oficial, fechas exactas y **duración aproximada**, y lo devuelve en una línea: *"Se viene [evento], ~[N] días, del [fecha] al [fecha]. ¿Es este?"*. Si es evento propio, preguntar fechas y duración al usuario.

### Bloque B — Ambición y alcance
3. **¿Con cuánto quieres participar / cuál es tu proyección?** — el objetivo (volumen / margen / captar cohorte / liquidar) y qué tan grande quiere jugarla. Define la escala del plan.
4. **¿Presupuesto proyectado aprox?** — cuánto quiere invertir en el evento (paid + producción). No necesita ser exacto; un rango basta para dimensionar.

### Bloque C — Munición
5. **¿Tienes los productos declarados / claros que vas a trabajar?** — Si sí, cuáles. Si no, el skill los detecta del catálogo (`product-classification.md`) y los propone para validar.
6. **¿Qué capacidad de ejecución tienes?** — ¿puede **enviar correos** (email/SMS)? ¿**generar/mover anuncios** (paid)? ¿**mover el sitio** (CRO/ficha)? ¿producir **creativos**? ¿asegurar **stock**? El brief solo apalanca las palancas que existen; no sirve recomendar paid si no hay quién lo prenda.

### Bloque D — Conexiones (lo inventaría el skill, no es pregunta abierta)
7. **¿Qué conectores MCP hay disponibles?** — Shopify, Meta, Google, Klaviyo, TikTok/Dashbo, Ahrefs/Semrush, etc. El skill revisa qué está conectado y usa **lo que tenga** para las previsiones de búsqueda y de producto. Lo que falte se declara como gap (no se inventa). Si falta Shopify, se exige conectarlo (Gate 0).

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
