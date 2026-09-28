/**
 * Auditoría de plantilla — pegar en la consola del navegador, en viewport móvil.
 * Devuelve un objeto con todo lo que necesita el reporte para la sección de anatomía.
 */
(() => {
  const H = document.documentElement.scrollHeight, vh = innerHeight;
  const pos = s => { const e = document.querySelector(s); if (!e) return null;
    const r = e.getBoundingClientRect(), t = r.top + scrollY;
    return { px: Math.round(t), pct: +(100*t/H).toFixed(1), pantallas: +(t/vh).toFixed(2),
             alto: Math.round(r.height) }; };

  const atc = pos('button[name="add"], .product-form__submit, [name=add]');

  const fijos = [...document.querySelectorAll('*')].filter(e => {
    const s = getComputedStyle(e), r = e.getBoundingClientRect();
    return (s.position === 'fixed' || s.position === 'sticky')
        && s.visibility !== 'hidden' && s.display !== 'none' && s.opacity !== '0'
        && r.height > 24 && r.width > 100;
  }).map(e => ({ cls: (e.className||'').toString().slice(0,40),
                 alto: Math.round(e.getBoundingClientRect().height),
                 txt: (e.innerText||'').trim().replace(/\s+/g,' ').slice(0,40) }));

  const ctaFijo = fijos.some(f => /agregar|comprar|a[ñn]adir|add to/i.test(f.txt));

  const hasta = atc ? atc.px + 80 : 2200;
  const vistos = new Set(), secuencia = [];
  for (const e of document.querySelectorAll('body *')) {
    const r = e.getBoundingClientRect(), t = r.top + scrollY;
    if (t < 400 || t > hasta || r.height < 18 || e.children.length > 1) continue;
    const txt = (e.innerText||'').trim().replace(/\s+/g,' ').slice(0,60);
    if (!txt || vistos.has(txt)) continue;
    vistos.add(txt); secuencia.push({ px: Math.round(t), pct: +(100*t/H).toFixed(1), txt });
  }
  secuencia.sort((a,b) => a.px - b.px);

  return {
    alto: H, viewport: vh,
    galeria: pos('media-gallery, .product__media-wrapper, .product-gallery'),
    h1: pos('h1'),
    resenas: pos('[class*=rating], [class*=review], .jdgm-prev-badge, .loox-rating'),
    precio: pos('.price, [class*=price]'),
    atc,
    pagoRapido: pos('.shopify-payment-button, [class*=express]'),
    elementosFijosVisibles: fijos,
    hayCTAfijo: ctaFijo,
    veredictoF1: atc && atc.pct > 15 && !ctaFijo
      ? 'F1 CONFIRMADO: CTA al ' + atc.pct + '% de la página y sin barra fija'
      : 'F1 no aplica',
    secuenciaHastaElCTA: secuencia,
  };
})()
