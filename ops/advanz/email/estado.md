# Advanz · OS Email · Estado

> Email, CRM, GHL, outbound y cold email **propios** de Advanz. Actualizado: 2026-10-19.

## Estado actual
- **Cold outreach con Diagnóstico Vivo = 🟢 canal principal** de adquisición. Meta: **100 diagnósticos entregados por semana** (15–20 por día). Dueño: el socio, más Patricio en las URLs top.
  - Flujo: scrapear tiendas en Jumpseller, Woo o Tienda Nube con dolor evidente → correr el diagnóstico vivo → enviar el hallazgo por DM o mail **sin pedir la llamada** → cerrar 1:1 a quien responde.
  - Activo: **~40 diagnósticos corridos y colgados en Vercel**.
  - **Bloqueo declarado**: enriquecer el contacto del founder. Cascada con corte de 5 min por URL: footer → IG → LinkedIn → WHOIS → prensa → SII. Tiers A/B/C.
- **CRM outbound**: Notion `repo-ecommerces` (Ecomm Scrapping CL, data_source `398a3015-2d00-808d-b2c3-000ba2c61301`), alimentado por la skill `ecomm-scraping-cl` (score de partner 1–5, solo marca propia DTC en Chile). Ejemplo real: Marê Swimwear salió de este CRM, tuvo discovery el 18/08 y propuesta el 21/08.
- **Nurturing**: workflow de **5 correos en GHL** que invita a la llamada de diagnóstico, en el canal Web Funnel (🟢). Regla: 0 leads sin gestionar al final del día.
- **Envío**: se propuso el esquema Gmail MCP (borradores para aprobar, 10–40 por día) → luego Instantly, Smartlead o Lemlist desde un **dominio secundario** con warmup. No hay confirmación de qué se implementó.
- Correos de ventas post-llamada: skills `advanz-sales-push-emails` y `advanz-closing-agent` (envío de contrato, follow-up, recuperación).

## Decisiones tomadas
- **2026-08-13**: Arquitectura de outbound en 3 capas (scraping → Notion → envío con seguimiento). Personalización de 1 línea por marca, opt-out, warmup y nunca el dominio principal. Solo correos corporativos públicos. (Propuesta; no quedó registrada la elección de A/B/C.)
- **(sin fecha)** Cero pitch en el primer toque: se entrega el hallazgo, no se vende la llamada. Si nadie responde, se arregla el copy del DM, no la oferta.
- **(sin fecha)** Todo lead (home, lander, DM, comentario, outbound) entra al workflow de GHL.

## Pendientes / próximos pasos
- [ ] Destrabar el enriquecimiento de contacto de los ~40 diagnósticos existentes ("se resuelve en 1–2 días").
- [ ] Confirmar la herramienta de envío en frío (Gmail manual o Instantly/Smartlead) y el dominio secundario con SPF/DKIM/warmup.
- [ ] Documentar los 5 correos del workflow GHL (asuntos, timing, CTA) en este OS.
- [ ] Secuencia de outbound: apertura con hallazgo + 2 follow-ups (día 3 y día 7).
- [ ] Conectar el form del lead magnet Shopify al workflow GHL: hoy el `fetch('/api/leads')` está comentado (ver OS CRO).
- Falta levantar: tasas reales (envíos, respuesta, agendas), acceso o API de GHL y la lista de dominios de envío.

## Fuentes
- `session_0124BSzEPvpANTGccKARkNha`: Web scraping y envío de correos automatizado (2026-08-13).
- `session_019ujiE2BjTxXhfWfZsBGABJ`: Objeciones Marê Swimwear (2026-08-21). CRM `repo-ecommerces`.
- `session_0179cirbXdFcapTCWR3J4wKJ`: Conexión blog a GHL (2026-09-12). No hay conector de GHL.
- Skills `advanz-acquisition-system` (`canales.md`), `ecomm-scraping-cl`, `advanz-closing-agent`, `advanz-setter-agent`.
