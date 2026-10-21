# Advanz Ops

Este repo es la base de operación de Advanz desde Claude Code. La operación se divide en **6 OS por área**. Cada OS atiende a las dos marcas: **Advanz** (marketing propio) y **AmazingCare** (cliente).

| OS (sesión) | Carpeta | Marcas |
|---|---|---|
| Email OS | `ops/email/` | `advanz/` · `amazingcare/` |
| Ads OS | `ops/ads/` | `advanz/` · `amazingcare/` |
| CRO OS | `ops/cro/` | `advanz/` · `amazingcare/` |
| Growth OS | `ops/growth/` | `advanz/` · `amazingcare/` (y el Command Center global) |
| Creative OS | `ops/creative/` | `advanz/` · `amazingcare/` |
| GEO/SEO OS | `ops/geo-seo/` | `advanz/` · `amazingcare/` |

Contexto de cada marca: `ops/marcas/advanz.md` y `ops/marcas/amazingcare.md`. Pedidos entre OS: `ops/handoffs.md`.

## Enrutamiento
- Si la sesión se llama `<Área> OS` (ej. `Ads OS`), **antes de hacer cualquier cosa** lee `ops/<área>/CLAUDE.md` y sigue sus instrucciones.
- Si no tiene OS asignado, identifica el área por la tarea y lee ese `CLAUDE.md`.
- Cada OS tiene su artifact **`<Área> OS · Command`** (especificación en `ops/_command/COMMAND.md`).
- Mapa completo: `ops/README.md`. Índice de sesiones: `ops/SESIONES.md`.

## Reglas globales
- Nada que gaste plata, publique o envíe (activar ads, cambiar presupuestos, enviar emails, publicar en la tienda o en el blog) se ejecuta sin OK explícito del usuario.
- Todo cambio aplicado se registra en el `CHANGELOG.md` del OS.
- Al cerrar el trabajo se actualiza `estado.md`, y luego se hace commit y push.
- Nunca se guardan secretos (tokens, keys, contraseñas) en el repo.
- Todas las sesiones OS comparten el branch de trabajo `claude/beautiful-bohr-sme4vz`. Antes de hacer push, corre `git pull --rebase origin claude/beautiful-bohr-sme4vz`. Cada OS edita solo su carpeta `ops/<área>/`, más `ops/handoffs.md` cuando corresponde.
- Idioma de trabajo: español (Chile).
