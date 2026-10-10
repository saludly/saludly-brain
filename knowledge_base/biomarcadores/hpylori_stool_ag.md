---
doc_id: "SLD-BIO-103"
biomarker_id: "hpylori_stool_ag"
name_es: "Antígeno de Helicobacter pylori en heces"
name_en: "Helicobacter pylori stool antigen"
abbreviation: "HpSA"
sinonimos: ["Antígeno H. pylori en heces", "H. pylori antígeno fecal", "Helicobacter pylori Ag heces", "HpSA"]
category: "Digestivo"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (positivo / negativo)"
unidad_canonica: "cualitativo"
specimen: "Heces, misma muestra que FIT y coprológico"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M4-GA-005"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-103 · Antígeno de *H. pylori* en heces

## A. Identificación
Detecta antígenos de *H. pylori* en heces con anticuerpos monoclonales. Indica infección activa, a diferencia de la serología en sangre, que puede quedar positiva tras la curación.

## B. Definición
*H. pylori* es una bacteria del estómago muy frecuente en Colombia, asociada a gastritis, úlcera y cáncer gástrico. La guía colombiana de 2025 recomienda tratar a todo adulto con infección activa.

## C. Espécimen y toma
Heces frescas o refrigeradas, de la misma muestra domiciliaria. Para evitar falsos negativos: sin inhibidores de bomba de protones en las 2 semanas previas ni antibióticos o bismuto en las 4 semanas previas.

## D. Intervalos y umbrales
Cualitativo; el corte lo define el fabricante. La prueba de aliento con urea C13 es la referencia no invasiva; el antígeno fecal monoclonal es la opción disponible en toma domiciliaria y su limitación se escribe en el informe.

## E. Interpretación
Positivo: infección activa probable. Negativo: sin infección activa, salvo uso reciente de inhibidores de bomba o antibióticos.

## F. Contexto del paciente y confusores
Inhibidores de bomba, antibióticos, bismuto, sangrado digestivo alto activo, heces muy líquidas.

## G. Relaciones
Puede explicar déficit de hierro (M3) y se lee con la sangre oculta en la vista médica.

## H. Tendencias
Tras tratamiento, el control se hace al menos 4 semanas después de terminar antibióticos.

## I. Prevención
Agua segura e higiene de manos; consulta para tratamiento.

## J. Pruebas complementarias
Prueba de aliento con urea C13; endoscopia según síntomas y edad.

## K. Cuándo no interpretar / cuándo escalar
Negativo con medicamentos recientes: no concluyente. Positivo: escalamiento 2 (GA-005).

## L. Evidencia
Asociación Colombiana de Gastroenterología 2025. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "infección activa probable por *H. pylori*; las guías colombianas recomiendan tratarla".
- Inferencias prohibidas: úlcera, gastritis, cáncer gástrico; recomendar antibióticos.
- Revisión profesional: todo positivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [digestivo, infeccioso, h_pylori, panel_estandar, saludly_brain_v1]
use_when: ["antígeno de H. pylori positivo o negativo", "déficit de hierro sin causa"]
combine_with: [ferritin, hemoglobin, fit_stool]
do_not_use_alone: ["descartar infección con inhibidores de bomba recientes"]
do_not_conclude: ["úlcera", "cáncer gástrico"]
escalate_when: ["resultado positivo"]
```
