---
doc_id: SLD-BIO-076
biomarker_id: anti_ttg_iga
name_es: Anti-tTG IgA
name_en: Anti-Tissue Transglutaminase IgA
abbreviation: tTG-IgA
sinonimos:
- Anti-transglutaminasa IgA
- tTG IgA
- Anti-tTG IgA
- Anticuerpos Anti-Transglutaminasa Tisular IgA (Cribado Celíaco)
- tTG-IgA
- Anti-Tissue Transglutaminase IgA
category: Inmunidad
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: U/mL
specimen: Suero
nivel_catalogo: refleja
panel: refleja
sexo: ambos
alimenta:
- COND-M4-GA-006
combine_with:
- iga
- ferritin
- vitamin_b12
- hemoglobin
tier: 3
status: COMPLETO
schema_version: '2.1'
clinical_priority: medium
requires_professional_review: false
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision: []
---

# Anticuerpos Anti-Transglutaminasa Tisular IgA (Anti-tTG IgA)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: COND-M4-GA-006. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-076. tTG-IgA. Categoría: Inmunidad. Tipo: measured_analyte. Tier 3 — indicado ante sospecha clínica, no cribado poblacional general.

## B. Definición

Anticuerpo dirigido contra la transglutaminasa tisular, enzima involucrada en la fisiopatología de la enfermedad celíaca. Es la prueba serológica de primera línea recomendada por ACG (American College of Gastroenterology) 2013 para cribado de enfermedad celíaca en personas ≥2 años con dieta que contiene gluten.

## C. Espécimen y toma

### Examen de laboratorio y espécimen

Sangre venosa (suero) · Método: inmunoensayo (ELISA). **No requiere ayuno** — de hecho, se recomienda mantener una dieta con gluten normal antes de la prueba, ya que la restricción de gluten puede generar falsos negativos.

### Condiciones de toma de muestra

Dieta con gluten normal (crítico — no debe hacerse tras iniciar dieta libre de gluten). **Requiere IgA total normal para ser confiable** (ver `iga.md`) — 2-3% de las personas con enfermedad celíaca tienen deficiencia selectiva de IgA, lo que genera falsos negativos en este ensayo.

## D. Intervalos y umbrales

### Intervalos y umbrales — SEPARADOS explícitamente, con gradiente de probabilidad (evidencia verificada esta sesión, múltiples fuentes concordantes)

- **Negativo:** <4 U/mL (rango consolidado de fuentes concordantes) — baja probabilidad de enfermedad celíaca, aunque no la descarta completamente, especialmente si hay deficiencia de IgA.
- **Positivo débil/equívoco:** 4-10 U/mL — resultado límite, requiere pruebas adicionales (DGP, EMA) o repetición.
- **Positivo:** >10 U/mL — alta probabilidad de enfermedad celíaca, requiere confirmación con biopsia intestinal en la mayoría de protocolos adultos.
- **Umbral de alta confianza diagnóstica (ESPGHAN 2020, población pediátrica, extrapolado con cautela a adultos):** **≥10 veces el límite superior normal**, confirmado con anticuerpos endomisiales (EMA) positivos en una segunda muestra, permite diagnóstico sin biopsia en protocolos pediátricos — en adultos, la biopsia sigue siendo el estándar de confirmación en la mayoría de guías.
- **Sensibilidad/especificidad (Rostom et al., revisión sistemática en *Gastroenterology*, citada ampliamente):** sensibilidad 93-96%, especificidad 97-98% para enfermedad celíaca no tratada.
- **URLs fuente:** https://healthrx.com/labs-celiac-panel/how-to-interpret ; https://healthmatters.io/understand-blood-test-results/t-transglutaminase-ttg-iga ; https://pubmed.ncbi.nlm.nih.gov/23103822/ — todas verificadas esta sesión (ago-2026).

## E. Interpretación

- **Positivo (>10 U/mL):** alta probabilidad de enfermedad celíaca — requiere biopsia duodenal confirmatoria en la mayoría de protocolos adultos.
- **Negativo con IgA total baja:** resultado NO confiable — repetir con Anti-tTG IgG o Anti-DGP.
- **Negativo con IgA total normal:** enfermedad celíaca poco probable, aunque no descarta completamente en casos atípicos.

## F. Contexto del paciente y confusores

### Contexto del paciente

Dieta con gluten al momento de la prueba (crítico), IgA total concurrente (obligatorio), síntomas digestivos, anemia ferropénica inexplicada, antecedente familiar de enfermedad celíaca.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: IgA total (obligatorio, para validar el resultado), Ferritina/Hemoglobina (anemia ferropénica como presentación frecuente), Vitamina B12/Folato (malabsorción asociada).
- `pattern_examples`: tTG-IgA positivo + anemia ferropénica inexplicada + IgA total normal = alta sospecha de enfermedad celíaca, derivar para biopsia confirmatoria.
- `cannot_conclude`: diagnóstico definitivo de enfermedad celíaca sin biopsia duodenal (en la mayoría de protocolos adultos) — la serología es de cribado, no diagnóstica por sí sola en adultos.

## H. Tendencias

### Tendencias temporales

Debe descender progresivamente tras iniciar dieta libre de gluten en enfermedad celíaca confirmada — útil para monitorear adherencia a la dieta, no para diagnóstico inicial repetido.

## I. Prevención

### Contexto preventivo

Cribado dirigido en personas con síntomas digestivos crónicos, anemia inexplicada, o antecedente familiar — no cribado poblacional universal.

## J. Pruebas complementarias

### Pruebas complementarias posibles

IgA total (si no se solicitó junto — debe pedirse siempre en conjunto), Anti-tTG IgG o Anti-DGP si IgA total es baja, biopsia duodenal si tTG-IgA es positivo.

## K. Cuándo no interpretar y cuándo escalar

### Cuándo NO interpretar / cuándo escalar

No interpretar un resultado negativo sin verificar IgA total normal. No diagnosticar enfermedad celíaca sin biopsia confirmatoria (protocolo adulto estándar). Escalar ante resultado positivo (>10 U/mL) para derivación a biopsia confirmatoria.

## L. Evidencia

### Evidencia científica

- **Nivel:** Fuerte — guía ACG 2013 (Rubio-Tapia et al.) y revisión sistemática Rostom et al. en *Gastroenterology*.
- Fuentes verificadas esta sesión: ver URLs en sección E.

## M. Seguridad para Saludly Brain

### eguridad para Saludly Brain

- **allowed_inferences:** "tTG-IgA positivo, alta probabilidad de enfermedad celíaca, requiere biopsia confirmatoria; siempre verificar IgA total antes de confiar en un resultado negativo".
- **prohibited_inferences:** diagnóstico definitivo de enfermedad celíaca sin biopsia; confiar en un resultado negativo sin verificar IgA total.
- **uncertainty_notes:** debe realizarse con dieta que contenga gluten — un resultado tras restricción de gluten puede ser falsamente negativo.
- **professional_review:** resultado positivo (>10 U/mL), o resultado equívoco (4-10 U/mL) con alta sospecha clínica.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - immunology
  - celiac_screening
  - gastrointestinal
  - tier_3
  - saludly_brain_v1
use_when:
  - "anemia ferropénica inexplicada, síntomas digestivos crónicos, o antecedente familiar de celíaca"
combine_with: [iga, ferritin, vitamin_b12, hemoglobin]
do_not_use_alone:
  - "diagnóstico de enfermedad celíaca sin biopsia"
  - "confiar en resultado negativo sin verificar IgA total"
do_not_conclude:
  - "enfermedad celíaca confirmada sin biopsia duodenal"
escalate_when:
  - "resultado positivo (>10 U/mL) — derivar a biopsia confirmatoria"
```
