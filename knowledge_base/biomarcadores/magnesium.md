---
doc_id: SLD-BIO-034
biomarker_id: magnesium
name_es: Magnesio Sérico
name_en: Serum Magnesium
abbreviation: Mg
sinonimos:
- Magnesio
- Mg
- Magnesio Sérico
- Serum Magnesium
category: metabolism_electrolytes
parameter_type: measured_analyte
tipo_resultado: numérico
unidad_canonica: mg/dL
specimen: Suero
nivel_catalogo: solo valor y rango
panel: estándar
sexo: ambos
alimenta:
- SEG-008
combine_with:
- calcium
- potassium
- creatinine
- egfr
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

# Magnesio Sérico

## Notas de decisión de Saludly (6 de octubre de 2026)

- Reglas que usan esta ficha: SEG-008. Si esta ficha y una regla dicen cosas distintas, manda la regla.

## A. Identificación

ID: SLD-BIO-034. Mg. Categoría: Metabolismo. Tipo: analito medido. Tier 2.

## B. Definición

Catión predominantemente intracelular (solo ~1% del magnesio corporal es sérico) — cofactor en cientos de reacciones enzimáticas, incluyendo la regulación del calcio y el potasio. Su medición sérica **refleja pobremente el estado real de magnesio intracelular/corporal total**, limitación ampliamente documentada en la literatura de fisiología.

## C. Espécimen y toma

### Espécimen y laboratorio

Sangre venosa (suero) · Método colorimétrico estandarizado. Unidad: mg/dL. No requiere ayuno.

## D. Intervalos y umbrales

- **Laboratory reference interval:** depende del laboratorio/método.
- **Clinical decision threshold (verificado esta sesión):** rango normal **1.3-2.1 mEq/L** (equivalente ~1.6-2.6 mg/dL; algunas fuentes reportan 1.7-2.2 mg/dL) — variación notable entre fuentes, consistente con la limitación ya señalada de que el magnesio sérico es una medida poco estandarizada y poco representativa de las reservas corporales reales.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026)

## E. Interpretación

- **Disminuido:** causas frecuentes — uso de diuréticos, inhibidores de bomba de protones (uso crónico), alcoholismo, diarrea crónica, mal control glucémico en diabetes.
- **Elevado:** infrecuente en ambulatorios sanos; principalmente relacionado con insuficiencia renal (reducción de excreción) o suplementación excesiva.
- **Limitación central:** un magnesio sérico "normal" no descarta depleción intracelular significativa — el sérico es la fracción más pequeña y menos representativa del magnesio corporal total.

## F. Contexto del paciente y confusores

### Contexto del paciente

Relevantes: medicamentos (diuréticos, IBP crónicos), consumo de alcohol, diarrea crónica, control glucémico, función renal, síntomas (calambres musculares, arritmias, fatiga).

## G. Relaciones con otros biomarcadores

- `interpret_together_with`: Calcio y Potasio (el magnesio bajo dificulta la corrección de hipocalcemia e hipopotasemia — es una causa de hipopotasemia/hipocalcemia refractaria al tratamiento si no se corrige primero), Creatinina/eGFR.
- `pattern_examples`: hipopotasemia que no responde a reposición de potasio + magnesio bajo = corregir magnesio primero, patrón clínico bien reconocido.
- `cannot_conclude`: estado real de magnesio corporal total a partir del valor sérico únicamente.

## H. Tendencias

### Tendencias temporales

Dada la limitación de que el sérico refleja pobremente las reservas corporales, un valor sérico estable no descarta depleción progresiva — su valor de tendencia es limitado comparado con otros biomarcadores del catálogo.

## I. Prevención

Acciones razonablemente relacionadas: revisión de medicamentos con un profesional (IBP crónicos, diuréticos), moderación de consumo de alcohol, dieta con fuentes de magnesio.

## J. Pruebas complementarias

### Pruebas complementarias posibles

Calcio y Potasio (si hay hipopotasemia/hipocalcemia refractaria, revisar magnesio como causa).

## K. Cuándo no interpretar y cuándo escalar

### Screening vs diagnóstico

Parte del panel metabólico ampliado — con limitación de sensibilidad documentada para detectar depleción real.

## L. Evidencia

### Evidencia científica

- **Nivel:** conocimiento fisiológico estándar; la limitación de sensibilidad del magnesio sérico frente al magnesio corporal total está ampliamente documentada en fisiología clínica y bioquímica.
- **Fuente:** NBME Laboratory Reference Values (https://www.nbme.org/sites/default/files/2025-03/NBME_Laboratory_Reference_Values.pdf) y ACCP Lab Values Table (https://www.accp.com/docs/sap/Lab_Values_Table_ACSAP.pdf) — verificado esta sesión (ago-2026).

## M. Seguridad para Saludly Brain

- **allowed_inferences:** "magnesio sérico alterado, considerar medicamentos (IBP, diuréticos) y contexto; un valor normal no descarta depleción intracelular si hay síntomas o hipopotasemia/hipocalcemia refractaria".
- **prohibited_inferences:** "magnesio normal = sin deficiencia posible" cuando hay contexto clínico sugerente (hipopotasemia refractaria, síntomas).
- **uncertainty_notes:** el magnesio sérico es una prueba de baja sensibilidad para el estado corporal total — comunicar esta limitación explícitamente.
- **professional_review:** magnesio marcadamente alterado, especialmente con síntomas (arritmias, calambres severos) o hipopotasemia/hipocalcemia refractaria a tratamiento.

---

# RAG_INSTRUCTIONS

```yaml
rag_tags:
  - electrolytes
  - metabolism
  - tier_2
  - saludly_brain_v1

use_when:
  - "hipopotasemia o hipocalcemia refractaria a tratamiento"
  - "uso crónico de IBP o diuréticos"

combine_with: [calcium, potassium, creatinine, egfr]

do_not_use_alone:
  - "descartar deficiencia de magnesio solo por valor sérico normal"

do_not_conclude:
  - "estado corporal total de magnesio a partir del valor sérico"

escalate_when:
  - "magnesio marcadamente alterado con síntomas o hipopotasemia/hipocalcemia refractaria"
```
