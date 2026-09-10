# GSAP (animation for HTML artifacts)

GSAP animates the DOM/SVG/canvas. Use it for **animated artifacts** (landing sections,
hero reveals, marquees, scroll effects, counters). Not for rendered video — that's Remotion.

## Loading

**Inside a claude.ai artifact** (no build): load from cdnjs — the only script CDN allowed
by the artifact CSP. Pin an exact version.
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
<script>gsap.registerPlugin(ScrollTrigger);</script>
```
Other free plugins on the same path: `Flip.min.js`, `Draggable.min.js`, `TextPlugin.min.js`,
`MotionPathPlugin.min.js`, `ScrollToPlugin.min.js`, `Observer.min.js`.
SplitText, ScrollSmoother, MorphSVG etc. are now free in GSAP 3.13 but ship in the bonus
files — if a plugin 404s on cdnjs, animate without it rather than breaking the artifact.

**In a bundled/npm project**: `import { gsap } from "gsap"` (installed at repo root).

## Core API

- `gsap.to(target, {vars})` / `gsap.from(...)` / `gsap.fromTo(target, fromVars, toVars)`
- `target` = CSS selector, element, or array. `gsap.utils.toArray(".x")` for lists.
- Common vars: `x, y, xPercent, yPercent, scale, rotate, opacity, duration, delay, ease,
  stagger, repeat, yoyo`. Transforms are GPU-friendly; prefer them over `top/left`.
- Easing: `power1..4.out/in/inOut`, `back.out(1.7)`, `elastic.out(1,0.3)`, `sine.inOut`,
  `expo.out`, `steps(n)`. Default is `power1.out`.

## Timelines (sequencing)
```js
const tl = gsap.timeline({ defaults: { ease: "power3.out", duration: 0.8 } });
tl.from(".title", { yPercent: 120, opacity: 0, stagger: 0.08 })
  .from(".lead", { y: 20, opacity: 0 }, "-=0.4")   // overlap 0.4s
  .to(".cta", { scale: 1, duration: 0.5 }, "<");     // start with previous
```
Position param: number = absolute time, `"+=0.5"`/`"-=0.5"` relative, `"<"`/`">"` start/end
of previous tween.

## ScrollTrigger (reveals on scroll)
```js
gsap.to(".card", {
  opacity: 1, y: 0,
  scrollTrigger: { trigger: ".card", start: "top 85%", toggleActions: "play none none reverse" },
});
```
For pinning / scrubbed animation: `scrollTrigger: { trigger, start: "top top", end: "+=100%", scrub: true, pin: true }`.

## Patterns that read as intentional (avoid "AI slop")
- Stagger word/line entrances instead of fading the whole block at once.
- Animate a single accent element (a rule, an underline, one icon) rather than everything.
- Respect reduced motion:
  `if (matchMedia("(prefers-reduced-motion: reduce)").matches) gsap.globalTimeline.timeScale(0.001);`
- Set the "from" state in CSS (`opacity:0`) so there's no flash before JS runs, or use
  `gsap.set()` first.

See `assets/gsap-artifact-template.html` for a complete, paste-ready starting point.
