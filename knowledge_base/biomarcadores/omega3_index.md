---
doc_id: "SLD-BIO-118"
biomarker_id: "omega3_index"
name_es: "Índice omega-3"
name_en: "Omega-3 index"
abbreviation: "O3I"
sinonimos: ["Índice omega-3", "Omega-3 index", "EPA+DHA en eritrocitos", "Índice de omega 3"]
category: "Ácidos grasos"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "%"
specimen: "Sangre total (membranas de glóbulos rojos)"
nivel_catalogo: "vitamina"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-118 · Índice omega-3

## A. Identificación
Porcentaje de EPA y DHA sobre el total de ácidos grasos de las membranas de los glóbulos rojos, por cromatografía de gases.

## B. Definición
Refleja el consumo de omega-3 de origen marino en los últimos meses, porque los glóbulos rojos viven unos 120 días.

## C. Espécimen y toma
Sangre total; el ayuno no es crítico.

## D. Intervalos y umbrales
El laboratorio de ejemplo no reporta intervalo ("No establecido"). En la literatura se ha propuesto un índice de 8 % o más como deseable y menor de 4 % como de mayor riesgo cardiovascular, pero no es un estándar clínico: esos cortes solo se muestran en la vista médica, como contexto.

## E. Interpretación
Se muestra el valor al paciente sin clase. Bajo en la vista médica: refuerza la recomendación de pescado.

## F. Contexto del paciente y confusores
Suplementos de omega-3, dieta vegetariana (el ALA de la linaza o la chía se convierte poco en EPA y DHA).

## G. Relaciones
Triglicéridos y riesgo cardiovascular (M1), como contexto.

## H. Tendencias
Cambia en semanas a meses con la dieta.

## I. Prevención y alimentos
Sardina, atún, salmón, trucha y otros pescados grasos dos veces por semana. Linaza y chía aportan omega-3 vegetal.

## J. Pruebas complementarias
Relación omega-6/omega-3 (en el panel).

## K. Cuándo no interpretar / cuándo escalar
No escala. Los suplementos en dosis altas con anticoagulantes requieren hablarlo con el médico.

## L. Evidencia
Por verificar. Corte del 8 %: propuesto en la literatura (Harris y von Schacky, 2004), sin consenso de guía.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "valor de omega-3; comer pescado graso con regularidad lo mejora".
- Inferencias prohibidas: riesgo cardiovascular individual a partir del índice, dosis de suplemento.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [acidos_grasos, omega3, nutricion, panel_estandar, saludly_brain_v1]
use_when: ["índice omega-3", "recomendación de pescado"]
combine_with: [omega6_omega3_ratio, triglycerides]
do_not_use_alone: ["estimar riesgo cardiovascular"]
do_not_conclude: ["riesgo cardiovascular alto"]
escalate_when: []
```
