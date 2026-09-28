---
name: advanz-shopify-blog-publisher
description: Publica blogs SEO/GEO optimizados en Shopify con pattern dual (respuesta directa + expansión), schema JSON-LD embebido, CSS bulletproof que sobrevive a temas de Shopify, y manejo correcto de YMYL para clientes de salud, suplementos y bienestar. Usa SIEMPRE que el usuario diga "publicar blog en Shopify", "armar blog con SEO", "blog para [cliente]", "enriquecer con SEO", "blog dual SEO GEO", "schema para blog", "corregir blog publicado", "rehacer blog Shopify", "blog para nutricionista", "blog de salud ecommerce", "FAQ schema", "redirect 301 blog", "blog YMYL"; cuando pegue contenido escrito por un profesional clínico (nutricionista, médico, kinesiólogo) para preparar a Shopify; o cuando comparta un blog ya publicado con problemas de CSS/contenido. NO usar para landing pages, páginas de producto, ni blogs WordPress — específico para artículos de blog en Shopify DTC. Aplicable a cualquier vertical ecommerce (suplementos, skincare, mascotas, alimentos funcionales, wellness).
---

# Advanz Shopify Blog Publisher

Sistema completo para publicar blogs en Shopify con optimización SEO + GEO (Generative Engine Optimization, citas en ChatGPT/Claude/Perplexity), pensado para clientes DTC del portfolio Advanz. Contiene templates probados en producción y aprendizajes específicos del comportamiento real de los temas de Shopify.

## Cuándo se activa este skill

- Cliente entrega contenido escrito por un profesional (nutricionista, médico) y hay que prepararlo para publicar.
- Hay que **rehacer** o **corregir** un blog ya publicado que no se ve bien.
- Se necesita **enriquecer** contenido existente con SEO/GEO sin reinventarlo.
- Hay que generar **ideas de blogs** nuevos para un cluster topical.
- Se necesita decidir **handle**, **meta tags**, **excerpt**, **author**, **tags** para un artículo.

## Reglas operativas (NO negociables)

### Regla 1 — Respetar el contenido del cliente
Cuando el cliente o un profesional entrega contenido, **NO se reescribe ni se resume**. Solo se **enriquece** con elementos SEO/GEO:
- Respuesta directa en negrita al inicio de cada sección
- H2 con pregunta literal que la gente busca
- Internal link a colección relevante
- Author box, disclaimer YMYL, schema
- Bibliografía respetada tal cual

Si Claude se descubre reescribiendo párrafos del cliente, detenerse y solo enriquecer.

### Regla 2 — Author = profesional clínico, NO agencia
En contenido YMYL (salud, suplementos, lipedema, bariátrica, deporte, embarazo, etc.), el campo **Author** en Shopify y en el schema Person DEBE ser el profesional clínico que firma el contenido. **Nunca poner "Advanz" como autor** de contenido clínico — destruye el E-E-A-T y el ranking en YMYL.

### Regla 3 — Verificar la paleta REAL de la marca
Antes de aplicar cualquier CSS, **verificar la paleta real** del sitio del cliente. No asumir. Si no se conoce, fetch el sitio o pedir el manual de marca. Aplicar un color equivocado (ej: violeta cuando la marca es celeste) hace que el cliente rechace el trabajo aunque el SEO esté perfecto.

### Regla 4 — Usar `em`, NO `rem` ni `px` para tipografía
Los temas de Shopify usan tamaños grandes de cuerpo (~22-24px). Si los destacados se fuerzan a `font-size: 1rem` o `16px`, **se ven más chicos que el cuerpo del artículo** y quedan ilegibles. Usar siempre `em` (relativo al contenedor padre) para que la tipografía escale con el tema.

- ✅ `font-size: 1.15em` (15% más grande que el cuerpo)
- ❌ `font-size: 1.05rem` (te clava a 17px aunque el tema tenga 24px)
- ❌ `font-size: 18px` (absoluto, peor todavía)

### Regla 5 — Schema embebido en el HTML del artículo
Para no tocar el tema/liquid del cliente, **los 2 scripts JSON-LD (Article + FAQPage) van pegados al final del HTML del artículo en el editor**, no en `theme.liquid` ni en una sección custom. Esto se llama "Opción A" y es la default.

### Regla 6 — Redirect 301 al cambiar handle
Si se cambia el handle/URL de un artículo ya publicado, **siempre activar el redirect 301** que Shopify ofrece al guardar. Si no se activa: se pierde el SEO acumulado del URL viejo y se generan 404s para links externos.

### Regla 7 — Pattern dual SEO+GEO por cada H2
Cada H2 sigue esta estructura:
1. **H2** = pregunta literal que la gente busca (ej: "¿Por qué el agua sola no es suficiente?")
2. **Respuesta directa** en `<p class="lede-answer"><strong>...</strong></p>` — 1-2 frases que respondan la pregunta autocontenidamente (lo que extraen Google featured snippets y los LLMs)
3. **Expansión** en párrafo normal — desarrollar la idea
4. **Lista o tabla** — escaneable
5. **Cierre** opcional con contexto adicional

### Regla 8 — Imágenes centradas con `<div class="article-image-center">`
El editor de Shopify mete `margin-left: 43.2315px; margin-right: 43.2315px;` en píxeles que NO centran en responsive. Reemplazar siempre por:
```html
<div class="article-image-center"><img src="..." alt="..." width="..." height="..."></div>
```

## Flujo de trabajo

### Caso A — Blog nuevo desde contenido del cliente

1. **Recibir** el contenido del cliente (Notion, Word, texto pegado).
2. **Verificar paleta de marca** del cliente. Si no se sabe, fetch el sitio.
3. **Identificar profesional clínico** que firma. Si no aparece, preguntar antes de continuar.
4. **Definir handle SEO-friendly** (kebab-case, palabras clave del topic).
5. **Generar campos SEO**: title (respetar el del cliente si lo dio), meta title, meta description, excerpt, tags. Ver `references/seo-fields.md`.
6. **Construir HTML** usando el template en `templates/blog-post-complete.html`. Aplicar pattern dual a cada H2. Ver `references/html-skeleton.md`.
7. **Insertar CSS bulletproof** al inicio del HTML. Ver `references/css-bulletproof.md` (cambiar variables de color por la paleta real del cliente).
8. **Insertar schema JSON-LD** al final del HTML. Ver `references/schema-templates.md`.
9. **Entregar al cliente** con los pasos exactos para pegar en Shopify. Ver `references/shopify-implementation.md`.

### Caso B — Corregir un blog ya publicado

1. **Diagnosticar el problema**: ¿contenido incorrecto en URL incorrecta? ¿CSS roto? ¿paleta equivocada? ¿texto colapsado?
2. **Si hay confusión de contenido** (ej: bariátrico publicado en URL de lipedema): cambiar title + handle + meta + tags + featured image, activar redirect 301.
3. **Si es problema de CSS**: revisar `references/lessons-learned.md` antes de proponer cambios. La mayoría de los problemas visuales ya fueron diagnosticados ahí.
4. **Pedir screenshot al usuario** del problema visual antes de tocar nada. No iterar a ciegas.
5. **Aplicar el CSS bulletproof** completo del template — es probable que el CSS anterior tenga errores comunes (rem en vez de em, color equivocado, margins ausentes).

### Caso C — Generar ideas de blogs para un cluster topical

1. **Identificar el pillar comercial** del cliente (ej: "Mejores [producto] en [país] [año]") — es la pieza más importante del cluster.
2. **Identificar 3-4 soportes** que cubran:
   - Caso de uso médico/condición (YMYL si aplica)
   - Caso de uso deportivo
   - Caso de uso lifestyle moderno (ayuno, vegano, etc.)
   - Soporte informacional puro (comparativo de tipos, ingredientes)
3. **Crear tarjetas en Notion** con etiquetas existentes del board del cliente. Ver `templates/notion-card-template.md`.
4. **Cada tarjeta** debe tener: contexto estratégico, objetivo SEO (query principal/secundarios/intención), estructura sugerida, preguntas para validar con el profesional clínico, recomendación de mes para publicar.

## Estructura del skill

| Archivo | Cuándo leerlo |
|---|---|
| `references/css-bulletproof.md` | Siempre que se arme HTML de un blog. Es el CSS probado en producción. |
| `references/html-skeleton.md` | Para entender el pattern dual SEO+GEO en cada H2. |
| `references/seo-fields.md` | Cuando hay que definir title/meta/handle/excerpt/tags. |
| `references/schema-templates.md` | Para insertar Article + FAQPage schema. Incluye reglas para YMYL. |
| `references/shopify-implementation.md` | Cuando hay que entregar instrucciones de pegado al cliente. |
| `references/ymyl-rules.md` | Para contenido de salud, suplementos, bienestar. NO opcional si el blog toca salud. |
| `references/lessons-learned.md` | Antes de iterar sobre un blog ya publicado. Lista de errores comunes con sus correcciones. |
| `templates/blog-post-complete.html` | Template completo HTML+CSS+schema listo para llenar. |
| `templates/notion-card-template.md` | Para crear tarjetas de ideas de blogs en boards de Notion. |

## Triggers de re-lectura

Cuando aparezca alguna de estas situaciones a mitad del flujo, releer el reference correspondiente:

- Cliente pide cambiar color/paleta → re-leer `lessons-learned.md` sección "Color de marca"
- Cliente dice "se ve gigante" o "se ve chico" → re-leer `lessons-learned.md` sección "Tipografía em vs rem"
- Cliente dice "no se centra" → re-leer `lessons-learned.md` sección "Imágenes responsive"
- Cliente pide cambiar autor → re-leer `ymyl-rules.md`
- Cliente pregunta por el redirect → re-leer `shopify-implementation.md` sección "Cambio de handle"
- Cliente cambia el topic del blog (ej: era lipedema, ahora es bariátrico) → re-leer `lessons-learned.md` sección "Corrección de contenido publicado"

## Output esperado

El skill entrega **siempre** estos artefactos al cliente:

1. **HTML completo** (CSS + cuerpo + schema embebido) listo para pegar en Shopify modo `<>`.
2. **Tabla de campos SEO** (title, handle, meta title, meta description, excerpt, tags, author, featured image alt) con valores específicos.
3. **Checklist de implementación** numerada con los pasos exactos en Shopify (renombrar imágenes, modo HTML, pegar, validar schema, request indexing).
4. **Justificación** breve de cada decisión SEO (por qué este handle, por qué este meta title, por qué este pattern dual).

## Lo que este skill NO hace

- No publica directamente en Shopify vía API (todo se pega manualmente o vía MCP de Shopify si está disponible).
- No genera contenido clínico desde cero — el contenido viene del profesional del cliente.
- No reemplaza al profesional clínico para validar afirmaciones de salud.
- No es para B2B, lead gen, ni landing pages — solo blogs de ecommerce DTC.
