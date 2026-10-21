# Advanz · OS CRO · Estado

> Landings, lead magnets, funnels, quiz y web **propios** de Advanz. Actualizado: 2026-10-19.

## Estado actual
- **Web funnel 🟢 activo**: home de advanz.cl + lander + workflow GHL. El sitio y el blog viven en **GoHighLevel** (sin confirmar si todo el home está en GHL). Meta: 20 leads por semana y 0 sin gestionar.
- **Lead magnet "La Guía Definitiva: Por qué Shopify gana"** (`/home/user/test/advanz-shopify-leadmagnet.html`):
  - Promete un PDF de 32 páginas (Shopify vs Jumpseller vs WooCommerce, 7 errores, checklist de 30 días, casos chilenos).
  - El form pide nombre, email y etapa de la tienda. CTA secundario: "Agenda un diagnóstico gratuito". Ataca el dolor de nivel **Plataforma** (pitch Migración).
  - ⚠️ **El form no está conectado**: `fetch('/api/leads')` comentado.
  - ⚠️ Claims sin verificar: "+200 emprendedores", "más de 20 tiendas", testimonios con iniciales. No hay evidencia de que el PDF exista (sin confirmar).
- **Funnel Cyber (Motor de Cyber)**: ruta `/cyber` con espacio reservado para la VSL.
  - Brief del funnel de 2 pasos (2026-09-07): Landing A opt-in (hook CyberMonday + prueba ROAS 7,04x / +$27M en 7 días + tease de 3 palancas) → Landing B con VSL + countdown + CTA a "Diagnóstico de Cyber de Advanz" (llamada gratis). Stack Next.js con captura → GHL por API y Pixel/CAPI/GA4. Referencia: el funnel de Peakk Media.
  - Esa sesión solo registra el brief inicial; no hay respuesta ni build en el transcript.
  - **VSL HTML + GSAP de 90"** construida el 2026-09-08 (`empresa/advanz/cyber-engine/2026-09-08_cyber-vsl.html`, en el PC local del equipo): 14 escenas, tema claro, tokens Advanz.
- **Quiz / assessment**: los reels con CTA "comenta [palabra]" deben llevar a un **lander de captura tipo quiz funnel**. El closing reconoce "lead post-assessment" como fuente. Skill `b2b-assessment-builder`. El quiz construido no aparece en los transcripts (sin confirmar).
- **Assessment de email** reutilizable como lead magnet: `advanz-email-engine/assets/email-engine-madurez.html` (madurez 1–5 según facturación).

## Accesos (probados 2026-10-19)
- **Vercel ✅**: equipo `matiasroldan-7968's projects` → `landeradvanz`, `web`, `advanz-hub`, `paid-media-engine`, `test`.
- **Shopify ⚠️**: conecta a amazingcare.cl, no a Advanz. No tocar desde este OS.
- **Ahrefs ❌**: "Insufficient plan" (sin Web Analytics). **GHL**: sin conector. **advanz.cl**: el proxy de la sesión lo bloquea (Chromium instalado, sin salida).

## Artifact y datos para el Command Center
- `ops/cro/advanz/os-data.json` (contrato 1.0, `fuente: "os"`): 5 KPIs (todos sin dato) y 6 fugas (F01–F06; se agregaron F05 medición y F06 funnel Cyber).
- Dashboard **Advanz · OS CRO**: https://claude.ai/artifact/JosGimV3RiLAsjf2qKdW3h (privado; lee archivos fijos cargados desde `os-data.json`, se recargan en cada cierre).

## Decisiones tomadas
- **2026-09-07**: Funnel Cyber de 2 pasos adaptado de Peakk, con marca, mercado Chile y data propia anonimizada. La oferta es un diagnóstico o llamada gratis atada al Growth Engine y al Motor de Cyber.
- **2026-09-08**: VSL primero en **HTML + GSAP** (prototipo editable). Se pasa a MP4 con Remotion solo cuando esté aprobada.
- **(sin fecha)** No enterrar el Diagnóstico Vivo detrás de un lead magnet genérico (lección de los $450k en ads).
- **(sin fecha)** Web funnel: probar end-to-end con 1 lead real y después no seguir puliendo.

## Pendientes / próximos pasos
- [ ] Habilitar una fuente de medición (Ahrefs Web Analytics, Clarity/GA4 o export de GHL) para tener la línea base de CVR, opt-in y agenda.
- [ ] Conectar el form del lead magnet Shopify a GHL, crear o confirmar el PDF y validar o quitar los claims no verificables.
- [ ] Decisiones abiertas del funnel Cyber: nombre exacto de la oferta, calendario (GHL o Calendly), opt-in más VSL o página única, y si el lead magnet es el "Cyber Opportunity Preview".
- [ ] Feedback de la VSL (copy, timing, colores) → render MP4 con Remotion → embeber en `/cyber`. La publicación como Artifact quedó bloqueada por permisos.
- [ ] Construir o confirmar el quiz funnel de captura para los CTA de reels.
- [ ] Probar end-to-end el web funnel (lander → GHL → 5 correos → agenda).
- Falta levantar: URLs vivas de lander y quiz, conversión actual, y dónde se aloja el código de los landers (Vercel u otro).

## Fuentes
- `session_01LqZBmMpzDuGBS6noCwmpeS`: Funnel landing + VSL Cyber para Advanz Chile (2026-09-07). Solo el brief inicial.
- `session_01VKZpMnCN6KptS1TKA9XEcc`: Lander Cyber + Quizz (2026-09-08). VSL GSAP.
- `session_01Vh8yEXgU79FsDDQaXPRGQM`: Agente | Contenido Reels (CTA → quiz funnel).
- `session_01Uth5F3kZToULKRveMxDzUN`: Ecommerce Builder (2026-09-21). Motor de conversión para clientes; rama `origin/claude/zen-sagan-cabhqo`.
- Repo: `advanz-shopify-leadmagnet.html` · rama `origin/claude/ecommerce-cyber-strategy-skill-mmm6m0` (skill event-strategy, `event-landing.md`).
- Skill `advanz-acquisition-system` (`canales.md`, Web Funnel).
