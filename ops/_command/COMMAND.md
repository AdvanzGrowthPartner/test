# Command de cada OS

Cada OS de área tiene **un** artifact propio: su tablero de mando, con las dos marcas adentro. Es lo primero que se abre para saber qué hacer en el área.

- **Título:** `<Área> OS · Command`, por ejemplo `Ads OS · Command`.
- **Tipo:** Dashboard de Artifacts (`type_url` https://claude.ai/artifact/GZLZthZ2sQjn7T16skfdeF). Se siguen las instrucciones que trae el tipo.
- **URL:** se guarda en `ops/<área>/command/URL` (una línea) y en `artifact_url` de los dos `os-data.json` del área.
- Los dashboards viejos por marca (`<Marca> · OS <Área>`) quedan congelados. No se actualizan más.

## Datos
`python3 ops/_command/exportar.py <área>` genera `ops/<área>/command/*.json`, que son arrays de filas, todas con la columna `marca`. Cada archivo se sube como dataset (archivo adjunto JSON) con el mismo id:

| Dataset | De dónde sale | Columnas clave |
|---|---|---|
| `kpis` | `kpis` de cada `os-data.json` | marca, nombre, valor, unidad, periodo, meta, estado (ok/warn/bad/sin-dato), fuente |
| `fugas` | `fugas` de cada `os-data.json`, ordenadas por severidad | marca, id, titulo, severidad, estado, accion, ejecuta, requiere_ok, acceso, evidencia |
| `handoffs` | `ops/handoffs.md`, pedidos abiertos para el área | marca, fecha, de, pedido |
| `accesos` | `accesos` de cada `os-data.json` | marca, conector, estado, nota |
| `cambios` | `CHANGELOG.md` de cada marca | marca, fecha, cambio, por_que, revertir |

## Página (en este orden)
1. **Selector de marca**: `Advanz` · `AmazingCare` · `Ambas` (parámetro `marca`, por defecto `Ambas`). Filtra todo lo de abajo.
2. **KPIs**: una fila de tarjetas por marca, con el valor, la unidad, el periodo y un chip de estado (ok, warn, bad o sin dato). Si hay meta, se muestra "meta X".
3. **Qué hacer ahora**: las fugas abiertas y en curso, ordenadas por severidad. Cada una muestra el título, la acción, quién la ejecuta, un chip **"Necesita tu OK"** cuando `requiere_ok` es verdadero y un chip de acceso (ok, sin conector, bloqueado). Las resueltas van al final, plegadas.
4. **Pedidos de otros OS**: los handoffs abiertos del área.
5. **Accesos**: una tabla de conector por marca con su estado. Lo bloqueado y lo sin conector va arriba.
6. **Últimos cambios**: los 10 más recientes, con "cómo revertir".

Va sin marketing y sin texto de relleno: es una herramienta de operación. Tiene que leerse bien al ancho de un teléfono.

## Refrescar (cada vez que el OS cierra trabajo)
1. `python3 ops/_command/exportar.py <área>`.
2. Por cada `ops/<área>/command/<dataset>.json` que cambió, súbelo como asset del Command y actualiza `datasets/<dataset>` con la nueva `url`, `name` y `updated`, como indica el tipo Dashboard.
3. Haz commit de los JSON junto con `estado.md` y `os-data.json`.
