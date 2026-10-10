---
doc_id: "SLD-BIO-104"
biomarker_id: "stool_exam"
name_es: "Coprológico"
name_en: "Stool examination (ova and parasites)"
abbreviation: "COP"
sinonimos: ["Coprológico", "Examen coprológico", "Coproscópico", "Parasitológico en heces", "Examen directo de heces"]
category: "Digestivo"
parameter_type: "panel"
tipo_resultado: "cualitativo por campo"
unidad_canonica: "cualitativo"
specimen: "Heces, misma muestra"
nivel_catalogo: "con patrón (parásitos) y solo valor (resto)"
panel: "estándar, todas las personas"
alimenta: ["COND-M4-IN-A02", "SEG-013"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "low"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
---

# SLD-BIO-104 · Coprológico

## A. Identificación
Examen macroscópico (consistencia, color, moco, sangre visible) y microscópico directo y con lugol (quistes, trofozoítos, huevos y larvas de parásitos).

## B. Definición
Busca parásitos intestinales y signos generales de alteración digestiva.

## C. Espécimen y toma
Heces frescas de la misma muestra domiciliaria. Una sola muestra tiene sensibilidad limitada para parásitos; varias muestras en días distintos detectan más, pero eso no cabe en la toma única.

## D. Intervalos y umbrales
Esperado: consistencia formada o blanda, color café, sin moco abundante ni sangre visible, sin parásitos.

## E. Interpretación
Separa parásitos patógenos (requieren tratamiento) de comensales (no lo requieren). La lista la firma el médico (IN-A02).

## F. Contexto del paciente y confusores
Antiparasitarios recientes, diarrea, medicamentos que alteran el tránsito.

## G. Relaciones
Eosinofilia (M3 HE-A03) refuerza helmintos; sangre visible se cruza con la sangre oculta (M4 GA-004).

## H. Tendencias
Un negativo en una sola muestra no descarta parasitosis.

## I. Prevención
Agua segura, lavado de manos y de alimentos.

## J. Pruebas complementarias
Coprológico seriado o pruebas específicas según el médico.

## K. Cuándo no interpretar / cuándo escalar
Sangre visible en heces: escalamiento 2 (SEG-013). Parásito patógeno: escalamiento 1 (IN-A02).

## L. Evidencia
Pendiente de fuente colombiana (Lote 4).

## M. Seguridad para Saludly Brain
- Inferencias permitidas: "parásito que suele requerir tratamiento" o "microorganismo que normalmente no causa enfermedad".
- Inferencias prohibidas: recomendar antiparasitarios; "desparasítate".
- Revisión profesional: sangre visible.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [digestivo, parasitos, coprologico, panel_estandar, saludly_brain_v1]
use_when: ["parásitos en heces", "eosinofilia", "sangre visible en heces"]
combine_with: [eosinophils_pct, wbc, fit_stool]
do_not_use_alone: ["descartar parasitosis con una sola muestra"]
do_not_conclude: ["enfermedad inflamatoria intestinal"]
escalate_when: ["sangre visible en heces"]
```
