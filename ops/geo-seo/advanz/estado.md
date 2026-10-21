# Advanz · OS GEO/SEO · Estado

> SEO, GEO y blog **propios** de advanz.cl. Actualizado: 2026-10-19.

## Estado actual
- 🔴 **Detenido como motor de leads** (no como activo). Es correcto para el largo plazo, pero no sirve para la necesidad de caja actual: la autoridad no se construye en semanas.
- **Qué sí se sostiene**: publicar por proceso lo que ya está hecho (por ejemplo, blogs HTML terminados), sin esperar leads de ahí.
- **Blog de advanz.cl en GoHighLevel**: no hay conector GHL en Claude. Opciones planteadas el 2026-09-12:
  - (1) Claude deja el post listo (SEO/GEO, meta, FAQ) y se pega a mano en GHL → Sites → Blogs (3–5 min).
  - (2) API de GHL (LeadConnector) vía Make, Zapier o n8n.
  - (3) Conector directo con credenciales.
  - Recomendación: empezar por (1). **No quedó registrada la decisión del usuario.**
- No hay auditoría, keywords, datos de Search Console ni de citas en LLM **del sitio propio** en los transcripts.
- Lo que existe es el **producto SEO/GEO para clientes**:
  - Skill `advanz-seo-geo-engine` (7 capas, 5 modos; desarrollada por Patricio).
  - Plantilla de reporte con marca ficticia "Vitalis".
  - Página de Notion reescrita al estándar Advanz (`39ea30152d0081aba064c265632dc471`).
  - Pricing del retainer en `contexto-marca.md`.

## Artifact del OS
- Dashboard "Advanz · OS GEO/SEO": https://claude.ai/artifact/BWRXxdf18LTzm3iBu5SUwS. Se dibuja desde `os-data.json` (contrato del Command Center). Actualizar ambos en cada cierre.
- Accesos probados el 19-oct: Ahrefs sin plan ("Insufficient plan"), Semrush sin unidades de API, Drive y Notion OK, Shopify conectado a amazingcare.cl (no aplica a Advanz).

## Decisiones tomadas
- **2026-10-19 (usuario): stack GEO/SEO = Notion + Search Console (por navegador/Cowork o export CSV) + Google Ads (Planificador de palabras clave) + una herramienta GEO por definir.** Ahrefs, Semrush y GHL quedan fuera. Ciclo semanal: export de GSC → `gsc_cubos.py` (cubos GANA / CASI / CTR_BAJO / NO_RINDE) → acciones en la grilla de Notion; además, 10 prompts GEO manuales hasta tener la herramienta.
- **(sin fecha, vigente)** SEO/GEO propio detenido. **Condición de reactivación**: caja resuelta por outbound y margen para invertir en un canal de retorno diferido.
- **2026-09-03**: Cada módulo de servicio en el board de Miro = **entregable/SOP (captura HTML) + card de la skill (Notion)**. El módulo SEO quedó completo. Las páginas de skill en Notion se escriben en lenguaje de negocio, con lo técnico en toggles.
- **2026-09-12**: Para publicar en GHL, se recomienda el flujo manual primero y automatizar con Make o n8n solo si la frecuencia lo justifica (sin confirmar la aceptación).

## Pendientes / próximos pasos
- [ ] Decidir la vía de publicación del blog en GHL (manual o API) y documentar el proceso.
- [ ] Baseline mínimo antes de reactivar: Search Console de advanz.cl, keywords de marca y de categoría, y prueba de citas GEO (si Advanz aparece en ChatGPT o Perplexity para "agencia ecommerce Chile" y similares).
- [ ] Reutilizar infoproductos públicos (páginas con video + CTA) como contenido indexable cuando exista la cadena (handoff con creative).
- [ ] Guardar la plantilla HTML del módulo SEO (Vitalis) en una carpeta central (`empresa/advanz/seo-geo-engine/`). Quedó pendiente el 2026-09-03.
- Falta levantar: accesos de Search Console y GA4 de advanz.cl, posts publicados en el blog GHL, y competidores orgánicos (agencias ecommerce Chile).

## Fuentes
- `session_01UWBEeacsHnLE26Uv3ST4RL`: Agente | Head of SEO/GEO (2026-09-03). Módulo SEO para Miro y Notion (servicio, no SEO propio).
- `session_0179cirbXdFcapTCWR3J4wKJ`: Conexión blog a GHL (2026-09-12).
- `session_01PgqvDweDuVrhrNNZKr9Rjq`: Estrategia de blogs y conversión de clientes (2026-08-26).
- Skill `advanz-acquisition-system` → `references/canales.md` (estado 🔴). Skill `advanz-seo-geo-engine` (`references/pricing-model.md`, rama `origin/claude/friendly-brahmagupta-arg9vp`).
