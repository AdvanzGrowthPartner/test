# Las 18 acciones del Email Engine — detalle operativo

Cada acción sigue la misma estructura: **Tipo · Qué es · Qué necesita · Dificultad · Métricas promedio · Tiempo y carga de equipo · Checklist de implementación · Do's / Don'ts · Conexión con el engine · Ejemplo de correo**.

Métricas son benchmarks DTC de referencia (Klaviyo/industria), no promesas. Se ajustan por vertical y madurez de lista.

---

## FASE 1 · CAPTURA & BASE
*¿A quién le hablo? — El cimiento. Sin esto, nada funciona.*

### 1.1 Captura de lista
- **Tipo:** Base · Ejecución
- **Qué es:** El mecanismo que convierte un visitante anónimo en un contacto con el que se puede hablar: popup, formulario o landing con incentivo claro.
- **Qué necesita:** Plataforma de email · popup/form · incentivo (cupón) · 1 campo de segmentación.
- **Dificultad:** Baja · cualquiera, sin equipo técnico.
- **Métricas:** Tasa de captura 2–5% del tráfico · incentivo típico 10–15% off · setup 1–2 días.
- **Tiempo y carga:** Setup 2–3 h una vez · mantención casi 0 (automático). No suma carga recurrente, pero depende 100% de que llegue tráfico.
- **Checklist:**
  - [ ] Popup o form activo con incentivo claro
  - [ ] Incentivo definido (no "10% genérico" sin ancla)
  - [ ] Pide al menos 1 dato para segmentar
  - [ ] El form conecta directo al flujo Welcome
- **Do's:** Ofrecer valor real por el email · pedir el mínimo de campos · conectar directo al Welcome.
- **Don'ts:** Pedir demasiados datos de entrada · popup que aparece al instante · dejar la lista sin incentivo.
- **Conexión:** Acquisition (sin tráfico no hay a quién captar) · CRO (el popup vive en el sitio).
- **Ejemplo:** Popup "Sumate y llevá 10% en tu 1ª compra" → campo email → CTA "Quiero mi descuento".

### 1.2 Segmentación por intención
- **Tipo:** Base · Data
- **Qué es:** Agrupar la base en cohortes según comportamiento (compró, abandonó carrito, solo navegó, no abre). El mismo correo rinde hasta 6× distinto según a quién llega.
- **Qué necesita:** Eventos de tracking · segmentos dinámicos · definición de cohortes.
- **Dificultad:** Media · encargado / con apoyo.
- **Métricas:** 4–6 cohortes base · uplift vs blast 2–6× por cohorte · setup 2–3 días.
- **Tiempo y carga:** Setup 2–3 h una vez · ajuste ~1 h/mes. Los segmentos dinámicos se actualizan solos. Suma poca carga pero hace eficiente todo lo demás.
- **Checklist:**
  - [ ] 4–6 cohortes por comportamiento
  - [ ] Segmentos dinámicos (no listas fijas)
  - [ ] Cada flujo anclado a una cohorte
  - [ ] Segmento de no-activos para excluir del blast
- **Do's:** Usar segmentos dinámicos · separar activos de no-activos · anclar cada flujo a una cohorte.
- **Don'ts:** Mandar todo a "toda la base" · usar listas estáticas que envejecen · ignorar a los no-abridores.
- **Conexión:** Systems (el reporting devuelve data que afina las cohortes) · todo el canal (cada flujo se ancla a un segmento).
- **Cohortes canónicas por rev/contacto (referencia Advanz):** Comprador 30d (el más alto) > Active-on-site > Carrito 45d > Suscriptor genérico (el más bajo).

### 1.3 Setup de deliverability
- **Tipo:** Base · Revisión semanal
- **Qué es:** La base técnica invisible: autenticar el dominio (SPF, DKIM, DMARC) y calentarlo. Si falla, no importa cuán bueno sea el correo — cae en spam.
- **Qué necesita:** Acceso al DNS del dominio · dominio de envío · monitor de reputación.
- **Dificultad:** Alta · requiere apoyo técnico.
- **Métricas:** Spam rate objetivo < 0,3% · bounce sano < 2% · setup 3–5 días + calentamiento.
- **Tiempo y carga:** Setup 3–5 h + calentamiento · monitoreo ~30 min/semana. Necesita revisión semanal ligera. Si se descuida, arrastra la reputación de toda la cuenta.
- **Checklist:**
  - [ ] SPF, DKIM y DMARC verificados
  - [ ] Dominio de envío dedicado y calentado
  - [ ] Spam rate monitoreado < 0,3%
  - [ ] Limpieza de rebotes activa
- **Do's:** Autenticar antes del primer envío · calentar el dominio gradualmente · monitorear reputación semanal.
- **Don'ts:** Enviar masivo desde dominio nuevo · comprar listas (destruye reputación) · ignorar hard bounces.
- **Conexión:** Systems (la reputación se vigila en el reporting) · Feedback (win-back y sunset la protegen).

---

## FASE 2 · BIENVENIDA
*¿Qué le ofrezco al que entra? — Fundacional. Lo primero que debe existir.*

### 2.1 Welcome Series ⭐ CORE
- **Tipo:** Clave · Ejecución
- **Qué es:** Serie automática que se dispara al suscribirse — el pico de intención de marca. Educa el problema, presenta la oferta ancla (bundle, no unidad) y entrega el incentivo con urgencia.
- **Qué necesita:** Lista con captura · 3–4 emails · cupón de bienvenida.
- **Dificultad:** Media · encargado de email.
- **Métricas:** Open rate 40–55% · CV% 8–15% · rev/contacto el más alto del sistema.
- **Tiempo y carga:** Setup 6–8 h (copy + diseño + armado) · mantención ~1 h/mes. Alto esfuerzo una vez, casi nulo después. Es lo primero que debe existir: rinde solo mientras entra tráfico.
- **Secuencia:** Email 1 bienvenida + cupón (inmediato) → Email 2 por qué el producto (+1d) → Email 3 prueba social + best-seller (+2d) → Email 4 urgencia del cupón (+4d).
- **Checklist:**
  - [ ] Flujo Welcome activo (no en draft)
  - [ ] Mínimo 3 emails en la serie
  - [ ] Entrega el incentivo prometido en la captura
  - [ ] Split por apertura (reenvía al que no abre)
  - [ ] Salida automática al comprar
- **Do's:** Enviar el 1º correo al instante · anclar el bundle, no la unidad · cerrar con urgencia del cupón.
- **Don'ts:** Dejar pasar horas para el 1º correo · vender de más sin educar · olvidar la salida al comprar.
- **Conexión:** Offer (ancla el bundle; sin oferta no hay qué vender) · Acquisition (se llena con la captura).

### 2.2 Bundle / producto de entrada
- **Tipo:** Clave
- **Qué es:** El correo de bienvenida ancla el bundle como producto de entrada, no la unidad. El cliente entra con ticket alto y percibiendo la marca como solución integral.
- **Qué necesita:** Bundle armado · PDP del bundle · comparativa de precio.
- **Dificultad:** Media · encargado + producto.
- **Métricas:** Uplift AOV +15–25% · vs unidad suelta ticket 2–3×.
- **Tiempo y carga:** Vive en Offer/producto · 0 h recurrente en email. No es carga de email: es una decisión de oferta que el correo ejecuta.
- **Checklist:**
  - [ ] Bundle definido como producto de entrada
  - [ ] Welcome destaca el bundle, no la unidad
  - [ ] Muestra el ahorro vs comprar suelto
  - [ ] CTA lleva a la PDP del bundle
- **Do's:** Mostrar el ahorro del bundle · posicionar como solución integral · bundle como CTA principal.
- **Don'ts:** Empujar la unidad más barata · esconder el precio del bundle · ofrecer demasiadas opciones a la vez.
- **Conexión:** Offer (esta pieza ES parte de Offer) · CRO (la PDP del bundle debe convertir).

---

## FASE 3 · VALIDACIÓN
*¿Qué mensaje convierte? — Aprende antes de escalar.*

### 3.1 A/B de asunto y oferta
- **Tipo:** Data · Revisión semanal
- **Qué es:** Cada campaña prueba dos versiones (asunto u oferta) y el ganador se replica. Convierte el envío en un experimento que mejora con data, no con intuición.
- **Qué necesita:** Volumen mínimo por variante · registro de resultados.
- **Dificultad:** Baja · encargado de email.
- **Métricas:** Muestra mínima ~1.000 por variante · el asunto mueve más (open) · ganador +10–30% open típico.
- **Tiempo y carga:** +15 min por campaña · revisión semanal de ganadores. Suma poco tiempo por envío pero exige disciplina de revisión. Sin registro, no aprende.
- **Checklist:**
  - [ ] A/B de asunto en cada campaña
  - [ ] Se prueba oferta dura vs blanda por cohorte
  - [ ] El ganador se documenta y replica
  - [ ] Registro de aprendizajes mensual
- **Do's:** Probar una variable a la vez · esperar significancia antes de decidir · documentar cada ganador.
- **Don'ts:** Cambiar 5 cosas y no saber qué ganó · decidir con muestra chica · olvidar registrar el aprendizaje.
- **Conexión:** Systems (los ganadores se documentan en el reporting) · Alcance (el aprendizaje mejora las campañas).

### 3.2 Quiz / zero-party data
- **Tipo:** Data · Optimización
- **Qué es:** Un quiz ("encuentra tu producto") captura la preferencia que el cliente declara explícitamente. Es el dato más limpio para segmentar y recomendar el producto correcto.
- **Qué necesita:** Herramienta de quiz · mapa respuesta→producto · integración con la base.
- **Dificultad:** Alta · con apoyo (setup) · luego autónomo.
- **Métricas:** CV% quiz hasta ~46% · vs directo a PDP ~3% · completion 60–80%.
- **Tiempo y carga:** Setup 8–12 h · mantención casi 0. Optimización de nivel medio-alto. No urge al arranque; entra cuando ya hay tráfico que vale la pena calificar.
- **Checklist:**
  - [ ] Quiz corto disponible (post-suscripción o en sitio)
  - [ ] Cada respuesta mapea a cohorte/producto
  - [ ] El resultado personaliza el Welcome
  - [ ] Los datos del quiz escriben en el perfil
- **Do's:** Mantenerlo corto (3–5 preguntas) · recomendar un producto al final · guardar las respuestas en el perfil.
- **Don'ts:** Hacerlo largo y tedioso · no dar resultado accionable · perder el dato capturado.
- **Conexión:** Foundations (el dato vuelve a la segmentación) · Acquisition (puente entre contenido y producto).

---

## FASE 4 · ALCANCE
*¿Cómo llego a la base? — Escala.*

### 4.1 Campañas (calendario)
- **Tipo:** Volumen · Ejecución · Revisión semanal
- **Qué es:** El envío manual a la base (calendario + eventos como Cyber/Black Friday). Genera volumen y presencia; su eficiencia depende de cuán segmentado esté.
- **Qué necesita:** Calendario de contenido · segmentos · plantilla de evento · copy + diseño por envío.
- **Dificultad:** Media · encargado + producción.
- **Métricas:** Open rate 25–35% · CV% 0,1–0,2% · frecuencia 1–3/semana.
- **Tiempo y carga:** Por campaña 2–4 h (copy + arte + armado). A 2/semana ~24–32 h/mes; a 3/semana ~36–48 h/mes. **LA MAYOR CARGA RECURRENTE DEL CANAL.** A más volumen, necesita producción dedicada o el ritmo se cae.
- **Checklist:**
  - [ ] Calendario mensual definido
  - [ ] Campañas segmentadas (no "a todos")
  - [ ] No-activos excluidos del blast
  - [ ] Plantilla de evento lista (para Cyber/Black Friday)
- **Do's:** Versionar por cohorte · excluir a los no-activos · tener lista la plantilla de evento.
- **Don'ts:** Mandar lo mismo a toda la base · sobre-enviar y quemar la lista · improvisar en fechas clave.
- **Conexión:** Contenido & Diseño (cada envío consume producción) · Validation (el A/B mejora cada campaña).
- **Nota Advanz:** En eventos, el flujo de carrito rinde ~15× más por contacto que el blast masivo. El blast trae volumen; el flujo trae eficiencia.

### 4.2 Browse Abandonment
- **Tipo:** Optimización · Ejecución
- **Qué es:** Flujo que se dispara cuando alguien ve un producto pero no lo agrega al carrito. Recupera intención antes de que se enfríe, con recordatorio dinámico del producto visto.
- **Qué necesita:** Evento "vio producto" · bloque de producto dinámico.
- **Dificultad:** Media · encargado de email.
- **Métricas:** Open rate 30–40% · CV% 0,4–0,8% · emails 2–3.
- **Tiempo y carga:** Setup 3–4 h · mantención casi 0 (automático). Se arma una vez y corre solo. Optimización que suma poca carga pero recupera tráfico tibio que se perdía.
- **Secuencia:** Email 1 "¿lo seguís pensando?" (+4h) → Email 2 objeción + FAQ (+1d) → Email 3 prueba social (+3d).
- **Checklist:**
  - [ ] Flujo Browse activo
  - [ ] Recordatorio dinámico del producto visto
  - [ ] Filtro que lo separa de Carrito y Post-compra
  - [ ] Salida al agregar carrito o comprar
- **Do's:** Mostrar el producto exacto que vio · aportar valor (no solo "volvé") · salir si avanza a carrito.
- **Don'ts:** Ser agresivo con quien solo mira · ofrecer descuento demasiado pronto · solaparse con el flujo de carrito.
- **Conexión:** Acquisition (captura intención del tráfico entrante) · CRO (depende de que la PDP registre la vista).

---

## FASE 5 · CONVERSIÓN
*¿Cómo cierro la venta? — Convierte al caliente.*

### 5.1 Carrito Abandonado ⭐ CORE
- **Tipo:** Clave · Ejecución
- **Qué es:** Se dispara cuando el cliente agrega al carrito y no compra. Intención máxima: ya eligió producto. Recordatorio suave → objeción + beneficio → incentivo final con urgencia.
- **Qué necesita:** Evento de carrito · 3 emails · cupón de cierre.
- **Dificultad:** Media · encargado de email.
- **Métricas:** Open rate 40–50% · CV% 3–5% · recupera 5–11% de carritos · rev/contacto muy alto.
- **Tiempo y carga:** Setup 5–7 h · mantención ~1 h/mes · en eventos +2 h por versión especial. Junto al Welcome, lo segundo que debe existir. En eventos requiere versión especial programada 48h antes.
- **Secuencia:** Email 1 recordatorio suave sin descuento (+1h) → Email 2 envío gratis/objeción (+24h) → Email 3 cupón leve + urgencia (+48h).
- **Checklist:**
  - [ ] Flujo Carrito activo
  - [ ] 1er correo sin descuento (proteger margen)
  - [ ] Escalado de incentivo en el 3er correo
  - [ ] Salida inmediata al comprar
  - [ ] Versión de evento lista y programada 48h antes
- **Do's:** Recordar sin descuento primero · resolver la objeción (envío, dudas) · cerrar con urgencia real.
- **Don'ts:** Regalar descuento en el 1º correo · esperar demasiado para el 1º envío · activar el flujo tarde en eventos.
- **Conexión:** Offer (recuerda el bundle elegido) · CRO (depende del checkout de la tienda).

### 5.2 Checkout Abandonado
- **Tipo:** Optimización · Ejecución
- **Qué es:** Distinto del carrito: este llegó a la página de pago y se cayó. La intención es aún más alta, así que el flujo es más corto y directo, con foco en resolver fricción.
- **Qué necesita:** Evento "checkout started" · 2 emails.
- **Dificultad:** Media · encargado de email.
- **Métricas:** Open rate 45–55% · CV% 4–8% · emails 1–2.
- **Tiempo y carga:** Setup 2–3 h · mantención casi 0. Corto y automático. Baja carga. Complementa al carrito recuperando al que ya intentó pagar.
- **Secuencia:** Email 1 recordatorio directo (+30min) → Email 2 urgencia + soporte/objeción (+12h).
- **Checklist:**
  - [ ] Flujo Checkout separado del de Carrito
  - [ ] 1er correo dentro de la 1ª hora
  - [ ] Ofrece ayuda/soporte, no solo descuento
  - [ ] Salida inmediata al comprar
- **Do's:** Enviar rápido (dentro de 1h) · ofrecer ayuda, no solo descuento · facilitar retomar el pago.
- **Don'ts:** Confundirlo con carrito genérico · tardar horas en el 1º correo · asumir que fue falta de interés.
- **Conexión:** CRO (a veces revela fricción técnica del checkout) · Workflows (se separa del flujo de carrito).

---

## FASE 6 · RETENCIÓN
*¿Cómo vuelven y multiplican? — El canal empieza a exigir cruzar áreas.*

### 6.1 Post-Compra / Recompra ⭐ CORE
- **Tipo:** Clave · Ejecución · Data
- **Qué es:** Se dispara con la compra. Agradece y enseña a usar el producto, hace cross-sell según lo comprado, y dispara la reposición al ciclo de consumo. Es la palanca real del ticket.
- **Qué necesita:** Evento de compra · lógica de cross-sell · ciclo de consumo estimado.
- **Dificultad:** Alta · encargado + data de producto.
- **Métricas:** Open rate 35–45% · repeat rate +10–20% · emails 3–4.
- **Tiempo y carga:** Setup 6–9 h (varios splits) · mantención ~1–2 h/mes. Necesita data de producto (ciclo de consumo, complementos). Es donde el canal empieza a exigir cruzar áreas.
- **Secuencia:** Email 1 gracias + cómo usar (+1d) → Email 2 cross-sell por producto comprado (+7d) → Email 3 reposición "¿se te acaba?" (+28d) → Email 4 invitación a suscripción (+30d).
- **Checklist:**
  - [ ] Flujo Post-compra activo
  - [ ] Split de cross-sell según producto comprado
  - [ ] Reposición ajustada al ciclo real de consumo
  - [ ] Puente a suscripción para consumibles
- **Do's:** Educar el uso primero · cross-sell lógico (complementos) · timing de reposición al consumo.
- **Don'ts:** Vender de más el día 1 · recomendar lo que ya compró · ignorar el ciclo de reposición.
- **Conexión:** Retention (depende de que el producto satisfaga) · Producto (necesita ciclo de consumo y cross-sell lógico).

### 6.2 Referidos · "Regala a un amigo"
- **Tipo:** Clave · Data · Optimización
- **Qué es:** El comprador satisfecho recibe un beneficio por traer a un amigo: le regala un descuento y, al canjearlo el amigo, ambos ganan. Convierte un cliente en canal de adquisición a costo casi cero y motiva la recompra de quien refiere. **El único flujo que adquiere Y retiene a la vez.**
- **Qué necesita:** App/sistema de referidos · doble incentivo · link único por cliente.
- **Dificultad:** Alta · con apoyo (setup app) · luego autónomo.
- **Métricas:** Nuevos clientes 10–30% del total · CVR referido 3–5× vs frío · efecto baja CAC + recompra.
- **Tiempo y carga:** Setup 8–12 h (app + flujo) · mantención ~1 h/mes. Requiere una app de referidos. Entra cuando ya hay base de compradores felices — por eso aparece recién a 60k.
- **Mecánica del doble incentivo:** El amigo recibe -X% en su primera compra; el que refiere recibe crédito al canjear el amigo. El crédito trae de vuelta al referidor = recompra.
- **Secuencia:** Disparar tras compra + review positiva (cliente feliz) → Email 1 "regala -20% a un amigo y gana crédito" con link único → Email 2 recordatorio "tu amigo aún no usó tu regalo" (+5d) → al canjear, ambos reciben beneficio automáticamente.
- **Checklist:**
  - [ ] Programa de referidos con doble incentivo definido
  - [ ] Flujo dispara tras compra + señal de satisfacción
  - [ ] Link único de referido por cliente
  - [ ] Correo de recordatorio si el amigo no canjea
  - [ ] Beneficio automático al canjear (ambos lados)
- **Do's:** Recompensar a ambos lados · disparar cuando el cliente está feliz · hacer el compartir de 1 clic.
- **Don'ts:** Premiar solo a uno · pedir referidos antes de entregar valor · complicar el canje.
- **Conexión:** Acquisition (trae clientes nuevos a costo casi cero) · Retention (el crédito trae de vuelta al referidor) · Producto (solo funciona si el producto satisface).
- **Benchmark:** Programas bien armados aportan 10–30% de nuevos clientes con CVR 3–5× sobre tráfico frío.

### 6.3 Suscripción
- **Tipo:** Optimización · Data
- **Qué es:** Para consumibles, la suscripción convierte la recompra repetida en ingreso predecible. El correo la propone cuando el cliente ya validó el producto (2ª–3ª compra).
- **Qué necesita:** Opción de suscripción en la tienda · beneficio de recurrencia · gestión self-service.
- **Dificultad:** Alta · con apoyo (setup) · producto.
- **Métricas:** Uplift LTV 2–4× · descuento típico 10–15% · churn objetivo < 8% mensual.
- **Tiempo y carga:** Setup 10–15 h (tienda + flujo) · mantención ~2 h/mes gestión. La más pesada de montar: toca la tienda, el pago y el flujo. Solo a escala (100k), cuando el patrón de recompra ya está probado.
- **Checklist:**
  - [ ] Opción de suscripción disponible en el producto
  - [ ] Flujo que la propone tras la 2ª–3ª compra
  - [ ] Beneficio claro de recurrencia (precio/regalo)
  - [ ] Gestión de suscripción self-service
- **Do's:** Ofrecerla cuando ya hay hábito · dar un beneficio real por suscribir · facilitar pausar/cancelar.
- **Don'ts:** Forzarla en la 1ª compra · esconder cómo cancelar · ofrecer sin ventaja clara.
- **Conexión:** Retention (el corazón de la recurrencia) · CRO/Tienda (requiere infraestructura de suscripción) · Systems (se automatiza al final).

---

## FASE 7 · FEEDBACK
*¿Qué dice la gente y qué limpio? — Refina.*

### 7.1 Solicitud de review / UGC
- **Tipo:** Ejecución · Data
- **Qué es:** Tras la entrega, pide una reseña. Las reviews y el UGC que captura alimentan la prueba social de los demás flujos (Welcome, Browse, Carrito) y la oferta.
- **Qué necesita:** Evento de entrega · app de reviews · incentivo leve.
- **Dificultad:** Media · encargado de email.
- **Métricas:** Tasa de respuesta 5–15% · timing 3–7 días post-entrega.
- **Tiempo y carga:** Setup 3–4 h · mantención casi 0 · curar UGC ~1 h/mes. Automático, baja carga. Su valor real está en reutilizar el UGC en los otros flujos.
- **Checklist:**
  - [ ] Flujo de solicitud de review activo
  - [ ] Se dispara al entregar (no al comprar)
  - [ ] Incentivo por reseña con foto/UGC
  - [ ] El mejor UGC se reutiliza en otros flujos
- **Do's:** Pedir después de recibir el producto · facilitar dejar la reseña · reutilizar el UGC en otros flujos.
- **Don'ts:** Pedir review antes de que llegue · complicar el proceso · desperdiciar el UGC capturado.
- **Conexión:** Feedback (esta pieza ES Feedback) · Offer/CRO (el UGC sube conversión en Welcome y Carrito).

### 7.2 Win-back + Sunset
- **Tipo:** Optimización · Revisión semanal
- **Qué es:** Para los que no abren hace 60–90 días: un intento fuerte de reactivación y, si no responde, se suprime del blast. Limpia la base y sube el open rate de todos los envíos.
- **Qué necesita:** Segmento de no-abridores · 2 emails · regla de supresión.
- **Dificultad:** Media · encargado de email.
- **Métricas:** Reactivación 5–15% del segmento · efecto sube open rate global · ciclo 60–90 días.
- **Tiempo y carga:** Setup 3–4 h · revisión mensual del segmento. Protege la reputación que sostiene la llegada de todos los demás correos.
- **Secuencia:** Email 1 "te extrañamos" + oferta fuerte → Email 2 última oportunidad (+5d) → suprimir del blast si no reacciona (+10d).
- **Checklist:**
  - [ ] Segmento de no-abridores 60–90d definido
  - [ ] Flujo de reactivación activo
  - [ ] Regla de supresión automática (sunset)
  - [ ] Los suprimidos salen del blast masivo
- **Do's:** Hacer una oferta fuerte y clara · suprimir si no reacciona · proteger la reputación del dominio.
- **Don'ts:** Seguir enviando a quien nunca abre · postergar la limpieza · confundir sunset con borrar contactos.
- **Conexión:** Foundations (protege la deliverability de la base) · Systems (la limpieza mejora las métricas del reporting).

---

## FASE 8 · SISTEMA
*¿Qué automatizo de lo validado? — Último. Nunca al principio.*

### 8.1 Automatizar lo validado
- **Tipo:** Optimización · Revisión semanal
- **Qué es:** Solo se automatiza el flujo que ya demostró conversión. Automatizar algo no validado escala el caos. Primero se prueba (fases 2–7), luego se sistematiza.
- **Qué necesita:** Flujos con CV% probada · 2–4 semanas de data · monitoreo.
- **Dificultad:** Media · encargado / operaciones.
- **Métricas:** Tiempo de validación 2–4 semanas · criterio CV% comprobada.
- **Tiempo y carga:** Gobierno continuo · requiere alguien que vigile el sistema. No es un flujo, es una disciplina de operación. A escala necesita a alguien dueño del sistema.
- **Checklist:**
  - [ ] Cada flujo automatizado tiene CV% comprobada
  - [ ] Nada se automatiza sin 2–4 semanas de data
  - [ ] Monitoreo de que la automatización no degrada
  - [ ] Documentación de cada flujo activo
- **Do's:** Validar antes de automatizar · documentar cada flujo activo · revisar que no degrade.
- **Don'ts:** Automatizar por automatizar · escalar un flujo sin data · dejar flujos sin dueño.
- **Conexión:** Systems (esta pieza ES Systems) · todo el canal (ordena y estabiliza lo validado).

### 8.2 Reporting → próxima vuelta
- **Tipo:** Data · Revisión semanal
- **Qué es:** La data del mes (qué cohorte convirtió, qué asunto ganó, qué flujo rindió) vuelve a la fase 1 y afina la segmentación. Cada vuelta del engine arranca mejor que la anterior.
- **Qué necesita:** Fuente de datos limpia · reporte por flujo y cohorte · ritual mensual.
- **Dificultad:** Media · encargado / con analista.
- **Métricas:** Frecuencia mensual · corta por flujo + cohorte · compara vs media / mes anterior.
- **Tiempo y carga:** Por mes 3–5 h de análisis · a escala pide perfil de análisis dedicado. Ritual mensual fijo. A 100k deja de caber en el encargado. Sin este loop, el canal no aprende ni escala.
- **Checklist:**
  - [ ] Reporte mensual de email establecido
  - [ ] Se mide por flujo Y por cohorte (no solo total)
  - [ ] Comparativa vs media / mes anterior
  - [ ] Los aprendizajes vuelven a la segmentación
- **Do's:** Medir por flujo y cohorte · comparar contra una media · cerrar el loop hacia la fase 1.
- **Don'ts:** Mirar solo el total · reportar sin accionar · dejar la data sin realimentar.
- **Conexión:** Systems (esta pieza ES Systems) · Foundations (su salida vuelve a la segmentación) · Data/Dashbo (depende de una fuente limpia).
