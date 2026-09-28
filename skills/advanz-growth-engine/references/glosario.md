# Glosario expandido — Términos del ecosistema ecommerce 2026

Este glosario se consulta cuando el cliente o el usuario pregunta por un término técnico, o cuando hace falta explicar un concepto en una propuesta o llamada de venta. Cada entrada sigue el formato: **definición simple → por qué importa → ejemplo concreto → señal de carencia**.

---

## Conceptos del Growth Engine

### Growth Engine

**Qué es:** El sistema completo de 8 etapas conectadas que ordena el crecimiento de un ecommerce. Cada etapa habilita la siguiente; cada vuelta del engine compone sobre la anterior.

**Por qué importa:** Sin un sistema, el negocio crece por ráfagas (un mes vendés mucho, otro nada). El engine convierte ráfagas en crecimiento sostenido y predecible.

**Ejemplo:** Una marca de electrolitos que tenía Foundations claras pero Workflows débiles. Después de cerrar Workflows + Retention, su LTV creció y dejó de depender de aumentar el budget de ads cada mes.

**Señal de que te falta esto:** Las decisiones de tu negocio se toman mes a mes, sin marco. "Este mes invertimos en ads, el próximo en email, el próximo en web." Sin orden, sin sistema.

---

### AI-readiness

**Qué es:** Qué tan preparada está tu tienda para ser leída, indexada y vendida por agentes IA (no solo por humanos). Incluye schema markup completo, JSON-LD limpio, server-side rendering, descripciones específicas y atributos verificables.

**Por qué importa:** En 2026, una parte creciente de las compras pasa por agentes IA (ChatGPT, Google AI Mode, Perplexity). Si tu tienda no es leíble por ellos, sos invisible para esos clientes.

**Ejemplo:** Cliente busca en ChatGPT "mejor electrolito para deportistas en Chile". El agente responde con 3 marcas. Si tu tienda tiene AI-readiness alta, podés ser una de esas 3. Si tiene PDPs vacías y sin schema, ChatGPT directamente no puede recomendarte aunque seas la mejor opción.

**Señal de que te falta esto:** No aparecés cuando preguntás a ChatGPT, Perplexity o Google AI Overviews por tu categoría.

---

### Citation Share / AI Citation Score

**Qué es:** Métrica nueva de 2026 que mide **cuántas veces y dónde aparece tu marca citada** en respuestas de engines generativos (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini). Es el equivalente al "ranking" del SEO clásico, pero para la era de los agentes IA.

**Por qué importa:** Las búsquedas tradicionales están cayendo (Gartner proyecta -25% en 2026). Si dependés solo de ranking en Google, vas a perder tráfico. La nueva visibilidad se mide por citation share.

**Ejemplo:** En enero tu marca aparece en 2 de cada 100 respuestas de ChatGPT sobre tu categoría. En junio aparece en 18 de cada 100. Tu citation share creció 9x sin haber gastado más en ads — ganaste visibilidad en una superficie nueva.

**Señal de que te falta esto:** No medís nada de esto. No sabés si te citan, ni dónde, ni en qué contexto.

---

## Conceptos de adquisición moderna

### GEO (Generative Engine Optimization)

**Qué es:** Optimización para que los engines generativos (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini) **citen tu contenido cuando responden consultas de compra**. Es una disciplina hermana del SEO pero con criterios distintos.

**Por qué importa:** El SEO clásico te lleva a aparecer en los 10 enlaces azules. El GEO te lleva a ser una de las 2-7 fuentes que el LLM cita en su respuesta. Cuando un engine te cita, es como un endorsement implícito que ningún ranking orgánico puede igualar.

**Ejemplo:** Un usuario pregunta "qué proteína tomar después de entrenar si soy vegana". ChatGPT responde mencionando 3 marcas con sus diferenciadores. Si trabajaste GEO, sos una de esas 3 — y la conversión es mucho mayor que un click frío de Google.

**Señal de que te falta esto:** Tu blog tiene mucho contenido pero ningún engine generativo te cita.

**Cómo se trabaja:**
- Schema markup completo (Product, Offer, FAQPage, AggregateRating, Article)
- Contenido en formato pregunta-respuesta de ~40 palabras debajo de H2
- Renderizado server-side
- Frescura trimestral (50% del contenido citado tiene <13 semanas de antigüedad)
- Mentions en third-party sources (las IAs prefieren earned media a brand-owned)

---

### AEO (Answer Engine Optimization)

**Qué es:** Subset de GEO enfocado específicamente en aparecer como **respuesta directa** en featured snippets, AI Overviews y respuestas de chatbots. Es lo que hace que tu marca sea "la respuesta" y no "una opción más".

**Por qué importa:** Los AI Overviews ya aparecen en aproximadamente la mitad de las búsquedas en US y crecen en LATAM. Cuando el usuario lee el AI Overview, muchas veces ni hace click — si no estás citado ahí, perdés la oportunidad.

**Ejemplo:** Búsqueda en Google: "cómo elegir electrolitos". Aparece un AI Overview de 4 bullets. Si tu blog está optimizado para AEO, sos la fuente citada del bullet 2.

**Señal de que te falta esto:** Tus posts ranquean pero el tráfico cayó porque AI Overviews se está comiendo los clicks.

---

### Agentic Commerce

**Qué es:** Modelo de comercio donde **agentes IA hacen la compra por el cliente final**. El usuario le dice a ChatGPT "comprame proteína vegana de menos de $30 con buenas reviews" y el agente lo investiga, compara y compra sin que el usuario abra una tienda.

**Por qué importa:** Es un canal de adquisición nuevo, en crecimiento acelerado. Shopify habilitó agentic storefronts para millones de merchants en marzo 2026. Si tu tienda no está habilitada, ese canal no existe para vos.

**Ejemplo:** ChatGPT Instant Checkout te permite comprar productos de Shopify directamente desde el chat. Google AI Mode tiene "Buy for me" para retailers seleccionados. Perplexity Pro tiene shopping integrado.

**Señal de que te falta esto:** Tus productos no están en Shopify Catalog mapeados correctamente. Tus PDPs no tienen el schema completo que los protocolos de agentic commerce requieren.

**Términos relacionados:**
- **UCP (Universal Commerce Protocol):** protocolo de Google + Shopify + retailers grandes (lanzado enero 2026)
- **ACP (Agent Commerce Protocol):** protocolo de OpenAI para Instant Checkout (fines de 2025)

---

### Schema Markup / JSON-LD

**Qué es:** Código invisible que se agrega a tu sitio para que **los buscadores y agentes IA entiendan exactamente qué hay en cada página**. JSON-LD es el formato técnico (la sintaxis) que Google y los engines generativos prefieren.

**Por qué importa:** Sin schema, los engines tienen que adivinar qué es tu página. Con schema, le decís explícitamente: "esto es un producto, cuesta X, tiene Y reviews, está disponible en Z tallas". Eso aumenta la probabilidad de aparecer en rich snippets, AI Overviews y respuestas generativas.

**Ejemplo:** Un PDP con schema Product + Offer + AggregateRating + FAQPage tiene 3-4x más probabilidad de aparecer en AI Overviews que un PDP sin schema, según estudios de 2026.

**Señal de que te falta esto:** Validás tu PDP en https://validator.schema.org/ y aparece vacío o con errores.

**Tipos esenciales para ecommerce:**
- `Product` — datos del producto
- `Offer` — precio, disponibilidad
- `AggregateRating` — promedio de reviews
- `FAQPage` — preguntas frecuentes
- `BreadcrumbList` — navegación
- `Article` / `BlogPosting` — para blog

---

## Conceptos de plataforma y CRM

### Klaviyo Customer Hub

**Qué es:** Funcionalidad nueva de Klaviyo (en beta para Shopify) que da al cliente **una cuenta de marca con tracking de pedidos, recomendaciones personalizadas, soporte y experiencias custom**. Va más allá del email marketing — es CRM completo.

**Por qué importa:** El cliente tiene un único lugar donde ve su historia con tu marca, sin tener que buscar emails ni revisar Shopify. Mejora retención, reduce tickets de "where is my order" y aumenta repeat purchase rate.

**Ejemplo:** Ministry of Supply usó Customer Hub y ganó 2,000 nuevas cuentas en 4 meses, con aumento de revenue per session.

**Señal de que te falta esto:** Tus clientes te escriben constantemente preguntando dónde está su pedido. Tu equipo de soporte responde lo mismo todos los días.

---

### Klaviyo Customer Agent

**Qué es:** Agente conversacional IA dentro de Klaviyo que **resuelve consultas de soporte y vende simultáneamente**. Conecta con datos en tiempo real (inventario, pedidos, perfil del cliente) para dar respuestas precisas y ofrecer productos relevantes.

**Por qué importa:** Resuelve hasta 90% de tickets nivel 1 sin humano, y convierte cada interacción de soporte en una posible venta. Casos públicos como LifeStraw reportaron +111% en ventas atribuidas a IA después del deploy.

**Ejemplo:** Cliente pregunta por WhatsApp "¿en qué viene mi pedido?". El Customer Agent responde con el tracking, ofrece el producto complementario que el cliente miró pero no compró, y aplica un cupón si es VIP. Todo en segundos, sin humano.

**Señal de que te falta esto:** Tu soporte es 100% humano y consume más de 10 horas/semana de equipo en preguntas repetitivas.

---

### CDP (Customer Data Platform)

**Qué es:** Plataforma que **unifica todos los datos de tu cliente en un solo lugar**: compras, navegación, emails, soporte, redes. Klaviyo Data ya cumple este rol con 350+ integraciones.

**Por qué importa:** Sin CDP, tus datos están fragmentados (Shopify por un lado, email por otro, soporte por otro). Con CDP, podés hacer segmentación predictiva, personalización avanzada y attribution que funciona.

**Ejemplo:** Sin CDP, no sabés que Juana abrió tu email, vio el producto X 3 veces en la web, abandonó el carrito, y después escribió por WhatsApp. Con CDP, todo eso es un único perfil que dispara el flow correcto.

**Señal de que te falta esto:** Tenés data en Shopify, en Mailchimp, en un Excel y en WhatsApp Business, todo separado.

---

### First-party data (Datos propios)

**Qué es:** Datos que vos capturaste directamente del cliente (con su consentimiento), no comprados ni inferidos por terceros. Ejemplos: email, comportamiento en tu web, historial de compra, preferencias declaradas en quizzes.

**Por qué importa:** Después de iOS 14 y la caída de cookies de terceros, los datos propios son **el único activo que sigue funcionando con precisión**. Las marcas que no tienen estrategia de first-party data dependen de canales que cada vez funcionan peor.

**Ejemplo:** Una marca con 50.000 emails de clientes que opt-in y datos de comportamiento puede correr campañas de Meta con audiencias custom 3-5x más efectivas que una marca sin esos datos.

**Señal de que te falta esto:** Tu lista de email tiene menos del 5% de tu base de clientes históricos. No sabés qué productos compraron ni qué les interesa.

---

## Conceptos de retención

### Predictive Segments

**Qué es:** Segmentos automáticos que **la IA crea y mantiene** basándose en comportamiento del cliente. Ejemplos: "alta probabilidad de churn", "due for replenishment" (le toca recomprar), "VIP", "win-back candidate".

**Por qué importa:** En vez de segmentar manualmente cada mes, la IA actualiza los segmentos en tiempo real y dispara los flows correctos automáticamente. Crece LTV sin trabajo manual.

**Ejemplo:** Klaviyo detecta que un cliente que compraba electrolitos cada 30 días no compra hace 45 → dispara flow de win-back con descuento + recordatorio de beneficio. Recupera al 30% antes de que se pierda definitivamente.

**Señal de que te falta esto:** No sabés cuáles de tus clientes están a punto de churnear. Te enterás cuando ya se fueron.

---

### Replenishment

**Qué es:** Estrategia para productos consumibles donde **predecís cuándo el cliente está por terminar el producto** y le ofrecés recompra antes de que tenga que pensarlo. Aplica fuerte en suplementos, beauty, pet food, cleaning, café.

**Por qué importa:** Si tu producto se consume cada 30 días, podés capturar la recompra 100% de las veces si avisás en el día 25 con la oferta correcta. Sin replenishment, el cliente se olvida o compra a la competencia que sí le avisó.

**Ejemplo:** Marca de café envía un email/WhatsApp el día 22 con "tu próxima bolsa se está acabando, dale +10% off si renovás antes del fin de semana". Recompra rate sube de 35% a 65%.

**Señal de que te falta esto:** Vendés consumibles pero no tenés ningún flow predictivo de recompra.

---

### LTV (Lifetime Value)

**Qué es:** Cuánto te va a comprar un cliente promedio **a lo largo de toda su vida como cliente**, no solo en su primera compra. Es la métrica que define la salud real de un ecommerce.

**Por qué importa:** Si tu CAC (costo de adquirir un cliente) es $20 y tu LTV es $40, el negocio funciona. Si el LTV es $25, estás en riesgo. Si es $15, perdés plata cada cliente nuevo. **El crecimiento sostenible viene de mover LTV, no solo de bajar CAC.**

**Ejemplo:** Marca A vende producto a $40 con LTV de $40 (compra una vez). Marca B vende producto a $40 con LTV de $200 (compra 5 veces). Marca B puede gastar 5x más en adquisición y seguir siendo rentable.

**Señal de que te falta esto:** No conocés tu LTV. Optimizás solo por ROAS de primera compra.

---

## Conceptos de medición

### Multi-channel Attribution

**Qué es:** Sistema que **asigna correctamente el crédito de cada venta a los canales que contribuyeron**, no solo al último click. Triple Whale, Shopify Analytics y herramientas similares ya lo entregan con IA.

**Por qué importa:** Si solo medís last-click, vas a sobrevalorar Google y subvalorar Meta, TikTok, email y orgánico. Las decisiones de inversión basadas en attribution rota destruyen margen.

**Ejemplo:** Una venta llegó después de: 1) ver Reel en TikTok, 2) buscar la marca en Google, 3) abrir email de carrito abandonado, 4) hacer click en último ad de Meta. Last-click le da 100% a Meta. Multi-channel atribuye porcentajes a cada canal.

**Señal de que te falta esto:** Decidís budget basado solo en lo que dice Meta Ads Manager o Google Ads. Sospechás que algunos canales están subatribuidos pero no podés probarlo.

---

### Tracking / Pixeles

**Qué es:** Códigos invisibles que se instalan en tu web para **registrar el comportamiento de cada visitante** y enviarlo a las plataformas de ads (Meta Pixel, TikTok Pixel, Google Ads conversion, GA4). Sin tracking correcto, las plataformas optimizan a ciegas.

**Por qué importa:** Las plataformas de ads aprenden de los pixeles. Si el pixel está mal instalado, Meta optimiza para "agregar al carrito" cuando vos querés "compra". Eso destruye ROAS sin que sepas por qué.

**Ejemplo:** Marca con pixel mal configurado: ROAS reportado 1.8x, ventas reales bajísimas. Después de fix: ROAS reportado 1.6x pero ventas reales 4x más altas, porque el pixel ahora optimiza correctamente.

**Señal de que te falta esto:** Tu ROAS reportado no coincide con tus ventas reales en Shopify. Las plataformas reportan conversiones distintas entre sí.

---

### CAPI (Conversions API)

**Qué es:** API server-side que envía datos de conversión a Meta directamente desde tu servidor, en vez de depender solo del pixel del navegador. Esquiva los bloqueos de iOS 14 y de los ad blockers.

**Por qué importa:** El pixel del navegador pierde aproximadamente 30-50% de eventos por iOS 14, ad blockers y privacidad. CAPI recupera buena parte de esos eventos. Sin CAPI, Meta optimiza con la mitad de la información.

**Ejemplo:** Marca solo con pixel: 60% de conversiones reportadas. Misma marca con CAPI: 92% de conversiones reportadas. Mismo ad spend, ROAS reportado sube 50% con datos más precisos.

**Señal de que te falta esto:** Tus reportes de Meta muestran muchas menos conversiones que tu Shopify Analytics.

---

## Las 7 Maletas (de Felipe Vergara)

**Qué es:** Marco de research del cliente desarrollado por Felipe Vergara que estructura toda la información necesaria para entender por qué alguien compra un producto. Las 7 maletas son: Cliente, Producto, Mercado, Competencia, Reviews, Redes y Anuncios.

**Por qué importa:** Sin investigación profunda, la propuesta de valor es genérica y los anuncios no convierten. Las 7 Maletas dan una base sólida para Foundations, Offer y Acquisition.

**Ejemplo:** Antes de armar campañas de Meta para una marca de skincare, hacer las 7 Maletas reveló que la audiencia real no era "mujeres 30-45 con piel sensible" sino "mujeres 28-38 con rutina influenciada por dermatólogos en Instagram". Cambió todo el creative y dobló el ROAS.

**Señal de que te falta esto:** Tu ICP es genérico. No sabés con palabras exactas qué dice tu cliente sobre su problema. No conocés a tus competidores en profundidad.

**Cómo se trabaja:** A través del skill `7-maletas` de Advanz que automatiza el research con análisis de reviews, social y ads.

---

## Conceptos LATAM específicos

### MercadoPago / Transbank / Flow

**Qué es:** Pasarelas de pago locales en LATAM. **Transbank** y **Flow** son chilenas. **MercadoPago** opera en toda la región (Chile, México, Colombia, Perú, Argentina). Cada plataforma maneja medios de pago locales, cuotas sin interés y compliance regulatorio.

**Por qué importa:** Sin pasarelas locales, perdés conversión en LATAM. Un checkout que solo acepta tarjetas internacionales convierte 30-50% menos que uno con cuotas, transferencia y débito local.

**Ejemplo:** Tienda chilena que solo acepta Stripe: CVR 1.2%. Misma tienda con Transbank + Webpay + Khipu: CVR 2.8%.

**Señal de que te falta esto:** Tu checkout no ofrece cuotas. No tenés transferencia bancaria como opción. Solo aceptas Stripe o PayPal.

---

### WhatsApp Business API

**Qué es:** API oficial de WhatsApp que permite **automatizar conversaciones, integrar con CRM y manejar volumen alto** sin perder la cuenta. Diferente del WhatsApp Business app (que es manual y limitado).

**Por qué importa:** En LATAM, WhatsApp es el canal #1 de conversación pre-venta y post-venta. Sin WhatsApp Business API, no podés escalar — la cuenta personal te limita a 256 contactos por broadcast y se bloquea con volumen.

**Ejemplo:** Marca chilena con 5.000 mensajes/mes de clientes. Con WhatsApp app: 1 persona dedicada respondiendo todo el día, escalación lenta. Con WhatsApp Business API + Klaviyo: agentes IA resuelven 80%, humano solo en casos complejos.

**Señal de que te falta esto:** Tu WhatsApp se bloquea, los clientes se quejan de tiempos de respuesta, no podés integrar la conversación con tu email/CRM.

---

## Cómo usar este glosario

Cuando el cliente o usuario menciona un término que no conoce, sacar la entrada relevante del glosario y contextualizarla al momento de la conversación. Cada entrada está pensada para responder en una sola explicación corta:
1. Qué es (sin tecnicismos)
2. Por qué importa para su negocio
3. Un ejemplo concreto
4. Cómo saber si le falta esto

**No tirar todo el glosario al cliente.** Sacar la entrada relevante, contextualizarla, seguir la conversación.
