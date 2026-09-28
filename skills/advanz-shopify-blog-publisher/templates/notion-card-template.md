# Template Notion Card — Ideas de Blogs SEO

Plantilla para crear tarjetas de ideas de blogs en boards de Notion para validación con el profesional clínico del cliente.

## Cómo usar

1. Identificar el data_source_id del board de SEO del cliente en Notion.
2. Verificar las etiquetas existentes (Autor, Categoría, Estado/Select) antes de crear.
3. Usar `Notion:notion-create-pages` con el contenido de la tarjeta.
4. **NUNCA inventar etiquetas nuevas** — usar solo las existentes.

## Etiquetas estándar de Amazing Care (referencia)

Si el cliente es Amazing Care, las etiquetas son:

- **Autor**: `Advanz`, `AmazingCare`
- **Categoría**: `Autoridad/Científico`, `Sabor/Formato`, `Composición/Nutrición`, `Condiciones`, `Deporte`
- **Select** (estado): `Revisión`, `Cambios`, `Aprobado`, `Publicado`

Para otros clientes, **fetch el board primero** para obtener las etiquetas reales.

## Contenido de cada tarjeta

Cada tarjeta debe tener **5 secciones obligatorias**:

### 1. 💡 Idea para validar con [profesional clínico]
Contexto estratégico: por qué este artículo importa, qué tráfico capturaría, qué pieza del cluster topical cubre.

### 2. 🎯 Objetivo SEO
- **Query principal**: la búsqueda exacta que apunta el artículo
- **Queries secundarios**: 3-4 variaciones long-tail
- **Intención**: comercial alta / informacional / mixta
- **Competencia**: alta / media / baja (con justificación)

### 3. 📋 Estructura sugerida
Outline numerado de los H2 que tendría el artículo. Esto le da al profesional una idea concreta de qué responder.

### 4. ✅ Para validar [profesional clínico]
Preguntas específicas que el profesional necesita responder antes de redactar el artículo. Esto reduce idas y vueltas.

### 5. 📊 Por qué importa / Recomendación de mes
Justificación estratégica + recomendación de cuándo publicar dentro del calendario del cliente.

## Template de contenido (markdown para Notion)

```markdown
## 💡 Idea para validar con [Profesional]

[Contexto estratégico de 2-3 párrafos: por qué este artículo importa para el cluster, qué query capturaría, qué pieza del funnel cubre.]

## 🎯 Objetivo SEO

- **Query principal:** [query exacta]
- **Queries secundarios:** [query 1], [query 2], [query 3]
- **Intención:** [Comercial alta / Informacional / Mixta]
- **Competencia:** [Alta global / Media / Baja con justificación]

## 📋 Estructura sugerida

1. **[H2 #1]** ([descripción breve])
2. **[H2 #2]** ([descripción breve])
3. **[H2 #3]** ([descripción breve])
4. **[H2 #4]** ([descripción breve])
5. **[H2 #5]** ([descripción breve])
6. **Conexión a producto** ([cómo se enlaza con la colección])

## ✅ Para validar [Profesional]

- ¿[Pregunta clínica 1]?
- ¿[Pregunta clínica 2]?
- ¿[Pregunta clínica 3]?
- ¿[Pregunta clínica 4]?

## 📊 Por qué es estratégico

[Justificación de la priorización: volumen de búsqueda, competencia, valor para el funnel.]

**Recomendación: publicar en mes [N].**
```

## Llamada al tool

```javascript
Notion:notion-create-pages({
  parent: { 
    type: "data_source_id", 
    data_source_id: "[ID_DEL_BOARD]" 
  },
  pages: [{
    properties: {
      "Entrada": "[Título del blog propuesto]",
      "Autor": "[AmazingCare | Advanz | etc.]",
      "Categoría": "[etiqueta existente del board]",
      "Select": "Revisión"  // siempre empezar en estado más temprano
    },
    content: "[markdown con las 5 secciones]"
  }]
})
```

## Reglas de batch creation

- **Crear máximo 4 tarjetas por batch.** Más que eso satura al cliente y al profesional clínico.
- **Cada batch debe ser un cluster temático coherente.** No mezclar topics distantes.
- **Mix obligatorio del batch:**
  - 1 pillar comercial (la pieza más importante)
  - 1 caso de uso médico/condición (YMYL)
  - 1 caso de uso lifestyle moderno (deporte, ayuno, vegano, etc.)
  - 1 soporte informacional puro (comparativo, tipos, ingredientes)

## Categorías recomendadas según topic

Para clientes de salud/suplementos (estilo Amazing Care):

| Tipo de artículo | Categoría sugerida |
|---|---|
| Pillar comercial ("Mejores X en Chile") | Composición/Nutrición |
| Caso médico (lipedema, bariátrica) | Condiciones |
| Caso deportivo (running, gym) | Deporte |
| Comparativo de tipos (magnesio, vitaminas) | Composición/Nutrición |
| Sabor / formato / experiencia | Sabor/Formato |
| Estudio científico / investigación | Autoridad/Científico |

## Estados del flujo

| Estado | Cuándo aplica | Próximo paso |
|---|---|---|
| `Revisión` | Recién creado, esperando feedback del profesional clínico | Cliente/profesional revisa |
| `Cambios` | Profesional pidió ajustes | Se actualiza la tarjeta |
| `Aprobado` | Profesional dio luz verde | Se redacta el artículo |
| `Publicado` | El blog ya está en Shopify | Se monitorea SEO |

## Ejemplo completo (Amazing Care)

**Title:** `Mejores Electrolitos en Chile 2026: Guía Completa para Elegir`

**Properties:**
- Autor: `AmazingCare`
- Categoría: `Composición/Nutrición`
- Select: `Revisión`

**Content:**

```markdown
## 💡 Idea para validar con Paula

Este es el **pillar comercial del cluster**. Cuando alguien pregunta a ChatGPT "qué electrolitos comprar en Chile" o busca "mejores electrolitos sin azúcar Chile", este artículo es el que debería aparecer. Hoy Amazing Care no compite por esta query porque no tiene contenido dedicado.

## 🎯 Objetivo SEO

- **Query principal:** mejores electrolitos en Chile 2026
- **Queries secundarios:** mejores electrolitos sin azúcar Chile, qué electrolitos comprar en Chile, electrolitos en polvo Chile
- **Intención:** Comercial alta — persona comparando opciones, lista para comprar
- **Competencia:** Media — hay listicles genéricos pero ninguno chileno serio

## 📋 Estructura sugerida

1. **Qué buscar en un electrolito** (criterios técnicos: sodio, potasio, magnesio, sin azúcar, registro sanitario)
2. **Comparativa honesta de marcas disponibles en Chile** (incluyendo competidores → da credibilidad y los LLMs lo citan más)
3. **Casos de uso** (deporte, ayuno, calor, resaca, lipedema, embarazo)
4. **Recomendación final con criterio** (no "el mejor es el nuestro", sino "para X caso, X; para Y caso, Y")
5. **Conexión a la colección de Amazing Care**

## ✅ Para validar Paula

- ¿Hay criterios técnicos adicionales que debería incluir desde nutrición clínica?
- ¿Qué marcas chilenas conoce y considera serias para incluir en comparativa?
- ¿Hay diferencia clínica entre formatos (polvo vs efervescente vs líquido) que deba destacar?
- ¿Algún caso de uso adicional que vea seguido en consulta?

## 📊 Por qué es la pieza más importante

Es el artículo madre del cluster. Todos los demás artículos linkearán a este, así que conviene tenerlo primero para construir autoridad desde el inicio. **Recomendación: publicar en mes 1.**
```
