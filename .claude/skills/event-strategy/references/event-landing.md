# Event Landing — lander pública genérica de captura (nurture)

Además del **brief interno** (conector + data del cliente), este skill produce un segundo entregable de otra naturaleza: una **lander pública, genérica, que habla del evento** y **captura leads con un formulario** para nutrir. No es específica de un cliente ni usa data privada — es un activo de tope de funnel.

## Para qué sirve y dónde encaja en el flujo

```
1. Ejercicio interno (brief con conectores)   → material y aprendizaje
2. Lander pública genérica del evento + form  → nutrir mercado y CAPTURAR leads   ← este archivo
3. Con cada lead capturado → recién el ejercicio profundo con SUS conectores
```

La lander va **antes** del ejercicio con conectores del prospecto: primero se atrae y se captura (genérico, sin data privada), y solo cuando el lead entra se corre el brief completo con sus MCP. Es la puerta de entrada, no el análisis.

## Reglas duras

- **Genérica, no específica de un cliente.** Habla del evento (ej. "CyberMonday 2026: cómo preparar tu ecommerce") con fechas verificadas por web, tips, urgencia de tiempo. Nunca expone data privada de una tienda.
- **Pública y compartible.** Se publica como Artifact (link abierto). Sirve para pauta, orgánico, bio, outreach.
- **Captura con formulario real.** El form guarda los leads de forma persistente y legible después — usar una **runtime capability** del Artifact (form/DB). **Cargar `artifact-capabilities` ANTES de escribir la página** para ver qué está disponible para esta cuenta y cómo declarar la captura; no usar `localStorage` para leads (se pierde). Campos mínimos: nombre, email, URL de la tienda, y opcional facturación aprox / evento de interés — justo lo que después alimenta el intake del brief.
- **Marca:** por defecto va con marca Advanz (es un activo de adquisición de Advanz). Si el usuario la quiere white-label o co-branded, preguntarlo.
- **No prometer lo que no se hará solo:** el form captura; el envío de correos de nurture y el ejercicio con conectores son pasos humanos/otros skills.

## Estructura de la lander (visual, escaneable)

1. **Hero:** el evento + su fecha verificada + cuánto falta (countdown/urgencia). "Se viene [evento], del X al Y."
2. **Por qué importa:** el evento como pico anual (dato de mercado, ej. CyberDay Chile >US$500M), y el costo de improvisar.
3. **Qué se necesita para llegar bien:** mini-checklist genérico (oferta, stock, tracking, lista, creativos, warm-up) — educa y crea urgencia de tiempo.
4. **La oferta de valor:** "te preparamos el preview de tu campaña con tu propia data" → el brief que hace este skill.
5. **Formulario de captura** (el CTA): nombre · email · URL tienda · (opcional) facturación / evento. Copy claro de qué recibe.
6. **Prueba/credibilidad:** qué entrega el análisis (mockup del brief, sin data real de terceros).

## Handoff

- Los leads capturados → se revisan y para cada uno se corre el **intake de 8 preguntas** (`intake.md`) + el brief con SUS conectores.
- Producción de la secuencia de nurture por correo → `advanz-email-engine`.
- Si se quiere una calculadora/quiz en vez de lander simple → `b2b-assessment-builder`.

**Regla:** la lander es genérica y captura; el valor real (el brief con data) se entrega recién cuando el lead entra y conecta sus fuentes.
