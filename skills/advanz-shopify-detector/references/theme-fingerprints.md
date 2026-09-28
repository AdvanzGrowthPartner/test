# Theme Fingerprints

Detailed signatures for identifying Shopify themes from public HTML/CSS.

## How theme detection works

Themes leave traces in 4 places:
1. **Footer attribution** — free/freemium themes often force a "Powered by X" link
2. **CSS class naming conventions** — each theme vendor has a signature BEM-style
3. **Section/block IDs** — `template--[shop_id]__[name]` reveals OS 2.0 + naming patterns
4. **Asset paths** — `/cdn/shop/t/[N]/assets/[filename]` filenames are theme-specific

## Detection priority

Run these checks in order. Stop at first high-confidence match.

```bash
# 1. Footer attribution (highest confidence)
grep -oiE "powered by ([a-z]+) theme" /home/claude/scrape_home.html

# 2. Theme name in JS bundle
grep -oE 'theme[_-]name["\\:\s]+["\']([^"\']+)' /home/claude/scrape_home.html

# 3. Asset filename signatures
grep -oE '/cdn/shop/t/[0-9]+/assets/[a-z\-_]+\.(css|js)' /home/claude/scrape_home.html | sort -u | head -20

# 4. Section IDs (reveals OS 2.0 architecture)
grep -oE 'template--[0-9]+__[a-z\-_]+' /home/claude/scrape_home.html | sort -u
```

---

## Themes — detailed fingerprints

### Dawn (Shopify free, official)
- **Vendor**: Shopify Inc.
- **Footer**: No forced attribution
- **Signature CSS**: `.shopify-section`, `.header__inline-menu`, `.product-form__buttons`, `.card__inner`
- **Asset signature**: `component-*.css` (component-cart.css, component-card.css, etc.)
- **JS modules**: `pubsub.js`, `cart-drawer.js`, `product-form.js`
- **When stores use it**: starter stores, MVPs, small DTC
- **Replicability for Advanz**: 🟢 Default base for new client migrations

### Shrine (Karat / Karat Themes)
- **Vendor**: Karat
- **Footer**: `Powered by [Shrine](https://shrinetheme.com/ "Shrine theme")` — FORCED attribution
- **Signature CSS**: `.shrine-`, `.kapital-`, blue/yellow color schemes default
- **Asset signature**: `shrine-*.css`, often paired with `bundle-*.js`
- **Common pattern**: tier-based quantity discount UI ("7 unidades / 14 unidades / 28 unidades") built-in
- **When stores use it**: snacks, supplements, food DTC (Caraboni is a textbook case)
- **Verticals seen**: food/snacks, supplements, beverages, wellness
- **Replicability for Advanz**: theme-native bundle UI is replicable in any theme with Liquid

### Impulse (Pixel Union)
- **Vendor**: Pixel Union
- **Footer**: No forced attribution (paid)
- **Signature CSS**: `.product-block-list`, `data-section-type="static-product"`, `.product-single__`, `.collection-grid__`
- **Asset signature**: `theme.scss.liquid` compiled, `vendor-*.js`
- **JS signature**: `data-section-id`, `data-section-type` attribute pattern
- **When stores use it**: fashion, apparel, lifestyle
- **Cost**: $350 one-time
- **Replicability for Advanz**: client must purchase theme to install

### Prestige (Maestrooo)
- **Vendor**: Maestrooo
- **Footer**: No forced attribution (paid)
- **Signature CSS**: Capitalized BEM — `.Header__`, `.Product__`, `.ProductMeta__`, `.Footer__`
- **Asset signature**: `prestige-*.css`, often `app.js` as main bundle
- **JS signature**: `window.theme = { ... }` config object
- **When stores use it**: premium DTC, beauty, fashion, lifestyle
- **Cost**: $380 one-time
- **Verticals seen**: beauty, fashion, premium consumer

### Motion (Archetype)
- **Vendor**: Archetype Themes
- **Footer**: No forced attribution (paid)
- **Signature CSS**: `.scroll-trigger`, `data-motion`, `data-animate`, `.split-text`
- **Asset signature**: `motion-*.css`, motion design system
- **JS signature**: heavy use of IntersectionObserver, scroll-triggered animations
- **When stores use it**: storytelling brands, premium DTC with brand identity focus
- **Cost**: $380 one-time

### Symmetry (Clean Themes)
- **Vendor**: Clean Themes
- **Footer**: No forced attribution
- **Signature CSS**: `.symmetry-`, `.module-`, `.section-`
- **Asset signature**: `symmetry.scss.liquid` compiled

### Warehouse (Archetype)
- **Signature CSS**: `.warehouse-`, prefix on most classes
- **When stores use it**: catalog-heavy, B2B-adjacent, hardware/tools

### Pipeline (Groupthought)
- **Vendor**: Groupthought
- **Footer**: No forced attribution
- **Signature CSS**: `.pipeline-`, `.template-product`, minimal design
- **When stores use it**: minimal premium, fashion, design objects

### Empire (Pixel Union)
- **Signature CSS**: `.empire-`, blog-heavy template structure
- **When stores use it**: editorial brands, content-heavy commerce

### Stiletto (Maestrooo)
- Variant of Prestige with fashion-specific sections
- **Verticals**: fashion, apparel

### Booster (Booster Apps)
- **Footer**: Often forced
- **Signature CSS**: `.booster-`
- **Reputation**: Lower quality, dropshipping-heavy

### Debutify
- **Signature CSS**: `.debutify-`
- **Reputation**: Dropshipping, conversion-app-heavy

### Turbo (theme by ?)
- **Signature CSS**: `.turbo-`
- **Use case**: high-performance focus

### Flex (Out of the Sandbox)
- **Vendor**: Out of the Sandbox
- **Signature CSS**: `.flex-`, modular sections
- **Cost**: $380

### Retina (Out of the Sandbox)
- **Vendor**: Out of the Sandbox
- **Signature CSS**: `.retina-`

### Broadcast (Out of the Sandbox)
- **Signature CSS**: `.broadcast-`

### Streamline / Showcase / Habitat / Palo Alto (Maestrooo)
- All share Maestrooo BEM capitalization pattern

### Custom/headless (Hydrogen, Remix, Next.js + Storefront API)
- **Signal**: no `/cdn/shop/t/` asset paths, but `cdn.shopify.com/s/files/` for product images still present
- **Signal**: routes don't follow `/products/[handle]` pattern strictly, may be `/p/[handle]` or other
- **JS**: React/Vue/Svelte bundle signatures (`__NEXT_DATA__`, `__remixContext`, `__sveltekit_`)
- **Detection**: harder — many app signals still work because they hook into Shopify backend, but theme detection doesn't apply

---

## Tell when it's heavily customized vs vanilla

| Sign of heavy customization | What it means for replicability |
|---|---|
| Section IDs without `template--[id]__` prefix | Custom theme, not OS 2.0 → harder to replicate cleanly |
| Mix of vendor signatures (`.shrine-` + `.Header__`) | Theme fork or merge → custom dev work involved |
| Inline `<style>` blocks > 500 lines | Heavy ad-hoc styling → copy means re-styling from scratch |
| Custom `assets/custom.js` with non-vendor prefix | Bespoke logic → may need reverse engineering |
| Metafields visible in product JSON (`metafields: { ... }` non-empty) | Theme relies on custom metafields → must replicate metafield schema before copying Liquid |

## What to report

In the analysis report, the theme line should look like:

```
Theme: Shrine (Karat) — confirmed via forced footer attribution + .shrine- class signatures
       Customization level: moderate (theme native bundle UI used as-is, custom inline styles for hero)
       Cost to install: $200-300 one-time (Shopify Theme Store)
       Replicability: theme-native bundle pattern is replicable in any theme with ~4 hours of Liquid work
```
