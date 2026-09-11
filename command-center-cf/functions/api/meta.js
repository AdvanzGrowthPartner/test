// Meta Ads — account-level insights for a month, straight from the Graph API.
// Secrets: META_TOKEN (long-lived system-user token), META_ACCOUNT (numeric id, no act_),
// optional META_ACCOUNT_MAYORISTA, FX_CLP_PER_USD (default 950).
const GRAPH = "https://graph.facebook.com/v21.0";

function monthRange(m) { // "2026-08" -> {since,until}
  const [y, mo] = m.split("-").map(Number);
  const since = `${y}-${String(mo).padStart(2, "0")}-01`;
  const until = new Date(y, mo, 0).toISOString().slice(0, 10);
  return { since, until };
}

export async function metaInsights(env, account, month) {
  if (!env.META_TOKEN || !account) return { error: "meta not configured" };
  const { since, until } = monthRange(month);
  const fields = "spend,purchase_roas,actions,impressions,reach,ctr,cpm,inline_link_clicks";
  const url = `${GRAPH}/act_${account}/insights?level=account&fields=${fields}` +
    `&time_range=${encodeURIComponent(JSON.stringify({ since, until }))}&access_token=${env.META_TOKEN}`;
  const r = await fetch(url);
  const j = await r.json();
  if (j.error) return { error: j.error.message };
  const row = (j.data && j.data[0]) || {};
  const fx = Number(env.FX_CLP_PER_USD || 950);
  const spend = Number(row.spend || 0);
  const roas = Number((row.purchase_roas || []).find(x => x.action_type === "omni_purchase")?.value ||
    (row.purchase_roas || [])[0]?.value || 0);
  const purchases = Number((row.actions || []).find(x => x.action_type === "omni_purchase")?.value || 0);
  return {
    account, currency: "USD", fx,
    spend_usd: spend, spend_clp: Math.round(spend * fx),
    roas,
    purchases,
    cpa_usd: purchases ? +(spend / purchases).toFixed(2) : null,
    sales_clp: Math.round(spend * roas * fx),
    impressions: Number(row.impressions || 0),
    reach: Number(row.reach || 0),
    ctr: row.ctr ? +Number(row.ctr).toFixed(2) : null,
    cpm_usd: row.cpm ? +Number(row.cpm).toFixed(2) : null,
    link_clicks: Number(row.inline_link_clicks || 0),
  };
}

export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const p = new URL(request.url).searchParams;
  const month = p.get("month") || new Date().toISOString().slice(0, 7);
  const acc = p.get("account") || env.META_ACCOUNT;
  const data = await metaInsights(env, acc, month);
  return json({ ok: !data.error, month, meta: data });
}
