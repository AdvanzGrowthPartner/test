# Orquestación y reglas de frontera

Este motor es el director de orquesta del ciclo *entender → auditar → implementar* sobre una tienda que controlamos. Su valor es coordinar, no reimplementar. Antes de resolver algo tú mismo, pregunta: ¿ya hay una hermana que lo hace mejor?

## Tabla de ruteo
| Necesidad concreta | Rutea a | Qué le pides / qué NO haces tú |
|---|---|---|
| Detectar apps/theme/stack (inferencia pública) | `advanz-shopify-detector` | Le pides el veredicto de stack. No copies sus fingerprints ni su curl. |
| Medir fugas de conversión + funnel (device, drop-off) + disciplina QA/rollback | `clarity-cro-audit` | Es la base de medición y la disciplina de "duplicar theme / QA / rollback" que este motor extiende a build+deploy. Consume su catálogo de 13 fugas; no lo reimplementes. |
| Cifras / benchmarks "debería ser X" | `advanz-ecomm-intelligence` | Le pides el número de referencia por tier/vertical. No adivines tasas. |
| Comparar contra competidores | `ecomm-benchmark-agent` | Solo si el usuario quiere benchmark competitivo; entrega DOCX. |
| SEO/GEO de PDP y colecciones, briefs de schema/liquid | `advanz-seo-geo-engine` | Si el gap es de búsqueda/citación LLM o schema. Sus briefs técnicos se ejecutan con la Fase 3 de este motor. |
| Recuperación off-site (carrito/browse/post-compra) | `advanz-email-engine` | Todo lo que sea flujo de email/Klaviyo. |
| Contenido de blog | `advanz-shopify-blog-publisher` | Artículos con schema; no PDP ni colecciones. |
| Dónde encaja estratégicamente (8 etapas) | `advanz-growth-engine` | Para narrar la secuencia/propuesta. Este motor ejecuta bajo sus etapas de CRO/Workflows. |
| Formato de todo lo que va a Notion | `advanz-notion-builder` | Blueprint, reporte y changelog salen con su estándar. |

## Reglas de frontera (evitar colisión)
1. **Carrito: on-site vs off-site.** La UI del carrito/drawer (código del theme) = este motor + clarity. La recuperación por email = `email-engine`. No armes flujos de email aquí.
2. **CRO: medir vs. construir.** `clarity-cro-audit` mide y recomienda (con su regla de "exponer, no escribir"). Este motor toma esos hallazgos y **sí** implementa/deploya, con las salvaguardas de la Fase 3. No dupliques la detección de fugas: cítala.
3. **Growth Engine.** No re-narres las 8 etapas ni el flywheel. Si el usuario pide estrategia/secuencia, rutea a `growth-engine`; este motor es el brazo ejecutor de la capa CRO/Workflows.
4. **PDP desde tres ángulos.** Conocimiento/benchmark → `ecomm-intelligence`; búsqueda/GEO → `seo-geo`; diagnóstico y build en vivo → este motor. Elige por intención, no corras las tres.
5. **Detector vs. este motor.** Scouting de una tienda que NO controlas (sin acceso admin) → `shopify-detector`. Entender/auditar/ejecutar sobre una tienda con acceso (propia o cliente) → este motor (que igual llama al detector para el stack).
6. **Contenido dual SEO/GEO** ya vive en `seo-geo` y `blog-publisher`. No agregues una tercera copia del patrón.

## Cómo invocar a una hermana
Nómbrala explícitamente en tu plan ("para el stack corro `advanz-shopify-detector`; para las cifras de referencia, `advanz-ecomm-intelligence`") y entrega su salida integrada en el reporte, sin re-derivarla. Si una hermana no está disponible en la sesión, dilo y sigue con lo que sí puedes, marcando el hueco.
