# Framework de las 7 Capas — Advanz SEO/GEO Engine

Este documento define el sistema completo. Las capas se construyen una sobre otra. **El orden importa.**

---

## Por qué este framework

En 2026, rankear bien significa optimizar dos sistemas en paralelo:

- **SEO clásico** — Google, Bing, otros buscadores tradicionales
- **GEO** (Generative Engine Optimization) — ChatGPT, Claude, Gemini, Perplexity, AI Overviews

Las señales se solapan pero no son idénticas. Las marcas que ganan son las que apilan capas correctamente.

---

## Capa 1 — Fundamentos técnicos crawleables

**Propósito:** Que Google y los crawlers de LLMs puedan acceder, leer y entender el sitio sin fricciones.

**Sin esto, nada funciona.** Es el piso mínimo no negociable.

### Checklist técnico

- **Core Web Vitals en verde**
  - LCP <2.5s en mobile (datos CrUX, no Lighthouse desktop)
  - INP <200ms
  - CLS <0.1
  - Para Shopify, fixes típicos: lazy loading correcto, font-display: swap, hero sin layout shift, JS no bloqueante

- **Indexabilidad correcta**
  - `robots.txt` no bloquea rutas críticas
  - `sitemap.xml` enviado a Search Console y Bing Webmaster
  - Canonical apunta al URL deseado (no a variantes ni filtros)
  - Hreflang configurado si hay multiidioma o multipaís
  - Sin páginas duplicadas (variantes de producto canonicalizadas)

- **Schema mínimo viable**
  - `Organization` en home + footer
  - `Product` + `Offer` + `AggregateRating` en cada PDP
  - `FAQPage` donde hay preguntas frecuentes
  - `BreadcrumbList` en navegación
  - `Article` en blog posts
  - JSON-LD validado en Schema Markup Validator y Rich Results Test

- **URLs limpias y semánticas**
  - Sin parámetros innecesarios
  - Sin typos (chequear cada slug — pasa más seguido de lo que parece)
  - Slugs ricos en keyword pero naturales
  - Estructura jerárquica clara: `/collections/{categoría}/{producto}`

- **Mobile-first impecable**
  - Tap targets ≥44px
  - Sin overlays bloqueando contenido
  - Misma información que desktop (Google indexa mobile)
  - Performance mobile específica (no asumir que desktop optimizado = mobile OK)

- **llms.txt en la raíz** (emergente, GEO)
  - Archivo markdown en `/llms.txt`
  - Lista las páginas que querés que LLMs usen como contexto canónico
  - Aún no es estándar, pero Anthropic y otros ya lo respetan parcialmente

### Output esperado de Capa 1

Sitio limpio, rápido, indexable, con datos estructurados. Google Search Console sin errores críticos. Lighthouse mobile >85.

---

## Capa 2 — Entidad de marca

**Propósito:** Que Google y LLMs sepan qué es tu marca, dónde, desde cuándo, quién la lidera, y la traten como entidad reconocida (no solo como string).

**Esta es la capa más subestimada y la de mayor leverage para GEO.**

### Checklist de entidad

- **Entrada en Wikidata**
  - Crear Q-item con: nombre legal, fundación, fundador, sede, industria, productos, distribuidores tier 1
  - No requiere Wikipedia
  - Es la fuente que más LLMs consultan para "saber" que una marca existe
  - 1-2 horas de trabajo, impacto desproporcionado

- **Schema Organization completo en home**
  ```json
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Nombre Comercial",
    "legalName": "Razón Social SpA",
    "foundingDate": "2022-01-01",
    "founder": { "@type": "Person", "name": "Nombre Fundador" },
    "address": { "@type": "PostalAddress", "addressLocality": "Santiago", "addressCountry": "CL" },
    "url": "https://dominio.cl",
    "logo": "https://dominio.cl/logo.png",
    "sameAs": [
      "https://www.instagram.com/marca",
      "https://www.tiktok.com/@marca",
      "https://www.mercadolibre.cl/perfil/marca",
      "https://www.wikidata.org/wiki/QXXXXXX"
    ]
  }
  ```
  - El campo `sameAs` es el que más mueve la aguja
  - Conecta el sitio con la entidad distribuida en redes y marketplaces

- **About page con narrativa estructurada**
  - No copy emocional vago
  - Estructura clara: qué hace la marca → desde cuándo → dónde → fundador (con nombre completo) → problema que resuelve → certificaciones → premios → prensa
  - Los LLMs extraen esto como bio canónica
  - Schema Person para el fundador si aplica

- **NAP consistente cross-canal**
  - Nombre, dirección, teléfono idénticos en web, Google Business, Instagram, TikTok, marketplaces
  - Cualquier discrepancia (comas, tildes, mayúsculas) confunde la entidad
  - Hacer auditoría inicial y crear documento maestro

- **Google Business Profile activo**
  - Aunque seas ecommerce puro, GBP construye entidad local
  - Categoría exacta
  - Fotos reales del producto y/o equipo
  - Posts semanales
  - Q&A respondido por el dueño
  - Reviews trabajadas activamente

### Output esperado de Capa 2

La marca aparece como entidad en Knowledge Graph de Google. LLMs reconocen el nombre cuando se pregunta por la categoría. Branded search empieza a subir.

---

## Capa 3 — Arquitectura de contenido

**Propósito:** Construir autoridad temática completa sobre la categoría. No keywords sueltas — clusters.

### Modelo cluster topical

```
                    Pillar (comercial)
              "Mejores [categoría] en Chile 2026"
                          │
        ┌─────────────┬───┴───┬─────────────┬──────────────┐
        │             │       │             │              │
   Informacional  Comparativo  Caso uso    Caso uso     Caso uso
   "¿Qué es X?"   "X vs Y"     específico  específico   específico
                                 1            2             3
        │             │       │             │              │
        └─────────────┴───────┴─────────────┴──────────────┘
                          │
              Links a PDPs y colecciones
```

### Tipos de contenido por intent

| Tipo | Propósito | Ejemplo (electrolitos) |
|---|---|---|
| Pillar | Pregunta madre, comercial | "Mejores electrolitos en Chile 2026" |
| Informacional | Captura intent educativo | "¿Qué son los electrolitos?" |
| Comparativo | Captura intent decisión | "Marca A vs Marca B vs Marca C" |
| Caso uso | Long-tail específico | "Electrolitos para resaca", "para niños", "para ayuno" |
| PDP | Conversión final | Página de producto enriquecida |
| Colección | Captura genérico comercial | /collections/electrolitos |

### Pattern dual SEO + GEO por pieza

Cada pieza sigue este patrón (detallado en `dual-content-pattern.md`):

```
H2 = pregunta literal del usuario

Primera oración = respuesta directa (1-2 frases)
   ← esto lo cita el LLM, esto va al featured snippet

Párrafo = expansión 40-80 palabras

Lista o tabla = detalles escaneables

Cierre = cita o evidencia con autor/estudio

Schema = FAQPage / HowTo / Article
```

### Internal linking semántico

- Cada pillar recibe links de TODOS sus soportes
- Cada PDP recibe link desde pillar comercial + 2-3 soportes
- Anchor varied (no exact-match repetido)
- Crea grafo denso que Google y LLMs leen como "tema dominado"

### Volumen mínimo viable

Por categoría principal del cliente:
- 1 pillar (3000-5000 palabras)
- 5-8 soportes (1200-2500 palabras cada uno)
- PDPs enriquecidos con descripción completa, tabla nutricional/spec en HTML, FAQ rica
- Colecciones con intro + outro (200-300 palabras cada uno)

### Output esperado de Capa 3

Cluster topical completo publicado en 8-12 semanas. Internal linking denso. Rankings empiezan a aparecer en posiciones 20-40 al mes 3 y subir.

---

## Capa 4 — E-E-A-T sistemático

**Propósito:** Demostrar Experience, Expertise, Authoritativeness, Trust. En categorías YMYL es factor #1 para Google y multiplicador fuerte para citas en LLMs.

### Categorías YMYL (Your Money Your Life)

Si tu cliente está en una de estas, E-E-A-T es no negociable:
- Salud y wellness (suplementos, skincare con claims, dispositivos médicos)
- Finanzas (créditos, seguros, inversiones)
- Legal
- Información cívica/electoral
- Seguridad (productos para niños, autos, etc.)

### Componentes E-E-A-T

- **Author boxes con credenciales verificables**
  - Cada artículo firmado por persona real
  - Foto, bio 2-3 líneas, credenciales (nutricionista, MD, MSc, etc.)
  - Link a LinkedIn o web personal
  - Schema Person + mainEntityOfPage
  - Si no hay autor calificado interno, contratá freelance (costo marginal)

- **Revisión médica/profesional en YMYL**
  - "Revisado médicamente por Dr. X" + fecha + link a perfil
  - Schema `reviewedBy` con Person
  - Aplica a: artículos sobre salud, dosis, condiciones, embarazo, niños

- **Página de "Expertos que recomiendan"**
  - Directorio público de profesionales que avalan la marca
  - Foto, especialidad, credenciales (RUT colegio profesional si aplica)
  - Cada perfil con schema Person
  - Esta es la página E-E-A-T más alto-leverage en categoría salud — casi nadie la hace bien
  - Aplica a suplementos, skincare, mascotas (con veterinarios), food (con nutricionistas)

- **Certificaciones visibles**
  - Logos en footer + página dedicada con explicación
  - Para Chile: ISP (Instituto de Salud Pública), INTA, registros sanitarios, ISO, sello SAG si aplica, código de barras GS1
  - Para ingredientes activos: link al estudio científico que respalda la afirmación

- **Trust signals en cada página**
  - Reviews promedio visibles
  - Número de clientes atendidos
  - Años en el mercado
  - Garantía de devolución
  - Contacto humano visible (WhatsApp, teléfono, email)
  - Política de privacidad y términos accesibles

### Output esperado de Capa 4

Sitio que Google y LLMs reconocen como autoridad temática. Mejora notable en rankings YMYL al mes 4-6.

---

## Capa 5 — Off-page distribuida

**Propósito:** Construir presencia en las fuentes que Google y LLMs consideran confiables, distribuida entre múltiples tipos de menciones.

**El juego cambió:** link building agresivo ya no funciona. La estrategia es presencia orgánica distribuida.

### Mix recomendado (mensual, sostenido)

| Tipo | Frecuencia | Impacto SEO | Impacto GEO |
|---|---|---|---|
| Digital PR en medios tier 1-2 | 1-2/mes | Muy alto | Muy alto |
| Guest posts en blogs nicho | 2/mes | Alto | Medio |
| Podcasts (founder o experto) | 1/mes | Medio | Alto |
| Aparición en listicles externos | Continuo | Alto | Muy alto |
| Foros nicho con valor real | 2-4/mes | Bajo | Muy alto |
| Reviews UGC en marketplaces | Continuo | Bajo | Muy alto |
| Embajadores con contenido propio | Continuo | Medio | Alto |
| Reddit + Quora orgánico | 2-4/mes | Bajo | Muy alto |

### Por qué Reddit y foros importan tanto en GEO

Los LLMs (especialmente ChatGPT y Claude) tienen Reddit como fuente principal de "qué piensa la gente real". Una mención orgánica en r/chile, r/CL_Skincare, r/runningChile, o foros nicho vale más para citas en LLMs que 3 backlinks de blogs de bajo tráfico.

**Reglas para Reddit/Quora:**
- Nunca spam
- Aportar valor primero (responder preguntas, compartir experiencias)
- La marca aparece solo cuando es relevante orgánicamente
- Account aged 3-6+ meses antes de empezar
- Mejor que la cuenta sea de empleado real, no de "marca"

### El asset más subestimado: listicles externos

Cuando un usuario pregunta a ChatGPT "mejores [categoría] en Chile", el LLM sintetiza lo que dicen los listicles existentes. Si no estás en esos listicles, no existís.

**Estrategia:**
1. Identifica los 20 listicles que ya rankean para tu query principal
2. Outreach a los autores: ofrecer muestras de producto, datos exclusivos, entrevista con founder
3. Conseguir aparecer en al menos 5-8 de ellos en 6 meses
4. Para listicles que no podés influenciar, crear el tuyo propio (con criterio editorial honesto, no listicle de marca)

### Por qué digital PR > link building

- Una mención en El Mostrador Bienestar genera: link + brand mention + tráfico referral + autoridad para LLMs
- Un link de un blog de PBN genera: nada útil + riesgo de penalización
- El costo es similar; el ROI es 10x diferente

### Output esperado de Capa 5

10+ menciones tier 1-2 acumuladas al mes 9. Aparición en 5+ listicles externos top. Branded search creciendo 30-50% mes a mes.

---

## Capa 6 — UX, CRO y señales de comportamiento

**Propósito:** Que el usuario que llega a la página se quede, lea, convierta. Google mide esto y lo usa como ranking factor.

### Componentes

- **Search intent matching milimétrico**
  - Si query es informacional → página abre con respuesta, no con CTA de compra
  - Si query es comercial → producto visible above the fold
  - Si query es comparativo → comparación clara, no solo promoción de marca propia
  - Confundir intent es la causa #1 de páginas que rankean fugaz y caen

- **Title + meta que ganan el click**
  - Title con keyword + diferenciador + número/año si aplica
  - Meta con beneficio claro + CTA implícito
  - Probar variantes con datos de Search Console
  - Largo correcto: title 50-60 chars, meta 140-160 chars

- **PDPs que responden objeciones antes de que aparezcan**
  - Ingredientes/specs en HTML (no en imagen)
  - Tabla nutricional/comparativa crawleable
  - Comparación con alternativas frecuentes
  - FAQ de 6-8 preguntas
  - Reviews con foto
  - Política de devolución visible
  - Envío y plazo de entrega claros

- **Velocidad real, no solo Lighthouse**
  - CrUX data (datos reales de Chrome) es lo que Google usa
  - Optimizar para percentil 75 de usuarios mobile en redes 3G/4G chilenas
  - No para desktop con fibra Vitacura

- **Conversión como señal de calidad**
  - Página que convierte = usuario satisfecho = señal positiva
  - Trabajar CRO sobre PDPs impacta SEO indirectamente
  - Tests A/B continuos en above-the-fold, CTA, copy

### Output esperado de Capa 6

CTR en SERP +20-40% sobre baseline. Dwell time +50%. Conversión orgánica 2-3x.

---

## Capa 7 — Monitoring y feedback loop

**Propósito:** Lo que no se mide no se optimiza. Tracking dual obligatorio.

### Stack SEO clásico

- **Google Search Console**
  - Impresiones, clicks, CTR, posición media por query
  - Errores de cobertura
  - Performance por país y dispositivo

- **Ahrefs o Semrush**
  - Keyword tracking
  - Backlinks (cantidad y calidad)
  - Share of voice vs competidores
  - Content gap analysis

- **GA4**
  - Tráfico orgánico
  - Conversiones por landing
  - Comportamiento (engagement rate, sessions per user)

- **Looker Studio dashboard semanal**
  - Top 20 KW
  - Evolución de posiciones
  - Conversiones orgánicas
  - Gaps vs competidores

### Stack GEO nuevo

- **AI Citation Score**
  - Test mensual de 20-30 queries en ChatGPT, Claude, Gemini, Perplexity
  - Tracking: si la marca aparece, en qué posición, con qué contexto, citada con link o sin link
  - Documento de seguimiento en Notion del cliente

- **Plataforma GEO** (al menos una)
  - Profound — más maduro, US-centric
  - Otterly — más barato, multi-engine
  - Peec.ai — España, buena cobertura LATAM
  - Automatiza el tracking de citas

- **Branded search volume**
  - Proxy de salud de marca
  - Correlaciona fuerte con citas LLM
  - Monitorear en Search Console + Google Trends

- **Share of model**
  - % de queries de la categoría donde aparece la marca vs competencia
  - Métrica de "dominancia" en LLMs

### Cadencia

| Frecuencia | Qué se mide | Quién |
|---|---|---|
| Diaria | Errores 404, caídas de tráfico, alertas Search Console | Automático |
| Semanal | Top 20 keywords, conversiones orgánicas, nuevos backlinks | Strategist |
| Mensual | AI Citation Score, share of model, content performance | Strategist + Founder |
| Trimestral | Auditoría técnica completa, ajuste de roadmap, benchmark | Equipo completo |

### Output esperado de Capa 7

Dashboard claro de salud SEO + GEO. Decisiones basadas en data, no en intuición. Cliente con visibilidad total del progreso.

---

## Resumen visual del framework

```
┌──────────────────────────────────────────────────────────────┐
│ Capa 7 — Monitoring y feedback loop                          │
├──────────────────────────────────────────────────────────────┤
│ Capa 6 — UX, CRO y comportamiento                            │
├──────────────────────────────────────────────────────────────┤
│ Capa 5 — Off-page distribuida (PR, listicles, foros)         │
├──────────────────────────────────────────────────────────────┤
│ Capa 4 — E-E-A-T sistemático (authors, expertos, certs)      │
├──────────────────────────────────────────────────────────────┤
│ Capa 3 — Arquitectura de contenido (cluster topical)         │
├──────────────────────────────────────────────────────────────┤
│ Capa 2 — Entidad de marca (Wikidata, schema Org, NAP)        │
├──────────────────────────────────────────────────────────────┤
│ Capa 1 — Fundamentos técnicos (CWV, schema, mobile, llms.txt)│
└──────────────────────────────────────────────────────────────┘
```

Construir de abajo hacia arriba. Saltar capas = falla del sistema.
