---
name: ecomm-google-ads
description: "Estrategia, estructura, auditoría y optimización de Google Ads para cualquier ecommerce DTC/B2C: Performance Max, Shopping, Merchant Center y feed de productos, Search de marca y genérico, remarketing/YouTube, Enhanced Conversions, negativas y canibalización de marca. Usa SIEMPRE que digan 'Google Ads', 'PMax', 'Performance Max', 'Shopping', 'Merchant Center', 'feed de productos', 'títulos del feed', 'productos rechazados', 'campaña de marca', 'keywords', 'negativas', 'search terms', 'audita mi Google Ads', 'Enhanced Conversions', 'YouTube Ads', 'canibalización de marca', 'escalar Google'. SOLO ecommerce — NO lead gen, B2B ni SaaS."
---

# Google Ads para Ecommerce

## Paso 0 — Contexto de marca

Carga `clientes/<marca>/contexto-marca.md` (plantilla en `clientes/_plantilla/`). Mínimo necesario:
país, AOV, margen bruto, catálogo (SKUs, categorías), gasto actual, plataforma (Shopify u otra),
estado de Merchant Center, % de revenue que viene de búsquedas de marca.

Fórmulas: ROAS break-even = 1 / margen · CPA máx = AOV × margen · presupuesto diario mínimo = CPA × 3.

## Paso 1 — Tracking

1. Conversión **Purchase como acción PRINCIPAL** (no secundaria). Revisar que no haya duplicados (GA4 importado + tag nativo contando doble).
2. **Enhanced Conversions** activadas.
3. GA4 con eventos ecommerce: `view_item`, `add_to_cart`, `begin_checkout`, `purchase` con value y currency.
4. Vinculaciones: Google Ads ↔ GA4 ↔ Merchant Center ↔ Search Console.
5. Consent Mode v2 donde aplique.

## Paso 2 — Arquitectura en 4 capas

| Capa | % presupuesto | Objetivo | Notas |
|---|---|---|---|
| Performance Max | 50-60% | Feed + Shopping + Search + YouTube + Display | Asset groups por categoría. Señales de audiencia (no restricciones). **Excluir términos de marca.** |
| Search Marca | 10-15% | Proteger marca | Exacta + frase. ROAS 8-15x. |
| Search No-marca | 15-25% | Long-tail de alta intención | "[tipo de producto] comprar [país]". Revisar search terms semanal. |
| Remarketing / YouTube | 10-15% | Recordación | Secundario, no motor. |

Cuentas chicas (< USD 2k/mes): 1 PMax (o Standard Shopping) + 1 Search marca. Nada más.

## Paso 3 — Feed = 80% del éxito en Shopping

| Campo | Regla |
|---|---|
| Título | [Marca] + [Producto] + [Atributo clave] + [Variante]. Keywords al inicio. Máx 150. **Nunca el default de Shopify.** |
| Descripción | Beneficios + keywords en los primeros 150 caracteres. Sin relleno de marketing. |
| Imagen | Fondo blanco, ≥ 800×800, sin texto sobreimpreso. |
| Precio / stock | Sync en tiempo real. Google castiga fuerte el sin-stock. |
| GTIN / MPN / brand | Obligatorio para matching. Si es marca propia sin GTIN: `identifier_exists = no`. |
| google_product_category | La más específica de la taxonomía. |
| custom_label_0-4 | Margen, bestseller, nuevo, temporada, rango de precio → segmentar PMax. |

Títulos optimizados solos: +20-40% CTR. Apps: DataFeedWatch, Simprosys, Feedonomics o reglas del
propio Merchant Center.

**Diagnóstico de Merchant Center:** productos rechazados, advertencias, precio no coincide,
políticas (salud, claims), envío y devoluciones configurados.

## Paso 4 — Search: keywords y negativas

- Estructura por intención, no por match type: marca / categoría / problema / competidor.
- Revisar **search terms cada semana**; negativizar lo informacional ("qué es", "gratis", "DIY", "trabajo").
- Lista de negativas compartida a nivel cuenta.
- Para ideas y volumen usa Semrush/Ahrefs (MCP si están conectados) o Keyword Planner; cruza con Search Console → skill `ecomm-search-console`.

## Paso 5 — Trampas frecuentes

- **Canibalización de marca por PMax**: si > 70% del revenue de PMax viene de marca, está comiendo tráfico orgánico. Separar Search marca + excluir marca en PMax + medir ROAS no-marca.
- **PMax con feed pobre**: optimizar el feed antes de subir presupuesto.
- **Conversión secundaria mal configurada**: Smart Bidding optimiza a lo que ve.
- **Cambiar tROAS > 15-20% de golpe**: reinicia aprendizaje.

## Paso 6 — Diagnóstico por métrica

| Síntoma | Causa | Acción |
|---|---|---|
| Impresiones bajas en Shopping | Feed / presupuesto / tROAS muy alto | Arreglar feed, bajar tROAS 10% |
| CTR bajo Shopping | Título, imagen o precio no competitivo | Reescribir título, revisar precio vs competencia |
| CTR ok, CVR bajo | PDP / checkout | skill `ecomm-pdp-optimizer` / `clarity-cro-audit` |
| ROAS alto pero no escala | Todo es marca | Separar marca, invertir en no-marca |
| Google cae 2-3 semanas después de apagar Meta | Meta creaba la demanda | Decidir con MER, no ROAS por plataforma |

## Paso 7 — Entregable

Resumen ejecutivo → números vs break-even → hallazgos priorizados (tracking, feed, estructura,
pujas, keywords) → plan 30 días → supuestos. Incluye siempre el % marca vs no-marca.

## Reglas

- No hacer cambios en la cuenta sin aprobación explícita.
- Profundizar: `advanz-ecomm-intelligence/references/paid-media.md`, `benchmarks.md`, `latam-context.md`.
- Competencia: Google Ads Transparency Center (`ecomm-benchmark-agent/references/ads-intelligence.md`).
- Orquestación Meta + Google: Meta crea demanda, Google la captura. Reparto típico 60-70% Meta / 25-35% Google; ajustar con MER.
