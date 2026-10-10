---
doc_id: "SLD-BIO-102"
biomarker_id: "fit_stool"
name_es: "Sangre oculta en heces inmunoquímica"
name_en: "Fecal immunochemical test"
abbreviation: "FIT"
sinonimos: ["Sangre oculta en heces", "SOH", "SOMF inmunoquímica", "Prueba inmunoquímica fecal", "FIT", "iFOBT"]
category: "Digestivo"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (positivo / negativo)"
unidad_canonica: "cualitativo"
specimen: "Heces, una muestra"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M4-GA-004"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-102 · Sangre oculta en heces inmunoquímica (FIT)

## A. Identificación
Detecta hemoglobina humana en las heces con anticuerpos específicos. Es la prueba de tamizaje colorrectal que define la Res. 3280 para personas de 50 a 75 años.

## B. Definición
Busca sangrado del colon que no se ve a simple vista. Al ser inmunoquímica, detecta hemoglobina humana y no reacciona con la carne de la dieta.

## C. Espécimen y toma
Una muestra de heces con el kit del laboratorio, en casa, el mismo día de la visita. A diferencia de la prueba de guayaco, no exige dieta previa. Conservar según el fabricante; la hemoglobina se degrada con el calor y el tiempo.

## D. Intervalos y umbrales
Resultado cualitativo. El corte de positividad lo fija el fabricante (suele expresarse en ng de hemoglobina por mL de buffer) y debe constar en el informe del laboratorio.

## E. Interpretación
Positivo: hay sangre en el tubo digestivo bajo y se necesita colonoscopia; no es un diagnóstico de cáncer, y las causas benignas son frecuentes. Negativo: no descarta pólipos ni cáncer, por eso el tamizaje se repite cada 2 años.

## F. Contexto del paciente y confusores
Hemorroides o fisuras con sangrado, menstruación (contaminación), antiinflamatorios o anticoagulantes (no anulan un positivo). Edad y antecedente familiar de cáncer colorrectal para la vista médica.

## G. Relaciones
Con anemia o déficit de hierro (M3), refuerza la necesidad de colonoscopia.

## H. Tendencias
Un negativo vale para 2 años en el tamizaje formal.

## I. Prevención
Alimentación con fibra, actividad física, menos carnes procesadas y alcohol.

## J. Pruebas complementarias
Colonoscopia ante cualquier positivo.

## K. Cuándo no interpretar / cuándo escalar
Un positivo no se repite para "confirmar": va a colonoscopia (escalamiento 2, GA-004).

## L. Evidencia
Res. 3280 de 2018, USPSTF 2021. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "sangre oculta positiva; requiere colonoscopia".
- Inferencias prohibidas: cáncer, pólipos, repetir la prueba en vez de colonoscopia.
- Revisión profesional: todo positivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [digestivo, colorrectal, tamizaje, panel_estandar, saludly_brain_v1]
use_when: ["sangre oculta positiva o negativa", "tamizaje colorrectal por edad"]
combine_with: [hemoglobin, ferritin]
do_not_use_alone: ["descartar cáncer colorrectal"]
do_not_conclude: ["cáncer", "pólipos"]
escalate_when: ["cualquier resultado positivo"]
```
