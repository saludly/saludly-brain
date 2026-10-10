---
doc_id: "SLD-BIO-131"
biomarker_id: "remnant_cholesterol"
name_es: "Colesterol remanente"
name_en: "Remnant cholesterol"
abbreviation: "Col. remanente"
sinonimos: ["Colesterol remanente", "Remnant cholesterol", "Colesterol de lipoproteínas remanentes"]
category: "Lípidos"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "mg/dL"
formula: "colesterol total - HDL - LDL"
entradas: ["total_cholesterol", "hdl_c", "ldl_c"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor y rango (contexto)"
panel: "calculado, todas las personas"
alimenta: ["COND-M1-CA-001", "COND-M1-CA-003", "SEG-014"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-131 · Colesterol remanente

## A. Identificación
Colesterol que transportan las lipoproteínas ricas en triglicéridos (las que no son LDL ni HDL).

## B. Definición
Se asocia a riesgo cardiovascular más allá del LDL, sobre todo cuando los triglicéridos están altos.

## C. Cálculo y condiciones
Solo tiene sentido si el LDL es **medido** (directo). Si el laboratorio calcula el LDL con la fórmula de Friedewald, el remanente sale igual a triglicéridos / 5 y no aporta nada nuevo: en ese caso no se calcula. Requiere ayuno de 8 horas o más.

## D. Intervalos y umbrales
Sin intervalo del laboratorio ni corte de guía adoptado en los lotes. Se muestra solo el valor; en la vista médica se puede anotar un corte de la literatura cuando se verifique.

## E. Interpretación
Contexto de dislipidemia e hipertrigliceridemia; nunca forma un hallazgo propio.

## F. Contexto del paciente y confusores
Ayuno insuficiente, LDL calculado, triglicéridos de 400 mg/dL o más (el LDL directo pierde precisión).

## G. Relaciones
Triglicéridos, LDL, no-HDL, ApoB (M1).

## H. Tendencias
Baja con las mismas medidas que bajan los triglicéridos.

## I. Prevención
Reducir azúcar, harinas refinadas y alcohol; actividad física.

## J. Pruebas complementarias
ApoB (en el panel).

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Por verificar; sin guía adoptada en los lotes.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "dato de contexto sobre tus grasas en sangre".
- Inferencias prohibidas: riesgo cardiovascular individual a partir del remanente.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [lipidos, calculado, contexto_cardiovascular, saludly_brain_v1]
use_when: ["triglicéridos altos con LDL medido"]
combine_with: [triglycerides, ldl_c, non_hdl_c, apob]
do_not_use_alone: ["estimar riesgo cardiovascular"]
do_not_conclude: ["enfermedad cardiovascular"]
escalate_when: []
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Colesterol total 228, HDL 36, LDL medido 142 | 50 mg/dL, solo valor |
| PDF mujer 34 años | Colesterol total 214, HDL 58, LDL medido 136 | 20 mg/dL, solo valor |
| LDL calculado | LDL por Friedewald | No se calcula |
