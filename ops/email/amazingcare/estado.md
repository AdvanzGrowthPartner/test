# AmazingCare · OS Email (Klaviyo, CRM, retención)

## Estado actual
**Último dato leído: 19 oct 2026 (Klaviyo, 1–19 oct). Dashboard del OS: https://claude.ai/artifact/95qFrTBGfTPqeE8UcJYDZH · datos en `os-data.json`.**

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
- [ ] Mantener `os-data.json` y el dashboard al día en cada cierre (contrato del Command Center).
- [ ] Pendientes FP que quedaron abiertos: fecha de activación y bases del concurso (el correo del 1-sep estaba mal calendarizado), y copy y propuesta del Plan Amazing Contigo. Validar si se cerraron (sin confirmar).
- [ ] Huincha "18 sept" en los flujos: el cliente la dejó en radar para planificar cambios masivos con más tiempo en la próxima campaña.

## Fuentes
- session_01MLGvNVcyGZBjw1Ey4x8HPU: Klaviyo Cyber oct-26 (war room https://claude.ai/artifact/4NHYGwnx1PFnXEVMp12b7S, pestaña Status/Stock)
- session_01X7qEXaRtGv6z36odTW5a3t: campaña Fiestas Patrias, grilla de correos y comentarios en Notion (20-ago)
- session_01X6TVMKPeTJfuPs56hHBmVw: Reporting Master (reporte de email de agosto embebido en el command center)
- session_01BVePuAZzyGKWnTLxrwckRG: reporte semanal (códigos, CARRITO10)
- Notion: Grilla de correos, Lineamientos AGOSTO, Lineamientos anuales 2026
