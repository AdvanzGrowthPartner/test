// Meta — galería de creativos por rendimiento del mes (thumbnail + ROAS/CTR/gasto por anuncio).
// Ruta: /api/creatives?month=YYYY-MM  ·  Secrets: META_TOKEN, META_ACCOUNT, FX_CLP_PER_USD.
const GRAPH = "https://graph.facebook.com/v21.0";
function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  return { since: `${y}-${String(mo).padStart(2, "0")}-01`, until: new Date(y, mo, 0).toISOString().slice(0, 10) };
}
export async function creatives(env, account, month, limit = 9) {
  if (!env.META_TOKEN || !account) return { error: "meta not configured" };
  const { since, until } = monthRange(month);
  const tr = encodeURIComponent(JSON.stringify({ since, until }));
  // Un solo call: ads con su creative (thumbnail) + insights del mes embebidos.
  const fields = `name,effective_status,` +
    `creative{thumbnail_url,image_url},` +
    `insights.time_range(${JSON.stringify({ since, until })}){spend,purchase_roas,ctr,impressions,actions}`;
  const url = `${GRAPH}/act_${account}/ads?fields=${encodeURIComponent(fields)}&limit=200&access_token=${env.META_TOKEN}`;
  const r = await fetch(url);
  const j = await r.json();
  if (j.error) return { error: j.error.message };
  const fx = Number(env.FX_CLP_PER_USD || 950);
  const rows = [];
  for (const ad of (j.data || [])) {
    const ins = ad.insights?.data?.[0];
    if (!ins) continue;
    const spend = Number(ins.spend || 0);
    if (spend <= 0) continue;
    const roas = Number((ins.purchase_roas || []).find(x => x.action_type === "omni_purchase")?.value ||
      (ins.purchase_roas || [])[0]?.value || 0);
    const purchases = Number((ins.actions || []).find(x => x.action_type === "omni_purchase")?.value || 0);
    rows.push({
      name: ad.name,
      thumb: ad.creative?.image_url || ad.creative?.thumbnail_url || null,
      spend_usd: +spend.toFixed(0), spend_clp: Math.round(spend * fx),
      roas: roas ? +roas.toFixed(2) : null,
      ctr: ins.ctr ? +Number(ins.ctr).toFixed(2) : null,
      purchases,
    });
  }
  rows.sort((a, b) => b.spend_usd - a.spend_usd);
  return { creatives: rows.slice(0, limit) };
}
export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const p = new URL(request.url).searchParams;
  const month = p.get("month") || new Date().toISOString().slice(0, 7);
  const d = await creatives(env, p.get("account") || env.META_ACCOUNT, month);
  return json({ ok: !d.error, month, creatives: d.creatives || [], error: d.error });
}
