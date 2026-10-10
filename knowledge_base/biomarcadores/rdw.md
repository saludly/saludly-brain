---
doc_id: SLD-BIO-007
biomarker_id: rdw
name_es: RDW
name_en: Red Cell Distribution Width
abbreviation: RDW
sinonimos:
- RDW
- RDW-CV
- Ancho de distribución eritrocitaria
- RDW (Ancho de Distribución Eritrocitaria)
- Red Cell Distribution Width
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: '%'
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-002
- COND-M6-MI-A02
combine_with:
- mcv
- hemoglobin
- ferritin
- vitamin_b12
- folate
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

# RDW (Ancho de Distribución Eritrocitaria)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-002, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-007. RDW. Categoría: Hematología. Tipo: analito medido. Tier 2 — alto valor diferencial, no accionable sin el resto del hemograma.

## B. Definición

Mide la variabilidad en el tamaño de los eritrocitos (anisocitosis). Un RDW elevado indica una población eritrocitaria heterogénea en tamaño — útil para diferenciar causas de anemia con VCM similar, y ha sido estudiado como marcador pronóstico general en varias condiciones (más allá de anemia), aunque ese uso es de investigación, no de práctica preventiva establecida.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo · Tubo EDTA · Método: citometría de flujo automatizada. Unidad: % (coeficiente de variación) o fL (desviación estándar, según analizador). No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (UI Health Care, verificado esta sesión):** rango normal RDW-CV **9.0-14.5%** (ambos sexos, adultos).
- **URL fuente:** https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589

## E. Interpretación

- **Elevado (anisocitosis):** deficiencia de hierro (clásicamente RDW alto con VCM bajo, a diferencia de talasemia donde RDW suele ser normal pese a VCM bajo — distinción útil), deficiencia mixta de hierro y B12/folato, anemia en evolución/recuperación reciente.
- **Normal:** no descarta anemia, pero sugiere una población eritrocitaria más homogénea (más compatible con talasemia o anemia de enfermedad crónica no complicada que con deficiencia nutricional activa).

## F. Contexto del paciente y confusores

### Contexto del paciente

Dieta, antecedente de sangrado, tratamiento reciente de una deficiencia (el RDW puede estar elevado transitoriamente durante la recuperación, cuando conviven eritrocitos nuevos y viejos de distinto tamaño).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: VCM (obligatorio — el par VCM+RDW es más informativo que cualquiera de los dos solos), Ferritina, Vitamina B12/Folato.
- `pattern_examples`: VCM bajo + RDW alto = sugiere deficiencia de hierro; VCM bajo + RDW normal = sugiere talasemia o anemia de enfermedad crónica; VCM alto + RDW alto = sugiere deficiencia de B12/folato o anemia hemolítica.
- `cannot_conclude`: diagnóstico definitivo sin ferritina/B12/folato según corresponda.

## H. Tendencias

### Tendencias temporales

Se eleva transitoriamente durante la recuperación de una anemia tratada (mezcla de células nuevas y viejas) — no interpretar un RDW elevado en ese contexto como empeoramiento.

## I. Prevención

Alto valor para orientar eficientemente qué prueba complementaria pedir (ferritina vs B12/folato) ante una anemia ya detectada.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Ferritina (si VCM bajo + RDW alto), Vitamina B12/Folato (si VCM alto + RDW alto).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Herramienta de clasificación dentro del hemograma — no diagnóstica por sí sola.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar sobre morfología eritrocitaria.
- **Fuente:** UI Health Care, tabla de rangos CBC. https://www.healthcare.uiowa.edu/path_handbook/handbook/test299.html ; flashcard institucional agregada de valores CBC estándar: https://brainscape.com/flashcards/complete-blood-count-cbc-3941325/packs/5770589 — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "RDW alterado, combinar con VCM para orientar hacia deficiencia de hierro, B12/folato, talasemia o anemia de enfermedad crónica".
- **prohibited_inferences:** diagnóstico específico sin ferritina o B12/folato según el patrón VCM+RDW.
- **uncertainty_notes:** RDW elevado durante recuperación de una deficiencia tratada no indica empeoramiento.
- **professional_review:** anemia con RDW marcadamente alterado sin causa evidente tras evaluación básica.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - anemia_classification
  - tier_2
  - saludly_brain_v1
use_when:
  - "clasificando anemia junto con VCM"
combine_with: [mcv, hemoglobin, ferritin, vitamin_b12, folate]
do_not_use_alone:
  - "cualquier interpretación sin VCM concurrente"
do_not_conclude:
  - "diagnóstico definitivo sin ferritina o B12/folato"
escalate_when:
  - "anemia con RDW marcadamente alterado sin causa evidente"
```
