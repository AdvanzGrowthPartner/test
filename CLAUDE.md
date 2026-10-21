# Advanz Ops

Este repo es la base de operación de Advanz desde Claude Code. La operación está **separada por marca**: cada marca tiene sus propios 6 OS, y un OS nunca mezcla datos ni decisiones de la otra marca.

| Marca | Email | Ads | CRO | Growth | Creative | GEO/SEO |
|---|---|---|---|---|---|---|
| **Advanz** (marketing propio) | `ops/advanz/email` | `ops/advanz/ads` | `ops/advanz/cro` | `ops/advanz/growth` | `ops/advanz/creative` | `ops/advanz/geo-seo` |
| **AmazingCare** (cliente) | `ops/amazingcare/email` | `ops/amazingcare/ads` | `ops/amazingcare/cro` | `ops/amazingcare/growth` | `ops/amazingcare/creative` | `ops/amazingcare/geo-seo` |

## Enrutamiento
- Cada sesión OS se llama `<Área> OS` y su system prompt dice de qué marca es. **Antes de hacer cualquier cosa**, lee `ops/<marca>/<área>/CLAUDE.md` y sigue sus instrucciones.
- Si la sesión no tiene un OS asignado, identifica la marca y el área por la tarea y lee ese `CLAUDE.md`.
- Cada OS tiene su artifact **`<Área> OS · <Marca>`**, con los datos de una sola marca (spec en `ops/_command/COMMAND.md`).
- Mapa completo: `ops/README.md`. Índice de sesiones: `ops/SESIONES.md`.

## Reglas globales
- Nada que gaste plata, publique o envíe (activar ads, cambiar presupuestos, enviar emails, publicar en la tienda o en el blog) se ejecuta sin OK explícito del usuario.
- Todo cambio aplicado se registra en el `CHANGELOG.md` del OS.
- Al cerrar el trabajo se actualizan `estado.md` y el Command, y luego se hace commit y push.
- Nunca se guardan secretos (tokens, keys, contraseñas) en el repo.
- Todas las sesiones OS comparten el branch de trabajo `claude/beautiful-bohr-sme4vz`. Antes de hacer push, corre `git pull --rebase origin claude/beautiful-bohr-sme4vz`. Cada OS edita solo su carpeta `ops/<marca>/<área>/`, más `ops/<marca>/handoffs.md` cuando corresponde.
- Idioma de trabajo: español (Chile).
