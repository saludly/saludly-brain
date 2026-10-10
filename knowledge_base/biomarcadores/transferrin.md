---
doc_id: SLD-BIO-078
biomarker_id: transferrin
name_es: Transferrina
name_en: Transferrin
abbreviation: TRF
sinonimos:
- Transferrina
- TRF
- Transferrin
category: iron_micronutrients
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-014
combine_with:
- serum_iron
- transferrin_saturation
- ferritin
tier: 2
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Transferrina

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-014. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-078. TRF. Categoría: Hierro/Micronutrientes. Tipo: analito medido (usada como variable para calcular saturación de transferrina, junto con o en lugar de TIBC medida directamente). Tier 2.

## B. Definición

Proteína de transporte de hierro sintetizada por el hígado. Su síntesis aumenta cuando las reservas de hierro están bajas (mecanismo compensatorio) y disminuye en inflamación crónica y hepatopatía — es, en cierto sentido, un espejo inverso de la ferritina.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método inmunoturbidimétrico. Unidad: mg/dL. No requiere ayuno estricto (aunque se solicita junto a hierro sérico, que sí se beneficia de toma matutina). Factor preanalítico: embarazo y uso de anticonceptivos orales elevan la transferrina fisiológicamente.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal **215-365 mg/dL (2.15-3.65 g/L)**.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Elevada:** deficiencia de hierro (respuesta compensatoria — el cuerpo produce más transportador cuando hay menos hierro que transportar), embarazo, uso de anticonceptivos orales/estrógenos.
- **Disminuida:** inflamación crónica (reactante de fase aguda negativo, igual que albúmina), hepatopatía (síntesis reducida), desnutrición, síndrome nefrótico (pérdida).

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: embarazo, uso de anticonceptivos orales/terapia hormonal, proceso inflamatorio/infeccioso activo, función hepática.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Hierro sérico (obligatorio, para calcular saturación de transferrina), Ferritina.
- `pattern_examples`: transferrina alta + hierro bajo + saturación baja = deficiencia de hierro clásica; transferrina baja + hierro bajo + ferritina normal/alta = más compatible con anemia de enfermedad crónica/inflamación que con deficiencia real.
- `cannot_conclude`: estado de reservas de hierro sin el resto del perfil.

## H. Tendencias

### Tendencias temporales

Cambia de forma más lenta y predecible que el hierro sérico — más útil que este último como indicador de tendencia, aunque menos estable que ferritina.

## I. Prevención

Utilidad como parte del perfil de hierro completo, especialmente para diferenciar deficiencia real de anemia de enfermedad crónica.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Hierro sérico (si no se solicitó junto), Ferritina, hs-CRP (para contextualizar inflamación).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstico aislado — su valor está en la combinación con hierro sérico para calcular saturación de transferrina.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar sobre metabolismo del hierro.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "transferrina alterada, interpretar junto a hierro sérico (saturación) y ferritina para diferenciar deficiencia real de anemia de enfermedad crónica".
- **prohibited_inferences:** diagnóstico de deficiencia de hierro a partir de transferrina aislada.
- **uncertainty_notes:** afectada por embarazo y anticonceptivos hormonales — considerar siempre este contexto antes de interpretar como alteración del metabolismo del hierro.
- **professional_review:** patrón combinado con hierro sérico y ferritina sugestivo de deficiencia significativa o de anemia de enfermedad crónica sin causa clara.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - iron_metabolism
  - anemia_workup
  - tier_2
  - saludly_brain_v1

use_when:
  - "diferenciando deficiencia de hierro real de anemia de enfermedad crónica"

combine_with: [serum_iron, transferrin_saturation, ferritin]

do_not_use_alone:
  - "diagnóstico de deficiencia de hierro"

do_not_conclude:
  - "estado de reservas de hierro sin el resto del perfil"

escalate_when:
  - "patrón combinado sugestivo de deficiencia significativa o anemia de enfermedad crónica sin causa clara"
```
