---
doc_id: "SLD-BIO-133"
biomarker_id: "phenoage"
name_es: "Edad biológica (PhenoAge)"
name_en: "Phenotypic age (PhenoAge)"
abbreviation: "PhenoAge"
sinonimos: ["Edad biológica", "PhenoAge", "Edad fenotípica", "Phenotypic age"]
category: "Envejecimiento"
parameter_type: "calculated"
tipo_resultado: "numérico"
unidad_canonica: "años"
formula: "Levine et al. 2018 (ver ficha COND-M6-MI-A02)"
entradas: ["albumin", "creatinine", "glucose", "hs_crp", "lymphocytes_pct", "mcv", "rdw", "alp", "wbc", "edad"]
specimen: "No aplica (calculado)"
nivel_catalogo: "solo valor (pantalla aparte)"
panel: "calculado, todas las personas"
alimenta: ["COND-M6-MI-A02"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "coeficientes tomados de una implementación pública que cita el artículo; verificar contra el artículo original"
---

# SLD-BIO-133 · Edad biológica (PhenoAge)

## A. Identificación
Estimación de la edad cuyo riesgo de mortalidad corresponde al de la persona, a partir de la edad y 9 analitos del panel.

## B. Definición
Modelo publicado por Levine y colaboradores en 2018, entrenado en población de EE. UU. (NHANES III). No tiene validación conocida en Colombia y no es un criterio clínico.

## C. Cálculo y condiciones
Unidades del modelo: albúmina en g/L, creatinina en µmol/L, glucosa en mmol/L, PCR en mg/dL (en logaritmo natural), linfocitos en %, VCM en fL, RDW en %, fosfatasa alcalina en U/L, leucocitos en 10³/µL y edad en años. La fórmula completa está en la ficha COND-M6-MI-A02. Se calcula solo con los 9 analitos medidos, glucosa en ayunas, edad de 20 años o más y sin embarazo.

## D. Intervalos y umbrales
No tiene intervalo: se muestra la edad biológica, la edad cronológica y la diferencia.

## E. Interpretación
Una edad biológica menor que la cronológica sugiere un perfil de riesgo más favorable que el promedio de la población del modelo, y viceversa. Su valor real está en la tendencia entre tomas.

## F. Contexto del paciente y confusores
Anemia (sube el RDW), infección reciente o hs-CRP mayor de 10 mg/L (sube PCR y leucocitos), hiperglucemia puntual. En esos casos se calcula con advertencia.

## G. Relaciones
Sus 9 analitos; ninguna condición depende de ella.

## H. Tendencias
Se compara con la toma siguiente; es el uso que más motiva.

## I. Prevención
Mejora con los mismos hábitos que mejoran sus componentes: control de la glucosa, actividad física, menos inflamación.

## J. Pruebas complementarias
No aplica.

## K. Cuándo no interpretar / cuándo escalar
No escala nunca (escalamiento 0).

## L. Evidencia
Levine ME, Lu AT, Quach A y otros. An epigenetic biomarker of aging for lifespan and healthspan. Aging. 2018;10(4):573-591.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "estimación de un modelo científico, útil para seguir en el tiempo".
- Inferencias prohibidas: expectativa de vida, "tu cuerpo tiene X años", envejecimiento acelerado sin segunda medición.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [envejecimiento, calculado, edad_biologica, pantalla_aparte, saludly_brain_v1]
use_when: ["pantalla de edad biológica", "objetivo envejecer de forma saludable"]
combine_with: [albumin, creatinine, glucose, hs_crp, lymphocytes_pct, mcv, rdw, alp, wbc]
do_not_use_alone: ["conclusiones clínicas"]
do_not_conclude: ["expectativa de vida", "envejecimiento acelerado sin segunda medición"]
escalate_when: []
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Los 9 analitos del PDF | 44,3 años |
| PDF mujer 34 años | Los 9 analitos del PDF, con anemia | 34,1 años, con advertencia por anemia |
| Falta un analito | Sin fosfatasa alcalina | No se calcula |
