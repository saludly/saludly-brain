---
doc_id: SLD-BIO-109
biomarker_id: chagas_elisa_total
name_es: Anticuerpos IgG contra Trypanosoma cruzi (ELISA de antígenos totales)
name_en: Trypanosoma cruzi IgG ELISA (whole antigen)
abbreviation: ELISA Chagas
sinonimos:
- ELISA Chagas
- Anticuerpos T. cruzi
- Chagas IgG
- Serología para Chagas
- Trypanosoma cruzi anticuerpos
- Anticuerpos IgG Trypanosoma cruzi (Chagas)
- Anticuerpos IgG Trypanosoma cruzi
category: Infecciosas
parameter_type: measured_analyte
tipo_resultado: cualitativo (reactivo / no reactivo) con índice
unidad_canonica: índice
specimen: Suero
nivel_catalogo: con patrón
panel: estándar, todas las personas, con consentimiento
alimenta:
- COND-M4-IN-003
tier: 2
status: BORRADOR
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: true
source_version: 2026-10
fuentes_estado: por verificar
---

# SLD-BIO-109 · ELISA de *Trypanosoma cruzi* (antígenos totales)

## A. Identificación
Primera prueba del algoritmo serológico de Chagas: ELISA con antígenos totales del parásito.

## B. Definición
Detecta anticuerpos contra *T. cruzi*, el parásito que transmite el pito (triatomino). En la fase crónica la persona puede no tener síntomas por años.

## C. Espécimen y toma
Suero, sin ayuno específico.

## D. Intervalos y umbrales
Reactivo o no reactivo según el índice y el corte del fabricante (por ejemplo, índice menor de 0,90 = no reactivo en el PDF de ejemplo).

## E. Interpretación
Un solo ELISA reactivo no basta: el diagnóstico exige dos pruebas con antígenos distintos. El laboratorio corre la segunda ELISA (antígenos recombinantes) como refleja; si discrepan, se necesita una tercera.

## F. Contexto del paciente y confusores
Reacción cruzada con *Leishmania*; procedencia de municipios endémicos (sube la probabilidad previa).

## G. Relaciones
Sin relaciones de laboratorio; en caso positivo, el médico pide evaluación cardíaca.

## H. Tendencias
Los anticuerpos persisten en la infección crónica.

## I. Prevención
Mejoras de vivienda en zonas endémicas; tamizaje de familiares, sobre todo hijos de madres positivas.

## J. Pruebas complementarias
Segunda ELISA recombinante (refleja), tercera prueba si hay discordancia, electrocardiograma según el médico.

## K. Cuándo no interpretar / cuándo escalar
Un solo reactivo: informe en espera de la segunda ELISA. Dos reactivos: escalamiento 2 con llamada (IN-003).

## L. Evidencia
Algoritmo de Chagas del Ministerio de Salud (pieza para gestantes). Lineamiento del INS para adultos: pendiente.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "pruebas reactivas para Chagas; se confirma con un segundo método".
- Inferencias prohibidas: daño cardíaco, mortal, incurable.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, chagas, serologia, panel_estandar, saludly_brain_v1]
use_when: ["serología de Chagas"]
combine_with: [chagas_elisa_recombinante]
do_not_use_alone: ["diagnóstico de Chagas con una sola prueba"]
do_not_conclude: ["cardiopatía chagásica"]
escalate_when: ["dos pruebas reactivas", "resultado discordante pendiente de tercera prueba"]
```
