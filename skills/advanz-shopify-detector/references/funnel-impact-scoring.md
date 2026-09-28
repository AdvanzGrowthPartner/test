# Funnel Impact Scoring — Cómo decidir si una app aporta o sobra

Esta referencia define el framework de scoring por app dentro del funnel. El objetivo: poder decir con base "esta app **aporta** / esta **sobra**" para cualquier app detectada, sin tener que recordar 80+ apps de memoria.

---

## Las 5 preguntas que definen si una app aporta

Para cada app detectada en una tienda, este skill responde estas 5 preguntas. La respuesta combinada da el veredicto.

### Pregunta 1 — ¿Qué capa del Growth Engine cubre?
Mapear cada app a 1-2 capas del framework Advanz:

| Capa | Apps típicas |
|---|---|
| **Foundations** | Theme, GDPR, Markets, Page Builder |
| **Offer** | Bundles, Upsells, Quantity tiers, Page Builder |
| **Validation** | Reviews/UGC, Video Commerce, Trust badges |
| **Acquisition** | Pixel/CAPI, Attribution/CDP, Affiliate |
| **Workflows** | Email, SMS, Popups, Push |
| **Retention** | Subscriptions, Loyalty, Bundles |
| **Feedback** | Heatmaps, A/B testing, Surveys |
| **Systems** | Chat/Helpdesk, Shipping/Tracking, Search |

Una app puede cubrir 2 capas (ej: Klaviyo = Workflows + Retention via flows). Una app que NO mapea a ninguna capa = sospechosa de overhead.

### Pregunta 2 — ¿La capacity está SIENDO USADA?
La detección sin validación de uso miente. Por cada app, validar con shadow buyer:

| App | Cómo validar uso real |
|---|---|
| Reviews | `data-number-of-reviews` > 0 + `count` reviews del producto |
| Subscriptions | PDP expone subscribe & save visible al usuario |
| Email | Klaviyo form visible / triggered (popup home, footer) |
| Bundles | PDP muestra opciones de bundle / pack-as-product visible |
| Upsell post-cart | Cart drawer/page muestra recomendaciones |
| Loyalty | Widget visible al user / botón cuenta de puntos |
| Chat | Widget de chat carga visible en bottom-right |
| GWP auto | Cart muestra gift item después de cumplir threshold |

Si una app aparece en HTML pero **NO se valida uso en shadow buyer** → reportar como "instalada pero no expuesta" (anti-pattern A1).

### Pregunta 3 — ¿Coincide con el tier de revenue del cliente?
Tabla cruzada de apps por tier:

| App | Starter (<$10k) | Mid ($10-50k) | Growth ($50-200k) | Premium ($200k-1M) | Plus (>$1M) |
|---|---|---|---|---|---|
| Klaviyo free | ✅ | ✅ | ↑ paid | paid | paid |
| Judge.me free | ✅ | ↑ Awesome | Awesome | ↑ Okendo | Okendo |
| Loox | overkill | ✅ | ✅ | ↑ Okendo | Okendo |
| Okendo | NO | NO | borderline | ✅ | ✅ |
| Shopify Subs native | ✅ | ✅ | ✅ | borderline | NO |
| Recharge | NO | NO | borderline | ✅ | ✅ |
| Skio | NO | NO | NO | ↑ premium | ✅ |
| PageFly | borderline | ✅ | borderline | NO (custom theme) | NO |
| Rebuy | NO | NO | NO | ✅ | ✅ |
| LoyaltyLion | NO | NO | NO | ✅ | ✅ |
| Attentive SMS | NO | NO | NO | borderline US | ✅ US |
| Elevar | NO | NO | si ads >$10k | ✅ | ✅ |

**Si app está en columna NO**: anti-pattern A3 (sobre-stackeado).
**Si app SHOULD estar pero no aparece**: anti-pattern A4 (sub-stackeado).

### Pregunta 4 — ¿Es reemplazable con menos costo?
Para cada app paga, validar 3 alternativas:

1. **Native Shopify lo cubre?** → recomendar migrar si tier <Premium
2. **Free tier de otra app lo cubre?** → ej. Tidio free vs Crisp paid
3. **Liquid + JS custom lo cubre?** → ej. quantity tier app reemplazable

Tier de reemplazo:
- Replicabilidad="Liquid nativo posible" → cliente con dev puede ahorrar 100%
- Replicabilidad="App alternativa free" → ahorro inmediato si features no críticas
- Replicabilidad="Otra app similar más barata" → ahorro de 30-60%
- Replicabilidad="No reemplazable" → mantener si tier lo justifica
- Replicabilidad="Native Shopify cubre" → migrar inmediatamente si tier <Premium

### Pregunta 5 — ¿Cuál es su Score ROI (1-5)?
Definido en Notion DB campo `Score ROI (1-5)`. Heurística:

- **5**: imprescindible, sin sustituto bueno, alto impacto medible (Klaviyo, Clarity, Elevar para ads>$10k)
- **4**: alto impacto pero hay alternativas decentes (Loox, Judge.me, ReConvert)
- **3**: nice-to-have, impacto medio, justificable solo en tiers altos (Cooee, Reviews.io)
- **2**: vendor pequeño o overhead respecto a free alternatives (Hotjar si Clarity ya está, Bucks)
- **1**: deprecated, redundante, o anti-pattern (PageFly cuando Advanz va a hacer migración)

---

## Output del scoring para una app

Por cada app detectada, generar este bloque conciso:

```
[APP NAME] — Capa: [stage]
✅ Uso confirmado: [sí/no - evidencia del shadow buyer]
✅ Tier match: [matches client tier / over-engineered / under-tier]
✅ Reemplazable: [sí con X / no justificado]
✅ Score ROI: [N/5]

Veredicto: MANTENER / DEPRECAR / REEMPLAZAR / ACTIVAR
Acción: [acción concreta en 1 oración]
```

---

## Ejemplos de scoring aplicado

### Ejemplo 1 — Klaviyo en cliente AmazingCare ($30k/mo estimado)

```
Klaviyo — Capa: Workflows + Retention
✅ Uso confirmado: SI - hay flows activos + popup home
✅ Tier match: Mid tier ($10-50k) ✓ paid tier $20-50/mo
✅ Reemplazable: NO en este caso, ya está al máximo en alternativas
✅ Score ROI: 5/5

Veredicto: MANTENER
Acción: Validar que flows post-purchase + abandoned cart estén activos
```

### Ejemplo 2 — PageFly en cliente The Good Vegan (Chile <$10k/mo estimado)

```
PageFly Premium ($49/mo) — Capa: Foundations + Offer
✅ Uso confirmado: SI - 29 assets cargados, PDP customizada
⚠️ Tier match: OVER-ENGINEERED para Starter (<$10k/mo)
⚠️ Performance cost: 29+ scripts inflan mobile loading
✅ Reemplazable: SÍ con Liquid nativo (Advanz puede armar sections en 12-16h)

Veredicto: REEMPLAZAR
Acción: Migrar layout actual a OS 2.0 sections nativas, deprecar PageFly, ahorro $49/mo + mejor performance mobile
```

### Ejemplo 3 — Judge.me en cliente GoHard (data-number-of-reviews=0)

```
Judge.me — Capa: Validation
❌ Uso confirmado: NO - 0 reviews después de instalación
✅ Tier match: Free tier OK
✅ Reemplazable: alternativa free Loox no es necesaria si Judge.me se activa bien
✅ Score ROI potencial: 4/5 (actual 0/5)

Veredicto: ACTIVAR (no deprecar)
Acción: Configurar Klaviyo flow 'pedir review' post-delivery + Judge.me campaign. Esfuerzo 2h, valor +30-60 reviews/mes
```
