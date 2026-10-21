# Command de cada OS

Cada OS (una marca × un área) tiene **un** artifact propio: su tablero de mando, **solo con datos de su marca**. Es lo primero que se abre para saber qué hacer en esa área y esa marca.

- **Título:** `<Área> OS · <Marca>`, por ejemplo `Ads OS · AmazingCare` o `Email OS · Advanz`.
- **Tipo:** Dashboard de Artifacts (`type_url` https://claude.ai/artifact/GZLZthZ2sQjn7T16skfdeF). Se siguen las instrucciones que trae el tipo.
- **URL:** se guarda en `ops/<marca>/<área>/command/URL` (una línea) y en `artifact_url` de `ops/<marca>/<área>/os-data.json`.
- **Nunca** se mezclan marcas en un Command. Los Command combinados del 21-oct quedan obsoletos.

## Datos
`python3 ops/_command/exportar.py <marca> <área>` genera `ops/<marca>/<área>/command/*.json`, que son arrays de filas. Cada archivo se sube como dataset (archivo adjunto JSON) con el mismo id:

| Dataset | De dónde sale | Columnas clave |
|---|---|---|
| `kpis` | `kpis` de `os-data.json` | nombre, valor, unidad, periodo, meta, estado (ok/warn/bad/sin-dato), fuente |
| `fugas` | `fugas` de `os-data.json`, ordenadas por severidad | id, titulo, severidad, estado, accion, ejecuta, requiere_ok, acceso, evidencia |
| `handoffs` | `ops/<marca>/handoffs.md`, pedidos abiertos para el área | fecha, de, pedido |
| `accesos` | `accesos` de `os-data.json` | conector, estado, nota |
| `cambios` | `CHANGELOG.md` | fecha, cambio, por_que, revertir |

## Página (en este orden)
1. **Encabezado** con la marca y el área, y la fecha de actualización de los datos.
2. **KPIs**: tarjetas con el valor, la unidad, el periodo y un chip de estado (ok, warn, bad o sin dato). Si hay meta, se muestra "meta X".
3. **Qué hacer ahora**: las fugas abiertas y en curso, ordenadas por severidad. Cada una muestra el título, la acción, quién la ejecuta, un chip **"Necesita tu OK"** cuando `requiere_ok` es verdadero y un chip de acceso (ok, sin conector, bloqueado). Las resueltas van al final, plegadas.
4. **Pedidos de otros OS**: los handoffs abiertos.
5. **Accesos**: lo bloqueado y lo sin conector va arriba.
6. **Últimos cambios**: los 10 más recientes, con "cómo revertir".

Va sin marketing y sin texto de relleno: es una herramienta de operación. Tiene que leerse bien al ancho de un teléfono.

## Refrescar (cada vez que el OS cierra trabajo)
1. `python3 ops/_command/exportar.py <marca> <área>`.
2. Por cada `ops/<marca>/<área>/command/<dataset>.json` que cambió, súbelo como asset del Command y actualiza `datasets/<dataset>` con la nueva `url`, `name` y `updated`, como indica el tipo Dashboard.
3. Haz commit de los JSON junto con `estado.md` y `os-data.json`.
