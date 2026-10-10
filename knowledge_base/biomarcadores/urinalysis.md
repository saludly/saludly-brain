---
doc_id: "SLD-BIO-101"
biomarker_id: "urinalysis"
name_es: "Uroanálisis"
name_en: "Urinalysis"
abbreviation: "UA"
sinonimos: ["Uroanálisis", "Parcial de orina", "Examen general de orina", "Citoquímico de orina", "Orina completa", "Urinalysis"]
category: "Riñón y vías urinarias"
parameter_type: "panel"
tipo_resultado: "cualitativo y semicuantitativo por campo"
unidad_canonica: "por campo (ver D)"
specimen: "Primera orina de la mañana, chorro medio"
nivel_catalogo: "con patrón (hematíes) y solo valor (resto de campos)"
panel: "estándar, todas las personas"
alimenta: ["COND-M2-NE-006", "COND-M4-IN-A01", "SEG-013"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-101 · Uroanálisis (tira y sedimento)

## A. Identificación
Panel de orina con tres partes: examen físico (color, aspecto, densidad), químico por tira reactiva (pH, proteínas, glucosa, cetonas, sangre, nitritos, esterasa leucocitaria, bilirrubina, urobilinógeno) y microscópico del sedimento (leucocitos, hematíes, células epiteliales, bacterias, cilindros, cristales).

## B. Definición
Evalúa de forma general el riñón y las vías urinarias, y da señales indirectas de metabolismo (glucosa, cetonas) e hígado (bilirrubina, urobilinógeno).

## C. Espécimen y toma
Primera orina de la mañana, chorro medio, en frasco estéril. Procesar idealmente en las 2 horas siguientes o refrigerar: la demora deja crecer bacterias y destruye células. No tomar durante la menstruación ni en los 3 días siguientes, ni tras sondaje o procedimiento urológico reciente.

## D. Intervalos y umbrales
| Campo | Esperado | Nota |
| --- | --- | --- |
| Densidad | 1,005 a 1,030 | Refleja hidratación |
| pH | 5,0 a 8,0 | Varía con la dieta |
| Proteínas, glucosa, cetonas, sangre, nitritos, esterasa, bilirrubina | Negativo | La tira de proteínas detecta sobre todo albúmina y no reemplaza la relación albúmina/creatinina |
| Urobilinógeno | 0,2 a 1,0 mg/dL | |
| Leucocitos en sedimento | 0 a 5 por campo | |
| Hematíes en sedimento | 0 a 3 por campo | Más de 3 = microhematuria (AUA, enmienda 2025) |
| Cilindros | No se observan u ocasionales hialinos | |

## E. Interpretación
Cada campo se interpreta junto con la sangre: glucosa en orina con la glucosa sérica, proteína en tira con la albúmina/creatinina, bilirrubina y urobilinógeno con la función hepática. La sangre en la tira solo cuenta si el sedimento confirma hematíes.

## F. Contexto del paciente y confusores
Menstruación, ejercicio intenso en 48 horas, infección urinaria, inhibidores de SGLT2 (glucosa en orina esperada), ayuno prolongado (cetonas), deshidratación (densidad alta), contaminación genital de la muestra (células epiteliales abundantes).

## G. Relaciones
Hematíes con albuminuria o TFG baja sugieren origen glomerular. Nitritos o esterasa solo cuentan como infección con síntomas (IDSA 2019). Glucosa en orina con glucosa sérica alta apoya diabetes.

## H. Tendencias
La microhematuria de bajo riesgo se repite a los 6 meses; la persistencia cambia la conducta.

## I. Prevención
Hidratación adecuada. Sin otras recomendaciones específicas del uroanálisis.

## J. Pruebas complementarias
Relación albúmina/creatinina (en el panel), urocultivo (lo pide el médico), citología o estudio urológico según riesgo.

## K. Cuándo no interpretar / cuándo escalar
No interpretar hematuria con menstruación. No reportar bacteriuria sin síntomas fuera del embarazo. Escalar según NE-006 (hematuria) y SEG-013 (resto de campos).

## L. Evidencia
AUA/SUFU 2020 con enmienda 2025 (microhematuria), IDSA 2019 (bacteriuria asintomática), KDIGO 2024. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "campo alterado que conviene repetir o revisar con el médico".
- Inferencias prohibidas: infección sin síntomas, cáncer, cálculos, enfermedad renal a partir de la tira.
- Revisión profesional: según las fichas de condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [renal, urinario, uroanalisis, panel_estandar, saludly_brain_v1]
use_when: ["interpretar microhematuria", "contexto de infección urinaria con síntomas", "glucosa o proteína en orina"]
combine_with: [uacr, egfr, glucose, bilirubin_total]
do_not_use_alone: ["diagnóstico de infección sin síntomas", "evaluación renal sin albúmina/creatinina"]
do_not_conclude: ["cáncer de vías urinarias", "litiasis"]
escalate_when: ["microhematuria con albuminuria o TFG baja", "cetonas con glucosa alta", "bilirrubina en orina positiva"]
```
