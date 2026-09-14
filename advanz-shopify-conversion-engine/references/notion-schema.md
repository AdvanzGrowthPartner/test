# Notion — Blueprint + Change/Decision Log (la memoria)

La skill sirve de verdad cuando la corrida N+1 sabe lo que hizo la N. Toda persistencia usa el estándar visual de `advanz-notion-builder` (TL;DR → índice → Mermaid horizontal → contenido escaneable → detalle en toggles). Formato = notion-builder; contenido = este esquema.

Al iniciar la Fase 0, **lee estas dos DBs primero**: si ya existe Blueprint/Log de la tienda, parte de ahí (no repropongas lo ya hecho, no pises un arreglo anterior).

## DB 1 — Store Blueprints (una página por tienda)
Propiedades:
- **Tienda** (title) — ej. "Amazing Care (amazingcare.cl)"
- **Plan / Moneda / País**
- **Theme publicado** — nombre + familia + id
- **Última corrida** (date) · **Modo** (blueprint/audit/implement)
- **Estado de riesgo** (select: limpio / desordenado / crítico) — p. ej. muchas copias de theme sin limpiar

Cuerpo de la página:
1. **TL;DR** — cómo está construida la tienda en 3 líneas.
2. **Mapa de superficies** (tabla): superficie → template → secciones (nativa/custom/app).
3. **Stack** (resumen del detector) y **modelo de datos** (metafields, selling plans, descuentos, markets).
4. **Paisaje de themes** (toggle): MAIN + pila de copias/backups + artefactos de app, con lectura de qué revela.
5. **Zonas "no tocar sin cuidado"** (callout): secciones custom frágiles, bloques de app, carrito intervenido.

## DB 2 — Change / Decision Log (una fila por cambio)
Es el registro que hace segura la iteración. Propiedades:
- **Cambio** (title) — ej. "PDP: barra de envío gratis en drawer"
- **Tienda** (relation → Blueprint)
- **Fecha** (date) · **Superficie** (select) · **Estado** (propuesto / en preview / publicado / revertido)
- **Riesgo** (bajo/medio/alto) — del eje riesgo-a-lo-construido
- **Archivos tocados** (text) — ej. `sections/cart-drawer.liquid`
- **Theme de trabajo** (text — nombre+id) · **Backup del MAIN** (text — nombre+id)
- **Hipótesis** (text) — qué esperamos que mejore y por qué
- **Resultado** (text) — métrica antes/después cuando exista (vía clarity/ShopifyQL)
- **Rollback ref** (text) — id del theme al que se vuelve

Cuerpo (toggle por cambio si hace falta): diff resumido, link de preview, checklist de QA firmada.

## Regla de oro
Ningún `implement` se cierra sin una fila en el Log con backup y rollback ref. Si falta eso, el cambio no está "hecho": está huérfano y la próxima corrida no podrá deshacerlo con seguridad.
