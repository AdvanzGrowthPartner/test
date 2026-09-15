# Fase 0 — Store Blueprint (llamadas exactas)

Objetivo: reconstruir *cómo está construida la tienda hoy* antes de tocar nada. Todo vía el MCP de Shopify (tienda conectada) o `switch-shop` si trabajas otra. Antes de cualquier GraphQL nuevo: `graphql_schema` → `validate_graphql_codeblocks` → ejecutar. Los nombres de tipos/mutations de este archivo están verificados contra Admin API 2024-10+.

## Índice
1. Contexto del shop
2. Paisaje de themes (y la pila de copias)
3. Lectura de la estructura de superficies
4. Stack de apps
5. Modelo de datos (metafields, selling plans, descuentos, mercados)
6. Forma del catálogo
7. Qué armar como entregable

---

## 1. Contexto del shop
`get-shop-info` → plan, moneda, país, timezone.

**Límites por plan (acotan qué se puede proponer):**
- Checkout: editar `checkout.liquid` o usar Checkout Extensibility real → **Shopify Plus**. En plan Shopify normal el checkout es prácticamente intocable salvo lo que permita el editor y las apps. No propongas cambios de código de checkout fuera de Plus.
- Scripts / Functions (descuentos, envío) → capacidades distintas por plan.
- Markets/multi-moneda → afecta precios y traducciones que un cambio de theme debe respetar.

## 2. Paisaje de themes
```graphql
query Themes {
  themes(first: 50) {
    nodes { id name role prefix processing themeStoreId updatedAt }
  }
}
```
- `role: MAIN` = **publicado = tienda en vivo**. Es el único que NUNCA se edita directo.
- `themeStoreId` mapea a la familia (ej. Trade=2699, Dawn=887, Horizon=2481). Identifica la familia: define el schema de secciones y settings que tus cambios deben respetar.
- **Lee la pila de copias.** Nombres tipo `Copia de X`, `[Backup]`, `Pre Fix Carrito`, fechas → huella del "editar sin romper a mano". Repórtala como riesgo (themes sin limpiar confunden y ocupan cuota) y como pista (qué se tocó antes y con miedo).
- **Artefactos de theme-apps**: `DO NOT DELETE - …`, `… Assets - DO NOT REMOVE`, `Section Store Demo` → apps que inyectan al theme; un cambio puede pisarlas. Márcalas.

## 3. Estructura de las superficies (leer archivos del theme MAIN)
La lectura de contenido de archivos usa `theme(id).files`. El `body` es una UNION:

```graphql
query ThemeFiles($id: ID!, $names: [String!]!) {
  theme(id: $id) {
    name role
    files(filenames: $names, first: 50) {
      nodes {
        filename
        contentType
        size
        body {
          ... on OnlineStoreThemeFileBodyText { content }
          ... on OnlineStoreThemeFileBodyBase64 { contentBase64 }
          ... on OnlineStoreThemeFileBodyUrl { url }
        }
      }
    }
  }
}
```
Variables típicas para mapear superficies (usa el `id` del MAIN):
```json
{ "id": "gid://shopify/OnlineStoreTheme/<MAIN_ID>",
  "names": ["templates/index.json","templates/product.json","templates/product.*.json",
            "templates/collection.json","templates/cart.json","config/settings_data.json"] }
```
- Los `templates/*.json` traen `sections` + `order` = **el orden real de secciones y bloques** de cada superficie. Eso es la arquitectura de merchandising.
- Si el template es `.liquid` (no `.json`), el theme es más viejo/custom → los cambios son más manuales y frágiles: anótalo.
- Puedes traer una sección concreta luego: `sections/main-product.liquid`, `sections/featured-collection.liquid`, etc. Usa `*` para listar (`"sections/*"`) y ver qué secciones custom existen.
- `config/settings_data.json` = configuración viva del theme (colores, tipografías, toggles). No lo pises: un cambio ahí afecta todo.

Registra, por superficie (home, PDP, colección, carrito): qué secciones la componen, cuáles son nativas del theme, cuáles custom, cuáles bloques de app.

## 4. Stack de apps
- Inferencia pública rápida → **rutea a `advanz-shopify-detector`** (no repliques su lógica de fingerprints).
- Complemento por Admin API donde aporte: canales de venta / publicaciones, y app embeds visibles en los templates leídos (bloques `@app` en el `order`, snippets de app).

## 5. Modelo de datos ("lo armado a mano" invisible)
- **Metafields / metaobjects** en producto y colección — definiciones:
```graphql
query MetafieldDefs {
  productDefs: metafieldDefinitions(first: 50, ownerType: PRODUCT) { nodes { namespace key name type { name } } }
  collectionDefs: metafieldDefinitions(first: 50, ownerType: COLLECTION) { nodes { namespace key name type { name } } }
}
```
Los metafields suelen alimentar secciones custom de la PDP (ingredientes, modo de uso, FAQ). Un cambio de theme que ignore un metafield rompe esos bloques.
- **Selling plans** (suscripciones) — si existen, la PDP y el carrito tienen lógica extra que no se puede romper.
- **Descuentos** activos (`discountNodes`) y **markets** (moneda/idioma por mercado).

## 6. Forma del catálogo
- `search_products` → nº de productos, estados, tipos.
- `search_collections` → nº y tipo (`collection_type:custom` vs `smart`). Las smart tienen reglas; las custom son curado manual. Esto importa para la Fase de colecciones.
- **Tramo reseller**: con el nº de productos y de categorías, determina si es un caso multi-producto y qué **tramo de tarifa** aplica. Chequea también heterogeneidad (¿muchos `templates/product.*.json` distintos? = "plantillas infinitas", bandera roja). Detección, arquitectura data-driven y tabla de tarifas en `reseller-scaling.md`.

## 7. Entregable
Store Blueprint (a Notion, esquema en `notion-schema.md`):
- Ficha: plan, moneda, theme publicado + familia, resumen de stack.
- Mapa de superficies → secciones/archivos.
- Modelo de datos: metafields/metaobjects, selling plans, descuentos, markets.
- **Riesgos de construcción** y **zonas "no tocar sin cuidado"** (secciones custom frágiles, bloques de app, config del theme).
