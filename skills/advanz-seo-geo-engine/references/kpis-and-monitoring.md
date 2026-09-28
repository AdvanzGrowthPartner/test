# KPIs y Monitoring — Tracking Dual SEO + GEO

Documento maestro para definir qué medir, cómo, con qué frecuencia.

---

## KPIs SEO clásicos

### Visibilidad
- Posición media (Search Console)
- Keywords en top 3 / top 10 / top 20
- Share of voice vs competidores (Ahrefs/Semrush)
- Featured snippets ganados

### Tráfico
- Sesiones orgánicas (GA4)
- Páginas vistas orgánicas
- Tráfico orgánico por landing
- Tráfico orgánico por dispositivo
- Tráfico orgánico por país

### Engagement
- Engagement rate orgánico
- Pages per session
- Avg session duration
- Bounce rate (engagement complementario)

### Conversión
- Conversiones orgánicas (GA4)
- Revenue orgánico
- AOV orgánico
- CAC orgánico (revenue / esfuerzo + inversión)

### Backlinks
- Referring domains nuevos/mes
- Quality score promedio (DR/DA)
- Diversidad de anchors
- Backlinks tóxicos identificados

---

## KPIs GEO nuevos

### AI Citation Score
Test mensual manual o automático de 20-30 queries en cada plataforma:
- ChatGPT (con web search activado y desactivado)
- Claude (con web search activado y desactivado)
- Gemini
- Perplexity

Para cada query, registrar:
- ¿La marca aparece? Sí/No
- ¿En qué posición? (1ra mención / mención secundaria / no aparece)
- ¿Con link a sitio propio?
- ¿Con qué contexto? (positivo / neutral / negativo)
- ¿Junto a qué competidores?

### Share of model
Por categoría, calcular:
- # queries donde aparece la marca / # queries totales testeadas
- # menciones primarias / # menciones totales
- Posición media en respuesta de LLM

### Branded search volume
- Volumen mensual de búsquedas de marca (Ahrefs/Semrush)
- Crecimiento mes a mes
- Correlación con citas LLM

### Menciones cross-canal
- Menciones en medios tier 1-2 logradas
- Menciones en foros (Reddit, Quora)
- Menciones en podcasts
- UGC publicado por embajadores

---

## Stack de herramientas recomendado

### Mínimo viable
- Google Search Console (free)
- Bing Webmaster (free)
- GA4 (free)
- Ahrefs o Semrush ($)
- Looker Studio dashboard (free)
- Notion para documentación
- Test manual mensual de LLMs (free)

### Standard pro
- Todo lo anterior +
- Otterly o Peec.ai ($)
- Hotjar o Clarity (free/$)
- Screaming Frog SEO Spider ($)

### Enterprise
- Todo lo anterior +
- Profound ($$)
- Ahrefs + Semrush (ambos para validar data)
- Custom alerts y dashboards
- Análisis de logs server-side

---

## Cadencia de reporting

### Diaria (automática)
- Alertas Search Console (errores cobertura, drops bruscos)
- Uptime monitoring
- Core Web Vitals alerts

### Semanal (strategist)
- Top 20 KW evolución
- Nuevos backlinks
- Conversiones orgánicas vs semana anterior
- Errores 404 detectados

### Mensual (cliente)
- AI Citation Score actualizado
- Share of voice y share of model
- Performance de contenido publicado
- Roadmap update
- Insights accionables (no data dump)
- Próximos pasos del siguiente mes

### Trimestral (estratégica)
- Auditoría técnica completa
- Benchmark vs competidores
- Ajuste de roadmap
- ROI total del trimestre
- Decisiones de inversión próximo trimestre

---

## Template de reporte mensual cliente

Estructura estándar en Notion (workspace `advanzgrowthpartner`):

```markdown
# Reporte SEO/GEO — [Cliente] — [Mes]

## Resumen ejecutivo
[2-3 párrafos: qué pasó, qué movió, qué viene]

## Métricas SEO
- Sesiones orgánicas: X (+ Y% vs mes anterior)
- Conversiones orgánicas: X
- Revenue orgánico: $X CLP
- Keywords en top 10: X (+ Y nuevas)
- Featured snippets: X

## Métricas GEO
- AI Citation Score: X / 30 queries
- Share of model en categoría: X%
- Branded search volume: X (+ Y%)
- Menciones nuevas: X

## Top 5 wins del mes
1. [Win 1 con métrica]
2. ...

## Trabajo realizado
- Contenido publicado: [lista con links]
- Optimizaciones técnicas: [lista]
- Outreach realizado: [lista]
- Schema implementado: [lista]

## Insights y aprendizajes
[Qué descubrimos que vale la pena documentar]

## Próximo mes
- Foco principal
- Deliverables
- Decisiones que necesitamos del cliente
```

---

## Dashboards Looker Studio template

Bloques esenciales:

1. **Header con resumen mes** (4 métricas clave en cards grandes)
2. **Sesiones orgánicas — line chart 12 meses**
3. **Top 20 keywords con posición media**
4. **Conversiones orgánicas por landing**
5. **Backlinks acumulados**
6. **AI Citation Score (manual upload mensual)**
7. **Share of voice vs competidores**
8. **Top contenido por sesiones / engagement**

Plantilla compartible en Drive del workspace para clonar por cliente.

---

## Señales de alerta (drop monitoring)

Setear alertas automáticas cuando:

- Tráfico orgánico cae >20% semana vs semana
- Posición media cae >5 posiciones en KW principal
- AI Citation Score cae >15% mes vs mes
- Errores 404 aumentan >30%
- Core Web Vitals salen de verde
- Conversión orgánica cae >25%

Cada alerta = investigación inmediata, no esperar al reporte mensual.
