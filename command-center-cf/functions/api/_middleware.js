// CORS + optional shared-key gate for all /api/* routes.
// Same-origin fetch from the dashboard needs no key; set CC_API_KEY only if
// you also call the API from other origins and want to gate it.
export async function onRequest(context) {
  const { request, env, next } = context;
  const origin = request.headers.get("Origin") || "*";
  const cors = {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "GET,OPTIONS",
    "Access-Control-Allow-Headers": "content-type,x-cc-key",
    "Access-Control-Max-Age": "86400",
  };
  if (request.method === "OPTIONS") return new Response(null, { headers: cors });

  if (env.CC_API_KEY) {
    const key = request.headers.get("x-cc-key") || new URL(request.url).searchParams.get("key");
    if (key !== env.CC_API_KEY) {
      return json({ ok: false, error: "unauthorized" }, 401, cors);
    }
  }
  const res = await next();
  const out = new Response(res.body, res);
  for (const [k, v] of Object.entries(cors)) out.headers.set(k, v);
  return out;
}
export function json(obj, status = 200, extra = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...extra },
  });
}
