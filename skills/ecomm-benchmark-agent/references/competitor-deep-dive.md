# Competitor Deep Dive — Web, Stack & Plataformas Conectadas

## Análisis de sitio web por competidor

Para cada competidor, documentar:

### Plataforma y CMS
- **Shopify** → Detectar por: `/collections/`, `/products/`, `cdn.shopify.com` en source, `Shopify.theme`
- **WooCommerce** → Detectar por: `/wp-content/`, `woocommerce`, `/product/`
- **Magento** → Detectar por: `/catalog/`, `mage/`, `Magento`
- **VTEX** → Detectar por: `vtex.com`, `/api/catalog/`
- **PrestaShop** → Detectar por: `/modules/`, `prestashop`
- **Webflow** → Detectar por: `webflow.io`, `data-wf-`
- **Custom / sin ecommerce** → Sin tienda online propia, solo marketplace o retail físico

### Apps y herramientas detectables
| Categoría | Apps comunes | Cómo detectar |
|-----------|-------------|---------------|
| Reviews | Loox, Judge.me, Yotpo, Stamped, custom | Widget en PDP, script en source |
| Chat / soporte | WhatsApp widget, Tidio, Zendesk, Intercom, chatbot IA | Botón flotante, script |
| Email capture | Klaviyo, Mailchimp, Omnisend, Privy, popup nativo | Popup al entrar, footer form |
| Suscripción | Recharge, Bold, Appstle, Seal, Loop | Opción "suscribirse" en PDP |
| Loyalty | Smile.io, LoyaltyLion, Yotpo Loyalty | Link "rewards" o "puntos" |
| Referidos | ReferralCandy, Friendbuy, Yotpo Referral | Link "referir amigo" |
| Upsell/cross-sell | ReConvert, Bold Upsell, Rebuy, Zipify OCU | Post-purchase page, in-cart offers |
| Analytics/pixel | Meta Pixel, GA4, TikTok Pixel, Hotjar, Clarity | Source code, network requests |
| FAQ | Helpcenter, custom, Shopify native | /faq, /preguntas-frecuentes, FAQ schema |
| Chatbot IA | Gorgias, Re:amaze, ChatGPT widget, custom | Chat widget, comportamiento IA |

### Ficha técnica del sitio
```
Competidor: [nombre]
URL: [dominio]
CMS: [plataforma]
Reviews app: [app + cantidad + rating visible]
Chat/soporte: [tipo + canal]
Email capture: [método + oferta]
Suscripción: [sí/no + modelo]
Loyalty: [sí/no + programa]
Referidos: [sí/no]
FAQ: [sí/no + schema]
Pixel/tracking: [Meta + GA4 + TikTok + otros]
WhatsApp: [sí/no + tipo: botón, widget, nutricionista, chatbot]
Chatbot IA: [sí/no + herramienta]
Velocidad percibida: [rápida/media/lenta]
Mobile UX: [buena/aceptable/mala]
SSL: [sí/no]
Idiomas: [cuáles]
Monedas: [cuáles]
```

## Distribución digital

### Canales a verificar por competidor
| Canal | Qué buscar | Query |
|-------|------------|-------|
| Sitio propio | ¿Tiene ecommerce? ¿Funciona? | `[dominio]` directo |
| Jumbo.cl | Ficha de producto activa | `site:jumbo.cl [marca]` |
| Falabella.com | Ficha de producto activa | `site:falabella.com [marca]` |
| MercadoLibre | Tienda oficial o sellers | `site:mercadolibre.cl [marca]` |
| Rappi | Presencia en la app | `[marca] rappi chile` |
| Paris.cl | Ficha de producto activa | `site:paris.cl [marca]` |
| Salcobrand | Ficha digital | `site:salcobrand.cl [marca]` |
| Cruz Verde | Ficha digital | `site:cruzverde.cl [marca]` |
| Farmacias Ahumada | Ficha digital | `site:farmaciasahumada.cl [marca]` |
| Cornershop / Uber Eats | Presencia en delivery | `[marca] cornershop chile` |
| Amazon (si aplica) | Tienda o sellers | `site:amazon.com [marca]` |

### Hallazgo de distribución digital
Cuando un producto está físicamente en un retailer PERO no indexado digitalmente en su ecommerce, esto es un hallazgo crítico. Documentar como:

> **⚠️ Hallazgo de distribución digital:** *[Marca] está físicamente en [retailer]. Sin embargo, no fue posible confirmar su presencia como producto indexado y buscable en [retailer.cl].* Si el producto no está indexado en el ecommerce del retailer, cualquier cliente que busque online '[categoría]' en esa plataforma no encontrará [marca].

## Plataformas conectadas por competidor

### Mapa de ecosistema digital
Para cada competidor, mapear todas las plataformas donde tiene presencia activa:

```
[Nombre competidor]
├── Sitio web → [URL] ([CMS])
├── Redes sociales
│   ├── Instagram → [@handle] ([seguidores] followers)
│   ├── TikTok → [@handle] ([seguidores] followers)
│   ├── YouTube → [canal] ([suscriptores])
│   ├── Facebook → [page] ([seguidores])
│   └── LinkedIn → [page] (si aplica)
├── Marketplaces
│   ├── MercadoLibre → [tienda/sellers] ([reviews])
│   ├── Rappi → [presencia]
│   └── [otros]
├── Retail online
│   ├── Jumbo.cl → [indexado sí/no]
│   ├── Falabella → [indexado sí/no]
│   └── [otros]
├── Comunicación
│   ├── WhatsApp → [business/nutricionista/chatbot]
│   ├── Email → [plataforma estimada]
│   └── SMS → [detectado sí/no]
└── Publicidad
    ├── Meta Ads → [activo sí/no]
    ├── Google Ads → [activo sí/no]
    └── TikTok Ads → [activo sí/no]
```

## Web opportunities — Qué buscar

### Gaps de conversión observables
1. **Sin reviews en sitio** → Oportunidad de captura de social proof
2. **Sin garantía visible** → Oportunidad de trust signal
3. **Sin packs o bundles** → Oportunidad de AOV
4. **Sin suscripción** → Oportunidad de LTV (especialmente en consumibles)
5. **Sin FAQ** → Oportunidad de SEO (FAQ schema) + reducción de fricción
6. **Sin WhatsApp** → Oportunidad de canal de conversión directa
7. **Sin blog** → Oportunidad de contenido SEO
8. **Sin chatbot** → Oportunidad de atención 24/7 y cualificación
9. **PDP sin elementos de urgencia/escasez** → Oportunidad de CRO
10. **Checkout sin trust signals** → Oportunidad de reducción de abandono
11. **Sin popup de captura** → Oportunidad de list building
12. **Sin post-purchase flow** → Oportunidad de retención y reviews
13. **Sin retargeting visible** → Oportunidad de recuperación
14. **Sin indexación en retailers** → Oportunidad de distribución digital
15. **Sin rich snippets** → Oportunidad de CTR orgánico

### Para el cliente (★): priorizar oportunidades donde
- El benchmark líder (🔝) ya lo hace bien
- El cliente no lo tiene o lo tiene desactivado
- La implementación es rápida (<2 semanas)
- El impacto en revenue es directo
