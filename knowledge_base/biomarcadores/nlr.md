---
doc_id: "SLD-BIO-144"
biomarker_id: "nlr"
name_es: "Relación neutrófilos/linfocitos"
name_en: "Neutrophil to lymphocyte ratio"
abbreviation: "NLR"
sinonimos: ["Relación neutrófilos/linfocitos", "NLR", "Índice neutrófilo-linfocito", "Neutrophil-lymphocyte ratio"]
category: "Inmunología"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
formula: "neutrófilos absolutos / linfocitos absolutos"
entradas: ["neutrophils_abs", "lymphocytes_abs"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor (vigilar)"
panel: "calculado, todas las personas"
alimenta: ["REL-030"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-144 · Relación neutrófilos/linfocitos

## A. Identificación
Cociente entre dos tipos de glóbulos blancos que refleja el balance entre inflamación y defensa.

## B. Definición
Se asocia a inflamación sistémica; su utilidad en personas sanas es limitada y no tiene guía.

## C. Cálculo y condiciones
Se calcula con neutrófilos y linfocitos absolutos.

## D. Intervalos y umbrales
Corte provisional de 3 (por verificar); solo para vigilar.

## E. Interpretación
Solo alimenta la señal para vigilar REL-030 junto con la PCR. Nunca llega solo al informe del paciente.

## F. Contexto del paciente y confusores
Infección reciente, ejercicio intenso, estrés agudo, corticoides.

## G. Relaciones
PCR ultrasensible, leucocitos.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Asociación descrita en estudios de cohorte; sin guía clínica.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un cálculo de tus glóbulos blancos acompaña a tu PCR alta".
- Inferencias prohibidas: "tienes una inflamación grave", "tienes cáncer".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [inmunologia, calculado, inflamacion, vigilar, saludly_brain_v1]
use_when: ["PCR alta"]
combine_with: [hs_crp, neutrophils_abs, lymphocytes_abs]
do_not_use_alone: [nlr]
do_not_conclude: []
escalate_when: []
```
