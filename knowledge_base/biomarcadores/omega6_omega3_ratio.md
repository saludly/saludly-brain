---
doc_id: "SLD-BIO-119"
biomarker_id: "omega6_omega3_ratio"
name_es: "Relación omega-6/omega-3"
name_en: "Omega-6 to omega-3 ratio"
abbreviation: "O6/O3"
sinonimos: ["Relación omega 6/omega 3", "Ratio omega-6/omega-3", "Cociente omega 6 omega 3"]
category: "Ácidos grasos"
parameter_type: "derived_ratio"
tipo_resultado: "numérico"
unidad_canonica: "sin unidad"
specimen: "Sangre total"
nivel_catalogo: "vitamina"
panel: "fuera del panel base"
alimenta: ["COND-M3-NU-A04"]
tier: 3
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-119 · Relación omega-6/omega-3

> **Decisión del 10 de octubre de 2026.** Retirada del panel base el 10 de octubre de 2026 (aprobación de Carlos): es una prueba especializada que no ofrecen los laboratorios clínicos comunes o que exige transporte especial, y ni Function Health ni Superpower la incluyen en su panel base. La ficha se conserva: si el resultado llega, se interpreta igual.

## A. Identificación
Cociente entre ácidos grasos omega-6 y omega-3 en sangre, por cromatografía de gases.

## B. Definición
Indica el balance entre los aceites vegetales (ricos en omega-6) y el pescado (rico en omega-3) en la dieta.

## C. Espécimen y toma
Sangre total.

## D. Intervalos y umbrales
Sin intervalo de referencia establecido ni meta de consenso.

## E. Interpretación
Siempre solo valor. Una relación alta acompaña a un índice omega-3 bajo y refuerza la misma recomendación.

## F. Contexto del paciente y confusores
Suplementos de omega-3, dieta con mucho aceite de soya o de maíz.

## G. Relaciones
Índice omega-3 (siempre juntos).

## H. Tendencias
Cambia con la dieta en semanas a meses.

## I. Prevención y alimentos
Más pescado graso; preferir aceite de oliva o de canola en lugar de cantidades grandes de aceites de soya o maíz.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
No escala.

## L. Evidencia
Por verificar; sin meta de consenso.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "valor informativo del balance de grasas de la dieta".
- Inferencias prohibidas: riesgo de enfermedad a partir de la relación.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [acidos_grasos, omega3, omega6, solo_informativo, panel_estandar, saludly_brain_v1]
use_when: ["relación omega-6/omega-3"]
combine_with: [omega3_index]
do_not_use_alone: ["estimar riesgo"]
do_not_conclude: ["inflamación", "riesgo cardiovascular"]
escalate_when: []
```
