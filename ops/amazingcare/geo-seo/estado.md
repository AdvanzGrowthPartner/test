# AmazingCare · OS GEO-SEO (SEO, GEO/IA, blog, Search Console, Merchant)

## Estado actual
**Último dato leído: Search Console del 1-jul-2025 al 10-sep-2026 (export del 11-sep) y GA4 de jun–sep 2026.**
- **SEO total (GSC, ~12 meses):** 299.351 impresiones (+87% contra enero), 5.837 clics, posición media 6,0.
  - Septiembre parcial (al 10-sep): 15.509 impresiones (−19%), 244 clics y posición 6,88.
  - **La marca convierte:** 78% de los clics en posición 1,3 y CTR 7%, con solo el 22% de las impresiones. "amazing care electrolitos" tiene CTR 10%.
  - **Lo genérico es el potencial:** "electrolitos" suma 69.670 impresiones en posición 6,3, con CTR 0,49%.
- **Blogs (~91K impresiones):**
  - En página 1 baja o página 2: Magnesio (22,5K impresiones, posición 8,1), Electrolitos: qué son (12,8K, posición 10,5) y Creatina (6,8K, posición 11,6).
  - El de más clics es Disautonomía. También rankean bariátrica y electrolitos para running.
  - Los firman nutricionistas colegiadas (E-E-A-T). Los artículos recientes traen schema JSON-LD y FAQPage; los de 2025 probablemente no.
  - Cadencia: 6 publicados en agosto (meta 4 al mes).
- **Fichas de producto orgánicas:** 208.505 impresiones en posición 5,66.
- **Merchant free listings:** casi apagados. 578 impresiones y 29 clics en 12 meses (aunque con posición 3,6 y CTR 5%, el mejor del sitio). En agosto: 13 sesiones (`product_sync`). El grueso de Shopping es pagado (PMax).
- **Orgánico en Shopify (sesiones):**

| Mar | Abr | May | Jun | Jul | Ago |
|---|---|---|---|---|---|
| 2.389 | 2.603 | 4.546 | 1.430 | 1.067 | 1.875 (+76%) |

  - Agosto: 1.875 sesiones → 78 ventas → CVR 4,16% → ~$3,6M estimados. El blog es ~4% del orgánico.
- **GEO / IA (GA4, jun–sep):**
  - ChatGPT: 72 sesiones, 75% nuevos, engagement 52,8% y **3 compras** (Mix 5 sticks y Maracuyá 30 en septiembre). Es el 88% del tráfico de IA. Gemini: 8.
  - Aterriza en fichas de producto y en la página de ciencia/certificaciones, no en el blog.
  - Tendencia: may 14 → jun 14 → jul 12 → ago 22 → sep 24 (en 14 días).
- **Señales GEO:** autoría ✅ · schema ✅ · FAQ parcial · Wikidata y `llms.txt` pendientes · AggregateRating sin verificar · AI Citation Score sin línea base.

## Pedidos de Antonia Quezada (WhatsApp, 19-oct) · en curso
Diagnóstico solo de lectura (Shopify + Notion), sin cambios aplicados todavía. Esperando el OK del usuario.
- [ ] **POTS y disautonomía** (`pots-disautonomia-mareos-fatiga-desmayos`, publicado el 28-sep): Antonia no lo escribió ni lo aprobó. Ocultarlo y redirigir 301 a `electrolitos-disautonomia`, que es el blog de disautonomía con más clics y no se toca.
- [ ] **Creatina y electrolitos** (`creatina-y-electrolitos-hidratacion`, autor "Amazing Care"): ocultarlo y relanzarlo después en la misma URL con texto de Antonia y enlace a la PDP de Creatina Creapure.
- [ ] **Los 2 de Cyber** (`suplementos-en-cyber-como-comparar` y `mejores-electrolitos-chile`): están sin portada y quedaron primeros en el listado. Al de Cyber se le cambia la fecha a una anterior; "Mejores electrolitos" es keyword evergreen, así que se queda y necesita portada.
- [ ] **Alergias y Viajes**: Shopify tiene la versión vieja. Hay que pasar a Shopify la versión de Notion que corrigió Antonia (texto, imágenes y bibliografía). En Viajes, Antonia volvió a mencionar el **alcohol**, que se había sacado el 28-sep: confirmar con ella.
- [ ] **Quimioterapia** (nuevo, para el mes del cáncer de mama, plazo 19-oct): el borrador está en `borradores/2026-10-19-electrolitos-quimioterapia.html`, sin cupón. Faltan subir las imágenes de Notion y el OK para publicar.
- [ ] Antonia pide ideas para los nuevos blogs de creatina este mes.

## Decisiones tomadas
- **1-sep:** el reporte SEO excluye PMax (va por el carril pagado y aparece solo como nota). Separa orgánico, Merchant free listing, blog y GEO.
- **No cambiar los titles de artículos** (Patricio: resetea las impresiones). La palanca es el CTR y empujar posiciones.
- **Keywords atadas a producto real:** foco en electrolitos, fibra y Energy. Magnesio no tiene producto. En sep-26 creatina tampoco tenía, pero **desde oct-26 sí existe Creatina Creapure**, así que el blog de creatina (6,8K impresiones) pasa a tener producto detrás (sin confirmar si ya se enlazó).
- **Merchant:** solo free listing, marcado como venta pendiente. En una nota interna figura como no contratado (setup a cotizar).
- **Blogs YMYL:** el autor siempre es el profesional clínico, nunca Advanz. El contenido del cliente se enriquece, no se reescribe (skill `advanz-shopify-blog-publisher`).
- **11-sep:** se construyó `functions/api/gsc.js` (API de Search Console, `webmasters.readonly`, `GSC_SITE_URL=sc-domain:amazingcare.cl`) y se rehízo la pestaña SEO del command center en 3 vistas: SEO general, fichas/Merchant y blogs.
- **14-sep:** se propuso un GEO Scoreboard: auditar 10 prompts de compra en ChatGPT y registrar si aparece Amazing, en qué posición y qué fuentes cita. Crear un segmento fijo "Canal IA" en GA4 y Shopify.

## Pendientes / próximos pasos
- [ ] Subir los 3 blogs de página 2 (Magnesio, Electrolitos qué son, Creatina) al top 5, y enlazar el blog de creatina a la nueva PDP de Creatina.
- [ ] Optimizar el feed de Merchant para ganar free listings (cotizar el setup).
- [ ] Correr la auditoría de los 10 prompts en ChatGPT (necesita Chrome logueado o que el usuario lo haga a mano) y armar el GEO Scoreboard.
- [ ] Schema `Review`/`AggregateRating` en las PDP, Wikidata y `llms.txt`. Reforzar la página de ciencia/certificaciones (COA, composición).
- [ ] Conectar los secrets de GSC en el command center de Cloudflare para tener datos en vivo.
- [ ] Reporte SEO de septiembre y octubre (solo existe el de agosto). Subirlo a Notion en Reportes Mensuales.
- [ ] Listicle de conversión estilo claranovalabs con el contenido del blog de lipedema (pedido el 26-ago, sin entregable).

## Fuentes
- session_01LShHSCJAqKAqsnPedFPhRW: reporte SEO de agosto (https://claude.ai/code/artifact/e978475d-a771-41a1-8250-4985be6c182b) y drafts de las skills `advanz-reporting` y `advanz-seo-geo-engine` (modo F)
- session_01X6TVMKPeTJfuPs56hHBmVw: export de Search Console del 11-sep y pestaña SEO/GEO del command center
- Rama `origin/claude/epic-pasteur-1v818p`: `command-center-cf/functions/api/gsc.js` y `command-center-cf/data/gsc-export/*.csv`
- session_014qJfxPHjDMJgFTkac6jMLo: análisis del canal IA/ChatGPT (14-sep)
- session_01PmvGFUXiETFEMitMuHkvin: blog de lipedema y electrolitos (26-ago; solo se leyó el inicio)
- Artifact de referencia SEO: https://claude.ai/code/artifact/ca6a37d6-0a9c-4f02-812c-3d93d01285c7 (no leído)
