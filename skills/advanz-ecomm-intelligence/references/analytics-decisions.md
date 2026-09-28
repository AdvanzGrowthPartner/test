# Analytics & Decision Frameworks

## The 7 Vital Metrics
1. **CVR** (Sessions → Purchases): efficiency of the store. Weekly. Target: 2.5-3%+.
2. **AOV** (Revenue / Orders): ticket size. Weekly. Target: varies by niche, optimize with bundles/upsell.
3. **RPV** (CVR × AOV): revenue per visitor. THE north star metric. Weekly. Shows combined efficiency.
4. **ROAS** (Ad revenue / Ad spend): per-channel efficiency. Weekly. Must be above break-even.
5. **MER** (Total revenue / Total ad spend, all channels): system efficiency. Weekly. Target: 3-5x healthy.
6. **CAC** (Total marketing spend / New customers): cost to acquire. Monthly. Must be < AOV × margin.
7. **LTV** (Avg revenue per customer in 12m): customer value. Monthly. Must be >3× CAC.

## Key Formulas
```
Break-even ROAS = 1 / Gross Margin
  Example: 60% margin → BE ROAS = 1.67x

CPA Maximum = AOV × Gross Margin
  Example: $74 AOV × 60% = $44.40 max CPA

RPV = CVR × AOV
  Example: 2.5% × $74 = $1.85 per visitor

MER = Total Revenue / Total Ad Spend (all channels)
  Example: $50K revenue / $12K spend = 4.17x MER

LTV:CAC Ratio
  <1:1 = losing money per customer
  1-2:1 = surviving
  3:1 = healthy, sustainable
  5:1+ = scale aggressively
```

## Diagnostic Framework — When Metrics Are Bad

| Symptom | Where's the problem? | Action |
|---------|---------------------|--------|
| CTR low (<1%) | CREATIVE — hook doesn't stop scroll | New hook/creative. Don't touch audience. |
| CTR high (>2%) + CVR low (<1%) | PDP — ad promises what page doesn't deliver | Fix PDP: images, copy, trust, reviews. Ads are fine. |
| CPC high (>$2) | AUDIENCE saturated or creative irrelevant | Go broader or new creative angle. |
| CPA rising week over week | Creative FATIGUE (frequency >3) | Rotate creatives. Add 3 new, pause worst 2. |
| ROAS low but CPA acceptable | AOV too low — acquiring cheap but they buy little | Bundles, upsells, free shipping threshold, BNPL. |
| Everything ok but revenue flat | Audience CEILING — no more people to reach | Open new channel (Google, organic), activate retention. |
| CVR high but AOV low | Lots of small purchases | Bundles, minimum for free shipping, cross-sell in cart. |
| CVR low across all traffic sources | Store-wide trust/UX problem | Audit checkout, trust signals, speed, mobile UX. |
| MER < 2x | Combined system unprofitable | Review channel by channel. Pause worst performer. |
| LTV:CAC < 2:1 | Acquiring expensive + not retaining | Invest in retention (E7) before scaling acquisition. |
| Repeat rate < 15% | Leaky bucket mode | Fix post-purchase flows, cross-sell, win-back BEFORE scaling ads. |
| Email revenue < 15% of total | Flows broken or absent | Priority: abandoned cart + welcome. Covers 70% of impact. |

## Weekly Dashboard Template
Track every Monday: Revenue, Orders, AOV, CVR, RPV, Sessions, Meta spend + ROAS, Google spend + ROAS, MER, Email revenue %. Compare vs prior week with Δ%.

## Monthly Dashboard Template
Track end of month: CAC, LTV estimated (12m), LTV:CAC ratio, Repeat purchase rate, % revenue from recurring customers, Active subscribers, NPS.

## Decision Rules
**When to scale ads:** CPA below max for 5+ consecutive days, ROAS above break-even, CVR stable, creative not fatigued.
**When to pause ads:** CPA above max for 3+ days, ROAS below break-even, frequency >4 with declining CTR.
**When to fix store before ads:** CVR <1.5%, bounce rate >65%, checkout abandonment >80%.
**When to prioritize retention over acquisition:** Repeat rate <15%, LTV:CAC <2:1, revenue from recurrents <20%.
**When to add a channel:** Current channel at ceiling (scaling budget doesn't increase revenue proportionally). Typically: start Meta → add Google → add organic → add TikTok.

## Attribution Reality
Meta claims first-touch/view-through. Google claims last-click. Both overcount. MER is the only honest unified metric.
Post-checkout survey "How did you find us?" gives real attribution. GA4 often shows "direct" for what was actually word-of-mouth, podcast, or social.
Turn off Meta → if Google ROAS drops in 2-3 weeks, Meta was creating demand Google captured.
