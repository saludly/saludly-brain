---
doc_id: SLD-BIO-077
biomarker_id: serum_iron
name_es: Hierro sérico
name_en: Serum Iron
abbreviation: Fe
sinonimos:
- Hierro sérico
- Hierro
- Fe
- Serum Iron
category: iron_micronutrients
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: µg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-002
- COND-M3-HE-006
combine_with:
- ferritin
- transferrin
- transferrin_saturation
- hemoglobin
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

# Hierro sérico

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-002, COND-M3-HE-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-077. Fe. Categoría: Hierro/Micronutrientes. Tipo: analito medido. Tier 2 — se ordena siempre junto al resto del perfil de hierro, nunca aislado.

## B. Definición

Concentración de hierro circulante unido a transferrina. Tiene **alta variabilidad diurna** (más alto en la mañana) y es fácilmente influenciable por ingesta reciente de hierro — por eso su valor aislado es mucho menos confiable que ferritina o saturación de transferrina para evaluar reservas corporales de hierro.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico estandarizado. Unidad: µg/dL. **Ayuno matutino recomendado** (a diferencia de ferritina) por su variabilidad diurna y sensibilidad a ingesta reciente. Factor preanalítico crítico: suplementación de hierro reciente (incluso 24h antes) puede elevarlo artificialmente.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal de hierro sérico total **50-150 µg/dL**. Capacidad total de fijación de hierro (TIBC): 250-310 µg/dL.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevado:** suplementación reciente, sobrecarga de hierro (hemocromatosis), hepatopatía, ingesta reciente.
- **Disminuido:** deficiencia de hierro, inflamación crónica (redistribución del hierro, no necesariamente depleción real), pérdida sanguínea.
- Por su alta variabilidad, **un solo valor de hierro sérico tiene bajo valor diagnóstico aislado** — su utilidad real está en combinación con transferrina (para calcular saturación).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: suplementación de hierro reciente, hora de la toma, dieta reciente, proceso inflamatorio/infeccioso activo.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Ferritina, Transferrina (obligatorio, para calcular saturación de transferrina), Hemoglobina.
- `pattern_examples`: hierro bajo + transferrina alta (TIBC alta) + saturación baja = patrón clásico de deficiencia de hierro; hierro bajo + transferrina baja (TIBC baja) + saturación variable = patrón más compatible con anemia de enfermedad crónica/inflamación.
- `cannot_conclude`: estado real de reservas de hierro sin el resto del perfil.

## H. Tendencias

### Tendencias temporales

Alta variabilidad día a día — no es un buen marcador de tendencia longitudinal aislado; Ferritina es preferible para seguimiento de reservas en el tiempo.

## I. Prevención

Utilidad principalmente como parte del panel de hierro completo, no como marcador aislado de cribado.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Transferrina/TIBC (si no se solicitaron juntas — deberían pedirse siempre en conjunto), Ferritina, hs-CRP (para contextualizar si hay inflamación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstico aislado — su valor depende completamente de interpretarse junto al resto del perfil de hierro.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar sobre metabolismo del hierro.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "hierro sérico alterado, requiere interpretación junto a transferrina/saturación y ferritina — no interpretar de forma aislada".
- **prohibited_inferences:** diagnóstico de deficiencia o sobrecarga de hierro a partir de hierro sérico aislado.
- **uncertainty_notes:** alta variabilidad diurna y sensibilidad a suplementación reciente — de los biomarcadores del catálogo, uno de los que menos debe interpretarse solo.
- **professional_review:** valores marcadamente alterados combinados con el resto del perfil de hierro (transferrina/saturación/ferritina).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - iron_metabolism
  - anemia_workup
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando perfil de hierro completo junto a ferritina y transferrina"

combine_with: [ferritin, transferrin, transferrin_saturation, hemoglobin]

do_not_use_alone:
  - "cualquier interpretación sin el resto del perfil de hierro"

do_not_conclude:
  - "deficiencia o sobrecarga de hierro a partir de hierro sérico aislado"

escalate_when:
  - "valores marcadamente alterados combinados con ferritina/saturación"
```
