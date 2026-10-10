---
doc_id: "SLD-BIO-132"
biomarker_id: "tc_hdl_ratio"
name_es: "Relación colesterol total/HDL"
name_en: "Total cholesterol to HDL ratio"
abbreviation: "CT/HDL"
sinonimos: ["Relación colesterol total/HDL", "Índice de Castelli", "Índice aterogénico", "CT/HDL", "TC/HDL ratio"]
category: "Lípidos"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
formula: "colesterol total / HDL"
entradas: ["total_cholesterol", "hdl_c"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor y rango (contexto)"
panel: "calculado, todas las personas"
alimenta: ["COND-M1-CA-001", "COND-M1-CA-005", "SEG-014"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-132 · Relación colesterol total/HDL

## A. Identificación
Cociente entre el colesterol total y el HDL, conocido también como índice de Castelli.

## B. Definición
Resume en un número el balance entre el colesterol que se acumula en las arterias y el que se retira de ellas.

## C. Cálculo y condiciones
Se calcula siempre que estén colesterol total y HDL medidos.

## D. Intervalos y umbrales
Sin corte de guía adoptado en los lotes. Las guías usadas en el módulo M1 prefieren el no-HDL y la ApoB para decidir; la relación se muestra como valor de contexto. Los cortes tradicionales que circulan en la literatura no se usan hasta verificarlos.

## E. Interpretación
Contexto de dislipidemia y riesgo global; nunca forma un hallazgo propio.

## F. Contexto del paciente y confusores
HDL muy alto puede dar una relación baja que tranquiliza de más.

## G. Relaciones
Colesterol total, HDL, no-HDL, ApoB (M1).

## H. Tendencias
Mejora con más actividad física y menos azúcar.

## I. Prevención
Las de dislipidemia (M1 CA-001).

## J. Pruebas complementarias
No-HDL y ApoB (en el panel).

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "dato de contexto sobre el balance de tu colesterol".
- Inferencias prohibidas: riesgo cardiovascular individual a partir de la relación.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [lipidos, calculado, contexto_cardiovascular, saludly_brain_v1]
use_when: ["contexto del perfil lipídico"]
combine_with: [total_cholesterol, hdl_c, non_hdl_c, apob]
do_not_use_alone: ["decidir riesgo cardiovascular"]
do_not_conclude: ["enfermedad cardiovascular"]
escalate_when: []
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Colesterol total 228, HDL 36 | 6,33, solo valor |
| PDF mujer 34 años | Colesterol total 214, HDL 58 | 3,69, solo valor |
| Sin HDL | HDL no medido | No se calcula |
