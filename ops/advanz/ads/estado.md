# Advanz · OS Ads · Estado

> Paid media **propio** de Advanz (no clientes). Actualizado: 2026-10-19.

> **2026-10-21:** el tablero del área ahora es **Ads OS · Command** (https://claude.ai/artifact/FfZgya6fwoGvMNqcJ2kbjB), con las dos marcas. El dashboard anterior por marca queda congelado.

## Estado actual
- 🔴 **Canal detenido por decisión**, no por olvido (skill `advanz-acquisition-system`). Meta semanal: 0.
- Cuenta Meta **"Advanz Growth Partner"** `120273191181276` (BM `936238854582653`, CLP). Al 2026-09-28 estaba en **UNSETTLED**: tiene un pago pendiente y el MCP de Meta no la puede consultar.
- No hay campañas propias activas ni historial de campañas en los transcripts revisados. Todo el trabajo de ads de las sesiones legacy es para clientes (Amazing Care, Mason Care, nad).
- Aprendizaje histórico: **$450k CLP → 1 cierre**, empujando un lead magnet genérico de Cyber mientras el Diagnóstico Vivo quedaba escondido detrás (fecha sin confirmar).
- Tracking previsto para landers: Pixel + CAPI + GA4 en el stack `growth-engine-lander` (sin confirmar si está activo en advanz.cl).

## Artifact y datos del OS
- `os-data.json` publicado según el contrato del Command Center (`fuente: "os"`): 3 KPIs, 4 fugas (F01–F04), 4 accesos.
- Dashboard **Advanz · OS Ads**: https://claude.ai/artifact/EPTBn5enjm5DQ54usEhkQY (privado hasta que se comparta). Muestra KPIs y fugas; la tabla de accesos no se subió (el clasificador bloqueó esa subida) y queda solo en el JSON.
- Accesos probados el 2026-10-19: Meta Ads MCP conecta, pero la cuenta Advanz está UNSETTLED (`is_queryable=false`). Semrush responde, sin unidades de API. No hay conector para Google Ads, LinkedIn Ads ni GHL.

## Decisiones tomadas
- **(fecha sin confirmar, previa a 2026-09)** Se apagan los ads propios. Motivos: no hay presupuesto para sostener el aprendizaje, el mensaje no está validado en frío, y el outbound con Diagnóstico Vivo reemplaza el gasto a costo cero.
- **Condición de reactivación**: un nivel de dolor o tipo de contenido con tasa de respuesta consistente en outbound y orgánico. Ese ángulo validado es el que recibe presupuesto. "Ads amplifica, no descubre."
- **Regla**: nunca encender ads como solución a que otro canal no produce.

## Pendientes / próximos pasos
- [ ] Regularizar el pago pendiente de la cuenta Meta (UNSETTLED) para recuperar la lectura por MCP, aunque el canal siga apagado.
- [ ] Confirmar si existe cuenta de Google Ads propia de Advanz y su ID (no aparece en los transcripts).
- [ ] Revisar Pixel/CAPI en advanz.cl (GHL) y en los landers de Vercel antes de cualquier reactivación.
- [ ] Cuando growth marque un ángulo validado: plan de test chico (presupuesto, CPL y costo por llamada objetivo). Tiene que estar en PAUSED hasta tener OK.
- Falta levantar: historial de la campaña de $450k (fechas, objetivo, creativos, CPL) y presupuesto disponible.

## Fuentes
- `session_016wE9PpDN1DgP2VEWk9evA4`: Conexión de Meta a Claude (2026-09-28). Estado y IDs de cuentas.
- `session_016C6G8y2Z5UcGJTsPrdryGk`: Agente | Sistema de Ads (2026-09-07). Solo trabajo de clientes (playbook de escalado horizontal).
- `session_01D5MWLLVq8KnUJhXrkVdBoR`: Revisión sistema aprobación anuncios (2026-08-21). Cliente Amazing Care; lectura parcial.
- `session_013f2ikzQ9br78MUgmJY7o7J`: Copywriting Meta/Google (2026-08-21). Cliente Amazing Care.
- Skill `advanz-acquisition-system` → `references/canales.md` (estado 🔴 y condición de reactivación).
