// Obtiene el refresh_token de Google Ads (una vez). Node 18+.
// Uso:  GOOGLE_ADS_CLIENT_ID=xxx GOOGLE_ADS_CLIENT_SECRET=yyy node get-google-refresh-token.mjs
// (o editá las constantes de abajo). Abre el navegador, autorizás, y la terminal imprime el token.
import http from "node:http";
import { exec } from "node:child_process";

const CLIENT_ID = process.env.GOOGLE_ADS_CLIENT_ID || "PEGA_TU_CLIENT_ID";
const CLIENT_SECRET = process.env.GOOGLE_ADS_CLIENT_SECRET || "PEGA_TU_CLIENT_SECRET";
const PORT = 5599;
const REDIRECT = `http://localhost:${PORT}/oauth2callback`;
// Ads:  https://www.googleapis.com/auth/adwords
// Search Console: https://www.googleapis.com/auth/webmasters.readonly
// Podés pedir ambos scopes a la vez (separados por espacio) para un solo refresh_token.
const SCOPE = process.env.SCOPE || "https://www.googleapis.com/auth/adwords";

if (CLIENT_ID.startsWith("PEGA_")) {
  console.error("Falta client_id/secret. Pasalos por variables de entorno o editá el archivo.");
  process.exit(1);
}

const authUrl =
  "https://accounts.google.com/o/oauth2/v2/auth?" +
  new URLSearchParams({
    client_id: CLIENT_ID, redirect_uri: REDIRECT, response_type: "code",
    scope: SCOPE, access_type: "offline", prompt: "consent",
  });

const opener = process.platform === "darwin" ? "open" : process.platform === "win32" ? "start" : "xdg-open";
console.log("\nAbrí este URL, autorizá la cuenta con acceso al MCC, y volvé:\n\n" + authUrl + "\n");
try { exec(`${opener} "${authUrl}"`); } catch {}

http.createServer(async (req, res) => {
  if (!req.url.startsWith("/oauth2callback")) { res.end("ok"); return; }
  const code = new URL(req.url, REDIRECT).searchParams.get("code");
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      code, client_id: CLIENT_ID, client_secret: CLIENT_SECRET,
      redirect_uri: REDIRECT, grant_type: "authorization_code",
    }),
  });
  const j = await r.json();
  console.log("\n=== TU GOOGLE_ADS_REFRESH_TOKEN ===\n" + (j.refresh_token || JSON.stringify(j)) + "\n");
  res.end("Listo. Volvé a la terminal: ahí está tu refresh_token. Podés cerrar esta pestaña.");
  setTimeout(() => process.exit(0), 300);
}).listen(PORT, () => console.log(`Esperando el callback en ${REDIRECT} ...`));
