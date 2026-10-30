# AmazingCare · OS Growth (reporting, KPIs de negocio, dashboards, cierres, estrategia)

## Estado actual
**Último dato leído: 4 oct 2026, Cyber Amazing en curso (evento del 2 al 11 oct).**
- **Cyber oct-26 (war room):**
  - Plan pagado de $3M para 10 días. El modelo proyectaba ~$18M netos, con el punto dulce de inversión en $5–6M.
  - Día 2: $2,37M netos y 57 órdenes. Acumulado $3,86M → ritmo de ~$14M.
  - Creatina: 20 unidades el sábado y 19% de los pedidos la llevan (el plan era 8%). Stock: 160 de 180.
  - Ningún SKU se agota al ritmo actual (stock al 3-oct): Pack 60 340, Súper 165, Berries 30 315, Piña 30 135, Fibra 279, Energy 180, Creatina 160.
  - Modelo de saturación: T(S)=A·(1−e^(−S/K)), con A $40,75M y K $5,0M. Se recalibró con la venta del día 2.
- **Comparativo de eventos (base neta):**

| Evento | Venta neta | Órdenes | AOV | Inversión pagada | ROAS | Otros |
|---|---|---|---|---|---|---|
| CyberDay jun-26 | $25,76M | 698 | $36.633 | $5,0M | 5,15 | CPA $9.788; 52% clientes nuevos |
| Cyber oct-25 | — | — | — | — | 5,95× | — |

  - Con +53% de inversión vino +32% de venta (ROAS marginal ~3,6×).
  - El "CAC $7.166" del reporte es gasto ÷ todas las órdenes. El CAC real por cliente nuevo es ~$13.700.
- **Sep 1–14 (reporte quincenal):** $7,66M netos, 217 ventas, ROAS 3,98, 145 clientes nuevos (71 recurrentes). +35% en venta neta y +28% en órdenes contra el 18–31 ago. CELEBRACONAMAZING llevaba 338 usos acumulados.
- **Ago 1–20 (matriz):** inversión $2,84M, 242 ventas, $7,55M, ROAS 2,66 (breakeven 2,5), margen neto ~$180K. 74% pagado / 26% orgánico. 161 clientes nuevos y 78 recurrentes.
- **Command Center del cliente:** artifact https://claude.ai/code/artifact/a7910047-dbb2-4ee3-a9e0-e368af258290 (V16, 14-sep).
  - Pestañas: Reporte (por defecto) · Rentabilidad · Campañas · CRO · SEO/GEO · Email · Histórico.
  - Score ABC por canal, calculadora de MER y proyección.
- **Versión hosteable** en Cloudflare Pages: proyecto `amazing-command-center`, código en `origin/claude/epic-pasteur-1v818p:command-center-cf/`.
  - 8 Functions: meta, google, klaviyo, shopify, meta-creatives, gsc, all, _middleware. Solo lectura.
  - No consta que esté deployado ni que tenga los secrets cargados (sin confirmar).
- **Cockpit Next.js alternativo:** https://advanz-motor.pages.dev (Diagnóstico con Growth Score 76, Inteligencia por ángulo, Evento FP). Al usuario le pareció "sin valor agregado" y se recalibró el 10-sep. Estado actual sin confirmar.

## Decisiones tomadas
- **30-oct · Split de campañas por categoría (pedido del cliente):** propuesta visual v2 con paleta del command center (violeta/cian, Poppins + Space Grotesk) https://claude.ai/artifact/WRgGJosVF96dLd8qCR1WEe (fuente `propuestas/2026-10-30-split-campanas.html`). Mix 90 días Shopify: electrolitos 86% · Energy 5% · Creatina 4% · Fibra 3%. Escenario A $3M = 6 campañas (Google Brand 150K, PMax ELE 640K, Search Rendimiento 360K; Meta Prosp ELE 850K, Prosp Rendimiento 550K, RT 450K) y ~20 creativos. Escenario B ~$5M = 10 campañas + TikTok de prueba y ~37 creativos. Pisos: Meta 43 compras/mes por campaña, Google 30 conv/mes. Pendiente decisión del cliente. **v5 (30-oct, actual → objetivo):** mapas de calor + tortas + cuadros de respuesta por bloque. Actual = 5 campañas ~$2,37M, ROAS plataforma 4,55×. Escalera: E1 estructura + reemplazo cada 2 sem ($2,46M, 4,98×) → E2 + Creatina ($3,01M = presupuesto cliente, 4,8×) → E3 + Search Rendimiento ($3,41M) → E4 escalar ganadores ($3,86M) → E5 + TikTok ($4,56M, 4,15×, 9 campañas, 46 creativos/mes: 23 estáticos + 23 videos → cliente 10 + IA 13). Marginal de cada etapa ≥ 2,5. Escalar lo actual a $4,56M sin split daría 3,6×. Fatiga medida: Prospección 5,8× semana con creativos nuevos → 4,8× → 2,4× a la 3ª semana; Retención 9,0× (sep) → 3,9× (oct, mismo catálogo). Energy no paga CPA propio (venta/pedido $13,6K) → va dentro de Creatina con Pack Boost. **v4 (30-oct, plan de medios):** selector A/B; A = 7 campañas, $3,0M, 10 ad sets, 15 creativos nuevos/mes (11 estáticos + 4 videos), ~325 compras de plataforma (~4,1×); B = 11 campañas, $5,02M, 20 ad sets, 37 nuevos/mes (17 estáticos + 20 videos → cliente 10 + 10 videos IA), ~486 compras (~3,7×). Audiencias agrupadas (Meta abr–oct): Runner/isotónica 8,6× CPA US$5,7 (100% evento) · Adv+ 5,4× · Condiciones P4 4,6× (siempre activo, la mejor fuera de evento) · Deportista mix 4,6× · Similares 4,2× (89% evento) · Bienestar 3,5× CPA US$12,6. Estáticos no son el cuello de botella (20/mes alcanza en A); el cuello es video en B. **v3:** fondo crema, Meta con CBO por categoría + ABO de testeo de audiencias + ABO retargeting (A 7 campañas, B 11 / $5,02M). Creativos por campaña y formato: A 16 nuevos/mes (2 shooting, 5 est IA, 4 promoted, 2 UGC, 3 clip IA); B 35 (4, 7, 3, 12, 9). Histórico Meta abr–oct: mejores audiencias Isotónica 8,8× y Deportes 6,5× (eventos), Top regiones 7,0×, P4 Salud 4,6× (always-on); núcleo 25–44 (F 25–34 CPA US$7,9), excluir 65+; IG stories/feed > FB; promoted sueltos 1,4–2,4× → solo RT. Regiones Shopify: Valparaíso 161 y Biobío 100 pedidos rinden; Coquimbo US$421 para 22 pedidos. Supuesto a validar: CPA Search no-brand ~$12K (sin datos de Google Ads).
- **21-oct · Command "Growth OS · AmazingCare":** https://claude.ai/artifact/AaQ652nEWo7t2cMSyruyfv (Dashboard privado, solo datos AmazingCare). Datasets = `command/*.json` de `exportar.py`; se refresca en cada cierre.
- **19-oct · accesos probados (solo lectura):** Shopify, Meta Ads (DTC y Mayorista), Notion y Drive responden. Sin conector: Google Ads, GA4, Cloudflare. Sin probar: Klaviyo, Miro, Ahrefs.
- **Reportes al cliente:** cortos y estratégicos, sin tecnicismos ni culpas. Los cambios se cuentan como "preparación para el evento", con verbos de mejora. La expectativa se declara, no se promete. Los próximos pasos se separan en **Cliente (estrategia y marca)** y **Advanz (ajustes y publicación)**.
- **Fuente de verdad:** matriz/Shopify (último clic no directo) para conversiones, CPA y ROAS. Plataformas para inversión, CTR y costos por etapa. Paid y orgánico se separan por UTM.
- **Comparaciones:** mismo tramo del mes anterior (p. ej., 3–20 ago contra 3–20 jul), sin evento adentro.
- **14-sep:** el reporte quincenal se hace como HTML estático siguiendo la plantilla del reporte del lunes 7-sep y se sube como artifact (el JS dentro del command center no daba el mismo resultado). Después se embebió como pestaña "Reporte" del command center.
- **Skills:** `advanz-reporting` cubre los 3 canales (paid, email, SEO), con drafts entregados el 1-sep para instalar en claude.ai. La skill `event-strategy` está en la rama `claude/ecommerce-cyber-strategy-skill-mmm6m0`.
- Ahrefs y Semrush quedan fuera (plan insuficiente o sin unidades). SEO se mide con Search Console, Shopify y la grilla de Notion.

## Pendientes / próximos pasos
- [ ] Validar el split con Google Ads por campaña (90 días) y volumen de "creatina"/"electrolitos" en el Planificador; luego presentar A vs B al cliente.
- [ ] **Reporte de cierre del Cyber oct-26** (2–11 oct): no hay data después del 4-oct. Usar el war room y el "Reporte Cierre Cyber" de junio como plantilla, y comparar los 3 eventos en base neta.
- [ ] Actualizar la skill `event-strategy` con las lecciones del Cyber: neto contra bruto, el gotcha del IVA en ShopifyQL (`gross_sales`/`net_sales` van sin IVA), la calculadora de saturación, las definiciones de CAC y la auditoría de apilamiento de descuentos (Kaching). Se ofreció y no hubo respuesta.
- [ ] Command Center en vivo: deploy en Cloudflare más secrets (Meta, Klaviyo, Shopify, Google Ads, GSC) en la máquina de Matías. Después, cablear "actualiza el command center con <mes>" y barrer el histórico ene–jul 2026 y 2025.
- [ ] Reportes de cierre de mes: agosto (sesión del 31-ago, solo se leyó el inicio) y septiembre completo (solo existe el del 1–14). Octubre pendiente.
- [ ] Pedir al cliente los **COGS por producto** para fijar CPA y CAC objetivo por producto y canal.
- [ ] Definir la convivencia de códigos en eventos: hay 6 códigos sin fecha de término compitiendo con el cupón del evento.

## Fuentes
- session_01MLGvNVcyGZBjw1Ey4x8HPU: war room Cyber oct-26 y skill event-strategy (https://claude.ai/artifact/4NHYGwnx1PFnXEVMp12b7S)
- session_01X6TVMKPeTJfuPs56hHBmVw: Reporting Master y Command Center (artifact a7910047…, código en la rama `claude/epic-pasteur-1v818p`)
- session_014qJfxPHjDMJgFTkac6jMLo: reporte sep 1–14 (https://claude.ai/code/artifact/a43e7192-a677-47b6-af35-8dc3d02bda97) y pestaña Reporte del command center
- session_01VjaHS4QzC4uGuNMfJXSH7k: dashboard advanz-motor.pages.dev
- session_01BVePuAZzyGKWnTLxrwckRG: reporte semanal del 21-ago (archivo local `reportes/2026-08-21_reporte-agosto-fiestas-patrias.html`)
- session_01C27HXkYcaUjgLQLMhHAd4C: cierre de agosto (la sesión solo trae el planteamiento inicial)
- Notion: "Reporte Cierre Cyber" (jun-26), "Reporte Cierre Julio 2026", páginas "Septiembre" y "Cierre agosto"
