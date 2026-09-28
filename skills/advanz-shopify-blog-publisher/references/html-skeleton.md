# HTML Skeleton — Pattern Dual SEO+GEO

Pattern probado para que un blog rankee en Google **y** sea citado por LLMs (ChatGPT, Claude, Perplexity, Gemini).

## La estructura por cada H2

```
H2 = pregunta literal que la gente busca
  ↓
Respuesta directa en negrita (1-2 frases autocontenidas)
  ↓
Expansión en párrafo normal (contexto adicional)
  ↓
Lista o tabla (escaneable)
  ↓
Cierre opcional (caso específico, advertencia, etc.)
```

## Por qué este pattern funciona

### Para Google
- **H2 con pregunta literal** matchea queries de "People Also Ask" y búsquedas long-tail.
- **Respuesta directa en negrita** es lo que Google extrae como featured snippet.
- **Listas y tablas** mejoran tiempo en página y reducen bounce rate.

### Para LLMs (GEO)
- **Respuesta autocontenida en 1-2 frases** es lo que los LLMs citan textualmente. Si la respuesta requiere contexto previo, el LLM no la usa.
- **Estructura predecible** facilita que el LLM extraiga información sin alucinaciones.
- **Schema FAQPage embebido** (ver `schema-templates.md`) le dice al LLM "esta es una respuesta directa a esta pregunta".

## Ejemplo concreto del pattern

### ❌ Sin pattern dual

```html
<h2>El sodio</h2>
<p>El sodio suele tener mala fama porque se asocia con la retención de líquidos. 
Pero en algunas personas con disautonomía es importante no restringirlo demasiado 
porque puede empeorar síntomas como mareos y fatiga.</p>
```

Problemas: H2 no es una query buscable. No hay respuesta extraible para snippet. El LLM no puede citar autocontenidamente.

### ✅ Con pattern dual

```html
<h2 id="sodio">¿Es necesario evitar el sodio si se tiene lipedema?</h2>

<p class="lede-answer"><strong>No necesariamente. Si bien una restricción moderada 
de sodio puede ayudar a algunas mujeres con retención de líquidos, restringirlo 
en exceso puede empeorar síntomas como mareos, fatiga y presión baja, 
especialmente en pacientes con lipedema que también presentan disautonomía.</strong></p>

<p>El sodio tiene mala fama porque se asocia rápidamente con edema y retención. 
Pero el cuerpo necesita sodio para mantener el volumen sanguíneo, una presión 
arterial estable y la capacidad de hidratar las células. La pregunta no es 
"¿hay que evitarlo?", sino "¿cuánto se necesita según cada caso?".</p>

<p>En algunas mujeres con lipedema que también presentan:</p>

<ul>
  <li>Presión arterial baja.</li>
  <li>Mareos al levantarse o cambios posturales.</li>
  <li>Fatiga persistente.</li>
  <li>Síntomas compatibles con disautonomía (POTS u otros).</li>
</ul>

<p>...una restricción excesiva de sodio puede <strong>empeorar los síntomas</strong> 
en lugar de mejorarlos. Por eso conviene personalizar este punto con un profesional.</p>
```

Por qué este funciona:
- `id="sodio"` permite linkear desde el TOC y desde otros artículos.
- H2 es pregunta literal que la gente busca.
- `lede-answer` es 100% autocontenida — un LLM puede citarla sin contexto previo.
- Expansión da profundidad sin repetir.
- Lista hace el contenido escaneable.

## Reglas de longitud para la respuesta directa

La `<p class="lede-answer">` debe ser:
- **Mínimo 25 palabras**: si es muy corta, no es suficientemente descriptiva para ser snippet.
- **Máximo 60 palabras**: si es muy larga, Google la corta a la mitad en el snippet.
- **Ideal: 35-50 palabras**.
- Una o dos oraciones, no más.
- Autocontenida: el lector no debe necesitar contexto previo.
- Sin pronombres ambiguos ("esto", "eso", "estos") sin antecedente claro.

## Estructura completa del HTML de un blog

```html
<style>
/* CSS bulletproof — ver references/css-bulletproof.md */
</style>

<!-- 1. INTRO LEDE: respuesta directa al título del artículo -->
<p class="intro-lede"><strong>[Respuesta directa al título, 35-50 palabras]</strong></p>

<!-- 2. Párrafo de contexto que NO es lede -->
<p>[Contexto narrativo del problema, 2-3 oraciones]</p>

<!-- 3. Imagen principal del artículo -->
<div class="article-image-center">
  <img src="..." alt="[Alt descriptivo con keyword]" width="..." height="...">
</div>

<!-- 4. Párrafo de transición + presentación del profesional -->
<p>En este artículo, [Nombre del profesional] —[rol clínico]— explica [tópicos a cubrir].</p>

<hr>

<!-- 5. TABLA DE CONTENIDOS -->
<div class="toc">
  <h3>Lo que vas a encontrar en este artículo</h3>
  <ul>
    <li><a href="#h2-1-id">[Pregunta del H2 1]</a></li>
    <li><a href="#h2-2-id">[Pregunta del H2 2]</a></li>
    <!-- ... -->
  </ul>
</div>

<hr>

<!-- 6. SECCIÓN CON PATTERN DUAL (repetir por cada H2) -->
<h2 id="h2-1-id">[Pregunta literal]</h2>

<p class="lede-answer"><strong>[Respuesta directa autocontenida 35-50 palabras]</strong></p>

<p>[Expansión: contexto que respalda la respuesta]</p>

<p>[Lista de items si aplica:]</p>
<ul>
  <li><strong>[Item]</strong>: [explicación].</li>
</ul>

<p>[Cierre opcional con matiz o advertencia.]</p>

<hr>

<!-- ... repetir bloque H2 por cada sección ... -->

<!-- 7. CTA DE PRODUCTO -->
<div class="cta-product">
  <h3>[Hook contextual al artículo]</h3>
  <p>[Descripción del producto con internal link a la colección]</p>
  <p><a href="/collections/[slug]" class="btn-primary">Ver [producto] →</a></p>
</div>

<!-- 8. AUTHOR BOX -->
<div class="author-box">
  <div class="author-info">
    <h4>[Nombre del profesional]</h4>
    <p class="role">[Rol clínico con credenciales]</p>
    <p>[Bio breve de 2-3 oraciones con experiencia clínica relevante]</p>
  </div>
</div>

<!-- 9. DISCLAIMER MÉDICO (solo si es YMYL) -->
<div class="medical-disclaimer">
  <p><strong>Aviso importante:</strong> este artículo tiene fines educativos y no 
  reemplaza el seguimiento con tu equipo médico. Sigue siempre las indicaciones 
  de tu profesional tratante. Los suplementos no son medicamentos y no están 
  diseñados para diagnosticar, tratar o curar ninguna enfermedad.</p>
</div>

<!-- 10. BIBLIOGRAFÍA / REFERENCIAS CIENTÍFICAS -->
<div class="references">
  <h3>Referencias científicas</h3>
  <ol>
    <li>[Autor]. <em>[Título del paper]</em>. [Journal]. [Año].</li>
    <!-- ... -->
  </ol>
</div>

<!-- 11. SCHEMA JSON-LD: Article + FAQPage (ver schema-templates.md) -->
<script type="application/ld+json">...</script>
<script type="application/ld+json">...</script>
```

## Reglas de IDs de H2

Cada H2 debe tener un `id` único y descriptivo en kebab-case. Esto permite:
- Linkear desde el TOC
- Linkear desde otros artículos del cluster
- Linkear desde redes sociales con anchor (`/blog/articulo#sodio`)

Convención:
- `id="que-es-X"` para definiciones
- `id="sintomas-X"` para listas de síntomas
- `id="cuando-consultar"` para llamada a la acción profesional
- `id="X-vs-Y"` para comparaciones

## Internal linking

Cada blog debe tener al menos:
- **1 link a la colección de producto relevante** (en CTA o naturalmente en el cuerpo)
- **1-2 links a otros artículos del cluster** (cuando existan)
- **0 links externos a competidores** (obvio pero a veces se cuela)

Los internal links deben ser **contextuales**, no forzados. Ejemplo:

```html
<!-- ✅ Bueno: enlace natural en el cuerpo -->
<p>Si estás en proceso post-bariátrico y buscas una opción de hidratación 
práctica, puedes conocer los <a href="/collections/electrolitos"><strong>electrolitos 
en polvo sin azúcar de Amazing Care</strong></a>: fórmula con 6 iones esenciales.</p>

<!-- ❌ Malo: enlace al medio de un párrafo sin contexto -->
<p>El sodio es importante. <a href="/collections/electrolitos">Compra aquí</a>. 
También el potasio importa.</p>
```
