# Cyber Playbook — Pre / Peak / Post

El evento no es un día, es tres fases con restricciones distintas. La mayoría del valor (y de los errores) está en el Pre y en el Post, no en el Peak.

**Calendario Chile 2026:**
- **CyberDay:** lunes 1 a miércoles 3 de junio (organiza la Cámara de Comercio de Santiago, sitio Cyber.cl + CyberApp).
- **CyberMonday:** segundo semestre (típicamente octubre/noviembre).
- CyberDay 2025 superó los US$520M en ventas (+4,6% YoY). Es un punto de inflexión anual de ingresos para un DTC.
- **Novedad 2026:** debuta "Cyber AI", un agente conversacional en Cyber.cl que recomienda productos en lenguaje natural. Es una **superficie GEO nueva** — ver nota al final.

---

## FASE PRE (T-14 a T-1) — Preparar el engine

Restricción típica: **falta de munición.** Si la lista, los creativos, las audiencias, la oferta y el tracking no están listos antes, en el peak se improvisa y se pierde.

Checklist Pre (en orden de prioridad):

1. **Tracking QA (lo primero).** Pixel + CAPI de Meta vivos y con buen match. Conversiones de Google/TikTok registrando. GA4 OK. UTMs de Klaviyo marcando email como fuente en Shopify. Si esto no está, todo lo demás se mide mal. (Gate 0 de `optimization-rules.md`.)
2. **Oferta y bundles definidos.** Qué SKUs entran, con qué descuento, qué bundles, qué umbral de envío gratis. Chequear margen unitario de cada oferta.
3. **Crecimiento de lista.** Popup de captura con gancho de early access ("entérate primero del cyber"). Cada email/teléfono capturado pre-evento es revenue owned barato en el peak.
4. **Audiencias armadas.** Retargeting de visitantes/ATC/checkout de las últimas semanas calentando. Lookalikes de compradores. Custom audiences de la lista.
5. **Banco de creativos.** 3-5 variantes de creativo de cyber por canal, listas para rotar sin frenar campañas. (Producción → célula creativa / `advanz-paid-media`.)
6. **Warm-up de campañas.** Subir presupuesto **gradualmente** los días previos para que el algoritmo entre al peak con learning resuelto, no en frío.
7. **Inventario.** Confirmar stock de los SKUs que se van a empujar. Definir el plan si un ganador se queda sin stock.
8. **Cadencia de email planificada** (ver abajo).
9. **Sitio listo para carga.** Revisar velocidad móvil, pausar apps no críticas, tener el plan de triage si el CVR cae bajo carga.

**Trampa Chile a evitar (riesgo Sernac + reputacional):** NO inflar precios en la segunda quincena de mayo para fingir un descuento mayor en junio. Comparadores como Knasta y SoloTodo muestran el historial de precios y exponen el "salto" — quema confianza y expone a fiscalización. El descuento debe ser real.

---

## FASE PEAK (Jun 1-3) — Mover la restricción cada 3-6 horas

Acá corre el loop del Cyber Pulse. No es "setear y olvidar"; es leer y mover.

**Cadencia de lectura:**
- Día 1 (lunes), arranque: pulse cada 3 horas las primeras 12h (el lunes concentra la mayor demanda).
- Resto del peak: pulse cada 6 horas, más uno al despertar y uno antes de dormir.
- Alertas: si Meta `ads_get_errors` o Dashbo indicators tiran algo crítico, pulse inmediato.

**Loop de cada pulse:** traer las 4 fuentes → Gate 0 → diagnosticar restricción → aplicar reglas del canal → entregar Cyber Pulse. (Todo en `optimization-rules.md`.)

**Prioridades operativas del peak:**
- Escalar ganadores +20%, matar perdedores (3x kill), rotar creativo fatigado.
- Stock-aware: redirigir spend de SKUs que se agotan a SKUs con stock y margen.
- Owned: ejecutar la cadencia de email (abajo). El revenue de email en peak suele ser el más barato disponible.
- Proteger lo que funciona (sección "No tocar" del pulse).

**Cadencia de email/SMS del peak (canal propio):**
1. **Teaser** (T-2 a T-1): "se viene", early access para VIP/lista.
2. **Live** (día 1, 00:00-mañana): "estamos en vivo", oferta principal.
3. **Midpoint** (día 2): recordatorio + social proof / bestsellers.
4. **Last chance** (día 3 tarde): urgencia real, "últimas horas".
5. **Extendido** (T+1, opcional): muchos DTC extienden 1-2 días post-evento oficial; sirve para capturar a los rezagados y a quienes esperaron el "último día".

---

## FASE POST (T+1 a T+14) — Donde se gana el LTV

Restricción típica: **el cohorte se enfría.** La mayoría de los DTC celebran las ventas del evento y sueltan al comprador nuevo. Ahí se pierde el verdadero retorno del cyber.

1. **Extended cyber (T+1 a T+2):** correr la cola. Quien no compró el último día a veces compra al día siguiente con "última oportunidad".
2. **Retención del cohorte cyber:**
   - Welcome flow para compradores primerizos del evento → segunda compra.
   - Flow de "segunda compra" con incentivo suave para los que compraron una vez.
   - Win-back para los que agregaron al carrito y no compraron.
3. **Segmentación RFM del cohorte:** separar one-time buyers de potenciales recurrentes; tratarlos distinto.
4. **Debrief cuantitativo:** comparar el evento vs baseline (ver `benchmarks-cyber.md`). Qué canal rindió, qué SKU, qué creativo, qué restricción dominó cada fase.
5. **Feedback al Growth Engine:** los aprendizajes del cyber alimentan las etapas Acquisition/Retention/Feedback del `advanz-growth-engine` del cliente. Lo que funcionó en cyber es hipótesis para el resto del año.

---

## Nota GEO: "Cyber AI" 2026

El sitio oficial Cyber.cl estrena en 2026 un agente conversacional ("Cyber AI") que recomienda productos en lenguaje natural. Es una superficie de descubrimiento nueva, tipo GEO/agentic commerce. Implicancia para clientes Advanz: la calidad de los datos de producto (títulos, atributos, schema, claridad de oferta) influye en si el agente recomienda o no la marca. No es accionable a último minuto para CyberDay, pero es un punto para el debrief Post y para la estrategia GEO del año (`advanz-seo-geo-engine` / `advanz-growth-engine`).
