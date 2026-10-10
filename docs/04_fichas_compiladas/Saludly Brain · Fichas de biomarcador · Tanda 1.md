# Fichas de biomarcador · Tanda 1 — Orina, heces, serologías, PSA y ANA

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Esta tanda crea las fichas base de 11 analitos del panel estándar que no tenían ficha: uroanálisis, tres pruebas de heces, cinco serologías, PSA total y ANA. Son las que necesitaban primero las fichas de condición de los módulos M2, M4, M5 y M6, y la ficha de seguridad SEG-013.

Antes había dicho que esta tanda tenía 13 fichas. Conté mal: son 11. El total pendiente de la Fase 1 baja de 34 a 32 fichas.

## Esquema 2.1

Estas fichas estrenan el esquema al que se van a normalizar las 100 existentes. Frente al esquema 2.0 agrega cinco campos que el motor necesita:

| Campo nuevo | Para qué sirve |
| --- | --- |
| `sinonimos` | Nombres con que aparece el analito en un informe de laboratorio; los usa la normalización (Fase 3) |
| `unidad_canonica` | Unidad en que el motor guarda el valor |
| `tipo_resultado` | Numérico, cualitativo (reactivo / no reactivo) o semicuantitativo (título, cruces) |
| `nivel_catalogo` | Con patrón, solo valor y rango, vitamina o refleja |
| `alimenta` | Fichas de condición o de seguridad que usan este analito |

Las secciones van siempre en el mismo orden, de la A a la M, y cierran con el bloque `RAG_INSTRUCTIONS`.

## Estado de las fuentes

Ninguna de estas fichas se escribió con fuentes leídas completas en esta sesión. Usan las guías que citan los lotes (casi todas confirmadas solo por resultado de búsqueda) y conocimiento clínico general. Por eso todas llevan `status: "BORRADOR"` y `fuentes_estado: "por verificar"`. La firma médica y la lectura de fuentes las pasan a COMPLETO.

## Índice

| doc_id | biomarker_id | Analito | Tipo de resultado | Alimenta |
| --- | --- | --- | --- | --- |
| SLD-BIO-101 | urinalysis | Uroanálisis (tira y sedimento) | Cualitativo y semicuantitativo | M2 NE-006, M4 IN-A01, SEG-013 |
| SLD-BIO-102 | fit_stool | Sangre oculta en heces inmunoquímica (FIT) | Cualitativo | M4 GA-004 |
| SLD-BIO-103 | hpylori_stool_ag | Antígeno de *H. pylori* en heces | Cualitativo | M4 GA-005 |
| SLD-BIO-104 | stool_exam | Coprológico | Cualitativo | M4 IN-A02, SEG-013 |
| SLD-BIO-105 | anti_hcv | Anticuerpos contra hepatitis C | Cualitativo con índice | M4 IN-001 |
| SLD-BIO-106 | hbsag | Antígeno de superficie de hepatitis B | Cualitativo con índice | M4 IN-002 |
| SLD-BIO-107 | anti_hbs | Anticuerpos contra el antígeno de superficie | Numérico | M4 IN-002 |
| SLD-BIO-108 | anti_hbc | Anticuerpos totales contra el core de hepatitis B | Cualitativo con índice | M4 IN-002 |
| SLD-BIO-109 | chagas_elisa_total | ELISA de *T. cruzi* (antígenos totales) | Cualitativo con índice | M4 IN-003 |
| SLD-BIO-110 | psa_total | Antígeno prostático específico total | Numérico | M5 UR-001 |
| SLD-BIO-111 | ana_hep2 | Anticuerpos antinucleares por IFI en HEp-2 | Semicuantitativo (título y patrón) | M6 RE-A01 |

---

## SLD-BIO-101 · Uroanálisis (tira y sedimento)

```yaml
doc_id: "SLD-BIO-101"
biomarker_id: "urinalysis"
name_es: "Uroanálisis"
name_en: "Urinalysis"
abbreviation: "UA"
sinonimos: ["Uroanálisis", "Parcial de orina", "Examen general de orina", "Citoquímico de orina", "Orina completa", "Urinalysis"]
category: "Riñón y vías urinarias"
parameter_type: "panel"
tipo_resultado: "cualitativo y semicuantitativo por campo"
unidad_canonica: "por campo (ver D)"
specimen: "Primera orina de la mañana, chorro medio"
nivel_catalogo: "con patrón (hematíes) y solo valor (resto de campos)"
panel: "estándar, todas las personas"
alimenta: ["COND-M2-NE-006", "COND-M4-IN-A01", "SEG-013"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Panel de orina con tres partes: examen físico (color, aspecto, densidad), químico por tira reactiva (pH, proteínas, glucosa, cetonas, sangre, nitritos, esterasa leucocitaria, bilirrubina, urobilinógeno) y microscópico del sedimento (leucocitos, hematíes, células epiteliales, bacterias, cilindros, cristales).

### B. Definición

Evalúa de forma general el riñón y las vías urinarias, y da señales indirectas de metabolismo (glucosa, cetonas) e hígado (bilirrubina, urobilinógeno).

### C. Espécimen y toma

Primera orina de la mañana, chorro medio, en frasco estéril. Procesar idealmente en las 2 horas siguientes o refrigerar: la demora deja crecer bacterias y destruye células. No tomar durante la menstruación ni en los 3 días siguientes, ni tras sondaje o procedimiento urológico reciente.

### D. Intervalos y umbrales

| Campo | Esperado | Nota |
| --- | --- | --- |
| Densidad | 1,005 a 1,030 | Refleja hidratación |
| pH | 5,0 a 8,0 | Varía con la dieta |
| Proteínas, glucosa, cetonas, sangre, nitritos, esterasa, bilirrubina | Negativo | La tira de proteínas detecta sobre todo albúmina y no reemplaza la relación albúmina/creatinina |
| Urobilinógeno | 0,2 a 1,0 mg/dL |  |
| Leucocitos en sedimento | 0 a 5 por campo |  |
| Hematíes en sedimento | 0 a 3 por campo | Más de 3 = microhematuria (AUA, enmienda 2025) |
| Cilindros | No se observan u ocasionales hialinos |  |

### E. Interpretación

Cada campo se interpreta junto con la sangre: glucosa en orina con la glucosa sérica, proteína en tira con la albúmina/creatinina, bilirrubina y urobilinógeno con la función hepática. La sangre en la tira solo cuenta si el sedimento confirma hematíes.

### F. Contexto del paciente y confusores

Menstruación, ejercicio intenso en 48 horas, infección urinaria, inhibidores de SGLT2 (glucosa en orina esperada), ayuno prolongado (cetonas), deshidratación (densidad alta), contaminación genital de la muestra (células epiteliales abundantes).

### G. Relaciones

Hematíes con albuminuria o TFG baja sugieren origen glomerular. Nitritos o esterasa solo cuentan como infección con síntomas (IDSA 2019). Glucosa en orina con glucosa sérica alta apoya diabetes.

### H. Tendencias

La microhematuria de bajo riesgo se repite a los 6 meses; la persistencia cambia la conducta.

### I. Prevención

Hidratación adecuada. Sin otras recomendaciones específicas del uroanálisis.

### J. Pruebas complementarias

Relación albúmina/creatinina (en el panel), urocultivo (lo pide el médico), citología o estudio urológico según riesgo.

### K. Cuándo no interpretar / cuándo escalar

No interpretar hematuria con menstruación. No reportar bacteriuria sin síntomas fuera del embarazo. Escalar según NE-006 (hematuria) y SEG-013 (resto de campos).

### L. Evidencia

AUA/SUFU 2020 con enmienda 2025 (microhematuria), IDSA 2019 (bacteriuria asintomática), KDIGO 2024. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "campo alterado que conviene repetir o revisar con el médico".
- Inferencias prohibidas: infección sin síntomas, cáncer, cálculos, enfermedad renal a partir de la tira.
- Revisión profesional: según las fichas de condición que alimenta.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [renal, urinario, uroanalisis, panel_estandar, saludly_brain_v1]
use_when: ["interpretar microhematuria", "contexto de infección urinaria con síntomas", "glucosa o proteína en orina"]
combine_with: [uacr, egfr, glucose, bilirubin_total]
do_not_use_alone: ["diagnóstico de infección sin síntomas", "evaluación renal sin albúmina/creatinina"]
do_not_conclude: ["cáncer de vías urinarias", "litiasis"]
escalate_when: ["microhematuria con albuminuria o TFG baja", "cetonas con glucosa alta", "bilirrubina en orina positiva"]
```

---

## SLD-BIO-102 · Sangre oculta en heces inmunoquímica (FIT)

```yaml
doc_id: "SLD-BIO-102"
biomarker_id: "fit_stool"
name_es: "Sangre oculta en heces inmunoquímica"
name_en: "Fecal immunochemical test"
abbreviation: "FIT"
sinonimos: ["Sangre oculta en heces", "SOH", "SOMF inmunoquímica", "Prueba inmunoquímica fecal", "FIT", "iFOBT"]
category: "Digestivo"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (positivo / negativo)"
unidad_canonica: "cualitativo"
specimen: "Heces, una muestra"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M4-GA-004"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Detecta hemoglobina humana en las heces con anticuerpos específicos. Es la prueba de tamizaje colorrectal que define la Res. 3280 para personas de 50 a 75 años.

### B. Definición

Busca sangrado del colon que no se ve a simple vista. Al ser inmunoquímica, detecta hemoglobina humana y no reacciona con la carne de la dieta.

### C. Espécimen y toma

Una muestra de heces con el kit del laboratorio, en casa, el mismo día de la visita. A diferencia de la prueba de guayaco, no exige dieta previa. Conservar según el fabricante; la hemoglobina se degrada con el calor y el tiempo.

### D. Intervalos y umbrales

Resultado cualitativo. El corte de positividad lo fija el fabricante (suele expresarse en ng de hemoglobina por mL de buffer) y debe constar en el informe del laboratorio.

### E. Interpretación

Positivo: hay sangre en el tubo digestivo bajo y se necesita colonoscopia; no es un diagnóstico de cáncer, y las causas benignas son frecuentes. Negativo: no descarta pólipos ni cáncer, por eso el tamizaje se repite cada 2 años.

### F. Contexto del paciente y confusores

Hemorroides o fisuras con sangrado, menstruación (contaminación), antiinflamatorios o anticoagulantes (no anulan un positivo). Edad y antecedente familiar de cáncer colorrectal para la vista médica.

### G. Relaciones

Con anemia o déficit de hierro (M3), refuerza la necesidad de colonoscopia.

### H. Tendencias

Un negativo vale para 2 años en el tamizaje formal.

### I. Prevención

Alimentación con fibra, actividad física, menos carnes procesadas y alcohol.

### J. Pruebas complementarias

Colonoscopia ante cualquier positivo.

### K. Cuándo no interpretar / cuándo escalar

Un positivo no se repite para "confirmar": va a colonoscopia (escalamiento 2, GA-004).

### L. Evidencia

Res. 3280 de 2018, USPSTF 2021. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "sangre oculta positiva; requiere colonoscopia".
- Inferencias prohibidas: cáncer, pólipos, repetir la prueba en vez de colonoscopia.
- Revisión profesional: todo positivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [digestivo, colorrectal, tamizaje, panel_estandar, saludly_brain_v1]
use_when: ["sangre oculta positiva o negativa", "tamizaje colorrectal por edad"]
combine_with: [hemoglobin, ferritin]
do_not_use_alone: ["descartar cáncer colorrectal"]
do_not_conclude: ["cáncer", "pólipos"]
escalate_when: ["cualquier resultado positivo"]
```

---

## SLD-BIO-103 · Antígeno de *H. pylori* en heces

```yaml
doc_id: "SLD-BIO-103"
biomarker_id: "hpylori_stool_ag"
name_es: "Antígeno de Helicobacter pylori en heces"
name_en: "Helicobacter pylori stool antigen"
abbreviation: "HpSA"
sinonimos: ["Antígeno H. pylori en heces", "H. pylori antígeno fecal", "Helicobacter pylori Ag heces", "HpSA"]
category: "Digestivo"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (positivo / negativo)"
unidad_canonica: "cualitativo"
specimen: "Heces, misma muestra que FIT y coprológico"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M4-GA-005"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Detecta antígenos de *H. pylori* en heces con anticuerpos monoclonales. Indica infección activa, a diferencia de la serología en sangre, que puede quedar positiva tras la curación.

### B. Definición

*H. pylori* es una bacteria del estómago muy frecuente en Colombia, asociada a gastritis, úlcera y cáncer gástrico. La guía colombiana de 2025 recomienda tratar a todo adulto con infección activa.

### C. Espécimen y toma

Heces frescas o refrigeradas, de la misma muestra domiciliaria. Para evitar falsos negativos: sin inhibidores de bomba de protones en las 2 semanas previas ni antibióticos o bismuto en las 4 semanas previas.

### D. Intervalos y umbrales

Cualitativo; el corte lo define el fabricante. La prueba de aliento con urea C13 es la referencia no invasiva; el antígeno fecal monoclonal es la opción disponible en toma domiciliaria y su limitación se escribe en el informe.

### E. Interpretación

Positivo: infección activa probable. Negativo: sin infección activa, salvo uso reciente de inhibidores de bomba o antibióticos.

### F. Contexto del paciente y confusores

Inhibidores de bomba, antibióticos, bismuto, sangrado digestivo alto activo, heces muy líquidas.

### G. Relaciones

Puede explicar déficit de hierro (M3) y se lee con la sangre oculta en la vista médica.

### H. Tendencias

Tras tratamiento, el control se hace al menos 4 semanas después de terminar antibióticos.

### I. Prevención

Agua segura e higiene de manos; consulta para tratamiento.

### J. Pruebas complementarias

Prueba de aliento con urea C13; endoscopia según síntomas y edad.

### K. Cuándo no interpretar / cuándo escalar

Negativo con medicamentos recientes: no concluyente. Positivo: escalamiento 2 (GA-005).

### L. Evidencia

Asociación Colombiana de Gastroenterología 2025. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "infección activa probable por *H. pylori*; las guías colombianas recomiendan tratarla".
- Inferencias prohibidas: úlcera, gastritis, cáncer gástrico; recomendar antibióticos.
- Revisión profesional: todo positivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [digestivo, infeccioso, h_pylori, panel_estandar, saludly_brain_v1]
use_when: ["antígeno de H. pylori positivo o negativo", "déficit de hierro sin causa"]
combine_with: [ferritin, hemoglobin, fit_stool]
do_not_use_alone: ["descartar infección con inhibidores de bomba recientes"]
do_not_conclude: ["úlcera", "cáncer gástrico"]
escalate_when: ["resultado positivo"]
```

---

## SLD-BIO-104 · Coprológico

```yaml
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
```

### A. Identificación

Examen macroscópico (consistencia, color, moco, sangre visible) y microscópico directo y con lugol (quistes, trofozoítos, huevos y larvas de parásitos).

### B. Definición

Busca parásitos intestinales y signos generales de alteración digestiva.

### C. Espécimen y toma

Heces frescas de la misma muestra domiciliaria. Una sola muestra tiene sensibilidad limitada para parásitos; varias muestras en días distintos detectan más, pero eso no cabe en la toma única.

### D. Intervalos y umbrales

Esperado: consistencia formada o blanda, color café, sin moco abundante ni sangre visible, sin parásitos.

### E. Interpretación

Separa parásitos patógenos (requieren tratamiento) de comensales (no lo requieren). La lista la firma el médico (IN-A02).

### F. Contexto del paciente y confusores

Antiparasitarios recientes, diarrea, medicamentos que alteran el tránsito.

### G. Relaciones

Eosinofilia (M3 HE-A03) refuerza helmintos; sangre visible se cruza con la sangre oculta (M4 GA-004).

### H. Tendencias

Un negativo en una sola muestra no descarta parasitosis.

### I. Prevención

Agua segura, lavado de manos y de alimentos.

### J. Pruebas complementarias

Coprológico seriado o pruebas específicas según el médico.

### K. Cuándo no interpretar / cuándo escalar

Sangre visible en heces: escalamiento 2 (SEG-013). Parásito patógeno: escalamiento 1 (IN-A02).

### L. Evidencia

Pendiente de fuente colombiana (Lote 4).

### M. Seguridad para Saludly Brain

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

---

## SLD-BIO-105 · Anticuerpos contra hepatitis C (anti-VHC)

```yaml
doc_id: "SLD-BIO-105"
biomarker_id: "anti_hcv"
name_es: "Anticuerpos contra el virus de la hepatitis C"
name_en: "Hepatitis C virus antibody"
abbreviation: "Anti-VHC"
sinonimos: ["Anti-VHC", "Anti HCV", "Anticuerpos hepatitis C", "HCV Ab", "Hepatitis C anticuerpos totales"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice (S/CO)"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas, con consentimiento"
alimenta: ["COND-M4-IN-001"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Inmunoensayo que detecta anticuerpos contra el virus de la hepatitis C. Es la prueba inicial del algoritmo de tamizaje.

### B. Definición

Un resultado reactivo indica contacto con el virus en algún momento. No distingue infección activa de infección resuelta: para eso está el ARN viral, que el laboratorio corre como refleja.

### C. Espécimen y toma

Suero, sin ayuno específico.

### D. Intervalos y umbrales

Reactivo o no reactivo según el índice y el corte del fabricante (por ejemplo, índice menor de 1,00 = no reactivo en el PDF de ejemplo).

### E. Interpretación

No reactivo: sin evidencia de infección, salvo exposición muy reciente (los anticuerpos tardan semanas o meses en aparecer). Reactivo: se interpreta solo con el ARN viral.

### F. Contexto del paciente y confusores

Exposición reciente (periodo de ventana), inmunosupresión (puede no generar anticuerpos), falsos positivos con índices bajos.

### G. Relaciones

Con ALT alta, se lee en el patrón hepático (M4).

### H. Tendencias

Los anticuerpos suelen persistir tras la curación; no sirven para controlar el tratamiento.

### I. Prevención

No compartir objetos con sangre; tratamiento curativo disponible.

### J. Pruebas complementarias

ARN de hepatitis C (refleja).

### K. Cuándo no interpretar / cuándo escalar

Reactivo: escalamiento 2 con llamada del médico, nunca por WhatsApp (IN-001).

### L. Evidencia

Lineamiento de tamizaje de hepatitis C del Ministerio de Salud, USPSTF 2020. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "anticuerpos reactivos; se necesita el ARN viral para saber si la infección está activa".
- Inferencias prohibidas: cirrosis, incurable, contagio a la familia.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_c, serologia, panel_estandar, saludly_brain_v1]
use_when: ["anti-VHC reactivo o no reactivo"]
combine_with: [hcv_rna, alt, ast]
do_not_use_alone: ["afirmar infección activa"]
do_not_conclude: ["cirrosis", "infección activa sin ARN"]
escalate_when: ["cualquier resultado reactivo"]
```

---

## SLD-BIO-106 · Antígeno de superficie de hepatitis B (HBsAg)

```yaml
doc_id: "SLD-BIO-106"
biomarker_id: "hbsag"
name_es: "Antígeno de superficie del virus de la hepatitis B"
name_en: "Hepatitis B surface antigen"
abbreviation: "HBsAg"
sinonimos: ["HBsAg", "Antígeno de superficie hepatitis B", "AgHBs", "Antígeno Australia"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas, con consentimiento"
alimenta: ["COND-M4-IN-002"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Inmunoensayo que detecta una proteína de la envoltura del virus de la hepatitis B.

### B. Definición

Su presencia indica infección actual, aguda o crónica. Si persiste más de 6 meses, la infección es crónica.

### C. Espécimen y toma

Suero, sin ayuno específico.

### D. Intervalos y umbrales

Reactivo o no reactivo según el índice y el corte del fabricante.

### E. Interpretación

Siempre se interpreta con anti-HBc total y anti-HBs, en los cinco estados de la ficha IN-002.

### F. Contexto del paciente y confusores

La vacuna puede dar un HBsAg reactivo transitorio en los días siguientes a la aplicación; la enfermera pregunta si hubo vacuna reciente. Falsos positivos con índices bajos.

### G. Relaciones

Con ALT alta, se lee en el patrón hepático (M4).

### H. Tendencias

La negativización con aparición de anti-HBs indica resolución.

### I. Prevención

Vacunación de convivientes y parejas; no compartir objetos con sangre.

### J. Pruebas complementarias

Carga viral, HBeAg, anti-HBc IgM, según el médico.

### K. Cuándo no interpretar / cuándo escalar

Reactivo: escalamiento 2 con llamada (IN-002).

### L. Evidencia

CDC 2023 (interpretación serológica), Res. 1314 de 2020. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "la prueba muestra una infección por hepatitis B; el médico explicará los siguientes pasos".
- Inferencias prohibidas: hepatitis crónica sin tiempo de evolución, cirrosis, incurable.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_b, serologia, panel_estandar, saludly_brain_v1]
use_when: ["interpretar el panel de hepatitis B"]
combine_with: [anti_hbc, anti_hbs, alt]
do_not_use_alone: ["clasificar el estado de hepatitis B"]
do_not_conclude: ["infección crónica sin persistencia de 6 meses", "cirrosis"]
escalate_when: ["cualquier resultado reactivo"]
```

---

## SLD-BIO-107 · Anticuerpos contra el antígeno de superficie (anti-HBs)

```yaml
doc_id: "SLD-BIO-107"
biomarker_id: "anti_hbs"
name_es: "Anticuerpos contra el antígeno de superficie de hepatitis B"
name_en: "Hepatitis B surface antibody"
abbreviation: "Anti-HBs"
sinonimos: ["Anti-HBs", "AcHBs", "Anticuerpos anti antígeno de superficie", "HBsAb"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "mUI/mL"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas, con consentimiento"
alimenta: ["COND-M4-IN-002"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Inmunoensayo cuantitativo de los anticuerpos protectores contra la hepatitis B.

### B. Definición

Aparecen tras la vacuna o tras una infección resuelta. Con anti-HBc no reactivo indican inmunidad por vacuna.

### C. Espécimen y toma

Suero, sin ayuno específico.

### D. Intervalos y umbrales

10 mUI/mL o más: nivel considerado protector. Menos de 10: sin anticuerpos detectables en nivel protector.

### E. Interpretación

Menos de 10 con HBsAg y anti-HBc no reactivos: estado susceptible y recomendación de vacuna. En personas vacunadas hace años, los anticuerpos pueden bajar de 10 aunque quede memoria inmunológica; el médico decide si basta una dosis de refuerzo.

### F. Contexto del paciente y confusores

Inmunosupresión y diálisis (respuesta menor a la vacuna), tiempo desde la última dosis.

### G. Relaciones

Siempre con HBsAg y anti-HBc (IN-002).

### H. Tendencias

Baja con los años tras la vacunación.

### I. Prevención

Vacuna contra la hepatitis B.

### J. Pruebas complementarias

Anti-HBs después de la vacuna, según el médico.

### K. Cuándo no interpretar / cuándo escalar

No escala por sí solo; el estado susceptible tiene escalamiento 1 (IN-002).

### L. Evidencia

CDC 2023. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "no tienes anticuerpos detectables en nivel protector; existe una vacuna".
- Inferencias prohibidas: "nunca te vacunaron", "no tienes defensas" sin matizar.
- Revisión profesional: no requerida.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_b, vacunacion, panel_estandar, saludly_brain_v1]
use_when: ["estado de inmunidad contra hepatitis B"]
combine_with: [hbsag, anti_hbc]
do_not_use_alone: ["clasificar infección"]
do_not_conclude: ["nunca vacunado"]
escalate_when: []
```

---

## SLD-BIO-108 · Anticuerpos totales contra el core de hepatitis B (anti-HBc)

```yaml
doc_id: "SLD-BIO-108"
biomarker_id: "anti_hbc"
name_es: "Anticuerpos totales contra el antígeno core de hepatitis B"
name_en: "Total hepatitis B core antibody"
abbreviation: "Anti-HBc total"
sinonimos: ["Anti-HBc total", "Anti core hepatitis B", "AcHBc total", "HBcAb total"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas, con consentimiento"
alimenta: ["COND-M4-IN-002"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "high"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Inmunoensayo que detecta anticuerpos (IgG e IgM) contra el núcleo del virus de la hepatitis B.

### B. Definición

Indica infección pasada o actual; la vacuna no lo produce. Es la prueba que separa la inmunidad por vacuna de la inmunidad por infección.

### C. Espécimen y toma

Suero, sin ayuno específico.

### D. Intervalos y umbrales

Reactivo o no reactivo según el índice y el corte del fabricante.

### E. Interpretación

Reactivo con HBsAg no reactivo y anti-HBs protector: infección pasada resuelta. Reactivo aislado (HBsAg y anti-HBs negativos): varias interpretaciones posibles (infección resuelta con anticuerpos que bajaron, falso positivo, infección oculta); requiere evaluación médica.

### F. Contexto del paciente y confusores

Falsos positivos con índices bajos; transfusiones recientes.

### G. Relaciones

Siempre con HBsAg y anti-HBs (IN-002).

### H. Tendencias

Persiste de por vida tras la infección.

### I. Prevención

Importante si la persona va a recibir inmunosupresión o quimioterapia: hay riesgo de reactivación.

### J. Pruebas complementarias

Carga viral de hepatitis B ante anti-HBc aislado, según el médico.

### K. Cuándo no interpretar / cuándo escalar

Anti-HBc aislado: escalamiento 2 con llamada. Infección pasada resuelta: escalamiento 1 con nota de reactivación (IN-002).

### L. Evidencia

CDC 2023. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "señal de una infección por hepatitis B, actual o pasada".
- Inferencias prohibidas: infección activa sin HBsAg, contagio.
- Revisión profesional: todo reactivo.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [infeccioso, hepatitis_b, serologia, panel_estandar, saludly_brain_v1]
use_when: ["interpretar el panel de hepatitis B", "riesgo de reactivación con inmunosupresión"]
combine_with: [hbsag, anti_hbs]
do_not_use_alone: ["afirmar infección activa"]
do_not_conclude: ["infección activa sin HBsAg"]
escalate_when: ["anti-HBc aislado", "anti-HBc reactivo con inmunosupresión declarada"]
```

---

## SLD-BIO-109 · ELISA de *Trypanosoma cruzi* (antígenos totales)

```yaml
doc_id: "SLD-BIO-109"
biomarker_id: "chagas_elisa_total"
name_es: "Anticuerpos IgG contra Trypanosoma cruzi (ELISA de antígenos totales)"
name_en: "Trypanosoma cruzi IgG ELISA (whole antigen)"
abbreviation: "ELISA Chagas"
sinonimos: ["ELISA Chagas", "Anticuerpos T. cruzi", "Chagas IgG", "Serología para Chagas", "Trypanosoma cruzi anticuerpos"]
category: "Infecciosas"
parameter_type: "measured_analyte"
tipo_resultado: "cualitativo (reactivo / no reactivo) con índice"
unidad_canonica: "índice"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas, con consentimiento"
alimenta: ["COND-M4-IN-003"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: true
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Primera prueba del algoritmo serológico de Chagas: ELISA con antígenos totales del parásito.

### B. Definición

Detecta anticuerpos contra *T. cruzi*, el parásito que transmite el pito (triatomino). En la fase crónica la persona puede no tener síntomas por años.

### C. Espécimen y toma

Suero, sin ayuno específico.

### D. Intervalos y umbrales

Reactivo o no reactivo según el índice y el corte del fabricante (por ejemplo, índice menor de 0,90 = no reactivo en el PDF de ejemplo).

### E. Interpretación

Un solo ELISA reactivo no basta: el diagnóstico exige dos pruebas con antígenos distintos. El laboratorio corre la segunda ELISA (antígenos recombinantes) como refleja; si discrepan, se necesita una tercera.

### F. Contexto del paciente y confusores

Reacción cruzada con *Leishmania*; procedencia de municipios endémicos (sube la probabilidad previa).

### G. Relaciones

Sin relaciones de laboratorio; en caso positivo, el médico pide evaluación cardíaca.

### H. Tendencias

Los anticuerpos persisten en la infección crónica.

### I. Prevención

Mejoras de vivienda en zonas endémicas; tamizaje de familiares, sobre todo hijos de madres positivas.

### J. Pruebas complementarias

Segunda ELISA recombinante (refleja), tercera prueba si hay discordancia, electrocardiograma según el médico.

### K. Cuándo no interpretar / cuándo escalar

Un solo reactivo: informe en espera de la segunda ELISA. Dos reactivos: escalamiento 2 con llamada (IN-003).

### L. Evidencia

Algoritmo de Chagas del Ministerio de Salud (pieza para gestantes). Lineamiento del INS para adultos: pendiente.

### M. Seguridad para Saludly Brain

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

---

## SLD-BIO-110 · Antígeno prostático específico total (PSA)

```yaml
doc_id: "SLD-BIO-110"
biomarker_id: "psa_total"
name_es: "Antígeno prostático específico total"
name_en: "Total prostate-specific antigen"
abbreviation: "PSA"
sinonimos: ["PSA", "PSA total", "Antígeno prostático específico", "APE", "Antígeno prostático total"]
category: "Salud del hombre"
parameter_type: "measured_analyte"
tipo_resultado: "numérico"
unidad_canonica: "ng/mL"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, hombres, con consentimiento"
alimenta: ["COND-M5-UR-001"]
tier: 1
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Inmunoensayo de una proteína producida por la próstata.

### B. Definición

Sube con el cáncer de próstata, pero también con el crecimiento benigno de la próstata, la inflamación, la infección y algunas actividades. Es una prueba de tamizaje, no de diagnóstico.

### C. Espécimen y toma

Suero. Evitar eyaculación y bicicleta en las 48 horas previas. Requiere el consentimiento de la visita, que explica riesgos y beneficios (Res. 3280).

### D. Intervalos y umbrales

Corte tradicional: 4,0 ng/mL, o el límite que declare el laboratorio. Zona gris: 4,0 a 10,0 ng/mL, en la que se corre PSA libre como refleja. Existen intervalos por edad, que el médico puede preferir.

### E. Interpretación

De 50 a 75 años se lee como tamizaje formal; fuera de esa edad, como valor a revisar con el médico. Con finasterida o dutasterida, el valor medido se multiplica por 2.

### F. Contexto del paciente y confusores

Eyaculación o ciclismo en 48 horas, prostatitis, infección urinaria, sondaje reciente, inhibidores de 5-alfa reductasa, testosterona exógena.

### G. Relaciones

PSA libre (refleja) en zona gris; infección urinaria con síntomas (M4 IN-A01) como causa de elevación.

### H. Tendencias

La velocidad de cambio entre tomas importa más que un valor aislado cercano al corte.

### I. Prevención

Conversación informada con el médico sobre el tamizaje.

### J. Pruebas complementarias

Tacto rectal, PSA libre, resonancia o biopsia según el médico.

### K. Cuándo no interpretar / cuándo escalar

Sin consentimiento, no se mide. Escalamiento según UR-001.

### L. Evidencia

Res. 3280 de 2018, AUA/SUO 2026. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "PSA por encima del valor de referencia; tiene varias causas, la mayoría benignas".
- Inferencias prohibidas: cáncer, tumor, necesidad de biopsia.
- Revisión profesional: PSA elevado en edad de tamizaje o mayor de 10 ng/mL.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [salud_hombre, prostata, tamizaje, panel_estandar, saludly_brain_v1]
use_when: ["PSA total", "tamizaje de próstata por edad"]
combine_with: [psa_free, urinalysis]
do_not_use_alone: ["diagnóstico de cáncer de próstata"]
do_not_conclude: ["cáncer", "hiperplasia prostática"]
escalate_when: ["PSA elevado de 50 a 75 años", "PSA mayor de 10 ng/mL"]
```

---

## SLD-BIO-111 · Anticuerpos antinucleares por IFI en HEp-2 (ANA)

```yaml
doc_id: "SLD-BIO-111"
biomarker_id: "ana_hep2"
name_es: "Anticuerpos antinucleares por inmunofluorescencia indirecta en células HEp-2"
name_en: "Antinuclear antibodies by indirect immunofluorescence on HEp-2 cells"
abbreviation: "ANA"
sinonimos: ["ANA", "Anticuerpos antinucleares", "AAN", "ANA IFI", "ANA HEp-2", "FAN"]
category: "Inmunología"
parameter_type: "measured_analyte"
tipo_resultado: "semicuantitativo (título y patrón ICAP)"
unidad_canonica: "título (1:x) y patrón (AC-xx)"
specimen: "Suero"
nivel_catalogo: "con patrón"
panel: "estándar, todas las personas"
alimenta: ["COND-M6-RE-A01"]
tier: 2
status: "BORRADOR"
schema_version: "2.1"
clinical_priority: "medium"
requires_professional_review: false
source_version: "2026-10"
fuentes_estado: "por verificar"
```

### A. Identificación

Inmunofluorescencia indirecta sobre células HEp-2, con resultado en título (diluciones 1:80, 1:160, 1:320 y mayores) y patrón según la nomenclatura internacional ICAP (por ejemplo, AC-2 moteado fino denso, AC-4 moteado fino).

### B. Definición

Detecta anticuerpos contra componentes del núcleo celular. Están presentes en casi todas las personas con lupus, pero también en una parte importante de la población sana.

### C. Espécimen y toma

Suero, sin ayuno específico. El laboratorio debe reportar título y patrón; un "positivo" sin título no es interpretable.

### D. Intervalos y umbrales

Negativo: menos de 1:80. Los criterios EULAR/ACR 2019 usan 1:80 o más solo como puerta de entrada para lupus, junto con criterios clínicos. Cerca del 14 % de la población general tiene ANA positivo (Satoh 2012).

### E. Interpretación

A mayor título, mayor probabilidad de que se asocie a enfermedad, pero ningún título diagnostica por sí solo. El patrón AC-2 (moteado fino denso) se asocia con frecuencia a personas sanas.

### F. Contexto del paciente y confusores

Edad (más frecuente en mayores), sexo femenino, infecciones virales recientes, algunos medicamentos, enfermedad tiroidea autoinmune.

### G. Relaciones

Anti-TPO positivo o TSH alta (M2) se asocian a ANA positivo; la vista médica los cruza.

### H. Tendencias

Puede mantenerse positivo por años sin enfermedad; no se usa para seguimiento.

### I. Prevención

No aplica.

### J. Pruebas complementarias

Anti-ENA, anti-ADN de doble cadena y complemento, según el médico y los síntomas.

### K. Cuándo no interpretar / cuándo escalar

Positivo sin título o sin patrón: no interpretable. Escalamiento según RE-A01 (1:80, nivel 1; 1:160 o más, nivel 2).

### L. Evidencia

Satoh 2012 (prevalencia), criterios EULAR/ACR 2019, nomenclatura ICAP. Por verificar.

### M. Seguridad para Saludly Brain

- Inferencias permitidas: "ANA positivo es frecuente en personas sanas; se comenta con el médico, sobre todo si hay síntomas".
- Inferencias prohibidas: lupus, enfermedad autoinmune, "tu sistema inmune te ataca".
- Revisión profesional: 1:160 o más.

```yaml
# RAG_INSTRUCTIONS
rag_tags: [inmunologia, autoinmunidad, ana, panel_estandar, saludly_brain_v1]
use_when: ["ANA positivo o negativo"]
combine_with: [anti_tpo, tsh, esr, hs_crp]
do_not_use_alone: ["diagnóstico de enfermedad autoinmune"]
do_not_conclude: ["lupus", "artritis reumatoide"]
escalate_when: ["título de 1:160 o más", "ANA positivo con síntomas declarados"]
```

---

## Firma médica de la tanda

Las fichas de biomarcador no llevan firma una por una. El médico revisa la tanda completa y marca aquí las que aprueba o cambia.

| Ficha | Aprobada | Cambios |
| --- | --- | --- |
| SLD-BIO-101 Uroanálisis | \[ \] |  |
| SLD-BIO-102 FIT | \[ \] |  |
| SLD-BIO-103 *H. pylori* | \[ \] |  |
| SLD-BIO-104 Coprológico | \[ \] |  |
| SLD-BIO-105 Anti-VHC | \[ \] |  |
| SLD-BIO-106 HBsAg | \[ \] |  |
| SLD-BIO-107 Anti-HBs | \[ \] |  |
| SLD-BIO-108 Anti-HBc | \[ \] |  |
| SLD-BIO-109 ELISA Chagas | \[ \] |  |
| SLD-BIO-110 PSA | \[ \] |  |
| SLD-BIO-111 ANA | \[ \] |  |

- Nombre y registro ReTHUS:
- Fecha: