---
doc_id: SLD-BIO-009
biomarker_id: insulin
name_es: Insulina
name_en: Insulin
abbreviation: INS
sinonimos:
- Insulina
- Insulina basal
- Insulina en ayunas
- INS
- Insulin
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µUI/mL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M1-EM-A02
combine_with:
- glucose
- homa_ir
- triglycerides
- hdl_c
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Insulina

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M1-EM-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-009. INS. Categoría: Metabolismo. Tipo: analito medido (variable de entrada para HOMA-IR). Tier 2 — no rutinaria para todos.

## B. Definición

Hormona pancreática central en la regulación de la glucosa. Su medición en ayunas, combinada con la glucosa en ayunas, permite estimar resistencia a la insulina mediante el cálculo de HOMA-IR — su valor aislado sin glucosa concurrente tiene interpretación limitada.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero/plasma) · Método: inmunoensayo (quimioluminiscencia). Unidad: µUI/mL (alt: pmol/L). **Requiere ayuno de ≥8 horas**, igual que la glucosa con la que se combina para el cálculo de HOMA-IR — deben tomarse en la misma muestra/momento.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método — existe variabilidad interensayo documentada en la literatura de HOMA-IR (ver `homa_ir.md`), lo que hace que un valor "normal" de insulina dependa fuertemente de qué ensayo usa el laboratorio aliado.
- **Conclusión de evidencia (respuesta completa, no vacío):** no existe un umbral clínico único de insulina en ayunas aislada validado por guía de sociedad médica — el mismo problema de variabilidad interensayo documentado en `homa_ir.md` aplica aquí de forma directa, ya que la insulina es la variable de entrada más variable de ese índice. El enfoque clínicamente correcto y respaldado es usar el índice combinado (HOMA-IR) en vez de buscar un punto de corte de insulina aislada — esta es la conclusión final, no una brecha pendiente de resolver con más búsqueda.

## E. Interpretación

- **Elevada (en ayunas):** compatible con resistencia a la insulina — el páncreas compensa produciendo más insulina para mantener la glucosa normal; es frecuentemente el primer cambio detectable, antes de que la glucosa misma se altere.
- **Disminuida:** en el contexto de glucosa elevada, puede sugerir menor reserva de producción pancreática (más relevante en diabetes tipo 1 o diabetes tipo 2 avanzada) — requiere contexto clínico y, si corresponde, péptido C para diferenciar.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: estado de ayuno confirmado, IMC/circunferencia abdominal, antecedentes de síndrome de ovario poliquístico, antecedente familiar de diabetes tipo 2.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Glucosa (obligatorio, para calcular HOMA-IR), Triglicéridos y HDL-C (componentes del síndrome metabólico asociado a resistencia a la insulina).
- `pattern_examples`: insulina elevada + glucosa normal = resistencia a la insulina compensada (fase temprana); insulina elevada + glucosa también elevada = resistencia a la insulina con compensación pancreática insuficiente.
- `cannot_conclude`: diagnóstico de diabetes o prediabetes a partir de insulina — ese diagnóstico se basa en criterios de glucosa/HbA1c (ver `glucose.md`, `hba1c.md`), no en insulina.

## H. Tendencias

### Tendencias temporales

Cambia con manejo de peso y actividad física en semanas-meses — útil para seguimiento de respuesta a intervención de estilo de vida en personas con resistencia a la insulina ya identificada.

## I. Prevención

Acciones razonablemente relacionadas: manejo de peso, actividad física, reducción de carbohidratos refinados — mismo racional que para glucosa/triglicéridos elevados.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Glucosa (si no se solicitó junto — debe pedirse siempre en la misma muestra para HOMA-IR), Péptido C si hay sospecha de diabetes ya establecida y se busca diferenciar tipo 1 vs 2.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica de diabetes por sí sola — es una herramienta de detección temprana de resistencia a la insulina, un estado prediabético funcional que puede preceder por años a la alteración de glucosa/HbA1c.

## L. Evidencia

### Evidencia científica

- **Nivel:** el uso de insulina en ayunas para calcular HOMA-IR está ampliamente establecido en la literatura de resistencia a la insulina — ver evidencia detallada de variabilidad de umbrales en `homa_ir.md`.
- **Fuente:** ver evidencia detallada de variabilidad interensayo en `homa_ir.md` (Kollárová et al. 2019, EPIRCE 2013, biobanco a gran escala 2025). Nivel de evidencia: cohort/observacional, con conclusión consistente entre fuentes de que no existe un ensayo ni umbral de insulina estandarizado internacionalmente — esta es la conclusión verificada, no una fuente pendiente de citar.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "insulina en ayunas elevada, considerar junto a glucosa para calcular HOMA-IR y evaluar resistencia a la insulina".
- **prohibited_inferences:** diagnóstico de diabetes o prediabetes a partir de insulina aislada.
- **uncertainty_notes:** existe variabilidad interensayo significativa en la medición de insulina que afecta directamente la fiabilidad de HOMA-IR — comunicar esta limitación.
- **professional_review:** insulina marcadamente elevada combinada con otros componentes de síndrome metabólico, o sospecha clínica de síndrome de ovario poliquístico con componente metabólico.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - metabolism
  - insulin_resistance
  - tier_2
  - saludly_brain_v1

use_when:
  - "sospecha de resistencia a la insulina"
  - "calculando HOMA-IR junto a glucosa"
  - "síndrome de ovario poliquístico con componente metabólico"

combine_with: [glucose, homa_ir, triglycerides, hdl_c]

do_not_use_alone:
  - "diagnóstico de diabetes o prediabetes"

do_not_conclude:
  - "diagnóstico de diabetes a partir de insulina aislada"

escalate_when:
  - "patrón combinado de resistencia a la insulina con múltiples componentes de síndrome metabólico"
```
