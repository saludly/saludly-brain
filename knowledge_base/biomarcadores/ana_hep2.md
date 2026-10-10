---
doc_id: "SLD-BIO-111"
biomarker_id: "ana_hep2"
name_es: "Anticuerpos antinucleares por inmunofluorescencia indirecta en células HEp-2"
name_en: "Antinuclear antibodies by indirect immunofluorescence on HEp-2 cells"
abbreviation: "ANA"
sinonimos: ["ANA", "Anticuerpos antinucleares", "AAN", "ANA IFI", "ANA HEp-2", "FAN"]
category: "Inmunología"
parameter_type: "measured_analyte"
tipo_resultado: "semicuantitativo (título y patrón ICAP)"
unidad_canonica: "título (1:x) y patrón (AC-xx)"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M6-RE-A01"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-111 · Anticuerpos antinucleares por IFI en HEp-2 (ANA)

## A. Identificación
Inmunofluorescencia indirecta sobre células HEp-2, con resultado en título (diluciones 1:80, 1:160, 1:320 y mayores) y patrón según la nomenclatura internacional ICAP (por ejemplo, AC-2 moteado fino denso, AC-4 moteado fino).

## B. Definición
Detecta anticuerpos contra componentes del núcleo celular. Están presentes en casi todas las personas con lupus, pero también en una parte importante de la población sana.

## C. Espécimen y toma
Suero, sin ayuno específico. El laboratorio debe reportar título y patrón; un "positivo" sin título no es interpretable.

## D. Intervalos y umbrales
Negativo: menos de 1:80. Los criterios EULAR/ACR 2019 usan 1:80 o más solo como puerta de entrada para lupus, junto con criterios clínicos. Cerca del 14 % de la población general tiene ANA positivo (Satoh 2012).

## E. Interpretación
A mayor título, mayor probabilidad de que se asocie a enfermedad, pero ningún título diagnostica por sí solo. El patrón AC-2 (moteado fino denso) se asocia con frecuencia a personas sanas.

## F. Contexto del paciente y confusores
Edad (más frecuente en mayores), sexo femenino, infecciones virales recientes, algunos medicamentos, enfermedad tiroidea autoinmune.

## G. Relaciones
Anti-TPO positivo o TSH alta (M2) se asocian a ANA positivo; la vista médica los cruza.

## H. Tendencias
Puede mantenerse positivo por años sin enfermedad; no se usa para seguimiento.

## I. Prevención
No aplica.

## J. Pruebas complementarias
Anti-ENA, anti-ADN de doble cadena y complemento, según el médico y los síntomas.

## K. Cuándo no interpretar / cuándo escalar
Positivo sin título o sin patrón: no interpretable. Escalamiento según RE-A01 (1:80, nivel 1; 1:160 o más, nivel 2).

## L. Evidencia
Satoh 2012 (prevalencia), criterios EULAR/ACR 2019, nomenclatura ICAP. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "ANA positivo es frecuente en personas sanas; se comenta con el médico, sobre todo si hay síntomas".
- Inferencias prohibidas: lupus, enfermedad autoinmune, "tu sistema inmune te ataca".
- Revisión profesional: 1:160 o más.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [inmunologia, autoinmunidad, ana, panel_estandar, saludly_brain_v1]
use_when: ["ANA positivo o negativo"]
combine_with: [anti_tpo, tsh, esr, hs_crp]
do_not_use_alone: ["diagnóstico de enfermedad autoinmune"]
do_not_conclude: ["lupus", "artritis reumatoide"]
escalate_when: ["título de 1:160 o más", "ANA positivo con síntomas declarados"]
```
