# Leverage Scoring — ¿hay ola? ¿cuánto leverage? ¿qué movimiento?

El skill no aprueba campañas: **detecta oportunidad y la puntúa por leverage.** Este archivo dice cómo, y cómo llegar siempre a un movimiento (nunca un no-go seco).

---

## Los 4 tests de oportunidad

Correr los 4 sobre la data (`data-pull.md`) antes de puntuar. Cada uno es sí/parcial/no.

1. **¿Hay ola de demanda?** El volumen de búsquedas de la categoría sube hacia el evento **y/o** el histórico propio del cliente muestra peak en ese evento. (Sin ola → el evento es empujado por precio, no por demanda — proyectar conservador.)
2. **¿Hay ganador surtible y con margen?** Existe ≥1 producto ganador (`product-classification.md`) con stock proyectado para el peak y margen que tolera el descuento planeado. (Sin esto → no hay punta de lanza para paid.)
3. **¿Hay canal rentable para empujarlo?** El histórico de tráfico (`order_referrer_source`) o el Meta pasado muestran al menos un canal con retorno para esa categoría. (Sin esto → apoyarse en owned/orgánico.)
4. **¿Alcanza el tiempo?** T-N ≥ lead-time mínimo de la vertical (`event-calendar.md`). (Si no → acotar alcance, no cancelar.)

---

## El score de leverage (por movimiento candidato)

Para cada movimiento posible (empujar el ganador X por Meta, armar bundle Y, arreglar el fantasma Z, exprimir la lista, etc.):

```
Leverage = (Impacto esperado × Probabilidad de éxito) ÷ (Esfuerzo × Tiempo requerido)
```

- **Impacto:** cuánto revenue/AOV mueve, contra el baseline propio.
- **Probabilidad:** qué tan probado está (ganador con histórico > fantasma sin arreglar > apuesta nueva).
- **Esfuerzo × Tiempo:** producción, budget, coordinación — y **si el reloj lo permite**. Un movimiento de alto impacto que no cabe en T-N tiene leverage bajo *para este evento*.

Rankear los movimientos. Los **3 de mayor leverage** son el corazón del preview. El #1 debería ser, casi siempre, empujar al ganador probado por su canal más rentable — es lo más seguro y de mayor retorno.

---

## Estacional vs Always-on (qué mecánica recomienda el score)

Cruce de los tests con la mecánica (detalle en `event-calendar.md`):

| Situación | Mecánica recomendada |
|-----------|----------------------|
| Ola sí + ganador con margen + tiempo ok | **Estacional full:** descuento real, urgencia, teaser→live→last-chance, escalar paid en el ganador |
| Ola sí + margen ajustado | **Estacional suave:** descuento moderado + bundle para proteger margen + fuerte en owned (barato) |
| Sin ola clara **o** margen no tolera descuento | **Always-on reforzado:** precio plano, más presión en el canal más rentable, contenido, sin quemar margen |
| Tiempo insuficiente (T-N < mínimo) | **Entrada acotada:** un solo ganador + un canal + owned; declarar que se llegó tarde |

---

## Regla dura: SIEMPRE proponer un movimiento

Nunca devolver "no hay oportunidad, no hagas nada". Siempre hay un piso:

- **Poca ola →** always-on reforzado en el ganador (capturar la demanda base mejor, sin descuento profundo).
- **Sin margen para descuento →** bundle/AOV + owned, no oferta que quema caja.
- **Se llegó tarde →** entrada chica de un ganador + owned (lo más rápido de activar).
- **Catálogo débil (puros fantasmas/zombies) →** arreglar la ficha del mejor fantasma como jugada de mediano plazo + always-on mientras tanto.

**Pero ser tosco con el riesgo:** cada movimiento va con su riesgo explícito y su nivel de confianza. "Se puede entrar, pero con esta plata y este stock el techo es X; el riesgo es Y." El consultor decide el sí/no — el skill nunca romantiza una oportunidad que no está.

---

## Preguntas de discovery al consultor (lo que la data no dice)

Antes de cerrar la estrategia, preguntar esto (agrupado, no de a una). Son las variables que ni Shopify ni las búsquedas revelan:

**Del evento pasado:**
- ¿Qué se vendió la vez pasada en este evento? ¿Cuál fue el hero?
- ¿Qué campaña / canal / creativo funcionó y cuál no?
- ¿Qué se nota que faltó (creativo, segmento, flow, stock)? — para no repetirlo.

**De recursos y límites:**
- ¿Hay presupuesto aprobado para este evento? ¿De cuánto? ¿Aprobado por quién (ABC / dueño)?
- ¿Qué stock real se puede comprometer del/los ganador(es)?
- ¿Qué margen tolera descuento en cada ganador? (define estacional vs always-on)
- ¿Hay capacidad de producción (creativo, email) para el reloj que queda?

**De objetivo y no-negociables:**
- ¿Cuál es el objetivo del evento (volumen / margen / captar cohorte / liquidar stock)?
- ¿Qué cosas NO se pueden dejar de lado sí o sí este evento?
- ¿Hay algún lanzamiento, restock o fecha propia que se cruce?

**Regla de cierre:** el skill entrega la **primera estrategia base** con lo que sabe + supuestos declarados, y usa estas preguntas para afinar. El consultor lidera con el cliente hasta validar; el sí/no final y el cierre humano no son del skill.
