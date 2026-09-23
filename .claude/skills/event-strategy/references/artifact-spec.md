# Artifact Spec — el preview visual de la campaña

El output central del skill es un **artifact HTML self-contained** que previsualiza la campaña y proyecta el resultado. Regla de oro: **cualquiera lo entiende en 60 segundos y ve dónde está la oportunidad y el foco de mayor leverage.** No es un dashboard de data — es un *preview de decisión*.

**TODO es una declaración visual** (no párrafos): cada bloque se muestra como gráfico, timeline, matriz, barra o semáforo — texto solo para el veredicto y las etiquetas. El objetivo es dar claridad de "cómo se ve" ANTES de activar. Se construye **recién después de las 8 respuestas del intake** (`intake.md`), nunca antes.

Construir con `web-artifacts-builder` (o `diagram-engine` para las piezas de mapa/matriz). Cargar `artifact-design` antes de escribir. Un solo archivo, responsive, theme-aware, sin dependencias externas fuera del allowlist.

### Piezas visuales obligatorias
- **Header "Análisis de marca → [URL]"** con las **variables analizadas** como chips (las 10 de la batería ecommerce en `intake.md`): facturación, AOV, zonas de mayor venta, avatar/recurrencia, colecciones, producto, canales, envío, tendencia, oportunidad/gap.
- **Cronograma en GANTT** (barras por fase de producción sobre un eje de fechas T-N → evento → post), no una lista.
- **Matriz de producto visual** con los 4 roles etiquetados: 🟢 **ganador** · 🔵 **sidekick (acompañamiento)** · 🟠 **fantasma** · ⚫ **zombie**.
- **Tendencia** ("dónde se mueve la tendencia"): curva/heat del evento pasado + estacionalidad de demanda, marcando el peak y el valle.
- **Estructura de oferta y campaña**: visual (tarjetas/arco), qué pack ancla, qué sube AOV, qué comunica cada fase.
- **Tiempo de preparación**: legible del propio Gantt (semáforo 🟢/🟡/🔴 del reloj).
- **Proyección**: rango visual (conservador/esperado/stretch) + confianza.

### Módulos ampliados (war room de campaña)
El output evolucionó de "preview" a **war room**: además de lo anterior, incluir cuando la data lo permita —
- **Gráficos combinados reales** (usar Chart.js UMD desde cdnjs, pinneado; temear leyendo las CSS vars):
  - *Tendencia*: **barras sesiones + barras ventas + línea CR%** (diario del evento pasado). El insight suele ser que el CR sube y el tráfico es plano.
  - *A quién le vendes vs conversión*: **barras (sesiones/ventas) + línea CR%** por dispositivo / segmento / canal.
  - *Zonas de venta y conversión*: gráfico **vertical**, con **todas las regiones/zonas con venta** (no solo el top). Las barras van en **volumen de pedidos**, no en facturación (el volumen ordena mejor la cola larga y evita que una zona con ticket alto distorsione), + **línea CR% por región** en eje secundario. Ordenar por pedidos desc.
- **Oferta irresistible (visual):** el mix como stack **ancla (bundle) → upsell de carrito → crosssell**, + una **matriz de test** (variante × hipótesis × métrica × qué ganó) para ver cómo testear antes del peak.
- **Proyección interactiva:** slider de **inversión media** + split Meta/Google + ROAS editable → **calcula revenue por canal (Google y Meta) y MER en vivo** (JS vanilla). Declarar que el ROAS es supuesto de planificación.
- **Calculadora de volumen de creativos:** slider de inversión + mezcla video/estático → **# de conceptos, videos (UGC/creador) y estáticos recomendados**, con la lógica de *volumen mínimo para que la plataforma distribuya* ("con poca plata no dispersar; con mucha, necesitas volumen real").
- **Distribución por rendimiento:** cómo repartir budget por canal pre‑evento vs peak, y la regla viva (+20% al que supera ROAS objetivo, 3x kill, proteger lo que funciona) → deriva a `ecomm-cyber-audit`.
- **Salida orgánica + email + anuncios:** playbook visual (qué avisar/postear/links; secuencia teaser→live→last + flujos carrito/browse/post‑compra; estáticos vs video UGC según inversión).
- **Landing de campaña `/cyber` (o `/black`):** medir tráfico y CR de la URL del evento por fuente, aislado del resto del sitio; base de retarget.

### UX (no negociable) — estética Shopify / Polaris
- **Look & feel tipo admin de Shopify (Polaris):** ground gris claro, cards blancas con borde sutil y radio ~12–14, verde marca #008060, tipografía Inter + IBM Plex Mono para datos. Claro y aireado; dark = slate, nunca negro. Si el usuario ofrece pantallazos de su Shopify, pedirlos para calibrar.
- **Header STICKY que funciona de índice:** barra fija arriba con anclas a cada sección (`#s1`…`#sN`) + `scroll-behavior:smooth` y `scroll-margin-top`. Permite saltar directo a cualquier punto.
- **Cards siempre "normal vs cyber":** cada métrica clave se muestra comparada — día normal → día evento + el multiplicador (facturación, órdenes, CR, AOV). El evento no sube el ticket: multiplica volumen y conversión.
- **Canales reales, no lumps:** nunca escribir "owned+search". Desglosar los canales que corren de verdad (Google, Meta [IG+FB], Directo/Marca, Orgánico, Email/Owned) con su revenue real y estado (corriendo / por conectar). Email suele caer en "directo" por falta de UTM → marcarlo.
- **Proteger marcos y rangos:** nada se sale de su caja; ejes con min/max; overflow controlado. Fechas y badges grandes; leyendas **laterales**.
- **Días del evento separados** (ej. 5 · 6 · 7, no "5–7") con su % esperado de venta por día.
- **Gantt con "qué definir / qué comunicar / qué asegurar / qué calentar"** desglosado en boxes, no solo la barra. Incluir la fase de **comunicación** (teaser/anticipo) y la de **retención** post-evento.
- **Fotos de producto y creativos (feature obligatorio):** el artifact SIEMPRE llama las imágenes reales. Traer por MCP `featuredMedia.preview.image.url` de Shopify (y, si aplica, creativos de Meta), armar un **catálogo en JS** (nombre, precio, stock, estado, url) y renderizar:
  - **Galería "Catálogo en vivo"** de tiles de producto (foto + precio + stock reales) en la sección de productos.
  - **"Vista previa de anuncio"** con la MISMA foto del hero en los 3 formatos que hay que redimensionar: **1:1 (feed), 4:5 (feed vertical), 9:16 (stories/reels)**, con badge del evento, gancho, precio tachado→oferta y CTA. Así se representan los "ads" aunque no se ejecute nada.
  - **Miniaturas reales en el carrito** (§ oferta) para el pack ancla y el GWP.
  - **Patrón técnico (clave):** cada imagen es `<img src="{url CDN}" onerror="this.remove()">` **sobre un tile/fondo de marca por sabor o tipo** (limón, maracuyá, naranja, berries, mix, accesorio). Donde el entorno permite el CDN (Claude Code local, HTML descargado, sitio del cliente) se ven las **fotos reales**; donde el visor de claude.ai bloquea hosts externos por CSP, cae al **tile de marca** y nunca se ve roto. Egress del entorno suele bloquear `cdn.shopify.com` → **no se pueden bajar los bytes para data URI**, así que el visor de claude.ai muestra el fallback; entregar además el **archivo HTML** (se abre en el navegador del usuario con las fotos reales) y decirlo explícito. Nunca prometer fotos reales dentro del preview de claude.ai sin allowlistear `cdn.shopify.com`.
- **Oferta con la lógica del porqué** (por qué el GWP, por qué el upsell, por qué el crosssell), visual, con imágenes de producto.
- **Proyección:** escenario del evento **fijo/normalizado** (no movible) + un **planificador de pauta interactivo** aparte (slider de inversión con tope realista — p.ej. $10M en cyber — que alimenta a TODOS los outputs siguientes, incluida la calculadora de creativos, sin re-mover). Meta = azul, Google = amarillo. Incluir **MER explicado con fórmula**, **ROAS medio sin evento / en eventos** (por validar si no hay data de ads), e **histórico real de eventos** (año, inversión, revenue, MER).
- **Volumen de creativos:** slider **video↔estático** (el video convierte mejor) enganchado a la MISMA inversión; # conceptos escala con presupuesto (volumen mínimo para que la plataforma distribuya).
- **Distribución por rendimiento:** barras **verticales agrupadas** (fase × canal), no barras laterales.
- **Salida = comportamiento del evento en el tiempo:** un flujo temporal (teaser→VIP→live→proof→last→cola) + orgánico/email/anuncios.
- **Landing `/cyber`:** **emular visualmente la página** (mock con barra de URL, hero, productos) + qué medir y por qué.
- Todo interactivo es JS vanilla o Chart.js (UMD desde cdnjs, pinneado); sin dependencias fuera del allowlist del Artifact.

### Refinamientos de detalle (aprendidos en cliente)
- **Fondo con aura de marca:** base clara con auras radiales suaves de los colores de la marca (Advanz) detrás del contenido (`body::before`, opacidad baja). Nunca compite con la data.
- **Gantt con rol + qué verificar por etapa:** cada fila del Gantt lleva su **rol** y su **checklist de verificación** inline; sin chips decorativos sueltos debajo. Barras grandes.
- **Oferta = AHORRO primero:** el héroe del mensaje es el ahorro (en sticks, en producto y en envío), no el precio bajo. El **GWP (regalo) va SIEMPRE atado al pack, nunca suelto** (regalar suelto = regalar margen). El carrito muestra precio tachado + "ahorras $X".
- **Proyección:** los supuestos (inversión/ROAS por escenario) van en una **mini-tabla lateral** que acompaña las barras, no en texto chico. Escenario tope = "todo sale bien" (no inflar; respetar el ROAS techo histórico de la cuenta).
- **Distribución de inversión conectada al planificador:** las barras de $ por fase se recalculan con el slider de inversión y el split (no valores hardcodeados); mostrar la referencia del evento anterior.
- **Landing con 3 vistas (home · PDP · carrito), las 3 obligatorias**, con **marcadores numerados flotantes** en el mock conectados por número (01, 02…) a la checklist de must-haves. Envío gratis y countdown visibles en las 3.
- **Checklist por área + por etapa:** 6 áreas (Producto y stock · Web & CRO · Social Media · Campañas · Email · Revisor final), cada una verificable pre/durante/post. Ver `event-checklist.md`.

---

## Módulos v2 — el war room completo (canónico, aprendido en producción)

Estos módulos son el estándar actual del artifact. Todo lo que se refiera a un **producto o un canal va como ficha con logo/color** (fichas que se componen entre sí), no como texto suelto.

**A. Capa de datos / fuentes conectadas (primer bloque, arriba del todo).** Grid de cards con **logo real de cada fuente** (Shopify, Klaviyo, Meta, Google, Notion, TikTok) + qué alimenta cada una + estado *conectado*. Mensaje: "data real, nada inventado — todo sale de estas conexiones sobre las fechas reales del evento". **Los logos van como SVG inline** (no favicons ni imágenes externas: el egress y la CSP los bloquean; el SVG inline siempre se ve). Google = "G" a 4 colores; Meta = loop; el resto, marca+letra.

**B. Tendencia DENTRO del evento vs EVENTO vs EVENTO (dos bloques distintos, no confundir).** *Tendencia dentro del evento* = día a día de UN evento (sesiones+ventas+CR%). *Evento vs evento* = comparar dos ediciones entre sí (ej. CyberDay Jun vs CyberMonday Oct): split por día, por canal y por producto, con el titular de comportamiento (creció por **volumen** o por **ticket**).

**C. Matriz de producto = 4 cuadrantes** (no lista): **Ganadores** (estrella, potenciar) · **Sidekicks** (acompañan, upsell/cross) · **Perdedores** (tráfico que no cierra, solo orgánico) · **Zombies** (sin movimiento, fuera). Eje = plata que movió × rol; cada producto es una ficha con mini-color + $ real. **Mecánica de Ganadores explícita** (con el porqué): despacho gratis + GWP (vaso/botella) atado al pack + upsell en PDP y carrito.

**D. Oferta = bundles tipo checkout Shopify**, armados del **producto real (MCP)**: ancla / upsell / crosssell como product-cards (foto, precio tachado→oferta, ahorro, "por qué") + el carrito mock. Se lee como el checkout real.

**E. Creativos = ÁNGULOS, no dimensiones.** Cada ángulo (dolor · solución · ahorro · prueba social · autoridad · urgencia) con su **claim** (el copy) y su **CTA**. Explicar cómo se trabaja cada ángulo (estático 4 pilares + video UGC). Los formatos (1:1/4:5/9:16) son secundarios, no el eje. **Campañas y creativos idealmente en un solo bloque.**

**F. Lógica de canales (Meta vs Google).** Meta **full desde el D1** (agarra el vuelto antes, remarketea por audiencia); Google **sube en el peak** (cierra por intención y distribución). Ponerlo como fichas con logo.

**G. Gantt por canal, a ~10 días con los días marcados** (calentamiento · on-event · post). Lanes: Social · Email · SEO · Campañas. Los **correos salen por día** (mostrar el envío diario), los **flujos y campañas son permanentes**.

**H. Funnel HORIZONTAL (no vertical), evento vs tradicional + proyección.** Sesiones → add to cart → checkout → venta, con el % en cada paso; marcar la **fuga del pago**. Debajo: CR día normal → CR evento (×2,5) → **CR proyectado si se tapan las fugas** (la conversión de evento no es lineal: sube mucho "si se da con la tecla").

**I. Captura por tráfico (form Klaviyo).** Mini-funnel: sesiones → **vieron el form** (view rate) → **lo enviaron** (submit rate) → suscriptores. Proyección: subir view rate y submit rate escala la captura. Notar que la mayoría del tráfico es **móvil** → form mobile-first.

**J. Recuperación de carro: normal vs evento.** Comparar el flujo de carrito en período normal (recipients→ventas→$ recuperado, rev/recipient) vs la ventana del evento. El patrón real: en el evento el flujo suele **casi no disparar** (flujo Cyber en borrador) → cuantificar la **plata en la mesa** (abandonos × rev/recipient normal).

**K. CRO = el sitio en modo Cyber (no hacemos landers).** El framing correcto: *no se arma una landing aparte, se pone TODO el sitio en descuento + add-ons de conversión en home/PDP/carrito.* Mostrar los 3 mocks (home·PDP·carrito) + los add-ons como **chips cortos** (countdown, envío gratis, upsell, reviews, mobile <3s, checkout+UTMs), con su impacto — **sin párrafos largos**.

**L. No repetir + Verificar (juntos).** Los errores del evento anterior con su fix + el check final pre-D1. "Descartar / no repetir / verificar" son la misma decisión (qué NO hacer).

**M. Engine de escalado.** Diagrama de palancas: **pre-cargado** (SEO = intención+posicionamiento previo · Email = captura+FOMO previo · CRO = base + upgrades) → **palancas en vivo** que realmente se escalan (**contenido orgánico + ads**, con gate 48h / +20% al de mejor CPA / 3× kill) → resultado (meta $).

**N. Competidores (radar real).** Rankear por **presencia de pauta real** vía Meta Ads Library (# creativos activos + antigüedad + ángulos), con **link directo a la página de cada uno en la Ads Library**. Marcar dónde estamos y el diferencial. Presupuesto/alcance/seguidores: la Ads Library no los da → dejarlos como "por levantar", no inventarlos.

**O. Lanzamiento de producto nuevo (bloque aislado).** Cuando entra un producto nuevo como upsell: precio (con descuento del evento) · **precio por porción/stick** · precio en pack · ahorro total · **días de uso** · **días "a $0"** (los que paga el descuento) · variaciones de ángulo (precio/día, velocidad de envío, duración). Números que no existan aún = placeholder marcado.

**P. Rentabilidad — "la raya para la suma" (al final).** P&L del evento: Revenue → −COGS → **Margen bruto** → −Inversión ads → −Costo operativo (email·CRO·banners·SEO·flujos·social·creativos·creadores) → **Utilidad**. Más **unit economics**: AOV · margen/orden · **CAC tope** · contribución/orden. Regla comercial: escalar mientras el **CAC ≤ tope**; el cliente suele ganar **por volumen, no por margen**. Y una **comparación de los últimos 3 eventos** (tabla con heatmap) mostrando **dónde se mueve la aguja** (inversión, revenue, ROAS, envíos email, flujos activos, video/UGC, SEO, GWP, deliverability). Pedir al cliente margen%, COGS, CAC tope y AOV reales — no asumir.

**Q. Interactividad que no confunde.** El **planificador** con slider de inversión + **barra de split Meta/Google de dos colores con % explícito** (nunca un slider ambiguo) + ROAS editable → revenue por canal + **gauge de la meta** ($ objetivo). Los **escenarios van como BOTONES** (Conservador/Esperado/Todo sale bien): al tocar uno, el planificador se setea solo y se enciende "qué tiene que pasar".

### Sistema visual v2 (no negociable)
- **Committed light: fondo blanco + color de marca** (aura radial suave de marca detrás). No depender del tema del sistema.
- **Tipografía a máximo 5 tamaños** (ej. 11/13/15/19/24), base ~15px. Nada de 20+ tamaños distintos.
- **Heatmaps verde/rojo en tablas** (verde = mueve la aguja, rojo = fuga/riesgo) con leyenda.
- **Sin emojis como imagen ni como marcador.** Producto/canal → foto real o **card/ficha limpia** (nombre + color de marca), logo SVG, o dot de color. Nunca un emoji de fruta/caja como "foto".
- **Aire entre bloques** (margen generoso entre secciones y dentro de las cards). Nada saturado.
- **Textos de bajada legibles** (nunca gris translúcido que no se lee): los sublabels van en color de marca o muted con contraste.
- **GSAP** (gsap + ScrollTrigger UMD desde cdnjs) para entrada del hero y reveal por scroll, con `prefers-reduced-motion` y `gsap.from` (sin FOUC).

### Límite DURO de imágenes de producto (confirmado en producción)
El egress bloquea `cdn.shopify.com` (403) en **todos los entornos disponibles, incluida una sesión Cowork/remota en red "trusted"**. No hay forma de bajar los bytes por MCP, curl, image-proxy ni Cowork. Y la CSP del visor de claude.ai bloquea hotlink de hosts externos. Por lo tanto, **dentro del preview de claude.ai la foto real no se puede embeber** salvo que:
1. **Infra/IT allowliste `cdn.shopify.com`** en el egress (ahí se bajan y se embeben como data URI), o
2. **El usuario pegue las fotos en el chat** → quedan en el disco de la sesión (`.../images/*.png`) → se leen y se embeben como **data URI** (esto NO pasa por egress y sí funciona).
Mientras tanto: `<img src="{url CDN}">` (se ve en Cloudflare/local/sitio) **sobre una card/ficha de marca limpia** como fallback (sin gradientes rainbow, sin emoji). Entregar además el **HTML** para abrir en el navegador. **Decir la limitación explícito; nunca prometer fotos reales en el preview sin (1) o (2).**

---

## Encabezado (lo primero que se ve)

```
[Cliente] · [Evento] · [fecha del evento]
Veredicto en una línea: [hay ola fuerte, entramos con X / oportunidad media, entrada acotada / sin ola, always-on reforzado]
```
El veredicto sale del scoring (`leverage-scoring.md`). Es honesto y tosco, no vendedor.

---

## Las 6 secciones del preview

### 1. El reloj ⏱️ — ¿cuánto tiempo queda y alcanza?
- Timeline horizontal de HOY → evento, con los hitos de producción (`event-calendar.md`: oferta, tracking, lista, creativos, audiencias, warm-up, email, sitio) ubicados en su T-N.
- Semáforo del reloj: 🟢 holgado / 🟡 justo / 🔴 tarde (contra el lead-time mínimo de la vertical).
- Si es 🔴: banner claro "se entra tarde — alcance acotado a [X]".

### 2. Qué NO puede fallar 🚦 — el checklist tosco
Semáforo de los no-negociables de la vertical (`product-classification.md` §B):
| Ítem | Estado | Nota |
|------|--------|------|
| Tracking (pixel/CAPI/GA4/UTMs) | 🟢🟡🔴 | |
| Stock del/los ganador(es) | 🟢🟡🔴 | |
| Oferta y margen definidos | 🟢🟡🔴 | |
| Sitio/velocidad para carga | 🟢🟡🔴 | |
| [Ítem propio de la vertical: tallas / sets / stock depth] | 🟢🟡🔴 | |
Rojo aquí = riesgo directo a la campaña. Es lo que el consultor tiene que resolver antes.

### 3. Matriz de productos 🎯 — qué entra y con qué rol
- Matriz 2×2 **vistas × ventas** con los SKU ubicados y coloreados: 🟢 ganador / 🔵 acompañamiento / 🟠 fantasma / ⚫ zombie.
- Al lado, la lectura en texto: cuál es el hero, cuál sube AOV, qué fantasma vale la pena arreglar, qué se ignora.
- Marcar stock/margen del ganador (si no hay stock, badge de alerta).

### 4. Mix de canales 📡 — dónde está la plata rentable
- Barras del revenue histórico por canal en ese evento (o baseline): paid (Meta/Google/TikTok), owned (email/SMS), orgánico/directo.
- Marcar el canal más rentable y el de más volumen (no siempre el mismo).
- La recomendación de dónde poner el peso, con el porqué.

### 5. Mecánica de oferta 🏷️ — estacional vs always-on
- Cuál mecánica se recomienda (del scoring) y por qué, en una tarjeta.
- Si estacional: el arco de comunicación (teaser → live → midpoint → last-chance) sobre un mini-timeline.
- Recordatorio de la trampa de precios (Sernac/Knasta): descuento real.

### 6. Proyección 📈 — cómo se vería vs el último evento
Ver método abajo. Mostrar:
- **Rango:** conservador — **esperado** — stretch (barras o bullet), nunca número puntual.
- **vs último evento:** lift esperado sobre el histórico propio.
- **Por canal:** cuánto aporta cada uno en el escenario esperado.
- **Nivel de confianza** declarado (alto si hay histórico propio del mismo evento; bajo si es direccional).
- Los **supuestos** en texto (spend plan, stock, margen) — la proyección es tan buena como ellos.

---

## Cierre del artifact (no es sección de gráfico, es la bajada)

- **Los 3 movimientos de mayor leverage** (del scoring), cada uno con: qué, por qué (dato), impacto esperado, dónde/quién, esfuerzo, y plazo dentro del reloj.
- **Riesgos y no-negociables** en una línea cada uno.
- **Handoff explícito:** "esto es el preview; el consultor valida con el cliente; la ejecución en vivo la toma `ecomm-cyber-audit`."

---

## Método de proyección (lo más delicado — no equivocarse)

Extrapolar lineal está **mal**: las ventas de evento no son uniformes.

**Fórmula (curva de pacing):**
`Total proyectado = ventas acumuladas ÷ % esperado acumulado a esa altura`

**Insumos, en orden de preferencia:**
1. **Curva del propio cliente en el mismo evento anterior** (Shopify, `data-pull.md` §1a) — lo único que captura su patrón real. Confianza alta.
2. **Curva direccional del evento** (`event-calendar.md`) si no hay histórico propio. Declararla como direccional. Confianza baja/media.

**Ajustes obligatorios:**
- **Ola de búsquedas:** si la demanda de la categoría viene fuerte/débil este año, ajustar el esperado.
- **Fecha dentro del mes:** evento post-sueldo → menos conservador; pre-sueldo → más conservador (`event-calendar.md`).
- **Por canal, distinto:** paid escala con el spend que se *va a desplegar* (no con el ritmo actual); owned (email/SMS) es pulsado — sube en cada envío (live/midpoint/last-chance); orgánico/directo surfea la ola.

**Reglas de honestidad:**
- Siempre **rango**, nunca número puntual. Error alto si el histórico es pobre (±25-35%).
- Declarar **confianza** y **supuestos**.
- Si falta una fuente, decirlo en la sección (“Meta no conectado — paid proyectado sobre spend plan × ROAS histórico”). No inventar.

*(Patrón heredado y ampliado de `ecomm-cyber-audit/references/owner-view.md`.)*

---

## Variante Notion (si el consultor la pide)

Si piden dejarlo como página editable para el equipo, volcar el mismo contenido con `advanz-notion-builder` (TL;DR → Mermaid horizontal → secciones escaneables → toggles). El artifact HTML es el preview visual; Notion es el registro editable. Ambos comen de la misma lectura.

---

## Qué NO hacer en el artifact
- No convertirlo en un dashboard de métricas sin bajada. Cada sección apunta a una decisión.
- No mostrar proyección puntual sin rango/confianza.
- No incluir SKU zombie como si fueran opción.
- No prometer ejecución — el artifact previsualiza, no ejecuta.
