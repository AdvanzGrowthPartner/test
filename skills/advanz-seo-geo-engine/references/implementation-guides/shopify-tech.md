# Implementación Técnica — Shopify

Guía operativa para devs de Advanz (Felipe, Matías, freelancers) implementando SEO/GEO en Shopify.

---

## Archivos clave del theme

### Para títulos y metas
- `layout/theme.liquid` — head global, fonts, meta viewport
- `sections/header.liquid` — esquema de meta tags
- `snippets/social-meta-tags.liquid` — OpenGraph y Twitter Cards
- `templates/*.liquid` y `templates/*.json` — template específico por tipo de página

### Para schema/JSON-LD
- `snippets/structured-data.liquid` (a crear si no existe)
- `templates/product.json` o `templates/product.liquid`
- `templates/collection.json`
- `templates/article.liquid`

### Para performance
- `assets/theme.css` — CSS principal
- `assets/theme.js` — JS principal
- `layout/theme.liquid` — donde se cargan scripts

---

## Schema Organization en home

Crear `snippets/schema-organization.liquid`:

```liquid
{% if template == 'index' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{{ shop.name }}",
  "legalName": "Razón Social SpA",
  "url": "{{ shop.url }}",
  "logo": "{{ 'logo.png' | asset_url }}",
  "foundingDate": "2022-01-01",
  "founder": {
    "@type": "Person",
    "name": "Nombre Fundador"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle X 1234",
    "addressLocality": "Santiago",
    "addressRegion": "Región Metropolitana",
    "postalCode": "7500000",
    "addressCountry": "CL"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+56-2-2XXX-XXXX",
    "contactType": "Customer Service",
    "areaServed": "CL",
    "availableLanguage": "Spanish"
  },
  "sameAs": [
    "https://www.instagram.com/marca",
    "https://www.tiktok.com/@marca",
    "https://www.facebook.com/marca",
    "https://www.linkedin.com/company/marca",
    "https://www.mercadolibre.cl/perfil/marca",
    "https://www.wikidata.org/wiki/QXXXXXX"
  ]
}
</script>
{% endif %}
```

Incluir en `layout/theme.liquid` dentro de `<head>`:
```liquid
{% render 'schema-organization' %}
```

---

## Schema Product en PDPs

Crear o editar `snippets/schema-product.liquid`:

```liquid
{% if template contains 'product' %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{ product.title | escape }}",
  "description": "{{ product.description | strip_html | escape }}",
  "image": [
    {% for image in product.images %}
      "{{ image | image_url: width: 1200 }}"{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ],
  "sku": "{{ product.selected_or_first_available_variant.sku }}",
  "mpn": "{{ product.selected_or_first_available_variant.barcode }}",
  "brand": {
    "@type": "Brand",
    "name": "{{ product.vendor }}"
  },
  "offers": {
    "@type": "Offer",
    "url": "{{ shop.url }}{{ product.url }}",
    "priceCurrency": "{{ cart.currency.iso_code }}",
    "price": "{{ product.selected_or_first_available_variant.price | money_without_currency | remove: ',' | remove: '.' | divided_by: 100.0 }}",
    "priceValidUntil": "{{ 'now' | date: '%Y' | plus: 1 }}-12-31",
    "availability": "{% if product.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
    "seller": {
      "@type": "Organization",
      "name": "{{ shop.name }}"
    }
  }
  {% if product.metafields.reviews.rating_count > 0 %}
  ,"aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{{ product.metafields.reviews.rating }}",
    "reviewCount": "{{ product.metafields.reviews.rating_count }}"
  }
  {% endif %}
}
</script>
{% endif %}
```

---

## Schema FAQPage

Crear `snippets/schema-faq.liquid` que toma metafield con preguntas:

```liquid
{% if product.metafields.custom.faq.value %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {% for item in product.metafields.custom.faq.value %}
    {
      "@type": "Question",
      "name": "{{ item.question | escape }}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{ item.answer | escape }}"
      }
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>
{% endif %}
```

Setup metafield en admin: `custom.faq` (tipo list of objects con question + answer).

---

## Schema BreadcrumbList

Crear `snippets/schema-breadcrumb.liquid`:

```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "{{ shop.url }}"
    }
    {% if template contains 'product' and product.collections.first %}
    ,{
      "@type": "ListItem",
      "position": 2,
      "name": "{{ product.collections.first.title }}",
      "item": "{{ shop.url }}{{ product.collections.first.url }}"
    }
    ,{
      "@type": "ListItem",
      "position": 3,
      "name": "{{ product.title }}",
      "item": "{{ shop.url }}{{ product.url }}"
    }
    {% elsif template contains 'collection' %}
    ,{
      "@type": "ListItem",
      "position": 2,
      "name": "{{ collection.title }}",
      "item": "{{ shop.url }}{{ collection.url }}"
    }
    {% endif %}
  ]
}
</script>
```

---

## Title y meta description dinámicos

En `layout/theme.liquid` dentro de `<head>`:

```liquid
<title>
  {%- if template == 'index' -%}
    {{ shop.metafields.seo.home_title }}
  {%- elsif template contains 'product' -%}
    {{ product.metafields.seo.title | default: product.title }} | {{ shop.name }}
  {%- elsif template contains 'collection' -%}
    {{ collection.metafields.seo.title | default: collection.title }} | {{ shop.name }}
  {%- elsif template contains 'article' -%}
    {{ article.title }} | {{ shop.name }}
  {%- else -%}
    {{ page_title }} | {{ shop.name }}
  {%- endif -%}
</title>

<meta name="description" content="{%- if template == 'index' -%}{{ shop.metafields.seo.home_description }}{%- elsif template contains 'product' -%}{{ product.metafields.seo.description | default: product.description | strip_html | truncatewords: 25 }}{%- elsif template contains 'collection' -%}{{ collection.metafields.seo.description | default: collection.description | strip_html | truncatewords: 25 }}{%- else -%}{{ page_description | default: shop.description }}{%- endif -%}" />
```

Metafields setup:
- `shop.metafields.seo.home_title` (single line text)
- `shop.metafields.seo.home_description` (multi line text)
- Por producto y colección: `seo.title` y `seo.description`

---

## llms.txt en raíz

Crear página Shopify con handle `llms-txt`:

Plain text content:
```
# [Marca]

> [Descripción 1-2 frases qué hace la marca]

## Categorías principales

- [Categoría 1]: https://dominio.cl/collections/categoria-1
- [Categoría 2]: https://dominio.cl/collections/categoria-2

## Productos destacados

- [Producto top 1]: https://dominio.cl/products/producto-1
- [Producto top 2]: https://dominio.cl/products/producto-2

## Recursos informacionales

- Qué son [ingrediente]: https://dominio.cl/blogs/news/que-son
- Guía completa: https://dominio.cl/blogs/news/guia
- FAQ: https://dominio.cl/pages/faq

## Acerca de

- Sobre [Marca]: https://dominio.cl/pages/about
- Contacto: https://dominio.cl/pages/contact

## Optional

- Blog: https://dominio.cl/blogs/news
- Mayorista: https://dominio.cl/pages/mayorista
```

Para que esté accesible en `/llms.txt`, hay dos opciones:
1. Crear la page con handle `llms-txt` y usar redirect 301 desde `/llms.txt` a `/pages/llms-txt`
2. Mejor: usar Shopify Hydrogen o app que sirva archivo plano (más limpio)

---

## Imágenes optimizadas

En PDPs:
```liquid
{% for image in product.images %}
<img
  src="{{ image | image_url: width: 800 }}"
  srcset="{{ image | image_url: width: 400 }} 400w,
          {{ image | image_url: width: 800 }} 800w,
          {{ image | image_url: width: 1200 }} 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="{{ image.alt | default: product.title }}"
  loading="lazy"
  width="800"
  height="800"
/>
{% endfor %}
```

Alt text setup:
- Default: `product.title`
- Mejor: campo `image.alt` editado manualmente con keyword
- Patrón: "[Producto] [variante/sabor/color] [marca] [atributo clave]"

---

## URL canonical

En `layout/theme.liquid`:

```liquid
<link rel="canonical" href="{{ canonical_url }}" />
```

Shopify lo hace bien por default. Solo verificar que no se esté inyectando duplicado por apps.

---

## Hreflang (si aplica)

Para marca con sitio Chile + sitio internacional:

```liquid
<link rel="alternate" hreflang="es-CL" href="https://dominio.cl{{ canonical_path }}" />
<link rel="alternate" hreflang="es" href="https://dominio.com/cl{{ canonical_path }}" />
<link rel="alternate" hreflang="x-default" href="https://dominio.com{{ canonical_path }}" />
```

---

## Checklist post-implementación

- [ ] Validar Schema en https://validator.schema.org/
- [ ] Validar Rich Results en https://search.google.com/test/rich-results
- [ ] Verificar canonical en cada tipo de template
- [ ] Verificar que llms.txt sea accesible
- [ ] Solicitar re-crawl en GSC de páginas modificadas
- [ ] Esperar 1-2 semanas y verificar rich snippets en SERP
- [ ] Monitorear errores en GSC primeros 30 días
