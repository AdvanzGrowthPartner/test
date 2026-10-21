# Changelog · Advanz OS CRO

Cambios aplicados en plataformas (lo más reciente arriba).

| Fecha | Cambio | Por qué | Cómo revertir |
|---|---|---|---|

## 2026-10-19 · Arranque del OS y artifact del Command Center
- **Qué**: se creó `os-data.json` (contrato Command Center 1.0) y el Dashboard privado "Advanz · OS CRO" (https://claude.ai/artifact/JosGimV3RiLAsjf2qKdW3h). Handoff de advanz/growth.
- **Por qué**: para que Growth combine las fugas entre los OS.
- **Plataformas**: ninguna modificada; en Shopify, Vercel y Ahrefs solo se hicieron lecturas.
- **Revertir**: borrar `os-data.json` (el Command Center vuelve a usar la semilla) y eliminar el artifact.
