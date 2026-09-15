# Resellers / catálogos multi-producto — desafío, solución y tarifa

Conocimiento operativo del rol. Aplica cuando la tienda es un **reseller o catálogo heterogéneo**: ~15-20+ productos, o **3+ categorías**, donde cada producto tiene elementos 100% distintos (beneficios, objetivos, modo de uso, claims). Se detecta en la Fase 0 y condiciona el enfoque de PDP (Fase 1), la priorización/scoping (Fase 2) y la tarifa.

## El desafío
Cada producto es distinto, así que "hacer una plantilla por producto" lleva a **plantillas infinitas**: inmanejable, imposible de mantener, y cada nueva ficha requiere tiempo humano. El equipo termina abriendo una plantilla nueva por SKU.

## La solución: UNA plantilla dinámica, datos por producto (no plantillas infinitas)
El objetivo es un **formato automatizable** donde la proyección de beneficios/objetivos de cada producto vive en **datos estructurados**, y una sola sección los renderiza. Agregar un producto = llenar datos, **no** abrir una plantilla.

Arquitectura en Shopify:
1. **Esquema canónico de datos** (la "inmersión en la BBDD" que hace Advanz):
   - Metaobjects reutilizables para bloques repetibles: p. ej. `beneficio` (icono, título, texto), `objetivo`, `ingrediente`, `modo_uso`.
   - Metafields en el producto que referencian esos metaobjects (lista) + metafields simples (`custom.claim_principal`, `custom.publico_objetivo`).
   - Definir tipos con `metafieldDefinitions` (ver `store-blueprint.md` §5); mapear primero los atributos que YA existen para no duplicar.
2. **Una sección de producto dinámica** (`sections/main-product.liquid` o un bloque custom) que **itera** esos metafields/metaobjects y renderiza los bloques de beneficio/objetivo por producto. Si un producto no tiene un bloque, no se muestra — cero plantillas vacías.
3. **Variantes de layout acotadas, no infinitas**: si una categoría necesita un layout distinto (p. ej. suplemento vs. accesorio), usa **2-3 templates** de producto (`templates/product.suplemento.json`, `product.accesorio.json`) que comparten **la misma sección dinámica**. Nunca una plantilla por SKU.
4. **Carga a escala**: llenar/actualizar datos por CSV / Matrixify / `productUpdate` con metafields, no a mano ficha por ficha. Eso es lo que hace "automatizable" el formato.

Resultado: un producto nuevo se publica llenando su fila de datos; la ficha se arma sola con la plantilla dinámica. Sin tiempo humano por SKU, sin romper el resto.

Regla de no-romper (enlaza con `safe-implementation.md`): las rutas de metafield que la plantilla lee son contrato. Si migras a este esquema, **mapea y preserva** los metafields existentes antes de cambiar la sección; un cambio que renombre una ruta rompe todas las fichas a la vez.

## Detección automática del tramo (Fase 0)
Con `search_products` (conteo) y `search_collections` (nº y tipo) ya tienes lo necesario. Determina:
- **Nº de productos** → define el tramo de tarifa (tabla abajo).
- **Heterogeneidad**: ¿3+ categorías?, ¿los productos usan sets de metafields divergentes o comparten pocos? Alta heterogeneidad = candidato fuerte al esquema data-driven.
- Señal de "plantillas infinitas" ya existentes: muchos `templates/product.*.json` distintos en el Blueprint → bandera roja, es justo lo que este enfoque resuelve.

## Tarifa por gestión de productos / BBDD
Fee **extra** sobre el engagement base, por el trabajo de estructurar la BBDD y el formato automatizable. Tramos (normalizados sin solape):

| Productos | Fee extra | Enfoque |
|---|---|---|
| **1 – 5** | **$0** (sin aumento) | Plantilla estándar; no requiere gestión de BBDD |
| **6 – 10** | **+$300.000** | Esquema de datos + plantilla dinámica |
| **11 – 25** | **+$400.000** | + curado de colecciones/categorías |
| **26 – 2.000** | **+$600.000** | Personalización **limitada** (data-driven a escala) |
| **2.000+** | **Revisión con owner Shopify** | Caso a caso; no cotizar automático |

Supuestos usados por la skill (confirmar con el owner si cambian):
- Moneda **CLP** (contexto Chile). Si el engagement se cotiza en USD, ajustar.
- Es un fee de **gestión** que acompaña la migración/optimización; asumir **mensual** salvo indicación contraria. Si es one-time, marcarlo en la cotización.
- Los tramos originales venían solapados en 5 y 25; aquí quedan sin solape. Cambiar la tabla aquí si el owner define otra cosa — es la única fuente de verdad de estos números en la skill.

## Cómo lo usa la skill
- **Fase 0**: reporta nº de productos, heterogeneidad, tramo y fee correspondiente en el Blueprint.
- **Fase 1 (PDP)**: si es reseller/heterogéneo, recomienda el esquema data-driven en vez de más plantillas.
- **Fase 2**: incluye el fee del tramo en el scoping/roadmap; a partir de 26 productos aclara "personalización limitada"; en 2.000+ **no** cotiza — escala a revisión con owner Shopify.
- Nunca prometas personalización ilimitada sobre 26 productos ni cotices automático sobre 2.000: son las dos barreras que evitan romper el margen y el alcance.
