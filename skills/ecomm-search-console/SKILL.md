---
name: ecomm-search-console
description: "Análisis de Google Search Console para cualquier ecommerce: quick wins (posición 4-20 con impresiones), CTR bajo vs curva esperada, canibalización de keywords, páginas que caen, cobertura/indexación, Core Web Vitals, marca vs no-marca y plan de acción por URL (PDP, colección, blog). Usa SIEMPRE que digan 'Search Console', 'GSC', 'export de Search Console', 'por qué bajó mi tráfico orgánico', 'CTR bajo', 'quick wins SEO', 'keywords en página 2', 'canibalización', 'páginas no indexadas', 'cobertura', 'Core Web Vitals', 'qué keywords me traen tráfico', 'reporte SEO mensual'. SOLO ecommerce. Para estrategia SEO/GEO completa usar advanz-seo-geo-engine."
---

# Search Console para Ecommerce

GSC es la fuente de verdad de lo que Google **ya** piensa de la tienda. Esta skill la convierte en
una lista de acciones por URL. La estrategia SEO/GEO completa vive en `advanz-seo-geo-engine`.

## Paso 0 — Fuente de datos (en este orden)

1. **MCP de Ahrefs con GSC conectado** (`mcp__Ahrefs__gsc-keywords`, `gsc-pages`, `gsc-ctr-by-position`, `gsc-performance-history`, `gsc-page-history`). Usa `doc` antes del primer uso.
2. **Export ZIP de GSC** (`Consultas.csv`, `Páginas.csv`, `Gráfico.csv`, `Países.csv`, `Dispositivos.csv`). Procesar con pandas, nunca a ojo.
3. Sin datos: pedirlos. **No inventar posiciones ni clics.** Lo estimado se marca como "pendiente de validar".

Ventana estándar: últimos 3 meses vs 3 meses anteriores (y YoY si hay estacionalidad, p.ej. Cyber).
Carga también `clientes/<marca>/contexto-marca.md` para saber el término de marca y las categorías.

## Paso 1 — Segmentar antes de analizar

- **Marca vs no-marca** (regex con nombre de marca y errores de tipeo). El crecimiento real es no-marca.
- **Tipo de URL** por patrón Shopify: `/products/` (PDP), `/collections/` (colección), `/blogs/` (blog), `/pages/`, home.
- **Dispositivo**: móvil suele ser > 70%.

## Paso 2 — Los 6 análisis

| # | Análisis | Filtro | Acción |
|---|---|---|---|
| 1 | **Quick wins** | Posición 4-20, impresiones altas, no-marca | Reforzar on-page: title, H1, contenido, enlaces internos desde páginas fuertes |
| 2 | **CTR bajo** | CTR < esperado para su posición (ver curva abajo) | Reescribir title + meta description; añadir schema (Product, FAQ, Review) para rich results |
| 3 | **Canibalización** | Misma query con 2+ URLs rankeando alternadas | Elegir URL canónica, consolidar/redirigir, ajustar enlazado interno |
| 4 | **Caídas** | URLs con −30% clics período vs período | Revisar cambios recientes, indexación, competencia en SERP, actualización de algoritmo |
| 5 | **Contenido faltante** | Queries con impresiones sin URL que responda bien (ranking de home o blog genérico) | Crear colección o artículo dedicado |
| 6 | **Salud técnica** | Cobertura, CWV, sitemaps, mejoras | Ver checklist técnico |

**Curva de CTR orientativa (orgánico, no-marca, 2025):** pos 1 ≈ 25-30% · 2 ≈ 13-16% · 3 ≈ 9-11% ·
4-5 ≈ 5-7% · 6-10 ≈ 2-4% · 11-20 ≈ < 1.5%. Con AI Overviews o Shopping arriba, esperar menos.
Si hay MCP, usa la curva real del sitio (`gsc-ctr-by-position`) en vez de la genérica.

## Paso 3 — Checklist técnico para Shopify

- Variantes y parámetros (`?variant=`) canonicalizados al producto.
- Colecciones filtradas (`/collections/x/tag`) sin indexar si duplican.
- `/collections/all` y búsqueda interna fuera del índice.
- Productos agotados permanentes: 301 a sustituto o colección, no 404 masivo.
- Sitemap enviado; "Descubierta, no indexada" alta = problema de calidad o enlazado.
- CWV móvil: LCP < 2.5s, INP < 200ms, CLS < 0.1. Apps pesadas → `advanz-shopify-detector`.

## Paso 4 — Priorizar

Puntaje por URL = impresiones × (CTR esperado − CTR actual) → clics potenciales. Ordenar por clics
potenciales y multiplicar por CVR y AOV de la tienda para expresarlo en **revenue potencial**.

## Paso 5 — Entregable

1. Resumen: clics, impresiones, CTR, posición; marca vs no-marca; tendencia.
2. Top 10 quick wins (URL, query, posición, impresiones, acción concreta, revenue potencial).
3. Top CTR a reescribir con **title y meta propuestos** listos para pegar.
4. Canibalizaciones con URL ganadora.
5. Issues técnicos.
6. Plan 30 días y qué medir a los 14/28 días (GSC tarda ~2-4 semanas en reflejar).

## Reglas

- H2 y FAQs con la **formulación literal de la query** de GSC.
- Títulos de PDP: [Producto] + [atributo] + [marca], ≤ 60 caracteres visibles.
- Implementar en blogs de Shopify → `advanz-shopify-blog-api` / `advanz-shopify-blog-publisher`.
- Estrategia de clusters, entidad, E-E-A-T, GEO → `advanz-seo-geo-engine`.
