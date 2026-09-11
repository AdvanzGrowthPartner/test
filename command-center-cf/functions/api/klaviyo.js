// Klaviyo — email channel: campaign + flow revenue for a month.
// Secrets: KLAVIYO_KEY (private API key pk_...), KLAVIYO_CONV_METRIC (default RP5iQ9 = Placed Order).
const BASE = "https://a.klaviyo.com/api";
const REV = "2024-10-15"; // Klaviyo API revision

function monthRange(m) {
  const [y, mo] = m.split("-").map(Number);
  const start = new Date(Date.UTC(y, mo - 1, 1)).toISOString();
  const end = new Date(Date.UTC(y, mo, 1)).toISOString();
  return { start, end };
}
async function report(kind, env, month) {
  const { start, end } = monthRange(month);
  const body = {
    data: {
      type: `${kind}-values-report`,
      attributes: {
        statistics: ["recipients", "conversions"],
        timeframe: { start, end },
        conversion_metric_id: env.KLAVIYO_CONV_METRIC || "RP5iQ9",
        filter: `equals(send_channel,"email")`,
      },
    },
  };
  const r = await fetch(`${BASE}/${kind}-values-reports/`, {
    method: "POST",
    headers: {
      Authorization: `Klaviyo-API-Key ${env.KLAVIYO_KEY}`,
      "content-type": "application/json",
      accept: "application/json",
      revision: REV,
    },
    body: JSON.stringify(body),
  });
  const j = await r.json();
  if (j.errors) return { error: j.errors[0]?.detail || "klaviyo error" };
  const results = j?.data?.attributes?.results || [];
  let rev = 0, conv = 0;
  for (const row of results) {
    const tag = (row.groupings && row.groupings.flow_name) || "";
    if (/NUTRI|NO USAR|Nutrikit/i.test(tag)) continue; // excluir circuito de códigos
    rev += Number(row.statistics?.conversion_value || 0);
    conv += Number(row.statistics?.conversions || 0);
  }
  return { revenue_clp: Math.round(rev), conversions: conv };
}

export async function klaviyo(env, month) {
  if (!env.KLAVIYO_KEY) return { error: "klaviyo not configured" };
  const [camp, flow] = await Promise.all([report("campaign", env, month), report("flow", env, month)]);
  if (camp.error) return camp; if (flow.error) return flow;
  return {
    campaigns_clp: camp.revenue_clp,
    flows_clp: flow.revenue_clp,
    total_clp: camp.revenue_clp + flow.revenue_clp,
    flow_share: camp.revenue_clp + flow.revenue_clp ? +(flow.revenue_clp / (camp.revenue_clp + flow.revenue_clp)).toFixed(3) : 0,
  };
}

export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  const d = await klaviyo(env, month);
  return json({ ok: !d.error, month, klaviyo: d });
}
