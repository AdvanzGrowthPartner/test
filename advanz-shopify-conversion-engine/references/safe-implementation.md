# Fase 3 — Implementación sin romper (protocolo + mecánica)

Escribir al theme equivocado tumba las ventas en vivo. Este archivo es el cómo. Las reglas del SKILL.md (nunca tocar MAIN, publish es humano, backup + rollback) son la ley; esto las hace ejecutables. Mutations verificadas contra Admin API 2024-10+.

## El bucle seguro (resumen)
```
duplicar MAIN → theme de trabajo (unpublished)
   ↓
leer archivo actual (files query)
   ↓
editar en local (aditivo, respetando la familia del theme)
   ↓
themeFilesUpsert AL THEME DE TRABAJO  ← nunca al MAIN
   ↓
preview (URL del theme de trabajo)
   ↓
QA de regresión contra el Blueprint
   ↓
[GATE humano: presentar diff + preview + QA]
   ↓
backup del MAIN actual (queda unpublished, fechado, ≥14 días)
   ↓
themePublish (theme de trabajo)  ← solo con OK explícito
```

## 1. Crear el theme de trabajo (duplicar el MAIN)
No hay una mutation `themeDuplicate`. Opciones, en orden de preferencia:
1. **Admin UI (recomendado, 1 clic):** Online Store → Themes → en el tema publicado, "Duplicate". Renómbralo con convención `[WIP] Advanz <AAAA-MM-DD> <cambio>`. Pide al usuario que lo haga o confirma que ya existe uno.
2. **Shopify CLI (dev en su máquina):** versiona en git y trabaja unpublished:
   ```bash
   shopify theme pull --theme <MAIN_ID>            # baja el vivo a local
   git checkout -b fix/<cambio>
   # editar, commitear
   shopify theme push --unpublished --theme-name "[WIP] Advanz <fecha> <cambio>"
   ```
3. **Fallback API:** `themeCreate` desde un `src` (zip) + `themeFilesUpsert`. Pesado; úsalo solo si no hay acceso a Admin/CLI.

Verifica el resultado con la query `themes` (debe existir un `UNPUBLISHED` nuevo con tu nombre). Guarda su `id` = `WORK_ID`.

## 2. Leer antes de escribir
`themeFilesUpsert` **reemplaza el archivo completo**. Trae el contenido actual primero (query `ThemeFiles` de `store-blueprint.md`) y edítalo sobre esa base. Nunca construyas el archivo desde cero de memoria: borrarías trabajo manual existente.

## 3. Escribir al theme de trabajo
Input verificado: `OnlineStoreThemeFilesUpsertFileInput` = `{ filename, body: { type: TEXT|BASE64|URL, value } }`.
```graphql
mutation UpsertThemeFiles($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
  themeFilesUpsert(themeId: $themeId, files: $files) {
    upsertedThemeFiles { filename }
    job { id done }
    userErrors { field code message }
  }
}
```
```json
{ "themeId": "gid://shopify/OnlineStoreTheme/<WORK_ID>",
  "files": [ { "filename": "sections/main-product.liquid",
               "body": { "type": "TEXT", "value": "<contenido completo editado>" } } ] }
```
- **`themeId` SIEMPRE es `WORK_ID`, nunca el MAIN.** Compruébalo antes de ejecutar: relee el `role` del theme destino; si es `MAIN`, DETENTE.
- Revisa `userErrors`. Si `job` no está `done`, el procesado es async: reconsulta el theme.
- Mutations relacionadas: `themeFilesCopy` (copiar archivos entre themes), `themeFilesDelete` (borrar archivos del theme de trabajo).

### Cómo generar el código (respetar lo construido)
- **Aditivo, no destructivo.** Añade una sección/bloque nuevo o extiende el existente; evita reescrituras grandes.
- **Usa el schema de la familia del theme** (Trade, Dawn, Horizon…): settings de sección, `{% schema %}`, presets. No hardcodees textos/colores — exponlos como settings para que el merchant los edite y para poder apagarlos.
- **Envuelve lo nuevo en un flag/setting** cuando puedas (ej. `{% if section.settings.enable_x %}`). Así el rollback parcial es un toggle, no un redeploy.
- **Respeta metafields y selling plans** del Blueprint: si un bloque lee `product.metafields.custom.ingredientes`, no cambies esa ruta.
- No toques `config/settings_data.json` salvo que el cambio lo exija y lo declares.

## 4. Preview
Cada theme tiene URL de preview (`?preview_theme_id=<WORK_ID>` sobre el dominio). Compárate contra el MAIN en vivo, lado a lado, en desktop y mobile.

## 5. QA de regresión (contra el Blueprint) — mínimo obligatorio
- [ ] Add-to-cart funciona en PDP (todas las variantes/selling plans).
- [ ] Carrito/drawer custom sigue renderizando y calculando (zona sensible en amazingcare).
- [ ] Secciones de app (reviews, slider, bundles) siguen vivas — no se pisó su bloque.
- [ ] Sin errores Liquid (no aparece contenido crudo `{{ }}` ni secciones vacías).
- [ ] Home/colección: el orden de secciones no se alteró involuntariamente.
- [ ] Mobile: layout, sticky ATC, tap targets.
- [ ] Velocidad: no se agregó un script pesado bloqueante.
- [ ] Lo que ya funcionaba sigue funcionando (revisa el mapa de superficies del Blueprint).
Documenta el resultado. "Sin romper" se demuestra con esta checklist, no se asume.

## 6. GATE humano + publicar
Presenta: qué archivos cambiaron (diff), link de preview, resultado del QA, y el plan de rollback. **Espera OK explícito.** La skill no publica por iniciativa propia.
```graphql
mutation PublishTheme($id: ID!) {
  themePublish(id: $id) { theme { id name role } userErrors { field message } }
}
```

## 7. Backup + rollback
- **Antes de publicar**, asegura que el MAIN actual queda como copia unpublished fechada (duplícalo en Admin si hace falta): `[Backup pre-<cambio>] <AAAA-MM-DD>`. Mantener ≥14 días. Es lo que el equipo ya hacía a mano — aquí es obligatorio.
- **Rollback** = `themePublish` del backup. Instantáneo. Ténlo identificado (id + nombre) antes del publish.

## 8. Cerrar → Fase 4
Registra en el Change/Decision Log (ver `notion-schema.md`): archivos, hipótesis, theme de trabajo + backup (ids/nombres), y referencia de rollback. Sin esto, la próxima corrida no sabe qué se cambió.
