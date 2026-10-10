---
doc_id: "SLD-BIO-140"
biomarker_id: "anti_ccp"
name_es: "Anticuerpos contra péptido citrulinado cíclico"
name_en: "Anti-cyclic citrullinated peptide antibodies"
abbreviation: "Anti-CCP"
sinonimos: ["Anti-CCP", "Anticuerpos anti péptido citrulinado", "Péptido citrulinado", "Anticitrulina", "ACPA", "Anti-cyclic citrullinated peptide"]
category: "Inmunología"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "U/mL"
activa_si: ["factor reumatoide positivo (opcional; lo decide Saludly con el laboratorio)"]
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja (opcional)"
panel: "refleja, opcional"
alimenta: ["REL-031"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
notas_decision: ["Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre)."]
---

# SLD-BIO-140 · Anticuerpos contra péptido citrulinado cíclico

## A. Identificación
Anticuerpos contra proteínas citrulinadas, más específicos de artritis reumatoide que el factor reumatoide.

## B. Definición
Pueden aparecer años antes de la artritis reumatoide, pero en personas sin síntomas no la diagnostican.

## C. Espécimen y toma
Suero retenido de la misma toma.

## D. Intervalos y umbrales
Se usa el intervalo del laboratorio.

## E. Interpretación
Solo refuerza la señal para vigilar REL-031. Nunca crea una condición por sí solo.

## F. Contexto del paciente y confusores
Tabaquismo.

## G. Relaciones
Factor reumatoide, ANA, VSG, PCR.

## H. Tendencias
Se compara con la toma anterior solo si es del mismo laboratorio.

## I. Prevención
No aplica.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
Positivo con FR positivo: sugerir consulta si hay síntomas articulares.

## L. Evidencia
Criterios ACR/EULAR 2010. Pendiente de verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "un anticuerpo salió positivo; si tienes dolor o inflamación de articulaciones, conviene consultarlo".
- Inferencias prohibidas: "tienes artritis reumatoide".
- Revisión profesional: no requerida, salvo lo que indique la condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [inmunologia, refleja, autoinmunidad, saludly_brain_v1]
use_when: ["FR positivo"]
combine_with: [rheumatoid_factor, ana_hep2]
do_not_use_alone: [anti_ccp]
do_not_conclude: []
escalate_when: []
```
