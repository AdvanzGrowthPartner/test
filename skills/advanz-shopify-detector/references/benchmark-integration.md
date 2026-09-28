# Integration with Benchmark Skills

Este skill se conecta con `ecomm-benchmark-agent` y `ecomm-competitive-benchmark`. Esta referencia define cómo se invoca y qué información intercambian.

---

## Invocación desde `ecomm-competitive-benchmark`

Cuando el benchmark identifica competidores Shopify y necesita destripar sus stacks, este skill se invoca para cada uno.

### Trigger phrases que activan la integración
- "destripa el stack de [competidor]"
- "qué apps usa [competidor]"
- "compara mi stack vs [competidor]"
- "para el benchmark de competencia, analiza [URL Shopify]"
- "mega-stack del segmento [vertical]"

### Inputs requeridos del benchmark
- `competitor_url` — URL pública del competidor
- `client_advanz` — cliente Advanz al que se compara (para mapear "qué le serviría")
- `client_revenue_tier` — tier estimado del cliente (Starter/Mid/Growth/Premium/Plus)
- `vertical` — vertical para filtrar apps no aplicables
- `pais` — Chile/USA/UK/etc para evaluar pagos LATAM

### Outputs que el detector entrega al benchmark
```yaml
competitor: <name>
stack:
  total_cost_usd_month: <number>
  apps_detected: <number>
  coverage_growth_engine: <X/8>
  bucket: <Sub-stackeado/Lean/Mid/Heavy/Enterprise>
  apps_by_category:
    Reviews: [<app>]
    Subscriptions: [<app>]
    ...
diagnosis:
  anti_patterns: [<A1, A2, A3...>]
  what_works: [<bullet1>, <bullet2>]
  what_overspends: [<bullet1>]
  what_missing: [<bullet1>]
transferable_to_client:
  - app: <name>
    reason: <why it would help>
    cost: <$N/mo>
    effort: <horas Advanz>
not_transferable:
  - app: <name>
    reason: <over-engineered for client tier>
```

---

## Invocación desde `ecomm-benchmark-agent`

El benchmark agent puede invocar este skill para 2 casos:

### Caso A — Diagnóstico de un cliente Advanz propio
Cuando se está armando el reporte mensual de un cliente y se quiere validar:
- ¿El stack actual del cliente sigue siendo el correcto?
- ¿Hay capacity instalada sin uso?
- ¿Hay redundancias después de meses de operación?

### Caso B — Discovery de prospect
Antes de una llamada de venta con un prospect, scan rápido de su tienda Shopify para:
- Identificar gaps obvios (capas faltantes)
- Estimar peso del stack actual y oportunidad
- Preparar pitch específico

### Flujo de Caso B (más común)
```
1. Sales/closer le pasa URL del prospect al benchmark
2. Benchmark invoca este skill
3. Skill scrape la tienda + shadow buyer
4. Skill consulta Notion DB Shopify Apps Catalog para enriquecer
5. Skill devuelve diagnóstico
6. Benchmark integra con investigación de mercado del prospect
7. Output final = pitch personalizado para la call
```

---

## Compatibilidad con `advanz-cco-agent`

El cco-agent gestiona el pipeline comercial. Cuando un lead viene con URL Shopify:

1. cco-agent detecta que la URL es Shopify (lookup básico)
2. cco-agent invoca este skill antes de la discovery call
3. Diagnóstico se carga en la entrada del lead en Notion (DB Leads)
4. Closer arriba a la call con datos concretos del stack del prospect

**Lo que se carga al lead**:
- Plataforma confirmada (Shopify)
- Theme + customization level
- Apps detectadas (count + lista corta)
- Anti-patterns visibles externamente
- Quick wins potenciales (top 3 acciones)

Esto convierte la discovery call de "preguntas genéricas" a "diagnóstico evidente" y eleva el closing rate.

---

## Patrones cross-skill replicables

Cuando este skill identifica un pattern interesante en una tienda (ej: outcome-based naming), lo guarda en Notion `Shopify Tools Library` (DB de tiendas). Luego:

- `viral-hooks` puede pedirle "dame hooks para nombres outcome-based" → consulta los nombres reales detectados
- `ecomm-benchmark-agent` puede pedir "qué patterns están usando los líderes del vertical X" → query a tiendas analizadas
- `advanz-closing-agent` puede usar evidencia: "Marca Y (líder) usa esto, vos no"

---

## Reglas para mantener la integración consistente

1. **Cada análisis nuevo** se sube siempre a Notion DB `Shopify Tools Library` (tienda) — no a memoria temporal
2. **Apps nuevas detectadas** se agregan a `Shopify Apps Catalog` con `Estado="Por validar"` para revisión humana
3. **Patterns transferibles** identificados deben citar tienda fuente (`Visto en tiendas` field)
4. **Diagnósticos NO se almacenan permanentes** — son output de inferencia, regenerable. Solo se persiste evidencia bruta y catálogo de apps
5. **Cliente Advanz target field** en el catálogo se llena solo con clientes existentes Advanz; "Cualquiera DTC" / "Solo enterprise" / "Solo LATAM" son tags genéricos
