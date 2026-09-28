# Owner View — el Cyber Status para el dueño y el equipo

Hay dos salidas en este skill, de la misma lectura cruzada:

| Salida | Para quién | Pregunta que responde | Cadencia |
|--------|-----------|------------------------|----------|
| **Cyber Pulse** (en SKILL.md) | operador / quien está en los controles | "¿qué muevo ahora?" | cada 3-6h en peak |
| **Cyber Status** (este archivo) | dueño + status de equipo (Notion) | "¿cómo va el negocio, dónde se fuga, qué priorizamos?" | mañana / mediodía / noche, o por hito |

El dueño no quiere 5 gráficos. Quiere saber, en 60 segundos: **¿se rompió algo? ¿vamos bien? ¿cómo cerramos? ¿dónde se nos escapa plata? ¿qué hacemos ahora?** El Cyber Status responde exactamente eso.

---

## Cómo proyectar (lo más delicado)

Extrapolar lineal (horas transcurridas → regla de tres) **está mal**: las ventas de cyber no son uniformes. El Día 1 carga con la urgencia del lanzamiento, el Día 2 baja, el Día 3 repunta en la tarde con el "última oportunidad".

**Método correcto — curva de pacing:**

`Total proyectado = ventas acumuladas hasta ahora ÷ % esperado acumulado hasta esta hora`

**Mejor insumo:** la curva hora-a-hora del **propio cliente en su cyber anterior** (sacar de Shopify histórico del evento pasado). Si existe, usar esa. Es lo único que captura su patrón real de compra.

**Si no hay histórico propio**, usar esta curva direccional de CyberDay Chile (3 días, front-loaded), **declarándola como direccional**:
- **Día 1 ≈ 40%** del total (el día más fuerte; dentro del día: peak de lanzamiento en la mañana, baja al mediodía, segundo peak en la noche).
- **Día 2 ≈ 28%** (día valle).
- **Día 3 ≈ 32%** (repunte de last-chance en la tarde/noche).

**Reglas de honestidad de la proyección:**
- En las primeras horas el error es alto (±25-35%). **Entregar siempre un rango** (conservador / esperado / stretch), no un número puntual.
- La confianza sube a medida que avanza el evento. Decir explícitamente el nivel de confianza.
- Reportar la **trayectoria** (vamos adelante / en línea / detrás del ritmo esperado), que es más útil que el número absoluto temprano.

**Proyección por canal** — no todos se proyectan igual:
- **Paid (Meta/Google/TikTok):** escala con el presupuesto que *vas a desplegar*, no solo con el ritmo actual. Proyectar sobre el plan de spend de la fase.
- **Owned (email/SMS):** es pulsado, sube en cada envío (live → midpoint → last-chance). Tiene spikes futuros conocidos; proyectar incluyéndolos.
- **Orgánico/directo:** surfea la ola general del evento.

---

## Template del Cyber Status (formato Notion)

Markdown que pega limpio en Notion. Semáforo 🟢🟡🔴 arriba (patrón Radar CEO de Advanz). Escaneable en 60 segundos.

```markdown
# 🚦 Cyber Status — [Cliente] — Día [X] · [hora] hrs

> **Veredicto en una línea:** [todo en orden / hay 1 cosa que atender / hay algo roto, acción ya]

## 1. Semáforo de sistemas — ¿se rompió algo?
| Sistema | Estado | Nota |
|---------|--------|------|
| Tracking (pixel/CAPI/GA4) | 🟢/🟡/🔴 | |
| Sitio (velocidad/uptime) | 🟢/🟡/🔴 | |
| Stock de ganadores | 🟢/🟡/🔴 | |
| Pagos / checkout | 🟢/🟡/🔴 | |
| Entrega de ads | 🟢/🟡/🔴 | |

## 2. Cómo vamos (real hasta ahora)
- **Ventas:** $[X] · [N] órdenes · AOV $[Y] · CVR [Z]%
- **vs objetivo del evento:** [A]% cumplido · **vs día normal:** [×N]
- **MER blended:** [W]x (target [T]x)

## 3. Proyección de cierre del evento
- **Rango:** $[conservador] — **$[esperado]** — $[stretch]
- **Trayectoria:** [adelante / en línea / detrás] del ritmo esperado
- **Confianza:** [baja — primeras horas / media / alta]

## 4. Proyección por canal
| Canal | Aporta hoy | Proy. cierre | Lectura |
|-------|-----------|--------------|---------|
| Meta | $ / % | $ | [carga / flojo] |
| Google | $ / % | $ | |
| TikTok | $ / % | $ | |
| Email/Owned | $ / % | $ | |
| Orgánico/Directo | $ / % | $ | |

## 5. Ajustes de inversión / volumen
- **Escalar:** [campañas ganadoras, +X%]
- **Frenar:** [campañas quemadas]
- **Reasignar:** [de dónde → a dónde, y por qué]

## 6. Campañas quemadas / costos altos
| Campaña | Spend | ROAS | Estado | Acción |
|---------|-------|------|--------|--------|
| | | | quemada/fatiga/cara | pausar/rotar/bajar |

## 7. Fugas detectadas 💸
- **Presupuesto:** [spend en perdedores / SKUs sin stock / creativos fatigados]
- **Ventas:** [caída de CVR / abandono de checkout / demanda sin stock / gaps de tracking]

## 8. Cuidado con (próximas horas) ⚠️
- [Stock de SKU ganador acercándose a OOS]
- [Margen si se profundiza descuento]
- [Fatiga creativa esperada Día 2]
- [Inflación de CPM nocturna]

## 9. Nos faltó (gaps — para no repetir)
- [Lo que se nota que faltó del Pre: creativo, segmento, flow, etc.]

## 10. Prioridades AHORA (top 3)
- [ ] 1. [acción, dueño, plazo]
- [ ] 2.
- [ ] 3.

---
*Próxima lectura: [hora] · Fuentes: Shopify + Meta + Dashbo (TikTok/Google) + email*
```

---

## Cómo llenar cada bloque (mapeo a las preguntas del dueño)

| Pregunta del dueño | Bloque | De dónde sale |
|--------------------|--------|----------------|
| ¿Se rompió algo? | 1. Semáforo | Gate 0 + Meta `ads_get_errors` + Shopify checkout funnel + inventario |
| ¿Está todo ok? | 1 + 2 | Veredicto + números reales |
| Proyecciones iniciales | 3 | Curva de pacing (arriba) |
| Proyección de canales | 4 | Mix actual + plan de spend + spikes de email |
| Ajustes inversión/volumen | 5 | `optimization-rules.md` aplicado a la restricción |
| Campañas quemadas / caras | 6 | Meta `ads_get_ad_entities` + Dashbo por campaña |
| Qué nos faltó | 9 | Checklist Pre de `cyber-playbook.md` vs lo que se ve |
| Dónde tener cuidado | 8 | Stock, margen, fatiga, CPM — riesgos forward |
| Qué priorizar | 10 | Top 3 acciones por leverage (la #1 mueve la restricción) |
| Dónde se fuga plata/ventas | 7 | Cruce: spend en losers/OOS (presupuesto) + CVR/checkout/stock/tracking (ventas) |
| Resumen global Notion | todo | Este template completo |

**Regla:** si una fuente no respondió o el tracking falla, decirlo en el bloque correspondiente ("Meta no devolvió data") en vez de inventar. Un dueño que confía en un número inventado toma una decisión peor que uno que sabe que falta el dato.
