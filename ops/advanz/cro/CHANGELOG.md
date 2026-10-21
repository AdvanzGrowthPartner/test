# Changelog · Advanz OS CRO

Cambios aplicados en plataformas (lo más reciente arriba).

| Fecha | Cambio | Por qué | Cómo revertir |
|---|---|---|---|
| 2026-10-21 | Se creó el Command "CRO OS · Advanz" (https://claude.ai/artifact/3GJg2aU3AJRYjMcRmhM2rw), solo con datos de Advanz. `artifact_url` y `command/URL` apuntan ahí. El Command combinado (4Lbw3Q…) y el dashboard "Advanz · OS CRO" quedan congelados. | Spec `ops/_command/COMMAND.md`: un Command por marca y área | Volver `artifact_url` al Command anterior y borrar el artifact |
| 2026-10-21 | Se creó el artifact "CRO OS · Command" (https://claude.ai/artifact/4Lbw3Q7xcoAXmeFC1MVcZw) con las dos marcas; `artifact_url` de os-data.json apunta ahí. El dashboard anterior por marca queda congelado. | Spec `ops/_command/COMMAND.md`: un Command por área | Volver `artifact_url` al dashboard anterior y borrar el artifact |
| 2026-10-19 | Se creó `os-data.json` (contrato Command Center 1.0) y el Dashboard privado "Advanz · OS CRO" (https://claude.ai/artifact/JosGimV3RiLAsjf2qKdW3h). Ninguna plataforma modificada: solo lecturas en Shopify, Vercel y Ahrefs. | Handoff de advanz/growth: que Growth combine las fugas entre los OS | Borrar `os-data.json` (vuelve la semilla) y eliminar el artifact |
