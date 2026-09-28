# Automatizaciones y Flows — Auditoría Competitiva

## Objetivo
Detectar qué automatizaciones tiene cada competidor activas y cuáles debería tener el cliente. En ecommerce, las automatizaciones son la infraestructura invisible que separa una tienda que vende de una que escala.

## Cómo detectar automatizaciones desde afuera

### Método 1: Compra de prueba (Gold standard)
Si es posible, hacer una compra pequeña o simular el proceso hasta el checkout para observar:
- ¿Hay popup de captura de email al entrar?
- ¿Qué oferta da el popup? (% descuento, envío gratis, lead magnet)
- ¿Llega email de bienvenida? ¿En cuánto tiempo?
- ¿Hay email de carrito abandonado? (abandonar checkout y esperar)
- ¿Hay email post-compra? ¿Pide review?
- ¿Hay email de cross-sell?
- ¿Hay WhatsApp post-compra?

### Método 2: Observación de señales (cuando no se puede comprar)
| Señal observable | Automatización probable |
|-----------------|----------------------|
| Popup al entrar con email capture | Welcome series (email 1 a 3 en las primeras 48h) |
| "10% OFF primera compra" en popup | Discount code delivery → abandoned browse |
| Widget de reviews en PDP (Loox, Judge.me, Yotpo) | Post-purchase review request email (automático) |
| "Suscríbete y ahorra" en PDP | Subscription management flows (renewal, skip, cancel) |
| "Envío gratis sobre $X" | Threshold upsell automático en cart |
| Botón WhatsApp activo | Al menos notificaciones manuales; posiblemente flows automatizados |
| Chat widget (Gorgias, Tidio, etc.) | Chatbot con respuestas automáticas + ticket routing |
| "Programa de puntos" / "Rewards" | Loyalty automation (puntos por compra, por review, por referido) |
| "Refiere a un amigo" | Referral automation (código único + reward) |
| Countdown timer en PDP o cart | Urgency automation (probablemente estática, no personalizada) |
| "Te enviamos un WhatsApp con tu tracking" | WhatsApp transactional notifications |
| "Últimas X unidades" | Inventory-based urgency (puede ser real o fake) |

## Mapa de automatizaciones por etapa

### Pre-compra
| Automatización | Qué hace | Herramientas comunes | Impacto |
|---------------|----------|---------------------|---------|
| **Welcome series** | 3-5 emails al nuevo suscriptor: bienvenida → educación → oferta | Klaviyo, Mailchimp, Omnisend | CVR +20-40% sobre no tener |
| **Browse abandonment** | Email/push si visitó producto sin agregar al carrito | Klaviyo, Omnisend | Revenue recover 3-5% |
| **Abandoned cart** | Email/SMS/WhatsApp si abandonó carrito | Klaviyo, Shopify native, WhatsApp API | Revenue recover 5-15% |
| **Back in stock** | Notificación cuando producto vuelve a tener stock | Klaviyo, Back in Stock app | Conversión alta (alta intención) |
| **Price drop alert** | Notificación si baja precio de producto visto | Klaviyo, custom | Activación de indecisos |

### Post-compra
| Automatización | Qué hace | Herramientas comunes | Impacto |
|---------------|----------|---------------------|---------|
| **Order confirmation + tracking** | Confirmar pedido + enviar tracking | Shopify native, Klaviyo, WhatsApp | Expectation setting, reduce WISMO |
| **Delivery notification** | Avisar cuando llega el pedido | Shipping app, WhatsApp | Experiencia + reduce tickets |
| **Review request** | Pedir reseña 5-14 días post-entrega | Loox, Judge.me, Yotpo, Klaviyo | Social proof generation |
| **Cross-sell** | Recomendar productos complementarios post-compra | Klaviyo, ReConvert, Rebuy | AOV / 2nd purchase rate |
| **Educational drip** | Secuencia educativa sobre cómo usar el producto | Klaviyo, Mailchimp | Reduce returns, increase satisfaction |
| **Replenishment reminder** | Recordar recompra cuando se estima que el producto se acabó | Klaviyo (predictive), custom | Repeat purchase rate +15-25% |

### Retención
| Automatización | Qué hace | Herramientas comunes | Impacto |
|---------------|----------|---------------------|---------|
| **Win-back** | Re-activar clientes inactivos (60-90 días sin compra) | Klaviyo, Omnisend | Reactivación 3-8% |
| **Sunset / re-permission** | Limpiar lista de inactivos totales | Klaviyo | Deliverability + ahorro |
| **VIP segmentation** | Trato especial a top customers | Klaviyo, loyalty app | LTV +20-40% en segmento VIP |
| **Birthday / anniversary** | Oferta especial en fecha personal | Klaviyo, CRM | Engagement + conversión |
| **Subscription management** | Recordar, skip, pause, cancel flows | Recharge, Bold, Appstle | Reduce churn suscripciones |
| **Referral trigger** | Pedir referido después de review positiva o 2da compra | ReferralCandy, Yotpo | CAC reduction vía word-of-mouth |

### Soporte y CX
| Automatización | Qué hace | Herramientas comunes | Impacto |
|---------------|----------|---------------------|---------|
| **Chatbot FAQ** | Responder preguntas frecuentes 24/7 | Gorgias, Tidio, custom | Reduce tickets 30-50% |
| **WhatsApp flows** | Flujos conversacionales: pedido, tracking, recompra | WhatsApp Business API, Zoko | Canal directo, open rate 90%+ |
| **Returns automation** | Proceso de devolución self-service | Loop, ReturnGO | Reduce fricción, ahorra CS time |
| **NPS / CSAT post-delivery** | Encuesta de satisfacción automatizada | Klaviyo, Typeform, Delighted | Feedback loop + detección problemas |

## Tabla comparativa para el benchmark

```
| Automatización          | [Cliente ★] | [Comp. 1] | [Comp. 2] | [Comp. 3] |
|------------------------|-------------|-----------|-----------|-----------|
| Welcome series          | ⚠️/✅/❌    |           |           |           |
| Abandoned cart email    |             |           |           |           |
| Abandoned cart WhatsApp |             |           |           |           |
| Review request          |             |           |           |           |
| Post-purchase drip      |             |           |           |           |
| Cross-sell email        |             |           |           |           |
| Replenishment reminder  |             |           |           |           |
| Win-back                |             |           |           |           |
| Subscription flows      |             |           |           |           |
| Referral automation     |             |           |           |           |
| Loyalty / rewards       |             |           |           |           |
| WhatsApp transactional  |             |           |           |           |
| Chatbot / FAQ auto      |             |           |           |           |
| NPS / CSAT              |             |           |           |           |
```

Badges: ✅ Detectado activo · ⚠️ Probable/parcial · ❌ No detectado · N/A No aplica

## Revenue impact estimado por automatización

Para dar contexto al cliente sobre qué automatizaciones priorizar:

| Automatización | Revenue recovery/uplift estimado | Tiempo implementación |
|---------------|--------------------------------|----------------------|
| Abandoned cart (email) | 5-15% de carritos abandonados | 1-2 semanas |
| Welcome series | +20-40% conversión nuevos suscriptores | 1-2 semanas |
| Review request | +50-200% generación de reviews | 1 semana |
| Replenishment reminder | +15-25% repeat purchase rate | 2-3 semanas |
| Win-back | 3-8% reactivación de inactivos | 1-2 semanas |
| Cross-sell post-purchase | +5-15% 2nd purchase rate | 2-3 semanas |
| WhatsApp transactional | Open rate 90%+ vs 20% email | 2-4 semanas |
| Referral program | -15-30% CAC en clientes referidos | 3-4 semanas |
| Subscription | +30-60% LTV por suscriptor | 4-6 semanas |
