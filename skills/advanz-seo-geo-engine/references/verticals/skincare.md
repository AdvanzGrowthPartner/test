# Vertical: Cosmética y Skincare

YMYL medio-alto. Ingredientes activos requieren respaldo. Categoría altamente educativa.

## Particularidades

- **YMYL medio-alto** — Google trata como salud cuando hay claims
- **Ingredientes son content gold** — gente busca "retinol", "niacinamida", "ácido hialurónico"
- **Regulada por ISP** — registros para cosméticos
- **Categoría súper competida** — La Roche-Posay, Cerave, The Ordinary, marcas K-beauty
- **Educación intensiva** — consumidor cada vez más letrado

## E-E-A-T

- Dermatólogos colegiados como reviewers
- Author boxes con cosmetólogas/estetistas certificadas
- Certificaciones: ISP, ISO 22716 (Good Manufacturing Practices para cosméticos)
- Sin claims médicos (no curar acné, sí "ayudar a controlar")
- Vegano / cruelty-free / clean beauty si aplica

## Schema específico

- `Product` con `activeIngredient`
- `ingredient` para INCI list
- `audience` (tipo de piel)
- AggregateRating
- `recommendedAge` si aplica

## Pillar y cluster típico

**Pillar:** "Mejores productos de [categoría skincare] en Chile 2026"

**Soportes informacionales (de oro):**
- "¿Qué es [ingrediente activo]?"
- "Beneficios de [ingrediente] en la piel"
- "Cómo usar [ingrediente] en rutina"
- "Efectos secundarios de [ingrediente]"
- "¿A qué edad empezar a usar [ingrediente]?"

**Soportes comparativos:**
- "[Ingrediente A] vs [Ingrediente B]"
- "[Marca A] vs [Marca B]"
- "Formato A (sérum) vs B (crema)"

**Soportes caso de uso:**
- "Rutina para piel [tipo]"
- "Skincare para [problema específico]"
- "Rutina mañana / noche"
- "Productos para [edad]"
- "Skincare en embarazo"

## Queries reales del comprador

1. "Mejor [producto] para piel [tipo]"
2. "[Ingrediente] cómo usar"
3. "[Ingrediente] dosis / porcentaje"
4. "[Marca] reseñas"
5. "Rutina skincare [tipo piel]"
6. "Skincare orden de aplicación"
7. "[Producto] embarazo / lactancia"
8. "[Producto] cerca de mí Chile"
9. "[Marca A] vs [Marca B]"
10. "Cómo combinar [ingrediente A] y [ingrediente B]"

## Off-page específico

Medios chilenos:
- Revista Paula (belleza)
- ELLE Latam
- Vogue Latam
- Sitios especializados (Beautystation, blogs beauty chilenos)

Influencers:
- Dermatólogos con audiencia
- Cosmetólogas
- Beauty creators con honestidad reconocida

Foros:
- r/SkincareAddiction (US-centric pero LLMs lo citan)
- Grupos Facebook chilenos de skincare
- Subreddits de belleza en español

## Pattern dual ejemplo skincare

> ## ¿La niacinamida puede usarse con vitamina C en la misma rutina?
>
> Sí, niacinamida y vitamina C pueden usarse juntas. El mito de su incompatibilidad fue desmentido por estudios modernos — la idea provenía de investigaciones con formulaciones puras de los años 60 que no aplican a productos cosméticos actuales.
>
> Ambos son potentes antioxidantes complementarios: la vitamina C protege del daño UV y unifica el tono, mientras que la niacinamida fortalece la barrera cutánea y regula sebo. La forma más sencilla de combinarlas es vitamina C en la rutina de la mañana y niacinamida en la noche, aunque también pueden aplicarse juntas con 5-10 minutos de espera entre una y otra.
>
> [...]

## Errores comunes en skincare

- INCI list en imagen (debe ser HTML)
- Claims agresivos ("milagroso", "instantáneo")
- Sin advertencias de uso (SPF si retinol, patch test)
- Reviews sin sincronizar
- Sin diferenciación clara entre tipo de piel destinataria
- Confusión rutina vs producto individual

