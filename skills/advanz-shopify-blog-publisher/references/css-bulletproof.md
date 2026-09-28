# CSS Bulletproof para Blogs de Shopify

Este CSS está probado en producción (Amazing Care, mayo 2026) y resuelve los problemas reales que los temas de Shopify causan en blogs:

- Tipografía que se ve más chica que el cuerpo (problema más común)
- Espacios colapsados entre H2 / listas / párrafos
- Imágenes que no se centran en responsive
- `<strong>` que el tema infla a tamaño gigante
- CTAs que se estiran feo cuando se centran

## Cómo usar este CSS

Pegar al inicio del HTML del artículo en el editor de Shopify (modo `<>`). El cliente NO necesita tocar el tema/liquid — todo va dentro del artículo.

## Variables de color por cliente

Antes de usar, **reemplazar los colores celeste de Amazing Care por la paleta real del cliente actual**. Buscar y reemplazar:

| Color Amazing Care | Significado | Reemplazar por |
|---|---|---|
| `#0CB7F2` | Color de marca principal (celeste vibrante) | Color de marca del cliente |
| `#E6F7FD` | Fondo suave de cajas destacadas (celeste muy suave) | Tinte muy suave del color de marca |
| `#0C5A7A` | Texto fuerte dentro de cajas (azul oscuro) | Tono oscuro del color de marca |
| `#0995C5` | Hover del botón (celeste más oscuro) | 20% más oscuro que el color principal |
| `#B8E7F5` | Borde sutil del CTA | Tinte medio del color de marca |
| `#FFA000` y `#FFF8E1` y `#5C4500` | Disclaimer médico (ámbar) | NO cambiar — el ámbar es estándar de warnings |

## CSS completo

```html
<style>
/* ===== INTRO LEDE (la respuesta directa del primer párrafo) ===== */
.intro-lede {
  font-size: 1.15em !important;
  font-weight: 400 !important;
  line-height: 1.6 !important;
  background: #E6F7FD !important;
  border-left: 4px solid #0CB7F2 !important;
  padding: 22px 26px !important;
  border-radius: 8px !important;
  margin: 1rem 0 2.5rem 0 !important;
  color: #1F2937 !important;
}
.intro-lede strong {
  font-weight: 600 !important;
  color: #0C5A7A !important;
}

/* ===== LEDE ANSWER (respuesta directa después de cada H2) ===== */
.lede-answer {
  font-size: 1.1em !important;
  font-weight: 400 !important;
  line-height: 1.6 !important;
  background: #E6F7FD !important;
  border-left: 3px solid #0CB7F2 !important;
  padding: 20px 24px !important;
  border-radius: 6px !important;
  margin: 1.5rem 0 2rem 0 !important;
  color: #1F2937 !important;
}
.lede-answer strong {
  font-weight: 600 !important;
  color: #0C5A7A !important;
}

/* ===== ESPACIADO DE H2 Y LISTAS ===== */
.article-content h2,
.rte h2,
article h2 {
  margin-top: 3rem !important;
  margin-bottom: 1.25rem !important;
}
.article-content ul,
.article-content ol,
.rte ul,
.rte ol,
article ul,
article ol {
  margin-top: 1rem !important;
  margin-bottom: 1.75rem !important;
  padding-left: 1.75rem !important;
}
.article-content li,
.rte li,
article li {
  margin-bottom: 0.6rem !important;
  line-height: 1.6 !important;
}

/* ===== IMÁGENES CENTRADAS RESPONSIVE ===== */
.article-image-center {
  text-align: center !important;
  margin: 2.5rem auto !important;
}
.article-image-center img {
  display: block !important;
  margin: 0 auto !important;
  max-width: 100% !important;
  height: auto !important;
  border-radius: 8px !important;
}

/* ===== TABLA DE CONTENIDOS (TOC) ===== */
.toc {
  background: #FAFAFA;
  padding: 22px 30px;
  border-radius: 12px;
  margin: 2rem 0 3rem 0;
  border-left: 3px solid #0CB7F2;
}
.toc h3 {
  margin-top: 0 !important;
  margin-bottom: 1rem !important;
  font-size: 1.1em;
  color: #1F2937;
}
.toc ul {
  list-style: none !important;
  padding-left: 0 !important;
  margin: 0 !important;
}
.toc li {
  padding: 0.6rem 0 !important;
  border-bottom: 1px solid #E5E5E5;
  margin-bottom: 0 !important;
}
.toc li:last-child { border-bottom: none; }
.toc a {
  color: #0C5A7A;
  text-decoration: none;
}
.toc a:hover { color: #0CB7F2; }

/* ===== CTA DE PRODUCTO (alineado izquierda, NO centrado) ===== */
.cta-product {
  background: linear-gradient(135deg, #E6F7FD 0%, #F0FCFE 100%);
  padding: 2rem 2.5rem;
  border-radius: 16px;
  text-align: left;
  margin: 3rem 0;
  border: 1px solid #B8E7F5;
}
.cta-product h3 {
  margin-top: 0 !important;
  margin-bottom: 0.75rem !important;
  color: #0C5A7A;
}
.cta-product p {
  font-size: 1em !important;
  line-height: 1.6 !important;
  margin-bottom: 1.25rem !important;
}
.btn-primary {
  display: inline-block;
  padding: 0.85rem 1.75rem;
  background: #0CB7F2;
  color: white !important;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95em;
  transition: background 0.2s;
}
.btn-primary:hover { background: #0995C5; }

/* ===== AUTHOR BOX (el profesional clínico) ===== */
.author-box {
  display: flex;
  gap: 1.5rem;
  padding: 1.75rem 2rem;
  background: #E6F7FD;
  border-radius: 12px;
  margin: 2.5rem 0;
  align-items: flex-start;
  border-left: 4px solid #0CB7F2;
}
.author-box .author-info {
  flex: 1;
}
.author-box h4 {
  margin: 0 0 0.35rem 0 !important;
  font-size: 1.15em;
  color: #0C5A7A;
}
.author-box .role {
  margin: 0 0 0.85rem 0 !important;
  font-style: italic;
  color: #4B5563;
  font-size: 0.95em;
}
.author-box p {
  margin: 0.4rem 0 !important;
  font-size: 0.95em;
  line-height: 1.55;
}

/* ===== DISCLAIMER MÉDICO YMYL (ámbar, separado del author) ===== */
.medical-disclaimer {
  background: #FFF8E1;
  border-left: 4px solid #FFA000;
  padding: 1.25rem 1.5rem;
  border-radius: 8px;
  font-size: 0.9em;
  margin: 2rem 0;
  color: #5C4500;
}
.medical-disclaimer strong { color: #5C4500; }
.medical-disclaimer p {
  margin: 0 !important;
  font-size: 0.9em !important;
}

/* ===== BIBLIOGRAFÍA / REFERENCIAS CIENTÍFICAS ===== */
.references {
  background: #FAFAFA;
  padding: 1.75rem 2rem;
  border-radius: 12px;
  margin: 2.5rem 0;
  font-size: 0.95em;
}
.references h3 {
  margin-top: 0 !important;
  margin-bottom: 1rem !important;
  color: #1F2937;
}
.references ol {
  padding-left: 1.5rem !important;
}
.references li {
  margin-bottom: 0.6rem !important;
  line-height: 1.55;
}

/* ===== RESPONSIVE MOBILE ===== */
@media (max-width: 768px) {
  .author-box {
    flex-direction: column;
  }
  .intro-lede, .lede-answer {
    padding: 16px 18px !important;
  }
  .cta-product {
    padding: 1.5rem;
    text-align: center;
  }
}
</style>
```

## Por qué cada decisión

### `font-size: 1.15em` (no 1rem, no 18px)

`em` es relativo al contenedor padre. Si el tema usa cuerpo en 22px, `1.15em` = 25.3px. Si el tema usa 16px, `1.15em` = 18.4px. **Escala con el tema en lugar de pelearse con él.** Esto resuelve el problema número 1 reportado por clientes: "el destacado se ve más chico que el cuerpo".

### `!important` en todo lo crítico

Los temas de Shopify (especialmente Dawn y forks comerciales) tienen reglas CSS muy agresivas para `<strong>`, `h2`, `ul`, etc. Sin `!important`, el CSS del tema gana siempre. Usar `!important` en propiedades estructurales (margin, padding, font-size) es la única forma de garantizar consistencia visual.

### `border-left` en lugar de `border` completo

Las cajas con borde lateral (`border-left: 4px solid`) son la convención visual moderna para "callout" o "respuesta destacada". Da estructura sin sobrecargar visualmente. Probado en Amazing Care, Stripe docs, GitHub docs, Notion.

### CTA con `text-align: left`

Cuando se centra un CTA con texto largo en un tema con cuerpo grande, las líneas se estiran de manera fea y el botón queda perdido. `text-align: left` mantiene la legibilidad y deja el botón con visualmente integrado.

### Author box con `display: flex`

Permite agregar foto del profesional en el futuro sin reescribir el HTML. En mobile colapsa a `flex-direction: column` automáticamente.

### Disclaimer médico en ámbar

`#FFA000` es el código universal de "warning / atención" en design systems. No usar el color de marca para el disclaimer — se confunde visualmente con las cajas destacadas y el cliente termina ignorándolo.

## Errores comunes al adaptar este CSS

| Error | Síntoma | Solución |
|---|---|---|
| Cambiar `em` por `rem` | Destacados se ven más chicos que el cuerpo | Volver a `em` |
| Olvidar `!important` | El CSS del tema sobrescribe los estilos | Agregar `!important` en propiedades críticas |
| Quitar las clases compuestas (`.article-content h2`) | El espaciado de H2 no aplica | Mantener las 3 variantes (`.article-content h2, .rte h2, article h2`) porque distintos temas usan distintos wrappers |
| Centrar el CTA | Se ve estirado y feo | `text-align: left` |
| Usar el color de marca para el disclaimer médico | El cliente lo confunde con otra caja de marca | Mantener ámbar (`#FFA000`) |
| Usar imágenes con `margin-left: 43px` (el default del editor) | No centra en responsive | Envolver en `<div class="article-image-center">` |
