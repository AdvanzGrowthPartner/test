# Paid Media — Strategy, Structure, Scaling

## Meta Ads Architecture

### Campaign Structure: Cold/Warm/Hot
Cold (Prospecting) 60% budget: ASC (Advantage+ Shopping) or CBO broad. Audience: broad or Lookalike 1-3% of buyers. Creatives: UGC, Problem→Solution, educational. ROAS target: 1.5-2.5x.
Warm (Retargeting) 30%: Manual ABO with exclusions. Audience: visitors 7-30d, VC no ATC, ATC no purchase. Creatives: carousel viewed products, offer, urgency. ROAS: 3-6x.
Hot (Retention) 10%: DPA or manual. Audience: customers 30-180d, 1x buyers, inactive. Creatives: new launches, bundles. ROAS: 2-4x.

### Audiences in 2025
Broad + ASC is default for prospecting when >50 purchases/week + CAPI server-side. The algorithm beats manual targeting.
Lookalike 1-3% when <50 purchases/week. Source: buyers (best), ATC (second), visitors (third).
Custom retargeting: visitors 7/14/30d, VC no ATC, ATC no purchase, exclude buyers.
Custom engagement: IG/FB interaction 30-90d. Use as signal in ASC.
Customer list: from Shopify/Klaviyo. Segment 1 purchase vs 2+ vs inactive. Use for retention + Lookalike seed.

### 5 Creative Types
1. UGC testimonial — customer talking to camera, 15-30 sec. Highest credibility for cold.
2. Problem→Solution — 3 sec pain visual → product as hero.
3. Before/After — split screen or temporal sequence. Beauty, pets, sport.
4. Unboxing/Demo — product arriving, being used. Reduces online-vs-physical gap.
5. Educational/Myth-busting — data + problem + solution. Health, longevity, wellness.

### Hook Bank (first 3 seconds)
Pain question: "¿[Problem]?" Shocking stat: "X% of [group] has [problem]". Pattern interrupt: unexpected visual. Counter-intuition: "What everyone does is wrong". Direct result: end result FIRST. Social proof: "X people already [result]".

### Scaling Rules
Scale 20-30% every 3-5 days when ROAS stable >5 days. Kill ad: CTR <1% after 1K impressions or CPA >2x target for 3+ days. Rotate creatives: frequency >3 or CTR declining. Min 3-5 active creatives per ad set. Min daily budget = CPA target × 3.
Horizontal scaling: new ad set, different creative angle, same audience. When vertical (budget) scaling starts degrading.

### Creative Fatigue
Happens when frequency >3/week and CPA rises 10-25%. Solution: rotate, NOT pause campaign. Need 3-5 creatives active + new pieces every 2-3 weeks. Creative volume = competitive advantage.

### Diagnostic Framework
CTR low → creative problem (change hook). CTR high + CVR low → PDP problem (fix page). CPC high → audience saturated (go broader). CPA rising → fatigue (rotate). ROAS low + CPA ok → AOV low (bundles/upsells). Everything ok but flat → ceiling (add channels).

## Google Ads Architecture

### 4 Campaign Layers
1. Performance Max (50-60%): Feed + Shopping + Search + YouTube + Display + Discovery. Feed = 80% of success. Asset groups by category. Audience signals (not restrictions). Exclude brand terms.
2. Search Brand (10-15%): Exact + phrase. Protect brand. ROAS 8-15x.
3. Search Non-brand (15-25%): Long-tail high-intent keywords. "[product type] buy [country]". Review Search Terms weekly. Add negatives aggressively.
4. Remarketing (10-15%): Display + YouTube. Visual reminder, not primary.

### Feed Optimization (80% of Shopping success)
Title: [Brand] + [Product] + [Key attribute] + [Variant]. Max 150 chars. Keywords first. NOT Shopify defaults.
Description: benefits + keywords in first 150 chars. No marketing copy.
Image: white bg, high res (800x800 min), product visible, no text overlay.
Price/stock: real-time sync. Google penalizes out-of-stock hard.
GTIN/MPN: required for matching. Category: most specific Google taxonomy.
Custom labels: margin, bestseller, new, seasonal — for PMax segmentation.
App recommendation: DataFeedWatch, Simprosys, FeedHub. Optimized titles alone: +20-40% CTR.

### PMax Traps
Brand cannibalization: if >70% revenue from brand searches, PMax is eating organic brand traffic. Solution: separate brand Search campaign + exclude brand from PMax. Measure PMax non-brand ROAS.

### Meta + Google Flywheel
Meta creates demand (sees ad) → doesn't buy immediately → Googles days later → Google captures → purchase. Google gets attribution, Meta created demand. MER (total revenue / total spend) is the unified metric. If you turn off Meta and Google ROAS drops in 2-3 weeks, Meta was creating the demand.

## TikTok Ads (Supplementary)
Lower intent than Meta/Google. Better for awareness + viral potential. CPMs often lower but CVR also lower. Best for: visual products, younger demos, trend-based content. Creative format: native TikTok style (not polished ads). Use Spark Ads (boost organic TikToks). Test with 10-15% of budget after Meta + Google are stable.

## Budget Allocation (Typical Ecomm)
Total ad spend: Meta 60-70%, Google 25-35%, TikTok 0-10%.
Minimum viable: CPA × 3 per day per campaign. At $20 CPA = $60/day = $1,800/mo minimum.
Scale when: CPA consistently below max for 5+ days. Don't scale when CPA is above target.

## Tracking (Non-Negotiable)
Meta: Pixel + CAPI server-side. Without CAPI: lose ~40% data post-iOS14. EMQ (Event Match Quality) target: >6.0.
Google: Conversion tag + Enhanced Conversions. Purchase as PRIMARY (not Secondary).
GA4: Events configured — page_view, view_item, add_to_cart, begin_checkout, purchase.
Domain verification + Aggregated Event Measurement for Meta.
UTM tracking consistent across ALL channels.
