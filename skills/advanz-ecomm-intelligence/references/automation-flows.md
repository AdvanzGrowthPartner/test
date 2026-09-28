# Automation & Flows — Email, SMS, WhatsApp, Tools

## The 5 Essential Email Flows (priority order)

### 1. Abandoned Cart (RPR $3.65, top 10% $28.89)
Email 1 (2-4h): reminder, product image, CTA. NO discount. 30-40% convert here alone.
SMS 1 (6-12h): "Tu [producto] te está esperando. [link]". Opt-in required.
Email 2 (24h): social proof — reviews of abandoned product + urgency + guarantee.
Email 3 (48h): incentive — 10% off or free shipping. ONLY for carts > threshold. Unique code + countdown.
SMS 2 (60-72h): last notice — discount expiring + direct checkout link with code applied.
Retargeting ad (12-24h): DPA dynamic showing abandoned product.
GOLDEN RULE: No discount in email 1. Reserve for email 3. Only for high-value carts.
Segmentation: high cart (full sequence + discount), low cart (2 emails only, no discount), new customer (more trust), returning (shorter, no discount), VIP (personal email from founder).

### 2. Welcome Series (RPR $2.65, top 10% $21.18)
Email 1 (immediate): promised discount + value prop + CTA to hero product. Open rate 45-55%. DO NOT waste on generic "thanks for subscribing".
Email 2 (day 2): brand story, values, "why we exist". Humanize.
Email 3 (day 4): social proof — best reviews with photos. "What others say."
Email 4 (day 6): educational — how to use product, guide, routine. Value without selling.
Email 5 (day 8): urgency — discount expiring. Countdown. CTA to hero or bundle.

### 3. Post-Purchase (60%+ open rate)
Day 0: branded order confirmation (not Shopify default). Tracking + estimated delivery.
Day 3: usage guide — how to use product correctly. Video/photos. KEY for results and good reviews.
Day 7: request review with photo. Incentive: 10% off or loyalty points. Direct link.
Day 14: cross-sell — "People who bought X also love Y." Complementary product with result logic.

### 4. Browse Abandonment (RPR $1.07)
Email 1 (4-6h): "Something caught your eye?" + product viewed + 2-3 similar recommendations.
Email 2 (24h): testimonial of that product + optional soft incentive (free shipping, not discount).
Suppression: max 1 browse email per 3-5 days per person. Exclude anyone in abandoned cart flow.

### 5. Win-back (RPR $0.84)
Timing varies by niche repurchase cycle:
Supplements: start day 50 (cycle 30d). Skincare: day 75 (cycle 60d). Pets: day 50 (cycle 30-45d). Sportswear: day 120 (cycle 90-180d).
Email 1: "We miss you" + bestsellers + what's new. No discount.
Email 2 (15 days later): exclusive 15-20% off or free shipping. Urgency.
Email 3 (15 days later): last chance, best offer. If no open after 3 emails → move to inactive list. Protect deliverability.

## SMS Strategy
Abandoned cart: YES (12h + 72h). Welcome: optional (only if explicit SMS opt-in). Browse abandonment: NO (too cold, feels invasive). Post-purchase review reminder: optional (day 7 if no email open). Win-back with discount: YES.
SMS open rate: 90%+. But personal — 1 bad SMS = block forever.

## WhatsApp Commerce (Critical for LATAM)

### 3 Modes
1. Reactive support: WA button in header + PDP. Min response <5 min. Always active.
2. Proactive sales (conversational commerce): Click-to-WA Ads for high-consideration products (>$40, needs advice). Script: discover need (2-3 questions) → recommend 1 product → direct checkout link. CVR benchmark: 15-30%.
3. Automated flows + broadcast: API + CRM. Pre-approved templates. Abandoned cart, confirmation, tracking, post-delivery, reactivation, back-in-stock.

### Broadcast Rules
Max 2 promo broadcasts/month. Block rate >2% = too much/irrelevant. Best: product launches (early access), back-in-stock, exclusive WA-only promos, weekly value tips (1/week max).

### Click-to-WA Ads
Works for: >$40, personalization needed (supplement advice, skin type, sizing, pet breed), first purchase with high distrust.
Does NOT work for: impulse/low-ticket, products that buy in 30 sec on PDP.
Response time: <5 min critical. >15 min = conversion drops dramatically.

## Automation Tools Stack
Klaviyo: email/SMS flows, segmentation, analytics. Native Shopify integration. The standard for ecomm.
GHL (GoHighLevel): CRM, landing pages, WhatsApp, pipeline, email, forms. All-in-one for agencies.
n8n: orchestration between systems. Webhooks, workflows. Self-hosted (free) or cloud. Shopify event → n8n → WhatsApp/GHL/Klaviyo.
Zapier/Make: simpler integrations when n8n is overkill.
Key automations to build: new subscriber → welcome flow, abandoned cart → multi-channel recovery, purchase → post-purchase sequence, NPS 0-6 → CX alert, review 5★ → referral invite, 60d no purchase → win-back trigger.

## Review Capture Flow
Day 3: confirm delivery (catch problems early). Day 5: NPS 1-click (segment promoters/detractors). Day 7: request review with photo (incentive: 10% off or points). Day 10: SMS reminder. Day 14: NPS 9-10 → referral invite. NPS 0-6 → internal CX alert for personal contact.
