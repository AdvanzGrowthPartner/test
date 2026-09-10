---
name: content-motion-studio
description: >-
  Produce animated content — animated web artifacts and rendered videos — with three
  tools wired together: GSAP (DOM/scroll animation), Simple Icons (3000+ brand SVG icons con
  su color oficial), and Remotion (programmatic React → MP4/GIF video). Use this skill
  SIEMPRE que el usuario quiera "meter content", armar un artifact animado, un video, un
  reel/ad/promo, un logo animado, una landing con movimiento, un hero animado, íconos de
  marca (Shopify, Meta, Stripe, WhatsApp, TikTok…), motion graphics, un GIF, o diga
  "anímame esto", "hazlo con movimiento", "video con Remotion", "usa GSAP", "ponle los
  íconos de", "genera un video/mp4/gif", "content animado para redes/ads". Also trigger on
  English: animate, motion, video, reel, promo, animated landing/hero, brand icons, GIF.
  Runs on the repo-root install of gsap + simple-icons + remotion.
license: Complete terms in LICENSE.txt
---

# Content Motion Studio

One skill, three engines, two kinds of output. Pick the engine by what the user needs to
end up with:

| Output the user wants | Engine | Why |
|---|---|---|
| An **interactive/animated page** (artifact): hero reveal, scroll effects, marquee, animated landing/one-pager | **GSAP** | Animates the live DOM; ships as a single self-contained HTML artifact |
| A **video file**: reel, ad variant, promo, animated logo, social clip (.mp4/.gif) | **Remotion** | Renders React to real frames → encoded video |
| **Brand icons** in either of the above (Shopify, Meta, Stripe, WhatsApp, …) | **Simple Icons** | 3000+ official glyphs with brand hex; inline as SVG |

Simple Icons is the shared ingredient — it feeds both the GSAP artifact and the Remotion video.

## Setup (already installed at repo root)

`gsap`, `simple-icons`, and `remotion` (+ `@remotion/cli/bundler/renderer`, `react`) are in
`package.json`. If `node_modules/` is missing (fresh container), run `npm install` at the
repo root once. Everything below reuses that install — no per-project install.

## Do this

### 1 — Animated artifact (GSAP + Simple Icons)
For anything that should be an **animated page** the user views/interacts with:
1. Start from `assets/gsap-artifact-template.html` — a paste-ready, opinionated dark hero
   with staggered word entrance, a brand-icon marquee, and scroll-reveal cards.
2. Swap the copy, palette (`--accent`, `--bg`, `--ink`), and brand icons. Generate icons with:
   ```bash
   node scripts/icon.mjs <slug> --size 40           # brand-colored SVG to stdout
   node scripts/icon.mjs --search <query>           # find the right slug
   ```
3. Publish it as an Artifact (or send the HTML). Read `references/gsap.md` before writing
   GSAP so timelines/ScrollTrigger/easing are used well and it loads from cdnjs correctly.

**Design bar:** avoid the "AI slop" defaults — no everything-centered + purple-gradient +
uniform-rounded-corners + Inter. Animate with intent (stagger, one accent element, respect
`prefers-reduced-motion`). If the user's brand voice/theme is known (e.g. an Advanz theme),
apply it.

### 2 — Video (Remotion + Simple Icons)
For a **video file** deliverable:
```bash
# scaffold → preview → render
bash scripts/new-video.sh <name> "Title"
npx remotion studio videos/<name>/src/index.ts          # optional live preview
bash scripts/render-video.sh videos/<name>/src/index.ts Main            # -> videos/<name>/out/Main.mp4
bash scripts/render-video.sh videos/<name>/src/index.ts Main --gif      # looping GIF
bash scripts/render-video.sh videos/<name>/src/index.ts Main --props '{"title":"Nuevo drop"}'
```
The render script auto-detects the pre-installed Chromium, so nothing downloads. Edit
`videos/<name>/src/Scene.tsx` for the animation and `Root.tsx` `defaultProps` for content
(title/subtitle/iconSlug/bg/accent). Read `references/remotion.md` before editing — Remotion
is **frame-driven** (`interpolate`/`spring`/`useCurrentFrame`), not a GSAP timeline. When the
file is ready, deliver it with SendUserFile.

Sensible sizes: reels/TikTok `1080×1920`, feed square `1080×1080`, YouTube `1920×1080`;
duration in frames = seconds × fps (30fps default).

### 3 — Just brand icons
If all they need is a logo/icon strip: run `scripts/icon.mjs` (see `references/simple-icons.md`
for the code path and named-export naming). Use `--color currentColor` for icons that inherit
button/nav text color, `--color brand` (default) for the official color.

## Deciding fast
- "landing / página / hero / que se mueva al scrollear / artifact" → **GSAP artifact** (§1)
- "video / reel / ad / mp4 / gif / clip / logo animado para redes" → **Remotion** (§2)
- "ícono/logo de <marca>" → **Simple Icons** (§3), or inline into §1/§2

## Files
- `assets/gsap-artifact-template.html` — animated artifact starting point
- `scripts/icon.mjs` — Simple Icons → SVG (by slug/name, brand-colored, searchable)
- `scripts/new-video.sh` — scaffold a Remotion project under `videos/<name>/`
- `scripts/render-video.sh` — render a composition to MP4/GIF with the local Chromium
- `references/gsap.md` · `references/simple-icons.md` · `references/remotion.md` — read the
  relevant one before writing code with that tool.
