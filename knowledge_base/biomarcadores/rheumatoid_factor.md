---
doc_id: "SLD-BIO-134"
biomarker_id: "rheumatoid_factor"
name_es: "Factor reumatoide"
name_en: "Rheumatoid factor"
abbreviation: "FR"
sinonimos: ["Factor reumatoide", "FR", "RF", "Factor reumatoideo", "Factor reumatoideo cuantitativo", "Látex FR", "Rheumatoid factor"]
category: "Inmunología"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "UI/mL"
specimen: "Suero"
nivel_catalogo: "solo valor y rango (vigilar)"
panel: "estándar, todas las personas"
alimenta: ["REL-031"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-134 · Factor reumatoide

## A. Identificación
Anticuerpo (casi siempre IgM) dirigido contra la porción Fc de la IgG.

## B. Definición
Aparece en la artritis reumatoide, pero también en otras enfermedades autoinmunes, infecciones crónicas (hepatitis C), en personas mayores y en una parte de la población sana.

## C. Espécimen y toma
Suero de la toma de la mañana. Se pide método cuantitativo (nefelometría o turbidimetría), no la prueba manual de látex.

## D. Intervalos y umbrales
Se usa el intervalo del laboratorio (habitualmente menor de 14 a 20 UI/mL). Positivo alto: más de 3 veces el límite superior (criterio ACR/EULAR 2010, que solo se aplica con sinovitis).

## E. Interpretación
En una persona sin síntomas articulares un FR positivo **no** es artritis reumatoide: su valor predictivo es bajo. Por eso solo alimenta una señal para vigilar (REL-031) junto con ANA, VSG y PCR.

## F. Contexto del paciente y confusores
Edad mayor de 60 años, hepatitis C, infecciones crónicas, tabaquismo.

## G. Relaciones
ANA, VSG, PCR ultrasensible; anti-CCP como refleja (SLD-BIO-140).

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Anti-CCP si el FR sale positivo (refleja).

## K. Cuándo no interpretar / cuándo escalar
No escala por sí solo. Si hay dolor o inflamación de articulaciones declarados, se sugiere consulta.

## L. Evidencia
Criterios ACR/EULAR 2010 de artritis reumatoide (Aletaha 2010). Pendiente de verificar con la fuente completa.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un marcador inmunológico salió por encima del rango; por sí solo no indica una enfermedad".
- Inferencias prohibidas: "tienes artritis reumatoide", "tienes una enfermedad autoinmune".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [inmunologia, autoinmunidad, vigilar, saludly_brain_v1]
use_when: ["FR fuera de rango", "señal autoinmune con ANA"]
combine_with: [ana_hep2, esr, hs_crp, anti_ccp]
do_not_use_alone: [rheumatoid_factor]
do_not_conclude: []
escalate_when: []
```
