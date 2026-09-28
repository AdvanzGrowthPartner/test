# Protocolo Manual de Testing GEO

Cómo testear mensualmente el AI Citation Score de un cliente Advanz.

---

## Frecuencia

Mensual, primer lunes de cada mes. Resultados van al reporte mensual del cliente.

---

## Setup de testing

Plataformas a testear (4):
1. **ChatGPT** — con web search activado, modo GPT-5
2. **Claude** — con web search activado
3. **Gemini** — modo default
4. **Perplexity** — modo default (Pro si está disponible)

Setup adicional recomendado:
- Cuenta limpia (modo incógnito / cuenta sin historial sesgado)
- VPN Chile (las respuestas pueden variar por geografía)
- Documentar fecha y hora exacta del test

---

## Queries a testear (template para vertical suplementos)

Queries genéricos categoria (12 queries):
1. "mejores electrolitos en Chile"
2. "mejores electrolitos sin azúcar Chile"
3. "electrolitos marca chilena"
4. "electrolitos para deporte Chile"
5. "electrolitos para resaca"
6. "electrolitos para ayuno intermitente"
7. "electrolitos veganos Chile"
8. "marcas de electrolitos chilenas vs internacionales"
9. "dónde comprar electrolitos en Santiago"
10. "electrolitos sin endulzantes artificiales"
11. "qué electrolitos comprar en Chile"
12. "electrolitos LMNT alternativa Chile"

Queries marca (8 queries):
13. "[marca] reseñas"
14. "[marca] vale la pena"
15. "[marca] vs [competidor 1]"
16. "[marca] vs [competidor 2]"
17. "ingredientes de [marca]"
18. "[marca] efectos secundarios"
19. "[marca] dónde comprar"
20. "es buena marca [marca]"

Queries comparativas (5 queries):
21. "[marca] vs LMNT"
22. "[marca] vs Gatorade"
23. "[marca] vs Powerade"
24. "[marca] vs sueros caseros"
25. "[marca] vs hidratación con agua"

Queries específicos de uso (5 queries):
26. "[producto] para triatlón"
27. "[producto] para ciclismo"
28. "[producto] en embarazo"
29. "[producto] para niños"
30. "[producto] para clima caluroso"

---

## Tabla de resultados

Por query y por plataforma, registrar en spreadsheet:

| Query | Plataforma | Aparece (S/N) | Posición | Con link | Contexto | Competidores citados | Notas |
|---|---|---|---|---|---|---|---|

Posición:
- **Primaria** — primera o segunda marca mencionada
- **Secundaria** — mencionada pero no destacada
- **Lista** — mencionada en lista de varias
- **No aparece**

Contexto:
- **Positivo** — recomendada activamente
- **Neutral** — mencionada sin opinión
- **Negativo** — mencionada con caveat negativo

---

## Cálculo de scores

### Score total (de 30 queries x 4 plataformas = 120 oportunidades)
```
Score = (apariciones primarias × 3 + secundarias × 2 + lista × 1) / (120 × 3)
```

### Share of model
```
Share of model = apariciones marca / apariciones totales en queries de categoría
```

### Citation rate por plataforma
```
ChatGPT rate = apariciones en ChatGPT / 30
Claude rate = apariciones en Claude / 30
...
```

---

## Análisis y acción

Después del test, generar 1-página de insights:

1. **Score evolución** vs mes anterior
2. **Plataforma con mejor performance** — y por qué
3. **Plataforma con peor performance** — y por qué
4. **Competidores que ganaron terreno** — y qué los está citando
5. **Queries críticos donde no aparecemos** — y plan de acción
6. **Quick wins detectados** — listicles donde aparecer, foros donde participar

---

## Trigger de alertas

Crear alerta cuando:
- Score total cae >15% vs mes anterior
- Aparece pérdida de posición primaria en queries de marca
- Competidor X nuevo aparece consistentemente
- Plataforma entera deja de citar la marca

Cada alerta = investigación inmediata + ajuste de roadmap.

---

## Documentación en Notion

Cada mes crear página en Notion del cliente:
- Workspace `advanzgrowthpartner`
- Path: `/{Cliente}/Reportes/{YYYY-MM} AI Citation Test`
- Estructura: tabla con resultados + insights + acciones

Linkear desde el reporte mensual general.

---

## Automatización futura

Si el cliente está en tier Pro o Enterprise, recomendar plataforma de monitoring automatizado:
- **Otterly** — más accesible, multi-LLM
- **Peec.ai** — base España, buena cobertura LATAM
- **Profound** — premium, US-centric

Estas plataformas automatizan el test diario/semanal y generan dashboards. El testing manual mensual sigue siendo útil como sanity check y para queries muy específicos del nicho.
