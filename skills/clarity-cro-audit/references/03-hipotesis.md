# Hipótesis por etapa del funnel

## Formato obligatorio

Cada hipótesis se escribe así. Si falta una línea, no está lista para reportarse.

```
H<n> · <Título en una línea, afirmativo>
Etapa      : <paso del funnel>
Evidencia  : <dato con número> · <dónde verlo en Clarity>
Causa      : <mecanismo concreto, no "mala UX">
Test       : <cambio específico, ejecutable en <2 semanas>
Métrica    : <tasa exacta que debe moverse> · de <actual> a <objetivo>
Impacto    : <sesiones/mes recuperables si acierta>
Confianza  : Alta / Media / Baja + por qué
```

Reglas:
- **Causa** debe ser falsable. "El usuario no encuentra el botón" sirve; "la página no
  convierte" no.
- **Impacto** siempre en sesiones absolutas, nunca solo en %.
- Máximo 8 hipótesis por reporte. Más es una lista de deseos.
- Si dos hipótesis compiten por explicar la misma fuga, decláralo y propón el test que las
  separa.

---

## Biblioteca por etapa

### Entrada → primera interacción

- El anuncio promete algo que la landing no muestra en el primer viewport (mensaje roto).
- Aterrizan en colección cuando el anuncio hablaba de un producto: un clic extra innecesario.
- La página tarda en responder al toque (INP alto) y en webview in-app se percibe como rota.
- Popup o banner de bienvenida bloquea el primer scroll en móvil.
- El tráfico simplemente no es cualificado (audiencia de red de terceros, tipo audience network).

Señales: scroll bajo, tiempo activo bajo, retrocesos rápidos altos, salida en la URL de entrada.

### Colección → PDP

- La grilla no da razones para entrar: falta precio por unidad, reseñas, badge de más vendido.
- Demasiados productos equivalentes (mismo sabor, distintos formatos) → parálisis de elección.
- El quick-add compite con el clic a la ficha y el usuario ni ve la PDP.
- Orden de la colección no coincide con la intención del anuncio.
- Filtros ausentes o inutilizables en móvil.

Señales: alta tasa de salida en `/collections/`, scroll profundo sin clic, clics fallidos sobre
imágenes o precios en el heatmap.

### PDP → Agregar al carro

- La variante (sabor/formato) no está preseleccionada y el botón no responde hasta elegir.
- Error de JavaScript en el selector de variantes → el botón queda muerto.
- El precio por unidad o el ahorro del pack no está explícito: no se entiende cuál conviene.
- Información crítica (envío, plazo, garantía) está bajo el pliegue o dentro de acordeones.
- Falta prueba social cerca del CTA cuando el usuario viene frío desde social.
- CTA fuera del primer viewport en móvil y sin barra fija.

Señales: clics continuos sobre el botón, clics fallidos en la zona de variantes, scroll bajo,
errores JS del tema.

### ATC → inicio de checkout

- El carrito lateral se abre y no muestra un CTA de pago evidente.
- Aparece un upsell o cross-sell que interrumpe en lugar de sumar.
- El costo de envío aparece recién en el carrito y rompe la expectativa.
- El usuario usa el carrito como lista de deseos (comportamiento normal en consideración media).
- Falta señal de urgencia o de garantía en el momento del salto.

Señales: "Quitar del carro" alto dentro del segmento, retrocesos rápidos altísimos, salidas en
la URL de producto tras el ATC.

### Checkout → compra

En Shopify, si Clarity no está instalado vía Customer Events **esto es una caja negra**. No
inventes hipótesis: instala la medición o cruza con los datos de Shopify. Cuando sí hay datos,
lo habitual es costo de envío, métodos de pago, campos obligatorios y validaciones.

### Transversales

- Móvil y desktop tienen funnels distintos: siempre revisa por separado antes de concluir.
- Los navegadores in-app (Instagram, Facebook) no autocompletan y pierden sesión al cambiar de
  app: fugas altas ahí son de contexto, no de diseño.
- Usuarios recurrentes con tasas mucho mejores indican que el problema es de primera visita:
  falta de confianza, no de usabilidad.
