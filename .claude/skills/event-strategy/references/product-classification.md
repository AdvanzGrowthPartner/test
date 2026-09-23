# Product & Vertical Classification

Dos clasificaciones que hay que resolver antes de sugerir nada: **qué es cada producto** (para saber qué entra al evento y con qué rol) y **de qué vertical es la tienda** (porque cambia la mecánica, el lead-time y qué no puede fallar).

---

## A. Clasificación de productos (los 4 tipos)

Se calcula cruzando 3 señales de Shopify (`data-pull.md` §1d): **vistas** (demanda/atención), **ventas/unidades** (conversión real), **stock + margen** (capacidad de surtir y de descontar). Ventana de lectura: últimos 60-90 días + el mismo evento del año anterior.

| Tipo | Definición | Señal (vistas × ventas) | Rol en el evento | Qué hacer |
|------|-----------|--------------------------|------------------|-----------|
| 🟢 **Ganador** | Tracciona: vende consistente, tiene demanda y stock, y margen que aguanta descuento | Vistas altas **+** ventas altas | **La punta de lanza.** Es el que se empuja con paid + owned + hero del sitio | Escalar. Asegurar stock. Es el ancla de la oferta y de la proyección |
| 🔵 **Acompañamiento** | No es héroe, pero sube AOV: complementa al ganador, arma bundle, cruza | Ventas medias, alta afinidad con el ganador (se compran juntos) | **Sube la canasta.** Bundle, cross-sell, umbral de envío gratis, upsell post-compra | Emparejar con el ganador. No gastar paid directo en él |
| 🟠 **Fantasma** | Le miran pero no compran: hay demanda, falla la conversión (precio, ficha, prueba social, stock de talla, fricción) | Vistas altas **+** ventas bajas | **Oportunidad escondida.** Si se arregla la ficha/oferta antes del evento, puede pasar a ganador | Diagnosticar y arreglar (PDP, precio, reviews, tallas). Si no da el tiempo, NO empujar con paid |
| ⚫ **Zombie** | Ni lo miran ni lo compran | Vistas bajas **+** ventas bajas | **Peso muerto.** No entra al evento | No gastar un peso en él. A lo sumo, remate silencioso para liberar caja/stock |

**Reglas duras:**
- **Solo se empujan ganadores** con presupuesto de adquisición. Acompañamiento va pegado al ganador (bundle/AOV). Fantasma solo si se alcanza a arreglar la ficha. Zombie nunca.
- **Stock-aware:** un ganador sin stock proyectado para el peak deja de ser ganador para efectos de paid — no se quema budget en demanda que no se puede surtir. Es la fuga más cara y más invisible.
- **Margen-aware:** si el ganador no tiene margen para descuento real, va a always-on (precio plano, más presión de canal), no a oferta profunda.
- Un fantasma bien diagnosticado es el mayor leverage escondido del evento: la demanda ya existe, solo falta desatascar la conversión.

**Cómo se ve en el artifact:** matriz 2×2 con los SKU ubicados por cuadrante y coloreados por los 4 tipos. Aprendido en producción: la matriz **no se explica sola** si solo pinta boxes — hay que rotular los ejes con palabras y dar la lectura. Regla de diseño (ver `artifact-spec.md`):
- **Eje X = ventas/conversión** (izq: poco vende → der: mucho vende). **Eje Y = atención/vistas** (abajo: nadie mira → arriba: mucho miran). Escribir el eje con esas palabras, no solo "vistas/ventas".
- Cada cuadrante lleva **una línea de lectura**: 🟢 arriba-der "miran y compran → escalar" · 🟠 arriba-izq "miran y NO compran → arreglar ficha" · 🔵 abajo-der (o medio) "compra de acompañamiento → bundle" · ⚫ abajo-izq "ni miran ni compran → fuera".
- Nunca dejar la matriz como decoración: cada SKU real ubicado, con su color de tipo.

### La mecánica del ganador (qué se le ata, y por qué)
El ganador no se empuja "a secas" — se le monta una mecánica que sube AOV y protege margen. Patrón canónico (adaptar por vertical):
- **Despacho gratis sobre el pack** (no sobre la unidad suelta) → mueve a multipack y sube ticket.
- **GWP (regalo) atado al pack, nunca suelto** (ej. vaso/botella): el regalo es gancho de AOV, no un SKU que se regala aislado. Si el GWP se puede comprar solo, deja de traccionar el pack.
- **Upsell de acompañamiento en PDP y carrito** (ej. un complemento de alto margen o un lanzamiento): se ofrece donde ya hay intención de compra, con el *por qué* visible (completar la rutina / el ahorro / el uso).
- El **héroe del mensaje es el AHORRO** (por unidad, en producto, envío incluido), no "precio bajo". El precio ancla; el ahorro convence.

Esto se dibuja en el artifact como fichas de producto (foto + rol + qué se le ata), no como texto corrido. Ver `artifact-spec.md` (bundles Shopify-style, upsell chips).

---

## A′. Rentabilidad y unit economics — la raya para la suma

Clasificar qué entra es la mitad; la otra es **si el número cierra**. Antes de cerrar la oferta, resolver la economía unitaria del evento y ponerla en el brief como "raya para la suma":

- **Margen del producto:** cuánto tolera descuento real. Un ganador sin margen va a always-on (precio plano + presión de canal), no a oferta profunda. Leer costo por metafield (`data-pull.md` §1e).
- **CAC techo:** el costo de adquisición máximo que el cliente acepta pagar por una orden. Sobre ese techo, escalar quema caja.
- **AOV objetivo:** el ticket que hace que el CAC techo sea rentable. La mecánica del ganador (multipack + GWP + upsell) existe para **subir el AOV por encima del punto donde el CAC cierra**.
- **La lógica de volumen vs margen:** muchos DTC de consumible **ganan por volumen, no por margen unitario** — aceptan un CAC alto (hasta el techo) porque el LTV/recompra y el ticket lo sostienen. Hay que decir explícito bajo qué lógica juega el cliente: *"rentable hasta CAC $X porque gana por volumen y recompra, no por margen del día"*. No aplicar la lógica de margen a un negocio de volumen ni viceversa.
- **ROAS/MER de equilibrio:** el mínimo para no perder con el descuento del evento. Definir el breakeven y sobre él el objetivo. Regla práctica común: ROAS objetivo ≥ ~5× marca terreno rentable en eventos de consumible con estos números — pero **calcularlo desde el margen real del cliente, no asumirlo**.
- **Comparar los últimos eventos** (2-3 ediciones): inversión / revenue / ROAS / CAC / AOV lado a lado, para ver **dónde se mueve la aguja** y qué palanca (más spend, mejor AOV, mejor CVR) mueve más el resultado.

En el artifact esto es el bloque de **rentabilidad**: P&L simple del evento (revenue − COGS − pauta − operación = contribución), unit economics (margen · CAC techo · AOV · ROAS breakeven vs objetivo) y la tabla comparativa de eventos. Números del cliente, patrón reusable. Ver `artifact-spec.md`.

---

## B. Clasificación de vertical (define la mecánica)

Antes de sugerir oferta/canales/lead-time, definir de qué vertical es la tienda. Se infiere del catálogo (`search_products`, categorías, atributos) y se confirma con el consultor.

### 👗 Moda / apparel
- **Qué manda:** curva de tallas y stock por variante; visual (lookbook, fotografía); temporada.
- **Mecánica de evento:** distinguir **liquidación** (rematar temporada saliente, margen bajo, urgencia de stock) de **novedad** (colección nueva a descuento suave). No mezclar el mensaje.
- **Lead-time:** el más largo (~21-28 días) — producción creativa visual pesada.
- **Qué NO puede fallar:** stock por talla del ganador (quiebre de talla mata la conversión), fotos, tabla de tallas, política de cambio/devolución visible.
- **Proyección:** cuidado con devoluciones — proyectar sobre venta neta, no bruta.

### 🧴 Skincare / beauty / wellness
- **Qué manda:** régimen/rutina (se venden sets, no unidades sueltas); educación; alto margen → **espacio real para descontar**.
- **Mecánica de evento:** sets/kits de gifting (fuerte en Madre, San Valentín, Navidad), sampling, suscripción, upsell de "rutina completa".
- **Lead-time:** ~14-21 días (contenido educativo + armado de sets).
- **Qué NO puede fallar:** claims/ingredientes claros, prueba social (reviews), regimen bien explicado, gifting a tiempo en fechas de regalo. Si es salud/YMYL, cuidado con claims (ver `advanz-shopify-blog-publisher` / `advanz-seo-geo-engine`).
- **Proyección:** el alto margen permite mecánica estacional agresiva sin romper la caja.

### 🥫 Consumible / alimento funcional / suplementos
- **Qué manda:** ciclo de recompra (intervalo entre compras conocido) → se puede **predecir la ola** por reposición; profundidad de stock; AOV vía multipack.
- **Mecánica de evento:** packs/multipacks, "stock up ahora", suscripción con descuento, umbral de envío gratis.
- **Lead-time:** el más corto (~10-14 días) — pero el **stock hay que asegurarlo antes** porque el volumen es alto.
- **Qué NO puede fallar:** stock depth (se agota rápido), logística/envío para volumen, fecha de vencimiento del lote que entra a oferta.
- **Proyección:** usar el intervalo de recompra del propio cliente para anticipar cuándo vuelve el cohorte.

### 🏠 Otros (hogar, tech, mascotas, juguetes…)
Aplicar el mismo marco: ¿es de gifting o de auto-consumo? ¿alto o bajo margen? ¿stock simple o por variante? ¿ciclo de recompra o compra única? Definir eso y derivar mecánica + lead-time + qué no puede fallar por analogía con las tres de arriba.

---

## Cómo usar esta clasificación

1. Resolver la **vertical** → fija lead-time mínimo (`event-calendar.md`), mecánica candidata y el checklist de "qué no puede fallar".
2. Clasificar el **catálogo** → define qué SKU entra y con qué rol.
3. El **ganador ancla la proyección**; el acompañamiento define la estrategia de AOV; el fantasma es el leverage escondido; el zombie se ignora.
4. Todo esto entra al scoring de leverage (`leverage-scoring.md`) y al artifact (`artifact-spec.md`).
