---
doc_id: "SLD-BIO-116"
biomarker_id: "biotin"
name_es: "Biotina (vitamina B7)"
name_en: "Biotin (vitamin B7)"
abbreviation: "B7"
sinonimos: ["Biotina", "Vitamina B7", "Vitamina H", "Biotin"]
category: "Vitaminas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/L"
specimen: "Suero"
nivel_catalogo: "vitamina"
panel: "fuera del panel base"
alimenta: ["COND-M3-NU-A04", "regla de interferencia de biotina (documento 04)"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-116 · Biotina (vitamina B7)

> **Decisión del 10 de octubre de 2026.** Retirada del panel base el 10 de octubre de 2026 (aprobación de Carlos): es una prueba especializada que no ofrecen los laboratorios clínicos comunes o que exige transporte especial, y ni Function Health ni Superpower la incluyen en su panel base. La ficha se conserva: si el resultado llega, se interpreta igual. La regla de interferencia de la biotina se mantiene con la pregunta al paciente "¿tomas biotina?".

## A. Identificación
Biotina en suero por inmunoensayo.

## B. Definición
Vitamina hidrosoluble del grupo B. Su importancia en el panel no es el déficit, que es raro, sino el exceso: los suplementos para cabello, piel y uñas traen dosis muy altas que alteran muchos inmunoensayos.

## C. Espécimen y toma
Suero. La enfermera pregunta si toma suplementos de biotina o "para el cabello y las uñas" y cuándo fue la última dosis.

## D. Intervalos y umbrales
El laboratorio de ejemplo no reporta intervalo ("No establecido"); el laboratorio aliado debe confirmar si lo tiene.

## E. Interpretación
Biotina alta, o suplemento declarado, invalida la interpretación de TSH, T4 libre, T3 total, anticuerpos tiroideos, B12, folato, IGF-1 y otros inmunoensayos hasta repetirlos sin el suplemento. Según el método, puede dar valores falsamente altos o bajos y puede imitar un hipertiroidismo.

## F. Contexto del paciente y confusores
Suplementos de belleza, multivitamínicos, dosis altas por indicación médica.

## G. Relaciones
Todas las pruebas por inmunoensayo del panel.

## H. Tendencias
Baja en pocos días al suspender el suplemento.

## I. Prevención y alimentos
Huevo cocido, nueces y semillas. La clara de huevo cruda reduce su absorción.

## J. Pruebas complementarias
Repetir las pruebas afectadas sin el suplemento.

## K. Cuándo no interpretar / cuándo escalar
Biotina alta o suplemento declarado: bloquea las pruebas afectadas (escalamiento 1, repetir). Sin intervalo del laboratorio, la regla depende solo del cuestionario.

## L. Evidencia
Advertencia de la FDA sobre interferencia de biotina en pruebas de laboratorio. Por verificar.

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "la biotina puede alterar algunos de tus resultados; hay que repetirlos sin el suplemento".
- Inferencias prohibidas: interpretar tiroides u otras pruebas afectadas con biotina alta.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [vitaminas, interferencia, biotina, inmunoensayo, panel_estandar, saludly_brain_v1]
use_when: ["biotina alta", "suplemento de biotina declarado", "resultados de tiroides incongruentes"]
combine_with: [tsh, free_t4, total_t3, vitamin_b12, folate, igf1]
do_not_use_alone: []
do_not_conclude: ["deficiencia de biotina"]
escalate_when: ["biotina alta con resultados de tiroides alterados"]
```
