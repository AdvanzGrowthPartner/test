// Aggregate endpoint the dashboard calls: /api/all?month=2026-08
// Runs Meta + Google + Klaviyo + Shopify in parallel and returns one JSON the front hydrates from.
// (Creatives are on-demand at /api/meta-creatives, fetched when the Campañas tab opens.)
import { metaInsights } from "./meta.js";
import { googleAds } from "./google.js";
import { klaviyo } from "./klaviyo.js";
import { shopify } from "./shopify.js";
import { gsc } from "./gsc.js";

export async function onRequestGet({ request, env }) {
  const { json } = await import("./_middleware.js");
  const month = new URL(request.url).searchParams.get("month") || new Date().toISOString().slice(0, 7);
  const [meta, google, kl, sh, se] = await Promise.allSettled([
    metaInsights(env, env.META_ACCOUNT, month),
    googleAds(env, month).catch(e => ({ error: String(e.message || e) })),
    klaviyo(env, month),
    shopify(env, month),
    gsc(env, month, { window: "365" }).catch(e => ({ error: String(e.message || e) })),
  ]);
  const val = r => (r.status === "fulfilled" ? r.value : { error: String(r.reason) });
  const m = val(meta), g = val(google), k = val(kl), s = val(sh), gs = val(se);

  const paidSpend = (m.spend_clp || 0) + (g.spend_clp || 0);
  const paidSales = (m.sales_clp || 0) + (g.sales_clp || 0);
  // MER blended real = venta total del negocio (Shopify) / inversión total en medios (Meta+Google)
  const merReal = (s.sales_clp && paidSpend) ? +(s.sales_clp / paidSpend).toFixed(2) : null;

  return json({
    ok: true,
    month,
    generated_at: new Date().toISOString(),
    meta: m,
    google: g,
    klaviyo: k,
    shopify: s,
    gsc: gs,
    paid: {
      spend_clp: paidSpend || null,
      sales_clp: paidSales || null,
      roas_blended: paidSpend ? +(paidSales / paidSpend).toFixed(2) : null,
      mer_real: merReal,
    },
  });
}
