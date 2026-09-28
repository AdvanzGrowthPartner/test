# Checklist Exhaustivo de Diagnóstico — 7 Capas

Lista operativa para auditar un cliente ecommerce DTC. Marca cada item como ✅ presente, ⚠️ parcial, ❌ ausente.

---

## Capa 1 — Técnico

### Performance
- [ ] LCP <2.5s mobile (CrUX, no Lighthouse)
- [ ] INP <200ms
- [ ] CLS <0.1
- [ ] Tamaño total página <2MB
- [ ] Imágenes en WebP/AVIF
- [ ] Fonts con font-display: swap
- [ ] JS no bloqueante

### Indexabilidad
- [ ] robots.txt accesible y correcto
- [ ] sitemap.xml enviado a GSC
- [ ] sitemap.xml enviado a Bing Webmaster
- [ ] Canonical correcto en cada tipo de página
- [ ] Sin páginas duplicadas indexadas
- [ ] Hreflang si aplica multiidioma
- [ ] Sin redirect chains
- [ ] Sin 404s en internal links

### Schema
- [ ] Organization en home
- [ ] Product + Offer en PDPs
- [ ] AggregateRating en PDPs
- [ ] FAQPage donde aplica
- [ ] BreadcrumbList en navegación
- [ ] Article en blog posts
- [ ] WebSite con SearchAction
- [ ] Validado en Schema Markup Validator
- [ ] Validado en Rich Results Test

### URLs
- [ ] Sin typos en slugs
- [ ] Estructura jerárquica clara
- [ ] Sin parámetros innecesarios
- [ ] Slugs en idioma del cliente (no inglés si es CL)

### Mobile
- [ ] Tap targets ≥44px
- [ ] Sin contenido oculto solo mobile
- [ ] Misma info en mobile que desktop
- [ ] No popups intrusivos

### GEO técnico
- [ ] llms.txt en raíz
- [ ] Contenido principal renderizado en SSR (no solo CSR)
- [ ] OpenGraph tags completos
- [ ] Twitter Card tags

---

## Capa 2 — Entidad de marca

- [ ] Wikidata Q-item creado
- [ ] Schema Organization en home con todos los campos
- [ ] sameAs apuntando a redes + marketplaces + Wikidata
- [ ] About page con narrativa estructurada
- [ ] Schema Person para fundador en about
- [ ] NAP consistente cross-canal (auditado)
- [ ] Google Business Profile activo
- [ ] GBP categoría exacta
- [ ] GBP posts semanales
- [ ] GBP Q&A respondida
- [ ] GBP reviews activas

---

## Capa 3 — Arquitectura de contenido

### Estructura
- [ ] Pillar comercial principal publicado
- [ ] Mínimo 5 soportes informacionales
- [ ] Mínimo 2 soportes comparativos
- [ ] Mínimo 3 soportes caso de uso
- [ ] PDPs enriquecidos (descripción completa, specs en HTML, FAQ)
- [ ] Colecciones con intro + outro
- [ ] Internal linking semántico denso

### Pattern dual SEO+GEO
- [ ] H2s con queries literales
- [ ] Respuestas directas en primera oración
- [ ] Listas/tablas para skim
- [ ] Citas o evidencia con autor/estudio
- [ ] Schema apropiado por tipo

### On-page
- [ ] Title único por página, 50-60 chars, con keyword
- [ ] Meta description única, 140-160 chars, con CTA
- [ ] H1 único por página, con keyword
- [ ] Jerarquía H1>H2>H3 respetada
- [ ] Alt text descriptivo en imágenes (no "image" o "imagen")
- [ ] Internal links con anchor varied
- [ ] Sin keyword stuffing

---

## Capa 4 — E-E-A-T

### Authors
- [ ] Cada blog post firmado por persona real
- [ ] Author box con foto y bio
- [ ] Credenciales explícitas
- [ ] Link a LinkedIn o web personal
- [ ] Schema Person

### YMYL (si aplica)
- [ ] Revisión médica/profesional en artículos YMYL
- [ ] "Revisado por Dr. X" + fecha
- [ ] Schema reviewedBy

### Autoridad
- [ ] Página "Expertos que recomiendan" pública
- [ ] Mínimo 5 perfiles con credenciales verificables
- [ ] Certificaciones visibles en footer
- [ ] Página dedicada a certificaciones con explicación
- [ ] Links a estudios científicos para claims (si aplica)

### Trust signals
- [ ] Reviews promedio visibles en cada PDP
- [ ] Total de clientes/reviews comunicado
- [ ] Años en mercado visible
- [ ] Garantía de devolución clara
- [ ] WhatsApp / teléfono / email accesible
- [ ] Política de privacidad y términos accesibles

---

## Capa 5 — Off-page

### Backlink profile
- [ ] DR/DA conocido (Ahrefs/Moz)
- [ ] Mínimo 30 referring domains de calidad
- [ ] Diversidad de anchor texts
- [ ] Sin backlinks tóxicos masivos
- [ ] Sin patrones de PBN

### Menciones tier 1-2
- [ ] Aparición en al menos 3 medios tier 1-2 últimos 12 meses
- [ ] Aparición en al menos 5 listicles externos top
- [ ] Aparición en al menos 2 podcasts del nicho

### Foros y comunidades
- [ ] Marca mencionada orgánicamente en Reddit/Quora del nicho
- [ ] Sin patrones de spam
- [ ] Discusión en grupos Facebook del nicho

### Marketplaces
- [ ] Reviews en Mercado Libre / Amazon / marketplaces locales
- [ ] AggregateRating sincronizado con sitio propio

### Embajadores
- [ ] Programa de embajadores activo
- [ ] Contenido generado por embajadores en sus canales
- [ ] UGC sincronizado al sitio propio

---

## Capa 6 — UX, CRO, comportamiento

### Search intent
- [ ] Cada landing matcheada al intent del query principal
- [ ] PDPs con producto above the fold
- [ ] Blog posts con respuesta above the fold
- [ ] Sin confusión informacional vs transaccional

### SERP CTR
- [ ] Title optimizado para click
- [ ] Meta description con CTA implícito
- [ ] Tests A/B en title/meta de top pages
- [ ] Rich snippets ganados (rating stars, FAQ, breadcrumb)

### PDP completeness
- [ ] Ingredientes/specs en HTML, no imagen
- [ ] Tabla comparativa
- [ ] FAQ 6-8 preguntas
- [ ] Reviews con foto
- [ ] Política devolución visible
- [ ] Envío y plazos claros

### Conversión
- [ ] CRO activo en PDPs
- [ ] Testing continuo
- [ ] Heatmaps / session recordings (Hotjar, Clarity)

---

## Capa 7 — Monitoring

### SEO clásico
- [ ] Google Search Console configurado
- [ ] Bing Webmaster configurado
- [ ] GA4 tracking orgánico segmentado
- [ ] Ahrefs/Semrush con KW tracking
- [ ] Looker Studio dashboard semanal

### GEO
- [ ] Plan de testing manual mensual de 20-30 queries
- [ ] Plataforma GEO activa (Profound/Otterly/Peec.ai)
- [ ] Branded search volume monitoreado
- [ ] Share of model calculado mensualmente

### Reporting
- [ ] Cliente recibe reporte mensual
- [ ] Métricas comunicadas en lenguaje de cliente
- [ ] Insights accionables, no solo data dump
- [ ] Roadmap actualizado trimestralmente

---

## Sistema de scoring rápido

Para output en widget:

- Capa con <50% items ✅ → score **rojo**
- Capa con 50-70% → score **amarillo**
- Capa con 70-90% → score **verde claro**
- Capa con >90% → score **verde**

Score total = promedio ponderado:
- Capa 1: peso 1.5
- Capa 2: peso 1.5
- Capa 3: peso 1.5
- Capa 4: peso 1.0
- Capa 5: peso 1.0
- Capa 6: peso 1.0
- Capa 7: peso 0.5

Score SEO = capas 1,3,5,6 ponderadas
Score GEO = capas 1,2,3,4,5 ponderadas
