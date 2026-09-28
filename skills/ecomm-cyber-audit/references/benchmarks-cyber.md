# Benchmarks — cómo juzgar la performance del cyber

**El benchmark real es el propio cliente, no la industria.** Dos tiendas en la misma vertical tienen márgenes, marca, lista y madurez distintas. Comparar el ROAS de cyber de Amazing Care contra un "promedio de suplementos" no dice nada accionable. Comparar contra **los últimos 30 días del propio cliente** lo dice todo.

Por eso este skill juzga el cyber como **lift sobre baseline**, no contra números externos.

---

## Paso 1 — Construir el baseline del cliente (en la fase Pre)

Sacar de Shopify (`run-analytics-query`) los últimos 30 días pre-evento:
- Ventas diarias promedio
- CVR promedio
- AOV promedio
- Sesiones diarias promedio
- % revenue owned (email/SMS)

Y de Meta + Dashbo:
- ROAS promedio por canal
- MER blended promedio
- CPM / CPC promedio (para detectar la inflación de subasta del cyber)

Guardar este baseline. Es la vara contra la que se mide cada pulse.

---

## Paso 2 — Juzgar el evento como lift

Durante y después del evento, cada métrica se lee como múltiplo del baseline:

| Métrica | Cómo leerla en cyber |
|---------|----------------------|
| **Ventas diarias** | Debe multiplicar el baseline varias veces. Un cyber sano hace en 3 días lo de varias semanas normales. Si apenas iguala un día normal, algo falla (oferta débil, tracking roto, o no se comunicó). |
| **CVR** | Suele subir vs baseline (intención de compra alta). Si el CVR **cae** bajo baseline con más tráfico → restricción Tienda/Oferta. |
| **AOV** | Puede bajar (descuentos) o subir (bundles/umbral). Si cae fuerte sin que suba el volumen suficiente → revisar canasta. |
| **CPM/CPC** | Sube en cyber (todos pujan). Esperarlo. Lo que importa es que el ROAS/MER aguante pese al CPM más caro. |
| **MER blended** | El número rey. Debe sostenerse cerca o sobre el target del cliente pese al CPM inflado. Si el MER se desploma, la adquisición dejó de ser rentable → mover a owned/retención. |
| **% revenue owned** | En cyber el email/SMS suele aportar una porción relevante. Si es marginal, hay palanca sin explotar (lista chica o cadencia floja). |

---

## Referencias directionales (Chile / LATAM) — usar con cuidado

Son rangos orientativos, **no targets**. El target siempre es el lift sobre el propio baseline.

- **Macro:** CyberDay Chile 2025 superó US$520M en ventas totales (+4,6% YoY, fuente CCS). El evento es un punto de inflexión anual de ingresos — un DTC bien preparado concentra una parte desproporcionada de su mes (o trimestre) en estos 3 días.
- **Móvil:** la mayoría del tráfico cyber en Chile es móvil. El CVR y la velocidad móvil pesan más que en un día normal.
- **Despacho:** en Chile el envío gratis frecuentemente mueve la conversión más que un % extra de descuento (el costo de despacho en RM puede superar los $10.000). Palanca clave de canasta.
- **CPM:** esperar inflación de subasta durante los 3 días. No interpretar CPM alto como fracaso si el MER aguanta.

> No inventar ROAS/CVR "promedio de industria" con falsa precisión. Si Patricio pide un benchmark externo puntual y no hay baseline propio, decir que el dato confiable es el baseline del cliente y, si hace falta contexto de mercado, buscarlo con `ecomm-benchmark-agent` o búsqueda web fechada — no rellenar de memoria.

---

## Paso 3 — Debrief Post (qué medir al cierre)

1. **Revenue total del evento vs baseline** (cuántas semanas normales equivalió).
2. **Mix de canal:** qué aportó Meta, Google, TikTok, email — por revenue real (atribución Shopify), no por ROAS de plataforma.
3. **MER blended del evento** vs MER baseline.
4. **Top SKUs** y si hubo quiebres de stock (revenue perdido).
5. **Qué restricción dominó cada fase** (de los pulses) — el aprendizaje operativo.
6. **Cohorte capturado:** cuántos compradores nuevos, cuántos entraron a flows de retención. Esto define el retorno real del cyber (LTV), que se cobra en los meses siguientes.

El debrief no es un reporte bonito: es el insumo que alimenta las etapas Acquisition/Retention/Feedback del Growth Engine del cliente para el resto del año.
