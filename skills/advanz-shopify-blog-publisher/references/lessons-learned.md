# Lessons Learned — Errores Reales y Sus Correcciones

Este documento captura los errores específicos cometidos durante la implementación de blogs de Amazing Care (mayo 2026) y sus correcciones. **Leer esto antes de iterar sobre cualquier blog** para evitar repetir las mismas equivocaciones.

## Error 1: Color de marca equivocado (violeta vs celeste)

### Lo que pasó
Usé violeta `#C15DFF` como color de las cajas destacadas asumiendo que era un color "premium genérico". El cliente Amazing Care tiene paleta celeste, no violeta. El cliente reaccionó: *"no, ese style no es del color del cliente, el color del cliente es celeste"*.

### Por qué pasó
- No verifiqué la paleta real del cliente antes de aplicar CSS.
- Asumí que un color "neutral/premium" iba a funcionar.
- No hice fetch al sitio del cliente para validar.

### Cómo evitarlo
**Antes de aplicar CSS de marca, SIEMPRE:**
1. Preguntar al usuario por la paleta de marca (si no la tiene a mano).
2. Si no la tiene, hacer `web_fetch` o `web_search` del sitio del cliente.
3. Si el sitio no es accesible (403, login), pedir el manual de marca.
4. **Nunca asumir** colores "neutrales" o "premium" — la marca tiene paleta definida.

### Paleta correcta usada después
- Color principal: `#0CB7F2` (celeste vibrante de marca)
- Fondo suave: `#E6F7FD` (celeste muy suave)
- Texto fuerte: `#0C5A7A` (azul oscuro de marca)

## Error 2: Tipografía absoluta (rem) vs relativa (em)

### Lo que pasó
Forcé `font-size: 1rem !important` en las cajas destacadas. El tema de Amazing Care usa cuerpo en ~22-24px. Resultado visual: **los destacados se veían MÁS CHICOS que el cuerpo del artículo**, ilegibles. El cliente reaccionó: *"mira la diferencia de textos... el tamaño cambia mucho es ilegible"*.

### Por qué pasó
- Asumí que `1rem = 16px` era estándar y suficiente.
- No consideré que los temas DTC modernos usan tipografía agresivamente grande (cuerpo en 22-24px) para legibilidad.
- Forcé el tamaño en lugar de dejarlo escalar.

### Cómo evitarlo
**Para tipografía en CSS de Shopify, usar SIEMPRE `em` (relativo al padre):**

| Unidad | Cuándo usar | Por qué |
|---|---|---|
| `em` | ✅ **Default para tipografía** | Escala con el tema. `1.1em` siempre será 10% más grande que el contenedor. |
| `rem` | ❌ Evitar en blogs Shopify | Te clava al root (16px típicamente), pelea con el tema. |
| `px` | ❌ Evitar | Absoluto, peor todavía. |
| `%` | Solo para anchos | No para tipografía. |

### Regla numérica probada
- Cuerpo del artículo: 1em (el del tema)
- Lede answer: **1.1em** (10% más grande)
- Intro lede: **1.15em** (15% más grande)
- Disclaimer médico: **0.9em** (10% más chico)
- Bibliografía: **0.95em** (5% más chico)

## Error 3: Espacios colapsados entre H2 y bullets

### Lo que pasó
El cliente mostró screenshot donde el H2 estaba pegado al primer bullet de la lista, sin espacio. Los párrafos también se pegaban al H2 siguiente. El cliente reaccionó: *"siguen viéndose cosas colapsadas ejemplo baja los títulos, antes de los bullets"*.

### Por qué pasó
- El tema de Shopify no aplicaba margins consistentes a `h2` cuando se generaba desde el editor.
- No tenía CSS que forzara separación.

### Cómo evitarlo
Incluir SIEMPRE en el CSS bulletproof:

```css
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
}
```

**Por qué las 3 variantes de selector** (`.article-content`, `.rte`, `article`): distintos temas de Shopify usan distintos wrappers para el contenido del artículo. Cubrir las 3 garantiza que el CSS aplique en cualquier tema.

## Error 4: Imágenes que no se centran

### Lo que pasó
El cliente: *"las imágenes no están centradas"*. Al inspeccionar, las imágenes tenían el style del editor de Shopify:
```html
<img style="margin-right: 43.2315px; margin-bottom: 16px; margin-left: 43.2315px; float: none;" ...>
```

### Por qué pasó
El editor de Shopify, cuando insertas una imagen desde su botón de "Insert image", le aplica `margin-left` y `margin-right` en píxeles específicos calculados para el ancho del editor. Estos píxeles no centran en responsive porque el ancho del contenedor cambia.

### Cómo evitarlo
**Envolver SIEMPRE las imágenes en `<div class="article-image-center">`:**

```html
<div class="article-image-center">
  <img src="..." alt="..." width="..." height="...">
</div>
```

Con el CSS correspondiente:

```css
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
```

Esto garantiza centrado en cualquier ancho de pantalla, sin píxeles hardcodeados.

## Error 5: CTA estirado y feo cuando está centrado

### Lo que pasó
El CTA del producto, con `text-align: center`, se veía estirado y desproporcionado en el tema de Amazing Care (que tiene cuerpo grande).

### Por qué pasó
Cuando el cuerpo del tema es grande (22-24px), un CTA centrado con texto largo estira las líneas y el botón queda perdido en medio de un párrafo gigante.

### Cómo evitarlo
**`text-align: left` por default en CTAs.** Más legible, mejor jerarquía visual.

```css
.cta-product {
  text-align: left;  /* NO center */
}
.cta-product p {
  font-size: 1em !important;  /* Forzar para que no escale con el tema */
  line-height: 1.6 !important;
}
```

El botón sí queda como inline-block, no estirado.

## Error 6: Author box plano que parece párrafo más

### Lo que pasó
La primera versión del author box era solo `<h4>` + `<p>` simple, sin encapsular. El cliente: *"destacar la nutri"*.

### Por qué pasó
Confundí "incluir el author" con "destacar el author". Son cosas distintas.

### Cómo evitarlo
**El author box DEBE ser una caja visualmente diferenciada del cuerpo:**

```html
<div class="author-box">
  <div class="author-info">
    <h4>Paula Camus</h4>
    <p class="role">Nutricionista especialista en Cirugía Bariátrica y Lipedema</p>
    <p>Bio de 2-3 oraciones con experiencia clínica relevante.</p>
  </div>
</div>
```

Con CSS de caja celeste con borde lateral (ver `css-bulletproof.md`).

**Por qué importa:** en YMYL, el author es uno de los factores de E-E-A-T más importantes. Si se ve como un párrafo más, Google no lo detecta visualmente y la confianza del lector tampoco se construye.

## Error 7: Disclaimer del mismo color que el author box

### Lo que pasó
Primera versión: el disclaimer médico estaba dentro del mismo div del author box. El cliente no podía distinguir uno del otro.

### Por qué pasó
Pensé que "todo lo legal/clínico" iba junto.

### Cómo evitarlo
**El disclaimer médico va en una caja SEPARADA y en color ámbar** (warning, no marca):

```css
.medical-disclaimer {
  background: #FFF8E1;        /* amarillo muy suave */
  border-left: 4px solid #FFA000;  /* ámbar de warning */
  color: #5C4500;             /* texto oscuro */
}
```

Razón: el ámbar es el color universal de "warning" en design systems. Un lector escanea el artículo y SABE que esa caja es "información importante de seguridad" porque el color habla por sí solo.

## Error 8: Texto redundante en respuestas directas

### Lo que pasó
Las respuestas directas (`lede-answer`) repetían frases del párrafo de expansión que las seguía. El cliente: *"acotar lo redundante"*.

### Por qué pasó
Estaba siendo demasiado descriptivo en la respuesta directa, agregando contexto que ya se desarrollaba después.

### Cómo evitarlo
**Reglas de longitud:**
- Lede answer: 25-50 palabras, MÁXIMO 60.
- Una o dos oraciones, no más.
- Autocontenida pero NO exhaustiva.
- Si la respuesta tiene "Y además, X también es importante porque...", esa parte va al párrafo de expansión, no en la respuesta directa.

**Ejemplo de reducción:**
- Antes (60 palabras): *"Es importante consultar con tu equipo de cirugía bariátrica —nutricionista, cirujano o médico tratante— cuando aparecen síntomas como mareos persistentes, taquicardia, fatiga intensa, dolores de cabeza frecuentes o cualquier signo que pueda indicar deshidratación o desequilibrio electrolítico."*

- Después (22 palabras): *"Consulta con tu equipo si aparecen mareos persistentes, taquicardia, fatiga intensa, dolores de cabeza frecuentes o cualquier signo de deshidratación o desequilibrio electrolítico."*

## Error 9: Confundir contenido publicado (bariátrico vs lipedema)

### Lo que pasó
El cliente había publicado contenido de **pacientes bariátricos** en la URL `/lipedema-y-electrolitos` con el title de lipedema. Cuando le pasé la "corrección", originalmente le di el contenido de lipedema en lugar de cambiar el title/URL al de bariátrico.

### Por qué pasó
- Asumí que el contenido era el correcto y que el problema era cosmético.
- No leí cuidadosamente el contenido vs el title antes de proponer correcciones.

### Cómo evitarlo
**Cuando se reciba un blog ya publicado para corregir, FIRST:**
1. Leer el contenido completo.
2. Leer el title actual y el handle.
3. **Verificar coincidencia**: ¿el contenido coincide con el title?
4. Si NO coinciden, preguntar al cliente: "¿el title actual es el correcto y hay que ajustar el contenido, o el contenido es el correcto y hay que ajustar title + handle + redirect?"
5. **Nunca asumir** cuál de los dos es el "correcto".

## Error 10: No advertir del redirect 301 al cambiar el handle

### Lo que pasó
En la primera corrección, propuse cambiar el handle sin enfatizar la importancia del redirect 301. Eso podría haber roto SEO acumulado del URL anterior.

### Cómo evitarlo
**SIEMPRE que se cambie un handle, escribir CRÍTICO en mayúsculas:**

> **CRÍTICO:** Cuando cambies la URL en Shopify, **activa el redirect 301 automático** que ofrece Shopify (te lo va a preguntar al guardar). Si no, cualquier persona que ya tenga el link viejo va a caer en 404 y Google también. El redirect 301 manda el tráfico viejo al nuevo URL sin perder el SEO acumulado.

## Error 11: Iterar el CSS sin pedir screenshot

### Lo que pasó
En varias iteraciones del CSS, propuse cambios "a ciegas" sin haber visto cómo se veía el blog en el tema del cliente. Cada iteración requería un nuevo screenshot del cliente para validar.

### Cómo evitarlo
**Antes de iterar CSS, SIEMPRE pedir screenshot.** Frase exacta:

> "Para ajustar el CSS necesito ver cómo se está viendo el blog en tu tema. ¿Me puedes mandar un screenshot de la zona que no se ve bien?"

Es más rápido pedir un screenshot que iterar 3 veces a ciegas.

## Error 12: HTML demasiado largo / cliente no quiere "tener que tocar más cosas"

### Lo que pasó
El cliente dijo explícitamente: *"todo el enrich de schema y demás que no se ve en la preview pero que optimiza viene después"* y *"lo del schema y demás dejalo dentro, no quiero tener que tocar más cosas"*.

### Por qué pasó
Originalmente entregué el HTML del cuerpo separado del schema. El cliente quería todo en un solo pegado.

### Cómo evitarlo
**Default: entregar HTML completo en UN SOLO bloque de código.** Incluir:
- `<style>` al inicio
- Cuerpo del artículo
- 2 bloques `<script type="application/ld+json">` al final

Que el cliente pueda copiar todo de una vez, pegar en modo HTML, y olvidarse.

## Resumen: Reglas de oro para evitar todos estos errores

1. **Antes de aplicar CSS**, verificar paleta de marca real (fetch o preguntar).
2. **Para tipografía**, usar `em` siempre. Nunca `rem` ni `px`.
3. **Forzar margins** en h2/ul/ol con `!important` y 3 selectores (.article-content, .rte, article).
4. **Envolver imágenes** en `<div class="article-image-center">`.
5. **CTAs alineados a la izquierda**, no centrados.
6. **Author box como caja diferenciada**, con celeste de marca + borde lateral.
7. **Disclaimer médico en ámbar separado**.
8. **Respuestas directas de 25-50 palabras**, no más.
9. **Antes de corregir un blog**, leer contenido vs title y preguntar cuál es el correcto.
10. **Siempre advertir del redirect 301** al cambiar handle.
11. **Pedir screenshot** antes de iterar CSS.
12. **Entregar todo en un solo bloque de HTML** (CSS + cuerpo + schema).
