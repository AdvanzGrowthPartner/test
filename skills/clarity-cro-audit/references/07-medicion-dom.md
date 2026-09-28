# Medición del DOM

La analítica dice cuánta gente se cae. El DOM dice dónde estaba parada cuando se cayó. Cruzar
las dos cosas es lo que convierte un diagnóstico en un ticket.

Se ejecuta en el navegador, sobre la página en vivo, en viewport móvil (390 px de ancho). Basta
con la consola del navegador o cualquier herramienta que evalúe JavaScript en la página.

---

## Paso 1 · Anatomía de la plantilla

Devuelve la posición de cada bloque en píxeles y en porcentaje de página. El porcentaje es lo
que se cruza con el mapa de desplazamiento.

```js
(() => {
  const H = document.documentElement.scrollHeight, vh = innerHeight;
  const q = s => { const e = document.querySelector(s); if (!e) return null;
    const t = e.getBoundingClientRect().top + scrollY;
    return { px: Math.round(t), pct: +(100*t/H).toFixed(1), pantallas: +(t/vh).toFixed(2) }; };
  return { alto: H, viewport: vh,
    galeria:  q('media-gallery, .product__media-wrapper, .product-gallery'),
    h1:       q('h1'),
    resenas:  q('[class*=rating], [class*=review], .jdgm-prev-badge, .loox-rating'),
    precio:   q('.price, [class*=price]'),
    variante: q('variant-radios, variant-selects, .product-form__input, [class*=swatch]'),
    atc:      q('button[name="add"], .product-form__submit, [name=add], button[type=submit]'),
    pagoRapido: q('.shopify-payment-button, [class*=express]'),
  };
})()
```

## Paso 2 · ¿Hay CTA fijo?

El falso positivo típico es el carrito lateral cerrado, que está `fixed` y contiene la palabra
«carrito». Por eso hay que filtrar por visibilidad.

```js
[...document.querySelectorAll('*')].filter(e => {
  const s = getComputedStyle(e), r = e.getBoundingClientRect();
  return (s.position === 'fixed' || s.position === 'sticky')
      && s.visibility !== 'hidden' && s.display !== 'none' && s.opacity !== '0'
      && r.height > 24 && r.width > 100;
}).map(e => ({ tag: e.tagName, cls: (e.className||'').toString().slice(0,40),
               alto: Math.round(e.getBoundingClientRect().height),
               txt: (e.innerText||'').trim().replace(/\s+/g,' ').slice(0,40) }))
```

Si ningún elemento visible contiene el CTA y el botón está bajo el pliegue → **F1 confirmado**.

## Paso 3 · Secuencia de contenido entre el precio y el botón

Lista, en orden, todo lo que hay en el tramo crítico. Es lo que llena la tabla de anatomía del
reporte.

```js
(() => {
  const H = document.documentElement.scrollHeight;
  const btn = document.querySelector('button[name="add"], .product-form__submit');
  const hasta = btn ? btn.getBoundingClientRect().top + scrollY + 80 : 2200;
  const vistos = new Set(), filas = [];
  for (const e of document.querySelectorAll('body *')) {
    const r = e.getBoundingClientRect(), t = r.top + scrollY;
    if (t < 600 || t > hasta || r.height < 18 || e.children.length > 1) continue;
    const txt = (e.innerText||'').trim().replace(/\s+/g,' ').slice(0,60);
    if (!txt || vistos.has(txt)) continue;
    vistos.add(txt); filas.push([Math.round(t), (100*t/H).toFixed(1)+'%', txt]);
  }
  return filas.sort((a,b) => a[0]-b[0]);
})()
```

## Paso 4 · Escalera de precios

Sin abrir el navegador siquiera: la API pública de Shopify basta.

```
GET /collections/<handle>/products.json?limit=250
```

Para cada producto: extraer las unidades del título con `/(\d+)\s*[Ss]ticks?|unidades|c[aá]psulas/`
y dividir el precio. Ordenar por unidades y mirar si el precio unitario baja de verdad.

## Paso 5 · Carrito

Abrir el carrito con productos dentro y verificar cuatro cosas:

1. ¿Hay barra de progreso de envío gratis?
2. ¿Los descuentos por volumen aparecen aplicados con su monto?
3. ¿El botón de pago está anclado al borde inferior del panel?
4. ¿El total mostrado coincide con lo que promete la comunicación?

Solo la cuarta suele fallar. Las tres primeras conviene declararlas explícitamente como «no
tocar» en el reporte: evita que el equipo gaste días en algo que ya funciona.

---

## Nota sobre las capturas

Si el entorno no puede alcanzar el sitio (proxy, sitio privado, staging con clave), no bloquees
la auditoría: la API pública de productos y la medición del DOM desde el navegador del usuario
alcanzan para todo. Para las ilustraciones, reconstruye la plantilla a escala con la foto y los
precios reales, y dilo en el pie de figura. Un mockup anotado con las posiciones medidas
comunica mejor que una captura sin anotar.
