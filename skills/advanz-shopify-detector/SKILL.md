---
name: advanz-shopify-detector
description: Detector + diagnóstico de stack Shopify para Advanz. Identifica apps, theme y addons de tienda Shopify pública vía HTML, JS, network y shadow buyer. Emite veredicto sobre si stack está sub/sobre-stackeado al tier de revenue, qué apps aportan vs sobran, y patterns replicables. Usa cuando el usuario pegue URL Shopify o pida 'analiza esta tienda', 'qué tools/apps usa', 'destripa esta tienda', 'cómo replicar esto', 'qué pixel/review/subscription', 'cuánto invierte en stack', 'mi stack vs competidor X', 'qué le falta', 'diagnóstico stack', 'peso stack', 'shadow buyer', 'simula checkout', 'mega-stack vertical X'. Motor de inferencia para ecomm-benchmark-agent (destripa competidores), ecomm-competitive-benchmark y advanz-cco-agent (discovery prospects). Persiste en Notion 'Shopify Tools Library' (tiendas) y enriquece 'Shopify Apps Catalog' (apps con signatures, score ROI, replicabilidad). SOLO Shopify — no WooCommerce, Tienda Nube ni Jumpseller.
---

# Advanz Shopify Detector

Detector + diagnóstico de stacks Shopify. Este skill NO es una enciclopedia de apps — la enciclopedia vive en Notion. Este skill es el **motor de inferencia**: detecta lo que hay, evalúa si vale la pena, y emite veredicto accionable.

## Cuándo se usa

1. **Análisis directo**: el usuario pega URL Shopify y pide entender el stack
2. **Discovery de prospect**: pre-call analysis para cco-agent
3. **Benchmark de competencia**: invocado por ecomm-competitive-benchmark
4. **Pattern mining**: el usuario quiere extraer lo que usan los líderes del vertical

## Cuándo NO se usa

- Tiendas que no son Shopify (WooCommerce, Tienda Nube, Jumpseller, Wix, Magento) — abortar
- Análisis B2B/SaaS sin componente ecommerce — usar otros skills
- Sin URL pública / sitio bloqueado por bot detection — pedir credenciales o admitir limitación

## Workflow obligatorio

### Paso 0 — Pre-flight (siempre)
Confirmar que es Shopify ANTES de analizar:
```bash
curl -sL -A "Mozilla/5.0 ..." "$URL" | grep -oE "Shopify\.shop|cdn\.shopify|/cdn/shop/|myshopify"
```
Si no devuelve nada → la tienda NO es Shopify, abortar.

### Paso 1 — Detección (6 capas)
Ejecutar las 6 capas de detección descritas en `references/detection-patterns.md`:
1. App blocks embebidos (`shopify://apps/`)
2. Selling plan groups (subscription engine identification)
3. Dominios externos (CDN signatures por categoría)
4. JS globals (window.* signatures)
5. Custom elements (apps reemplazadas por Liquid)
6. Active shadow buyer (validar configuración real)

### Paso 2 — Validación contra false positives
Antes de declarar una detección con confianza alta, verificar contexto. Casos típicos:
- Loox/Yotpo/Okendo a veces aparecen como menciones cruzadas en código legacy
- Recharge legacy puede quedar después de migración a Skio
- Judge.me instalado con 0 reviews no cuenta como "en uso"

Si un signal es ambiguo, validar con grep contextual ±30 chars o aceptar la app como "probable" con confianza <75%.

### Paso 3 — Enriquecimiento desde Notion
Por cada app detectada, consultar `Shopify Apps Catalog` (Notion DB `ecce7849-2386-430a-bfd7-4e2a229bf4cf`):
- Score ROI
- Capa Growth Engine
- Cuándo SÍ vale / cuándo NO vale
- Alternativas
- Cliente Advanz target

Si la app NO está en el catálogo:
1. Reportarla con confianza estimada
2. Crear entrada nueva con `Estado="Por validar"`
3. La pattern library acumulativa crece automáticamente

### Paso 4 — Diagnóstico de peso del stack
Aplicar el framework de `references/stack-weight-diagnostic.md`:
- Calcular TOTAL_COST, APPS_COUNT, COVERAGE, UTILIZATION
- Clasificar en bucket (Sub-stackeado, Lean, Mid-stack, Heavy, Enterprise)
- Detectar los 7 anti-patterns estructurales (A1-A7)
- Cruzar con tier de revenue del cliente

### Paso 5 — Scoring por app
Para cada app detectada, aplicar las 5 preguntas de `references/funnel-impact-scoring.md`:
1. ¿Qué capa cubre?
2. ¿Está siendo usada?
3. ¿Coincide con el tier?
4. ¿Es reemplazable más barato?
5. ¿Cuál es su Score ROI?

Output por app: MANTENER / DEPRECAR / REEMPLAZAR / ACTIVAR + acción concreta.

### Paso 6 — Persistencia en Notion
SIEMPRE crear entrada en `Shopify Tools Library` (Notion DB `13ce4773-1586-4c99-8bec-ebae6dd77bff`) con:
- Tienda + URL + país + vertical
- Stack detectado (apps por categoría)
- Costo mensual estimado
- Anti-patterns visibles
- Highlights replicables
- Cliente Advanz candidato

NO almacenar diagnósticos (son output regenerable). SÍ almacenar evidencia bruta y patterns observados.

### Paso 7 — Output al usuario
4 secciones obligatorias:
1. **Peso del stack** — bucket, costo, coverage
2. **Lo que funciona** — apps con uso confirmado e impacto
3. **Anti-patterns detectados** — A1-A7 aplicables con acción
4. **Recomendaciones priorizadas** — top 3 por impacto/esfuerzo

Formato: prosa concisa + tablas para datos comparativos. NO listar las 80 apps del catálogo — listar solo las detectadas en la tienda analizada.

## Referencias

- `references/detection-patterns.md` — patrones de detección por categoría (no por marca)
- `references/theme-fingerprints.md` — fingerprints de themes (Dawn forks, paid themes, custom)
- `references/stack-weight-diagnostic.md` — framework de diagnóstico de peso del stack
- `references/funnel-impact-scoring.md` — scoring por app dentro del funnel
- `references/benchmark-integration.md` — integración con ecomm-benchmark-agent y cco-agent
- `references/notion-schema.md` — schemas de las 2 DBs Notion
- `references/report-template.md` — estructura del output

## Reglas firmes

1. **NUNCA listar el catálogo completo** de apps al usuario. Solo apps detectadas en la tienda analizada.
2. **NUNCA declarar detección al 100%** sin signal confirmatorio (no solo menciones en HTML).
3. **SIEMPRE persistir en Notion** al final del análisis — pattern library acumulativa es el ROI del skill.
4. **Si una app NO está en el catálogo Notion**, crearla con estado "Por validar" — NO inventar score ni costo.
5. **Stack diagnóstico SIEMPRE cruzado con tier de revenue del cliente** — una app puede ser excelente para tier Premium y catastrófica para Starter.
6. **Apps de uso "instalado pero no expuesto"** son tan importantes como apps faltantes — anti-pattern A1.
7. **El skill NO es una encyclopedia** — para info detallada de una app específica, consultar Notion `Shopify Apps Catalog`.

## Atajos comunes

### Para discovery de prospect (cco-agent)
Saltar Paso 7 detalle, devolver solo:
- Plataforma confirmada
- Apps detectadas (count + top 5)
- Top 3 anti-patterns
- Top 3 quick wins potenciales

### Para benchmark de competencia
Output estructurado en YAML (ver `benchmark-integration.md`) en lugar de prosa.

### Para análisis libre del usuario
Output completo en 4 secciones + tabla de apps + recomendaciones.

## Limitaciones conocidas

- **Server-side tracking invisible**: pixels via Klaviyo CAPI o Elevar no aparecen en HTML público. Reportar como "probable activo via CAPI".
- **Apps detrás de auth**: portal de suscripciones, loyalty backend, partner tools no son detectables sin login.
- **Tier de revenue estimado**: el skill no tiene acceso a revenue real del prospect. Pedirle al usuario el tier estimado o inferir por # productos + tráfico Similarweb.
- **Tiendas headless**: si la tienda corre headless (Next.js consumiendo Shopify Storefront API), muchos signals no aparecen en HTML. Detectar como "headless" y limitar conclusiones.
