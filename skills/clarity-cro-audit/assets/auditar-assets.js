/* auditar-assets.js · F13 — peso, dimensiones y prioridad de las imágenes
   Pegar en la consola, en viewport móvil (390 px), sobre la ficha más visitada.
   Devuelve un objeto listo para copiar al reporte. */
(async () => {
  const vw = innerWidth, dpr = devicePixelRatio || 1;
  const imgs = [...document.images].filter(i => i.currentSrc);

  const peso = async (u) => {
    try {
      const r = await fetch(u, { method: 'HEAD', mode: 'cors' });
      return +r.headers.get('content-length') || null;
    } catch { return null; }
  };

  const filas = [];
  for (const i of imgs.slice(0, 30)) {
    const r = i.getBoundingClientRect();
    const url = i.currentSrc;
    const bytes = await peso(url);
    filas.push({
      src: url.split('?')[0].split('/').pop(),
      anchoParametro: /[?&]width=(\d+)/.exec(url)?.[1] ?? null,   // null = original
      archivo: i.naturalWidth + '×' + i.naturalHeight,
      mostrada: Math.round(r.width) + '×' + Math.round(r.height),
      exceso: r.width ? +(i.naturalWidth / (r.width * dpr)).toFixed(1) : null,
      kb: bytes ? Math.round(bytes / 1024) : 'sin CORS',
      prioridad: i.getAttribute('fetchpriority') || '—',
      carga: i.getAttribute('loading') || '—',
      enPrimeraPantalla: r.top < innerHeight
    });
  }

  const scripts = [...document.scripts].filter(s => s.src);
  const externos = scripts.filter(s => !s.src.includes(location.host));
  const apps = ['loox', 'judge', 'okendo', 'yotpo', 'stamped', 'reviews.io']
    .filter(a => document.documentElement.innerHTML.toLowerCase().includes(a));
  const pre = [...document.querySelectorAll('link[rel="preconnect"],link[rel="dns-prefetch"]')]
    .map(l => l.href);

  const primera = filas.filter(f => f.enPrimeraPantalla);
  const kbPrimera = primera.reduce((a, f) => a + (typeof f.kb === 'number' ? f.kb : 0), 0);
  const sinAncho = filas.filter(f => !f.anchoParametro);
  const mayor = filas.reduce((a, f) => (typeof f.kb === 'number' && f.kb > (a?.kb ?? 0) ? f : a), null);

  const out = {
    viewport: vw + ' px · dpr ' + dpr,
    imagenes: filas,
    resumen: {
      imagenesSinParametroDeAncho: sinAncho.length,
      mayor: mayor ? mayor.src + ' · ' + mayor.kb + ' KB · ' + mayor.archivo : null,
      kbEnPrimeraPantalla: kbPrimera,
      conPrioridadAlta: filas.filter(f => f.prioridad === 'high').length,
      lazyEnPrimeraPantalla: primera.filter(f => f.carga === 'lazy').length,
      scriptsExternos: externos.length,
      preconexiones: pre,
      appsDeResenas: apps
    },
    veredictoF13: []
  };

  const v = out.veredictoF13;
  if (sinAncho.length)               v.push('GRAVE · ' + sinAncho.length + ' imagen(es) servidas sin parámetro de ancho: Shopify entrega el archivo original.');
  if (kbPrimera > 1024)              v.push('GRAVE · ' + kbPrimera + ' KB en la primera pantalla. Umbral: 1.024 KB.');
  if (!out.resumen.conPrioridadAlta) v.push('MEDIO · Ninguna imagen declara fetchpriority="high". El navegador adivina el LCP.');
  if (out.resumen.lazyEnPrimeraPantalla) v.push('MEDIO · Hay loading="lazy" en la primera pantalla: empeora el LCP.');
  if (!pre.some(u => u.includes('cdn.shopify'))) v.push('MEDIO · Falta preconnect al CDN de imágenes.');
  if (externos.length > 25)          v.push('MEDIO · ' + externos.length + ' scripts externos.');
  if (apps.length > 1)               v.push('GRAVE · Dos o más apps de reseñas instaladas: ' + apps.join(', ') + '.');
  filas.filter(f => f.exceso > 2).forEach(f => v.push('MEDIO · ' + f.src + ' se sirve a ' + f.exceso + '× el tamaño mostrado.'));
  if (!v.length) v.push('OK · Sin hallazgos de F13.');

  console.table(filas);
  console.log(out.veredictoF13.join('\n'));
  return out;
})();
