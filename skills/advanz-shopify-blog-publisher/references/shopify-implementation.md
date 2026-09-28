# Implementación en Shopify — Pasos Operativos

Cómo entregar el blog al cliente para que lo pegue en Shopify sin errores.

## Pre-requisitos

Antes de pegar nada en Shopify, el cliente necesita:

- Acceso a la tienda Shopify (admin.shopify.com).
- Permiso de edición de blogs (rol Owner o Staff con permisos de Online Store).
- Las imágenes ya renombradas y listas para subir.

## Paso a paso para un blog NUEVO

### 1. Renombrar imágenes (antes de subir nada)

Renombrar todas las imágenes a kebab-case descriptivo:
- ✅ `electrolitos-bariatrica-amazing-care.jpg`
- ❌ `IMG_4582.jpg`
- ❌ `imagen final v2.PNG`

Comprimir si pesan más de 200KB usando https://tinypng.com.

### 2. Crear el artículo

En Shopify Admin:
1. **Online Store → Blog Posts → Add blog post**
2. Pegar el **Title** (del cliente o del template SEO-fields)
3. En **Edit website SEO**:
   - Pegar el **Meta title** (50-60 chars)
   - Pegar el **Meta description** (140-160 chars)
   - **Verificar el handle** — Shopify auto-genera uno desde el title, pero hay que ajustarlo al SEO-friendly (sin palabras vacías).
4. Pegar el **Excerpt** en el campo correspondiente
5. **Cambiar el Author** al profesional clínico (no a la agencia ni la marca)
6. Subir la **Featured image** y completar su **Alt text**

### 3. Pegar el HTML del cuerpo

1. En el editor de contenido, hacer clic en el ícono `<>` (modo HTML / Source code)
2. Pegar **todo el HTML** del template completo (CSS al inicio + cuerpo + schema al final)
3. **NO salir todavía del modo HTML** — mientras se está en HTML, subir las imágenes inline:
   - Reemplazar los `src="..."` placeholders con las URLs reales del CDN de Shopify
   - O salir del modo HTML, posicionar el cursor donde va cada imagen, subirla, y eso genera el `<img>` automáticamente

### 4. Verificar previsualización

1. Visibility = **Hidden** (guardar como borrador primero)
2. Clic en **Preview** → revisar:
   - ¿Las cajas destacadas se ven con el color de marca correcto?
   - ¿Los H2 tienen suficiente espacio antes y después?
   - ¿Las imágenes están centradas?
   - ¿El CTA se ve bien (no estirado)?
   - ¿El author box se ve diferenciado?

### 5. Validar schema

1. Abrir https://search.google.com/test/rich-results
2. Pegar la URL del preview (que Shopify genera)
3. Verificar:
   - Detección de Article schema ✅
   - Detección de FAQPage schema ✅
   - Sin errores ni warnings

### 6. Publicar

1. Visibility = **Visible**
2. Save → confirmar

### 7. Request indexing

1. Abrir Google Search Console
2. Inspeccionar URL → pegar la URL del artículo publicado
3. Clic en **Request indexing**
4. Esperar 1-3 días para que Google lo procese

### 8. Distribuir

- Email a base: incluir el blog en el siguiente newsletter
- IG / TikTok story: screenshot del article con link
- Grupos de Facebook / WhatsApp: link directo

## Paso a paso para CORREGIR un blog ya publicado

### Caso A: Solo cambia el contenido (mismo topic, mismo URL)

1. Abrir el artículo existente en Shopify
2. Entrar al modo HTML
3. Reemplazar todo el contenido por el HTML nuevo
4. Save
5. **No** se necesita redirect

### Caso B: Cambia el topic / título / handle (caso bariátrico vs lipedema)

**CRÍTICO:** este es el caso más delicado porque cambiar el handle puede romper SEO acumulado y generar 404s.

1. Abrir el artículo existente
2. Cambiar el **Title** al nuevo
3. Cambiar el **Handle** al nuevo
4. **Shopify mostrará un popup**: *"¿Crear un redirect de la URL anterior?"*
5. **SIEMPRE aceptar el redirect** — esto crea un redirect 301 que:
   - Manda el tráfico viejo a la URL nueva sin pérdida
   - Pasa el SEO acumulado a la URL nueva
   - Evita 404s para links externos
6. Actualizar **Meta title** y **Meta description**
7. Actualizar **Excerpt**
8. Actualizar **Tags**
9. Si la featured image ya no es relevante, reemplazarla (y actualizar su alt text)
10. Modo HTML → reemplazar todo el contenido
11. Actualizar el `dateModified` del Schema Article
12. Save
13. Verificar el redirect: abrir la URL vieja en incógnito → debe redirigir a la nueva
14. Request indexing de la URL nueva en Google Search Console
15. Opcional: pedir desindexación de la URL vieja (Search Console → Removals)

### Caso C: Solo cambia CSS / formato (corrección visual)

1. Modo HTML
2. Reemplazar **solo el bloque `<style>...</style>`** al inicio del HTML
3. Save
4. Preview → confirmar visualmente
5. **No** se necesita redirect ni re-indexing

## Errores comunes en la implementación

### Error 1: El cliente pega el HTML pero las cajas destacadas no aparecen
**Causa:** el editor de Shopify a veces strippa el `<style>` cuando entra y sale del modo HTML.
**Solución:** pegar siempre con el modo HTML activo. Después de pegar, **no salir y volver a entrar** al modo HTML — eso suele strippar elementos.

### Error 2: Las imágenes pierden los `<div class="article-image-center">` wrapper
**Causa:** el editor de Shopify tiene un parser que reemplaza el wrapper por su propio HTML cuando se sube una imagen por el botón de "Insert image".
**Solución:** subir las imágenes **primero al CDN de Shopify** (Settings → Files), y luego pegar el HTML con el `src` ya apuntando al CDN. Esto evita que el editor reemplace el HTML.

### Error 3: El schema desaparece después de guardar
**Causa:** algunos temas de Shopify tienen sanitizadores HTML que eliminan `<script>` tags por seguridad.
**Solución:** verificar después de guardar que los `<script>` siguen ahí. Si no, hay dos opciones:
- Pedir al dev que agregue una excepción para JSON-LD
- Usar la app "JSON-LD for SEO" de Shopify (gratuita) que inyecta schema vía liquid

### Error 4: El cliente cambió el author pero el schema sigue diciendo otra cosa
**Causa:** el campo Author de Shopify y el `author.name` del schema JSON-LD son independientes.
**Solución:** actualizar AMBOS — el campo Author en la UI y el `name` dentro del `<script>` del Article schema.

### Error 5: El handle quedó con tildes o ñ
**Causa:** Shopify auto-genera el handle del title y a veces deja tildes.
**Solución:** editar manualmente el handle, sin tildes ni ñ. Ejemplo: `cirugia-bariatrica` (no `cirugía-bariátrica`).

## Checklist final pre-publicación

Antes de marcar como Visible, validar:

- [ ] Title pegado y correcto
- [ ] Handle SEO-friendly (sin palabras vacías, sin tildes)
- [ ] Meta title 50-60 caracteres
- [ ] Meta description 140-160 caracteres
- [ ] Excerpt ≤200 caracteres
- [ ] Author = profesional clínico (no agencia ni marca)
- [ ] Featured image renombrada y con alt text
- [ ] Tags 8-12 separados por coma
- [ ] CSS bulletproof al inicio del HTML
- [ ] Pattern dual SEO+GEO en cada H2 (lede-answer presente)
- [ ] Imágenes inline en `<div class="article-image-center">` con alt text
- [ ] Internal link a colección relevante presente
- [ ] Author box con bio del profesional
- [ ] Disclaimer médico (si es YMYL)
- [ ] Bibliografía con referencias científicas
- [ ] Schema Article con `author.knowsAbout`
- [ ] Schema FAQPage con una entry por H2
- [ ] Schema validado en validator.schema.org
- [ ] Schema validado en search.google.com/test/rich-results
- [ ] Preview visual revisado en desktop y mobile
- [ ] Request indexing en Google Search Console (después de publicar)

## Entregable para el cliente

Cuando se le pasa al cliente, entregar:

1. **HTML completo** en un bloque de código copiable
2. **Tabla de campos SEO** con los valores exactos a copiar
3. **Checklist numerada** con los pasos arriba
4. **Link a Search Console** para hacer el request indexing
5. **Estimación de tiempo:** la implementación toma ~20 minutos

Si el cliente no es técnico, ofrecer hacer la implementación en su tienda directamente (con acceso staff).
