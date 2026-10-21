# Ops · Mapa de los OS

Toda la operación corre desde Claude Code con **6 OS, uno por área**. Cada OS es una sesión fija (`<Área> OS`) y atiende a las dos marcas. Su memoria vive en este repo y su tablero de mando es el artifact `<Área> OS · Command`.

```
ops/
├── marcas/
│   ├── advanz.md            ← quién es Advanz (marketing propio: leads → llamadas → clientes)
│   └── amazingcare.md       ← quién es AmazingCare (cliente ecommerce)
├── handoffs.md              ← pedidos entre OS
├── _command/                ← spec y exportador de los Command
├── <área>/                  ← email · ads · cro · growth · creative · geo-seo
│   ├── CLAUDE.md            ← instrucciones del OS (misión por marca, herramientas, skills, reglas)
│   ├── command/             ← datos del Command (generados) + URL del artifact
│   ├── advanz/
│   │   ├── estado.md        ← dónde quedamos: estado, decisiones, pendientes
│   │   ├── os-data.json     ← KPIs, fugas y accesos (contrato del Command Center)
│   │   └── CHANGELOG.md     ← cambios aplicados + cómo revertir
│   └── amazingcare/         ← misma estructura
└── growth/command-center/   ← consolidado global de los 6 OS (lo mantiene Growth OS)
```

## Los 6 OS

| OS | Qué cubre | Herramientas principales |
|---|---|---|
| **Email OS** | Flujos, campañas y retención (AmazingCare). Nurturing, outbound y CRM (Advanz) | Klaviyo, Gmail, Shopify |
| **Ads OS** | Meta y Google: estructura, presupuesto, tracking y testing | Meta Ads, export de Google Ads |
| **CRO OS** | Tienda, PDP y checkout (AmazingCare). Landings, lead magnets y quiz (Advanz) | Shopify, Vercel, navegador |
| **Growth OS** | Reporting, KPIs de negocio, roadmap y priorización entre áreas | Shopify analytics, Notion, Drive |
| **Creative OS** | Ángulos, hooks, UGC, estáticos, video, copies y sistema visual | Canva, Magnific, Pletor, Figma |
| **GEO/SEO OS** | SEO, blog, Search Console y visibilidad en IA | Notion, Search Console, Shopify blog |

**Growth OS** prioriza: mantiene el Command Center global y deriva el trabajo a los otros OS a través de `handoffs.md`.

## Cómo operar
1. Abre el OS del área (`ops/SESIONES.md`) y su Command para ver qué hay pendiente en cada marca.
2. Pide el cambio indicando la marca. Por ejemplo: *"AmazingCare: reactiva Pack_P6 con $10 USD/día"* o *"Advanz: arma la secuencia de follow-up del diagnóstico"*.
3. El OS propone el cambio y **espera tu OK** antes de tocar la plataforma.
4. Aplica el cambio y lo registra en `CHANGELOG.md`. Después actualiza `estado.md` y `os-data.json`, refresca el Command y hace push.

## Nombres de sesión
- Los OS se llaman `Email OS`, `Ads OS`, `CRO OS`, `Growth OS`, `Creative OS` y `GEO/SEO OS`.
- Una sesión puntual nueva se nombra `<Área> — <tema>` (por ejemplo `Ads — Black Friday AmazingCare`) y deja su resultado en la carpeta del área.
