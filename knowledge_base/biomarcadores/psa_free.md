---
doc_id: "SLD-BIO-129"
biomarker_id: "psa_free"
name_es: "Antígeno prostático específico libre"
name_en: "Free prostate-specific antigen"
abbreviation: "PSA libre"
sinonimos: ["PSA libre", "fPSA", "Antígeno prostático libre", "PSA L"]
category: "Salud del hombre"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
calculo_asociado: "porcentaje de PSA libre = PSA libre / PSA total x 100"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja, hombres"
activa_si: ["psa_total entre 4,0 y 10,0 ng/mL"]
alimenta: ["COND-M5-UR-A02"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-129 · PSA libre

## A. Identificación
Fracción del PSA que circula sin unirse a proteínas.

## B. Definición
En la zona gris del PSA total, un porcentaje de PSA libre bajo se asocia a mayor probabilidad de cáncer y uno alto a causas benignas.

## C. Espécimen y toma
Suero de la misma toma, procesado pronto: el PSA libre es menos estable que el total.

## D. Intervalos y umbrales
El corte del porcentaje está pendiente de fuente en el Lote 5. Valores habituales en la literatura: menor de 10 % (mayor probabilidad) y mayor de 25 % (menor probabilidad). Sin firma médica, la ficha UR-A02 solo muestra el porcentaje.

## E. Interpretación
Solo en la vista médica; no cambia el texto del paciente.

## F. Contexto del paciente y confusores
Los mismos del PSA total; demora en el procesamiento baja el PSA libre.

## G. Relaciones
PSA total (SLD-BIO-110).

## H. Tendencias
No aplica.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Las del PSA total.

## K. Cuándo no interpretar / cuándo escalar
No escala por sí solo.

## L. Evidencia
Pendiente de fuente.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "dato de apoyo para tu médico".
- Inferencias prohibidas: probabilidad de cáncer en el texto del paciente.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [salud_hombre, prostata, refleja, saludly_brain_v1]
use_when: ["PSA total en zona gris"]
combine_with: [psa_total]
do_not_use_alone: []
do_not_conclude: ["cáncer de próstata"]
escalate_when: []
```
