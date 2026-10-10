---
doc_id: "SLD-BIO-114"
biomarker_id: "vitamin_k1"
name_es: "Vitamina K1 (filoquinona)"
name_en: "Vitamin K1 (phylloquinone)"
abbreviation: "Vit K1"
sinonimos: ["Vitamina K1", "Filoquinona", "Vitamina K", "Phylloquinone"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
specimen: "Suero en ayunas protegido de la luz"
nivel_catalogo: "vitamina"
panel: "fuera del panel base"
alimenta: ["COND-M3-NU-A04"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-114 · Vitamina K1 (filoquinona)

> **Decisión del 10 de octubre de 2026.** Retirada del panel base el 10 de octubre de 2026 (aprobación de Carlos): es una prueba especializada que no ofrecen los laboratorios clínicos comunes o que exige transporte especial, y ni Function Health ni Superpower la incluyen en su panel base. La ficha se conserva: si el resultado llega, se interpreta igual.

## A. Identificación
Filoquinona en suero por HPLC.

## B. Definición
Vitamina liposoluble necesaria para la coagulación y el hueso.

## C. Espécimen y toma
Suero en ayunas: refleja sobre todo lo que se comió el día anterior. Protegido de la luz.

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 0,10 a 2,20 ng/mL).

## E. Interpretación
Muestra la ingesta reciente más que las reservas. Viaja con los triglicéridos, que la suben. El déficit con efecto en la coagulación se ve en el tiempo de protrombina y el INR, no en este valor.

## F. Contexto del paciente y confusores
Warfarina (antagonista de la vitamina K), antibióticos prolongados, mala absorción de grasas, triglicéridos altos.

## G. Relaciones
Tiempo de protrombina e INR (SEG-006), triglicéridos.

## H. Tendencias
Varía de un día a otro con la dieta.

## I. Prevención y alimentos
Espinaca, brócoli, repollo, lechuga y otras hojas verdes. **A quien toma warfarina nunca se le recomienda comer más hojas verdes sin hablar con su médico**: un cambio brusco altera el efecto del medicamento.

## J. Pruebas complementarias
Tiempo de protrombina e INR (ya en el panel).

## K. Cuándo no interpretar / cuándo escalar
Con warfarina: sin recomendación alimentaria, solo nota para el médico. Bajo con INR alto sin anticoagulante: se lee en SEG-006 (escalamiento 2).

## L. Evidencia
Regla de vitaminas (documento 07). Fuentes por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "vitamina K1 baja en esta toma; refleja sobre todo la alimentación reciente".
- Inferencias prohibidas: cambiar la dieta a personas con warfarina, problema de coagulación por este valor.
- Revisión profesional: personas con warfarina.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, liposoluble, vitamina_k, coagulacion, panel_estandar, saludly_brain_v1]
use_when: ["vitamina K1 fuera de rango"]
combine_with: [pt, inr, triglycerides]
do_not_use_alone: ["evaluar coagulación"]
do_not_conclude: ["trastorno de coagulación"]
escalate_when: ["vitamina K1 baja con INR alto sin anticoagulante"]
```
