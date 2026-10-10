---
doc_id: SLD-BIO-016
biomarker_id: platelets
name_es: Plaquetas
name_en: Platelets
abbreviation: PLT
sinonimos:
- Recuento de plaquetas
- Plaquetas
- PLT
- Platelets
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: x10³/µL
specimen: Sangre total EDTA
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M3-HE-005
- SEG-006
combine_with:
- mpv
- wbc
- hemoglobin
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

# Plaquetas (PLT)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M3-HE-005, SEG-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-016. PLT. Categoría: Hematología. Tipo: analito medido. Tier 1.

## B. Definición

Fragmentos celulares derivados de megacariocitos, esenciales para la hemostasia primaria (formación del tapón plaquetario). Su conteo es parte estándar del hemograma de cribado.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo (CBC) · Tubo EDTA · Método: analizador hematológico automatizado. Unidad: células/µL (o ×10⁹/L). No requiere ayuno. Factor preanalítico importante: la **pseudotrombocitopenia por agregación plaquetaria inducida por EDTA** es una interferencia de laboratorio conocida y relativamente frecuente — un conteo bajo inesperado sin sangrado clínico debe hacer sospechar este artefacto antes que trombocitopenia real.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (Cleveland Clinic/MedlinePlus, verificado esta sesión):** rango normal en adultos **150,000-400,000 plaquetas/µL (150-400 ×10⁹/L)**. Algunas referencias (UI Health Care) extienden el límite superior hasta 450,000/µL — Saludly debe validar el límite exacto con el laboratorio aliado, ambos rangos son clínicamente aceptados. Trombocitopenia: <150,000/µL. Trombocitosis: >450,000/µL.
- **URL fuente:** https://my.clevelandclinic.org/health/diagnostics/21782-platelet-count — verificado esta sesión (ago-2026).

## E. Interpretación

- **Elevado (trombocitosis):** reactiva (inflamación, infección, deficiencia de hierro, post-esplenectomía, ejercicio) es mucho más frecuente que trombocitosis primaria (proceso mieloproliferativo) — la distinción requiere contexto clínico y, si corresponde, evaluación dirigida.
- **Disminuido (trombocitopenia):** causas incluyen destrucción periférica (autoinmune, hiperesplenismo), producción reducida (medular), consumo (coagulopatía), o el artefacto de pseudotrombocitopenia por EDTA ya mencionado.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: síntomas de sangrado (petequias, equimosis fáciles, sangrado de encías), medicamentos (heparina, quimioterapia), infección/inflamación reciente, antecedente de esplenectomía.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: VPM/MPV (tamaño plaquetario, orienta si la médula está produciendo plaquetas jóvenes de reemplazo), Leucocitos, Hemoglobina (para evaluar si hay afectación de más de una línea celular, lo que orienta hacia causa medular).
- `cannot_conclude`: causa específica de trombocitopenia/trombocitosis sin diferencial completo y contexto clínico.

## H. Tendencias

### Tendencias temporales

Un descenso progresivo sostenido, o el compromiso simultáneo de otras líneas celulares (anemia + leucopenia + trombocitopenia), es más preocupante que una alteración aislada de plaquetas.

## I. Prevención

Utilidad preventiva principalmente como parte del cribado hematológico general y para detectar trombocitopenia/trombocitosis asintomática antes de procedimientos o síntomas de sangrado.

## J. Pruebas complementarias

### Pruebas complementarias posibles

VPM/MPV si no se solicitó junto; repetir en tubo citrato si se sospecha pseudotrombocitopenia por EDTA (interferencia de laboratorio conocida).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del hemograma de cribado — no diagnóstico de ninguna condición hematológica específica por sí solo.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar; la pseudotrombocitopenia por EDTA es un artefacto de laboratorio ampliamente documentado en hematología clínica.
- **Fuente:** Cleveland Clinic, "Platelet Count (PLT)." https://my.clevelandclinic.org/health/diagnostics/21782-platelet-count — verificado esta sesión (ago-2026). Nivel de evidencia: referencia clínica institucional estándar.

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "conteo plaquetario alterado, considerar contexto clínico (sangrado, infección reciente) y, si es bajo de forma inesperada, considerar artefacto de laboratorio antes de asumir hallazgo real".
- **prohibited_inferences:** diagnóstico de trombocitopenia autoinmune, proceso mieloproliferativo, u otra condición hematológica específica a partir del conteo aislado.
- **uncertainty_notes:** un conteo bajo inesperado sin síntomas de sangrado y sin otra línea celular afectada debe generar sospecha de pseudotrombocitopenia por EDTA antes que alarma clínica.
- **professional_review:** trombocitopenia marcada, trombocitosis marcada y persistente, síntomas de sangrado activo, o compromiso simultáneo de otras líneas celulares.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - hemostasis
  - tier_1
  - saludly_brain_v1

use_when:
  - "interpretando hemograma completo"
  - "evaluando riesgo de sangrado o síntomas hemorrágicos"

combine_with: [mpv, wbc, hemoglobin]

do_not_use_alone:
  - "diagnóstico de trombocitopenia autoinmune o proceso mieloproliferativo"

do_not_conclude:
  - "condición hematológica específica sin diferencial y contexto clínico"

escalate_when:
  - "trombocitopenia o trombocitosis marcada"
  - "síntomas de sangrado activo (petequias, equimosis, sangrado de encías)"
  - "compromiso simultáneo de otras líneas celulares (anemia, leucopenia)"
```
