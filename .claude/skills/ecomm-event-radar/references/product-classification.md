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

**Cómo se ve en el artifact:** matriz 2×2 (vistas en un eje, ventas en el otro) con los SKU ubicados por cuadrante y coloreados por los 4 tipos. Ver `artifact-spec.md`.

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
