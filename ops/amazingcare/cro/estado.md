# AmazingCare · OS CRO (web Shopify, PDP, checkout, landing, Clarity)

## Estado actual
**Último dato leído: 2–4 oct 2026, Cyber Amazing.**
- **Problema de la escalera de precios en el Cyber (el cliente lo reportó como "grave"):**
  - La app **Kaching Bundles** suma descuentos por cantidad sobre precios que ya venían con −30%. Se activó el 2 oct a las 12:50 (hora Chile), 50 minutos después del lanzamiento.
  - Ladder invertido: 5×30 sticks de un sabor con −15% sale a ~$476 por stick, mientras el **Súper Pack 150 cuesta ~$527 por stick** (10% más caro).
  - Tramos inconsistentes según el producto: Súper Pack y Mix 30 tienen −10% x2, Piña 30 −15% x5, Pack 60 x2 = 0%, y mezclar sabores no tiene descuento.
  - AMAZING10 venció el 2 oct a las 16:27. Desde el **3 oct a las 13:17 los pedidos de 2–5 unidades ya no reciben descuento por cantidad** (pendiente verificar en la tienda).
  - Prueba "15% OFF ORDER" en el pedido #10063.
- **Embudo del Cyber:**
  - Día 1: el checkout rindió +19% sobre el día 1 de junio, pero agregar al carrito cayó (7,6% de las sesiones contra 13,2%).
  - Día 2: sesión→carrito −32% y conversión −31%. El AOV subió 4%.
  - Meta: solo el 59% de los clics llega a ver la página (lo sano es ≥75%). Posible velocidad de carga o navegador interno de IG.
- **Móvil:** ~87% del tráfico, convierte 4,75% contra 14,9% en desktop (CyberDay jun-26). El cierre de checkout se estimó en 49%.
- **Conversión base:**
  - Ago 1–20: 2,35%. Sesión→carrito 6,61%, carrito→checkout 88,8%, checkout→compra 40,1%.
  - Sep 1–14: 2,11%.
- **PDP que más convierten (60 días a sep-26):**

| PDP | Conversión | Sesiones |
|---|---|---|
| Berries 30 | 2,86% | 665 |
| Mix Sabores 30 | 2,69% | 446 |
| Súper Pack 150 | 2,68% | 411 |
| Energy Tropical 10 | 2,39% | 1.545 |
| `pack-mix-60` | 1,16% | 10.680 (recibe todo el tráfico frío) |

- **Prueba social:** ~300 reseñas en la PDP, sin schema `AggregateRating` verificado.
- **Tráfico desde IA:** ChatGPT aterriza en fichas de producto y en la página de ciencia/certificaciones.

## Decisiones tomadas
- **2-oct:** se armó la pestaña "Deploy CRO" en el war room, con línea de tiempo, simulador de escalera y checklist (`ac_deploy_fix`). Solo lectura: no se tocó la tienda.
- **Sep-26:** los anuncios se derivan a la PDP que más convierte para cada producto (Energy→Energy Tropical, Berries→Berries 30, packs→Súper Pack 150, mix→Mix 30), no a `pack-mix-60`.
- **Mecánica ganadora para eventos (skill event-strategy):** despacho gratis sobre el pack, regalo (vaso o botella) atado al pack y nunca suelto, upsell de Energy en PDP y carrito, con el ahorro como protagonista.
- Envío gratis sobre $50.000 a todo Chile (claim FP y Cyber).

## Pendientes / próximos pasos
- [ ] **Verificar y corregir la escalera de precios / Kaching** después del Cyber: tramos consistentes y Súper Pack siempre más barato por stick que comprar sueltos.
- [ ] Atacar la fuga entre clic y visita de Meta (59%): velocidad de carga, navegador interno de IG, peso de la landing.
- [ ] CRO móvil: checkout y paso a carrito (palancas "checkout móvil" y "checkout +5 pts" del war room, con efectos supuestos).
- [ ] Hacer visible el pop-up de captura de Klaviyo (compartido con el OS Email).
- [ ] Schema `Review`/`AggregateRating` en las PDP (también ayuda a GEO).
- [ ] Página "Dónde comprar" / localizador de tiendas, si se activa la capa 2 de Ads Retail.
- [ ] **Sin historial de Clarity:** se pidió cruzar Clarity, GA4 y Shopify para el tráfico de Google Ads que se deriva al blog (26-ago), pero no hay resultado. Falta levantar heatmaps y grabaciones de PDP y checkout.
- [ ] Listicle de conversión estilo claranovalabs para el blog de lipedema (pedido el 26-ago; la sesión terminó al inicio, sin entregable).

## Fuentes
- session_01MLGvNVcyGZBjw1Ey4x8HPU: war room, pestaña Deploy CRO (https://claude.ai/artifact/4NHYGwnx1PFnXEVMp12b7S)
- session_01Lete8uGMuJPaG3Gy8QkcMA: PDP que más convierten (60 días)
- session_01BVePuAZzyGKWnTLxrwckRG: funnel y tasas de paso de agosto
- session_014qJfxPHjDMJgFTkac6jMLo: funnel sep 1–14 y aterrizajes de ChatGPT
- session_01QUkQ6zmmEVF2WciHSJVky6: tráfico de Google Ads al blog (solo se leyó el pedido)
- session_01PmvGFUXiETFEMitMuHkvin: listicle de conversión del blog de lipedema (se leyó solo el inicio)
- Rama `origin/claude/ecommerce-cyber-strategy-skill-mmm6m0`: skill `event-strategy` (`references/product-classification.md`)
