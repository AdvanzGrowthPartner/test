# Event Calendar — el año completo de eventos DTC (Chile)

El skill no piensa en "el cyber". Piensa en **un calendario anual de olas de demanda**, cada una con su fecha, su estacionalidad, su mecánica y su ventana de lead-time. La pregunta base siempre es: *¿qué ola viene, cuánto falta, y alcanza el tiempo para surfearla bien?*

> Las fechas exactas cambian cada año. Confirmar el año en curso con el volumen de búsquedas (`data-pull.md`) y con la fuente oficial cuando aplique (CyberDay/CyberMonday los organiza la **Cámara de Comercio de Santiago**, sitio Cyber.cl). Acá van las ventanas típicas.

---

## Mapa anual (Chile)

| Evento | Ventana típica | Vertical que más tracciona | Mecánica dominante |
|--------|----------------|-----------------------------|--------------------|
| **San Valentín** | 14 feb | skincare (gifting), moda, joyas, regalos | Gifting + set/bundle, urgencia de fecha |
| **Vuelta a clases** | fin feb – 2ª sem mar | consumible, hogar, moda básica | Reposición, packs, precio |
| **Día de la Mujer** | 8 mar | skincare, moda, wellness | Regalo/auto-regalo, contenido |
| **Día de la Madre** | 2º domingo de mayo | skincare, moda, joyas, gifting | Gifting premium, sets, envío a tiempo |
| **CyberDay** | inicios de junio (lun-mié, 3 días) | transversal — el peak anual del DTC | Descuento profundo, urgencia 72h |
| **Día del Padre** | 3er domingo de junio | moda, tech, gifting masculino | Gifting, sets |
| **Fiestas Patrias / 18** | mediados de septiembre | consumible (comida/bebida/asado), moda, hogar | Reposición + volumen, packs |
| **CyberMonday** | inicios de octubre | transversal (2º peak del año) | Descuento profundo, urgencia |
| **Halloween** | 31 oct | nicho (disfraz, skincare temática) | Nicho/temático |
| **Black Friday / Black Week** | último viernes de nov + semana | transversal, fuerte en moda y tech | Descuento profundo, se estira a "week" |
| **Navidad** | diciembre (peak 1-20 dic) | gifting transversal, skincare, moda, juguetes | Gifting + **deadline de envío** crítico |
| **Liquidación fin de temporada** | ene-feb / jul (cambio estación) | moda sobre todo | Remate de stock/tallas, margen bajo |
| **Evento propio de marca** | aniversario / lanzamiento / restock | cualquiera | Definido por la marca; menos ruido competitivo |

**CyberDay Chile mueve >US$500M en 3 días** — es el punto de inflexión anual de ingresos para un DTC. Black y CyberMonday son el 2º y 3er peak.

**Novedad GEO (Cyber.cl "Cyber AI"):** el sitio oficial estrena un agente conversacional que recomienda productos en lenguaje natural. Es superficie de descubrimiento nueva: la calidad de datos de producto (títulos, atributos, schema) influye en si recomienda la marca. No es accionable a último minuto, pero es punto para la estrategia GEO del año (`advanz-seo-geo-engine`).

---

## Regla de oro: la FECHA importa tanto como el evento

Dos cosas que el skill nunca puede ignorar:

### 1. Posición dentro del mes vs ciclo de pago
En Chile los sueldos caen típicamente **a fin de mes y alrededor del día 5**. Eso cambia el bolsillo del comprador:

- **Evento a fin de mes / principios (post-sueldo):** bolsillo lleno. Se puede empujar ticket más alto, bundles, AOV. La conversión de impulso es más fácil.
- **Evento a mediados de mes (pre-sueldo, bolsillo apretado):** la sensibilidad al precio sube. Funciona mejor la cuota sin interés, el envío gratis, el ticket más bajo, y el mensaje de "aprovecha ahora / paga después". Proyectar más conservador.
- **Cuándo cae exactamente:** CyberDay (inicios de junio) suele pillar bolsillo relativamente fresco; un evento propio a mediados de mes hay que apalancarlo distinto. Siempre mirar el día real del evento contra el ciclo de pago y ajustar mecánica + proyección.

### 2. Estacionalidad de la categoría (la ola de búsquedas)
Cada categoría tiene su curva anual de demanda, que **se adelanta a la venta**. Ejemplos: skincare sube pre-Madre y pre-Navidad; moda de abrigo sube en otoño; consumible de asado explota pre-18. El skill saca esta curva del **volumen de búsquedas** (`data-pull.md`) para saber *con cuánto tiempo adelantarse*: la campaña se prepara cuando la búsqueda empieza a subir, no cuando ya explotó.

---

## Ventanas de lead-time (cuánto tiempo hay que adelantarse)

El "reloj" del flujo. Contrastar T-N (días al evento) contra la ventana mínima de la vertical. Si T-N < mínimo → se entra tarde: acotar alcance y decirlo.

| Fase de producción | Cuándo debe estar lista (antes del evento) | Qué incluye |
|--------------------|---------------------------------------------|-------------|
| **Definición de oferta** | T-21 a T-14 | Qué SKUs, qué descuento real, qué bundles, umbral de envío gratis, margen chequeado |
| **Tracking QA** | T-14 | Pixel/CAPI Meta, conversiones Google/TikTok, GA4, UTMs de email marcando fuente |
| **Crecimiento de lista** | T-21 → T-1 | Popup early-access ("entérate primero"), captura barata = revenue owned en el peak |
| **Creativos** | T-10 a T-5 | 3-5 variantes por canal, listas para rotar |
| **Audiencias** | T-10 | Retargeting calentando, lookalikes, custom de la lista |
| **Warm-up de campañas** | T-5 a T-1 | Subir budget gradual para entrar con learning resuelto, no en frío |
| **Cadencia de email planificada** | T-7 | Teaser → live → midpoint → last-chance |
| **Sitio listo para carga** | T-3 | Velocidad móvil, apps no críticas pausadas, plan de triage de CVR |

**Lead-time mínimo por vertical (regla gruesa):**
- **Moda:** ~21-28 días (lookbook/creativo visual, curva de tallas, definir liquidación vs novedad).
- **Skincare:** ~14-21 días (educación/regimen, sets de gifting, sampling).
- **Consumible:** ~10-14 días (más simple: packs, stock depth, reposición) — pero el stock hay que asegurarlo antes.

Si el reloj no alcanza la ventana mínima → **no cancelar: acotar**. Entrar con un solo ganador + un canal + owned, y marcar que se llegó tarde. (Regla "siempre proponer algo" en `leverage-scoring.md`.)

---

## Estacional vs Always-on (dos mundos, no confundir)

El skill distingue siempre en qué mundo está la sugerencia:

| | **Estacional (evento)** | **Always-on** |
|---|---|---|
| Precio | Descuento real 30-70%, remate | Plano / precio lista |
| Motor | **Urgencia** ("se viene", "últimas horas"), escasez, deadline | Demanda continua, educación, LTV |
| Comunicación | Countdown, teaser → live → last-chance | Flujos evergreen, contenido, retención |
| Objetivo | Volumen, liquidar unidades, capturar cohorte | Margen estable, recurrencia, base |
| Cuándo el skill lo recomienda | Hay ola + ganador + stock + margen para descontar | No hay ola clara, o margen no tolera descuento, o se llegó muy tarde |

**Regla:** si NO hay condiciones para estacional (sin ola, sin margen, o tarde), la recomendación por defecto es **always-on reforzado** (más presión en el canal más rentable a precio plano), no forzar un descuento que quema margen. Eso es "siempre proponer algo" sin romper la caja.

---

## Fases del evento (heredadas, para el handoff)

Este skill trabaja sobre todo la fase **PRE**. Para el detalle de PEAK (ejecución en vivo) y POST (retención del cohorte) el motor es `ecomm-cyber-audit` (`references/cyber-playbook.md`). Nombrarlas en el preview para que el consultor vea el arco completo:

- **PRE (T-N a T-1):** preparar munición — oferta, tracking, lista, creativos, audiencias, warm-up. Restricción típica: falta de munición. ← **acá vive este skill.**
- **PEAK (evento en curso):** mover la restricción cada 3-6h. ← `ecomm-cyber-audit`.
- **POST (T+1 a T+14):** retener el cohorte, correr la cola, debrief. ← `ecomm-cyber-audit`.

**Trampa Chile (recordar siempre en el preview):** no inflar precios en las semanas previas para fingir descuento mayor. Comparadores (Knasta, SoloTodo) exponen el salto y hay riesgo Sernac + reputacional. El descuento debe ser real.
