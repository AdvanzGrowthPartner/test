# Schema JSON-LD para Blogs Shopify

Schema estructurado le dice a Google y a los LLMs **qué es** el contenido y **cómo interpretarlo**. Sin schema, el algoritmo tiene que adivinar; con schema, sabe.

Cada blog debe tener **2 bloques de schema** pegados al final del HTML del artículo:

1. **Article schema** — identifica el artículo, autor, fecha, tema
2. **FAQPage schema** — captura las preguntas/respuestas de los H2 para que aparezcan como rich results en Google y citas en LLMs

## Por qué embebido en el HTML del artículo (no en theme.liquid)

**Opción A (la default): schema embebido en el HTML del artículo.**
- Ventaja: el cliente NO tiene que tocar el tema/liquid.
- Ventaja: cada artículo controla su propio schema sin depender del dev.
- Desventaja: hay que copiar/pegar cada vez.

**Opción B: schema generado dinámicamente desde liquid.**
- Solo aplicar si el cliente tiene un dev disponible y quiere mantenerlo a largo plazo.
- Requiere editar `article.liquid` o `article-template.liquid`.

**Default: Opción A.**

## 1. Article Schema (template)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title completo del artículo]",
  "image": "[URL absoluta de la featured image]",
  "datePublished": "[YYYY-MM-DD de publicación]",
  "dateModified": "[YYYY-MM-DD de última edición]",
  "author": {
    "@type": "Person",
    "name": "[Nombre completo del profesional]",
    "jobTitle": "[Rol clínico completo con credenciales]",
    "knowsAbout": ["[Tema 1]", "[Tema 2]", "[Tema 3]", "[Tema 4]"]
  },
  "reviewedBy": {
    "@type": "Person",
    "name": "[Nombre del profesional]",
    "jobTitle": "[Rol clínico breve]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[Nombre de la marca]",
    "logo": {
      "@type": "ImageObject",
      "url": "[URL absoluta del logo]"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "[URL absoluta del artículo]"
  },
  "about": [
    {"@type": "[Tipo schema]", "name": "[Concepto principal del artículo]"},
    {"@type": "Thing", "name": "[Concepto secundario]"}
  ]
}
</script>
```

### Notas sobre cada campo

**`headline`**: literalmente el title del artículo. Si es más largo de 110 caracteres, Google lo rechaza. En ese caso, usar `name` en lugar de `headline`.

**`image`**: debe ser URL absoluta (con https://). Idealmente proporción 16:9 o 4:3. Mínimo 1200x630px para que sea elegible para AMP / Discover.

**`datePublished` y `dateModified`**: formato ISO 8601 `YYYY-MM-DD`. Si el artículo se edita después de publicar, **actualizar el dateModified** — Google da más peso a contenido reciente.

**`author.knowsAbout`**: lista de 3-5 temas en los que el profesional es experto. Esto le dice a Google y a los LLMs "este Person es autoridad en estos temas". Es uno de los factores más fuertes de E-E-A-T.

**`reviewedBy`**: si el autor y el revisor son la misma persona, igual incluirlo. Si son distintos (ej: nutricionista escribe, médico revisa), es aún más fuerte para YMYL.

**`about`**: array de hasta 3-4 conceptos centrales del artículo. Para YMYL, usar tipos schema más específicos cuando aplica:
- `MedicalCondition` — para condiciones médicas (Lipedema, Diabetes, etc.)
- `MedicalProcedure` — para procedimientos (Cirugía bariátrica, etc.)
- `Drug` — para medicamentos
- `Diet` — para dietas o regímenes alimentarios
- `Thing` — fallback genérico

### Ejemplo lleno (caso bariátrico)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Electrolitos en pacientes bariátricos: por qué son clave para una hidratación efectiva",
  "image": "https://cdn.shopify.com/s/files/1/0903/3092/3304/files/lipedema-electrolitos-amazing-care2.png?v=1779329483",
  "datePublished": "2026-05-13",
  "dateModified": "2026-05-22",
  "author": {
    "@type": "Person",
    "name": "Paula Camus",
    "jobTitle": "Nutricionista especialista en Cirugía Bariátrica y Lipedema",
    "knowsAbout": ["Cirugía bariátrica", "Nutrición clínica", "Hidratación", "Electrolitos"]
  },
  "reviewedBy": {
    "@type": "Person",
    "name": "Paula Camus",
    "jobTitle": "Nutricionista especialista en Cirugía Bariátrica"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Amazing Care",
    "logo": {"@type": "ImageObject", "url": "https://amazingcare.cl/cdn/shop/files/logo.png"}
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://amazingcare.cl/blogs/noticias/electrolitos-pacientes-bariatricos"
  },
  "about": [
    {"@type": "MedicalProcedure", "name": "Cirugía bariátrica"},
    {"@type": "Thing", "name": "Electrolitos"},
    {"@type": "Thing", "name": "Hidratación post-bariátrica"}
  ]
}
</script>
```

## 2. FAQPage Schema (template)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Pregunta literal del H2]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Respuesta de la lede-answer textual, sin las negritas, sin saltos de línea]"
      }
    }
    // ... una entry por cada H2 con respuesta directa
  ]
}
</script>
```

### Reglas para FAQPage

- **Una entry por cada H2** que tenga `<p class="lede-answer">`.
- El `name` debe ser **idéntico** al H2 (incluyendo signo de interrogación).
- El `text` debe ser **idéntico** a la respuesta directa (pero sin las etiquetas `<strong>`, sin saltos de línea, en una sola línea).
- Si el artículo tiene 5 H2 con respuesta directa, deben haber 5 entries.
- **No duplicar entries** (Google penaliza schema con duplicados).

### Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| Respuesta del schema diferente al contenido visible | Google marca "structured data mismatch" | Hacer copy-paste literal del `lede-answer` |
| Entries duplicadas | Schema rechazado | Revisar manualmente que cada `name` sea único |
| Comillas dobles dentro del `text` sin escapar | JSON inválido | Usar `\"` o reformular sin comillas |
| Más de 10 entries | Google las limita igual | Mantener 3-7 entries por FAQPage |

## Validación obligatoria

**Antes de marcar el artículo como publicado, validar los 2 schemas en:**

1. https://validator.schema.org — confirma que el JSON-LD es sintácticamente válido
2. https://search.google.com/test/rich-results — confirma que Google lo va a indexar como rich result

**Si alguno reporta error**, NO publicar. Los errores más comunes son:
- Comillas mal escapadas
- Fechas en formato incorrecto
- URL relativa donde debería ser absoluta
- Campos obligatorios ausentes (`headline`, `image`, `datePublished`)

Después de publicar y validar, **request indexing** en Google Search Console pegando la URL.

## Reglas YMYL especiales para schema

En contenido YMYL (salud, finanzas, legales), el schema debe incluir adicionalmente:

### `author` con perfil detallado
- `knowsAbout`: lista de temas de expertise
- `alumniOf`: universidad donde se tituló (si está disponible públicamente)
- `worksFor`: organización actual (si aplica)

### `reviewedBy` como pieza separada
Idealmente con un profesional distinto al autor (ej: nutricionista escribe, médico de la especialidad revisa). Si solo hay un profesional, igual incluirlo en `reviewedBy`.

### `about` con tipos schema específicos
Usar `MedicalCondition`, `MedicalProcedure`, `MedicalEntity` en lugar de solo `Thing`.

### Speakable schema (opcional, pero poderoso)
Marca qué partes del artículo se leen mejor en voz alta (asistentes de voz). Útil para conditional rich results.

```html
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [".intro-lede", ".lede-answer"]
}
```

Esto le dice a asistentes de voz "lee esto si te preguntan por este tema".

## Decisiones de schema para casos especiales

### Si el artículo no tiene profesional clínico (caso raro)
**No publicar como YMYL.** Si igual hay que publicarlo:
- `author` = Organization (la marca) en lugar de Person
- Sin `reviewedBy`
- Schema básico Article, no Article+MedicalWebPage

### Si el artículo es un listicle / comparativa
Sumar `ItemList` schema con los items comparados.

### Si el artículo es un how-to (paso a paso)
Cambiar Article por `HowTo` schema con `step` array.
