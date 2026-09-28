# Advanz Ecomm Skills

Biblioteca de skills de Claude para operar **cualquier ecommerce DTC/B2C**: pauta (Meta y Google),
Search Console, SEO/GEO, CRO, PDP, ángulos de anuncios, construcción de tienda, email, benchmark
de competencia y más.

Las skills son genéricas. Lo específico de cada tienda vive en `clientes/<marca>/contexto-marca.md`,
así la misma biblioteca sirve para cualquier cliente.

## Catálogo

### Adquisición (pauta)

| Skill | Para qué |
|---|---|
| [`ecomm-meta-ads`](skills/ecomm-meta-ads/SKILL.md) | Estructura, auditoría, tracking (CAPI/EMQ), escalado y diagnóstico de Meta Ads |
| [`ecomm-google-ads`](skills/ecomm-google-ads/SKILL.md) | PMax, Shopping, feed/Merchant Center, Search de marca y genérico |
| [`ecomm-ad-angles`](skills/ecomm-ad-angles/SKILL.md) | Ángulos de anuncios → matriz ángulo × hook × formato × copy |
| [`advanz-video-intelligence`](skills/advanz-video-intelligence/SKILL.md) | Análisis de videos con personas y guiones UGC / talking head |
| [`viral-hooks`](skills/viral-hooks/SKILL.md) | Banco de hooks para anuncios y contenido |

### Orgánico (SEO / GEO)

| Skill | Para qué |
|---|---|
| [`ecomm-search-console`](skills/ecomm-search-console/SKILL.md) | Quick wins, CTR, canibalización, caídas e indexación desde GSC |
| [`advanz-seo-geo-engine`](skills/advanz-seo-geo-engine/SKILL.md) | Estrategia SEO + GEO en 7 capas, verticales, plan 12 meses |
| [`advanz-shopify-blog-publisher`](skills/advanz-shopify-blog-publisher/SKILL.md) | Blogs SEO/GEO para Shopify con schema y reglas YMYL |
| [`advanz-shopify-blog-api`](skills/advanz-shopify-blog-api/SKILL.md) | Publicar/corregir artículos por Admin API sin romper nada |

### Conversión (CRO / PDP)

| Skill | Para qué |
|---|---|
| [`ecomm-pdp-optimizer`](skills/ecomm-pdp-optimizer/SKILL.md) | Auditoría en 8 bloques y PDP reescrita lista para pegar |
| [`clarity-cro-audit`](skills/clarity-cro-audit/SKILL.md) | Ciclo CRO completo con Shopify + Clarity: diagnóstico, QA, rollback y readout |

### Tienda y stack

| Skill | Para qué |
|---|---|
| [`ecomm-store-builder`](skills/ecomm-store-builder/SKILL.md) | Construir o migrar una tienda: arquitectura, páginas, apps, tracking, lanzamiento |
| [`advanz-shopify-detector`](skills/advanz-shopify-detector/SKILL.md) | Detectar apps, tema y stack de cualquier tienda Shopify |

### Retención (email)

| Skill | Para qué |
|---|---|
| [`advanz-email-engine`](skills/advanz-email-engine/SKILL.md) | 18 acciones de email por fase y por nivel de facturación |
| [`advanz-email-diagnostico`](skills/advanz-email-diagnostico/SKILL.md) | Diagnóstico y madurez del canal email |

### Estrategia, investigación y competencia

| Skill | Para qué |
|---|---|
| [`advanz-ecomm-intelligence`](skills/advanz-ecomm-intelligence/SKILL.md) | Cerebro consultor con benchmarks 2025-26 (paid, CRO, retención, LATAM, nichos) |
| [`advanz-growth-engine`](skills/advanz-growth-engine/SKILL.md) | Marco de 8 etapas para diagnosticar y armar roadmap de un ecommerce |
| [`7-maletas`](skills/7-maletas/SKILL.md) | Investigación de cliente y mercado (por qué compran) |
| [`ecomm-benchmark-agent`](skills/ecomm-benchmark-agent/SKILL.md) | Benchmark competitivo: ads, funnel, SEO, prueba social, automatizaciones |
| [`ecomm-cyber-audit`](skills/ecomm-cyber-audit/SKILL.md) | Preparación y auditoría para Cyber / fechas peak |
| [`ecomm-scraping-cl`](skills/ecomm-scraping-cl/SKILL.md) | Scraping y detección de tiendas (Chile) |

## Flujo recomendado para un ecommerce nuevo

```
contexto-marca.md → 7-maletas → advanz-growth-engine (diagnóstico)
   ├─ tienda:     ecomm-store-builder → ecomm-pdp-optimizer → clarity-cro-audit
   ├─ pauta:      ecomm-ad-angles → ecomm-meta-ads + ecomm-google-ads
   ├─ orgánico:   ecomm-search-console → advanz-seo-geo-engine → blog-publisher
   └─ retención:  advanz-email-engine
```

## Instalación

### Claude Code: como plugin (recomendado para el equipo)

```
/plugin marketplace add advanzgrowthpartner/test
/plugin install advanz-ecomm-skills@advanz-ecomm
```

### Claude Code: copiar a tu carpeta personal

```bash
git clone https://github.com/advanzgrowthpartner/test.git advanz-ecomm-skills
cd advanz-ecomm-skills
./scripts/install.sh                 # todas
./scripts/install.sh ecomm-meta-ads  # solo algunas
```

### Claude Code: dentro del repo de un cliente

Copia las carpetas que necesites a `.claude/skills/` del repo del cliente y commitéalas. Todo el
que abra ese repo las tiene disponibles.

### claude.ai / app de escritorio

```bash
./scripts/package.sh   # genera dist/<skill>.zip
```

Sube cada zip en **Settings → Capabilities → Skills**.

## Adaptar a un ecommerce nuevo

1. `cp -r clientes/_plantilla clientes/<marca>`
2. Completa `clientes/<marca>/contexto-marca.md` (economía unitaria, producto, avatar, canales).
3. Pídele a Claude la tarea: *"audita el Meta Ads de <marca>"*, *"optimiza esta PDP"*,
   *"dame ángulos para <producto>"*. Las skills leen el contexto en el Paso 0 y piden lo que falte.

> Si el repo es público, no subas `clientes/<marca>/` con datos sensibles: mantenlo en el repo
> privado del cliente o agrégalo a `.gitignore`.

## Conectores que aprovechan las skills (opcionales)

Meta Ads MCP, Google/Ahrefs (GSC), Semrush, Shopify, Klaviyo, Notion. Si no están conectados, las
skills trabajan con exports (CSV/ZIP) o piden los datos.

## Reglas comunes

- Las skills **proponen**; ningún cambio en cuentas de pauta o en la tienda se ejecuta sin aprobación humana.
- Nunca inventan datos, reseñas ni cifras: lo estimado se marca como pendiente de validar.
- Solo ecommerce DTC/B2C (no B2B, SaaS ni lead gen).

## Contribuir

Cada skill es una carpeta con `SKILL.md` (frontmatter `name` + `description`) y opcionalmente
`references/`, `assets/`, `scripts/`. Para una skill nueva, copia la estructura de
`skills/ecomm-meta-ads/` y agrégala al catálogo de arriba.
