// Shopify — rentabilidad del mes (ventas totales, pedidos, ticket) + top productos.
// Usa ShopifyQL vía Admin GraphQL (requiere scopes read_reports, read_products).
// Secrets: SHOPIFY_SHOP (subdominio *.myshopify, ej "25trtw-d5"), SHOPIFY_TOKEN (Admin API token),
//          SHOPIFY_API_VERSION (default 2024-10).
function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  return { since: `${y}-${String(mo).padStart(2, "0")}-01`, until: new Date(y, mo, 0).toISOString().slice(0, 10) };
}
async function gql(env, query) {
  const ver = env.SHOPIFY_API_VERSION || "2024-10";
  const r = await fetch(`https://${env.SHOPIFY_SHOP}.myshopify.com/admin/api/${ver}/graphql.json`, {
    method: "POST",
    headers: { "X-Shopify-Access-Token": env.SHOPIFY_TOKEN, "content-type": "application/json" },
    body: JSON.stringify({ query }),
  });
  return r.json();
}
function parseTable(resp) {
  const q = resp?.data?.shopifyqlQuery;
  const t = q?.tableData;
  if (!t) return { cols: [], rows: [] };
  const cols = (t.columns || []).map(c => c.name);
  return { cols, rows: t.rowData || [] };
}
async function shopifyql(env, ql) {
  const query = `{ shopifyqlQuery(query: ${JSON.stringify(ql)}) { __typename ` +
    `... on TableResponse { tableData { columns { name dataType } rowData } } ` +
    `parseErrors { code message } } }`;
  const resp = await gql(env, query);
  if (resp.errors) return { error: resp.errors[0]?.message || "shopify graphql error" };
  const pe = resp?.data?.shopifyqlQuery?.parseErrors;
  if (pe && pe.length) return { error: pe[0].message };
  return parseTable(resp);
}

export async function shopify(env, month) {
  if (!env.SHOPIFY_SHOP || !env.SHOPIFY_TOKEN) return { error: "shopify not configured" };
  const { since, until } = monthRange(month);
  // Totales del mes
  const totals = await shopifyql(env,
    `FROM sales SHOW total_sales, orders, average_order_value SINCE ${since} UNTIL ${until}`);
  if (totals.error) return totals;
  const row = totals.rows[0] || [];
  const idx = n => totals.cols.indexOf(n);
  const num = v => Number(String(v ?? "0").replace(/[^\d.-]/g, "")) || 0;
  const sales = num(row[idx("total_sales")]);
  const orders = num(row[idx("orders")]);
  const aov = num(row[idx("average_order_value")]);
  // Top productos por venta
  const prod = await shopifyql(env,
    `FROM sales SHOW total_sales, net_items_sold GROUP BY product_title ` +
    `SINCE ${since} UNTIL ${until} ORDER BY total_sales DESC LIMIT 8`);
  let products = [];
  if (!prod.error) {
    const ti = prod.cols.indexOf("product_title"), si = prod.cols.indexOf("total_sales"), ui = prod.cols.indexOf("net_items_sold");
    products = prod.rows.map(r => ({ title: String(r[ti]), sales_clp: num(r[si]), units: num(r[ui]) }));
  }
  // Imágenes (best-effort: mapea title -> featuredImage)
  try {
    const img = await gql(env, `{ products(first: 60, sortKey: BEST_SELLING) { edges { node { title featuredImage { url } } } } }`);
    const map = {};
    for (const e of (img?.data?.products?.edges || [])) map[e.node.title] = e.node.featuredImage?.url || null;
    products = products.map(p => ({ ...p, image: map[p.title] || null }));
  } catch (e) { /* imágenes opcionales */ }

  return { sales_clp: Math.round(sales), orders, aov_clp: Math.round(aov), products };
}

export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  const d = await shopify(env, month);
  return json({ ok: !d.error, month, shopify: d });
}
