// Google Ads — account-level spend/conversions/value for a month (no MCP needed).
// Secrets: GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
//          GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID (the account, digits only),
//          GOOGLE_ADS_LOGIN_CUSTOMER_ID (the MCC, digits only), FX_CLP_PER_USD.
// The Google Ads API returns cost in micros of the account currency. If the account
// currency is CLP, cost is already in CLP (÷1e6); if USD, multiply by FX.
const API = "https://googleads.googleapis.com/v17";

function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  const since = `${y}-${String(mo).padStart(2, "0")}-01`;
  const until = new Date(y, mo, 0).toISOString().slice(0, 10);
  return { since, until };
}
async function accessToken(env) {
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: env.GOOGLE_ADS_CLIENT_ID,
      client_secret: env.GOOGLE_ADS_CLIENT_SECRET,
      refresh_token: env.GOOGLE_ADS_REFRESH_TOKEN,
      grant_type: "refresh_token",
    }),
  });
  const j = await r.json();
  if (!j.access_token) throw new Error(j.error_description || "oauth failed");
  return j.access_token;
}

export async function googleAds(env, month) {
  if (!env.GOOGLE_ADS_REFRESH_TOKEN || !env.GOOGLE_ADS_CUSTOMER_ID) return { error: "google ads not configured" };
  const { since, until } = monthRange(month);
  const cid = env.GOOGLE_ADS_CUSTOMER_ID.replace(/-/g, "");
  const token = await accessToken(env);
  const query = `SELECT metrics.cost_micros, metrics.conversions, metrics.conversions_value, ` +
    `metrics.impressions, metrics.clicks FROM customer ` +
    `WHERE segments.date BETWEEN '${since}' AND '${until}'`;
  const r = await fetch(`${API}/customers/${cid}/googleAds:searchStream`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "developer-token": env.GOOGLE_ADS_DEVELOPER_TOKEN,
      "login-customer-id": (env.GOOGLE_ADS_LOGIN_CUSTOMER_ID || cid).replace(/-/g, ""),
      "content-type": "application/json",
    },
    body: JSON.stringify({ query }),
  });
  const j = await r.json();
  if (j.error || (Array.isArray(j) && j[0]?.error)) return { error: (j.error || j[0].error)?.message || "google ads error" };
  let costMicros = 0, conv = 0, value = 0, impr = 0, clicks = 0;
  const chunks = Array.isArray(j) ? j : [j];
  for (const c of chunks) for (const row of (c.results || [])) {
    costMicros += Number(row.metrics?.costMicros || 0);
    conv += Number(row.metrics?.conversions || 0);
    value += Number(row.metrics?.conversionsValue || 0);
    impr += Number(row.metrics?.impressions || 0);
    clicks += Number(row.metrics?.clicks || 0);
  }
  const fx = Number(env.FX_CLP_PER_USD || 950);
  const usd = String(env.GOOGLE_ADS_CURRENCY || "CLP").toUpperCase() === "USD";
  const cost = costMicros / 1e6, val = value; // value in account currency units
  const toClp = n => Math.round(usd ? n * fx : n);
  return {
    spend_clp: toClp(cost), conversions: +conv.toFixed(1),
    sales_clp: toClp(val), roas: cost ? +(val / cost).toFixed(2) : null,
    impressions: impr, clicks,
  };
}

export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  try { const d = await googleAds(env, month); return json({ ok: !d.error, month, google: d }); }
  catch (e) { return json({ ok: false, month, google: { error: String(e.message || e) } }); }
}
