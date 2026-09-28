# Stack AI-Native 2026 — Recomendado para clientes Advanz

Este archivo se consulta cuando hay que recomendar herramientas concretas, hacer audit de stack, o explicar la capa IA con detalle técnico.

---

## Stack mínimo recomendado por etapa de cliente

### Cliente nuevo / pequeño (<$5M CLP/mes ventas)

| Capa | Herramienta | Por qué |
|------|-------------|---------|
| Storefront | Shopify + Shopify Magic (gratis) | Asistencia nativa AI, sin costo extra |
| Email | Klaviyo plan free → Klaviyo paid | Hasta 250 contactos free, escalable |
| Soporte | Shopify Inbox (gratis) | Chat básico para empezar |
| Analytics | Shopify Analytics + GA4 | Suficiente para volumen inicial |

**Total stack:** mínimo costo, máxima capacidad para tamaño.

---

### Cliente en crecimiento ($5M-30M CLP/mes ventas)

| Capa | Herramienta | Por qué |
|------|-------------|---------|
| Storefront | Shopify + Shopify Magic | Base sólida con AI nativo |
| CRM/Email | Klaviyo + Customer Hub (beta para Shopify) | Customer Hub trae soporte + tracking + experiencias personalizadas |
| Cart/AOV | Rebuy o similar | Personalización de cart con IA, lift de AOV documentado |
| Discovery | Octane AI o similar | Quiz interactivo + segmentación auto en Klaviyo |
| Soporte | Klaviyo Customer Agent | Resuelve hasta 90% L1, vende mientras resuelve |
| Analytics | Triple Whale o similar | Multi-channel attribution con IA |

**Acá vive la mayoría de los clientes Advanz activos.** Stack ejecutable, ROI claro.

---

### Cliente avanzado / enterprise (>$30M CLP/mes ventas)

Todo lo anterior +

| Capa | Herramienta | Por qué |
|------|-------------|---------|
| Creative | Smartly.io | Creative AI a escala, justifica con ad spend alto |
| Soporte voz | AI voice agents (Ringly o similar) | 73% calls resueltas sin humano |
| Inventory | AI inventory agents | Reducción 20-30% inventario sin afectar service |
| Subscription | Recharge + AI replenishment | Predictive reorder |
| Tickets | Gorgias AI (cuando volumen alto) | Resolución autónoma + escalación |
| Reporting MCP | Claude + Dashbo MCP + Notion MCP | Reportes en lenguaje natural, on-demand |

---

## Mapeo Stack ↔ Etapa del Growth Engine

| Etapa | Herramientas clave |
|-------|-------------------|
| 1. Foundations | Shopify, Schema validators, Citation tracking tools, skill `7-maletas` para research |
| 2. Offer | Shopify Magic (PDP copy), JSON-LD generators, Schema.org validator |
| 3. Validation | Octane AI (quiz), Klaviyo A/B testing, Hotjar/Lucky Orange |
| 4. Acquisition | Meta Advantage+, Google Performance Max, TikTok Smart+, Smartly.io, GEO tools |
| 5. Workflows | Klaviyo Customer Hub, Klaviyo Customer Agent, WhatsApp Business API + RCS |
| 6. Retention | Klaviyo predictive analytics, Recharge (subscriptions), Customer Hub memory, predictive segments |
| 7. Feedback | Reviews automation, Triple Whale dashboards, AI citation tracking (Geoptie/similar) |
| 8. Systems | Claude + MCPs (Dashbo, GA4, Meta, Shopify), Inventory AI agents, Smartly.io a escala |

---

## Decisiones críticas de stack

### ¿Klaviyo o Shopify Email?

- **Shopify Email:** OK hasta ~$5K USD/mes en ventas. Free, suficiente para empezar.
- **Klaviyo:** salta a Klaviyo cuando se supera ese umbral. La sincronización sub-200ms con Shopify, los flujos predictivos, Customer Hub y Customer Agent justifican el costo.
- **No correr ambos en paralelo** — emails duplicados al cliente.

### ¿Cuándo activar Customer Agent?

- Volumen de tickets >50/mes
- Soporte 100% humano consumiendo más de 10 hrs/semana
- Categoría con muchas WISMO (where is my order) — ahí el agent paga solo
- Marca con identidad de voz definida (el agent la mantiene)

### ¿Cuándo activar Smartly.io o creative AI a escala?

- Ad spend mensual sostenido >$3K USD/mes
- Equipo creativo saturado de iteraciones manuales
- Categoría donde el creative testing rápido importa (fashion, supplements, beauty)

### ¿Cuándo entrar en agentic surfaces (ChatGPT, Google AI Mode)?

- Tienda con catálogo en Shopify (las que están en otras plataformas tienen que esperar o migrar)
- PDPs con schema completo (sin esto no hay punto de entrada)
- Volumen suficiente para que valga la pena el setup

### ¿Cuándo entrar en Systems (Etapa 8)?

Aplicar la regla de oro:
- Foundations sólidas ✅
- Offer + Acquisition + Workflows operando con métricas conocidas ✅
- Retention con al menos 1 ciclo de medición (3+ meses) ✅
- Feedback estructurado capturando data en al menos 2 canales ✅

Si los 4 no se cumplen, Systems se posterga.

---

## Stack para LATAM — consideraciones específicas

**Pagos:**
- Transbank (Chile)
- MercadoPago (toda la región)
- Flow, Webpay (Chile)
- Khipu (Chile, transferencias)
- PayPal (internacional)

**Envíos:**
- Chilexpress, Starken, Correos Chile
- Servientrega (Colombia)
- Estafeta (México)

**Mensajería:**
- WhatsApp Business API (no opcional en LATAM)
- Klaviyo soporta WhatsApp + RCS desde 2026
- Twilio o Sendpulse como alternativa

**Idioma:**
- Klaviyo soporta español (LatAm neutro)
- Shopify Magic genera copy en español
- Cuidado con tools US-only que no manejan tildes/ñ correctamente

---

## Audit de stack — preguntas clave

Cuando se hace audit de stack de un cliente activo:

1. ¿Klaviyo está conectado a Shopify? ¿Sincroniza en tiempo real?
2. ¿Customer Hub está habilitado (es beta para Shopify)?
3. ¿Cuántos flujos automáticos están activos? ¿Cuáles?
4. ¿Hay quiz / mecanismo de calificación de leads?
5. ¿Schema markup en PDPs? ¿AggregateRating poblado?
6. ¿Server-side rendering en Shopify? (default es OK, pero apps custom pueden romperlo)
7. ¿Attribution multi-channel o solo last-click?
8. ¿WhatsApp como canal? ¿Conectado a Klaviyo?
9. ¿AI subject lines y Smart Send Time activos?
10. ¿Predictive segments seteados (churn, replenishment, VIP)?
11. ¿Reviews response automation activa?
12. ¿Citation tracking (cuántas veces sale en ChatGPT/Perplexity para su categoría)?

Cada "no" es un gap que se traduce en una recomendación → upsell.

---

## Lo que NO recomendamos

❌ **Tools genéricas sin integración Shopify nativa.** Si requiere Zapier para todo, va a romperse.

❌ **Stack fragmentado** (Mailchimp + Recart + Tidio + Helium 10 + ...). Mejor 4-5 herramientas integradas que 15 desconectadas.

❌ **Promesas de "AI mágica"** sin documentación clara de cómo funciona.

❌ **Tools que no soportan español/LatAm** para clientes regionales.

❌ **Migrar a stack nuevo cuando el actual funciona.** Auditar primero, optimizar lo que hay, y migrar solo si hay gap real.

❌ **Recomendar Systems (Etapa 8) sin las etapas 1-7 sólidas.** El stack más caro sobre cimientos rotos no produce valor — produce costos.
