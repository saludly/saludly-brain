---
doc_id: "SLD-BIO-110"
biomarker_id: "psa_total"
name_es: "Antígeno prostático específico total"
name_en: "Total prostate-specific antigen"
abbreviation: "PSA"
sinonimos: ["PSA", "PSA total", "Antígeno prostático específico", "APE", "Antígeno prostático total"]
category: "Salud del hombre"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, hombres, con consentimiento"
alimenta: ["COND-M5-UR-001"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-110 · Antígeno prostático específico total (PSA)

## A. Identificación
Inmunoensayo de una proteína producida por la próstata.

## B. Definición
Sube con el cáncer de próstata, pero también con el crecimiento benigno de la próstata, la inflamación, la infección y algunas actividades. Es una prueba de tamizaje, no de diagnóstico.

## C. Espécimen y toma
Suero. Evitar eyaculación y bicicleta en las 48 horas previas. Requiere el consentimiento de la visita, que explica riesgos y beneficios (Res. 3280).

## D. Intervalos y umbrales
Corte tradicional: 4,0 ng/mL, o el límite que declare el laboratorio. Zona gris: 4,0 a 10,0 ng/mL, en la que se corre PSA libre como refleja. Existen intervalos por edad, que el médico puede preferir.

## E. Interpretación
De 50 a 75 años se lee como tamizaje formal; fuera de esa edad, como valor a revisar con el médico. Con finasterida o dutasterida, el valor medido se multiplica por 2.

## F. Contexto del paciente y confusores
Eyaculación o ciclismo en 48 horas, prostatitis, infección urinaria, sondaje reciente, inhibidores de 5-alfa reductasa, testosterona exógena.

## G. Relaciones
PSA libre (refleja) en zona gris; infección urinaria con síntomas (M4 IN-A01) como causa de elevación.

## H. Tendencias
La velocidad de cambio entre tomas importa más que un valor aislado cercano al corte.

## I. Prevención
Conversación informada con el médico sobre el tamizaje.

## J. Pruebas complementarias
Tacto rectal, PSA libre, resonancia o biopsia según el médico.

## K. Cuándo no interpretar / cuándo escalar
Sin consentimiento, no se mide. Escalamiento según UR-001.

## L. Evidencia
Res. 3280 de 2018, AUA/SUO 2026. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "PSA por encima del valor de referencia; tiene varias causas, la mayoría benignas".
- Inferencias prohibidas: cáncer, tumor, necesidad de biopsia.
- Revisión profesional: PSA elevado en edad de tamizaje o mayor de 10 ng/mL.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [salud_hombre, prostata, tamizaje, panel_estandar, saludly_brain_v1]
use_when: ["PSA total", "tamizaje de próstata por edad"]
combine_with: [psa_free, urinalysis]
do_not_use_alone: ["diagnóstico de cáncer de próstata"]
do_not_conclude: ["cáncer", "hiperplasia prostática"]
escalate_when: ["PSA elevado de 50 a 75 años", "PSA mayor de 10 ng/mL"]
```
