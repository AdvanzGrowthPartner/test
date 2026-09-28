# Benchmarks y umbrales de lectura

Rangos de referencia para ecommerce DTC. Son puntos de partida para decidir "esto está mal",
no verdades absolutas: contrasta siempre contra el histórico del propio sitio.

## Métricas de sesión

| Métrica | Bien | Atención | Malo |
|---|---|---|---|
| Páginas por sesión | > 3,0 | 1,8 – 3,0 | < 1,8 |
| Profundidad de scroll media | > 50% | 35 – 50% | < 35% |
| Tiempo activo | > 90 s | 45 – 90 s | < 45 s |
| Retrocesos rápidos | < 5% | 5 – 10% | > 10% |
| Clics fallidos | < 2% | 2 – 5% | > 5% |
| Clics continuos (rage) | < 1% | 1 – 3% | > 3% |
| Tráfico de bots | < 5% | 5 – 10% | > 10% |
| Sesiones con error JS | < 5% | 5 – 15% | > 15% |

## Tasas del ciclo de venta

| Paso | Bien | Atención | Malo |
|---|---|---|---|
| Entrada → vista de producto | > 55% | 35 – 55% | < 35% |
| Colección → PDP | > 45% | 30 – 45% | < 30% |
| PDP → Agregar al carro | > 8% | 4 – 8% | < 4% |
| ATC → inicio de checkout | > 65% | 45 – 65% | < 45% |
| Inicio de checkout → compra | > 45% | 30 – 45% | < 30% |
| Conversión global | > 2% | 1 – 2% | < 1% |

Notas de interpretación:

- **PDP → ATC** medido por evento inteligente casi siempre subestima. Compáralo con el ATC real
  de Shopify antes de alarmarse.
- Un **ATC → checkout muy alto (>80%)** normalmente indica que el evento de "inicio de checkout"
  está disparando junto al ATC, no que el carrito sea perfecto.
- **Móvil** rinde entre 30% y 50% peor que desktop en casi todos los pasos. Compara móvil contra
  móvil.
- Tráfico de **navegador in-app** rinde peor que el mismo canal en navegador normal. Sepáralo.

## Core Web Vitals

| Métrica | Bueno | Necesita mejoras | Pobre |
|---|---|---|---|
| LCP | ≤ 2,5 s | 2,5 – 4,0 s | > 4,0 s |
| INP | ≤ 200 ms | 200 – 500 ms | > 500 ms |
| CLS | ≤ 0,1 | 0,1 – 0,25 | > 0,25 |

INP es el que más se correlaciona con fricción percibida en móvil: es cuánto tarda la interfaz
en responder a un toque.

## Cómo convertir un benchmark en objetivo

No apuntes al "bien" de la tabla en un salto. Objetivo realista de un test:
**cerrar entre un 25% y un 40% de la brecha** entre la tasa actual y el rango bueno. Eso
mantiene el reporte creíble y hace que el test tenga tamaño de muestra alcanzable.
