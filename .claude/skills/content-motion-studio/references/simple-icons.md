# Simple Icons (3000+ brand SVG icons)

Official monochrome brand glyphs (Shopify, Stripe, Meta, WhatsApp, Klaviyo, TikTok, Google
Ads, …). Each icon carries its **official brand hex**, so you can render on-brand or inherit
`currentColor`. All glyphs are `viewBox="0 0 24 24"` single-path SVGs — trivial to inline.

## Fastest path: the helper script
```bash
node .claude/skills/content-motion-studio/scripts/icon.mjs <slug|name> [--color <hex|brand|currentColor>] [--size <px>] [-o out.svg]
node .claude/skills/content-motion-studio/scripts/icon.mjs --search <query>   # find the slug
```
Examples:
```bash
node scripts/icon.mjs shopify                    # brand-colored, 24px, to stdout
node scripts/icon.mjs "google ads" --size 64 -o ads.svg
node scripts/icon.mjs meta --color currentColor  # inherits CSS text color (nav/buttons)
node scripts/icon.mjs --search whats             # -> whatsapp   WhatsApp   #25D366
```
`--color brand` (default) uses the official hex. Output is a clean `<svg>` you paste
straight into an artifact, a Remotion component, or save as a file.

## In code (npm project, e.g. Remotion)
```ts
import { siShopify } from "simple-icons";
siShopify.title; // "Shopify"
siShopify.hex;   // "7AB55C"
siShopify.path;  // the "d" attribute string
// -> <svg viewBox="0 0 24 24"><path d={siShopify.path} fill={`#${siShopify.hex}`} /></svg>
```
Dynamic lookup by slug (what the video scaffold uses):
```ts
import * as icons from "simple-icons";
const all = Object.values(icons).filter((i:any) => i && i.path && i.slug);
const icon = all.find((i:any) => i.slug === "shopify");
```
Named exports are `si<PascalCaseTitle>` (e.g. `siGoogleads`, `siWhatsapp`). When unsure of
the export name or slug, run `--search`.

## Notes
- Icons are trademarks of their owners — use them to *reference* a brand (integrations,
  "works with", logos strip), not to imply endorsement.
- They're monochrome by design; the brand hex gives the recognizable color. For multi-color
  logos Simple Icons is not the right source.
