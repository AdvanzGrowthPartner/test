# Advanz · OS Growth · Estado

> Funnel comercial, adquisición, métricas del negocio, pipeline y OS interno. Este OS prioriza y deriva a los demás. Actualizado: 2026-10-21.

## Estado actual
- **Command propio "Growth OS · Advanz"** (2026-10-21): https://claude.ai/artifact/7qL12oAKhA3sgqgspnGrR5. Es de tipo Dashboard, solo tiene datos de Advanz y sigue la spec `ops/_command/COMMAND.md`. Muestra KPIs, qué hacer ahora, oportunidades entre OS de Advanz, pedidos, accesos y cambios. La URL está en `command/URL` y en `os-data.json`.
- **Command Center de los 12 OS**: https://claude.ai/artifact/44LVZUHY5tgGH6P7Nb6vHk. Se ve **una marca a la vez** (Advanz o AmazingCare) y no tiene vista combinada.
  - `command-center/consolidar.py` nunca une fugas de marcas distintas. También genera `consolidado/oportunidades.<marca>.json` para el Growth OS de cada marca.
  - Corte del 21-oct: **los 12 OS tienen `os-data.json` propio** (0 en semilla). Hay 62 fugas abiertas y 17 oportunidades, 8 de ellas de Advanz.
  - Top Advanz: (1) el funnel propio no tiene medición (no hay dato de CVR, opt-in, agenda ni abandono); (2) el social video está detenido porque no se ha hecho la sesión batch; (3) el form del lead magnet está desconectado de GHL.
  - Accesos que más destraban en Advanz: GHL (sin conector) y Meta (UNSETTLED).
- **Sistema de adquisición** (skill `advanz-acquisition-system`). Métrica única: **diagnósticos entregados → agendados → cerrados**. Meta: 100/sem → 15–20% interés → 6–10 agendas → 2–3 cierres.
  - 🟢 Cold outreach · 🟢 Social estático · 🟢 Web funnel · 🟡 Video · 🔴 Ads · 🔴 SEO/GEO.
  - Tablero en Notion: 📊 Canales de Adquisición (Interno › Dept. Marketing › 💵 Sistema Adquisición). Diagnóstico por síntoma: pocos envíos → volumen · no responden → copy · no agendan → workflow GHL · no cierran → pitch.
- **Pipeline comercial**: lead → setter → discovery pagada ($150–200k de reserva) → propuesta → contrato.
  - Skills: `advanz-setter-agent`, `advanz-cco-agent` (3 pitches), `advanz-closing-agent`, `advanz-contract-generator`.
  - DBs en Notion: Leads y Cotizaciones (productos: Discovery $150k, DWY 3 meses, DFY por canal, Migración).
- **Deal documentado**: **Marê Swimwear** (moda de baño, ticket ~$77k CLP, ~67k sesiones/año, ~25% de recompra sin flujos de email).
  - Discovery el 18/08 y propuesta el 21/08 a las 10:00. Propuesta de 3 meses con capas CRO, email y ads, presentando precio mes 1 → mes 2 → total.
  - Objeción raíz: "esto o contratar a 2 personas" → reframe: Advanz deja el sistema y la contratación lo opera.
  - **Resultado del deal: sin confirmar.**
- **OS interno**:
  - 134 sesiones auditadas y clasificadas (2026-09-16), con router de skills `ADVANZ-OS-ORCHESTRATION.md` (PR #1).
  - Sesiones re-etiquetadas en carpetas: `carpeta:cliente-*`, `carpeta:interno-backend`, `grupo:*` (2026-09-21/22).
  - Blueprint de 4 roles (2026-09-15).
  - Estructura `ops/` con 12 OS (2026-10-19).

## Decisiones tomadas
- **2026-10-19**: Todos los OS publican su artifact sobre el mismo formato `os-data.json` (versión 1.0), y la fuente de verdad es el repo, no el artifact. Growth consolida y prioriza. La ejecución pasa por el OS dueño, por MCP o Cowork, siempre con OK.
- **(sin fecha, vigente)** El activo central es el **Diagnóstico Vivo**. El contenido pasa a ser una capa de credibilidad y no el motor de leads. Ads y SEO/GEO quedan detenidos hasta cumplir sus condiciones.
- **(sin fecha)** "No construir más rápido de lo que se vende": 1–2 piezas en paralelo con lo vendido. Double down cuando un ángulo pica.
- **(sin fecha)** Las dos capas espejo: público (infoproducto: el qué y el por qué, más CTA) e interno (SOPs: el cómo). Cadena: SOP → board Miro → video → página pública → CTA → post IG → DM.
- **2026-09-15**: Operar como 4 células (diseño IA, paid media, Shopify/backend, growth/comercial) con repo global (GitHub `advanz-os` + Notion). Ciclo: chat → hallazgo → validar → codificar → repo.
- **2026-09-16/17**: El router de skills cita las skills y no las modifica. Se archivaron 8 sesiones `matiascs-*`. PR #1 abierto.
- **2026-09-21/22**: Carpetas por cliente arriba e interno abajo. Los agentes de rol que operan para un cliente van a la carpeta de ese cliente. Se archivaron los duplicados.
- **2026-08-21 (Marê)**: No bajar el precio ante objeciones de validación. Siempre anclar fecha. Checkpoints en vez de promesas de cifras.

## Pendientes / próximos pasos
- [ ] Cada vez que un OS cierre trabajo: re-correr `consolidar.py`, re-subir los JSON al Command Center y `oportunidades.advanz.json` al Command de Growth.
- [ ] Sumar al Command de Growth el embudo diagnósticos → agendas → cierres cuando haya números reales (necesita export de GHL).
- [ ] Registrar los números reales semana a semana (diagnósticos enviados, respuestas, agendas, cierres) en el tablero de Notion y reflejarlos acá.
- [ ] Confirmar el resultado del deal Marê Swimwear y su aprendizaje (`funnel-intelligence`).
- [ ] Destrabar 🟡 Video: una sesión batch de Patricio de 2–3 h (handoff a creative).
- [ ] Revisar y mergear el PR #1 (router) y decidir si se vuelve `CLAUDE.md` global o se espeja en Notion.
- [ ] Consolidar duplicados de "Contenido SOP" y del diseñador (1 chat por cliente y 1 de skills).
- Falta levantar: MRR y clientes activos (Amazing Care, nad, Kite, Vanguard STT y otros), tasa discovery → contrato, y quién es dueño de cada canal por nombre.

## Fuentes
- `session_01Q3frq6c6YEgSmr8yxNFT4V`: Advanz OS | Agentes & skills (2026-09-16/17). Inventario y router.
- `session_01TupGAL6pK6e7nzRXnoxhz9`: [OS] Organizador de chats (2026-09-21/22). Lectura parcial: se omitieron las páginas más antiguas.
- `session_01GS3wvZZLV84tfQ61sjgeaq`: Advanz login para equipo de 4 roles (2026-09-15). Artifact https://claude.ai/artifact/Ffv7hoSRb63awDezWnJPvZ.
- `session_019ujiE2BjTxXhfWfZsBGABJ`: Objeciones Marê Swimwear (2026-08-21).
- `session_01UDo3RBzUo4ESdLMPLHN3cN`: Marê discovery (2026-08-18). **No se pudo leer**: el contenido queda tapado por miles de eventos de reconexión.
- `session_012vxt72uJmnjFRPZFHDHzKV`: Skills ecommerce en GitHub (2026-09-28). Rama `origin/claude/friendly-brahmagupta-arg9vp`, 21 skills.
- Rama `origin/claude/vigilant-edison-ak1920`: `ADVANZ-OS-ORCHESTRATION.md`.
- Skills `advanz-acquisition-system`, `advanz-cco-agent`, `advanz-closing-agent`, `advanz-setter-agent`, `advanz-growth-engine`.
