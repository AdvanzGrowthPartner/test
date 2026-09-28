# Límites de Clarity: qué no se puede afirmar

Antes de reportar cualquier número raro, pasa por esta lista. La mayoría de "hallazgos"
espectaculares en Clarity son artefactos de medición.

## Lo que Clarity no ve

- **El checkout de Shopify.** No corre scripts de terceros en `/checkouts/*` salvo instalación
  vía Customer Events (Web Pixel). Sin eso, no hay compra, no hay ingreso, no hay CVR real.
- **Ingresos, pedidos, AOV, devoluciones.** Clarity no es analítica de negocio.
- **Identidad entre dispositivos.** Un usuario en móvil y luego en desktop son dos usuarios.
- **Atribución.** El "canal" se infiere del referrer, no del UTM. Tráfico con
  `utm_medium=paid` desde la app de Instagram suele caer en "Other" o "Direct".
- **Iframes de terceros** (widgets de reseñas, chats, algunos pop-ups): el contenido no se
  graba, y los clics dentro pueden verse como clics muertos.

## Sesgos y trampas frecuentes

| Síntoma | Causa habitual | Qué hacer |
|---|---|---|
| Embudo en 0% | Paso negativo, paso imposible, o primer paso minoritario | Rehacer el embudo |
| Un evento cae a casi cero en un periodo corto | Cambio de tema que rompió la heurística, o volumen insuficiente | Comparar con ventana larga antes de declarar caída |
| El sitio propio aparece como principal referente | Sesiones nuevas por expiración de 30 min, o vueltas desde pasarelas externas | No leerlo como canal |
| Métricas mucho mejores en un periodo antiguo | Composición de tráfico distinta (una campaña masiva de baja calidad diluye los promedios) | Comparar por canal, no en agregado |
| Muchas sesiones de una red de audiencia de terceros | Inventario de baja calidad de las plataformas de anuncios | Excluirlo antes de sacar conclusiones sobre el sitio |
| Enviar formulario ≈ Agregar al carro | El `<form>` del producto se cuenta como formulario | No usar "Enviar formulario" como micro-conversión |
| Bots >10% | Rastreadores y tráfico sospechoso | Clarity los excluye del conteo principal; revísalo antes de comparar periodos |

## Retención y muestreo

- Los datos agregados del panel llegan hasta ~13 meses (`Last 365 days` funciona).
- Las **grabaciones** se retienen bastante menos que los agregados: para periodos antiguos vas
  a tener números pero no vídeo.
- En proyectos de mucho volumen Clarity **muestrea grabaciones**. Los agregados siguen siendo
  representativos; el conteo de grabaciones no.
- La Data Export API solo entrega los últimos 3 días: sirve para monitoreo, no para histórico.

## Qué se puede afirmar con confianza

- Tasas **relativas entre pasos** dentro de un mismo embudo y periodo.
- **Comparaciones entre segmentos** en la misma ventana temporal.
- Señales de fricción (**clics fallidos, rage, retrocesos, scroll**) a nivel de página.
- **Errores de JavaScript** propios del tema.
- Todo lo que se vea directamente en una **grabación**.

## Qué exige otra fuente

- Conversión real, ingreso, AOV, LTV → Shopify.
- Atribución por canal y campaña → GA4 / plataformas de anuncios.
- Costo por adquisición → plataformas de anuncios.

Un buen reporte de Clarity dice explícitamente dónde termina Clarity y empieza la otra fuente.
