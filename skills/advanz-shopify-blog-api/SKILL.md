---
name: "advanz-shopify-blog-api"
description: "Publicar y corregir artículos de blog en Shopify vía Admin API GraphQL (articleCreate/articleUpdate) sin destruir trabajo existente. Usar al publicar por API, editar un artículo ya publicado, o diagnosticar CTR con Search Console. Complementa advanz-shopify-blog-publisher."
---

# Shopify Blog — Publicación por API

Fork técnico de `advanz-shopify-blog-publisher`. Aquel cubre **contenido y diseño**: templates HTML, CSS bulletproof, paleta, reglas YMYL, pattern dual SEO+GEO. Este cubre la **operación por API**: cómo escribir en Shopify sin romper lo que ya está publicado.

Los dos se usan juntos. Si el trabajo es armar el HTML → el base. Si es escribirlo en la tienda → este.

## Cuándo se activa

- Publicar un artículo vía MCP de Shopify en vez de pegarlo a mano.
- Corregir un artículo **ya publicado** (una fecha, un link, una palabra).
- Auditar CTR/posición con un export de Search Console.
- Asignar SEO title, meta description, tags, autor o template por API.

---

# 🔴 Regla 1 — El body es full-replace: leer, modificar, devolver

**Existe porque ya se puso en riesgo trabajo del cliente.**

El campo `body` de Shopify es un bloque único. `articleUpdate` **reemplaza el body completo**; no hay operación de parche. Escribir desde la copia que uno tiene en contexto borra en silencio todo lo agregado desde afuera: imágenes insertadas en el cuerpo, correcciones del cliente, ajustes hechos en el editor.

**Flujo obligatorio para CUALQUIER cambio sobre un artículo existente:**

1. `graphql_query` → traer el `body` actual, **siempre**, aunque uno crea saber qué dice.
2. Search-and-replace **sobre ese texto**, solo al fragmento que cambia.
3. `articleUpdate` con el resultado.

Nunca reconstruir el body desde cero para arreglar una frase, una fecha o un link.

## Qué sobrevive a un reemplazo de body

| Elemento | Dónde vive | ¿Sobrevive? |
|---|---|---|
| Imagen destacada / portada | campo `image` | ✅ Sí |
| SEO title y meta description | metafields `global.*` | ✅ Sí |
| Tags, handle, autor, estado, templateSuffix | campos propios | ✅ Sí |
| **Imágenes dentro del artículo** | dentro de `body` | ❌ **NO** |
| **Cualquier edición hecha en el admin** | dentro de `body` | ❌ **NO** |

## Cuándo NO tocar por API y mandar a manual

Si el cambio es de **una o dos palabras** y el artículo ya tiene imágenes insertadas en el cuerpo o ya fue editado por el cliente: **avisar y que se haga a mano en el editor**. El riesgo de una reescritura no compensa ahorrarle un minuto a alguien.

Decirlo explícito: qué hay que cambiar, dónde, y por qué conviene a mano.

---

# 🔴 Regla 2 — Checklist pre-publicación

Errores reales cometidos en producción. Revisar los seis **antes** de cada `articleCreate` o `articleUpdate`.

### 1. URLs de colección sin tildes ni mayúsculas
Se publicó un botón a `/collections/hidratación-esencial` con tilde → renderizó como `hidrataci%C3%B3n-esencial` → 404 en vivo.

Los handles de Shopify son minúscula, sin tildes, sin ñ, con guiones. **Confirmarlos con una query de colecciones, nunca escribirlos de memoria:**

```graphql
query { collections(first: 50) { nodes { handle title productsCount { count } } } }
```

### 2. Fechas y deadlines
Se publicó "pide antes del domingo 14" cuando el 14 ya había pasado — y la fecha estaba en **tres lugares a la vez**: el bloque visual, la FAQ y el JSON-LD.

- Verificar el día de la semana con búsqueda web antes de escribir una fecha.
- **Preferir plazos que no caduquen** ("verás el plazo de entrega en el checkout") sobre fechas duras.
- Si un dato aparece en varios lugares, corregir todos o ninguno.

### 3. Ortografía del texto visible
Se publicó "evvalúe". Releer el texto que ve el usuario, no solo el HTML.

### 4. Sin placeholders
Buscar `[`, `REEMPLAZAR`, `TODO`, `nutricionista:` antes de publicar.

**Nunca publicar un esqueleto para "ganar volumen de aparición".** Corchetes de estructura indexados restan, no suman. Si el contenido necesita una afirmación que un profesional debe respaldar, se escribe antes de publicar o se deja en borrador.

### 5. Coherencia del schema con el handle real
El `mainEntityOfPage` y el `BreadcrumbList` deben apuntar al handle **real** del artículo. Caso visto: schema apuntando a `/electrolitos-migrana` cuando el handle era `/electrolitos-para-migrana`.

También: ningún `"image": "REEMPLAZAR_URL_CDN_HERO"` literal.

### 6. templateSuffix tiene que existir
`templateSuffix: "article"` requiere que exista `templates/article.article.json` en el tema. Si no existe, Shopify cae silenciosamente al default y el sufijo no hace nada.

Verificar antes:

```graphql
query { theme(id: "gid://shopify/OnlineStoreTheme/ID") {
  files(filenames: ["templates/article.json", "templates/article.article.json"], first: 10) { nodes { filename size } } } }
```

---

# 🔴 Regla 3 — Verificar en vivo después de publicar

No asumir que quedó bien. Hacer fetch de la URL publicada y revisar:

- Que los links renderizan sin encodear (`%C3%B3` = tilde que rompe).
- Que no quedaron placeholders visibles.
- Que el bloque de schema está presente.
- Que el contenido termina donde debe.

Es el único modo de distinguir un problema propio de uno del tema o de una app. Caso visto: una sección con productos placeholder que parecía rota resultó no existir en la página publicada — estaba solo en el editor de temas, sin guardar.

---

## Límites del API: qué se puede y qué no

| Se puede | No se puede |
|---|---|
| Crear, editar, publicar y despublicar artículos | Escribir en el tema **publicado** (MAIN) |
| Metafields de SEO, tags, autor, handle, template | Configurar secciones desde el editor de temas |
| Leer archivos del tema (`theme.files`) | Tocar configuración de apps de terceros |
| Colecciones, productos, precios | Subir imágenes desde disco local |

Cuando el problema está en una sección del tema o en una app, **decirlo y pasar la pelota**. Indicar qué hay que configurar y dónde, con los valores concretos (ej: qué colección asignar, de las que existen de verdad).

Las imágenes requieren URL HTTPS pública. El cliente sube las suyas; no intentar rutas locales.

---

## Flujo de publicación por API

**Siempre en este orden.** Saltarse la validación genera campos alucinados.

1. `graphql_schema` → confirmar nombres de tipos y campos.
2. `validate_graphql_codeblocks` → validar la operación.
3. `graphql_mutation` / `graphql_query` → ejecutar.

### Campos que NO existen (errores confirmados)

- `Blog.seo` y `Article.seo` **no existen**. El SEO vive en metafields.
- `Blog.articles` **no acepta `sortKey`**. Solo `first` y `reverse`.

### SEO por metafields

```graphql
mutation SetSeo($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { key value }
    userErrors { field message }
  }
}
```

Con `namespace: "global"`, `key: "title_tag"` y `"description_tag"`, `type: "single_line_text_field"`, `ownerId` = GID del artículo.

### Autor: acepta texto libre

`author: { name: "..." }` **no requiere un usuario staff de Shopify.** Esto desbloquea reatribuir artículos firmados por la agencia al profesional real que los escribió — el problema de E-E-A-T más caro en contenido YMYL, corregible en una sola pasada por API.

Si no hay profesional asignado, **preguntar antes de publicar**. No firmar con la agencia y no inventar un nombre clínico.

### Un artículo por llamada

No agrupar varios `articleCreate` con alias en una sola mutation. Falla por manejo de variables y deja estado a medias. Una llamada por artículo, verificando cada resultado.

### Borrador vs publicado

`isPublished: false` crea el borrador. Publicar recién cuando el contenido esté completo y el checklist pasado.

---

## Estructura del artículo

### 🔴 Copy siempre en positivo

El framing negativo quema la compra. El lector tiene que entender que esto es **una solución**, no una lista de lo que el producto no hace.

**Prohibido como estructura:**
- Tablas "Qué sí puede / Qué NO puede"
- Titulares negativos: "¿Por qué el agua sola NO alcanza?"
- Negaciones dentro del `lede-answer`, que es justo el bloque que Google y los LLMs extraen

**La precisión no se negocia** — se consigue afirmando lo que el producto sí hace, con el alcance correcto:

| En vez de | Escribir |
|---|---|
| "El agua sola no alcanza" | "El agua repone el líquido; la fórmula repone además los minerales que se fueron con él" |
| "No cura X" | "Repone lo que X te hizo perder, que es una de las causas del malestar" |
| "No reemplaza el tratamiento médico" | (va SOLO en el disclaimer, nunca en el cuerpo) |

Las negaciones van exclusivamente en el bloque de disclaimer al cierre, donde son obligatorias y explícitas.

### Responder la pregunta como la gente la escribe

H2 y FAQ con la **formulación literal de la query**, sacada de Search Console (pestaña Consultas) o del "Otras preguntas de los usuarios" del SERP — no con la versión que suena mejor.

- Query `magnesio para que sirve` → H2 "¿Para qué sirve el magnesio?", no "Beneficios del magnesio".
- Verificar que la keyword objetivo aparezca en: SEO title, H1, primer `lede-answer` y al menos un H2.
- Las FAQ salen de queries reales, no inventadas.

### Sin relleno, con tope

- **Máximo 6 H2 y ~1.200 palabras.** Si se pasa, sobra contenido.
- Prohibido repetir en la expansión lo que ya dijo el `lede-answer`, y los "En resumen" que solo reformulan.
- Tabla o lista antes que párrafo siempre que se pueda.
- Incluir una pregunta **comercial** en la FAQ (plazos de entrega, cómo elegir) — captura intención de compra dentro del artículo.

### Bloques JSON-LD

Tres, siempre: `Article`, `BreadcrumbList`, `FAQPage`. El `FAQPage` es lo que compite por AI Overviews.

---

## Diagnóstico con Search Console

El export de GSC llega como ZIP con `Consultas.csv`, `Páginas.csv`, `Gráfico.csv`, `Países.csv`, `Dispositivos.csv`. Procesar con pandas, no leer a ojo.

**El análisis que importa: CTR contra posición, no posición sola.**

Patrón encontrado en producción: los artículos con más impresiones tenían el **peor** CTR. 22.500 impresiones → 53 clics (0,24%). La relación estaba invertida.

Cuando eso pasa, el problema **no es de ranking, es de título y meta**. El CTR se decide en la SERP, antes de que nadie entre. Reescribir SEO title y meta con la query literal rinde más que cualquier pieza nueva.

### Cortes útiles

1. **Blog vs sitio**: qué % de impresiones y clics aporta el blog, y comparar CTR de ambos.
2. **Brand vs no-brand**: separar queries con el nombre de marca. El tráfico no-brand es el que mide SEO real.
3. **La veta**: posición 4-15, impresiones >300, clics ≤5. Visible y sin clics = título que no responde la query.
4. **Basura indexada**: anclas (`#seccion`) indexadas como URLs propias compitiendo con su artículo padre, paginación `?page=N`, artículos fantasma de page builders, URLs con typo.
5. **Nichos**: agrupar queries por tema y comparar volumen contra CTR. Un nicho puede convertir 10× mejor y tener 100× menos volumen — eso cambia la estrategia, no la valida.

Sin GSC ni Ahrefs operativos, las keywords se proponen por criterio de SERP y **quedan marcadas como pendientes de validar**. No presentar estimaciones como dato medido.

---

## Sincronización con la grilla de contenidos

Al publicar, actualizar el registro en Notion en la misma pasada: URL real, estado, fecha, categoría, título SEO, keyword objetivo, meta description.

- Los campos `select` solo aceptan valores existentes. Un valor nuevo hace fallar la llamada completa — consultar el schema del data source antes de escribir.
- Dejar anotado en la tesis lo que quedó **pendiente de validación** (claim que revisa un profesional, keyword sin volumen medido, conflicto de canibalización).
- Revisar que la URL de la grilla coincida con el handle real. Caso visto: dos artículos apuntando a la misma URL y uno marcado "Publicado" que nunca existió.

---

## Lo que este skill NO hace

- No reemplaza a `advanz-shopify-blog-publisher` para HTML, CSS, paleta ni reglas YMYL.
- No escribe contenido clínico desde cero ni valida afirmaciones de salud.
- No configura secciones del tema ni apps de terceros.
- No sube imágenes: requieren URL HTTPS pública.
- No garantiza que un archivo de skill editado en disco persista — los skills se guardan desde la propuesta, no escribiendo el archivo.