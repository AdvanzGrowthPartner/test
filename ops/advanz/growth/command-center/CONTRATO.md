# Contrato de datos · Artifacts de los OS

> Dueño: **Advanz · OS Growth**. Versión `1.0` (2026-10-19).
> Objetivo: que los 12 OS (2 grupos × 6 áreas) publiquen su artifact con **el mismo formato de datos**, para que el Command Center los combine y encuentre fugas y oportunidades cruzadas por marca.

## 1. Qué publica cada OS

1. Un archivo **`ops/<grupo>/<área>/os-data.json`** en el repo, con el formato de la sección 2. Esta es la fuente de verdad: el Command Center lee este archivo, no el artifact.
2. Su **artifact propio**: un Dashboard (tipo "Dashboard" de Artifacts) titulado `<Grupo> · OS <Área>`, que se dibuja a partir de ese mismo JSON (los KPIs arriba, después las fugas por severidad y los accesos). La URL del artifact se guarda en `artifact_url`.
3. Cada vez que el OS cierra trabajo, actualiza el `os-data.json` junto con su `estado.md`, en el mismo commit.

Mientras un OS no publique su archivo, el Command Center usa la **semilla** `ops/advanz/growth/command-center/semillas/<grupo>.<área>.json`. Growth la armó con lo que dice el `estado.md` de ese OS y aparece en el panel como `fuente: semilla-growth`. Cuando el OS publica su propio archivo, la semilla deja de usarse.

## 2. Formato (`os-data.json`)

```json
{
  "version": "1.0",
  "os_id": "amazingcare.cro",
  "grupo": "amazingcare",
  "area": "cro",
  "marca": "AmazingCare",
  "actualizado": "2026-10-19",
  "fuente": "os",
  "artifact_url": null,
  "kpis": [
    {"id": "cvr", "nombre": "Conversión del sitio", "valor": 2.11, "unidad": "%", "periodo": "2026-09-01/2026-09-14",
     "meta": null, "estado": "warn", "fuente": "Shopify"}
  ],
  "fugas": [
    {
      "id": "amazingcare.cro.F01",
      "titulo": "Solo el 59% de los clics de Meta llega a ver la página",
      "etapa": "acquisition",
      "punto_funnel": "trafico",
      "severidad": 4,
      "impacto_clp_mes": null,
      "impacto_nota": "Sano es ≥75%: hoy se pierden ~16 pts del tráfico pagado",
      "evidencia": "2.084 clics → 1.227 visitas (Cyber oct-26)",
      "estado": "abierta",
      "depende_de": [],
      "afecta_os": ["ads"],
      "accion": {
        "descripcion": "Auditar velocidad de la landing y el navegador interno de IG",
        "os_ejecutor": "cro",
        "via": "mcp",
        "conector": "Shopify",
        "requiere_ok": true,
        "acceso": "ok"
      }
    }
  ],
  "accesos": [
    {"conector": "Shopify", "estado": "ok", "nota": "Tienda amazingcare.cl"}
  ]
}
```

### Vocabularios cerrados (para que los datos se puedan cruzar)

| Campo | Valores |
|---|---|
| `grupo` | `advanz` · `amazingcare` |
| `area` | `email` · `ads` · `cro` · `growth` · `creative` · `geo-seo` |
| `etapa` (Growth Engine) | `foundations` · `offer` · `validation` · `acquisition` · `workflows` · `retention` · `feedback` · `systems` |
| `punto_funnel` | `trafico` · `captura` · `pdp` · `carrito` · `checkout` · `recompra` · `lead` · `agenda` · `cierre` · `medicion` · `contenido` |
| `severidad` | 1 (cosmético) … 5 (rompe el funnel o pierde plata hoy) |
| `estado` (fuga) | `abierta` · `en-curso` · `resuelta` |
| `kpis[].estado` | `ok` · `warn` · `bad` · `sin-dato` |
| `accion.via` | `mcp` (conector nativo en esta sesión) · `cowork` (Claude Cowork / navegador / terminal de otra máquina) · `manual` (lo hace una persona) |
| `accion.acceso` y `accesos[].estado` | `ok` · `sin-probar` · `bloqueado` · `sin-conector` · `sin-plan` |
| `conector` | El nombre del conector tal como aparece en Claude: `Shopify`, `Meta_Ads`, `Klaviyo`, `Notion`, `Google_Drive`, `Gmail`, `Miro`, `Vercel`, `Ahrefs`, `Semrush`, `Canva`, `Figma`, `Magnific`, `pletor`. Si no hay conector: `GHL`, `Google_Ads`, `Search_Console`, `GA4`, `Clarity`, `Instagram` |

### Reglas
- `id` de fuga: `<grupo>.<área>.F<nn>`, estable en el tiempo (no se renumera). Una fuga resuelta se queda con `estado: resuelta`.
- `depende_de` y `afecta_os` son los que permiten combinar: `depende_de` lista IDs de fugas de **otros OS** que hay que cerrar antes, y `afecta_os` lista las áreas que pierden si esta fuga sigue abierta.
- `impacto_clp_mes` va solo si hay un cálculo con fuente. Si no, `null`, y la estimación va en `impacto_nota`. No se inventan cifras.
- `requiere_ok` es `true` para todo lo que gaste plata, publique o envíe (regla global).
- Nada de secretos, tokens ni datos personales de clientes finales.

## 3. Cómo combina el Command Center

`python3 ops/advanz/growth/command-center/consolidar.py` lee los 12 archivos (o sus semillas), valida los vocabularios y genera `consolidado/`:

- **fugas.json**: todas las fugas abiertas, con su OS y su marca.
- **oportunidades.json** (y `oportunidades.<marca>.json`): grupos de fugas de **distintos OS** de una misma marca. **Nunca se juntan fugas de marcas distintas**, ni siquiera por `depende_de`. Las fugas se juntan cuando una depende de otra, cuando una afecta al área de la otra o cuando caen en el mismo punto del funnel. Una fuga sola también entra si su `afecta_os` toca otra área. Puntaje = severidad máxima × 5 + OS involucrados × 3 + severidad del resto de las fugas del grupo: manda lo más grave y, a igual gravedad, lo que mueve a más OS.
- **accesos.json**: qué conector destraba más fugas (por ejemplo, "regularizar Meta Advanz destraba N fugas"). Así se priorizan los accesos que faltan.
- **cobertura.json**: qué OS ya publicó su archivo y cuáles siguen en semilla.

Growth sube estos archivos al **Advanz OS Command Center** (https://claude.ai/artifact/44LVZUHY5tgGH6P7Nb6vHk) y deriva las oportunidades a cada OS vía `handoffs.md`.

## 4. Ejecutar cambios en las marcas

Cada fuga dice **por dónde** se arregla (`via`, `conector`) y si **hay acceso hoy** (`acceso`). El flujo es siempre el mismo:

1. Growth prioriza en el Command Center y deja el handoff al OS ejecutor.
2. El OS ejecutor propone el cambio concreto y **espera el OK del usuario** (`requiere_ok`).
3. Lo aplica por MCP (o por Cowork si el conector vive en otra máquina, como Google Ads), lo registra en su `CHANGELOG.md` y pasa la fuga a `resuelta` en su `os-data.json`.
