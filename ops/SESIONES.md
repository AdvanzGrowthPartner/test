# Índice de sesiones

Separado por marca. Cada marca tiene sus 6 OS, y cada OS tiene su Command, que muestra solo esa marca.

## Advanz

| Sesión | Command | Carpeta |
|---|---|---|
| [Email OS](https://claude.ai/code/session_01RWXdYvdkBSjz3AMKNi45bR) | [Email OS · Advanz](https://claude.ai/artifact/RDdvnsPtwXTKgerJWTriZs) | `ops/advanz/email/` |
| [Ads OS](https://claude.ai/code/session_01NRwmKqff5GE8sf8kbvcXQ4) | [Ads OS · Advanz](https://claude.ai/artifact/VoTvJuaJ7p6bdhGGzobSvC) | `ops/advanz/ads/` |
| [CRO OS](https://claude.ai/code/session_015JAuUwVRTEGJao24pQNXV9) | [CRO OS · Advanz](https://claude.ai/artifact/3GJg2aU3AJRYjMcRmhM2rw) | `ops/advanz/cro/` |
| [Growth OS](https://claude.ai/code/session_01HJcK5B9TkhrWRzVMacNcHM) | [Growth OS · Advanz](https://claude.ai/artifact/7qL12oAKhA3sgqgspnGrR5) | `ops/advanz/growth/` |
| [Creative OS](https://claude.ai/code/session_01AFgDnGY7uftMsHqZGhdSpb) | `Creative OS · Advanz` (URL en `ops/advanz/creative/command/URL`) | `ops/advanz/creative/` |
| [GEO/SEO OS](https://claude.ai/code/session_018Wd9wcnCba8vsnDnWzzF7k) | [GEO/SEO OS · Advanz](https://claude.ai/artifact/BWRXxdf18LTzm3iBu5SUwS) | `ops/advanz/geo-seo/` |

## AmazingCare

| Sesión | Command | Carpeta |
|---|---|---|
| [Email OS](https://claude.ai/code/session_016wdGkE6sAqWwmG2ZRfbjWo) | [Email OS · AmazingCare](https://claude.ai/artifact/RhKD7ygrYif6epFeNkYgtA) | `ops/amazingcare/email/` |
| [Ads OS](https://claude.ai/code/session_01GyAic6oByAumjSDeDms9Qy) | [Ads OS · AmazingCare](https://claude.ai/artifact/TqGTThsQCy2zoCAomDkt5k) | `ops/amazingcare/ads/` |
| [CRO OS](https://claude.ai/code/session_01E2WodPnkSH788pKwwxWygE) | [CRO OS · AmazingCare](https://claude.ai/artifact/Dc1qxXa6SRSnEhv6x2ERFY) | `ops/amazingcare/cro/` |
| [Growth OS](https://claude.ai/code/session_01Wju5Ux2p2ECNEeqmoGN39Y) | [Growth OS · AmazingCare](https://claude.ai/artifact/AaQ652nEWo7t2cMSyruyfv) | `ops/amazingcare/growth/` |
| [Creative OS](https://claude.ai/code/session_01W3actBkSkCVQDdJpPxHesx) | [Creative OS · AmazingCare](https://claude.ai/artifact/GXrYePKXhZf99tCa7qu6h3) | `ops/amazingcare/creative/` |
| [GEO/SEO OS](https://claude.ai/code/session_01BGkyj7SY2YcCd8cpbwhKj2) | `GEO/SEO OS · AmazingCare` (URL en `ops/amazingcare/geo-seo/command/URL`) | `ops/amazingcare/geo-seo/` |

## Armar los grupos en la app (una vez)
La app no permite asignar grupos desde una API, así que hay que hacerlo a mano:
1. En claude.ai/code, en el sidebar, entra a **Projects** y crea `Advanz` y `AmazingCare`.
2. Entra a cada sesión con los links de arriba, abre el menú (⋯) y usa **Move to project** para moverla al proyecto de su marca.

Etiquetas de respaldo en cada sesión: `grupo:<marca>`, `os:<área>` y `tipo:os`.

Sesiones puntuales activas:
- [Email — Klaviyo-Loox recuperación y reseñas (AmazingCare)](https://claude.ai/code/session_01U4wHUAdzXad6pDszrQihiw). Sus hallazgos quedaron en `ops/amazingcare/handoffs.md`.

## Legacy
- **2026-10-21:** 6 OS por área que mezclaban las dos marcas, con su Command combinado. Se archivaron con la etiqueta `legacy:2026-10-21-mezclado`. Sus cambios útiles siguen en el repo: el CHANGELOG de GEO/SEO AmazingCare como tabla y el `os-data.json` de Creative Advanz.
- **2026-10-19:** 58 sesiones viejas, archivadas con la etiqueta `legacy:2026-10-19`, entre ellas las de otros clientes y las de infraestructura. Lo útil quedó en `contexto-marca.md` y en cada `estado.md`.
