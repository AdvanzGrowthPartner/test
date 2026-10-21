# AmazingCare · OS Creative (creativos, videos, copies, contenido, paleta)

## Estado actual
**21-oct-2026:** el Dashboard propio queda congelado; el tablero vigente es el Creative OS · Command https://claude.ai/artifact/Lp1TYgozy1cMnH3Lnemq63.

**19-oct-2026 · arranque del OS y artifact.**
- Dashboard propio publicado: https://claude.ai/artifact/A15ucnSsaqSpmcLpp4HSkp (tipo Dashboard, privado). Se dibuja desde `os-data.json` (contrato v1.0 del Command Center), con 8 KPIs, 6 fugas (F01–F06) y los accesos.
- Accesos probados con lectura simple: Meta Ads (DTC y Mayorista habilitadas), Notion, Canva, Drive y Magnific responden. En Figma el asiento es View en plan starter (lee, no edita). Pletor exige plan pago. Las skills `advanz-paid-media:*` no están cargadas en esta sesión.

**Último dato leído: 30 sep–4 oct 2026, plan creativo del Cyber.**
- **Plan Cyber oct-26** (Notion "AC | Creativos Octubre - CYBER"):
  - 25 estáticos (3 pre-Cyber), casi todos de electrolitos, más 10 UGC y 11–12 videos de creadores.
  - Descuentos: 30% en electrolitos y packs, 35% en Energy, 40% en Fibra, 30% en accesorios y creatina. Envío gratis sobre $50K.
- **Sistema de contenido Amazing** (archivos en `sistema-content/` y Notion):
  - Nomenclatura con **SKU ciego**: `AC-VID-00XX` (video), `AC-EST-00XX` (estático), `AC-EVT-00XX` (evento). La clasificación vive en Notion (🎬 Creativos).
  - Etiqueta legible para Meta: `AC-VID-0031 · ELE · P1 · A2 · MOF`.
  - Correlativos al 12-sep: AC-VID hasta 0041, AC-EST hasta 0055, AC-EVT hasta 0022.
  - Reglas de pack: 1 pack = 1 avatar + 1 concepto. Nunca se inyecta un ad nuevo en un pack viejo. Los packs simultáneos se limitan con 20% del presupuesto ÷ CPA.
- **Top creativos (ago-26, ciclo 3–20):**
  - AC-VID-0027: ROAS 3,84, con poco presupuesto, así que hay margen para escalar.
  - Catálogo: 3,12 · AC-EST-0012: 2,40 · Clips Preparación Energy (AC-VID-0001): 2,15.
  - Estático Ago #3 Testimonios: el CPA más bajo ($7.780).
  - A rotar: AC-EST-0023 (0,77), @NutriAnto Activación Energy (0,96), AC-VID-0006 @Max_Zumaran (sin compras).
- **Fiestas Patrias (primeros días):**
  - AC-EVT-0013, de catálogo con copy que parte del dolor del cliente: ROAS 7,13 y 11 compras.
  - AC-EVT-0011: 5,48 · AC-EVT-0007: 3,05.
  - Ángulos ausentes: prueba social/testimonial, resaca/festejos y formato educativo.
- **Por ángulo (cockpit, sep-26):** 48% del gasto en "Descuento FP", con CTR 0,57%. **Disautonomía/Migraña tiene CTR 2,17% y solo recibe el 6%.** Retail: CTR 0,12%.
- **UGC sep-26:** @PaulaCamus (nutri) rinde 2,92×. @MartinTorres tiene CTR 6,39% pero no vende.
- **Videos clasificados:**
  - Lote Meli AC-VID-0017 a 0030 (16-ago).
  - 0031 Force/Hyrox: fundadores Gonzalo y Martín Vallejos, P1, candidato a Partnership Ad.
  - 0032 Nta. Paula Camus, lipedema/POTS: P4, claims a validar.
  - 0033 Clase AM Energy: cierre mixto Jumbo + web.
  - 0034 "Energy llegó a Jumbo": retail.
  - 6 videos de retail (Ahumada, Cruz Verde, Jumbo, SPID, STOP, Tottus): UGC 9:16 de 11–18 s.
  - AC-VID-0040/0041: sin pista de audio.

## Decisiones tomadas
- **Paleta y lock de marca (20-ago):** celeste `#00C3F0`, azul `#020C56` y blanco, con tipografía Jost. Ver `contexto-marca.md`.
- **Generador de estáticos con IA:** la IA nunca dibuja el producto ni el texto. El producto va como PNG sin fondo o packshot; el texto y el logo, siempre en la capa de diseño. QA humano obligatorio para hex, logo y texto.
- **26-ago:** las referencias de la competencia no se transcriben. Se entiende la estructura y se replica en la marca Amazing, destacando la oferta. El código del 25% va solo en las piezas de cierre; las de ángulo y las educativas abren sin código.
- Para producir primero en FP: "¿Carrete el 18? La resaca es deshidratación", testimonial, selector de sabores (empuja el Pack Mix 60) y "Formato práctico, listo para llevar".
- **Contenido de video (21-ago):** diversificar como los videos de Meli, pero variando fondo, guion, CTA y mensaje, y segmentar avatares a través del guion. Prioridades para el evento: P5 Familia + A7 Valor.
- **11-sep:** los assets se suben renombrados `SKU_1x1` / `SKU_9x16` a la biblioteca de Meta (`Septiembre/Meta-Assets/AON` y `/FP`). La API crea creativos de un solo asset, así que los verticales se agregan a mano.
- AC-EVT-0020/0021 (repiten el Pack 60 de 0017) y AC-EST-0050 (código FP en la carpeta AON) quedaron excluidos.
- Los avatares y ángulos de baja cobertura que hay que llenar son P4 Salud, P5 Familia y A7 Valor.

## Pendientes / próximos pasos
- [ ] Mantener `os-data.json` y el Dashboard al día en cada cierre (re-subir los JSON del artifact si cambian KPIs o fugas).
- [ ] Resolver acceso de edición en Figma y decidir si se paga Pletor o se usa Magnific como alternativa.
- [ ] Rendimiento creativo del Cyber oct-26: qué UGC, estático y ángulo ganó. Todavía no hay análisis.
- [ ] Llevar más presupuesto y piezas al ángulo **Disautonomía/Salud**, que tiene el mejor CTR (validando claims con el cliente).
- [ ] **Base 🎬 Creativos de Notion:** en ago-26 quedó con el data source huérfano (las vistas del SOP apuntan a `816cfa7b…`, que ya no existe). Confirmar si se arregló y si las fichas 0031–0055 están cargadas.
- [ ] Copy FP de los nuevos anuncios: lo redactó Claude (los posts originales no son reutilizables), así que falta la revisión del cliente o el equipo.
- [ ] End-card unificado de 2 s para los videos de retail ("Ahora en Jumbo · Tottus · Cruz Verde · Ahumada · SPID · STOP").
- [ ] Fotos de producto en artifacts: `cdn.shopify.com` está bloqueado en todos los entornos. La alternativa es pegarlas en el chat o pedir allowlist.

## Fuentes
- session_012bPVZ6HhBcBzZSQCVysRhn: paleta de colores (20-ago)
- session_01AVNrUSGKCEx7Pbdc95HgYK: análisis de textos de creativos, 31 referencias (26-ago)
- session_01XgqVQT3837vaL1jcGtqGMT: clasificación de videos 0031–0034 (25-ago)
- session_01Dix3y3CxXhRZp5tgjF9rA1: 6 videos de retail (25-ago)
- session_01Lete8uGMuJPaG3Gy8QkcMA: clasificación FP/AON y renombrado SKU (11/12-sep)
- session_01ESqY2NmD1L3w1PXJ8Dpwuw: 2 videos nuevos para clasificar (1-sep; solo se leyó el pedido)
- session_011spdrKTxeCHNXAtWYbAG1h: estáticos FP 2026 (21-ago; la sesión solo tiene análisis de imágenes, sin conclusión registrada)
- session_01VjaHS4QzC4uGuNMfJXSH7k: rendimiento por ángulo (advanz-motor.pages.dev)
- session_01MLGvNVcyGZBjw1Ey4x8HPU: plan creativo del Cyber (Notion)
- Archivos locales: `sistema-content/` (00-INDICE, analizar-creativos, generador-estaticos-ia-v2, flujo-aprobacion, generar-guiones, escalar-horizontal)
