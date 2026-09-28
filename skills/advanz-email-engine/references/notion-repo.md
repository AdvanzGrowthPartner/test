# Repo del Email Engine en Notion

Estructura jerárquica bajo la página **Email Marketing** del workspace advanzgrowthpartner. El objetivo: que cualquier duda mañana se corrija en el repo, sin reconstruir nada.

## Jerarquía

```
Email Marketing (página raíz existente)
└── 📧 Email Engine (página índice)
    ├── [diagrama global + flywheel + dependencias]
    ├── [tabla de las 8 fases]
    ├── [tabla de escalamiento por facturación]
    │
    ├── 1 · Captura & Base
    │   ├── [Mermaid de la fase]
    │   ├── Captura de lista
    │   ├── Segmentación por intención
    │   └── Setup de deliverability
    │
    ├── 2 · Bienvenida
    │   ├── [Mermaid de la fase]
    │   ├── Welcome Series
    │   └── Bundle / producto de entrada
    │
    ├── 3 · Validación
    │   ├── [Mermaid]
    │   ├── A/B de asunto y oferta
    │   └── Quiz / zero-party data
    │
    ├── 4 · Alcance
    │   ├── [Mermaid]
    │   ├── Campañas (calendario)
    │   └── Browse Abandonment
    │
    ├── 5 · Conversión
    │   ├── [Mermaid]
    │   ├── Carrito Abandonado
    │   └── Checkout Abandonado
    │
    ├── 6 · Retención
    │   ├── [Mermaid]
    │   ├── Post-Compra / Recompra
    │   ├── Referidos · regala a un amigo
    │   └── Suscripción
    │
    ├── 7 · Feedback
    │   ├── [Mermaid]
    │   ├── Solicitud de review / UGC
    │   └── Win-back + Sunset
    │
    ├── 8 · Sistema
    │   ├── [Mermaid]
    │   ├── Automatizar lo validado
    │   └── Reporting → próxima vuelta
    │
    ├── 🎚️ Escalamiento por facturación (página)
    └── 🧭 Cómo se conecta con el Growth Engine (página)
```

## Plantilla de cada página de acción

Cada una de las 18 acciones vive como página propia con esta estructura estándar (callout de tipo arriba, luego secciones):

```
[Callout] Tipo: {etiquetas} · Fase {N} · {nombre fase}

## Qué es
{párrafo}

## Qué necesita
- {bullet} ...

## Nivel de dificultad
{Baja/Media/Alta} · {quién lo ejecuta}

## Métricas promedio
| Métrica | Valor |

## Tiempo y carga de equipo
- Setup: {h}
- Mantención: {h/mes}
[Callout] {ehint: cuándo pide más manos}

## Checklist de implementación
- [ ] ...

## Do's & Don'ts
✓ Hacer: ...
✕ Evitar: ...

## Cómo se conecta con el engine
- {área}: {por qué}

## Ejemplo de correo
{descripción del mock / secuencia}

## Aparece desde
{nivel de facturación donde entra}
```

La fuente de verdad para llenar cada página es `references/flujos.md`.

## Cómo construirlo con el MCP de Notion

1. **Buscar la página raíz.** Usa `notion-fetch` con la URL de Email Marketing para obtener su ID.
2. **Crear la página índice** "📧 Email Engine" como hija, con los diagramas globales y las tablas.
3. **Crear las 8 páginas de fase** como hijas del índice. En cada una, pegar el Mermaid de esa fase (bloque `code` con lenguaje `mermaid`).
4. **Crear las 18 páginas de acción** como hijas de su fase, cada una con la plantilla de arriba llenada desde `flujos.md`.
5. **Crear las 2 páginas transversales** (escalamiento, conexión con el engine).

**Nota técnica sobre Mermaid en Notion:** Notion renderiza Mermaid dentro de un bloque de código con el lenguaje fijado en `mermaid`. Al crear vía MCP, se inserta como code block con `language: "mermaid"`. Si el MCP no soporta fijar el lenguaje directamente, se crea el code block y se deja indicado para ajustar el lenguaje a mano (1 clic por bloque).

## Mantenimiento

- **Una duda / corrección = una edición en la página de esa acción.** No se toca el resto.
- Si cambia un benchmark, se actualiza en la página de la acción y en `flujos.md` de la skill (mantener ambos sincronizados).
- Si se agrega una acción nueva, se crea su página bajo la fase que corresponda y se actualiza la tabla de escalamiento.
- El HTML interactivo (`assets/email-engine-madurez.html`) se adjunta como archivo o embed en la página índice para uso en vivo con clientes.
