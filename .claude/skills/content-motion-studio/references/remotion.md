# Remotion (programmatic video: React → MP4/GIF)

Remotion renders real video files from React components by drawing each frame in headless
Chromium and encoding with ffmpeg. Use it for **rendered deliverables** — reels, promos,
ad variants, animated logos, social clips. (For an in-browser animated *artifact*, use GSAP
instead — Remotion output is a video file, not an interactive page.)

## Scaffold → preview → render

```bash
# 1. Scaffold a project under videos/<name>/ (reuses repo-root node_modules)
bash .claude/skills/content-motion-studio/scripts/new-video.sh <name> "Title"

# 2. Preview interactively (Remotion Studio) — opens a local server
npx remotion studio videos/<name>/src/index.ts

# 3. Render to a file (uses the pre-installed Chromium automatically)
bash .claude/skills/content-motion-studio/scripts/render-video.sh videos/<name>/src/index.ts Main
bash .claude/skills/content-motion-studio/scripts/render-video.sh videos/<name>/src/index.ts Main --gif
bash .claude/skills/content-motion-studio/scripts/render-video.sh videos/<name>/src/index.ts Main --props '{"title":"Nuevo drop"}'
```
`render-video.sh` finds `/opt/pw-browsers/chromium-*/chrome-linux/chrome` and passes it to
Remotion, so nothing is downloaded. Send the resulting file with SendUserFile.

## Project shape (what the scaffold writes)
- `src/index.ts` — `registerRoot(RemotionRoot)`
- `src/Root.tsx` — one or more `<Composition id fps width height durationInFrames component defaultProps />`
- `src/Scene.tsx` — the React component drawn each frame

A composition's `defaultProps` are the editable content; override per-render with `--props '<json>'`.

## Animating (frame-driven, NOT GSAP)
Everything derives from the current frame — there is no timeline object mutating the DOM.
```tsx
import { useCurrentFrame, useVideoConfig, interpolate, spring, AbsoluteFill, Sequence } from "remotion";

const frame = useCurrentFrame();
const { fps, width, height } = useVideoConfig();

// map a frame range to a value, clamped
const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });

// natural motion
const pop = spring({ frame, fps, config: { damping: 12, mass: 0.6 } });
const scale = interpolate(pop, [0, 1], [0.2, 1]);
```
- `<AbsoluteFill>` = full-frame layer (stack them for background/content).
- `<Sequence from={30} durationInFrames={60}>` shifts children's frame 0 to frame 30 — use it
  to sequence shots without hand-computing offsets.
- Standard CSS/SVG for layout and styling.

## Brand icons in video
Import Simple Icons directly (see `simple-icons.md`) and render the path as SVG, animating
`transform`/`opacity` from the frame — the scaffold's `Scene.tsx` shows a spring icon entrance.

## Common config
- Vertical social (reels/TikTok): `width={1080} height={1920}`. Square: `1080x1080`.
  Landscape: `1920x1080`. Duration in frames = seconds × fps (default 30fps).
- Codecs: default `h264` → `.mp4`; `--gif` for looping GIF; `--codec=prores` for editing.
- Audio: `<Audio src={staticFile("track.mp3")} />` with files under a `public/` folder.
- Render a still (thumbnail): `npx remotion still <entry> <id> out.png --frame=45`.

## Gotchas
- `z` (zod) is only exported from `remotion` when `zod` is installed — the scaffold uses a
  plain TS props type instead, so schemas don't break the bundle. Add `zod` only if you want
  the Studio props editor with validation.
- Chromium runs as root here; the render script sets `--chrome-mode=chrome-for-testing`. If a
  render hangs, add `--concurrency=1`.
- Keep per-frame work cheap (no heavy re-parsing each frame) or renders crawl.

## Licensing (matters for an agency)
Remotion is free for individuals and small teams but **companies may need a paid company
license** depending on team size — confirm before shipping client work: https://remotion.dev/license

