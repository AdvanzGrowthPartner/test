# Setup del proyecto Clarity

Objetivo: dejar el proyecto en un estado donde cualquiera abra el panel y en 30 segundos sepa
dónde está la fuga. Sin esto, cada análisis se rehace desde cero.

---

## Mapa de la interfaz

| Qué | Dónde |
|---|---|
| ID de proyecto | `Configuración → Información general` (ej. `syzig98shn`) |
| URL base | `https://clarity.microsoft.com/projects/view/<ID>/dashboard` |
| Rango de fechas | Parámetro de URL: `?date=Last%2090%20days` · también `Last 365 days`, `Last 30 days`. Es la forma fiable; el selector visual es un popover frágil |
| Eventos inteligentes | `Configuración → Eventos inteligentes` |
| Embudos | `Configuración → Embudos` |
| Segmentos | Se crean desde el panel: `Filtros → …→ Aplicar → Guardar como segmento` |
| Exportación | `Configuración → Exportar datos` (API, últimos 3 días) |
| Grabaciones | Pestaña `Grabaciones`, hereda los filtros activos |
| Heatmaps | Pestaña `Mapas Térmicos`, por URL |

Trampas de la UI:
- Al guardar un segmento, el chip de fecha se guarda dentro del segmento. **Quítalo** antes de
  guardar para que el segmento sirva en cualquier ventana temporal.
- La tecla Escape cierra el diálogo de embudo y abre el embudo existente. No usar Escape.
- Un clic fuera de un popover aplica filtros involuntarios (ej. "Clics continuos: Sí"). Revisa
  siempre los chips activos antes de leer un número.

---

## Eventos inteligentes

Clarity trae ~15 eventos auto-detectados (Producto visto, Agregar al carro, Comenzar
finalización de la compra, Quitar del carro, Carro visto, Enviar formulario, Buscar,
Suscribirse, Clic de salida, etc.). Son inferencias del DOM.

**Auditoría obligatoria de cada evento que vayas a usar:**

1. Cuenta sesiones del evento en 90 días.
2. Compáralo con las páginas vistas de la URL equivalente (tarjeta *Páginas principales*).
3. Compáralo dentro del segmento "entra directo a la página" vs "navega hacia la página".
4. Cruza eventos entre sí: si "Enviar formulario" ≈ "Agregar al carro", el evento de formulario
   está capturando el `<form>` del producto, no un formulario real de contacto.

Si un evento no pasa la auditoría, **no lo uses como paso de embudo**; usa la URL.

**Eventos personalizados (recomendado).** `Configuración → Eventos inteligentes → Nuevo evento`
permite definir por selector CSS, texto de clic o URL, sin código. Los que valen la pena crear
en Shopify:

| Evento a crear | Definición | Por qué |
|---|---|---|
| `ATC real` | clic en el selector del botón Añadir al carro del tema | El auto-evento no distingue quick-add de PDP |
| `Abre drawer carrito` | clic en el icono de carrito | El carrito lateral no genera URL |
| `Ir a pagar` | clic en el botón de checkout del drawer | Último punto visible antes de perder al usuario |
| `Selecciona variante` | clic en el selector de sabor/formato | Diagnostica fricción de variantes |
| `Abre acordeón info` | clic en secciones de la PDP | Mide qué dudas tiene el usuario |

Además, la vía robusta es **enviar eventos desde el código** con `clarity("event", "nombre")`
en los mismos disparadores que ya usan Meta/GA4. Si el sitio ya tiene dataLayer, es media hora
de trabajo y elimina el problema de raíz.

---

## Embudos

Reglas de construcción:

1. **Nunca un paso negativo** ("Quitar del carro") dentro de un embudo de conversión.
2. **El primer paso debe cubrir a la mayoría del tráfico.** Si el 50% entra por PDP, un embudo
   que empieza en la home mide al 9% de la gente.
3. **Un embudo por camino real**, no uno solo intentando cubrir todo.
4. Mezclar tipos de paso: `Visitas a la página` (con operadores *empieza por / termina por /
   contiene / es exactamente / regex*) y `Eventos inteligentes`.
5. Nombrar con prefijo alfabético (`A.`, `B.`, `C.`) porque la lista se ordena por nombre.

**Set mínimo para un ecommerce Shopify:**

| Embudo | Pasos | Responde |
|---|---|---|
| A · Ciclo de venta | Producto visto → Agregar al carro → Comenzar checkout → Finalización | Salud del ciclo por eventos |
| B · Colección → PDP → Carro | contiene `/collections/` → contiene `/products/` → ATC → Checkout | El camino más transitado |
| C · Home → Colección → PDP | home exacta → `/collections/` → `/products/` → ATC | Si la home cumple su función |
| D · Home a compra | home → Producto visto → ATC → Checkout → Finalización | Ciclo completo desde home |

Añade uno por landing de campaña cuando haya paid fuerte.

---

## Segmentos

Se crean aplicando filtros y guardando. El filtro más potente es
`Acciones de usuario → Embudos`: elige embudo, paso y estado (**Reached / Didn't reach**).
Eso da segmentos de fuga exactos sin necesidad de lógica booleana.

**Set mínimo (déjalos creados en el proyecto):**

| # | Nombre | Filtro |
|---|---|---|
| 01 | Con compra | Eventos inteligentes = evento de conversión disponible |
| 02 | Fuga PDP sin ATC | Embudo A · paso ATC · Didn't reach |
| 03 | Fuga ATC sin checkout | Embudo A · paso Comenzar checkout · Didn't reach |
| 04 | Fuga en checkout | Embudo A · paso Finalización · Didn't reach |
| 05 | Entra directo a PDP | Ruta · URL de **entrada** contiene `/products/` |
| 06 | Entra por colección | Ruta · URL de **entrada** contiene `/collections/` |
| 07 | Fricción | Ideas: Clics fallidos o Retrocesos rápidos |
| 08 | Móvil | Información del usuario · Dispositivo = Móvil |

Con 02, 03 y 04 tienes "sesiones sin venta" segmentadas por **dónde** se cayeron, que es
mucho más accionable que un genérico "no compró".

---

## Catálogo de filtros disponibles

- **Información del usuario**: dispositivo, explorador, SO, ubicación, día de semana, tipo de
  usuario, Clarity user ID.
- **Acciones de usuario**: clics continuos (rage), clics fallidos (dead), desplazamiento
  excesivo, retrocesos rápidos, movimiento de cursor, texto escrito/seleccionado, página
  redimensionada/actualizada, intención, **texto en el que se ha hecho clic**, profundidad de
  scroll (min/máx %), eventos inteligentes (con O/Y), embudos (paso + estado).
- **Ruta**: URL de **entrada**, de **salida**, **visitada**, y URL de página de referencia.
  Operadores: empieza por, termina por, contiene, excluye, es exactamente, no es exactamente,
  regex, excluye regex.
- **Tráfico**: sitio de referencia, fuente, medio, campaña, canal, tráfico de bots.
- **Rendimiento**: puntuación, LCP, INP, CLS.
- **Producto / Sesión / Página / Filtros personalizados**.

`Ruta → URL de salida` es el sustituto del reporte de páginas de salida que Clarity no tiene.
