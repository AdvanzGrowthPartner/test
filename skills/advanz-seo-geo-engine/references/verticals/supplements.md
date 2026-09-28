# Vertical: Suplementos y Wellness

YMYL alto. E-E-A-T crítico. Categoría regulada por ISP en Chile.

## Particularidades

- **YMYL nivel alto** — Google y LLMs aplican filtros extra para contenido de salud
- **ISP / INTA** — Registros sanitarios obligatorios para venta legal
- **Claims regulados** — No se pueden hacer afirmaciones médicas sin respaldo
- **Categoría altamente competida** — LMNT, Liquid IV, Nuun a nivel global; en Chile GREZ, A Rueda, Chile Suplementos

## E-E-A-T no negociable

- Author boxes con nutricionistas, médicos del deporte, kinesiólogos colegiados
- Cada artículo YMYL revisado por profesional con RUT colegio
- Página "Expertos que recomiendan" obligatoria
- Certificaciones visibles: ISP, INTA, ISO si aplica, gluten-free, vegano

## Schema específico

- `Drug` o `DietarySupplement` puede aplicar (revisar con dev)
- Schema Product con `manufacturer`, `ingredient`, `recommendedIntake`
- `nutrition` con valores energéticos por porción
- `additionalProperty` para electrolitos por mg

## Pillar y cluster típico

**Pillar:** "Mejores [tipo de suplemento] en Chile 2026"

**Soportes informacionales:**
- "¿Qué es [ingrediente activo]?"
- "¿Para qué sirve [ingrediente]?"
- "¿Cuánto [ingrediente] necesito al día?"
- "Beneficios de [ingrediente] respaldados por ciencia"

**Soportes comparativos:**
- "Marca A vs Marca B vs Marca C"
- "Forma A vs Forma B (citrato vs gluconato, etc.)"
- "[Producto] vs alternativa natural"

**Soportes caso de uso:**
- "[Producto] para [actividad/condición]"
- "[Producto] durante embarazo / lactancia / niños"
- "[Producto] para ayuno intermitente / keto / vegano"
- "[Producto] para resaca / viajes / calor"

## Queries reales del comprador chileno

Categorías de query a testear en LLMs y Google:

1. "mejores [tipo de suplemento] en Chile"
2. "[tipo] sin azúcar Chile"
3. "[tipo] marca chilena"
4. "[tipo] para [caso de uso]"
5. "[ingrediente] dosis"
6. "[ingrediente] efectos secundarios"
7. "[marca] reseñas / opinión"
8. "[marca] dónde comprar"
9. "¿es seguro [producto] para [grupo]?"
10. "[marca A] vs [marca B]"

## Off-page específico

Medios chilenos prioritarios:
- Bienestar Paula (Copesa)
- El Mostrador Bienestar
- BioBio Salud
- La Tercera Bienestar
- A Rueda (deporte)
- Outdoors Chile
- Revista Sportlife

Podcasts del nicho:
- Podcast deportivos chilenos
- Médicos influencers
- Nutricionistas con canal propio

Embajadores con peso:
- Atletas con resultados (no influencers genéricos)
- Profesionales de la salud con audiencia
- Triatletas, ciclistas, runners reconocidos

## Distribución multicanal

Generalmente estos clientes ya venden en:
- Cruz Verde, Salcobrand, Ahumada (cadenas farmacéuticas)
- Jumbo, Tottus, Lider (supermercados)
- Mercado Libre, Falabella
- Spid (delivery rápido)

Esto es señal de autoridad de marca. Aprovecharlo en home (logos de distribuidores) y en schema (`sameAs` con perfiles en cada plataforma).

## Errores comunes en suplementos

- Tabla nutricional en imagen (debe ser HTML)
- Claims sin respaldo científico ("cura X", "previene Y")
- Sin author en blog posts
- Sin distinción clara entre uso recreativo y terapéutico
- Sin disclaimer médico
- Reviews dispersos en Mercado Libre sin sync al sitio propio
