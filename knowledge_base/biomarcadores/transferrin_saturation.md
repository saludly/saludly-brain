---
doc_id: SLD-BIO-079
biomarker_id: transferrin_saturation
name_es: Saturación de transferrina
name_en: Transferrin Saturation
abbreviation: TSAT
sinonimos:
- Saturación de transferrina
- '% de saturación de transferrina'
- IST
- TSAT
- Transferrin Saturation
category: iron_micronutrients
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: '%'
specimen: No aplica (calculado)
nivel_catalogo: con patrón
panel: calculado
sexo: ambos
alimenta:
- COND-M3-HE-002
- COND-M3-HE-006
- COND-M3-HE-A01
combine_with:
- serum_iron
- transferrin
- ferritin
formula: Saturación de transferrina = (Hierro sérico ÷ TIBC) × 100; TIBC puede medirse directamente o derivarse de transferrina
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Posible sobrecarga: > 45 % en mujeres premenopáusicas o > 50 % en el resto, con ferritina alta (COND-M3-HE-006).'
---

# Saturación de transferrina (TSAT)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Posible sobrecarga: > 45 % en mujeres premenopáusicas o > 50 % en el resto, con ferritina alta (COND-M3-HE-006).
- Reglas que usan esta ficha: COND-M3-HE-002, COND-M3-HE-006, COND-M3-HE-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-079. TSAT. Categoría: Hierro/Micronutrientes. Tipo: **parámetro calculado**. Tier 2.

## B. Definición

Porcentaje de los sitios de unión de la transferrina que están efectivamente ocupados por hierro. Es, junto con ferritina, uno de los dos pilares para evaluar el estado del hierro corporal — pero a diferencia de ferritina, **no se comporta como reactante de fase aguda**, lo que la hace más confiable en presencia de inflamación concurrente.

## C. Espécimen y toma

### Fórmula y limitaciones (obligatorio para parámetro calculado)

- **Fórmula:** TSAT = (Hierro sérico ÷ TIBC) × 100.
- **Variables necesarias:** Hierro sérico (medido), TIBC (Capacidad Total de Fijación de Hierro — puede medirse directamente o derivarse matemáticamente de transferrina; Saludly debe registrar cuál método usa el laboratorio aliado).
- **Cuándo NO debe calcularse:** si hierro sérico y TIBC/transferrina no provienen de la misma muestra/momento — combinar valores de fechas distintas invalida el cálculo.
- **Limitación:** hereda toda la variabilidad diurna del hierro sérico (ver `serum_iron.md`) — idealmente calculada con muestra matutina en ayunas.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método usado para TIBC.
- **Clinical decision threshold (derivado de componentes ya verificados esta sesión):** con Hierro sérico 50-150 µg/dL y TIBC 250-310 µg/dL (ver `serum_iron.md`), la saturación de transferrina normal calculada es aproximadamente **20-50%**. TSAT <20% sugiere deficiencia de hierro; TSAT >45-50% sugiere sobrecarga de hierro (ampliamente usado como criterio de cribado inicial de hemocromatosis junto a ferritina elevada).
- **URL fuente:** derivado de fuentes ya citadas en `serum_iron.md`/`transferrin.md` (Medscape Lab Values) — verificado esta sesión (ago-2026).

## E. Interpretación

- **Baja:** compatible con deficiencia de hierro cuando se acompaña de ferritina baja; si ferritina es normal/alta, más compatible con anemia de enfermedad crónica.
- **Alta:** sobrecarga de hierro (hemocromatosis), o suplementación reciente.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: hora de la toma (ayuno matutino ideal), suplementación de hierro reciente, proceso inflamatorio activo.

## G. Relaciones con otros biomarcadores

### Relaciones con otros biomarcadores (sección G)

- `interpret_together_with`: Ferritina (obligatorio — juntos son los dos pilares del diagnóstico de estado de hierro), Hierro sérico, Transferrina.
- `pattern_examples`: TSAT baja + ferritina baja = deficiencia de hierro con alta confianza; TSAT baja + ferritina normal/alta = sugiere inflamación concurrente enmascarando la ferritina, considerar hs-CRP.
- `cannot_conclude`: causa de la alteración sin el contexto clínico e inflamatorio completo.

## H. Tendencias

### Tendencias temporales

Menos variable día a día que hierro sérico aislado, pero hereda parte de su variabilidad diurna — ferritina sigue siendo el marcador más estable para tendencia longitudinal de reservas de hierro.

## I. Prevención

Junto a ferritina, es la herramienta preventiva más confiable para detectar deficiencia de hierro temprana, especialmente cuando hay sospecha de inflamación concurrente que podría enmascarar la ferritina.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ferritina (si no está disponible), hs-CRP (para contextualizar si hay inflamación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Es una de las herramientas más robustas de cribado del estado de hierro dentro del catálogo — pero sigue sin ser diagnóstica por sí sola de la causa subyacente (dietética, malabsortiva, por pérdida sanguínea).

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar; TSAT junto a ferritina es ampliamente reconocido como el estándar de evaluación del estado de hierro en la literatura hematológica.
- **Fuente:** derivado de fuentes ya citadas en `serum_iron.md`/`transferrin.md` — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "TSAT baja junto a ferritina baja sugiere deficiencia de hierro con buena confianza; TSAT baja con ferritina normal/alta sugiere considerar inflamación concurrente".
- **prohibited_inferences:** diagnóstico de causa específica de deficiencia (dietética, malabsortiva, por sangrado) sin historia clínica dirigida.
- **uncertainty_notes:** hereda variabilidad diurna del hierro sérico — idealmente interpretar con muestra matutina en ayunas.
- **professional_review:** TSAT muy baja con síntomas de anemia, o TSAT muy alta sugestiva de sobrecarga de hierro.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - iron_metabolism
  - anemia_workup
  - calculated_parameter
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando estado de hierro junto a ferritina, especialmente con sospecha de inflamación concurrente"

combine_with: [serum_iron, transferrin, ferritin]

do_not_use_alone:
  - "diagnóstico de causa de deficiencia de hierro"

do_not_conclude:
  - "causa específica sin historia clínica dirigida"

escalate_when:
  - "TSAT muy baja con síntomas de anemia"
  - "TSAT muy alta sugestiva de sobrecarga de hierro"
```
