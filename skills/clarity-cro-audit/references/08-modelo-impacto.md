# Modelo de impacto

Convierte hallazgos en pedidos y en margen. Sin costos: la skill no estima honorarios ni precios
de desarrollo. Estima **esfuerzo en días** y **retorno en pedidos**; quien lea pone el resto.

---

## La brecha por dispositivo es el mejor techo disponible

El método más honesto para proyectar impacto no es un benchmark de internet: es **el mismo
sitio en otro dispositivo**.

```sql
FROM sessions SHOW sessions, sessions_with_cart_additions, sessions_that_reached_checkout,
     sessions_that_completed_checkout, conversion_rate
GROUP BY session_device_type SINCE -90d UNTIL today
```

Si desktop convierte 5,54% y móvil 2,83% con el mismo catálogo, los mismos precios y las mismas
reseñas, entonces **la diferencia es de interfaz, no de producto ni de audiencia**. Eso da:

```
techo teórico   = sesiones_móvil × cvr_desktop − pedidos_móvil_actuales
objetivo real   = un tercio de esa brecha
```

Un tercio es la regla conservadora: móvil nunca iguala a desktop (contexto, distracción,
webview in-app), pero cerrar un tercio de una brecha del mismo sitio es defendible ante
cualquiera. Y a diferencia de un benchmark, **el cliente no puede discutirlo**: son sus propios
números.

## Proyección por hallazgo

Cada ticket declara su palanca mecánica, no un porcentaje mágico:

| Hallazgo | Palanca | Cómo se estima |
|---|---|---|
| F1 CTA bajo el pliegue | Exposición al CTA de `r%` a ~90% | `sesiones × (0,90 − r) × tasa_entre_expuestos / 6` |
| F2 Acantilado | Retención en la banda de `x%` a `x+20` | `sesiones × 0,20 × tasa_atc_actual` |
| F4 Información escondida | Fricción de decisión | +0,5 a +1 punto de carros |
| F6 Cupón | Paso carro → checkout | `carros × (nuevo% − actual%)` |
| F5 Escalera de precios | Ticket promedio | `% de pedidos que suben un escalón × Δprecio` |
| Checkout | Paso checkout → compra | `checkouts × (nuevo% − actual%)` |

**El divisor por 6 en F1** es deliberadamente conservador: quien ve el botón porque una barra
se lo puso delante está menos comprometido que quien llegó ahí scrolleando.

Y el techo de cada objetivo se fija con la tasa de desktop, no con la ambición. Si desktop hace
12,43% de carro y móvil 8,75%, el objetivo del ticket es 10,75%, no 15%.

## Solapamiento

Los hallazgos que actúan sobre la misma audiencia **no se suman**. Factor de **0,65** a la suma
bruta de los que comparten plantilla y segmento. Sin ese factor el reporte promete el doble de
lo que puede entregar.

## De pedidos a margen

```
pedidos_hoy         = sesiones × atc × paso_checkout × cierre
pedidos_proyectados = sesiones × atc' × paso_checkout' × cierre'
Δventas             = (pedidos_proy × ticket × (1 + Δticket)) − (pedidos_hoy × ticket)
Δmargen             = Δventas × margen
```

Solo dos cosas no salen de la plataforma: el **margen de contribución** y, a veces, el objetivo.
Todo lo demás es dato. Deja el margen marcado como supuesto, en un campo editable, y que el
resto se recalcule solo.

**No proyectes retorno sobre inversión ni payback.** No conoces sus costos, y meterlos vuelve
discutible un cálculo que hasta ahí era sólido.

## Rangos, no números

Extremo bajo: solo funcionan los dos tickets de mayor confianza. Extremo alto: funcionan todos.
Y una frase de falsación: «por debajo del extremo bajo, la hipótesis era incorrecta y hay que
volver a las grabaciones».

---

## Cuándo se ve la señal

**Descriptiva — 72 horas.** Dice si el cambio hizo lo que debía, no si vendió más. Mapa de
desplazamiento, clics sobre el elemento nuevo, cobertura de un evento. No requiere significancia
porque no es una comparación: es una verificación.

**De negocio — depende del volumen.**

```
n_por_brazo ≈ 16 × p̄ × (1 − p̄) ÷ δ²
```

- **A/B al 50%:** `2 × n ÷ sesiones_diarias`
- **Despliegue directo, lectura pre/post:** `n ÷ sesiones_diarias`

Para el ticket promedio la unidad es el pedido, no la sesión.

## Cronograma tipo

| Momento | Qué | Señal |
|---|---|---|
| Día 1–3 | Medición + verificación de errores + auditoría de checkout | Misma semana |
| Día 4–5 | CTA fijo | 72 h descriptiva · 10–14 d negocio |
| Día 6–12 | Reordenamiento de la ficha | 72 h scroll · 14 d carros |
| Día 13–16 | Cupón, card, precios | 10 d paso a checkout · 21 d ticket |
| Día 45 | Primera lectura consolidada | Comparable contra el trimestre |
| Semana 6–8 | Arquitectura de catálogo | 30 d posiciones orgánicas |
