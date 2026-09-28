# Reglas YMYL (Your Money Your Life)

YMYL = "Your Money or Your Life". Es la categoría de Google para contenido que puede impactar la salud, finanzas, seguridad o bienestar del lector. Para ecommerce de suplementos, salud, fitness, belleza médica y bienestar, **todos los blogs son YMYL**.

Google evalúa YMYL con criterios mucho más estrictos: E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness). Sin estos elementos, un blog YMYL no rankea aunque tenga todo el resto bien.

## Cuándo aplica YMYL

| Tema del blog | ¿Es YMYL? |
|---|---|
| Electrolitos, hidratación, salud | ✅ Sí |
| Lipedema, bariátrica, diabetes, cáncer | ✅ Sí (alto) |
| Suplementos (magnesio, vitaminas, omega-3) | ✅ Sí |
| Embarazo, lactancia, menopausia | ✅ Sí (alto) |
| Skincare, anti-aging | ✅ Sí (medio) |
| Comida para mascotas (con beneficios de salud) | ✅ Sí |
| Dietas (keto, vegana, ayuno intermitente) | ✅ Sí |
| Ejercicio para condiciones médicas | ✅ Sí |
| Ejercicio general (gym, running) | ⚠️ Medio (depende del enfoque) |
| Moda, decoración, juguetes | ❌ No |

**Regla práctica:** si el contenido sugiere consumir algo, hacer ejercicio, o cambiar un hábito que puede impactar la salud, es YMYL.

## Las 4 reglas no negociables en YMYL

### 1. Author = profesional clínico con credenciales públicas

**Obligatorio:** el campo Author del artículo (y del schema) debe ser una persona con credenciales clínicas verificables. **NUNCA la agencia (Advanz) ni la marca (Amazing Care)**.

Credenciales mínimas:
- Nutricionista titulado (con su matrícula si está disponible)
- Médico (con su especialidad y nº de colegiado si está disponible)
- Kinesiólogo / fisioterapeuta (titulado)
- Bioquímico, farmacéutico, psicólogo (según tema)

Si el contenido es de un creator/influencer sin credenciales clínicas, **no es contenido YMYL aceptable**. Hay 3 opciones:
- a) Sumar un profesional clínico como revisor (`reviewedBy` en schema)
- b) Reposicionar el blog como "opinión personal" / "mi experiencia" (cambia el ángulo SEO)
- c) No publicarlo

### 2. Bibliografía con fuentes científicas o institucionales

**Obligatorio:** al menos 3-5 referencias a:
- Papers peer-reviewed (Frontiers, NEJM, JAMA, Lancet, ScienceDirect, PubMed)
- Guidelines institucionales (OMS, FDA, NIH, ASMBS, sociedades médicas)
- Libros académicos de editoriales reconocidas (Academic Press, Elsevier, Springer)

**No vale:**
- Wikipedia
- Blogs de otras marcas
- Sitios genéricos como saludverdadera.com
- "Fuentes propias del autor sin link"

Formato sugerido:
```
Autor1, Autor2, AutorN. Título del paper en cursiva. Journal. Año.
```

Ejemplo:
```
Mechanick JI et al. Clinical Practice Guidelines for the Perioperative Nutrition, 
Metabolic, and Nonsurgical Support of Patients Undergoing Bariatric Procedures. 
Endocrine Practice. 2020.
```

### 3. Disclaimer médico obligatorio al cierre

**Obligatorio:** caja visible al final del artículo (antes de la bibliografía) con disclaimer médico.

Template estándar:

```html
<div class="medical-disclaimer">
  <p><strong>Aviso importante:</strong> este artículo tiene fines educativos y no 
  reemplaza el seguimiento con tu equipo médico. Sigue siempre las indicaciones 
  de tu profesional tratante. Los suplementos no son medicamentos y no están 
  diseñados para diagnosticar, tratar o curar ninguna enfermedad.</p>
</div>
```

**Adaptaciones según contexto:**
- Si es post-quirúrgico (bariátrica, cesárea): mencionar "tu cirujano y nutricionista de seguimiento"
- Si es embarazo/lactancia: mencionar "tu ginecólogo/obstetra y matrona"
- Si es niños: mencionar "tu pediatra"
- Si es deportivo intenso: mencionar "tu médico deportólogo"

### 4. Schema con E-E-A-T señalado

**Obligatorio:** el schema Article debe incluir:
- `author.knowsAbout`: lista de 3-5 temas de expertise del profesional
- `reviewedBy`: aunque sea la misma persona que escribe
- `about` con tipos schema específicos (`MedicalCondition`, `MedicalProcedure`, no solo `Thing`)

Ver `schema-templates.md` para los templates específicos.

## Lo que NO se puede hacer en YMYL

### ❌ Hacer afirmaciones de cura o tratamiento
- ❌ "Los electrolitos curan la fatiga"
- ❌ "El magnesio elimina la migraña"
- ❌ "Este suplemento previene la diabetes"
- ✅ "Los electrolitos pueden apoyar el bienestar muscular"
- ✅ "El magnesio se ha asociado con menor frecuencia de calambres en algunos estudios"

### ❌ Dar dosis específicas sin contexto profesional
- ❌ "Toma 600mg de magnesio antes de dormir"
- ✅ "La dosis diaria depende de tu peso, dieta y nivel de actividad — consulta con tu nutricionista para personalizarla. Como referencia, la dosis general recomendada en adultos es de 300-400mg/día (NIH)."

### ❌ Garantizar resultados
- ❌ "Te vas a sentir mejor en 7 días"
- ❌ "Verás los efectos al primer uso"
- ✅ "Algunas personas reportan mejoras en X-Y semanas, aunque los resultados pueden variar"

### ❌ Diagnosticar al lector
- ❌ "Si tienes fatiga, mareos y calambres, tienes deficiencia de electrolitos"
- ✅ "Estos síntomas pueden sugerir un desequilibrio de electrolitos, pero solo un profesional puede confirmarlo"

### ❌ Sustituir consulta médica
- ❌ "No necesitas ir al médico si tomas esto"
- ❌ "Antes de comprar este medicamento, prueba este suplemento"
- ✅ "Este suplemento puede ser un apoyo, pero no reemplaza el diagnóstico ni el tratamiento médico"

## Lo que SÍ tiene que estar en YMYL

### ✅ Lenguaje cauto y matizado
Usar "puede", "podría", "se ha asociado con", "algunos estudios sugieren", en lugar de "es", "garantiza", "cura".

### ✅ "Consulta con tu profesional" en cada CTA
El CTA del artículo debe incluir alguna mención a que el uso del producto debe coordinarse con el profesional de salud del lector. Esto:
- Protege legalmente a la marca
- Refuerza E-E-A-T (Google ve que la marca prioriza la salud sobre la venta)
- Mejora la conversión real (lectores informados convierten mejor que lectores presionados)

### ✅ "Cuándo consultar con un profesional" como sección dedicada
Idealmente como el último H2 antes del CTA. Lista las señales que indican que el lector debe consultar (no auto-medicarse). Ejemplo:

```
¿Cuándo consultar con un profesional?
- Síntomas persistentes > 2 semanas
- Síntomas que empeoran con el tiempo
- Cualquier signo de alarma específico al tema (sangrado, dolor agudo, etc.)
- Antes de iniciar suplementación si tienes condiciones crónicas
```

### ✅ Mención de poblaciones de riesgo
Si el contenido aplica a un suplemento o intervención, mencionar **quién no debería usarlo sin supervisión**:
- Embarazadas / lactantes
- Niños
- Adultos mayores con polifarmacia
- Personas con insuficiencia renal/hepática
- Personas en tratamiento con anticoagulantes (caso magnesio, vitamina K, etc.)

## Checklist YMYL

Antes de publicar un blog YMYL, validar:

- [ ] Author = profesional clínico (no agencia ni marca)
- [ ] Credenciales del autor visibles en el author box
- [ ] Al menos 3-5 referencias científicas en bibliografía
- [ ] Disclaimer médico al cierre (ámbar, visible)
- [ ] Schema Article con `author.knowsAbout`
- [ ] Schema Article con `reviewedBy`
- [ ] Schema con tipos específicos (`MedicalCondition`, `MedicalProcedure`)
- [ ] Lenguaje cauto en todo el artículo ("puede", no "cura")
- [ ] Ninguna afirmación de diagnóstico, cura o tratamiento
- [ ] Sin dosis específicas sin contexto profesional
- [ ] "Cuándo consultar con un profesional" como sección dedicada
- [ ] Mención de poblaciones de riesgo si aplica
- [ ] CTA con mención a consultar profesional

## Por qué esto importa para Advanz

**Para los clientes:**
- Sin YMYL bien hecho, los blogs no rankean (Google los penaliza algorítmicamente).
- Sin YMYL bien hecho, los LLMs no citan el contenido (porque detectan falta de E-E-A-T).
- Sin YMYL bien hecho, la marca queda expuesta legalmente.

**Para Advanz:**
- Es un diferenciador competitivo enorme. La mayoría de las agencias chilenas no hacen YMYL correctamente.
- Cuando un cliente ve cómo se hace bien y entiende el porqué, la retención sube.
- Cada cliente YMYL bien hecho se convierte en case study replicable.
