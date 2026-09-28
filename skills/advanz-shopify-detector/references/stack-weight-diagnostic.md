# Stack Weight Diagnostic — Cómo leer un stack y emitir veredicto

Detectar apps es solo la primera parte. El valor del skill está en **diagnosticar el stack como un todo**: ¿está sobre-stackeado? ¿sub-stackeado? ¿paga capacity sin usar? ¿le faltan capas críticas? Este archivo define el framework.

---

## Paso 1 — Calcular peso del stack

### Métricas a computar

```
TOTAL_COST = suma de "Costo USD/mes" de cada app detectada (rango medio del pricing)
APPS_COUNT = cantidad de apps con confianza ≥75%
COVERAGE = stages Growth Engine cubiertos / 8 (Foundations, Offer, Validation, Acquisition, Workflows, Retention, Feedback, Systems)
UTILIZATION = apps efectivamente en uso / apps instaladas
   (ej: Judge.me con 0 reviews = instalado, no en uso)
```

### Buckets de peso

| Bucket | TOTAL_COST | APPS_COUNT | Perfil típico |
|---|---|---|---|
| **Sub-stackeado** | <$50/mo | <3 | Tienda early-stage o vanilla Dawn. Falta capa Validation/Workflows |
| **Lean** | $50-200/mo | 3-6 | DTC <$50k/mo bien optimizado. Stack mínimo viable |
| **Mid-stack** | $200-600/mo | 6-10 | DTC $50-200k/mo. Stack completo equilibrado |
| **Heavy** | $600-1500/mo | 10-15 | DTC premium $200k-1M/mo. Algunas redundancias |
| **Enterprise** | >$1500/mo | 15+ | Shopify Plus / data-driven. Justificable solo con revenue alto |

### Output del paso 1

> "Stack actual: HEAVY ($1,100/mo en 12 apps detectadas). Coverage 7/8 stages Growth Engine. Utilization estimado 80% (1-2 apps instaladas sin uso visible)."

---

## Paso 2 — Detectar anti-patterns estructurales

Hay 7 patterns que indican mala arquitectura de stack, independiente del costo total:

### A1 — Capacity sin uso (instalado pero no expuesto)
**Cómo detectar**:
- `selling_plan_groups` presente en PDP pero PDP NO ofrece subscribe & save → Shopify Subscriptions activado backend, gap retention
- Judge.me con `data-number-of-reviews='0'` → instalado sin campaign de pedir reviews
- Klaviyo instalado sin popup home → pierden top-of-funnel email collection
- App de chat instalada pero widget no carga visible → gasto sin ROI

**Veredicto**: "X app instalada pero NO ofrecida al cliente. Activar en N horas dev o desinstalar."

### A2 — Doble engine en misma categoría (redundancia)
**Cómo detectar**:
- Clarity + Hotjar simultáneos → 80% feature overlap, deprecar Hotjar
- Recharge + Skio simultáneos → migración incompleta
- Klaviyo + OptiMonk con popups solapados → dobles disparos
- 2 reviews apps activos (raro, casi siempre false positive verificar)

**Veredicto**: "Redundancia en categoría X. Mantener Y, deprecar Z, ahorro mensual $N."

### A3 — Sobre-stackeado para el tier de revenue
**Cómo detectar**:
- Suma de costo apps > 5% del revenue mensual estimado
- Apps enterprise (Rebuy, LoyaltyLion, Attentive) en tiendas con tráfico <30k visitas/mes
- Triple stack analytics (Clarity + Hotjar + Mixpanel + Segment) sin data team

**Veredicto**: "Stack actual cuesta ~5% del revenue estimado. Reducir a X apps esenciales ahorra $N/mo sin pérdida medible."

### A4 — Sub-stackeado en capas críticas
**Cómo detectar capas obligatorias faltantes**:
- Sin app Reviews → falta Validation crítica
- Sin Email engine → pierde 20-30% revenue de flows
- Sin tracking confiable (Meta pixel, GA4, Clarity) → no se puede optimizar
- Sin upsell/bundles → AOV bajo techo

**Veredicto**: "Falta capa X. Recomendar app Y (alternativa Z más barata)."

### A5 — Pago apps que Liquid nativo cubre
**Cómo detectar**:
- App de sticky cart drawer cuando theme native lo soporta
- App announcement bar cuando OS 2.0 trae section
- App quick view cuando custom element del theme funciona
- App de quantity tiers cuando Liquid + JS reemplaza

**Veredicto**: "App X reemplazable con Liquid en N horas dev. Ahorra $Y/mo."

### A6 — Theme legacy con apps modernas pegadas
**Cómo detectar**:
- Theme pre-OS 2.0 (jQuery + handlebars + assets sin sections.json)
- HTML >20k líneas en PDP → tech debt grave
- Custom elements pegados forzadamente sobre theme antiguo

**Veredicto**: "Theme legacy genera tech debt. Migrar a OS 2.0 vanilla (Dawn fork) es ROI alto largo plazo. Performance mobile probable Lighthouse <40."

### A7 — Pago LATAM ausente en tienda LATAM
**Cómo detectar (Chile/México/Colombia/Argentina)**:
- Sin Mercado Pago
- Sin Webpay (Chile)
- Sin VentiPay/Fintoc (Chile checkout cuotas)
- Sin Cuotas/MSI (México)

**Veredicto**: "Friction crítica LATAM. Cliente local abandona checkout sin método familiar. Agregar X."

---

## Paso 3 — Cruzar con tier de revenue del cliente

El veredicto cambia según el tamaño del cliente. Tabla de referencia:

| Tier | Revenue/mo | Apps recomendados | Costo objetivo |
|---|---|---|---|
| **Starter** | <$10k | Klaviyo (free) + Judge.me (free) + Clarity (free) + Shopify Subs (native) | $0-30/mo |
| **Mid** | $10-50k | + Loox o Judge.me Awesome + Kaching/easyBundles + ReConvert + Klaviyo paid | $50-150/mo |
| **Growth** | $50-200k | + Recharge/Skio + Smile.io + UpCart + Elevar + Gorgias | $300-600/mo |
| **Premium** | $200k-1M | + Okendo + Rebuy + LoyaltyLion + Attentive SMS + Visually.io + Route | $1k-2k/mo |
| **Plus** | >$1M | + Segment + Triple Whale + Impact.com + Tolstoy/VideoWise + custom theme | $2k-5k+/mo |

**Si el stack actual no corresponde al tier**:
- Stack > tier → over-engineered, recomendar simplificación
- Stack < tier → opportunity costs, hay revenue dejado en la mesa

---

## Paso 4 — Generar veredicto final

Estructura del output (4 secciones obligatorias):

### 1. PESO DEL STACK
> Stack [Bucket] · [N] apps · ~$[TOTAL]/mo · coverage [X]/8 stages

### 2. LO QUE FUNCIONA
> Apps con uso confirmado e impacto medible. Mantener:
> - [App] cubriendo [stage] con buen ROI (Score 4-5)

### 3. ANTI-PATTERNS DETECTADOS
> Listar los que aplican de A1-A7 con acción concreta:
> - A1: [App] instalado sin usar → activar o desinstalar
> - A2: Redundancia [App1] + [App2] → mantener X, deprecar Y, ahorro $N/mo
> - A4: Falta capa [X] → recomendar [App Y]
> - A7: Sin [método pago LATAM] → agregar

### 4. RECOMENDACIONES PRIORIZADAS
> Top 3 acciones ordenadas por impacto/esfuerzo:
> 1. **Quick win** (1-2h, impacto alto): [acción concreta]
> 2. **Mejora media** (1-2 días, impacto medio): [acción]
> 3. **Stack evolution** (semanas, impacto largo plazo): [acción]

---

## Integración con `ecomm-benchmark-agent` y `ecomm-competitive-benchmark`

Este skill se invoca cuando esos benchmarks necesitan **destripar competidores**. Flujo típico:

```
ecomm-competitive-benchmark identifies 3 competidores →
  for each competidor:
    invoca advanz-shopify-detector con URL →
    detector retorna stack + diagnóstico →
  benchmark compara stacks: cliente vs competidor 1 vs 2 vs 3 →
  output: "Tu stack tiene X capas. Competidor más exitoso tiene Y."
```

### Inputs que el detector recibe del benchmark
- URL del competidor
- Tier estimado de revenue (si está calculado)
- Vertical del mercado
- Cliente Advanz al que se compara (para mapear "qué le serviría")

### Outputs que el detector entrega al benchmark
- Stack costo estimado
- Coverage Growth Engine
- 3 patterns transferibles más fuertes
- Apps que el cliente Advanz DEBERÍA tener pero no tiene
- Apps que NO debería copiar (overhead injustificado)

---

## Consultar la DB de Notion durante un análisis

Cuando este skill detecta una app, debe enriquecer la inferencia consultando `Shopify Apps Catalog` (`ecce7849-2386-430a-bfd7-4e2a229bf4cf`):

```python
# Pseudo-flujo
detected_apps = scan_store(url)  # ['Klaviyo', 'Judge.me', 'PageFly']

for app in detected_apps:
    catalog_entry = notion_query(
        database="Shopify Apps Catalog",
        filter={"App": app}
    )
    # catalog_entry contiene: score_roi, impacto, cuando_si, cuando_no, alternativas
    
    enriched_diagnosis = {
        "app": app,
        "verdict": evaluate(catalog_entry, client_tier, client_revenue),
        "alternatives": catalog_entry["Alternativas"]
    }
```

Si una app detectada NO está en el catálogo:
1. Reportarla con confianza ≥75%
2. Crear entrada nueva en el catálogo con `Estado="Por validar"`
3. Notion sirve como pattern library acumulativa
