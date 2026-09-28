---
name: ecomm-meta-ads
description: "Estrategia, estructura, auditoría y optimización de Meta Ads (Facebook + Instagram) para cualquier ecommerce DTC/B2C. Cubre arquitectura Cold/Warm/Hot, Advantage+ Shopping (ASC), audiencias, tracking (Pixel + CAPI + EMQ), catálogo/DPA, testing creativo, fatiga, reglas de escalado y diagnóstico por métrica. Usa SIEMPRE que digan 'Meta Ads', 'Facebook Ads', 'Instagram Ads', 'campañas de Meta', 'audita mi cuenta de Meta', 'ASC', 'Advantage+', 'CAPI', 'pixel', 'EMQ', 'catálogo de Meta', 'DPA', 'retargeting', 'lookalike', 'escalar campañas', 'me subió el CPA', 'bajó el ROAS', 'fatiga creativa', 'estructura de cuenta', 'presupuesto de Meta', 'test creativo'. SOLO ecommerce — NO lead gen, B2B ni SaaS."
---

# Meta Ads para Ecommerce

Skill transferible: funciona para cualquier tienda. La especificidad viene del **contexto de marca**,
no de la skill.

## Paso 0 — Cargar el contexto de la marca

Antes de recomendar nada, busca `clientes/<marca>/contexto-marca.md` (plantilla en
`clientes/_plantilla/contexto-marca.md`). Si no existe, pide como mínimo:

| Dato | Por qué importa |
|---|---|
| País / moneda | Benchmarks de CPM, CPA y medios de pago cambian por mercado |
| AOV y margen bruto | Define CPA máximo y ROAS break-even |
| Compras/semana atribuidas a Meta | Decide ASC broad vs lookalikes |
| Gasto mensual actual | Define cuántas campañas soporta la cuenta |
| Tracking: Pixel, CAPI, EMQ | Sin CAPI los datos no son confiables — se arregla antes que todo |
| Top 3 productos y sus reseñas | Solo se escala a PDPs con prueba social suficiente |

**Fórmulas base (muestra siempre el cálculo):**

- ROAS break-even = 1 / margen bruto (%) → margen 60% ⇒ ROAS BE 1.67
- CPA máximo = AOV × margen bruto
- Presupuesto diario mínimo por conjunto = CPA objetivo × 3
- MER = revenue total / inversión total en pauta (la métrica que manda)

## Paso 1 — Tracking primero (no negociable)

1. Pixel + **Conversions API server-side** (nativa de Shopify o vía GTM server). Sin CAPI se pierde ~40% de señal post-iOS14.
2. **EMQ ≥ 6.0** en Purchase. Enviar email, teléfono, fbp, fbc, external_id.
3. Dominio verificado + eventos priorizados.
4. Deduplicación event_id entre Pixel y CAPI.
5. Catálogo sincronizado sin errores (precio, stock, imágenes).

Si hay MCP de Meta disponible (`mcp__Meta_MCP__ads_get_dataset_quality`,
`ads_catalog_get_diagnostics`), úsalo para verificar en vez de preguntar.

## Paso 2 — Arquitectura de cuenta

| Capa | % presupuesto | Tipo | Audiencia | Creativos | ROAS esperado |
|---|---|---|---|---|---|
| Cold (prospección) | 60% | ASC o CBO broad | Broad, o LAL 1-3% de compradores | UGC, problema→solución, educativo | 1.5-2.5x |
| Warm (retargeting) | 30% | ABO con exclusiones | Visitas 7-30d, VC sin ATC, ATC sin compra | Carrusel/DPA, oferta, urgencia | 3-6x |
| Hot (retención) | 10% | DPA o manual | Clientes 30-180d, 1 compra, inactivos | Lanzamientos, bundles | 2-4x |

**Reglas de audiencia:**
- **> 50 compras/semana + CAPI OK** → ASC broad. El algoritmo le gana al targeting manual.
- **< 50 compras/semana** → LAL 1-3% (semilla: compradores > ATC > visitantes).
- Siempre excluir compradores recientes de prospección.
- Cuentas chicas (< USD 3k/mes): 1 campaña ASC + 1 retargeting. No fragmentar.

## Paso 3 — Sistema creativo

La creatividad es el targeting. Mínimo **3-5 creativos activos por conjunto** y **piezas nuevas cada 2-3 semanas**.

Para generar los ángulos, usa la skill **`ecomm-ad-angles`**. Para guiones con personas,
**`advanz-video-intelligence`**. Para hooks, **`viral-hooks`**.

Formatos que rinden en ecommerce: UGC testimonial (15-30s), problema→solución, antes/después,
unboxing/demo, educativo/mito, founder confesional, comparación de categoría.

**Test creativo:** 1 variable a la vez (ángulo > hook > formato > copy). Umbral de decisión: 1.000
impresiones para CTR, ~50 clics o 2× CPA gastado para conversión.

## Paso 4 — Diagnóstico por métrica

| Síntoma | Causa probable | Acción |
|---|---|---|
| CTR < 1% | Creativo / hook | Cambiar hook y ángulo |
| CTR alto + CVR bajo | PDP u oferta | Arreglar PDP → skill `ecomm-pdp-optimizer` |
| CPC alto | Audiencia saturada | Abrir a broad / nuevo ángulo |
| CPA sube 10-25% + frecuencia > 3 | Fatiga | Rotar creativos (NO pausar campaña) |
| ROAS bajo con CPA OK | AOV bajo | Bundles, umbral de envío gratis, upsell |
| Todo OK pero plano | Techo del canal | Escalar horizontal / sumar Google |
| Atribución Meta cae pero MER estable | Meta genera demanda que captura Google | Mirar MER, no ROAS de plataforma |

## Paso 5 — Escalado y reglas de corte

- **Escalar vertical**: +20-30% cada 3-5 días si ROAS estable > 5 días.
- **Escalar horizontal**: nuevo conjunto/ángulo, misma audiencia, cuando el vertical degrada.
- **Apagar anuncio**: CTR < 1% tras 1.000 impresiones, o CPA > 2× objetivo 3+ días.
- **Nunca** editar un conjunto en aprendizaje salvo que esté quemando > 2× CPA.

## Paso 6 — Entregable

Siempre en este orden:
1. **Resumen ejecutivo** (3 líneas): estado, principal fuga, acción #1.
2. **Números**: inversión, ROAS, CPA, CTR, CVR, frecuencia, MER, vs break-even.
3. **Hallazgos priorizados** por impacto × facilidad (tabla).
4. **Plan 30 días**: semana a semana, con presupuesto por capa.
5. **Riesgos y supuestos**: qué dato falta y qué cambia si está.

## Reglas

- **No ejecutar cambios en la cuenta sin aprobación explícita.** Proponer; el humano aprueba. Activar, pausar o cambiar presupuestos por MCP requiere confirmación caso a caso.
- Benchmarks siempre con fuente y mercado. Profundizar en `advanz-ecomm-intelligence/references/paid-media.md` y `benchmarks.md`.
- Investigación de competencia en Ad Library → `ecomm-benchmark-agent/references/ads-intelligence.md`.
- Claims de salud (suplementos, skincare): respetar políticas de Meta y regulación local.
