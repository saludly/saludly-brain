---
doc_id: "SLD-BIO-122"
biomarker_id: "mch"
name_es: "Hemoglobina corpuscular media"
name_en: "Mean corpuscular hemoglobin"
abbreviation: "HCM"
sinonimos: ["HCM", "MCH", "Hemoglobina corpuscular media", "Hb corpuscular media"]
category: "Hematología"
parameter_type: "derived_index"
tipo_resultado: "numérico"
unidad_canonica: "pg"
specimen: "Sangre total EDTA"
nivel_catalogo: "solo valor y rango (apoyo de condiciones)"
panel: "estándar, todas las personas"
alimenta: ["COND-M3-HE-002", "SEG-012"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-122 · Hemoglobina corpuscular media (HCM)

## A. Identificación
Índice del hemograma: hemoglobina / recuento de eritrocitos × 10.

## B. Definición
Cantidad promedio de hemoglobina en cada glóbulo rojo.

## C. Espécimen y toma
Sangre total EDTA, la del hemograma.

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 27,0 a 33,0 pg).

## E. Interpretación
Baja: glóbulos rojos con poca hemoglobina, típico del déficit de hierro y de los rasgos talasémicos. Alta: glóbulos rojos grandes (déficit de B12 o folato, alcohol, hipotiroidismo). Acompaña al VCM; casi nunca aporta algo que el VCM no diga.

## F. Contexto del paciente y confusores
Lipemia o leucocitos muy altos pueden falsear el cálculo.

## G. Relaciones
VCM, hemoglobina, RDW, ferritina (M3).

## H. Tendencias
Se normaliza al corregir la causa.

## I. Prevención
La de la causa.

## J. Pruebas complementarias
Las de la anemia (M3).

## K. Cuándo no interpretar / cuándo escalar
No escala sola (SEG-012).

## L. Evidencia
Hematología básica. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "dato de apoyo del hemograma".
- Inferencias prohibidas: talasemia o anemia por HCM aislada.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [hematologia, hemograma, indice_eritrocitario, panel_estandar, saludly_brain_v1]
use_when: ["apoyo en anemia"]
combine_with: [mcv, hemoglobin, rdw, ferritin]
do_not_use_alone: ["clasificar anemia"]
do_not_conclude: ["talasemia"]
escalate_when: []
```
