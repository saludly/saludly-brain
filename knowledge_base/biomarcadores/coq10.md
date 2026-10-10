---
doc_id: "SLD-BIO-120"
biomarker_id: "coq10"
name_es: "Coenzima Q10"
name_en: "Coenzyme Q10"
abbreviation: "CoQ10"
sinonimos: ["Coenzima Q10", "CoQ10", "Ubiquinona", "Ubiquinol"]
category: "Nutrientes"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µg/mL"
specimen: "Plasma o suero en ayunas, protegido de la luz"
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

# SLD-BIO-120 · Coenzima Q10

> **Decisión del 10 de octubre de 2026.** Retirada del panel base el 10 de octubre de 2026 (aprobación de Carlos): es una prueba especializada que no ofrecen los laboratorios clínicos comunes o que exige transporte especial, y ni Function Health ni Superpower la incluyen en su panel base. La ficha se conserva: si el resultado llega, se interpreta igual.

## A. Identificación
Coenzima Q10 total en plasma por HPLC.

## B. Definición
Molécula que el cuerpo produce y que participa en la producción de energía de las células. No es una vitamina en sentido estricto.

## C. Espécimen y toma
Plasma o suero en ayunas, protegido de la luz.

## D. Intervalos y umbrales
El laboratorio de ejemplo no reporta intervalo ("No establecido").

## E. Interpretación
Viaja con el colesterol LDL, así que baja cuando baja el LDL. Las estatinas reducen la CoQ10 en sangre; no está establecido que eso explique los síntomas musculares ni que suplementar los mejore.

## F. Contexto del paciente y confusores
Estatinas, LDL bajo o alto, suplementos.

## G. Relaciones
LDL (M1), CK si hay síntomas musculares con estatinas (SEG-007).

## H. Tendencias
Sin uso de seguimiento en prevención.

## I. Prevención y alimentos
Carnes, pescados grasos y vísceras aportan algo; el cuerpo produce la mayor parte.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
Solo valor. Los suplementos pueden disminuir el efecto de la warfarina: con anticoagulante, escalamiento 1 y sugerencia de consulta.

## L. Evidencia
Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "valor informativo de coenzima Q10".
- Inferencias prohibidas: recomendar suspender estatinas, dosis de suplemento, déficit.
- Revisión profesional: suplemento con warfarina.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [nutrientes, coq10, solo_informativo, panel_estandar, saludly_brain_v1]
use_when: ["valor de coenzima Q10", "estatinas con síntomas musculares"]
combine_with: [ldl_c, ck_cpk]
do_not_use_alone: ["explicar síntomas musculares"]
do_not_conclude: ["deficiencia de CoQ10", "miopatía por estatinas"]
escalate_when: ["suplemento de CoQ10 con warfarina"]
```
