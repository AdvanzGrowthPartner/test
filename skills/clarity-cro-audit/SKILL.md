---
name: clarity-cro-audit
description: "Ciclo completo de CRO para ecommerce Shopify: instalar y conectar fuentes, diagnosticar con Shopify + Clarity + DOM, proponer cambios sin romper, QA y rollback declarado, y readout a 14 y 30 días. Úsala al pedir auditoría CRO, puntos de fuga, plan CRO, qué puedo tocar sin romper, o al recibir un enlace de una tienda Shopify o de clarity.microsoft.com."
---

# Ciclo CRO · Shopify + Clarity + DOM

## 1. El ciclo completo

La auditoría no es el final: es la fase 2 de seis. Un diagnóstico que no llega a producción no
movió ningún número.

```
Fase 0  Instalar y conectar      → 15 min   → references/00-instalacion.md
Fase 1  Accesos y contexto       → 10 min   → sección 4
Fase 2  Diagnóstico              → 3 h      → secciones 5 a 9
Fase 3  Propuesta y prioridad    → 1 h      → secciones 10 a 12
Fase 4  Implementar sin romper   → continuo → references/14-implementacion.md
Fase 5  QA y validación          → 10 min por ticket
Fase 6  Readout e iteración      → días 14 y 30
```

Las fases 0 a 3 son la auditoría (4 a 6 horas). Las fases 4 a 6 son lo que la convierte en
resultados, y son las que hacen que exista una segunda auditoría.

## 2. Regla de oro: expone y recomienda, no ejecuta

**La skill nunca escribe en la tienda.** No publica temas, no cambia precios, no instala apps,
no toca inventario, no borra nada. Produce el análisis, el cambio listo para pegar y la
instrucción de dónde va; **toda escritura en la tienda es una acción humana** con nombre, fecha
y procedimiento de reversa.

Los outputs son estratégicos antes que operativos: la skill **trae la información y la expone**
para que la decisión la tome quien responde por el negocio. Un diagnóstico que puede tocar la
tienda por su cuenta solo se lee con miedo.

## 3. Fase 0 · Instalar y conectar

Detalle completo en `references/00-instalacion.md`. Lo mínimo:

- **Shopify por MCP es obligatorio.** Confirmar con `get-shop-info` que es la tienda correcta y
  correr la consulta A como prueba de humo. Si devuelve 0 filas, falta el permiso de Analytics
  — es el fallo número uno y lo habilita el dueño de la tienda, no se arregla desde acá.
- **Clarity no tiene MCP.** Se recorre por navegador; sin navegador se pide como cuatro
  capturas concretas. El diagnóstico no se detiene por eso.
- **Nada más se conecta.** Meta, Google, Klaviyo, Ahrefs y Semrush quedan fuera aunque estén
  disponibles: si entran, contaminan la proyección.

## 4. Fase 1 · Los accesos y las dos preguntas

Se piden juntos, en un solo mensaje, antes de abrir nada.

| | Acceso | Para qué | ¿Bloquea? |
|---|---|---|---|
| 1 | **Shopify · colaborador con permiso de Analytics** | Las seis consultas del embudo y del dinero | **Sí.** Sin esto no hay auditoría, hay opinión |
| 2 | **URL de la tienda y handle de 2 o 3 productos** | HTML, `products.json` y los tres scripts de DOM | **Sí**, pero es público: basta la URL |
| 3 | **Microsoft Clarity · lectura del proyecto** | Scroll, ranking de clics, grabaciones | No. Si falta, el reporte declara qué quedó sin confirmar |
| 4 | **Acceso al tema, o alguien que publique** | Solo para la fase 4, no para diagnosticar | No |

Y dos preguntas que no salen de ninguna herramienta:

- **Margen de contribución aproximado.** Único supuesto puro de la proyección. Se pregunta una
  vez, se fija y queda declarado a la vista — nunca como campo editable.
- **Qué no se puede tocar.** Precios, promesa de envío, acuerdos con marcas. Va directo a la
  lista de intocables de la fase 4.

## 5. Fase 2 · El orden de las fuentes

```
1. Shopify   → el embudo real y el dinero     ¿CUÁNTO se pierde y DÓNDE?
2. DOM       → la posición de cada elemento   ¿EN QUÉ PÍXEL?
3. Clarity   → el comportamiento              ¿POR QUÉ?
```

**Empezar por Clarity es el error clásico.** Sus eventos automáticos son heurísticas del DOM y
subcuentan: en una auditoría real marcó 2.821 carros contra 4.051 de Shopify, un 30% menos. Y
no ve el checkout de Shopify, que es donde está la gente con más intención del sitio.

Shopify da el embudo verdadero en **una consulta**. Clarity explica ese embudo. El DOM lo
convierte en un ticket. Consultas exactas en `references/10-herramientas.md`.

**Tres verificaciones antes de leer un número de Clarity** (detalle en `05-limites-clarity.md`):
si ve o no el checkout · cuánto subcuentan sus eventos frente a Shopify · si el embudo
configurado tiene sentido, porque son secuenciales y un paso mal puesto devuelve 0%.

## 6. El corte por dispositivo, y las tres ventanas

Es la primera pregunta después del embudo y suele ser el titular del reporte:

```sql
FROM sessions SHOW sessions, sessions_with_cart_additions, sessions_that_reached_checkout,
     sessions_that_completed_checkout, conversion_rate
GROUP BY session_device_type SINCE -90d UNTIL today
```

Si el 80% del tráfico es móvil y convierte la mitad que desktop, ya sabes dónde trabajar y
tienes el **techo de la proyección**: mismo sitio, mismo catálogo, mismos precios, otra
interfaz. No hace falta ningún benchmark externo.

Siempre tres ventanas: **365 días** para contexto y quiebres · **90 días** para el diagnóstico ·
**30 días** para confirmar que el hallazgo sigue vivo. Si el tráfico y los pedidos no van
acoplados en la serie de 12 meses, ese desacople es un hallazgo por sí mismo.

## 7. El catálogo de fugas

Trece patrones con detección, umbral y arreglo estándar en `references/06-catalogo-fugas.md`.
Se recorren **todos, siempre**, aunque el cliente ya traiga una hipótesis.

| | Fuga | Dónde |
|---|---|---|
| F1 | CTA bajo el pliegue | Ficha |
| F2 | Acantilado de scroll | Ficha |
| F3 | Checkout ciego | Medición |
| F4 | Información escondida | Ficha |
| F5 | Escalera de precios plana | Catálogo |
| F6 | Cupón mostrado sin aplicar | Carrito |
| F7 | Sin precio unitario en la grilla | Colección |
| F8 | Quick-add canibalizando la ficha | Colección |
| F9 | Navegación por menú | Arquitectura |
| F10 | Errores del tema | Transversal |
| F11 | Navegador in-app | Transversal |
| F12 | Eventos duplicados o sesgados | Medición |
| F13 | **Peso y prioridad de las imágenes** | Rendimiento |

**F13 corre primero:** es una descarga y seis comandos, no necesita accesos, y suele dar el
ticket cero — se arregla en horas, no tiene riesgo y afecta a todo el tráfico móvil. Es la fuga
que ningún mapa de calor muestra, porque quien la sufre se va antes de generar un evento.

## 8. Las piezas que faltan

Además de buscar fugas, se contrasta la tienda contra las **ocho piezas estándar** que las
tiendas Shopify que convierten bien ya tienen: barra fija de compra, imágenes priorizadas,
precio unitario, barra de envío gratis en la ficha, fecha de entrega, aviso de stock real,
comparador de formatos y una sola app de reseñas. Se ilustran **con código, no con imágenes**:
cuando lo que se entrega es «pega esto», un bloque de código se lee más rápido que un mockup.
Fragmentos listos en `references/12-piezas-estandar.md`.

## 9. Lo que no hay que tocar

Dos listas separadas: lo que ya funciona (con su número al lado) y lo que puede romper si se
toca sin medir — precios, cupones, URLs, el pixel de compra, el quick-add, la app de reseñas.
La regla: *un cambio que puede mover el dinero en las dos direcciones no se hace por criterio,
se mide.* Detalle en `references/13-no-tocar.md`, y se cruza con la lista de intocables que
declaró el cliente en la fase 1.

## 10. Fase 3 · Urgencia, y un solo orden

```
Urgencia = sesiones afectadas ÷ días de trabajo,
           y lo irreversible o lo que sangra hoy, antes que lo cosmético
```

En valor absoluto de sesiones, nunca en porcentaje. **Un hallazgo sin número de sesiones detrás
no se reporta.**

**Un solo bloque de prioridad en todo el entregable.** Entregar una matriz impacto/esfuerzo *y*
una lista de tickets dice lo mismo dos veces y el lector no sabe cuál manda. Se fusionan en una
sola sección, con tarjetas numeradas y tres grupos: **esta semana · semanas 2 y 3 · después de
medir**.

## 11. Bloques, items, tickets

- **Bloque** — una superficie del sitio: Medición · Ficha · Colección y catálogo · Carrito y
  cierre.
- **Item** — 0,5 a 3 días. Si pasa de 3, se parte.
- **Ticket** — item con especificación y cinco campos que casi nadie pone:

| Campo | Qué declara |
|---|---|
| **Dueño** | 🟣 lo hago yo · 🔵 necesita acceso al tema · 🟡 decisión de negocio |
| **Riesgo** | Bajo / medio / alto. Siempre declarado, incluso cuando es nulo |
| **Tiempo** | En horas o días |
| **Reversibilidad** | 🟢 aditivo · 🟡 reordena o modifica · 🔴 estructural o de negocio |
| **Cómo se sabe** | La métrica exacta, su valor de hoy y el plazo de lectura |

Distinguir el dueño es lo que hace que el plan arranque: sin eso el cliente asume que todo
depende de él. Declarar la reversibilidad es lo que hace que se despliegue: sin eso, nadie
toca nada.

## 12. Impacto: pedidos, no honorarios

La skill **no estima costos**. Estima esfuerzo en días y retorno en pedidos y margen. El techo
sale de la brecha por dispositivo del propio sitio, no de un benchmark. Fórmulas, factor de
solapamiento 0,65, tamaños de muestra y cronograma en `references/08-modelo-impacto.md`.

- **El calendario es impacto acumulado, no lista de tareas.** Cuatro barras semanales que se
  suman, rotuladas con los tickets que entraron en producción, y debajo dos rangos — mes 1 y
  mes 2 — en pedidos y en dinero. Semanas relativas, nunca fechas reales.
- **La proyección no tiene nada movible.** Sin campos editables ni deslizadores, el margen
  incluido. Sale entera de los datos de la conexión y se dibuja **con la estética de la
  plataforma auditada**. La última fila declara qué porcentaje de la brecha con desktop se está
  cerrando, que es el único supuesto real.

## 13. Fases 4 a 6 · Implementar, validar, iterar

Todo el detalle en `references/14-implementacion.md`. Las seis reglas que no se saltan:

1. **Nunca se edita el tema publicado** para nada que no sea 🟢. Se duplica, se cambia en la
   copia, se previsualiza, se hace QA, se publica — y el tema anterior se conserva 14 días.
2. **Cada ticket llega a la contraparte con cinco líneas:** qué se toca · **qué no se toca** ·
   cómo se revierte · cómo se verifica · cuándo se lee. La segunda línea evita la mayoría de
   los accidentes.
3. **QA de 10 minutos antes de publicar:** carro desde ficha y colección, cambio de variante,
   cupón, checkout hasta pago en un teléfono real, apertura desde navegador in-app, consola sin
   errores nuevos, render a 390 y 1120 px, y un pedido de prueba si se tocó carro o checkout.
4. **Una sola variable:** no se despliegan dos tickets sobre la misma superficie el mismo día,
   porque después no se puede atribuir nada.
5. **Se lee lo que corresponde y cuando corresponde.** Peso, clics y avance de paso se leen en
   días; conversión e ingresos necesitan semanas. Cada ticket declara en cuál de las dos vive.
6. **Readout a 14 y 30 días, con las mismas consultas.** Tres desenlaces: se cumplió, se
   documenta el delta real · no se movió, se archiva la hipótesis con su razón · empeoró,
   rollback inmediato con el procedimiento del propio ticket.

Cada readout deja una línea en el histórico. A la tercera auditoría la proyección se calibra
con resultados propios y no solo con la brecha móvil-desktop: es el único activo de esta skill
que no se puede copiar.

## 14. El entregable es visual

Regla: **una imagen dominante y tres o cuatro líneas de texto por sección.** Si hace falta más
texto, el hallazgo va dentro de un ticket plegado.

**Once componentes y cuatro roles de color**, chips de dueño, riesgo y reversibilidad, y
responsive verificado a 390 px y 1120 px, en claro y en oscuro. Y **doce secciones en orden de
urgencia**: los cinco de esta semana → dónde se cae la gente → el corte por dispositivo y canal
→ el peso de la ficha → actual vs propuesto → orden de ataque → las piezas que faltan →
calendario de 30 días → proyección → herramientas → lo que no hay que tocar → cómo se replica.

Especificación en `references/11-lenguaje-visual.md` y estructura en `references/09-entregable.md`.
Se publica como página autocontenida con `web-artifacts-builder` y se valida la paleta
dato/pérdida con `dataviz` antes de entregar.

## 15. Archivos

| Archivo | Cuándo |
|---|---|
| `references/00-instalacion.md` | **Antes que nada.** Instalar, conectar, verificar |
| `references/10-herramientas.md` | Qué fuente responde qué y con qué consulta |
| `references/06-catalogo-fugas.md` | El recorrido principal del diagnóstico |
| `references/07-medicion-dom.md` | Medir la plantilla en píxeles |
| `references/08-modelo-impacto.md` | Proyectar pedidos, margen y plazos |
| `references/12-piezas-estandar.md` | Las ocho ausencias, con su código |
| `references/13-no-tocar.md` | Lo que funciona y lo que puede romper |
| `references/14-implementacion.md` | **Fases 4 a 6.** Desplegar sin romper, QA, readout |
| `references/11-lenguaje-visual.md` | Cómo se ve el entregable |
| `references/09-entregable.md` | Esqueleto del reporte: doce secciones por urgencia |
| `references/01-setup.md` | Configurar embudos, segmentos y eventos en Clarity |
| `references/02-bloques.md` | Extracción bloque por bloque |
| `references/03-hipotesis.md` | Hipótesis por etapa |
| `references/04-benchmarks.md` | Umbrales de lectura |
| `references/05-limites-clarity.md` | Ante cualquier número raro |
| `assets/medir-plantilla.js` | Consola: anatomía y veredicto de F1 |
| `assets/auditar-assets.js` | Consola: peso, dimensiones y prioridad · veredicto de F13 |
| `assets/escalera-precios.js` | Consola: veredicto de F5 |

## 16. Alcance: 100% CRO

El diagnóstico usa **tres fuentes y nada más**: Shopify, el HTML y DOM del sitio, y Clarity.
Meta Ads, Google Ads, Klaviyo, Ahrefs y Semrush **no entran acá** — aparecen en una línea al
final, como el paso siguiente. Nada de medios, SEO ni retención contamina la proyección.

Todo lo que la skill entrega tiene que poder **copiarse y pegarse el mismo día**: consultas,
fragmentos de Liquid, el pixel de checkout, los scripts de consola. El criterio de calidad es
que mañana el diagnóstico esté vivo.

## 17. Replicar en un cliente nuevo

**Lo que cambia** son los números, los mockups y qué fugas están activas. **Lo que no cambia**
es el orden de fuentes, los trece patrones, las ocho piezas, los tres chips de dueño, los tres
niveles de reversibilidad y la regla de los 3 días por ticket.

Si un reporte se ve distinto de otro en la estructura, se ejecutó mal la skill. Si un cambio
llegó a producción sin QA ni rollback declarado, se saltó la fase 4 — y esa es la única forma
en que esta skill rompe algo.