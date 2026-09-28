# Template Visual de Diagnóstico

Estructura del widget interactivo Imagine que Claude debe generar cuando opera en Modo A (Diagnóstico).

---

## Estructura del widget — 5 tabs

### Tab 1 — Resumen Ejecutivo

Contenido:
- Score global (X/100)
- Score SEO (X/100) y Score GEO (X/100) separados
- 5 quick wins en cards
- 3 áreas críticas a resolver
- Estimación de tiempo a resultados visibles

Visual:
- 3 cards grandes con scores en la parte superior
- Gráfico de barras horizontal: 7 capas con su % completitud
- Lista de quick wins con icono de impacto/esfuerzo
- CTA a propuesta o brief técnico

### Tab 2 — SEO Técnico

Contenido:
- Core Web Vitals: LCP, INP, CLS con valores actuales
- Indexabilidad: robots, sitemap, canonical
- Schema implementado: lista de qué hay y qué falta
- URLs: typos, estructura, parámetros
- Mobile: tap targets, contenido visible

Visual:
- Tabla con 2 columnas: ítem vs estado (✅⚠️❌)
- Screenshots si aplica

### Tab 3 — Contenido

Contenido:
- Pillar comercial: existe / falta
- Soportes informacionales: # publicados vs ideal
- Soportes comparativos: # vs ideal
- PDPs enriquecidos: %
- Pattern dual SEO+GEO: %
- Internal linking: denso / disperso / ausente
- Cluster topical: completo / parcial / inexistente

Visual:
- Diagrama del cluster ideal
- Gaps marcados en rojo
- Lista de piezas a crear con prioridad

### Tab 4 — GEO / LLMs

Contenido:
- AI Citation Score actual: X/Y queries testeadas
- Apariciones por LLM: ChatGPT X, Claude Y, Gemini Z, Perplexity W
- Posicionamiento: primaria / secundaria / no aparece
- Competidores que sí aparecen
- Wikidata: sí / no
- Schema Organization: completo / parcial / ausente
- llms.txt: sí / no
- Menciones en foros: detectadas / no detectadas

Visual:
- Tabla de queries con cells por LLM mostrando aparición
- Comparativa vs top 3 competidores
- Lista de acciones GEO prioritarias

### Tab 5 — Roadmap

Contenido:
- Mes 1: foco + deliverables
- Mes 2-3: foco + deliverables
- Mes 4-6: foco + deliverables
- Mes 7-9: foco + deliverables
- Mes 10-12: foco + deliverables

Visual:
- Timeline horizontal con milestones
- Proyección de KPIs por trimestre
- Disclaimer de proyección

---

## Tokens de marca Advanz

Aplicar siempre:
- Background: `#0A0814`
- Gradient: `linear-gradient(135deg, #C15DFF 0%, #00DDFC 100%)`
- Texto principal: blanco / `rgba(255,255,255,0.85)`
- Texto secundario: `rgba(255,255,255,0.6)`
- Cards: glassmorphism `background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);`
- Font: Poppins, weights 300/400/500/600
- Borders: `1px solid rgba(255,255,255,0.1)`
- Border radius: `12px` para cards, `6px` para badges

## CTAs sugeridos al final del widget

3 botones que invoquen `sendPrompt()`:

1. "Convertir en propuesta upsell ↗" → propuesta cliente
2. "Generar brief técnico Sprint 1 ↗" → brief para dev
3. "Plan completo 12 meses ↗" → plan estratégico

---

## Loading messages para el widget

Variar según vertical:

**Suplementos:**
- "Escaneando schema de suplementos"
- "Testeando citas en LLMs"
- "Auditando E-E-A-T del cluster"
- "Calibrando para mercado chileno"

**Ropa:**
- "Analizando visual SEO"
- "Revisando schema Product variants"
- "Mapeando cluster por estilo"
- "Testeando presencia en Pinterest"

**Skincare:**
- "Revisando ingredientes activos"
- "Auditando claims regulatorios"
- "Mapeando cluster por tipo de piel"
- "Testeando GEO en queries beauty"

Mantener los mismos principios de loading messages del read_me (5-7 palabras, sin jargon dramatizado, neutros).
