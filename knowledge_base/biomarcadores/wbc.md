---
doc_id: SLD-BIO-008
biomarker_id: wbc
name_es: Leucocitos (conteo total)
name_en: White Blood Cell Count (Total)
abbreviation: WBC / Leucocitos
sinonimos:
- Recuento de leucocitos
- Leucocitos
- Glóbulos blancos
- WBC
- Leucocitos (conteo total)
- WBC / Leucocitos
- White Blood Cell Count (Total)
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: x10³/µL
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-A02
- COND-M3-HE-A03
- COND-M6-MI-A02
combine_with:
- neutrophils_abs
- lymphocytes_abs
- hs_crp
tier: 1
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Leucocitos (conteo total, WBC)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-A02, COND-M3-HE-A03, COND-M6-MI-A02. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-008. WBC. Categoría: Hematología. Tipo: analito medido. Tier 1.

## B. Definición

Conteo total de glóbulos blancos circulantes — engloba neutrófilos, linfocitos, monocitos, eosinófilos y basófilos. Refleja de forma general la actividad del sistema inmune/hematopoyético, pero es inespecífico sin el diferencial.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo (CBC) · Tubo EDTA · Método: analizador hematológico automatizado (citometría de flujo/impedancia). Unidad: células/µL (o ×10⁹/L). No requiere ayuno. Factor preanalítico: estrés agudo, ejercicio intenso reciente pueden elevarlo transitoriamente (leucocitosis por demarginación).

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (MedlinePlus/NIH, verificado esta sesión):** rango normal en adultos **4,500-11,000 WBC/µL (4.5-11.0 ×10⁹/L)**. Referencia complementaria (UI Health Care, hospital académico): 3.7-10.5 ×10³/mm³ para ambos sexos.
- **URL fuente:** https://medlineplus.gov/ency/article/003643.htm — verificado esta sesión (ago-2026).

## E. Interpretación

- **Elevado (leucocitosis):** infección (bacteriana con más frecuencia que viral), inflamación, estrés/ejercicio reciente, corticoides, tabaquismo, procesos hematológicos (requiere diferencial y contexto para distinguir causa reactiva de proceso hematológico primario).
- **Disminuido (leucopenia):** infección viral, ciertos medicamentos, procesos autoinmunes, causas hematológicas — requiere diferencial para precisar.
- **Dentro del intervalo:** no descarta infección o inflamación localizada leve.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: síntomas de infección/inflamación reciente, medicamentos (corticoides, quimioterapia, inmunosupresores), tabaquismo, ejercicio/estrés reciente al momento de la toma.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: diferencial (neutrófilos, linfocitos absolutos), hs-CRP.
- `pattern_examples`: leucocitosis + neutrofilia + hs-CRP elevada = patrón compatible con proceso infeccioso/inflamatorio agudo, más que leucocitosis aislada.
- `cannot_conclude`: tipo de infección o presencia de proceso hematológico primario sin diferencial completo y, si corresponde, evaluación dirigida.

## H. Tendencias

### Tendencias temporales

Valor puntual muy sensible a condiciones agudas (infección, estrés) — la tendencia longitudinal es menos informativa aquí que en biomarcadores metabólicos; una elevación aislada coincidente con síntomas de infección reciente no debe interpretarse como hallazgo estructural.

## I. Prevención

Utilidad preventiva limitada de forma aislada; su valor principal es como parte del hemograma de cribado general y como apoyo ante sospecha de proceso infeccioso/inflamatorio.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Diferencial leucocitario si no se solicitó junto (Saludly debe idealmente ofrecerlo siempre como parte del mismo hemograma, no como prueba separada).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del hemograma de cribado — no diagnóstico de infección, inflamación ni proceso hematológico específico por sí solo.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar.
- **Fuente:** MedlinePlus (NIH/National Library of Medicine), "WBC count." https://medlineplus.gov/ency/article/003643.htm — verificado esta sesión (ago-2026). Nivel de evidencia: referencia clínica institucional estándar.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "recuento leucocitario alterado, compatible con posible proceso infeccioso/inflamatorio o reactivo, requiere diferencial y contexto clínico".
- **prohibited_inferences:** "tiene una infección", "tiene leucemia" u otro diagnóstico hematológico específico a partir del conteo total aislado.
- **uncertainty_notes:** el conteo total sin diferencial tiene valor limitado — el sistema debe evitar generar interpretaciones fuertes sin el diferencial disponible.
- **professional_review:** valores marcadamente fuera de rango, especialmente sin causa reactiva evidente (sin infección/estrés/ejercicio reciente reportado), o síntomas sistémicos concurrentes (fiebre, pérdida de peso, sudoración nocturna).

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - immune_inflammation
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando hemograma completo"
  - "evaluando sospecha de infección o inflamación"

combine_with: [neutrophils_abs, lymphocytes_abs, hs_crp]

do_not_use_alone:
  - "diagnóstico de infección, inflamación o proceso hematológico"

do_not_conclude:
  - "tiene infección"
  - "tiene una neoplasia hematológica"

escalate_when:
  - "valor marcadamente fuera de rango sin causa reactiva evidente"
  - "síntomas sistémicos concurrentes (fiebre, pérdida de peso, sudoración nocturna)"
```
