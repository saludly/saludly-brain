---
doc_id: "SLD-BIO-130"
biomarker_id: "methylmalonic_acid"
name_es: "Ácido metilmalónico sérico"
name_en: "Serum methylmalonic acid"
abbreviation: "AMM"
sinonimos: ["Ácido metilmalónico", "AMM", "MMA", "Methylmalonic acid"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "µmol/L"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["vitamin_b12 entre 180 y 350 pg/mL"]
alimenta: ["COND-M3-NU-001", "COND-M3-HE-004"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-130 · Ácido metilmalónico

## A. Identificación
Metabolito que se acumula cuando falta B12 dentro de las células. Se mide por LC-MS/MS.

## B. Definición
Es un marcador funcional: muestra si la B12 alcanza a hacer su trabajo, más allá del valor total en sangre.

## C. Espécimen y toma
Suero de la misma toma.

## D. Intervalos y umbrales
Intervalo del laboratorio (en el PDF de ejemplo, 0,00 a 0,40 µmol/L).

## E. Interpretación
Alto con B12 indeterminada: déficit funcional de B12 (NU-001). Normal: la B12 indeterminada no se interpreta como déficit.

## F. Contexto del paciente y confusores
Función renal baja (sube el ácido metilmalónico sin déficit de B12), edad avanzada, deshidratación.

## G. Relaciones
B12, homocisteína, TFG (M2, M3).

## H. Tendencias
Baja al corregir el déficit.

## I. Prevención
La de la B12.

## J. Pruebas complementarias
Homocisteína (en el panel).

## K. Cuándo no interpretar / cuándo escalar
Con TFG menor de 60: interpretar con cautela y anotarlo en la vista médica.

## L. Evidencia
NICE NG239 2024. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "confirma o descarta un déficit funcional de B12".
- Inferencias prohibidas: anemia perniciosa.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, b12, marcador_funcional, refleja, saludly_brain_v1]
use_when: ["B12 entre 180 y 350"]
combine_with: [vitamin_b12, homocysteine, egfr]
do_not_use_alone: []
do_not_conclude: ["anemia perniciosa"]
escalate_when: []
```
