---
name: ecomm-store-builder
description: "Construcción y lanzamiento de una tienda ecommerce (Shopify por defecto) de cero o migración: arquitectura de catálogo y colecciones, navegación, páginas clave (home, PDP, colección, carrito, about, FAQ, políticas), stack de apps mínimo por etapa, pagos y envíos (con foco LATAM), tracking (GA4, Pixel+CAPI, Google), SEO base, email base y checklist de lanzamiento. Usa SIEMPRE que digan 'armar tienda', 'crear ecommerce', 'construir tienda Shopify', 'ecomm builder', 'migrar a Shopify', 'lanzar tienda', 'estructura de la tienda', 'qué apps instalo', 'checklist de lanzamiento', 'home de la tienda', 'arquitectura de colecciones', 'setup de Shopify'. SOLO ecommerce DTC/B2C."
---

# Ecomm Store Builder

Construye tiendas con criterio de conversión desde el día 1. Plataforma por defecto: **Shopify**
(adaptar si es WooCommerce, Tiendanube, Jumpseller o VTEX).

## Paso 0 — Brief

Completa `clientes/<marca>/contexto-marca.md`. Además: nº de SKUs y variantes, ¿migración o desde
cero? (plataforma origen, URLs y clientes a migrar), facturación esperada, país/es de venta,
logística (propia, 3PL, courier), equipo que operará la tienda, identidad visual disponible.

## Paso 1 — Arquitectura

- **Colecciones** por cómo busca el cliente (problema, uso, categoría), no por cómo organiza la bodega. Máx 2 niveles.
- **Menú**: 5-7 items. Best sellers y Packs/Bundles visibles.
- **URLs** limpias y con keyword; en migración, **mapa de redirecciones 301** URL por URL (productos, colecciones, blog, páginas).
- **Metafields/metaobjects** para beneficios, ingredientes, modo de uso, FAQ → la PDP escala sin editar HTML.

## Paso 2 — Páginas clave

| Página | Debe tener |
|---|---|
| Home | Promesa clara above the fold, best sellers, prueba social, categorías, beneficio de envío/garantía |
| Colección | Filtros útiles, orden por best seller, texto SEO corto arriba/abajo |
| PDP | Seguir `ecomm-pdp-optimizer` (8 bloques) |
| Carrito | Barra de envío gratis, cross-sell, total estimado con envío, medios de pago |
| About | Historia y equipo reales con fotos |
| FAQ / Envíos / Devoluciones | Plazos y costos claros; garantía explícita |
| Contacto | WhatsApp (obligatorio en LATAM) |

## Paso 3 — Stack mínimo por etapa

| Etapa (ventas/mes) | Stack |
|---|---|
| Lanzamiento (< USD 5k) | Tema OS 2.0 rápido, reseñas, email (Klaviyo o Shopify Email), WhatsApp, pagos locales |
| Tracción (5-30k) | + bundles/upsell, suscripciones si aplica, CAPI server-side, feed para Google |
| Escala (> 30k) | + loyalty/referidos, CDP/segmentación avanzada, CRO continuo, 3PL integrado |

Regla: cada app debe justificar su peso en velocidad. Diagnóstico de stack → `advanz-shopify-detector`.

## Paso 4 — Pagos, envíos, legal

- Pagos: tarjetas + locales (Chile: Webpay/Mercado Pago; México: OXXO/Mercado Pago; Colombia: PSE/Nequi) + cuotas/BNPL visible.
- Envíos: tarifas claras, umbral de envío gratis a ~1.3× AOV objetivo, plazos por zona.
- Legal: términos, privacidad, devoluciones según ley local, facturación electrónica. Ver `advanz-ecomm-intelligence/references/latam-context.md`.

## Paso 5 — Tracking y marketing base

- GA4 con eventos ecommerce · Meta Pixel + CAPI (EMQ ≥ 6) · Google Ads + Enhanced Conversions · Merchant Center con feed optimizado · Search Console + sitemap.
- Email: pop-up de captura + flujos welcome, carrito abandonado, browse, post-compra → `advanz-email-engine`.
- SEO base: titles/meta por plantilla, schema Product/Organization, colecciones con texto → `advanz-seo-geo-engine`.

## Paso 6 — Checklist de lanzamiento

- [ ] Compra de prueba end-to-end (cada medio de pago) y reembolso
- [ ] Emails transaccionales con marca
- [ ] Eventos de compra llegando a GA4, Meta (dedup) y Google
- [ ] Móvil revisado en dispositivo real; LCP < 2.5s
- [ ] Redirecciones 301 probadas (si migración) y sitemap enviado
- [ ] Políticas y contacto visibles; WhatsApp funcionando
- [ ] ≥ 10 reseñas en productos héroe antes de invertir en ads (importar si migración)
- [ ] Dominio, SSL, favicon, páginas 404 y de búsqueda revisadas

## Paso 7 — Primeros 30 días

Semana 1: QA y soft launch. Semana 2: flujos de email activos y primeras campañas
(`ecomm-meta-ads`, `ecomm-google-ads`). Semana 3-4: primera lectura CRO (`clarity-cro-audit`) y de
Search Console (`ecomm-search-console`). Marco completo por etapas → `advanz-growth-engine`.

## Reglas

- No publicar temas, cambiar precios ni instalar apps en la tienda sin aprobación explícita.
- Toda recomendación de app con alternativa y costo mensual aproximado.
