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
- **19-oct · accesos probados (solo lectura):** Shopify, Meta Ads (DTC y Mayorista), Notion y Drive responden. Sin conector: Google Ads, GA4, Cloudflare. Sin probar: Klaviyo, Miro, Ahrefs.
- **Reportes al cliente:** cortos y estratégicos, sin tecnicismos ni culpas. Los cambios se cuentan como "preparación para el evento", con verbos de mejora. La expectativa se declara, no se promete. Los próximos pasos se separan en **Cliente (estrategia y marca)** y **Advanz (ajustes y publicación)**.
- **Fuente de verdad:** matriz/Shopify (último clic no directo) para conversiones, CPA y ROAS. Plataformas para inversión, CTR y costos por etapa. Paid y orgánico se separan por UTM.
- **Comparaciones:** mismo tramo del mes anterior (p. ej., 3–20 ago contra 3–20 jul), sin evento adentro.
- **14-sep:** el reporte quincenal se hace como HTML estático siguiendo la plantilla del reporte del lunes 7-sep y se sube como artifact (el JS dentro del command center no daba el mismo resultado). Después se embebió como pestaña "Reporte" del command center.
- **Skills:** `advanz-reporting` cubre los 3 canales (paid, email, SEO), con drafts entregados el 1-sep para instalar en claude.ai. La skill `event-strategy` está en la rama `claude/ecommerce-cyber-strategy-skill-mmm6m0`.
- Ahrefs y Semrush quedan fuera (plan insuficiente o sin unidades). SEO se mide con Search Console, Shopify y la grilla de Notion.

## Pendientes / próximos pasos
- [ ] **Artifact del OS (contrato Command Center):** `os-data.json` publicado el 19-oct (`fuente: "os"`, 7 KPIs, 5 fugas, 11 accesos). Falta crear el Dashboard "AmazingCare · OS Growth" (el publish quedó bloqueado por permisos; requiere OK del usuario) y guardar su URL en `artifact_url`.
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
