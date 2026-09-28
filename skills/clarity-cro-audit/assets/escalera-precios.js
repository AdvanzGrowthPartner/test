/**
 * F5 — Escalera de precios. Pegar en la consola sobre cualquier tienda Shopify.
 * Cambiar el handle de la colección.
 */
(async (handle = 'all') => {
  const d = await fetch(`/collections/${handle}/products.json?limit=250`).then(r => r.json());
  const filas = d.products.map(p => {
    const v = p.variants[0];
    const m = p.title.match(/(\d+)\s*(sticks?|unidades|c[aá]psulas|sobres|d[ií]as)/i);
    const u = m ? parseInt(m[1]) : null;
    const precio = parseInt(v.price);
    return { titulo: p.title.slice(0, 50), precio, unidades: u,
             porUnidad: u ? Math.round(precio / u) : null };
  }).filter(f => f.unidades).sort((a, b) => a.unidades - b.unidades);

  const base = filas[0];
  filas.forEach(f => { f.vsBase = base ? Math.round(100 * (f.porUnidad / base.porUnidad - 1)) + '%' : '—'; });
  console.table(filas);

  const banderas = [];
  for (let i = 1; i < filas.length; i++) {
    if (filas[i].porUnidad >= filas[i-1].porUnidad)
      banderas.push(`${filas[i].titulo} es más caro por unidad que ${filas[i-1].titulo}`);
    else if (filas[i].porUnidad / filas[i-1].porUnidad > 0.90)
      banderas.push(`${filas[i].titulo} solo ahorra ${Math.round(100*(1-filas[i].porUnidad/filas[i-1].porUnidad))}% por unidad`);
  }
  return banderas.length ? { veredicto: 'F5 CONFIRMADO', banderas } : { veredicto: 'escalera sana' };
})()
