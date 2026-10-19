# Ops · Mapa de los OS

Toda la operación corre desde Claude Code. Cada **OS** es una sesión fija + una carpeta en este repo con su memoria:

```
ops/
├── advanz/                 ← marketing propio de Advanz (leads → llamadas → clientes)
│   ├── contexto-marca.md   ← quién es la marca (lo leen todos los OS del grupo)
│   ├── handoffs.md         ← pedidos entre OS del grupo
│   └── <os>/
│       ├── CLAUDE.md       ← instrucciones del OS (misión, herramientas, skills, reglas)
│       ├── estado.md       ← dónde quedamos: estado, decisiones, pendientes
│       └── CHANGELOG.md    ← cambios aplicados en plataformas + cómo revertir
└── amazingcare/            ← cliente ecommerce (misma estructura)
```

## Los 6 OS

| OS | Qué cubre | Herramientas principales |
|---|---|---|
| **Email** | Flujos, campañas, segmentos, retención (AC) · nurturing, outbound, CRM (Advanz) | Klaviyo, Gmail, Shopify |
| **Ads** | Meta / Google: estructura, presupuesto, tracking, testing | Meta Ads, Semrush |
| **CRO** | Tienda/PDP/checkout (AC) · landings, lead magnets, quiz (Advanz) | Shopify, Vercel, navegador |
| **Growth** | Reporting, KPIs de negocio, command center, roadmap y priorización | Shopify analytics, Notion, Drive |
| **Creative** | Ángulos, hooks, UGC, estáticos, video, copies, sistema visual | Canva, Magnific, Pletor, Figma |
| **GEO/SEO** | SEO técnico/on-page, blog, Search Console, visibilidad en IA | Ahrefs, Semrush, Shopify blog |

**Growth** es el OS que prioriza: define qué hay que hacer y lo deriva a los otros OS vía `handoffs.md`. Los otros cinco OS ejecutan.

## Cómo operar
1. Abre la sesión del OS (ver `ops/SESIONES.md`) y pide el cambio en lenguaje natural: *"sube 20% el presupuesto de la campaña de electrolitos"*, *"arma el flujo de carrito abandonado"*.
2. El OS lee su contexto, propone el cambio y **espera tu OK** antes de tocar la plataforma.
3. Aplica el cambio, lo registra en `CHANGELOG.md`, actualiza `estado.md` y hace push.
4. Si el cambio toca otra área, deja un handoff y la sesión del otro OS lo toma.

## Nombres y grupos de sesión
- **Grupo = marca:** `Advanz` y `AmazingCare` (se arman en la app como Projects; ver `ops/SESIONES.md`).
- **Nombre = área/canal + OS:** `Email OS`, `Ads OS`, `CRO OS`, `Growth OS`, `Creative OS`, `GEO/SEO OS`.
- Etiquetas de respaldo: `grupo:<marca>`, `os:<área>`, `tipo:os`.
- Sesiones puntuales nuevas: `<Área> — <tema>` (ej. `Ads — Black Friday`), dentro del grupo de su marca.
