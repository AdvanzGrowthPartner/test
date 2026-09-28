# JSON-LD Snippets — Listos para Copiar

Snippets listos para copiar y pegar, con placeholders marcados con `{{...}}`.

---

## Organization (para home)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{{Nombre Comercial}}",
  "legalName": "{{Razón Social}}",
  "url": "https://{{dominio.cl}}",
  "logo": "https://{{dominio.cl}}/logo.png",
  "foundingDate": "{{YYYY-MM-DD}}",
  "founder": {
    "@type": "Person",
    "name": "{{Nombre Fundador}}"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{Calle 1234}}",
    "addressLocality": "Santiago",
    "addressRegion": "Región Metropolitana",
    "postalCode": "{{XXXXXXX}}",
    "addressCountry": "CL"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+56-{{XXXXXXXXX}}",
    "contactType": "Customer Service",
    "areaServed": "CL",
    "availableLanguage": ["Spanish"]
  },
  "sameAs": [
    "https://www.instagram.com/{{handle}}",
    "https://www.tiktok.com/@{{handle}}",
    "https://www.facebook.com/{{handle}}",
    "https://www.mercadolibre.cl/perfil/{{handle}}",
    "https://www.wikidata.org/wiki/{{QXXXXXXX}}"
  ]
}
```

---

## Product con AggregateRating

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{Nombre del producto}}",
  "description": "{{Descripción 150-300 caracteres}}",
  "image": [
    "https://{{dominio.cl}}/cdn/shop/files/img1.jpg",
    "https://{{dominio.cl}}/cdn/shop/files/img2.jpg"
  ],
  "sku": "{{SKU}}",
  "mpn": "{{barcode}}",
  "brand": {
    "@type": "Brand",
    "name": "{{Marca}}"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://{{dominio.cl}}/products/{{handle}}",
    "priceCurrency": "CLP",
    "price": "{{precio sin separadores}}",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "{{Marca}}"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "151",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

---

## FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{Pregunta literal del usuario 1}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{Respuesta directa 40-80 palabras}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{Pregunta literal del usuario 2}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{Respuesta directa 40-80 palabras}}"
      }
    }
  ]
}
```

---

## Article con author y reviewedBy

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{Título del artículo}}",
  "image": "https://{{dominio.cl}}/cdn/shop/articles/img.jpg",
  "datePublished": "{{YYYY-MM-DD}}",
  "dateModified": "{{YYYY-MM-DD}}",
  "author": {
    "@type": "Person",
    "name": "{{Nombre Author}}",
    "url": "https://{{dominio.cl}}/pages/team/{{handle}}",
    "jobTitle": "{{Nutricionista / Médico / etc}}",
    "sameAs": [
      "https://www.linkedin.com/in/{{handle}}"
    ]
  },
  "reviewedBy": {
    "@type": "Person",
    "name": "{{Dr. Reviewer}}",
    "jobTitle": "{{Cargo del reviewer}}",
    "url": "https://{{dominio.cl}}/pages/team/{{handle-reviewer}}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{{Marca}}",
    "logo": {
      "@type": "ImageObject",
      "url": "https://{{dominio.cl}}/logo.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://{{dominio.cl}}/blogs/news/{{handle}}"
  }
}
```

---

## BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://{{dominio.cl}}"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{Categoría}}",
      "item": "https://{{dominio.cl}}/collections/{{categoria}}"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "{{Producto}}",
      "item": "https://{{dominio.cl}}/products/{{producto}}"
    }
  ]
}
```

---

## HowTo (para procesos paso a paso)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "{{Cómo [hacer X]}}",
  "description": "{{Descripción del proceso}}",
  "totalTime": "PT5M",
  "supply": [
    { "@type": "HowToSupply", "name": "{{Producto necesario 1}}" }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "{{Nombre paso 1}}",
      "text": "{{Descripción paso 1}}"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "{{Nombre paso 2}}",
      "text": "{{Descripción paso 2}}"
    }
  ]
}
```

---

## Person (para authors y reviewers)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{{Nombre completo}}",
  "jobTitle": "{{Cargo profesional}}",
  "image": "https://{{dominio.cl}}/cdn/team/foto.jpg",
  "description": "{{Bio 2-3 líneas}}",
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "{{Universidad}}"
  },
  "knowsAbout": [
    "{{Tema 1}}",
    "{{Tema 2}}"
  ],
  "sameAs": [
    "https://www.linkedin.com/in/{{handle}}",
    "https://www.instagram.com/{{handle}}"
  ]
}
```

---

## WebSite con SearchAction

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "{{Marca}}",
  "url": "https://{{dominio.cl}}",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://{{dominio.cl}}/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

---

## Reglas de validación

Antes de publicar cualquier schema:

1. Validar en https://validator.schema.org/
2. Validar en https://search.google.com/test/rich-results
3. Verificar que NO se dupliquen schemas (un Product schema solo, no dos)
4. Verificar que TODOS los campos requeridos estén poblados
5. URL absolutas, no relativas
6. Fechas en ISO 8601 (YYYY-MM-DD)
7. Precios sin separadores de miles ni símbolo de moneda

---

## Errores comunes

- Schema duplicado (app + theme inyectan ambos Product)
- Precio con separador ($23.990 en vez de 23990)
- Fecha mal formateada
- Image URL relativa en vez de absoluta
- AggregateRating con reviewCount 0 (Google lo rechaza)
- FAQPage con respuestas que no responden la pregunta
- Article sin author (Google lo rechaza para news)
