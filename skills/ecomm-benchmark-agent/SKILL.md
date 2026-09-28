---
name: ecomm-benchmark-agent
description: "Genera benchmarks digitales completos de competencia para ecommerce DTC/B2C. Usa esta skill SIEMPRE que el usuario pida: benchmark de competidores, análisis de competencia ecommerce, auditoría digital de marcas, comparar mi tienda vs competidores, investigar competidores ecommerce, benchmark digital, análisis de madurez digital, mapear el ecosistema digital de un segmento, detectar oportunidades vs competencia, o cualquier variante de 'quiero entender cómo vende mi competencia online'. También actívala cuando el usuario mencione: funnel de competencia, stack tecnológico de competidores, automatizaciones de competidores, SEO/AIO competitivo, presencia en redes de competidores, ads de competidores, social proof competitivo, o 'hazme un benchmark como el de AmazingCare'. Funciona para cualquier vertical ecommerce: suplementos, skincare, mascotas, moda, alimentos funcionales, wellness, deportes, hogar. SOLO ecommerce — NO usar para B2B, SaaS ni servicios."
---

# Ecommerce Benchmark Agent — Advanz

## Propósito

Generar un benchmark digital completo y accionable que permita entender en profundidad cómo cada competidor vende online, qué tecnología usa, dónde invierte, qué automatiza, cómo posiciona su marca, y cuáles son las brechas que el cliente puede explotar.

El output es un documento DOCX profesional con identidad Advanz, listo para entregar al cliente.

## Referencia obligatoria antes de generar

| Sección del benchmark | Archivo de referencia |
|---|---|
| Estructura general, formato, scoring | `references/framework.md` |
| Análisis de competidores: web, stack, plataformas | `references/competitor-deep-dive.md` |
| SEO, AIO, contenido, indexación | `references/seo-aio-analysis.md` |
| Funnels: tentativo actual y funnel ideal | `references/funnel-mapping.md` |
| Automatizaciones y flows | `references/automations-audit.md` |
| Ads, pauta digital, Meta Library, Google Ads | `references/ads-intelligence.md` |
| Social proof, reviews, UGC, confianza | `references/social-proof-trust.md` |
| Oportunidades y plan de acción | `references/opportunities-playbook.md` |

**Lee SIEMPRE `references/framework.md` primero.** Para benchmarks completos, lee TODOS los archivos. Para análisis parciales (solo SEO, solo ads, solo funnel), lee framework + el archivo específico.

## Flujo de ejecución

1. **Captura de contexto** — Identifica: marca cliente, categoría/vertical, mercado geográfico, competidores conocidos. Si el usuario no los da, pregunta.
2. **Investigación** — Usa web search para cada competidor: sitio web, redes sociales, Meta Ad Library, Google Ads Transparency, marketplaces, retailers. Busca JSON-LD, rich snippets, metadata.
3. **Análisis por sección** — Sigue la estructura de `references/framework.md` sección por sección.
4. **Scoring** — Aplica la matriz de madurez digital (14 dimensiones, escala 1-5, total /70).
5. **Oportunidades** — Cruza brechas del cliente vs. benchmark líder. Prioriza por impacto × velocidad de ejecución.
6. **Generación** — Produce el documento DOCX con la skill `docx` aplicando el diseño Advanz.

## Principios

- **Datos sobre opinión** — Cada claim debe tener evidencia observable (URL, screenshot lógico, dato indexable). Si no se puede confirmar, marcar como "⚠️ Por validar".
- **Lo que no está indexado no existe** — Si un competidor tiene algo offline pero no digital, eso es un hallazgo estratégico, no un gap de investigación.
- **Benchmark = accionable** — Cada sección debe terminar con implicaciones concretas para el cliente.
- **Español neutro LATAM** — Todo el output en español neutro. Sin modismos españoles.
- **100% ecommerce** — Toda la óptica es de venta online directa (DTC), marketplaces o retail ecommerce. No servicios, no B2B.

## Identidad visual Advanz en DOCX

- Font: Poppins (títulos) + Inter o sistema (cuerpo)
- Colores: fondo oscuro conceptual (#1A1A2E o similar), acentos purple-to-cyan (#C15DFF → #00DDFC)
- Tablas: bordes sutiles, header row con fondo gradient
- Badges: 🔝 para benchmark líder, ⚠️ para alertas, ✅ para confirmado, ★ para la marca cliente
- Gráficos: radar chart de madurez, bar chart de scores

## Notas de uso

- Si el usuario dice "hazme un benchmark de [marca]", interpretar como benchmark completo de su categoría: la marca + 3-5 competidores.
- Si el usuario dice "analiza a [competidor]", hacer un deep dive de ese competidor específico usando la estructura de `references/competitor-deep-dive.md`.
- Si el usuario pide "actualizar el benchmark de [cliente]", buscar en conversaciones previas el benchmark anterior y actualizarlo.
