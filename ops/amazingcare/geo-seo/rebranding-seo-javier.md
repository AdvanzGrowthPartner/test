# Rebranding AmazingCare · lo que el tema nuevo no puede perder (SEO/GEO)

Para Javier. Preparado por el GEO/SEO OS el 26-oct-2026. Si se cumple esta lista, el cambio de tema no le quita tráfico orgánico al sitio.

## 1. Tres piezas nuevas que hay que llevar al tema nuevo
Hoy están en el tema sin publicar **"Blog más leídos — Advanz 26-10"** (191099437352), que es una copia exacta del tema en vivo con 3 cambios. Si el rebranding sale antes de publicar esa copia, hay que copiar estos archivos al tema nuevo:

| Archivo | Para qué sirve |
|---|---|
| `sections/main-blog-ac.liquid` + `snippets/bgr-card-ac.liquid` + `templates/blog.json` (sección `main` tipo `main-blog-ac`) | Listado del blog: más leídos primero, filtro por tema, buscador y tiempo de lectura |
| `sections/ac-collection-faq.liquid` + la sección `ac_faq_electrolitos` en `templates/collection.electrolitos.json` | Texto y FAQ de /collections/electrolitos, con schema FAQPage. Hoy es el único texto indexable de esa página |

Los colores van fijos en el CSS de cada archivo: azul `#020c56` y celeste `#00c3f0`. Con la paleta nueva basta cambiar esos valores.

## 2. Lo que vive en el admin y no depende del tema (no tocar)
- Cuerpo de los artículos del blog, con sus bloques de producto (`AC-PRODUCTO-INLINE-*`) y el JSON-LD (Article, FAQPage, Breadcrumb). Están dentro del contenido, así que sobreviven a cualquier tema.
- SEO title y meta description de productos, colecciones y artículos.
- Redirecciones 301 (POTS y Creatina y electrolitos, entre otras).

## 3. Reglas para no perder posiciones
1. **No cambiar URLs ni handles.** Si algún producto, colección o artículo cambia de nombre, hay que crear la redirección 301 el mismo día.
2. **Mantener los templates con sufijo:** `collection.electrolitos`, `collection.packs`, `collection.accesorios`, `product.creatina`, `product.energy`, `product.fibra-prebiotica`, `product.packs`, `product.ficha-producto-accesorios` y `page.*`. Si el tema nuevo no los tiene, esas páginas caen al template genérico.
3. **Artículos:** usan los sufijos `article`, `fibra` y `energy`, pero hoy esos templates no existen y todos caen en `templates/article.json`. Si el tema nuevo crea `article.article.json`, cambia el diseño de casi todo el blog de una vez.
4. **Un H1 por página.** Ojo: /collections/electrolitos hoy no tiene H1 porque el banner de la colección está desactivado. El tema nuevo debería mostrar el título de la colección como H1.
5. **Schema y reseñas:** mantener el JSON-LD de producto con AggregateRating (Judge.me) y los snippets `booster-seo` / `avada-seo` mientras esas apps sigan instaladas. Antes de borrar una app de SEO, avisar.
6. **Apps que escriben en el tema:** GemPages (`gp-*`), EComposer (`ecom-*`), PageFly y BEAE. Sus secciones y templates hay que migrarlos o regenerarlos desde cada app. Si no, las landings armadas con ellas quedan en blanco.
7. **Velocidad:** no sumar scripts pesados. Core Web Vitals influye en el ranking.

## 4. Revisión antes y después de publicar
- [ ] Vista previa del tema nuevo en: home, una ficha de producto, /collections/electrolitos, /blogs/noticias y 2 artículos (Disautonomía y Magnesio).
- [ ] Con la vista previa, revisar en el código fuente que estén `<title>`, la meta description, el canonical, un solo H1 y los scripts `application/ld+json`.
- [ ] Publicar en un horario de bajo tráfico y guardar el ID del tema anterior para volver atrás en 1 clic.
- [ ] A las 48 h, revisar en Search Console la cobertura y las páginas con error, y avisar al GEO/SEO OS para comparar clics.
