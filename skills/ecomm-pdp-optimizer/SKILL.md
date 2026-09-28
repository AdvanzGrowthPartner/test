---
name: ecomm-pdp-optimizer
description: "Auditoría y reescritura de páginas de producto (PDP) para cualquier ecommerce: above the fold, galería, copy PAS, beneficios vs características, prueba social, confianza, oferta y AOV (bundles, cuotas, envío gratis), FAQ con schema, mobile y SEO on-page. Entrega un score por bloque y la PDP reescrita lista para pegar. Usa SIEMPRE que digan 'PDP', 'página de producto', 'ficha de producto', 'optimiza este producto', 'reescribe la descripción', 'copy de producto', 'por qué no convierte este producto', 'tengo tráfico pero no ventas', 'CTR alto CVR bajo', 'descripción para Shopify', 'bundle', 'mejorar conversión del producto'. SOLO ecommerce DTC/B2C."
---

# PDP Optimizer

La PDP es donde se decide la venta. Si los ads tienen CTR alto y CVR bajo, el problema está aquí.

## Paso 0 — Insumos

- **URL de la PDP** (leer el HTML o con navegador si está disponible) o captura/texto.
- Contexto de marca: `clientes/<marca>/contexto-marca.md` (avatar, diferenciador, claims permitidos, tono).
- Si hay datos: CVR de la PDP, tráfico por fuente, tasa de ATC, reseñas y rating, AOV.
- Si hay Shopify MCP: `get-product` para título, descripción, variantes, precio, imágenes, metafields.

Antes de escribir, destila la **ficha del producto**: beneficio principal, secundarios, mecanismo
(por qué funciona), avatar y su etapa de consciencia, transformación, diferenciador real, prueba
disponible, claims permitidos/prohibidos, precio y modelo (único, suscripción, bundle), oferta.
Si falta algo crítico, pídelo — no lo inventes.

## Paso 1 — Auditoría en 8 bloques (score 0-5 cada uno)

| Bloque | Qué debe tener |
|---|---|
| 1. Above the fold (móvil) | Título con keyword, rating + nº reseñas, precio + cuotas/BNPL, CTA visible sin scroll, envío y devolución |
| 2. Galería | ≥ 5 imágenes: lifestyle, detalle, escala, uso; video si es posible (+20-30% CVR) |
| 3. Copy | PAS (Problema → Agitación → Solución). Beneficios > características. Único, no el del proveedor |
| 4. Prueba social | ≥ 10 reseñas antes de escalar ads, rating ≥ 4.2, reseñas con foto, UGC |
| 5. Confianza | Garantía explícita, política de devolución clara, medios de pago locales, sello de seguridad, WhatsApp |
| 6. Oferta y AOV | Bundles (+15-25% AOV), escalera de cantidad, suscripción, umbral de envío gratis a 1.3× AOV |
| 7. Objeciones / FAQ | Las 5-8 objeciones reales respondidas; FAQ con schema FAQPage |
| 8. SEO / técnico | Title ≤ 60, meta ≤ 155, schema Product + Review + Offer, alt en imágenes, LCP < 2.5s |

Score total /40. < 20 = rehacer · 20-30 = optimizar · > 30 = testear detalles.

## Paso 2 — Reescritura

Entregar en este orden, listo para pegar en Shopify:

1. **Título** (SEO + claridad).
2. **Subtítulo / promesa** (1 línea con la transformación).
3. **3-5 bullets de beneficio** (resultado para el cliente, no característica).
4. **Descripción PAS** corta (≤ 150 palabras visibles) + bloque expandible con detalle.
5. **Mecanismo / ingredientes / materiales** explicados en lenguaje del cliente.
6. **Bloque de prueba** (qué reseñas destacar y dónde).
7. **Garantía y envío** (copy exacto).
8. **FAQ** (6-8 preguntas) + JSON-LD FAQPage.
9. **Title tag y meta description**.
10. **Oferta propuesta** (bundle / escalera / suscripción) con cálculo de margen.

Ángulos de copy consistentes con los ads: usa `ecomm-ad-angles` para que la PDP continúe la
promesa del anuncio (message match).

## Paso 3 — Priorizar cambios

Tabla: cambio · bloque · impacto esperado · esfuerzo · riesgo. Primero lo que afecta above the
fold en móvil y confianza; después oferta; después SEO.

Para medir y proteger el cambio (QA, rollback, readout 14/30 días) → `clarity-cro-audit`.

## Reglas

- **No escribir en la tienda sin aprobación.** Entregar el cambio y dónde va.
- Claims de salud: nada de "cura", "trata", "previene" sin respaldo regulatorio. Reglas YMYL en `advanz-shopify-blog-publisher/references/ymyl-rules.md`.
- Nunca inventar reseñas, cifras de ventas ni certificaciones.
- Benchmarks y tácticas: `advanz-ecomm-intelligence/references/conversion-optimization.md`.
- Mercado LATAM: cuotas, Webpay/Mercado Pago, WhatsApp y plazos de despacho son críticos.
