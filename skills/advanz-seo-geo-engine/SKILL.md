---
name: advanz-seo-geo-engine
description: Motor completo de diagnóstico, estrategia e implementación SEO + GEO (Generative Engine Optimization) para ecommerce DTC en cualquier vertical — suplementos, ropa, cosmética/skincare, mascotas, hogar, alimentos funcionales, wellness. Cubre las 7 capas del framework Advanz (técnico, entidad, contenido, E-E-A-T, off-page, UX/CRO, monitoring) tanto para Google clásico como para citas en LLMs (ChatGPT, Claude, Gemini, Perplexity). Usa SIEMPRE que el usuario diga 'diagnóstico SEO', 'auditoría SEO', 'plan SEO', 'GEO', 'AI SEO', 'optimización para LLMs', 'rankear en ChatGPT', 'citas en LLMs', 'AI citation score', 'AI Overviews', 'schema markup', 'Wikidata', 'E-E-A-T', 'autoridad temática', 'backlinks ecommerce', 'cluster topical', 'pillar content', 'mejorar tráfico orgánico', 'no aparezco en Google', 'no me citan en ChatGPT', 'optimizar PDPs', 'optimizar colecciones', 'YMYL', 'rich snippets', 'featured snippets', 'core web vitals', 'cómo rankear #1', 'estrategia de contenido ecommerce'. También actívala cuando el usuario pegue una URL de cliente ecommerce y pida diagnóstico, esté armando propuesta upsell SEO/GEO, escribiendo briefs para redactores o desarrolladores sobre SEO, decidiendo entre invertir en paid vs orgánico, comparando vs competidores en orgánico, o cuando hable de 'visibilidad de marca en buscadores', 'tráfico orgánico estancado', 'invisible en buscadores', 'autoridad de marca digital'. SOLO para ecommerce DTC/B2C — NO para B2B, SaaS, lead gen, ni servicios profesionales.
---

# Advanz SEO/GEO Engine

Motor completo y reutilizable para diagnosticar, planificar y entregar trabajo de SEO + GEO (Generative Engine Optimization) sobre clientes ecommerce DTC de Advanz.

**Principio rector:** En 2026 SEO y GEO no son canales separados — son la misma cosa observada desde dos motores distintos (Google y LLMs). Optimizar solo uno deja la mitad del tráfico de marca en la mesa.

---

## Cuándo activar este skill

Actívate apenas detectes uno de estos patrones:

- Usuario menciona SEO, GEO, rankings, tráfico orgánico, búsqueda, ChatGPT, AI Overviews, Perplexity
- Usuario pegó URL de cliente ecommerce y pide diagnóstico
- Usuario está armando propuesta upsell post-Paid Media
- Usuario pregunta "por qué no aparezco en Google / ChatGPT"
- Usuario habla de visibilidad de marca digital, autoridad temática, competidores orgánicos
- Cliente en migración (post-Shopify) sin estrategia orgánica establecida
- Cliente con paid media saturado que necesita reducir CAC vía orgánico
- Usuario menciona schema, Wikidata, backlinks, E-E-A-T, YMYL

**No te actives si:**
- Es un cliente B2B, SaaS, lead gen, o servicio profesional (este motor es DTC/B2C-only)
- El usuario solo quiere ayuda táctica con un meta tag puntual (responde inline sin invocar el motor completo)

---

## Verticales soportadas

Este motor está calibrado para 6 verticales DTC. Cada una tiene matices que están detallados en `references/verticals/`:

| Vertical | Archivo de referencia | Particularidades clave |
|---|---|---|
| Suplementos y wellness | `references/verticals/supplements.md` | YMYL alto, E-E-A-T crítico, ISP/INTA |
| Ropa y accesorios | `references/verticals/apparel.md` | Visual SEO, image search, schema Product variant |
| Cosmética y skincare | `references/verticals/skincare.md` | YMYL medio-alto, ingredientes, ISO/registros |
| Mascotas | `references/verticals/pets.md` | YMYL nicho veterinario, foros muy activos |
| Alimentos funcionales y bebidas | `references/verticals/food-bev.md` | Etiqueta limpia, certificaciones, registros sanitarios |
| Hogar y deco | `references/verticals/home-deco.md` | Visual SEO, Pinterest, schema Product detallado |

Antes de aplicar el framework, lee el archivo de la vertical correspondiente. Si el cliente combina varias (ej: marca de skincare que también vende suplementos), lee ambas.

---

## El framework — 7 capas

El sistema completo está documentado en `references/framework-7-layers.md`. **Léelo siempre como primer paso** cuando vas a hacer diagnóstico o plan completo.

Resumen rápido:

1. **Fundamentos técnicos** — Crawleable, rápido, schema mínimo
2. **Entidad de marca** — Wikidata, schema Organization, NAP consistente
3. **Arquitectura de contenido** — Cluster topical, pattern dual SEO+GEO
4. **E-E-A-T sistemático** — Authors con credenciales, revisión profesional, expertos
5. **Off-page distribuida** — Digital PR, listicles, Reddit, podcasts, embajadores
6. **UX, CRO y comportamiento** — Intent matching, CTR, dwell time, conversión
7. **Monitoring y feedback loop** — Tracking dual SEO + GEO, AI Citation Score

**Regla operativa crítica:** las capas se construyen en orden. No hacer Capa 5 (link building) si Capa 1 (técnico) está rota — es tirar plata.

---

## Modos de operación

Detectá qué quiere el usuario y operá en el modo correspondiente:

### Modo A — Diagnóstico

**Triggers:** "haz un diagnóstico SEO/GEO de [cliente.cl]", "auditoría SEO", "qué le falta a este cliente en orgánico"

**Proceso:**
1. Lee el archivo de vertical correspondiente
2. Lee `references/framework-7-layers.md`
3. Lee `references/diagnostic-checklist.md` (lista exhaustiva de qué chequear por capa)
4. Web fetch del home + 1-2 PDPs + colección principal + blog index
5. Web search de queries comerciales reales de la categoría en Chile para testear capa GEO
6. Web search de "marca + reseñas / opinión" para detectar social proof disperso
7. Genera output usando el template visual de `assets/diagnostic-template.md` (widget interactivo Imagine con 5 tabs: Resumen, SEO técnico, Contenido, GEO/LLMs, Roadmap)
8. Cierra con 5-7 quick wins priorizados por impacto vs esfuerzo

**Output esperado:** Widget interactivo + síntesis prose de fondo + CTA a propuesta upsell o brief técnico.

### Modo B — Plan estratégico

**Triggers:** "plan SEO/GEO completo", "cómo rankear #1", "roadmap orgánico 12 meses", "estrategia de contenido"

**Proceso:**
1. Lee `references/framework-7-layers.md` completo
2. Lee `references/12-month-plan.md` (sprints, milestones, deliverables)
3. Si ya hubo diagnóstico previo en la conversación, conectalo
4. Genera plan con 4 sprints de 90 días, deliverables por sprint, KPIs por capa
5. Incluí proyección honesta de timeline (mes 3, 6, 9, 12)
6. Cierre con opciones: convertir en propuesta, brief técnico, o sistematización

**Output:** Widget tipo "sistema completo" o docx según contexto.

### Modo C — Propuesta upsell

**Triggers:** "convierte esto en propuesta", "armame upsell SEO/GEO", "pricing SEO para [cliente]"

**Proceso:**
1. Lee `references/pricing-model.md` para tiers y rangos CLP
2. Conecta con la marca Advanz (tokens visuales `#0A0814`, gradiente `#C15DFF→#00DDFC`, Poppins)
3. Estructura: contexto del cliente → propuesta → tiers Base/Pro/Enterprise → ROI esperado → next steps
4. Usa formato HTML interactivo (no docx) salvo que el usuario pida explícitamente Word
5. Aplica el patrón de upsell post-Paid o post-Migración según el caso

**Output:** HTML interactivo branded Advanz con CTA a booking.

### Modo D — Brief técnico de implementación

**Triggers:** "brief Sprint 1", "cambios línea por línea", "qué le digo al dev", "implementación técnica"

**Proceso:**
1. Lee `references/implementation-guides/shopify-tech.md` (cambios específicos en theme.liquid, secciones, snippets)
2. Lee `references/implementation-guides/schema-snippets.md` (JSON-LD listos para copiar)
3. Lee `references/implementation-guides/copy-rewrites.md` (templates para title, meta, H1, descripciones PDP)
4. Si es Shopify, da paths exactos: `sections/header.liquid`, `templates/product.json`, `snippets/structured-data.liquid`
5. Si es WordPress, da plugins recomendados + cambios en functions.php
6. Incluí checklist de validación post-implementación

**Output:** Brief markdown estructurado, listo para enviar a Felipe, Matías o dev de turno.

### Modo E — Sistematización interna

**Triggers:** "esto debería ser una skill", "sistematízalo para Advanz", "generaliza para otros clientes"

**Proceso:**
1. Identifica qué pieza del trabajo es reutilizable
2. Pregunta si querés agregarlo como referencia nueva o como skill aparte
3. Si es referencia, genera el archivo dentro de la estructura adecuada
4. Si es skill nueva, invoca skill-creator

---

## Pattern dual SEO + GEO (la base de todo el contenido)

Cada pieza de contenido (blog post, PDP, página de categoría, FAQ) sigue este patrón:

```
H2 = pregunta literal del usuario (query de Google o LLM)

Primera oración = respuesta directa de 1-2 frases
(esto es lo que el LLM va a citar y lo que Google va a tomar como featured snippet)

Párrafo siguiente = expansión 40-80 palabras
(contexto, matices, condiciones)

Lista o tabla = detalles escaneables
(facilita extracción por LLMs y skim por humanos)

Cierre = cita o evidencia
(estudio, profesional con credenciales, dato medible)

Marcado = FAQPage, HowTo o Article schema según corresponda
```

Este patrón está expandido con ejemplos completos por vertical en `references/dual-content-pattern.md`.

---

## Tabla maestra: qué señal optimiza qué sistema

Cuando dudes sobre qué priorizar, usá esta tabla:

| Señal | Impacto SEO | Impacto GEO |
|---|---|---|
| Core Web Vitals | Alto | Bajo |
| Schema.org (Product, FAQ, Article) | Alto | Muy alto |
| Backlinks de autoridad | Muy alto | Medio |
| Menciones de marca sin link | Medio | Muy alto |
| Wikidata / Wikipedia | Medio | Muy alto |
| H2 = query exacto | Alto | Muy alto |
| Author boxes con credenciales | Alto (YMYL) | Alto |
| Reviews on-site con AggregateRating | Alto | Alto |
| Reviews dispersas en marketplaces | Bajo | Muy alto |
| Foros (Reddit, Quora, nicho) | Bajo | Muy alto |
| Long-form content (3000+ palabras) | Alto | Medio |
| Respuestas directas (40-60 palabras) | Medio | Muy alto |
| Internal linking | Alto | Medio |
| llms.txt en raíz | Nulo | Medio-alto |
| Branded search volume | Alto | Muy alto |

**Decisión por defecto:** apuntá a señales "muy alto en ambas" primero (schema, H2=query, branded search, Wikidata, AggregateRating).

---

## Métricas y KPIs

Tracking dual obligatorio. Detallado en `references/kpis-and-monitoring.md`.

**Stack SEO clásico:**
- Google Search Console (impresiones, clicks, CTR, posición)
- Ahrefs / Semrush (keywords, backlinks, share of voice)
- GA4 (tráfico orgánico, conversiones, comportamiento)
- Looker Studio dashboard semanal

**Stack GEO nuevo:**
- AI Citation Score (test mensual de 20-30 queries en ChatGPT, Claude, Gemini, Perplexity)
- Profound / Otterly / Peec.ai (automatización del tracking)
- Branded search volume (proxy de salud de marca)
- Share of model (% de queries de categoría donde aparece la marca)

**Cadencia:**
- Diaria: alertas automáticas (404s, caídas)
- Semanal: top 20 keywords + conversiones
- Mensual: AI Citation Score + content performance
- Trimestral: auditoría completa + ajuste de roadmap

---

## Reglas operativas no negociables

1. **Nunca prometas timeline de #1 en menos de 9 meses.** SEO/GEO real necesita 12 meses para dominar una categoría. Prometer menos es vender humo y quema el contrato.

2. **Nunca recomendes link building agresivo (PBNs, pago por link masivo).** En 2026 Google y LLMs lo detectan y penalizan. La estrategia es siempre digital PR + menciones orgánicas.

3. **Para clientes YMYL (suplementos, skincare, salud), E-E-A-T es no-negociable.** No puedes proponer contenido sin author boxes con credenciales y revisión profesional cuando aplique.

4. **Siempre considera la fricción con Paid Media.** SEO/GEO complementa, no canibaliza. Si el cliente tiene paid corriendo, mapea el overlap de keywords y el rol de cada canal.

5. **Para Shopify, usa paths exactos.** No genericeces — los devs internos de Advanz necesitan precision quirúrgica.

6. **Para reportes de cliente, usa Notion del workspace advanzgrowthpartner.** Nunca generes PDFs sueltos como deliverable sin Notion paralelo.

7. **Branding consistente.** Dark `#0A0814`, gradiente `#C15DFF→#00DDFC`, Poppins, glassmorphism. Aplicable a todos los HTML/widgets que sean cliente-facing.

8. **Disclaimer de proyecciones.** Toda proyección de mes 3/6/9/12 debe llevar nota de "estimación basada en ejecución consistente del plan; resultados varían por competencia, niche y velocidad de implementación".

---

## Estructura completa de referencias

Para no inflar este SKILL.md, todo el detalle vive en archivos separados. Léelos según el modo y vertical:

```
advanz-seo-geo-engine/
├── SKILL.md (este archivo)
├── references/
│   ├── framework-7-layers.md          ← Léelo SIEMPRE primero
│   ├── diagnostic-checklist.md        ← Lista exhaustiva por capa
│   ├── dual-content-pattern.md        ← Pattern + ejemplos
│   ├── 12-month-plan.md               ← Sprints, milestones
│   ├── pricing-model.md               ← Tiers Base/Pro/Enterprise
│   ├── kpis-and-monitoring.md         ← Stack y cadencia
│   ├── verticals/
│   │   ├── supplements.md
│   │   ├── apparel.md
│   │   ├── skincare.md
│   │   ├── pets.md
│   │   ├── food-bev.md
│   │   └── home-deco.md
│   └── implementation-guides/
│       ├── shopify-tech.md
│       ├── schema-snippets.md
│       └── copy-rewrites.md
├── assets/
│   ├── diagnostic-template.md         ← Estructura del widget
│   ├── proposal-template.md           ← Upsell post-Paid
│   └── client-onboarding-doc.docx     ← Doc educacional cliente
└── scripts/
    └── geo-citation-test.md           ← Protocolo manual de testing en LLMs
```

---

## Cierre

Este motor es el cerebro orgánico de Advanz. Úsalo para diagnosticar, planificar, vender, entregar y medir. Si encontrás algo que no está cubierto, agregalo como referencia nueva y avisame para mantenerlo vivo.

Resultado de uso correcto: clientes Advanz rankean #1-3 en sus categorías a 12 meses, son citados por defecto en LLMs en queries chilenas, y el orgánico empieza a aportar 30-40% del revenue total (vs ~10% promedio actual).
