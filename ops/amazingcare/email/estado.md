# AmazingCare · OS Email (Klaviyo, CRM, retención)

## Estado actual
**Último dato leído: 29 oct 2026 (Klaviyo y Shopify, 1–29 oct). Command: ver `command/URL`. Los dashboards anteriores (95qFrTBGfTPqeE8UcJYDZH, por marca, y KEm68mZ8Ezs6RXWkw1cAZc, combinado) quedan congelados · datos en `os-data.json`.**

### 30-oct · Fichas para diseño y peso de los correos
- **Fichas N01–N12 creadas en la grilla de Notion** con Aprobación final = Producción. N04 queda en Sin empezar porque falta la noticia. Links en `noviembre/fichas-notion.md`. Cada ficha tiene la referencia copiada de la página NOVIEMBRE, la composición con copy y las indicaciones para diseño, en 4–5 bloques. La página NOVIEMBRE no se tocó.
- **Peso:** los correos de octubre son 3 cortes PNG de una sola imagen, sin texto vivo, sin alt y con un único link. Pesos: Halloween ~1,86 MB, Valor stick ~0,90 MB y Pack Mix ~0,93 MB. En septiembre hubo cortes de hasta 2,3 MB. El HTML pesa ~15 KB, así que Gmail no recorta: el peso está en las imágenes. Regla nueva: ≤ 800 KB por correo, ≤ 200 KB por imagen, JPG 80% y texto clave en HTML (F10).
- **UTM:** las plantillas traen la UTM tipeada a mano y con errores (utm_campaign=pre-cyber en Valor stick, =haloween en Halloween). F04 se reabre.
- **Artifact Email Noviembre:** se corrigió la fuente "Venta atribuida a email" (el loader no leía la respuesta) y se agregó el enlace al Panel del Motor de Correo (G4oH1DpezsbDeyfJneiWBx), que sigue siendo el diagnóstico del motor.

### Corte 29-oct y plan de noviembre
- **Artifact de trabajo de noviembre:** https://claude.ai/artifact/TyheCMx6pWGUCpiq3c6TEL ("Email Noviembre · AmazingCare"). Es un dashboard con 6 pestañas: resumen de ventas, grilla, flujos con diagramas, campañas, accionables y sistema/claims. Ventas, campañas y flujos se leen en vivo de Shopify y Klaviyo; la grilla, los accionables y las reglas están en `noviembre/*.json`. El Command `command/URL` sigue siendo el tablero del OS.
- **Ventas octubre (Shopify, al 28-oct):** venta total $36,36M, venta neta $29,51M, 777 órdenes, ticket $37.976 y recompra 41,7%. En septiembre: $16,46M y 381 órdenes.
- **Email octubre (Klaviyo, Placed Order por canal):** $9,79M, el 26,9% de la venta total. Sep $3,83M (23,3%) · ago $4,03M · jul $3,19M · jun $5,91M · may $6,34M.
- **Campañas 1–29 oct:** $8,94M y 161 compras en 16 envíos (11 principales + 5 seguimientos), casi todos a base completa (~10.900). Eso pasa el techo de 80.000 destinatarios. Después del Cyber cayó todo: Checklist (26-oct) $26 por destinatario y Creatina AMAZINGWEEN (29-oct) $2 con dato parcial.
- **Flujos en 90 días:** Carritos_AON $1,54M y 27 compras (el que más vende) · Welcome_AON $412K, **en borrador desde el 4-oct** (sep $278K, oct $0) · Postcompra 1 compra en 597 · Recompra_AON 1 compra en 1.026 · Carritos_Cyber en borrador (jun $565K) · Navegación abandonada en borrador, falta la pieza.
- **Top productos en 30 días:** Súper Pack 150 $6,17M · Pack Mix 60 $5,55M · Berries 30 $4,17M (205 órdenes) · Creatina Creapure $2,09M.
- **Lineamientos de noviembre (Notion "NOVIEMBRE"):**
  - 8 correos spot más 4 de Black Friday, del mié 25 a las 10:00 al lun 30 a las 23:59.
  - Descuentos hasta 40% OFF: Electrolitos 30% ($530 el stick), Energy 35% ($780), Fibra 40%, Creatina 30% ($630), Creatina con Electrolitos 30% ($1.399).
  - Envío gratis sobre $50.000. Creatina con Electrolitos disponible desde el 24-nov.
- **Grilla propuesta:** N01–N12 en `noviembre/grilla.json`.
  - Los spot salen a las 14:30, en lunes o jueves, a segmento (Interesados ~3.000 o Compradores ~4.300), con envío gratis como mecanismo.
  - Los de Black salen a las 12:30.
  - Son ~63.900 destinatarios en el mes, bajo el techo de 80.000. La venta proyectada de campañas es ~$6,4M, de la cual ~$5,1M es Black.
  - Las 5 filas viejas de noviembre en la grilla de Notion tienen propuesta de qué hacer en `noviembre/grilla_previa.json`.
- **Estándar (sistematización en Notion, resumido en `noviembre/reglas.json`):**
  - Horarios: evento a las 12:30, contenido y segmento a las 14:30, nunca entre 18:00 y 19:00. Mejores días: jueves y lunes.
  - Frecuencia: 6–8 spot, techo de 80.000 destinatarios y nunca un tercer envío en 7 días al mismo segmento.
  - Reenvío a no-abridores: sí.
  - Asuntos: mecanismo en los primeros 40 caracteres, en mayúsculas.
  - Estructura de 7 módulos, con mecanismo obligatorio.

### Novedades 19–21 oct
- **Seguimiento de Creatina (no-aperturas):** salió el 19-oct a las 10:57 sin que nadie lo frenara. Llegó a 291 destinatarios, 33% abrió y no hubo compras. Ya no hay nada que decidir.
- **Push_Halloween (19-oct, 20:47):** 10.288 entregados, 22% de apertura, 0,21% de clics, 9 compras y $421K ($41 por destinatario).
- **Campañas 1–21 oct:** $8,29M y 151 compras. Octubre suma 9 envíos principales y 5 seguimientos, sobre el techo de 6–8 al mes.
- **Reseñas (handoff de la sesión "Email — Klaviyo-Loox", 21-oct):** Judge.me está activo, pero convierte ~2% (13 reseñas sobre ~690 órdenes en octubre). Faltan tres cosas: acceso a la configuración y stats de Judge.me (o una llamada de 15 min), decidir si se desinstala Loox y activar el flujo de recordatorio de reseñas en Klaviyo. Quedó como fuga F07.

### Cierre email Cyber oct-26 y post-Cyber (leído el 19-oct)
- **Campañas 1–19 oct:** $7,87M y 142 compras. Durante el Cyber (1–11 oct) fueron $7,45M y 137 compras, con ~$136 por destinatario.
- **Mejor envío:** "Cyber_Valor stick_Correo" (5 oct), con 10.679 entregados, 50 compras y $2,57M ($241 por destinatario).
- **"¡COMENZÓ!" corregido:** desde el 3 oct los envíos a base completa llegan a 10,5–10,9K perfiles. La base es SUSCRIPTORES + Amazing_Todos los compradores + Captura_Welcome_Popup 10%, y excluye Amazing_Compras_14d.
- **Post-Cyber:** PackMix_Push (14-oct) rindió $35 por destinatario y Creatina_5 cosas (17-oct) $6. Los clics bajaron a 0,07–0,10%: hay fatiga. El seguimiento de Creatina a no-aperturas estaba programado para el 19-oct a las 10:57.
- **Flujos 1–19 oct:** el de carrito trajo 13 compras y $735K, pero su primer correo (5 min) tuvo 0 compras. Post-compra y Recompra_AON tuvieron 0 compras.
- **Pop-up:** 18 vistas y 12 envíos entre el 28 sep y el 18 oct. Sigue casi sin mostrarse.
- **UTM:** las 13 campañas de octubre tienen `add_tracking_params` activo. Faltan los flujos y validar en GA4.

### Histórico (dato al 4 oct)
- **Base:** ~10,8–11K perfiles en Klaviyo. Conversión atribuida con Placed Order `RP5iQ9`, ventana de 5 días.
- **Envíos Cyber oct-26:**

| Correo | Envío (hora Chile) | Entregados | Apertura | Clics | Compras | Venta atribuida |
|---|---|---|---|---|---|---|
| Pre-Cyber "Prepara tu carrito" | 1 oct 21:31 | 7.858 | 26,4% | 0,9% | 17 | $1,09M |
| "¡COMENZÓ! Hasta 40% OFF" | 2 oct 12:17 | 3.037 (solo 28% de la base) | 20,5% | 1,3% | 7 | $422K |
| "¡NUEVA! Creatina Creapure" | 3 oct 20:37 | 10.825 | 9,9% (dato parcial) | 0,2% | 2 | $125K |

  - Total: 26 compras y $1,64M. Un correo a base completa rinde ~$139 por destinatario (~$1,25M netos si llega a toda la base).
  - El flujo de carrito en el evento aportó 2 compras por $109K (51 destinatarios). El día 1 había enviado 13 correos sin compras.
  - Seguimiento programado: "¡Creatina AmazingCare ahora formato stick!", lunes 5 oct 20:37, a no-aperturas.
- **Agosto-26:** campañas $2,83M y flujos $554K (snapshot del command center, se excluyen las etiquetas NO USAR/Nutrikit).
- **Julio-26:** 11 envíos → $3,34M, con apertura de 26,4%. Fue el peor mes del año en apertura.
- **Sep 1–14:** email $200K y 26 órdenes (reporte quincenal).
- **Captura:** en el CyberDay jun-26 el pop-up de Klaviyo casi no se mostró (0–6 vistas al día contra 1.000–2.400 sesiones diarias). El gap de recuperación de carrito en eventos se estimó en $600–750K "dejados en la mesa".
- **Patrón operativo:** las campañas se crean y envían el mismo día. En ago-26 no había nada programado con anticipación (Scheduled = 0).

## Decisiones tomadas
- **20-ago (Fiestas Patrias):**
  - Código **CELEBRACONAMAZING** al 25% en todo el catálogo, **solo por cupón** (no automático). El código va grande en las piezas comerciales.
  - En los educativos el código va en el bloque de cierre, no en el hero.
  - Se adapta lo ya aprobado sumando la "capa 18 sept"; no se rehace.
  - Calendario FP: Pack Mix (sáb 23) · "Se Adelantó el 18" (lun 24, 25% + código en el hero) · Mundo Bio Jumbo (jue 27, 20% en retail del 25-ago al 22-sep, **fuera del cupón**) · Bajón 3PM (28) · 5 Momentos (4-sep) · Manchas Blancas (6-sep, "últimos días").
  - Amazing Contigo y Concurso son iniciativas, no piezas de oferta.
- **Regla del cliente (Frani, 20-ago):** el código de descuento y el envío gratis van en piezas distintas, en paralelo. El pop-up FP lleva el Pack Mix.
- **Asuntos:** el % va dentro de los primeros 40 caracteres y la mecánica en mayúsculas.
- **Techo de frecuencia:** 6–8 envíos spot por mes. Agosto quedó en 11 por el adelanto de FP (no se sacó ninguno porque no hubo instrucción).
- **Oct-26:** no se envía nada sin confirmación. Las recomendaciones quedan como borrador.

## Pendientes / próximos pasos
- [x] **Cierre email del Cyber oct-26:** hecho el 19-oct (ver arriba).
- [x] (Resuelto: desde el 3-oct se envía a base completa.) Recomendación del 4-oct: reenviar "¡COMENZÓ!" al ~72% que no lo recibió (envío inteligente apagado o asunto distinto), más un envío a base completa el lunes 5 (CyberMonday) y otro el miércoles 7 ("últimas horas"). No hay confirmación de que se haya ejecutado.
- [ ] Arreglar la visibilidad del pop-up de captura y la recuperación de carrito antes del próximo evento. Se evaluó sumar recuperación por WhatsApp.
- [ ] **UTMs:** las campañas ya los llevan. Faltan los flujos y validar en GA4 (F04).
- [ ] **Post-Cyber:** bajar la frecuencia a base completa y segmentar por enganche (F05). Requiere OK.
- [ ] **Flujos de post-compra y recompra sin compras:** revisar timing, oferta y CTA (F06).
- [ ] **Reseñas (F07):** acceso a Judge.me, decidir sobre Loox y activar el flujo de recordatorio en Klaviyo. Requiere OK.
- [ ] **Antes de Black (todo requiere OK; detalle en la pestaña Accionables del artifact):**
  - [ ] A01 · Encender Welcome_AON (F08).
  - [ ] A02 · Armar Carritos_Black desde Carritos_Cyber (F09).
  - [ ] A03 · Cargar N01–N12 en la grilla de Notion.
  - [ ] A04 · Pop-up de captura.
  - [ ] A05 · Cerrar con Frani la mecánica de Black y la noticia de N04.
  - [ ] A06 · Recompra por formato.
  - [ ] A07 · Escalera del carrito.
  - [ ] A08 · Post-compra y pedido de reseña.
  - [ ] A10 · Audiencias de la semana Black.
  - [ ] A11 · Dominio y UTM en plantillas.
- [ ] Mantener `os-data.json` y el Command al día en cada cierre (contrato del Command Center).
- [ ] Pendientes FP que quedaron abiertos: fecha de activación y bases del concurso (el correo del 1-sep estaba mal calendarizado), y copy y propuesta del Plan Amazing Contigo. Validar si se cerraron (sin confirmar).
- [ ] Huincha "18 sept" en los flujos: el cliente la dejó en radar para planificar cambios masivos con más tiempo en la próxima campaña.

## Fuentes
- session_01MLGvNVcyGZBjw1Ey4x8HPU: Klaviyo Cyber oct-26 (war room https://claude.ai/artifact/4NHYGwnx1PFnXEVMp12b7S, pestaña Status/Stock)
- session_01X7qEXaRtGv6z36odTW5a3t: campaña Fiestas Patrias, grilla de correos y comentarios en Notion (20-ago)
- session_01X6TVMKPeTJfuPs56hHBmVw: Reporting Master (reporte de email de agosto embebido en el command center)
- session_01BVePuAZzyGKWnTLxrwckRG: reporte semanal (códigos, CARRITO10)
- Notion: Grilla de correos, Lineamientos AGOSTO, Lineamientos anuales 2026
