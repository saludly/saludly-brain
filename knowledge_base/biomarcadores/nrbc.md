---
doc_id: SLD-BIO-024
biomarker_id: nrbc
name_es: NRBC (Eritroblastos circulantes)
name_en: Nucleated Red Blood Cells
abbreviation: NRBC
sinonimos:
- Eritroblastos
- NRBC
- Glóbulos rojos nucleados
- NRBC (Eritroblastos circulantes)
- NRBC (Eritroblastos)
- Nucleated Red Blood Cells
category: hematology
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: /100 leucocitos
specimen: Sangre total EDTA
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-005
combine_with:
- hemoglobin
- wbc
tier: 4
status: COMPLETO
schema_version: '2.1'
clinical_priority: low
requires_professional_review: true
source_version: 2026-09
normalizado: '2026-10-06'
fuentes_estado: 'según la ficha original: fuentes marcadas como verificadas por su autor, sin reverificar en la normalización'
notas_decision:
- 'Medido a todos: revisión médica obligatoria; positivo, escalamiento 2 con llamada (SEG-005).'
---

# NRBC (Eritroblastos circulantes)

## Notas de decisión de Saludly (6 de octubre de 2026)

- Medido a todos: revisión médica obligatoria; positivo, escalamiento 2 con llamada (SEG-005).
- Reglas que usan esta ficha: SEG-005. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-024. NRBC. Categoría: Hematología. Tipo: analito medido. **Tier 4 — anómalo casi siempre en adultos; no es biomarcador de cribado preventivo, es un hallazgo que activa evaluación cuando aparece.**

## B. Definición

Eritrocitos inmaduros que todavía conservan el núcleo, normalmente confinados a la médula ósea. Su presencia en sangre periférica en un adulto (fuera del contexto neonatal, donde son fisiológicos) es casi siempre un hallazgo anormal que refleja estrés medular severo o infiltración de la médula ósea.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa · Hemograma completo · Tubo EDTA · Método: citometría de flujo automatizada (algunos analizadores lo reportan solo si se detecta, no como valor de rutina). Unidad: /100 leucocitos, o como corrección al conteo de WBC (los NRBC pueden falsear el WBC total si el analizador no los excluye).

## D. Intervalos y umbrales

- **Umbral clínico:** en adultos (fuera del período neonatal), **cualquier NRBC detectado es anormal** — no existe un "rango de referencia normal" >0 en adultos sanos.

## E. Interpretación

- **Presencia (cualquier valor >0 en adulto):** estrés medular severo (hemólisis severa, hipoxia severa, sangrado masivo), infiltración de médula ósea (fibrosis medular, metástasis, leucemia), asplenia (el bazo normalmente filtra estas células).

## F. Contexto del paciente y confusores

### Contexto del paciente

Antecedente de esplenectomía (relevante — la ausencia de bazo permite que estas células circulen sin ser filtradas, sin implicar necesariamente patología severa), síntomas de anemia severa, antecedente oncológico.

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Hemoglobina (para evaluar severidad de anemia asociada), WBC (para corregir el conteo si el analizador no lo hace automáticamente).
- `cannot_conclude`: causa específica sin evaluación hematológica dirigida (frotis, y si corresponde, estudio de médula ósea).

## H. Tendencias

### Tendencias temporales

No aplica como marcador de tendencia longitudinal — su aparición es en sí misma el hallazgo relevante, independientemente de la magnitud.

## I. Prevención

No aplica — no es un marcador preventivo, es un hallazgo de alerta.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Frotis de sangre periférica (obligatorio ante NRBC positivos sin esplenectomía conocida), evaluación hematológica dirigida — fuera del alcance operativo de Saludly, requiere derivación inmediata.

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

No es cribado — es un hallazgo incidental que, cuando aparece, requiere derivación, no interpretación por IA.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento hematológico estándar sobre fisiología de la médula ósea.
- **Fuente:** principio de hematología clínica estándar, consistente con la definición de rangos de referencia CBC verificados esta sesión para el resto del hemograma (ninguna fuente institucional consultada — MedlinePlus, ACCP, NBME, Medscape, StatPearls — reporta NRBC como componente del hemograma normal en adultos, lo cual confirma indirectamente que un valor >0 está fuera de cualquier rango de referencia adulto estándar).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** ninguna interpretación clínica autónoma — este es, junto con troponina, uno de los hallazgos donde Saludly Brain debe ser más conservador.
- **prohibited_inferences:** cualquier intento de explicar o minimizar un NRBC positivo sin antecedente de esplenectomía conocido.
- **uncertainty_notes:** hallazgo poco frecuente en un panel preventivo ambulatorio — su sola aparición, sin más contexto, ya amerita derivación.
- **professional_review:** **CUALQUIER NRBC detectado en un adulto sin esplenectomía conocida, siempre, sin excepción — requiere evaluación hematológica, no interpretación automática.**

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - hematology
  - tier_4
  - saludly_brain_v1
use_when:
  - "NRBC detectado en el hemograma — hallazgo de alerta, no de rutina"
combine_with: [hemoglobin, wbc]
do_not_use_alone:
  - "cualquier interpretación autónoma"
do_not_conclude:
  - "explicación benigna sin antecedente de esplenectomía conocido"
escalate_when:
  - "SIEMPRE, sin excepción, salvo esplenectomía ya conocida y documentada"
```
