# AmazingCare · OS Ads (paid media Meta/Google, UTM, tracking)

## Estado actual
**Último dato leído: Cyber Amazing oct-26, corte del sáb 3 oct ~22:00.** No hay cierre del evento (terminó el 11 oct).
- **Cyber oct-26 (plan pagado de $3M, 10 días):**
  - Día 2: $2,37M netos y 57 órdenes (81% del plan de ventas). Acumulado: $3,86M → proyecta ~$14M contra $18,4M del plan.
  - El usuario mencionó una meta de "30k", interpretada como $30M (sin confirmar). Para llegar haría falta un gasto pagado de ~$710K/día contra $160K/día hoy.
  - **Techo de inversión recomendado: ~$610K/día.** Hasta ahí el ROAS marginal es ≥2,5 y el gasto por orden queda bajo $8K.
  - Meta: US$165 el sábado (93% de lo planeado), ROAS de plataforma 13,2×. Prospección en $0. Regiones rinde 16,9× y remarketing CBO 13,4×. Remarketing ABO cae a 4,8× con frecuencia 2,0.
  - **Meta real está entre 3,7× (lo que ve Shopify, referrer social) y 11,6× (lo que reporta Meta).** De 2.084 clics solo 1.227 llegan a la página (59%), así que es un problema de CRO.
  - Google: **sin datos.** Esa sesión no tenía conector. El usuario dice que sí está conectado desde la terminal de Matías.
- **Estructura Meta (sep-26):**
  - `AC | CBO - Prospección`, con un pack por avatar: P1_Deportista_Rendimiento, P1_Deportista_Embajadores (0031), P2_Profesional_Energia, P3_Bienestar_Fibra, P6_Cotidiano_Hidratacion, P4_Salud_Autoridad (0032).
  - `AC | CBO - Adquisición - Fiestas Patrias` · `AC | ABO - Retención` · `AC | CBO - Alcance Retail` · campañas de Regiones y Remarketing (CBO/ABO) · "CYBER Oct 26".
- **Sep 1–14 (reporte quincenal):**
  - Meta: $1,16M y 62 órdenes. Prospección 5,51×, Retención 6,50×.
  - Google: $570K y 69 órdenes. Brand 9,9×, PMax 3,4×, Categoría 7,5×. El Brand se lee aparte (criterio de Patricio: es captura).
- **Agosto-26:**
  - Meta mes: ROAS 3,40×, US$2.790, 212 compras.
  - Matriz 1–20 ago: inversión $2,84M, 242 ventas, $7,55M, ROAS 2,66, CPA $15.866, CAC $11.736, 74% pagado.
  - Meta 3–20 ago: frecuencia 6,09 y CTR 1,11%. El 44% del gasto fue a la campaña de peor ROAS (`AC | CBO - Adquisición`, 0,84).
- **Google Ads (auditoría del 4 sep):**
  - PMax Principal: 2,00× en 30 días ($847.528). Antes del cambio de puja del 2–4 ago rendía 3,56×.
  - Search Brand 9,27× · Search Category Elect 1,22×.
  - La PMax está en "Maximizar valor de conversión" sin tROAS y no excluye la marca (posible canibalización con Brand).
- **Referencia CyberDay jun-26:** pagado $5,0M (Meta $3,79M, Google $996,6K). PMax Packs 10,56× (CPA $4.171) y PMax Fibra 13,54× (CPA $3.150). En 6 días el CPM subió 2,5× y el alcance diario cayó 9×.

## Decisiones tomadas
- **25-ago:** se migran los adsets de `ABO - Adquisición` a `CBO - Prospección`. Se recrean, sin duplicar Cotidiano ni Deportista. Pack Salud (0,13×) se reemplaza por 0032. Convención de nombres `P#_Avatar_Concepto`. Se recomienda subir la CBO a ~US$40–50/día.
- **25-ago:** los videos de retail (Jumbo, Tottus, farmacias, STOP) van a una campaña de **Alcance/Reconocimiento**, no de tráfico web. Opción: CTA a una página "Dónde comprar" (no existe).
- **21-ago:** estrategia en paralelo: siempre activo (AON) más una CBO de Fiestas Patrias. Google FP del 21 ago al 19 sep.
- **1-sep:** reportar el link-in-bio de IG por `utm_id` y no por source/medium (GA4 lo fragmenta). Agregar `utm_campaign` para Shopify.
- **11/12-sep:** se crearon 5 adsets y 17 anuncios **en PAUSA**:
  - FP Refresh Sept `120249281381030244` (EVT-0017/18/19/22).
  - Pack_P2 Energía `120249281428940244` (VID-0040/41, EST-0044).
  - Pack_P6 Cotidiano `120249281430190244` (EST-0045/47/52/54/55).
  - Pack_P3 Bienestar `120249281430570244` (EST-0049/51/53).
  - Pack_P1yP4 Deporte-Salud `120249281431670244` (EST-0046/48).
  - Destinos: la PDP que más convierte para cada producto. Los verticales 9:16 se agregan a mano.
- **UTM estándar Meta (sep-26):** `utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}`. El SKU va en `utm_content`.
- **Atribución en los reportes:** conversiones, CPA y ROAS salen de la matriz de Shopify (último clic no directo, sumando IG + FB + Meta). La inversión, el CTR y los costos por etapa salen de cada plataforma.
- **Semana del 18–22 ago:** auditoría del píxel/CAPI de Meta. La trazabilidad de compra subió de 28,6% a 35,7% y el EMQ de compra pasó a 9,3. En julio el CPA de Meta bajó $11.000 respecto de los últimos 2 años.

## Pendientes / próximos pasos
- [ ] **Cerrar el Cyber oct-26:** resultado final del 2–11 oct, ROAS real de Meta y Google, y contraste con la proyección. No hay data después del 4 oct.
- [ ] Traer la data real de Google Ads al war room y al command center (gasto, ROAS, PMax). Se habló de un conector Supermetrics/Windsor o de un prompt de Cowork.
- [ ] Confirmar si se aplicó **tROAS 3,0×** a la PMax Principal (recomendado el 4-sep) y si se revisaron los negativos de Search Category Elect y la exclusión de marca en PMax.
- [ ] Revisar si se activaron los 5 adsets / 17 anuncios del 12-sep (estaban en pausa, faltaban los verticales y la revisión del copy FP).
- [ ] Partnership Ad con Force (0031): falta vincular la identidad del partner.
- [ ] Canibalización: había 3 campañas de adquisición en paralelo en ago-26. Validar si se consolidaron.
- [ ] Acortador o redirect propio para el link-in-bio de IG (`go.amazingcare.cl/bio`, sin confirmar).

## Fuentes
- session_01MLGvNVcyGZBjw1Ey4x8HPU: war room Cyber oct-26, jefe de campañas → artifact https://claude.ai/artifact/4NHYGwnx1PFnXEVMp12b7S
- session_01Nrexzj2hLLxfP4wYyJS75r: auditoría de Google Ads (4-sep)
- session_01LPpgs61HBBdc6YNkTamUe4: tracking UTM del link-in-bio (1-sep)
- session_01Lete8uGMuJPaG3Gy8QkcMA: clasificación FP/AON y creación de adsets (11/12-sep)
- session_01XgqVQT3837vaL1jcGtqGMT: análisis de ads de agosto y migración ABO→CBO (25-ago)
- session_01Dix3y3CxXhRZp5tgjF9rA1: estrategia de Ads Retail (25-ago)
- session_01BVePuAZzyGKWnTLxrwckRG: reporte semanal (21-ago)
- session_014qJfxPHjDMJgFTkac6jMLo: reporte sep 1–14 → https://claude.ai/code/artifact/a43e7192-a677-47b6-af35-8dc3d02bda97
- session_01QUkQ6zmmEVF2WciHSJVky6: derivación de tráfico de Google Ads al blog. Solo se leyó el pedido inicial; no hay conclusiones.
