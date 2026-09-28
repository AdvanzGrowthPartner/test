# Schema de la DB `repo-ecommerces` (Notion)

`data_source_id`: **`398a3015-2d00-808d-b2c3-000ba2c61301`**

Estas son las columnas exactas y sus valores válidos. Al cargar con `Notion:notion-create-pages` o actualizar con `Notion:notion-update-page`, usar estos nombres literales. **No crear columnas nuevas** salvo pedido explícito de Patricio.

> Antes de la primera carga de una sesión, si hay duda de que el schema cambió, correr `Notion:notion-fetch` sobre el `data_source_id` y comparar. Notion crea IDs de opción nuevos si se agregan valores no listados; usar siempre los valores exactos de abajo para no ensuciar los selects.

## Columnas

| Columna | Tipo | Valores válidos |
|---|---|---|
| `Nombre` | title | libre (nombre de la marca) |
| `Ecommerce` | url | URL de la tienda |
| `Categoria` | select | `Suplementos`, `Suplementos + Cosmetica`, `Suplementos + Alimento funcional`, `Deportivo/Nutricion`, `Skincare`, `Otro` |
| `Tags` | multi_select | `Marca propia`, `Vegano`, `Colageno`, `Magnesio`, `Proteina`, `Nutricosmetica`, `Alimento funcional`, `Hongos funcionales`, `Natural/Herbal`, `Electrolitos`, `Farmaceutica`, `B2B retail` |
| `Plataforma` | select | `Shopify`, `WooCommerce`, `Jumpseller`, `Wix`, `Por confirmar` |
| `Score` | number | 1 a 5 |
| `Score Nivel` | select | `5 - Buena oportunidad`, `4 - Alta`, `3 - Media`, `2 - Baja`, `1 - Poco probable`, `Cartera` |
| `Facturacion Estimada` | select | `Menos de 10k`, `Mas de 10k`, `Por verificar` |
| `Distribucion Retail` | select | `Si`, `No`, `Por verificar` |
| `Cartera Productos` | select | `1-3`, `3-10`, `+10`, `Por verificar` |
| `Ads Activos` | select | `Si`, `No`, `Por verificar` |
| `Meta Pixel` | select | `Si`, `No`, `Por verificar` |
| `Google Tag` | select | `Si`, `No`, `Por verificar` |
| `Analytics Tag` | select | `Si`, `No`, `Por verificar` |
| `Clarity Tag` | select | `Si`, `No`, `Por verificar` |
| `Klaviyo Tag` | select | `Si`, `No`, `Por verificar` |
| `Firma Agencia` | select | `No`, `Si`, `Por verificar` |
| `Cual Agencia` | text | libre |
| `WhatsApp` | phone_number | ej. `+56912345678` |
| `Instagram` | url | link al perfil |
| `Correo Contacto` | email | correo principal |
| `Correo Secundario` | email | correo alternativo |
| `Founder LinkedIn` | url | link al LinkedIn del founder o de la empresa |

## Mapeo desde el output del script `detect.py`

El script devuelve booleanos y strings; mapear así al cargar:

- `signals.meta_pixel` (true/false/"Por verificar") → `Meta Pixel` = `Si`/`No`/`Por verificar`
- `signals.google_tag` → `Google Tag`
- `signals.analytics` → `Analytics Tag`
- `signals.clarity` → `Clarity Tag`
- `signals.klaviyo` → `Klaviyo Tag`
- `signals.ads_activos` → `Ads Activos`
- `signals.reviews` (string o null) → va en la ficha del body, no hay columna dedicada de reviews
- `cartera_productos` → `Cartera Productos` (o `Por verificar` si null y la marca está bloqueada)
- `contacto.whatsapp` → `WhatsApp`
- `contacto.instagram` → `Instagram`
- `contacto.correo_contacto` → `Correo Contacto`
- `contacto.correo_secundario` → `Correo Secundario`
- `plataforma` → `Plataforma`

`Categoria`, `Tags`, `Score`, `Score Nivel`, `Facturacion Estimada`, `Distribucion Retail`, `Firma Agencia`, `Founder LinkedIn` los asigna el criterio del modelo (no salen del script): categoría y tags por lo que vende la marca; score y facturación por la lógica de la SKILL.md; distribución retail y firma de agencia se infieren o se dejan `Por verificar` para cerrar en discovery.

## Formato de la ficha en el body de cada página

Cada página lleva, además de las propiedades, una ficha escaneable en el cuerpo:

```markdown
## Ficha Outbound — [Marca]

**URL:** [url]
**Score:** [n]/5 — [emoji] [nivel]
**Categoría:** [cat] · **Plataforma:** [plataforma]

### Diagnóstico light del engine
| Señal | Estado |
|---|---|
| Meta Pixel | [✅/❌/⚪] |
| Google / GA | ... |
| Google Ads | ... |
| TikTok Pixel | ... |
| Klaviyo | ... |
| Clarity | ... |
| Reviews | [app o Ninguna] |
| Catálogo | [1-3/3-10/+10] |

### Contacto
- **WhatsApp:** ...
- **Instagram:** ...
- **Correo:** ...
- **Founder / LinkedIn:** ...

### Nota (ángulo de entrada)
[Qué le falta y por dónde entrar comercialmente. Ej: "Solo GA, sin Meta pixel ni
retención. Ángulo: tracking + email flows + reviews como quick wins."]
```

Los `Por verificar` (cuando Cloudflare bloqueó las señales) se anotan en la nota como pendientes de la fase de calificación del pipeline.
