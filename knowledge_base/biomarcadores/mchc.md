---
doc_id: SLD-BIO-006
biomarker_id: mchc
name_es: CHCM
name_en: MCHC (Mean Corpuscular Hemoglobin Concentration)
abbreviation: CHCM / MCHC
sinonimos:
- CHCM
- MCHC
- Concentración de hemoglobina corpuscular media
- CHCM (Concentración de Hemoglobina Corpuscular Media)
- CHCM / MCHC
- MCHC (Mean Corpuscular Hemoglobin Concentration)
category: hematology
parameter_type: calculated_parameter
tipo_resultado: numérico
unidad_canonica: g/dL
specimen: Sangre total EDTA
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-012
combine_with:
- mcv
- mch
- hemoglobin
formula: CHCM = (Hemoglobina / Hematocrito) × 100
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# CHCM (Concentración de Hemoglobina Corpuscular Media)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-012. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-006. CHCM/MCHC. Categoría: Hematología. Tipo: **parámetro calculado**. Tier 2.

## B. Definición

Concentración de hemoglobina dentro de cada eritrocito (a diferencia de HCM, que es la cantidad absoluta). A diferencia de VCM/HCM, CHCM **sí aporta información diferenciada** en un escenario clínico específico: la esferocitosis hereditaria y ciertas hemoglobinopatías, donde CHCM está elevada de forma característica pese a VCM normal/bajo.

## C. Espécimen y toma

### Fórmula y limitaciones

- **Fórmula:** CHCM = (Hemoglobina / Hematocrito) × 100.
- **Variables necesarias:** Hemoglobina, Hematocrito.
- **Valor diferenciado real:** CHCM elevada (hipercrómica) es un hallazgo relativamente específico de esferocitosis hereditaria o, con menor frecuencia, ciertas hemoglobinopatías — a diferencia de HCM, que rara vez añade información sobre VCM.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal **32-37 g/dL** (fuentes varían: 31.5-37 g/dL Roswell Park, 32-36 g/dL Ozellemed).
- **URL fuente:** https://www.roswellpark.org/cancertalk/202310/understanding-your-blood-test-results ; https://ozellemed.com/en/reference-ranges-in-hematology-normal-vs-abnormal/ — verificadas esta sesión (ago-2026).

## E. Interpretación

- **Elevada (hipercrómica):** esferocitosis hereditaria, algunas hemoglobinopatías — hallazgo poco frecuente pero relativamente específico.
- **Disminuida (hipocrómica):** deficiencia de hierro, talasemia — coincide generalmente con VCM bajo.

## F. Contexto del paciente y confusores

### Contexto del paciente

Antecedente familiar de anemia hemolítica o esferocitosis, síntomas de hemólisis (ictericia, fatiga).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: VCM, HCM, Hemoglobina — CHCM elevada con VCM normal/bajo es la combinación relevante a señalar.
- `cannot_conclude`: diagnóstico de esferocitosis sin frotis de sangre periférica (fuera del alcance de Saludly).

## H. Tendencias

### Tendencias temporales

Relativamente estable — un hallazgo hipercrómico persistente amerita evaluación, no solo repetición.

## I. Prevención

Utilidad limitada como marcador preventivo — más relevante como hallazgo orientador de patología hemolítica hereditaria.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Frotis de sangre periférica si CHCM está elevada de forma inexplicada (fuera del alcance de Saludly, requiere derivación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Hallazgo orientador, no diagnóstico — la confirmación de esferocitosis requiere frotis y, en algunos casos, pruebas específicas de fragilidad osmótica.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar sobre morfología eritrocitaria.
- **Fuente:** Roswell Park Comprehensive Cancer Center y revisión de rangos hematológicos (Ozellemed, 2026) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "CHCM elevada (hipercrómica) sugiere considerar esferocitosis hereditaria u otra causa de hemólisis, especialmente con antecedente familiar".
- **prohibited_inferences:** diagnóstico de esferocitosis sin frotis de sangre periférica.
- **uncertainty_notes:** hallazgo relativamente específico pero infrecuente — no generar alarma desproporcionada sin contexto familiar o síntomas.
- **professional_review:** CHCM elevada persistente, especialmente con antecedente familiar de anemia hemolítica o síntomas de hemólisis.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - calculated_parameter
  - hemolysis
  - tier_2
  - saludly_brain_v1
use_when:
  - "CHCM elevada con VCM normal/bajo — posible esferocitosis"
combine_with: [mcv, mch, hemoglobin]
do_not_use_alone:
  - "diagnóstico de esferocitosis sin frotis de sangre periférica"
do_not_conclude:
  - "esferocitosis confirmada sin frotis"
escalate_when:
  - "CHCM elevada persistente con antecedente familiar o síntomas de hemólisis"
```
