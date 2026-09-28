# Notion Schema — 2 databases

Este skill usa 2 databases en Notion. Cada una tiene un propósito distinto.

---

## DB 1: `Shopify Tools Library` — tiendas analizadas

**ID**: `13ce4773-1586-4c99-8bec-ebae6dd77bff`
**URL**: https://www.notion.so/1ec7085864fd4a01a2665450729f56c7

**Propósito**: una fila por tienda analizada. Pattern library de stacks completos.

### Cuándo escribir
- Cada vez que se ejecuta análisis completo (modo activo o pasivo)
- Re-análisis de tienda ya existente → actualizar entrada existente, no duplicar

### Schema (campos principales)
- `Tienda` (title) — nombre de la marca
- `URL` (url) — URL pública
- `Vertical` (select) — Suplementos, Fashion, Wellness, etc.
- `País` (select) — Chile, USA, UK, etc.
- `Estado análisis` (select) — Pasivo / Activo (shadow buyer) / Parcial
- `Theme` (text) — nombre + customization level
- `# Apps detectadas` (number) — count confianza ≥75%
- `Costo mensual stack USD` (number) — suma estimada
- `Apps Reviews/Subscriptions/Bundles/Upsell/Email/SMS-Push/Search/Loyalty/Analytics/Chat` (multi_select)
- `Page builder` (select)
- `Pixels activos` (multi_select) — Meta, TikTok, GA4, GTM, etc.
- `Métodos pago LATAM` (multi_select)
- `Highlights replicables` (text) — top patterns transferibles
- `Anti-patterns` (text) — gaps + redundancias detectadas
- `UX Score` (number 1-5)
- `Funnel impact alto` (multi_select) — qué capas del Growth Engine cubre bien
- `Cliente Advanz candidato` (multi_select)
- `Customización theme` (select) — Vanilla / Moderate / Heavy

### Body de la página
Reporte estructurado del análisis. Plantilla en `report-template.md`.

---

## DB 2: `Shopify Apps Catalog` — catálogo de apps individuales

**ID**: `ecce7849-2386-430a-bfd7-4e2a229bf4cf`
**URL**: https://www.notion.so/03f8eb2d9b9f4922aac3dfa1687f773e

**Propósito**: una fila por app Shopify individual. Catálogo vivo con scoring y replicabilidad.

### Cuándo escribir
- Cuando se detecta una app NUEVA no presente en el catálogo
- Actualización: cuando una app ya en el catálogo se ve en otra tienda nueva (agregar a `Visto en tiendas`)

### Schema (campos principales)
- `App` (title) — nombre comercial
- `Categoría funcional` (select) — Reviews/UGC, Subscriptions, Bundles, etc.
- `URL App Store` (url)
- `Vendor site` (url)
- **Detection signatures**:
  - `Detection HTML signal` (text)
  - `Detection JS global` (text)
  - `Detection external domain` (text)
  - `Detection app block slug` (text)
- `Capa Growth Engine` (multi_select)
- `Costo USD/mes` (text) — rango/tiers
- `Modelo de precio` (select)
- `Impacto conversión` (select) — Alto +10% / Medio +3-8% / Bajo / Negativo / Compliance / Variable
- `Score ROI (1-5)` (number)
- `Replicabilidad` (select) — Liquid nativo / App free / Más barata / No reemplazable / Native Shopify
- `Cliente Advanz target` (multi_select) — clientes Advanz específicos + tags genéricos
- `Cuándo SÍ vale` (text)
- `Cuándo NO vale` (text)
- `Alternativas` (text)
- `Visto en tiendas` (multi_select)
- `False positive frecuente` (checkbox)
- `Notas detección` (text)
- `Estado` (select) — Verificado / Por validar / Deprecated

### Consulta típica desde el skill
```python
# Buscar app por nombre
app_data = notion_query(
    database="ecce7849-2386-430a-bfd7-4e2a229bf4cf",
    filter={"App": "Klaviyo"}
)
# Returns: score, capa, cuando_si, cuando_no, replicabilidad, alternativas
```

---

## Relación entre las 2 DBs

```
Tienda (Shopify Tools Library)
   ↓ contiene
[Klaviyo, Loox, PageFly, Kaching Bundles, Clarity, Subscriptions native]
   ↓ cada uno tiene metadata propia en
Shopify Apps Catalog
   ↑ que se enriquece con cada tienda nueva donde se detecte
```

El skill cruza ambas DBs:
- Tienda detectada con app X → buscar X en Apps Catalog → traer scoring + alternativas → enriquecer diagnóstico

---

## Cómo agregar entradas nuevas

### Tienda nueva
1. Ejecutar análisis completo (workflow 7 pasos del SKILL.md)
2. Crear página en `Shopify Tools Library` con todos los campos llenos
3. Body = reporte completo en formato markdown
4. Para cada app detectada, verificar si está en `Shopify Apps Catalog` → si no, agregar con `Estado="Por validar"`

### App nueva
1. Llenar campos obligatorios: `App`, `Categoría funcional`, `Detection HTML/JS/domain/app_block_slug` (al menos uno)
2. Llenar `Estado="Por validar"` (no `Verificado` hasta cross-validar en 2+ tiendas)
3. `Visto en tiendas` = la tienda donde se detectó por primera vez
4. Score ROI inicial estimado, ajustar con más data

### Re-validación periódica
Trimestralmente:
- Revisar apps con `Estado="Por validar"` y promover a `Verificado` si hay suficiente evidencia
- Marcar como `Deprecated` apps que ya no aparecen en análisis recientes
- Actualizar `Costo USD/mes` para apps con pricing changes
