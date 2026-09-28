---
name: ecomm-scraping-cl
description: Motor de prospección outbound de Advanz para ecommerce de MARCA PROPIA en Chile. Detecta plataforma y stack (Meta pixel, Google/Analytics, Clarity, Klaviyo, reviews), estima tamaño y facturación, saca contacto (WhatsApp, Instagram, correo, founder), puntúa probabilidad de partner (1-5), y carga cada marca en la base Notion "repo-ecommerces" con ficha completa. Usa SIEMPRE que Patricio diga "levanta ecommerce", "scrapea marcas", "busca marcas propias", "prospecta suplementos CL", "carga ecommerce a la DB", "amplía el repo de outbound", "encuentra tiendas para outbound", "diagnostica esta tienda para outbound", "score de partner", "estima facturación de esta marca", "arma prospectos", "Ecomm Scraping", o cuando pegue una URL de tienda chilena para meterla al repo de outbound. También para correr el detector sobre un lote o completar la base con prospectos nuevos. SOLO marca propia DTC chilena (suplementos, nutricosmética, proteína, alimento funcional, skincare) — NO revendedores, farmacias ni multimarca.
---

# Ecomm Scraping (CL)

Motor de prospección outbound del Departamento Comercial de Advanz. Convierte una búsqueda o una URL en un **prospecto calificado** cargado en Notion: plataforma detectada, stack diagnosticado, tamaño estimado, contacto extraído y score de partner asignado.

El principio central: **solo marca propia DTC en Chile** (perfil Amazing Care / Obio / DogMom). Una marca que fabrica o formula lo suyo tiene un dueño con quien negociar y un negocio que escalar. Un revendedor multimarca (farmacias, tiendas que venden marcas de terceros, importadores) no es prospecto — se descarta siempre.

## Cuándo NO usar esta skill

- Análisis de UN cliente ya en cartera → skills de reporting/consultoría.
- Tiendas fuera de Chile.
- Tiendas que revenden marcas de terceros (no marca propia).
- Diagnóstico técnico profundo de una tienda (apps una por una) → `advanz-shopify-detector`. Esta skill hace diagnóstico *light* orientado a priorizar outbound, no auditoría completa.

## Destino de los datos (Notion)

Base **`repo-ecommerces`**, dentro de la página "Ecomm Scrapping (CL)":
`data_source_id`: **`398a3015-2d00-808d-b2c3-000ba2c61301`**
Ruta: Interno › Dept. Comercial › Departamento Comercial › Ecomm Scrapping (CL).

**El schema ya existe. Nunca crear columnas nuevas** salvo que Patricio lo pida explícitamente. El listado exacto de columnas y sus valores válidos está en `references/notion-schema.md` — leerlo antes de la primera carga de una sesión. Fuera de esa DB (workspace distinto, o si el data_source_id cambió), verificar con `Notion:notion-fetch` sobre la página antes de asumir.

## Flujo de trabajo

### 1. Conseguir marcas reales (nunca inventar dominios)

Adivinar dominios genéricos no funciona: la enorme mayoría da conexión muerta o resulta ser otra cosa (un "vidasana.cl" es una red de profesionales, no una marca). **Siempre partir de marcas reales**, verificadas por búsqueda web o aportadas por Patricio.

Buscar por ecosistema, no por producto: buscar "colágeno chile" trae marketplaces y farmacias. Buscar nombres concretos de marcas, listados de "marcas chilenas de suplementos", o founders emprendedores del rubro rinde marcas propias reales. Cuando una búsqueda devuelva puros revendedores, cambiar el ángulo (vertical distinto, o buscar la marca por su nombre + "sitio oficial").

Verticales válidos: suplementos, nutricosmética/colágeno, proteína/deportivo, alimento funcional, skincare de marca propia, mascotas de marca propia. Si el pool de un vertical se agota, ampliar a un vertical adyacente antes de forzar.

### 2. Detectar plataforma y señales

Usar el script incluido, que hace todo el pipeline técnico de una pasada:

```bash
python3 scripts/detect.py "https://ejemplo.cl" "https://otra.cl"
```

El script, por cada URL:
- **Pre-flight de plataforma** por firma en el HTML (`cdn.shopify`/`myshopify`→Shopify, `woocommerce`/`wp-content`→WooCommerce, `jumpseller`→Jumpseller, `wixstatic`→Wix).
- **Firma dura ante Cloudflare**: si el home devuelve 429 con body diminuto, consulta `/meta.json`, que devuelve el `myshopify_domain` real y confirma Shopify saltando el bloqueo. Esta es la técnica clave — funciona donde el scraping normal es rechazado.
- **Señales de stack** (grep del HTML): Meta Pixel (`fbq`), Google Tag (`gtag`/GTM), Analytics (GA), TikTok (`ttq`), Klaviyo (`_learnq`), Clarity (`clarity.ms`), reviews (judge.me/loox/stamped/okendo), WhatsApp, Instagram, correos.
- **Tamaño de catálogo** vía `/products.json` (Shopify) o `/product-sitemap.xml` (WooCommerce) → 1-3 / 3-10 / +10.

Devuelve un JSON por marca con todo lo detectable. Cuando Cloudflare bloquea, la plataforma se confirma por `meta.json` pero los tags de apps quedan `Por verificar` — se cierran manualmente en la fase de calificación del pipeline. Esto es esperado, no un error.

Ver `references/detection.md` para el detalle de firmas, endpoints y el manejo de casos borde (redirects JS, plataformas headless, dominios que no resuelven).

### 3. Calcular Score de partner (1-5) y facturación

**Score = probabilidad de cerrar como partner.** Combina oportunidad de mejora (substack) con capacidad de pagar (tamaño/madurez):

| Score | Nivel | Perfil |
|---|---|---|
| **5** | Buena oportunidad | Marca propia real MUY substackeada — le faltan piezas core (Meta pixel, Klaviyo, Clarity, reviews). Máximo espacio para agregar valor rápido. |
| **4** | Alta | Substackeada con algo de base; buena oportunidad, menos huecos. |
| **3** | Media | Stack parcial, o marca "Por verificar" (Cloudflare bloqueó señales). Oportunidad real, requiere más discovery. |
| **2** | Baja | Bastante equipada; poco margen obvio → conversación de performance, no de setup. |
| **1** | Poco probable | Stack completo y maduro. Poco espacio para entrar; sirve de benchmark del sector. |
| **Cartera** | — | Ya es cliente de Advanz. Fuera del outbound frío (archivar, no puntuar). |

Regla de substack: **más piezas faltantes = más substackeada = score más alto**. Una marca con solo Google Analytics y nada más es oro (score 5). Una con Meta+Klaviyo+Clarity+reviews+afiliados ya está resuelta (score 1).

**Facturación estimada** (`Menos de 10k` / `Mas de 10k` USD/mes) se infiere cruzando señales, no hay dato público:
- Probable **+10k**: distribución en retail físico (supermercados/farmacias = volumen y respaldo), ads activos (varias plataformas de pauta en simultáneo = presupuesto), catálogo grande, o stack maduro (Klaviyo+Clarity+reviews = inversión en operación).
- Probable **<10k**: solo Google Analytics, catálogo chico, sin ads corriendo, sin retención. Marca emergente.

Es señal direccional para priorizar el esfuerzo comercial, no un dato contable. Si no hay señales suficientes (marca bloqueada), dejar `Por verificar`.

### 4. Cargar a Notion

Antes de cargar, leer `references/notion-schema.md` para los nombres y valores exactos de las columnas. Luego, por cada marca, crear una página en la DB con:

- **Todas las propiedades** rellenas (las detectables con dato real; las bloqueadas como `Por verificar`).
- **Ficha completa en el body**: URL, score, categoría, plataforma, tabla de diagnóstico de señales, contacto, y una nota corta con el *ángulo de entrada* (qué le falta y por dónde entrar comercialmente).

Antes de cargar, **evitar duplicados**: si no es obvio que la marca ya está en la DB, verificar. Amazing Care es cartera (archivada) — nunca re-agregarla como prospecto frío.

Batch: cargar de a ~10 páginas por llamada para no saturar. Al terminar, ordenar la vista por Score descendente para que los prospectos calientes queden arriba.

### 5. Fichas de contacto

WhatsApp e Instagram salen del home (el script los extrae). El correo sale de `/contacto` o de las políticas. Founder + LinkedIn requieren búsqueda dirigida y **en marcas chicas rara vez están indexados en prensa** — no quemar decenas de búsquedas persona por persona; se completan en el setting del pipeline. Cuando un founder aparece con nombre claro (ej. figura mediática del rubro), sí registrarlo.

## Reglas duras

- **Solo marca propia CL.** Revendedores, farmacias, multimarca e importadores se descartan siempre.
- **Nunca cargar un dominio no verificado.** Solo URLs confirmadas por pre-flight o `meta.json`. Si una marca no resuelve desde el entorno, marcarla `Por confirmar` en plataforma y anotarlo, no inventar.
- **No crear columnas** salvo pedido explícito. El schema ya está montado.
- **Cada ficha es output del sistema, no tarea manual de Patricio.** Su rol es acompañar (llamada) y dar claridad (roadmap). Nunca listar "pendientes del consultor".
- El score mide *probabilidad de partner*, no solo substack: una marca substackeada pero sin negocio real (catálogo de 1 producto, cero tráfico) no es un 5.

## Alimenta

Esta base es el front del **Departamento Comercial** (Leads → Llamadas → Cotizaciones → Clientes). Los prospectos de score alto entran al pipeline: cold outbound por WhatsApp/Instagram → calificación en detalle → diagnóstico A250 → propuesta.
