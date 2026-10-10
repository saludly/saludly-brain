---
doc_id: SLD-BIO-041
biomarker_id: bilirubin_total
name_es: Bilirrubina Total
name_en: Total Bilirubin
abbreviation: BT
sinonimos:
- Bilirrubina total
- BT
- Bilirrubina Total
- Total Bilirubin
category: hepatology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: con patrón
panel: estándar
sexo: ambos
alimenta:
- COND-M4-GA-A01
combine_with:
- bilirubin_direct
- alt
- ast
- ggt
- alp
- hemoglobin
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

# Bilirrubina Total

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-A01. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-041. BT. Categoría: Hepatología. Tipo: analito medido. Tier 2. Nota de auditoría: elimina el duplicado que existía en la lista original del usuario (aparecía en "Metabolismo" e "Hígado").

## B. Definición

Producto de degradación de la hemoglobina. Su fracción total incluye la bilirrubina no conjugada (indirecta, producida por la degradación de eritrocitos) y la conjugada (directa, procesada por el hígado y excretada por vía biliar). Se interpreta siempre junto a la fracción directa (`bilirubin_direct.md`) para determinar el origen del problema.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico (diazo, estandarizado). Unidad: mg/dL. No requiere ayuno, aunque el **ayuno prolongado puede elevar transitoriamente la bilirrubina** (relevante en síndrome de Gilbert, donde el ayuno es un desencadenante conocido de elevación leve). Factor preanalítico: la muestra debe protegerse de la luz (la bilirrubina se degrada por exposición lumínica, afectando la medición).

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold:** la ictericia clínicamente visible suele aparecer con bilirrubina total >2-3 mg/dL — pero el umbral exacto de "requiere evaluación" depende de si el patrón es predominantemente directo o indirecto (ver `bilirubin_direct.md`), no del valor total aislado.

## E. Interpretación

- **Elevada:** hemólisis (predomina fracción indirecta), síndrome de Gilbert (elevación leve, benigna, predomina indirecta, común y frecuentemente un hallazgo incidental sin significado patológico), enfermedad hepatocelular, obstrucción biliar (predomina fracción directa).
- El valor total aislado, sin el desglose en directa/indirecta, tiene interpretación clínica limitada — es el mismo principio que proteínas totales/albúmina.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: ayuno reciente/prolongado, síntomas (ictericia visible, coluria, acolia), antecedente familiar de síndrome de Gilbert, medicamentos hepatotóxicos.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Bilirrubina directa (obligatorio, para calcular la indirecta por diferencia y determinar el patrón), ALT/AST (patrón hepatocelular), GGT/ALP (patrón colestásico), Hemoglobina/Hematocrito (si se sospecha hemólisis).
- `pattern_examples`: bilirrubina total elevada + directa normal (predominio indirecto) + resto del panel hepático normal = patrón compatible con síndrome de Gilbert (benigno) o hemólisis (requiere hemograma); bilirrubina total elevada + directa elevada (predominio directo) + ALP/GGT elevadas = patrón colestásico.
- `cannot_conclude`: diagnóstico específico sin el desglose en fracción directa/indirecta y el resto del panel hepático.

## H. Tendencias

### Tendencias temporales

El síndrome de Gilbert produce fluctuaciones benignas relacionadas con ayuno, estrés o enfermedad intercurrente — una elevación leve fluctuante sin otros hallazgos hepáticos alterados es tranquilizadora, no motivo de alarma repetida.

## I. Prevención

Utilidad principalmente diagnóstica/de orientación — no tiene una acción preventiva independiente propia más allá de las ya mencionadas para el panel hepático general.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Bilirrubina directa (si no se solicitó junto — debe pedirse siempre en conjunto), hemograma completo si se sospecha hemólisis, resto del panel hepático (ALT/AST/GGT/ALP).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es diagnóstica aislada — requiere el desglose directa/indirecta y contexto clínico para orientar hacia causa hemolítica, hepatocelular, colestásica o benigna (Gilbert).

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hepatológico/hematológico estándar sobre el metabolismo de la bilirrubina.
- **Guideline complementaria (misma que el resto del panel hepático):** ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries, 2017. https://journals.lww.com/ajg/fulltext/10.1038/ajg.2016.517~acg-clinical-guideline-evaluation-of-abnormal-liver
- **Clinical decision threshold (verificado esta sesión, múltiples fuentes clínicas concordantes):** rango normal de bilirrubina total **0.1-1.2 mg/dL** (algunas fuentes reportan hasta 0.2-1.0 mg/dL — variación normal entre laboratorios/métodos). Ictericia clínicamente visible generalmente aparece con bilirrubina total **>2.5-3 mg/dL**. **Umbral específico del síndrome de Gilbert (relevante para no generar alarma innecesaria):** elevación de bilirrubina indirecta típicamente en el rango **1.2-3.0 mg/dL**, con el resto del panel hepático (ALT, AST, GGT, ALP) y hemograma completamente normales — patrón considerado diagnóstico o altamente compatible con Gilbert sin necesidad de pruebas genéticas adicionales, y afecta aproximadamente al 5-10% de la población general.
- **URL fuente:** https://mdtools.org/bilirubin-levels ; https://healthmatters.io/understand-blood-test-results/bilirubin-total ; https://emedicine.medscape.com/article/2074068-overview — verificadas esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "bilirrubina total elevada, requiere desglose en fracción directa/indirecta para orientar causa (hemolítica, síndrome de Gilbert benigno, hepatocelular o colestásica)".
- **prohibited_inferences:** cualquier diagnóstico específico a partir del valor total aislado sin el desglose.
- **uncertainty_notes:** el síndrome de Gilbert es una causa frecuente y benigna de elevación leve — Saludly no debe generar alarma desproporcionada ante elevaciones leves aisladas sin otros hallazgos del panel hepático.
- **professional_review:** ictericia clínica visible, elevación marcada, o patrón colestásico/hepatocelular con el resto del panel hepático alterado.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hepatology
  - bilirubin_metabolism
  - tier_2
  - saludly_brain_v1

use_when:
  - "evaluando función hepática o sospecha de hemólisis"
  - "ictericia o coluria referidas por el usuario"

combine_with: [bilirubin_direct, alt, ast, ggt, alp, hemoglobin]

do_not_use_alone:
  - "diagnóstico sin el desglose en fracción directa/indirecta"

do_not_conclude:
  - "enfermedad hepática grave a partir de una elevación leve aislada (posible síndrome de Gilbert benigno)"

escalate_when:
  - "ictericia clínica visible"
  - "patrón colestásico o hepatocelular con resto del panel alterado"
```
