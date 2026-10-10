---
doc_id: "SLD-BIO-127"
biomarker_id: "chagas_elisa_recombinante"
name_es: "ELISA de Trypanosoma cruzi con antígenos recombinantes"
name_en: "Trypanosoma cruzi recombinant antigen ELISA"
abbreviation: "ELISA Chagas recombinante"
sinonimos: ["ELISA recombinante Chagas", "Segunda ELISA Chagas", "Chagas antígenos recombinantes", "T. cruzi ELISA recombinante"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice"
specimen: "Suero de la misma toma"
nivel_catalogo: "refleja"
panel: "refleja"
activa_si: ["chagas_elisa_total reactivo"]
alimenta: ["COND-M4-IN-003"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-127 · Segunda ELISA de Chagas (antígenos recombinantes)

## A. Identificación
Segunda prueba del algoritmo serológico, con antígenos distintos a los de la primera ELISA.

## B. Definición
El diagnóstico serológico de Chagas exige dos pruebas con antígenos o principios distintos; esta es la segunda.

## C. Espécimen y toma
Suero de la misma muestra.

## D. Intervalos y umbrales
Reactivo o no reactivo según el fabricante.

## E. Interpretación
Las dos reactivas: probable infección crónica. Discordantes: se necesita una tercera prueba y el informe queda en espera.

## F. Contexto del paciente y confusores
Reacción cruzada con *Leishmania*.

## G. Relaciones
Primera ELISA (SLD-BIO-109).

## H. Tendencias
No aplica.

## I. Prevención
La de la ficha de la primera ELISA.

## J. Pruebas complementarias
Tercera prueba en discordancia; evaluación cardíaca si las dos son reactivas.

## K. Cuándo no interpretar / cuándo escalar
Las dos reactivas: escalamiento 2 con llamada (IN-003).

## L. Evidencia
Algoritmo de Chagas del Ministerio de Salud; lineamiento del INS para adultos pendiente.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "segunda prueba para Chagas reactiva o no reactiva".
- Inferencias prohibidas: daño cardíaco, mortal.
- Revisión profesional: todo resultado.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, chagas, serologia, refleja, saludly_brain_v1]
use_when: ["primera ELISA de Chagas reactiva"]
combine_with: [chagas_elisa_total]
do_not_use_alone: []
do_not_conclude: ["cardiopatía chagásica"]
escalate_when: ["dos ELISA reactivas", "resultados discordantes"]
```
