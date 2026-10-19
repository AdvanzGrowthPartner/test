# Advanz Ops

Este repo es la base de operación de Advanz desde Claude Code. La operación se divide en **2 grupos × 6 OS**:

| Grupo | Email | Ads | CRO | Growth | Creative | GEO/SEO |
|---|---|---|---|---|---|---|
| **Advanz** (marketing propio) | `ops/advanz/email` | `ops/advanz/ads` | `ops/advanz/cro` | `ops/advanz/growth` | `ops/advanz/creative` | `ops/advanz/geo-seo` |
| **AmazingCare** (cliente) | `ops/amazingcare/email` | `ops/amazingcare/ads` | `ops/amazingcare/cro` | `ops/amazingcare/growth` | `ops/amazingcare/creative` | `ops/amazingcare/geo-seo` |

## Enrutamiento
- Las sesiones OS se llaman `<Área> OS` (ej. `Ads OS`); la marca no va en el nombre sino en el grupo (Advanz / AmazingCare) y en el system prompt de la sesión. **Antes de hacer cualquier cosa**, lee `ops/<grupo>/<área>/CLAUDE.md` del grupo indicado en tu system prompt y sigue sus instrucciones.
- Si no tiene OS asignado, identifica grupo y área por la tarea y lee ese `CLAUDE.md`.
- Mapa completo y reglas: `ops/README.md`. Índice de sesiones: `ops/SESIONES.md`.

## Reglas globales
- Nada que gaste plata, publique o envíe (activar ads, cambiar presupuestos, enviar emails, publicar en la tienda o en el blog) se ejecuta sin OK explícito del usuario.
- Todo cambio aplicado se registra en el `CHANGELOG.md` del OS.
- Al cerrar el trabajo se actualiza `estado.md`, y luego se hace commit y push.
- Nunca se guardan secretos (tokens, keys, contraseñas) en el repo.
- Todas las sesiones OS comparten el branch de trabajo `claude/beautiful-bohr-sme4vz`. Antes de hacer push, corre `git pull --rebase origin claude/beautiful-bohr-sme4vz`. Cada OS edita solo su carpeta, más `handoffs.md` cuando corresponde.
- Idioma de trabajo: español (Chile).
