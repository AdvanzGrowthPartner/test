---
name: advanz-shopify-conversion-engine
description: Motor de conversión + implementación segura para tiendas Shopify propias o de cliente con acceso. MAPEA lo que ya está armado a mano (theme publicado y su pila de copias, apps, secciones, metafields), AUDITA la conversión por superficie (PDP, carrito, checkout, colecciones, home), detecta gaps vs. lo que un DTC necesita, y —si se autoriza— IMPLEMENTA en código Liquid y deploya SIN ROMPER (theme duplicado, QA de regresión, publish con aprobación humana, backup y rollback). Lee el store vivo por el MCP de Shopify (Admin GraphQL). Úsala cuando digan "audita mi tienda", "revisa el checkout/carrito/PDP/colecciones/home", "mejora la conversión", "qué le falta a mi tienda", "mapea cómo está construida", "arma esta colección", "toca el theme sin romper", "implementa este cambio", "deploy seguro", o peguen la URL de una tienda propia para auditar/mejorar con opción de ejecutar. Orquesta a shopify-detector, clarity-cro-audit, ecomm-intelligence, seo-geo y email-engine sin duplicarlas. SOLO Shopify DTC.
---

# Advanz — Shopify Conversion Engine

Este es el motor que va del **entender** al **ejecutar** sobre una tienda Shopify que controlamos (propia o de cliente con acceso). Su razón de existir es una frase del negocio: *"entender lo que ya está armado manualmente, aprender de eso, y hacer cambios futuros sin romper lo que funciona."*

Casi todo lo demás ya existe en la librería Advanz. Lo que **nadie** hacía hasta ahora, y es el corazón de esta skill:

1. **Leer la estructura real del theme vivo** (archivos Liquid, `templates/*.json`, secciones, bloques, metafields) — no solo la analítica ni el HTML renderizado.
2. **Implementar cambios de código y deployarlos con una disciplina de no-romper** que se pueda repetir mil veces sin miedo.
3. **Dejar memoria** de qué se cambió y por qué, para que la próxima corrida parta sabiendo cómo está construida la tienda.

Todo lo que sea CRO profundo, benchmark, SEO, email o detección de stack se **rutea** a la skill hermana correspondiente (ver `references/orchestration.md`). No lo reimplementes.

---

## Antes de empezar: identifica el MODO

No siempre hay que ejecutar código. Detecta la intención y elige:

| Modo | Cuándo | Fases que corres | ¿Toca código? |
|------|--------|------------------|---------------|
| **`blueprint`** | "mapea / entiende cómo está armada la tienda", "por qué hay tantos themes", "qué apps/secciones tenemos" | Fase 0 | No |
| **`audit`** (default) | "audita", "revisa el carrito/PDP/checkout/colecciones", "qué le falta", "mejora la conversión" | Fases 0 → 2 | No — entrega diagnóstico + roadmap |
| **`implement`** | "implementa este cambio", "arma esta colección", "toca el theme sin romper", "deploya" | Fases 0 → 4 | Sí — con las salvaguardas de la Fase 3 |

Si dudas, corre `audit` y ofrece pasar a `implement` sobre los hallazgos priorizados. **Nunca** saltes a implementar sin haber hecho el Blueprint (Fase 0): cambiar código sin saber qué está construido a mano es exactamente cómo se rompe una tienda.

---

## Fase 0 — BLUEPRINT: entender lo que ya está armado

Objetivo: un inventario fiel de *cómo está construida esta tienda hoy*, para que cualquier cambio la respete. Esta fase es obligatoria en todos los modos.

Sigue `references/store-blueprint.md` para las llamadas exactas (MCP + Admin GraphQL). El resumen de lo que tienes que reconstruir:

1. **Contexto del shop** — `get-shop-info` (plan, moneda, país, mercados). El plan define límites duros: p. ej. editar el `checkout.liquid` / Checkout Extensibility real requiere **Shopify Plus**; en planes normales el checkout es casi intocable (esto acota qué puedes proponer en esa superficie).
2. **Paisaje de themes** — lista TODOS los themes (`themes`), identifica el `MAIN` (publicado) y su **familia** (Dawn, Trade, Horizon…), y **lee la pila de copias/backups**. Una pila grande de "Copia de X", "[Backup]", "Pre Fix Carrito" es la huella del *"editar sin romper hecho a mano"*: nómbrala, no la ignores — dice qué se tocó antes y con miedo. Marca también los **artefactos de theme-apps** ("DO NOT DELETE …", "AVADA Assets …"): son apps que inyectan al theme y que un cambio puede pisar.
3. **Estructura de las superficies clave** — lee del theme MAIN: `templates/index.json`, `templates/product.json` (o `.liquid`), `templates/collection.json`, `templates/cart.json` y `config/settings_data.json`. De ahí sale el **orden de secciones y bloques** = la arquitectura de merchandising real. Anota qué secciones son nativas del theme vs. custom vs. bloques de app.
4. **Stack de apps** — para la inferencia pública rápida, **rutea a `advanz-shopify-detector`**. Complementa con lo visible por Admin API (canales, script tags, app embeds en templates). No repitas la lógica del detector aquí.
5. **Modelo de datos** — metafields y metaobjects en uso (producto/colección), selling plans (suscripciones), descuentos activos, mercados. Son "lo armado a mano" invisible en el HTML.
6. **Forma del catálogo** — nº de productos, nº y tipo de colecciones (smart vs. custom) vía `search_products` / `search_collections`.

**Entregable Fase 0 — Store Blueprint** (persistir en Notion vía `advanz-notion-builder`, esquema en `references/notion-schema.md`):
- Ficha: plan, theme publicado + familia, resumen del stack.
- Mapa de superficies: qué secciones/archivos componen home, PDP, colección, carrito.
- **Riesgos de construcción**: pila de themes sin limpiar, artefactos de app, secciones custom frágiles, personalizaciones que un cambio podría pisar.
- Zonas "no tocar sin cuidado" (lo muy customizado a mano).

---

## Fase 1 — AUDIT: conversión por superficie

Diagnostica cada superficie con `references/surface-playbooks.md`. Para cada superficie el playbook define: qué revisar, cómo se ve "bien" en DTC, los **límites de la plataforma/plan**, y a qué archivo/sección del Blueprint pertenece cada hallazgo (así el arreglo ya sabe dónde vive).

Superficies (en orden de impacto típico en conversión):

1. **PDP / ficha de producto** — la superficie con más apalancamiento.
2. **Carrito** (drawer o página) — dónde amazingcare ya tuvo un "Pre Fix Carrito".
3. **Checkout** — acotado por el plan; foco en lo editable (trust, express pay, upsell post-compra si hay app).
4. **Colecciones / PLP** — filtros, orden, merchandising, construcción de colecciones (smart rules vs. curado).
5. **Home / merchandising** — el hueco que ninguna skill cubría: jerarquía del hero, ruta a colección, bloques de prueba social.

**Datos de embudo reales**: no inventes tasas. Para medición de fugas y funnel (device, step drop-off) **rutea a `clarity-cro-audit`** (ShopifyQL + Clarity + su catálogo de 13 fugas). Esta skill consume ese diagnóstico; no reimplementa la medición.

Cada hallazgo se etiqueta: `superficie · severidad (alta/media/baja) · archivo/sección · ¿toca zona frágil del Blueprint?`.

---

## Fase 2 — GAPS & ROADMAP

1. **Gaps propios** = delta entre lo que hay hoy (Blueprint + Audit) y lo que un DTC de este tier necesita. Para el "debería" usa los benchmarks de **`advanz-ecomm-intelligence`** (no adivines cifras). Si el usuario quiere comparación contra rivales, **rutea a `ecomm-benchmark-agent`**.
2. **Prioriza** cada gap por tres ejes — el tercero es propio de este motor:
   - **Impacto** en conversión (usa el scoring de fugas de clarity si aplica).
   - **Esfuerzo** de implementación.
   - **Riesgo a lo ya construido** — ¿el cambio toca una sección custom, un bloque de app, o una zona "no tocar" del Blueprint? Alto riesgo = más QA y aprobación explícita.
3. **Roadmap**: lista ordenada de cambios, cada uno con superficie, hipótesis, archivos afectados, esfuerzo, riesgo y cómo se mediría el resultado.

**Entregable Fase 2**: reporte de conversión (diagnóstico + gaps + roadmap priorizado), en Notion con el estándar `advanz-notion-builder`. En modo `audit` este es el entregable final; ofrece pasar a `implement` sobre los ítems de bajo riesgo / alto impacto.

---

## Fase 3 — IMPLEMENT: cambiar el código sin romper

Aquí la skill escribe Liquid/JSON y deploya. Es poderoso y peligroso: **una escritura al theme equivocado tumba las ventas en vivo.** Por eso la disciplina de la Fase 3 no es negociable. El detalle mecánico (queries, mutations, ejemplos) está en `references/safe-implementation.md`; aquí van las reglas que **nunca** se rompen y el porqué:

1. **Nunca escribas al theme publicado (`role: MAIN`).** Todo cambio va a un **theme de trabajo** desatendido (unpublished). Motivo: el theme publicado es la tienda en vivo; editarlo es editar producción sin red.
2. **Trabaja sobre una copia del theme publicado**, no sobre el theme del store demo ni un backup viejo. La copia se crea duplicando el MAIN (en Admin, 1 clic, o documentado en el reference). Nómbrala con convención: `[WIP] Advanz <AAAA-MM-DD> <cambio-corto>`. Motivo: partir de una copia fiel del vivo garantiza que lo que pruebas es lo que se publicará.
3. **Lee antes de escribir.** Trae el contenido actual del archivo con la query de `files`, edítalo de forma **aditiva** (preferir settings/bloques de sección sobre hardcodear; envolver lo nuevo en un setting/flag cuando se pueda), y recién ahí `themeFilesUpsert` **al theme de trabajo**. Motivo: un upsert reemplaza el archivo completo; sin leer primero, borras trabajo manual existente.
4. **Respeta la familia del theme.** Usa el schema de secciones y los settings del theme (Trade, en amazingcare). No inventes clases ni pises el CSS del theme. Motivo: el theme fue armado a mano sobre esas convenciones; salirse de ellas es lo que "se ve roto".
5. **Preview + QA de regresión** contra el Blueprint antes de siquiera proponer publicar. Checklist mínima en el reference: add-to-cart funciona, el carrito custom sigue renderizando, secciones de app siguen vivas, no hay error Liquid, mobile OK, no se rompió lo que ya funcionaba. Motivo: "sin romper" se demuestra, no se asume.
6. **Publicar es una acción humana con aprobación explícita.** La skill **no** corre `themePublish` por iniciativa propia. Presenta el diff, el preview y el resultado del QA, y espera el OK. Motivo: publicar es irreversible en el sentido de que afecta ventas ya; la decisión es del dueño.
7. **Backup y rollback.** Antes de publicar, deja el MAIN actual como copia unpublished con fecha (mantener ≥14 días). El rollback = `themePublish` de ese backup. Motivo: es exactamente lo que el equipo ya hacía a mano ("Pre Fix Carrito [Backup]"); esta skill lo formaliza para que nunca falte.

Camino alternativo para un dev en su máquina (Shopify CLI: `shopify theme pull/push --theme <id> --unpublished`) también está documentado en el reference, para cuando el cambio es grande y conviene versionarlo en git.

---

## Fase 4 — LEARN & LOG: dejar memoria

El motor es útil de verdad cuando la corrida N+1 sabe lo que hizo la corrida N. Al cerrar cualquier `implement` (y al terminar un `audit`), actualiza en Notion (formato `advanz-notion-builder`, esquema en `references/notion-schema.md`):

- **Blueprint de la tienda** — refléjalo con los cambios (nuevas secciones, archivos tocados, apps).
- **Change / Decision Log** — una fila por cambio: fecha, superficie, archivos, hipótesis, qué se hizo, theme de trabajo + backup usados, resultado medido (si ya hay), y referencia de rollback.

La próxima corrida **lee esto primero** (parte de la Fase 0). Así "aprende de lo que hay" y no repropone algo ya probado ni pisa un arreglo anterior.

---

## Orquestación (no dupliques a las hermanas)

Ruteo resumido — detalle y reglas de frontera en `references/orchestration.md`:

| Necesidad | Skill |
|-----------|-------|
| Stack/apps de una tienda | `advanz-shopify-detector` |
| Medición de fugas CRO + funnel + QA/rollback (disciplina base) | `clarity-cro-audit` |
| Benchmarks / cifras "debería" | `advanz-ecomm-intelligence` |
| Comparación contra competidores | `ecomm-benchmark-agent` |
| SEO/GEO de PDP y colecciones, briefs de schema | `advanz-seo-geo-engine` |
| Recuperación off-site (carrito/browse abandonado) | `advanz-email-engine` |
| Contenido de blog | `advanz-shopify-blog-publisher` |
| Dónde encaja en la estrategia (8 etapas) | `advanz-growth-engine` |
| Formato de todo lo que va a Notion | `advanz-notion-builder` |

Frontera clave: **UI del carrito on-site = este motor / clarity; recuperación off-site = email-engine.** No re-narres las 8 etapas del Growth Engine; este motor *ejecuta* bajo sus etapas de CRO/Workflows.

---

## Archivos de referencia

- `references/store-blueprint.md` — Fase 0: llamadas exactas (MCP + Admin GraphQL) para mapear theme, apps, datos y catálogo.
- `references/surface-playbooks.md` — Fase 1: qué revisar por superficie (PDP, carrito, checkout, colecciones, home), "bien" DTC y límites.
- `references/safe-implementation.md` — Fase 3: protocolo de deploy sin romper, mutations de theme, QA de regresión, rollback, camino CLI.
- `references/orchestration.md` — ruteo a skills hermanas y reglas de frontera para no duplicar.
- `references/notion-schema.md` — esquema del Blueprint y del Change/Decision Log (la memoria).
