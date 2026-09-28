# Diagnóstico de Cliente — cómo mapear un cliente al Growth Engine

Este archivo se usa cuando el usuario pega un brief o describe un cliente y pide diagnóstico/propuesta.

---

## Proceso de diagnóstico (5 pasos)

### Paso 1 — Recolectar señales

Preguntar (si no está en el brief) o inferir:

**Sobre el negocio:**
- Vertical (suplementos, fashion, beauty, pet, home, etc.)
- Plataforma actual (Shopify, WooCommerce, Jumpseller, ninguna)
- Volumen mensual de ventas (rango)
- Antigüedad del negocio
- País / mercado principal

**Sobre el estado actual del Growth Engine (en orden):**
- ¿Tiene ICP claro, propuesta de valor diferenciada, 7 Maletas hechas? → Etapa 1
- ¿Tiene PDPs con schema, descripciones específicas, comparativas? → Etapa 2
- ¿Lee sus primeras ventas, hace A/B testing, tiene quizzes? → Etapa 3
- ¿Está corriendo paid media activo? Solo Meta o también Google/TikTok? ¿GEO setup? → Etapa 4
- ¿Aparece en respuestas de ChatGPT/Perplexity para su categoría? → Etapa 4 (GEO)
- ¿Tiene flujos de email automáticos? ¿Customer Hub/Agent? ¿WhatsApp commerce? → Etapa 5
- ¿Programa de retención, predictive segments, subscription, loyalty? → Etapa 6
- ¿Reviews trabajadas, captura de feedback en web/WhatsApp, citation tracking? → Etapa 7
- ¿Stack tech integrado, agentes IA, reportes automáticos vía MCP? → Etapa 8

**Sobre el dolor declarado:**
- ¿Qué dijo que necesita el cliente?
- ¿Qué métrica quiere mover (ventas, ROAS, LTV, CAC)?

---

### Paso 2 — Asignar score por etapa

Para cada una de las 8 etapas, asignar uno de estos estados:

- ✅ **Sólido** — la etapa está cubierta y operando bien
- ⚠️ **Débil** — la etapa existe pero tiene gaps importantes
- ❌ **Ausente** — la etapa no está cubierta

Ejemplo de output mental:
```
1. Foundations — ⚠️ (Shopify ok pero ICP genérico, sin 7 Maletas, AI-readiness incompleto)
2. Offer — ⚠️ (PDPs genéricas, sin comparativas, schema básico)
3. Validation — ❌ (no hay quiz ni A/B testing sistemático)
4. Acquisition — ✅ (Meta corriendo bien, ROAS estable)
5. Workflows — ⚠️ (3 flujos básicos, sin Customer Hub, sin WhatsApp commerce)
6. Retention — ❌ (sin segmentos predictivos, sin subscription, sin loyalty)
7. Feedback — ❌ (reviews ignoradas, sin citation tracking)
8. Systems — ❌ (no es momento — etapas anteriores débiles)
```

---

### Paso 3 — Identificar las 2-3 etapas críticas

**Reglas de priorización:**

1. **Si hay una ❌ antes de una ✅, atacar la ❌ primero.** El Growth Engine no salta etapas. No tiene sentido tener Acquisition sólido si Validation no existe — se tira plata.

2. **Si todas son ⚠️, priorizar por palanca:** la etapa que destrabe la siguiente con menor inversión.

3. **Si el dolor declarado coincide con una etapa débil/ausente, esa es prioridad 1.** Si el cliente dice "no retengo", aunque Acquisition esté débil, Retention es prioridad porque ahí está el dolor.

4. **Nunca recomendar Systems si Retention y Feedback no están sólidas.** Esto es la regla más importante del Growth Engine v2. Si el cliente pide "automatización" sin tener Retention/Feedback resueltos, la respuesta es "primero validemos qué retiene, después automatizamos eso".

5. **No proponer más de 3 etapas en una sola propuesta.** Más es overload y mata el cierre.

---

### Paso 4 — Mapear cada etapa crítica a un servicio Advanz

| Etapa crítica | Servicio Advanz que la cubre |
|---------------|------------------------------|
| Foundations | Diagnóstico A250 (incluye 7 Maletas + AI-readiness) |
| Offer | Migración Shopify (LITE/PRO/ENTERPRISE), CRO Consulting |
| Validation | Reporte CRO, Quiz Add-on, Benchmark Competencia |
| Acquisition | Paid Media (LITE/PRO/ENTERPRISE), Migración con SEO/GEO, Social Media |
| Workflows | Setup pack Workflows, Email Marketing, Customer Hub setup |
| Retention | Mantención Workflows, Email recurrente, Predictive segments, Subscription engine |
| Feedback | Reportes mensuales, Reviews automation, AI Citation Score |
| Systems | Plan ENTERPRISE, Add-ons integraciones, Mantención Web Avanzada, Reportes MCP |

**Regla:** cada etapa propuesta debe aterrizar en al menos 1 servicio web declarado. Si no aterriza, es un gap de oferta y hay que decirlo (no inventar servicios).

---

### Paso 5 — Estructurar la respuesta

Output estándar:

```markdown
## Diagnóstico actual

[1-2 párrafos. En qué etapa del Growth Engine está el cliente hoy. Qué está sólido, qué está débil. Sin tecnicismos innecesarios.]

## Etapas críticas (en orden de prioridad)

### 1. [Nombre etapa] — [estado]
- Lo que falta: [descripción concreta]
- Por qué es prioridad: [conexión con dolor del cliente o lógica del Growth Engine]

### 2. [Nombre etapa] — [estado]
[idem]

### 3. [Nombre etapa] — [estado]  (opcional, solo si aplica)
[idem]

## Roadmap recomendado

| Fase | Etapa | Servicio Advanz | Outcome esperado |
|------|-------|-----------------|------------------|
| 1 | [...] | [...] | [...] |
| 2 | [...] | [...] | [...] |
| 3 | [...] | [...] | [...] |

## Por qué este orden

[Explicación corta de cómo cada fase habilita la siguiente. Lógica del Growth Engine. Énfasis en por qué Systems no se trabaja todavía si etapas anteriores están débiles.]

## Métricas para medir avance

[3-5 métricas concretas — pueden ser ROAS, LTV, citation share, repeat purchase rate, CVR, etc., según etapas atacadas]

## Próximo paso

[Acción concreta — agendar A250, propuesta formal, llamada con [stakeholder]. Sin precio.]
```

---

## Ejemplos resueltos

### Ejemplo 1 — Marca de suplementos con Shopify, ventas estancadas

**Brief:** "Marca de electrolitos, en Shopify hace 1 año, vende ~$5M CLP/mes, gasta $1.5M en Meta, ROAS 2.1x. Ventas planas hace 4 meses. Klaviyo conectado pero solo bienvenida y carrito. Sin TikTok. Sin GEO. Sin reviews systematic."

**Diagnóstico mental:**
1. Foundations — ⚠️ (Shopify ok, ICP probable pero 7 Maletas no documentadas, AI-readiness incierta)
2. Offer — ⚠️ (asumimos PDPs genéricas)
3. Validation — ❌ (sin quiz, sin testing sistemático)
4. Acquisition — ⚠️ (solo Meta, sin GEO, sin TikTok)
5. Workflows — ❌ (solo 2 flujos básicos)
6. Retention — ❌ (recompra no trabajada en categoría que es 100% recompra)
7. Feedback — ⚠️ (reviews probables pero sin citation tracking)
8. Systems — ❌ (NO es momento — Retention y Feedback débiles)

**Etapas críticas (orden):**
1. **Workflows** (❌, alta palanca, categoría de recompra)
2. **Retention** (❌, electrolitos = replenishment, oro puro sin trabajar)
3. **Acquisition GEO** (⚠️, captura tráfico que se va a AI Overviews)

**Servicios mapeados:**
- Setup pack de Workflows + Customer Hub setup
- Email Marketing PRO (4 correos/mes con predictive segments + replenishment flow)
- Diagnóstico A250 para detectar GEO gaps + Mantención Web Avanzada para implementar GEO

**Por qué este orden:** Antes de gastar más en ads, capturamos lo que ya entra. Con Workflows + Retention sólidos, el ROAS efectivo sube y el LTV justifica subir budget. Después atacamos GEO para ampliar superficie de adquisición sin pelear CPMs en Meta.

**Por qué NO Systems todavía:** Aunque el cliente probablemente diría que sí a "automatización", no tiene sentido. Sin Retention y Feedback validados, los agentes IA no tienen data limpia para operar.

---

### Ejemplo 2 — Marca de fashion sin tienda propia (vende solo en Instagram)

**Brief:** "Marca de ropa femenina, vende solo por Instagram DM, $3M CLP/mes, 15K followers, sin tienda propia, considera Shopify. Quiere escalar."

**Diagnóstico mental:**
1. Foundations — ❌ (no hay tienda; ICP probable por venta DM pero no documentado)
2. Offer — ❌ (productos no estructurados, sin schema)
3-8. Todas ❌ porque no hay base

**Etapa crítica única:** **Foundations + Offer** simultáneas — armar la tienda con AI-readiness desde el día 1, partiendo de las 7 Maletas.

**Servicios mapeados:**
- Diagnóstico A250 (sin costo, base para todo)
- Migración / Desarrollo Shopify **PRO** (incluye PDPs con JSON-LD, SEO/GEO, conversión, hasta 200 SKU)
- Setup pack de Workflows básicos para empezar a capturar email/WhatsApp desde el día 1

**Por qué este orden:** No tiene sentido pensar en Acquisition o Retention sin tienda. Primer ciclo del Growth Engine = construir base. Segundo ciclo (3-6 meses después) = agregar Paid Media + Workflows avanzados. Tercer ciclo = Retention + Feedback + eventualmente Systems.

---

### Ejemplo 3 — Cliente activo Advanz, upsell

**Contexto:** Cliente activo con Migración Shopify PRO completa, Paid Media PRO mensual hace 4 meses, ROAS 3.2x, ventas crecen pero LTV plano.

**Diagnóstico mental:**
1. Foundations — ✅
2. Offer — ✅
3. Validation — ⚠️
4. Acquisition — ✅
5. Workflows — ⚠️ (4 flujos del setup pack pero sin Customer Hub)
6. Retention — ❌ (LTV plano = retention rota)
7. Feedback — ⚠️ (reviews sin trabajar)
8. Systems — ❌ (no es momento todavía)

**Etapa crítica (única, upsell):** **Retention + Feedback** como bloque.

**Servicio para ofrecer:**
- Email Marketing PRO (escalar de N a 4 correos/mes con predictive segments)
- Customer Hub / Customer Agent setup (capa nueva sobre setup pack existente)
- Reviews automation como flujo #6
- Subscription engine si la categoría aplica

**Pitch:** "Ya tenemos el Growth Engine girando — Foundations, Offer y Acquisition están sólidas. El próximo lift no viene de gastar más en ads, viene de retener a los clientes que ya estás trayendo. Las etapas 6 y 7 del engine están abiertas y ahí está el LTV que estás dejando en la mesa. Cuando estas dos estén operativas con data limpia, podemos empezar a hablar de Systems para automatizar lo que ya validamos que retiene."

---

### Ejemplo 4 — Cliente que pide "automatización" sin tener bases

**Brief:** "Tengo una tienda Shopify hace 6 meses, vende ~$2M CLP/mes. Quiero automatizar todo, escuché que se puede tener un agente IA que venda solo. Quiero eso."

**Diagnóstico mental:**
1-3. Probablemente débiles (poca data en 6 meses)
4. Acquisition probablemente ⚠️
5-7. Probablemente ❌ o ⚠️
8. Cliente pide Systems pero NO es momento

**Respuesta correcta:** Educar primero. Aplicar la regla de oro.

> "Te entiendo, pero te va a salir caro y lento si automatizamos ahora. Un agente IA que vende solo necesita data validada para operar bien — qué oferta retiene, qué dice tu cliente cuando compra, qué objeciones aparecen. Sin eso, el agente reproduce errores a escala.
>
> Mi recomendación: primero hacemos Diagnóstico A250 para mapear dónde estás en el Growth Engine. Probablemente faltan etapas 5, 6 y 7 (Workflows, Retention y Feedback) antes de poder hablar de Systems. Cuando esas estén sólidas, Systems multiplica los resultados de forma honesta."

---

## Checklist final antes de mandar el diagnóstico

- [ ] ¿Mapeé las 8 etapas en el orden correcto?
- [ ] ¿Identifiqué máximo 3 etapas críticas?
- [ ] ¿Cada etapa crítica aterriza en un servicio web declarado?
- [ ] ¿No salté etapas (no propongo Acquisition si Foundations está rota)?
- [ ] ¿No propuse Systems si Retention/Feedback están débiles?
- [ ] ¿Conecté el dolor declarado con la priorización?
- [ ] ¿No mencioné precios?
- [ ] ¿El roadmap es ejecutable, no aspiracional?
- [ ] ¿Las métricas de medición son concretas?
- [ ] ¿Usé "Growth Engine" y no "Flywheel" en la respuesta?
