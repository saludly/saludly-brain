---
doc_id: "SLD-BIO-137"
biomarker_id: "serum_protein_electrophoresis"
name_es: "Electroforesis de proteínas en suero"
name_en: "Serum protein electrophoresis"
abbreviation: "EFP"
sinonimos: ["Electroforesis de proteínas", "Electroforesis de proteínas en suero", "Proteinograma", "Proteinograma electroforético", "SPEP"]
category: "Inmunología"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo con fracciones"
unidad_canonica: "g/dL por fracción y presencia o no de banda monoclonal"
activa_si: ["globulinas altas o relación A/G menor de 1, o IgG o IgM muy altas (COND-M6-MI-002)"]
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
alimenta: ["COND-M6-MI-002"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-137 · Electroforesis de proteínas en suero

## A. Identificación
Separa las proteínas del suero (albúmina, alfa 1, alfa 2, beta y gamma) y busca una banda monoclonal.

## B. Definición
Una banda monoclonal indica una gammapatía (la mayoría es una gammapatía monoclonal de significado incierto, MGUS); el médico decide el estudio.

## C. Espécimen y toma
Suero retenido de la misma toma.

## D. Intervalos y umbrales
Se usa el informe del laboratorio: banda monoclonal presente o ausente, y su cuantía.

## E. Interpretación
Confirma o descarta COND-M6-MI-002. Un patrón policlonal (aumento difuso de gamma) apunta a inflamación o infección crónica, no a gammapatía.

## F. Contexto del paciente y confusores
Inflamación crónica, hepatitis, enfermedades autoinmunes (patrón policlonal).

## G. Relaciones
Proteínas totales, albúmina, globulinas, A/G, IgG, IgM, calcio, creatinina, hemoglobina.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Inmunofijación y cadenas livianas libres si hay banda (lo pide el médico).

## K. Cuándo no interpretar / cuándo escalar
Banda monoclonal: escalamiento 2 con revisión médica.

## L. Evidencia
IMWG (International Myeloma Working Group). Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "apareció una proteína que conviene estudiar con tu médico".
- Inferencias prohibidas: "tienes mieloma", "tienes cáncer".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [inmunologia, refleja, gammapatia, saludly_brain_v1]
use_when: ["globulinas altas", "A/G baja"]
combine_with: [total_protein, albumin, globulin, ag_ratio, igg, igm]
do_not_use_alone: [serum_protein_electrophoresis]
do_not_conclude: []
escalate_when: []
```
