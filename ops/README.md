# Ops · Mapa de los OS

La operación está **separada por marca**. Advanz y AmazingCare tienen cada una sus 6 OS (Email, Ads, CRO, Growth, Creative y GEO/SEO). Cada OS es una sesión fija con su propio Command (artifact) y su memoria en este repo.

```
ops/
├── _command/                    ← spec y exportador de los Command
├── advanz/                      ← marketing propio de Advanz (leads → llamadas → clientes)
│   ├── contexto-marca.md        ← quién es la marca (lo leen sus 6 OS)
│   ├── handoffs.md              ← pedidos entre los OS de Advanz
│   ├── growth/command-center/   ← consolidado de los 12 OS (lo mantiene Growth OS de Advanz)
│   └── <área>/
│       ├── CLAUDE.md            ← instrucciones del OS
│       ├── estado.md            ← dónde quedamos: estado, decisiones, pendientes
│       ├── os-data.json         ← KPIs, fugas y accesos (alimenta el Command)
│       ├── CHANGELOG.md         ← cambios aplicados + cómo revertir
│       └── command/             ← datos del Command + URL del artifact
└── amazingcare/                 ← cliente ecommerce (misma estructura)
```

## Los 6 OS de cada marca

| OS | Advanz | AmazingCare |
|---|---|---|
| **Email OS** | Nurturing, outbound, CRM | Flujos, campañas, retención (Klaviyo) |
| **Ads OS** | Ads de generación de leads | Meta y Google de performance |
| **CRO OS** | Landings, lead magnets, quiz | Tienda, PDP, checkout |
| **Growth OS** | Funnel comercial y pipeline | Reporting, KPIs y roadmap |
| **Creative OS** | Reels, carruseles y VSL | Creativos para ads, UGC y copies |
| **GEO/SEO OS** | Blog de advanz.cl y presencia en IA | Blog, Search Console y presencia en IA |

## Cómo operar
1. Abre el OS de la marca y el área (`ops/SESIONES.md`) y su Command.
2. Pide el cambio en lenguaje natural. El OS propone el cambio y **espera tu OK** antes de tocar la plataforma.
3. Aplica el cambio y lo registra en `CHANGELOG.md`. Después actualiza `estado.md` y el Command, y hace push.
4. Si el cambio toca otra área de la misma marca, deja un handoff en `ops/<marca>/handoffs.md`.

## Nombres y grupos
- **Grupo = marca** (`Advanz`, `AmazingCare`). En la app los grupos se arman a mano con **Projects**; ver `ops/SESIONES.md`.
- **Nombre de la sesión = área + OS**: `Email OS`, `Ads OS`, `CRO OS`, `Growth OS`, `Creative OS` y `GEO/SEO OS`.
- **Command = `<Área> OS · <Marca>`**, para distinguirlos en la galería de artifacts.
