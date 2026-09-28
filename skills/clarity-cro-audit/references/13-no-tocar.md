# Lo que no hay que tocar

Toda auditoría entrega una lista de cambios. Muy pocas entregan la lista contraria, y es la que
evita el daño. Son dos listas distintas y no hay que mezclarlas:

1. **Funciona · no tocar** — está midiendo bien o vendiendo bien. Tocarlo solo resta.
2. **Puede romper · no tocar sin medir** — cambiarlo tiene efecto directo sobre el dinero y no
   hay forma de saber el signo sin un experimento.

---

## Lista 1 · Funciona, no tocar

Se arma con lo que el diagnóstico encontró **sano**, con su número al lado. Patrones que
aparecen casi siempre:

| Qué | Por qué no se toca |
|---|---|
| El paso carro → checkout, si está sobre 75% | Está por encima del estándar; el problema está después |
| El quick-add de la colección, si concentra los clics | Es el camino de compra real, aunque no sea el diseñado |
| El desktop, cuando ya convierte al doble que móvil | Es el techo de la proyección, no el problema |
| La grilla de colección, si el scroll llega al final | El usuario ve el catálogo completo |
| El evento de compra de Shopify | Es la fuente de verdad; cualquier cambio invalida el histórico |

**Cómo se escribe:** una línea por ítem, con el número que lo respalda. Sin número, no entra —
si no se midió, no se sabe que funciona.

---

## Lista 2 · Puede romper, no tocar sin medir

| Qué | Qué puede romper | Cómo se hace, si se hace |
|---|---|---|
| **Precios y escalera de formatos** | Margen. Un 5% mal puesto se come la ganancia del resto del plan | Decisión de negocio, con margen de contribución a la vista, y en un solo formato primero |
| **Cupones y descuentos automáticos** | Doble descuento, o canibalizar el precio lista | Probar en un cupón de prueba antes de tocar la regla |
| **URLs, handles y consolidación de SKUs** | Tráfico orgánico existente | Revisar tráfico por URL antes; redirecciones 301 obligatorias |
| **El pixel o el evento de compra** | El histórico entero deja de ser comparable | Nunca durante la auditoría. Se agrega, no se reemplaza |
| **El tema completo (cambio de plantilla)** | Todo a la vez, sin poder atribuir nada | Si se hace, se hace después de leer los tickets, no antes |
| **Quitar el quick-add para «forzar» la ficha** | Es el camino de compra mayoritario | No se quita: se mejora la ficha y se compara |
| **Avisos de escasez inventados** | Confianza, y es irreversible | Solo atado a inventario real |
| **Apps: desinstalar sin revisar el tema** | Restos de código que rompen el render | Revisar bloques huérfanos antes de desinstalar |
| **Reescribir la ficha entera de una vez** | Imposible atribuir la mejora o la caída | Un cambio por lectura |

---

## La regla que ordena las dos listas

> Un cambio que puede mover el dinero en las dos direcciones **no se hace por criterio: se
> mide.** Un cambio que solo puede mejorar — peso de imágenes, un botón visible, un dato que
> faltaba — no necesita experimento, necesita fecha.

Esa frontera es la que decide qué va en «esta semana» y qué va en «después de medir» dentro del
orden de ataque.

---

## Cómo entra al entregable

Como sección propia, siempre penúltima, en dos columnas visuales — verde a la izquierda, ámbar
a la derecha — con listas cortas. No lleva tickets ni tiempos: no hay nada que ejecutar. Su
función es que nadie gaste dos días en algo que ya estaba bien, ni rompa en una tarde lo que
sostiene el margen.
