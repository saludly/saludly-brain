# Módulo M1 · Cardiometabólico — Fichas de condición

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento convierte las condiciones de Cardiología y Endocrinología metabólica (Lote 1) en reglas que el motor puede ejecutar. Son 16 fichas: 12 condiciones incluidas y 4 de apoyo. Cada una trae su regla en formato estructurado, el texto que el paciente puede leer, las frases prohibidas, dos o más casos de prueba y un espacio para la firma del médico.

Ninguna ficha produce un diagnóstico. Cada una describe una asociación con un nivel de coincidencia y una recomendación de seguimiento.

## Cómo leer una ficha

| Campo | Qué significa |
| --- | --- |
| `tipo` | **incluida**: aparece en el informe con su nombre. **apoyo**: modifica otra condición y no aparece sola |
| `detectabilidad` | **D1**: el laboratorio basta. **D2**: necesita medidas de la enfermera o cuestionario. **D3**: señal parcial; confirmarla exige una prueba que Saludly no hace |
| `criterios` | Cada señal que el motor evalúa, con su umbral y unidad |
| `regla_central` | Qué combinación de criterios activa la condición |
| `coincidencia` | **alta**: todos los criterios centrales con datos completos. **moderada**: criterios centrales con datos incompletos, o uno central más apoyo. **baja**: solo apoyo; se muestra como "vigilar" |
| `escalamiento` | **0** informativo · **1** comentarlo en el próximo control · **2** consulta médica en las próximas semanas · **3** el equipo médico llama el mismo día hábil |
| `nivel_lenguaje` | Resultado observado, patrón compatible, riesgo potencial o condición que requiere evaluación médica |
| `por_verificar` | Lo que todavía no está confirmado en la fuente completa y el médico debe mirar con más cuidado |

## Cómo firmar

1. Lee cada ficha completa, incluidos los casos de prueba: son el comportamiento exacto que tendrá el sistema.
2. Marca una opción en el bloque de firma: aprobada, aprobada con cambios o rechazada.
3. Si cambias algo (un umbral, un nivel de escalamiento, una frase), escríbelo en "Cambios"; el equipo lo aplica y vuelve a correr los casos.
4. Pon tu nombre, tu número de registro (ReTHUS) y la fecha.

Mientras una ficha no esté firmada, el motor la usa solo con datos de prueba, nunca con pacientes reales.

## Índice

| ID | Condición | Tipo | Detectabilidad | Datos que usa | Escalamiento |
| --- | --- | --- | --- | --- | --- |
| COND-M1-CA-001 | Dislipidemia aterogénica | Incluida | D1 | LDL, no-HDL, HDL, triglicéridos | 1 |
| COND-M1-CA-002 | Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar | Incluida | D2 | LDL, antecedente familiar | 2 |
| COND-M1-CA-003 | Hipertrigliceridemia | Incluida | D1 | Triglicéridos, ayuno, alcohol | 1 o 2 |
| COND-M1-CA-004 | Lipoproteína(a) elevada | Incluida | D1 | Lp(a) con su unidad | 1 |
| COND-M1-CA-005 | Riesgo cardiovascular global elevado | Incluida | D2 | Edad, sexo, presión, tabaquismo, colesterol, HDL, diabetes | 1 o 2 |
| COND-M1-CA-006 | Hipertensión arterial o presión elevada (sospecha) | Incluida | D3 | Presión de la enfermera, automonitoreo en Apple Health | 1, 2 o 3 |
| COND-M1-CA-007 | Riesgo de insuficiencia cardíaca en personas con diabetes | Incluida | D3 | NT-proBNP, diabetes | 2 |
| COND-M1-CA-A01 | Discordancia ApoB / LDL | Apoyo | D1 | ApoB, LDL, triglicéridos | Modifica CA-001 y CA-005 |
| COND-M1-CA-A02 | Inflamación de bajo grado | Apoyo | D3 | hs-CRP, infección reciente | Modifica CA-005 |
| COND-M1-EM-001 | Prediabetes | Incluida | D1 | Glucosa, HbA1c | 1 |
| COND-M1-EM-002 | Diabetes tipo 2 en rango diagnóstico | Incluida | D1 | Glucosa, HbA1c | 2 |
| COND-M1-EM-003 | Síndrome metabólico | Incluida | D2 | Cintura, triglicéridos, HDL, presión, glucosa | 1 |
| COND-M1-EM-004 | Obesidad y sobrepeso | Incluida | D2 | Peso, talla, cintura | 1 o 2 |
| COND-M1-EM-005 | Glucosa baja en ayunas | Incluida | D3 | Glucosa, tubo y tiempo de proceso, medicamentos | 1, 2 o 3 |
| COND-M1-EM-A01 | Riesgo alto de diabetes (FINDRISC) | Apoyo | D2 | Cuestionario FINDRISC | Modifica EM-001 |
| COND-M1-EM-A02 | Resistencia a la insulina (HOMA-IR) | Apoyo | D1 | Insulina, glucosa, HOMA-IR | Modifica EM-001 y EM-003 |

Descartadas en el Lote 1 y fuera de este módulo: homocisteína como riesgo cardiovascular (pasa a Nutrición), lesión miocárdica por troponina (la troponina queda como "solo valor y rango" con su regla de seguridad), fibrilación auricular, diabetes tipo 1 o LADA y diabetes gestacional.

---

## COND-M1-CA-001 · Dislipidemia aterogénica

**Qué detecta.** Colesterol LDL o no-HDL por encima de los cortes de tamizaje, con o sin HDL bajo y triglicéridos altos. Su importancia real depende del riesgo cardiovascular global (CA-005).

```yaml
id: COND-M1-CA-001
nombre: Dislipidemia aterogénica
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: ldl_alto
    biomarcador: ldl_c
    condicion: ">= 130"
    unidad: mg/dL
  - id: no_hdl_alto
    biomarcador: non_hdl_c
    condicion: ">= 160"
    unidad: mg/dL
  - id: hdl_bajo
    biomarcador: hdl_c
    condicion: "< 40 si hombre; < 50 si mujer"
    unidad: mg/dL
  - id: tg_alto
    biomarcador: triglycerides
    condicion: ">= 150"
    unidad: mg/dL
regla_central: "ldl_alto OR no_hdl_alto"
contexto_obligatorio: ["ayuno_horas >= 8 si el LDL es calculado", "embarazo == false"]
excluye_si: ["COND-M1-CA-002"]
coincidencia:
  alta: "ldl_alto AND no_hdl_alto"
  moderada: "ldl_alto XOR no_hdl_alto"
  baja: "hdl_bajo AND tg_alto AND NOT (ldl_alto OR no_hdl_alto)"
escalamiento: 1
modificado_por: ["COND-M1-CA-A01"]
nivel_lenguaje: riesgo_potencial
confusores: ["ayuno_insuficiente", "tsh_alta (causa secundaria posible)", "estatina_en_uso (se lee como control, no como detección)"]
guias: ["GPC Colombia dislipidemias 2014", "ACC/AHA 2026, manejo de dislipidemia"]
por_verificar: "Los cortes de 130 y 160 mg/dL son cortes operativos de tamizaje. Las guías fijan metas según el riesgo global, no un corte único."
frase_permitida: "Tu colesterol LDL está por encima del valor que usamos para tamizaje. Lo que significa para ti depende de tu riesgo cardiovascular global, que conviene revisar con tu médico."
frases_prohibidas: ["tienes dislipidemia", "tienes enfermedad cardiovascular", "debes tomar estatinas", "tu colesterol es peligroso"]
recomendaciones_sugeridas: ["fibra soluble y leguminosas", "menos grasa saturada y ultraprocesados", "actividad aeróbica la mayoría de días"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | LDL 142, colesterol total 228, HDL 36 (no-HDL 192), triglicéridos 238 | Activa, coincidencia alta, escalamiento 1 |
| Positivo moderado · PDF mujer 34 años | LDL 136, colesterol total 214, HDL 58 (no-HDL 156) | Activa, coincidencia moderada, escalamiento 1 |
| Negativo | LDL 110, colesterol total 185, HDL 50 (no-HDL 135) | No activa |
| Vigilar | LDL 120, no-HDL 150, HDL 35 (hombre), triglicéridos 210 | No activa como condición; se muestra como "vigilar" |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-002 · Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar

**Qué detecta.** LDL mayor o igual a 190 mg/dL. La GPC colombiana trata este nivel como riesgo alto sin necesidad de calculadora. El antecedente familiar de evento cardiovascular temprano refuerza la sospecha de origen familiar.

```yaml
id: COND-M1-CA-002
nombre: Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D2
criterios:
  - id: ldl_muy_alto
    biomarcador: ldl_c
    condicion: ">= 190"
    unidad: mg/dL
  - id: antecedente_familiar
    contexto: antecedente_familiar_cv_temprano
    condicion: "familiar de primer grado: hombre < 55 años o mujer < 65 años"
regla_central: "ldl_muy_alto"
contexto_obligatorio: ["embarazo == false"]
excluye_si: []
coincidencia:
  alta: "ldl_muy_alto AND antecedente_familiar"
  moderada: "ldl_muy_alto AND (NOT antecedente_familiar OR antecedente_familiar desconocido)"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["tsh_alta (hipotiroidismo como causa secundaria)", "albuminuria importante (causa renal secundaria)", "estatina_en_uso"]
guias: ["GPC Colombia dislipidemias 2014"]
por_verificar: "Criterios diagnósticos formales de hipercolesterolemia familiar (por ejemplo, Dutch Lipid Clinic) no se aplican en la versión 1."
frase_permitida: "Tu colesterol LDL está en un nivel que las guías consideran alto por sí solo. Conviene una consulta médica en las próximas semanas, y que tus familiares cercanos también se lo revisen."
frases_prohibidas: ["tienes hipercolesterolemia familiar", "es genético", "vas a tener un infarto"]
recomendaciones_sugeridas: ["consulta médica", "revisión del perfil lipídico en familiares de primer grado", "alimentación baja en grasa saturada"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo alto | LDL 205, padre con infarto a los 50 años | Activa, coincidencia alta, escalamiento 2; desplaza a CA-001 |
| Positivo moderado | LDL 196, sin dato de antecedente | Activa, coincidencia moderada, escalamiento 2 |
| Negativo | LDL 175 | No activa (CA-001 sí puede activarse) |
| Con confusor | LDL 198, TSH 9,5 | Activa; la vista médica muestra hipotiroidismo como posible causa secundaria |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-003 · Hipertrigliceridemia

**Qué detecta.** Triglicéridos en ayunas mayores o iguales a 150 mg/dL. Desde 500 mg/dL sube el escalamiento; desde 1.000 mg/dL la guía añade la prevención de pancreatitis. La urgencia solo sale de una bandera crítica del laboratorio o de síntomas.

```yaml
id: COND-M1-CA-003
nombre: Hipertrigliceridemia
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: tg_alto
    biomarcador: triglycerides
    condicion: ">= 150"
    unidad: mg/dL
  - id: tg_muy_alto
    biomarcador: triglycerides
    condicion: ">= 500"
    unidad: mg/dL
  - id: tg_severo
    biomarcador: triglycerides
    condicion: ">= 1000"
    unidad: mg/dL
regla_central: "tg_alto"
contexto_obligatorio: ["ayuno_horas >= 8"]
excluye_si: []
coincidencia:
  alta: "tg_alto AND ayuno confirmado AND NOT alcohol_48h"
  moderada: "tg_alto AND (alcohol_48h OR dato de alcohol faltante)"
escalamiento:
  base: 1
  si_tg_muy_alto: 2
  si_bandera_critica_laboratorio: 3
nivel_lenguaje: riesgo_potencial
confusores: ["ayuno_insuficiente (no interpretable)", "alcohol_48h", "diabetes descontrolada", "corticoides"]
guias: ["ACC/AHA 2026, manejo de dislipidemia"]
por_verificar: "Una sola medición no demuestra persistencia; el texto lo dice y sugiere repetir."
frase_permitida: "Tus triglicéridos están por encima del rango deseable en esta medición. Conviene repetirlos y revisar alimentación y alcohol."
frase_permitida_tg_severo: "Tus triglicéridos están muy altos. Las guías piden atención médica en este nivel para prevenir complicaciones como la inflamación del páncreas."
frases_prohibidas: ["tienes pancreatitis", "tienes enfermedad cardiovascular"]
recomendaciones_sugeridas: ["reducir azúcar, harinas refinadas y alcohol", "actividad física regular", "repetir la medición"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Triglicéridos 238, ayuno 11 h | Activa, coincidencia alta, escalamiento 1 |
| Muy alto | Triglicéridos 620, ayuno 10 h | Activa, escalamiento 2 |
| Severo | Triglicéridos 1.150 | Activa, escalamiento 2, frase de triglicéridos severos |
| Sin ayuno | Triglicéridos 260, ayuno 4 h | No interpretable; no activa |
| Negativo · PDF mujer 34 años | Triglicéridos 98 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-004 · Lipoproteína(a) elevada

**Qué detecta.** Lp(a) por encima de 50 mg/dL o de 105 nmol/L (ESC/EAS). Es un factor de riesgo heredado y estable: se mide una vez en la vida. La unidad del laboratorio es obligatoria, porque mg/dL y nmol/L no se convierten de forma confiable entre sí.

```yaml
id: COND-M1-CA-004
nombre: Lipoproteína(a) elevada
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: lpa_alta_mg
    biomarcador: lpa
    condicion: "> 50"
    unidad: mg/dL
  - id: lpa_alta_nmol
    biomarcador: lpa
    condicion: "> 105"
    unidad: nmol/L
  - id: lpa_alta_acc
    biomarcador: lpa
    condicion: ">= 125"
    unidad: nmol/L
    nota: "corte ACC/AHA 2026; se menciona en la vista médica"
regla_central: "lpa_alta_mg OR lpa_alta_nmol"
contexto_obligatorio: ["unidad declarada por el laboratorio"]
excluye_si: []
coincidencia:
  alta: "regla_central con unidad declarada"
escalamiento: 1
nivel_lenguaje: riesgo_potencial
confusores: []
reglas_especiales: ["no convertir entre mg/dL y nmol/L", "no repetir en tomas futuras salvo indicación médica"]
guias: ["ESC/EAS 2025, actualización de dislipidemias", "ACC/AHA 2026"]
frase_permitida: "Tu lipoproteína(a) está alta. Es un factor que se hereda y que suma al riesgo cardiovascular; conviene comentarlo con tu médico y que tus familiares cercanos se la midan una vez."
frases_prohibidas: ["vas a tener un infarto", "tienes enfermedad cardiovascular", "esto se cura con dieta"]
recomendaciones_sugeridas: ["controlar los demás factores de riesgo (LDL, presión, tabaco)", "medición en familiares de primer grado"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | Lp(a) 64 mg/dL | Activa, coincidencia alta, escalamiento 1 |
| Negativo · PDF hombre 46 años | Lp(a) 18 mg/dL | No activa |
| Unidad nmol/L | Lp(a) 140 nmol/L | Activa; la vista médica menciona también el corte ACC/AHA |
| Sin unidad | Lp(a) 70, unidad vacía | No interpretable; no activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-005 · Riesgo cardiovascular global elevado

**Qué detecta.** Riesgo a 10 años de un evento cardiovascular fatal o no fatal, con SCORE2 recalibrado para Colombia (SCORE2-PURE), la calculadora que adopta la GPC colombiana de hipertensión de 2025. Se usa el algoritmo SCORE2 de la región de riesgo alto y el resultado se multiplica por 0,61 en hombres y 0,75 en mujeres, los factores del estudio PURE-Colombia (2025). Solo se calcula entre 40 y 69 años, sin diabetes ni enfermedad cardiovascular, y con todos los datos. Fuera de eso se muestran los factores de riesgo sin porcentaje.

```yaml
id: COND-M1-CA-005
nombre: Riesgo cardiovascular global elevado
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D2
entradas:
  - edad (40 a 69 años)
  - sexo
  - presion_sistolica (enfermera)
  - tabaquismo actual (enfermera)
  - total_cholesterol (mg/dL; se convierte a mmol/L dividiendo por 38,67)
  - hdl_c (mg/dL; misma conversión)
calculadora:
  modelo: "SCORE2 (SCORE2 working group, Eur Heart J 2021), coeficientes por sexo con interacciones por edad"
  region: "riesgo alto (la que usó PURE-Colombia según la mortalidad cardiovascular colombiana)"
  recalibracion_colombia: {hombres: 0.61, mujeres: 0.75, fuente: "Lopez-Lopez et al., PURE-Colombia, Eur J Prev Cardiol 2025;32:564-72"}
  verificacion: "reproduce exactamente el ejemplo publicado del artículo SCORE2 (5,9 % y 14,0 % en hombres; 4,2 % y 13,7 % en mujeres)"
  implementacion: "motor/score2.py"
categorias_provisionales:
  menores_de_50: {bajo_moderado: "< 2,5 %", alto: "2,5 a < 7,5 %", muy_alto: ">= 7,5 %"}
  de_50_a_69: {bajo_moderado: "< 5 %", alto: "5 a < 10 %", muy_alto: ">= 10 %"}
regla_central: "categoria in [alto, muy_alto]"
contexto_obligatorio: ["todas las entradas presentes", "edad entre 40 y 69"]
no_calcular_si: ["enfermedad cardiovascular establecida declarada", "diabetes conocida o HbA1c >= 6,5", "COND-M1-CA-002 activa (LDL >= 190)", "embarazo"]
coincidencia:
  alta: "regla_central con todas las entradas"
modificado_por: ["COND-M1-CA-A01", "COND-M1-CA-A02", "COND-M1-CA-004"]
escalamiento:
  alto: 1
  muy_alto: 2
nivel_lenguaje: riesgo_potencial
guias: ["GPC Colombia HTA 2025 (Minsalud e IETS)", "SCORE2 working group, Eur Heart J 2021", "PURE-Colombia, Eur J Prev Cardiol 2025"]
por_verificar: "Las categorías de riesgo son las de la ESC 2021 por edad; falta confirmar si la GPC HTA 2025 usa las mismas. En diabetes, la calculadora no aplica y decide el médico (SCORE2-Diabetes no está implementado)."
frase_permitida: "Con tu edad, presión, colesterol y hábitos, tu riesgo estimado de un evento cardiovascular en los próximos 10 años es de {riesgo} %, en la categoría {categoria}. Es una estimación de un modelo ajustado a población colombiana, no una predicción segura."
frases_prohibidas: ["vas a tener un infarto", "porcentaje de riesgo fuera de 40 a 69 años o sin datos completos"]
recomendaciones_sugeridas: ["dejar de fumar si aplica", "control de presión", "actividad física", "consulta para definir metas de colesterol"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Incompleto · PDF hombre 46 años sin datos de la enfermera | Edad 46, colesterol 228, HDL 36; falta presión y tabaquismo | No se calcula; se listan los factores y lo que falta |
| Bajo · PDF hombre 46 años con datos de la enfermera | Presión 128, no fumador, colesterol 228, HDL 36 | 2,2 %, bajo a moderado; no activa |
| Fuera de edad · PDF mujer 34 años | Edad 34 | No se calcula; se muestran factores sin porcentaje |
| Con diabetes | Edad 58, HbA1c 7,1 | No se calcula; la vista médica lo explica |
| Muy alto | Hombre 62 años, presión 152, fumador, colesterol 245, HDL 38 | 13,1 % (21,5 % antes de recalibrar), muy alto, escalamiento 2 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-006 · Hipertensión arterial o presión elevada (sospecha)

**Qué detecta.** Presión de 130/80 mmHg o más en la toma de la enfermera. Siempre es sospecha: la guía colombiana pide confirmar con automonitoreo en casa o con monitoreo ambulatorio. Si el paciente registra su presión con tensiómetro en Apple Health, esos registros cuentan como automonitoreo para el médico.

```yaml
id: COND-M1-CA-006
nombre: Hipertensión arterial o presión elevada (sospecha)
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: pa_elevada
    contexto: presion_enfermera
    condicion: "sistólica >= 130 OR diastólica >= 80"
    unidad: mmHg
    medicion: "promedio de las 2 últimas de 3 tomas, sentado, tras 5 minutos de reposo, tensiómetro validado"
  - id: pa_grado_2
    contexto: presion_enfermera
    condicion: "sistólica >= 140 OR diastólica >= 90"
  - id: pa_severa
    contexto: presion_enfermera
    condicion: "sistólica >= 180 OR diastólica >= 120"
  - id: ampa_confirma
    contexto: apple_health_presion
    condicion: "promedio de al menos 7 días de registros >= 130/80"
regla_central: "pa_elevada"
contexto_obligatorio: ["presión medida por la enfermera"]
excluye_si: ["hipertensión diagnosticada declarada (se lee como control, no como detección)"]
coincidencia:
  alta: "pa_elevada AND ampa_confirma"
  moderada: "pa_elevada sin automonitoreo"
escalamiento:
  base: 1
  si_pa_grado_2: 2
  si_pa_severa: 3
dispara: ["reflejas aldosterona y renina", "revisión del estudio inicial: creatinina, TFG, uroanálisis, albúmina/creatinina, sodio, potasio, TSH y ácido úrico (ya en el panel)"]
contexto_adicional: ["notificación de hipertensión del Apple Watch: refuerza la recomendación de confirmar, no cambia la coincidencia"]
nivel_lenguaje: patron_compatible
confusores: ["dolor, ansiedad o esfuerzo antes de la toma", "café o cigarrillo 30 minutos antes", "manguito de tamaño inadecuado"]
guias: ["GPC Colombia HTA 2025 (Minsalud e IETS)", "AHA/ACC 2025, presión arterial alta"]
por_verificar: "El umbral de 180/120 como presión severa sale de AHA/ACC 2025, leída solo por resultado de búsqueda. Leer la guía completa antes de la firma."
frase_permitida: "Tu presión en la visita estuvo en {valor}, por encima de 130/80. Una sola toma no confirma hipertensión: conviene medirla en casa varios días con un tensiómetro validado y revisarlo con tu médico."
frase_permitida_severa: "Tu presión estuvo muy alta en la visita. Nuestro equipo médico te va a llamar hoy. Si tienes dolor de pecho, dolor de cabeza intenso, dificultad para hablar o falta de aire, ve a urgencias."
frases_prohibidas: ["eres hipertenso", "tienes hipertensión", "el reloj detectó hipertensión"]
recomendaciones_sugeridas: ["automonitoreo 7 días, mañana y noche", "reducir sal", "actividad física", "reducir alcohol"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo grado 1 | Promedio 134/84, sin automonitoreo | Activa, coincidencia moderada, escalamiento 1; activa aldosterona y renina |
| Positivo grado 2 con confirmación | Promedio 146/92; Apple Health con promedio de 7 días 141/89 | Activa, coincidencia alta, escalamiento 2 |
| Severa | Promedio 184/112 | Activa, escalamiento 3, llamada el mismo día |
| Negativo | Promedio 118/76 | No activa |
| Hipertensión conocida | Promedio 138/86, toma antihipertensivo | No activa como detección; la vista médica muestra control |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-007 · Riesgo de insuficiencia cardíaca en personas con diabetes

**Qué detecta.** NT-proBNP de 125 pg/mL o más en una persona con diabetes. Es una señal parcial: confirmar o descartar insuficiencia cardíaca exige un ecocardiograma, que Saludly no hace. Solo se mide en personas con diabetes.

```yaml
id: COND-M1-CA-007
nombre: Riesgo de insuficiencia cardíaca en personas con diabetes
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: ntprobnp_alto
    biomarcador: nt_probnp
    condicion: ">= 125"
    unidad: pg/mL
  - id: diabetes
    condicion: "diabetes conocida declarada OR COND-M1-EM-002 activa"
regla_central: "ntprobnp_alto AND diabetes"
activacion_de_la_prueba: "refleja cuando glucosa o HbA1c están en rango de diabetes; propuesta: también cuando la enfermera registra diabetes conocida"
contexto_obligatorio: ["diabetes"]
excluye_si: []
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con TFG < 60, fibrilación auricular declarada o edad >= 75"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["edad avanzada", "fibrilación auricular", "enfermedad renal (TFG baja)", "obesidad (puede bajar el valor)"]
guias: ["ADA Standards of Care (vía Diabetes Care 2025)"]
por_verificar: "Diabetes Care 2025 cuestiona la evidencia del tamizaje; por eso queda como señal parcial."
frase_permitida: "En personas con diabetes, un valor de NT-proBNP como el tuyo es una señal para revisar la función del corazón. No es un diagnóstico: el médico puede pedir un ecocardiograma."
frases_prohibidas: ["tienes insuficiencia cardíaca", "tu corazón está fallando"]
recomendaciones_sugeridas: ["consulta médica", "control de la diabetes y la presión"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | HbA1c 7,2, glucosa 148, NT-proBNP 210 | Activa, coincidencia alta, escalamiento 2 |
| Con confusor | Diabetes conocida, NT-proBNP 180, TFG 48 | Activa, coincidencia moderada |
| Negativo | Diabetes conocida, NT-proBNP 60 | No activa |
| Sin diabetes | Sin diabetes; la prueba no se pidió | No aplica |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-A01 · Discordancia ApoB / LDL (apoyo)

**Qué detecta.** ApoB alta con LDL controlado: hay más partículas aterogénicas de las que el LDL sugiere. Es más útil con triglicéridos mayores de 200 mg/dL o con diabetes. No aparece sola: refuerza CA-001 y CA-005 en la vista médica.

```yaml
id: COND-M1-CA-A01
nombre: Discordancia ApoB / LDL
modulo: M1
especialidad: cardiologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: apob_alta
    biomarcador: apob
    condicion: ">= 130"
    unidad: mg/dL
    nota: "percentil 90 aproximado en adultos no tratados (NLA 2024)"
  - id: ldl_no_alto
    biomarcador: ldl_c
    condicion: "< 130"
    unidad: mg/dL
  - id: contexto_util
    condicion: "triglycerides > 200 OR diabetes"
regla_central: "apob_alta AND ldl_no_alto"
modifica: ["COND-M1-CA-001", "COND-M1-CA-005"]
efecto: "Si CA-001 no está activa, se muestra como vigilar en la vista médica. Si contexto_util se cumple, se destaca."
guias: ["ACC/AHA 2026", "NLA 2024 (consenso de expertos)"]
por_verificar: "Corte de discordancia operativo; las guías no fijan uno único."
frase_permitida_medico: "ApoB por encima del percentil 90 con LDL menor de 130 mg/dL: posible subestimación del riesgo por LDL."
frases_prohibidas: ["tu colesterol engaña", "tienes enfermedad cardiovascular"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | ApoB 138, LDL 118, triglicéridos 240 | Activa como apoyo destacado |
| Negativo · PDF hombre 46 años | ApoB 118, LDL 142 | No activa (no hay discordancia: ambos altos) |
| Negativo | ApoB 95, LDL 110 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-CA-A02 · Inflamación de bajo grado (apoyo)

**Qué detecta.** hs-CRP mayor de 2 mg/L sin infección reciente: modifica el riesgo cardiovascular. Una sola medición no basta; la guía pide una segunda sin infección. Por encima de 10 mg/L sugiere un proceso agudo y no se usa como riesgo cardiovascular.

```yaml
id: COND-M1-CA-A02
nombre: Inflamación de bajo grado
modulo: M1
especialidad: cardiologia
tipo: apoyo
detectabilidad: D3
criterios:
  - id: hscrp_alta
    biomarcador: hs_crp
    condicion: "> 2 AND <= 10"
    unidad: mg/L
  - id: hscrp_aguda
    biomarcador: hs_crp
    condicion: "> 10"
    unidad: mg/L
regla_central: "hscrp_alta AND NOT infeccion_reciente_2_semanas"
modifica: ["COND-M1-CA-005"]
efecto: "Vista médica: modificador de riesgo a confirmar con una segunda medición. Si hscrp_aguda, no modifica y se sugiere repetir."
confusores: ["infección o fiebre en 2 semanas", "ejercicio intenso en 48 horas", "obesidad", "tabaquismo"]
guias: ["ESC/EAS 2025 (modificador de riesgo)"]
por_verificar: "El corte de 2 mg/L viene del texto del Focused Update citado por la ESC; confirmar en el documento completo."
frase_permitida_medico: "hs-CRP de {valor} mg/L sin infección declarada: posible modificador de riesgo; repetir para confirmar."
frases_prohibidas: ["tienes inflamación", "tienes una infección"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | hs-CRP 3,4, sin infección declarada | Activa como apoyo, a confirmar |
| Con confusor | hs-CRP 4,1, infección respiratoria hace 1 semana | No activa; se sugiere repetir |
| Proceso agudo | hs-CRP 18 | No activa; se sugiere repetir |
| Negativo · PDF mujer 34 años | hs-CRP 0,8 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-001 · Prediabetes

**Qué detecta.** Glucosa en ayunas entre 100 y 125 mg/dL o HbA1c entre 5,7 y 6,4 %. Si las dos están en ese rango en la misma muestra, la coincidencia es alta.

```yaml
id: COND-M1-EM-001
nombre: Prediabetes
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D1
criterios:
  - id: glucosa
    biomarcador: glucose
    condicion: "entre 100 y 125"
    unidad: mg/dL
  - id: hba1c
    biomarcador: hba1c
    condicion: "entre 5.7 y 6.4"
    unidad: "%"
regla_central: "glucosa OR hba1c"
contexto_obligatorio: ["ayuno_horas >= 8 (para glucosa)", "embarazo == false"]
excluye_si: ["COND-M1-EM-002", "diabetes conocida declarada"]
coincidencia:
  alta: "glucosa AND hba1c"
  moderada: "glucosa XOR hba1c"
modificado_por: ["COND-M1-EM-A01", "COND-M1-EM-A02"]
escalamiento: 1
nivel_lenguaje: riesgo_potencial
confusores: ["corticoides", "ayuno_insuficiente", "anemia o hemoglobinopatía (baja la confianza en HbA1c; manda la glucosa)", "HbA1c sin método certificado NGSP"]
guias: ["ADA Standards of Care 2026, sección 2", "GPC Colombia DM2 2016"]
frase_permitida: "Tus resultados de glucosa están en un rango que las guías asocian con mayor riesgo de desarrollar diabetes. Es el mejor momento para actuar: pequeños cambios hacen una diferencia grande."
frases_prohibidas: ["tienes prediabetes", "eres prediabético", "vas a ser diabético"]
recomendaciones_sugeridas: ["caminata de 15 minutos después de las comidas principales", "cambiar bebidas azucaradas por agua", "más fibra", "sueño regular"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Glucosa 112, HbA1c 6,0, ayuno 11 h | Activa, coincidencia alta, escalamiento 1; HOMA-IR 5,5 como apoyo |
| Positivo moderado | Glucosa 94, HbA1c 5,9 | Activa, coincidencia moderada |
| Negativo · PDF mujer 34 años | Glucosa 86, HbA1c 5,2 | No activa |
| Con anemia | Glucosa 92, HbA1c 5,8, hemoglobina 10,9 | Activa con coincidencia baja ("vigilar"): la HbA1c pierde confianza con anemia |
| Diabetes | Glucosa 131, HbA1c 6,7 | No activa (manda EM-002) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-002 · Diabetes tipo 2 en rango diagnóstico

**Qué detecta.** Glucosa en ayunas de 126 mg/dL o más, o HbA1c de 6,5 % o más. La ADA 2026 acepta como confirmación dos pruebas distintas alteradas en la misma muestra; si solo una está en rango, hay que repetir. El tipo exacto de diabetes no se puede clasificar con este panel.

```yaml
id: COND-M1-EM-002
nombre: Diabetes tipo 2 en rango diagnóstico
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D1
criterios:
  - id: glucosa_dm
    biomarcador: glucose
    condicion: ">= 126"
    unidad: mg/dL
  - id: hba1c_dm
    biomarcador: hba1c
    condicion: ">= 6.5"
    unidad: "%"
regla_central: "glucosa_dm OR hba1c_dm"
contexto_obligatorio: ["ayuno_horas >= 8 (para glucosa)", "embarazo == false"]
excluye_si: ["diabetes conocida declarada (se lee como control de diabetes en la vista médica)"]
coincidencia:
  alta: "glucosa_dm AND hba1c_dm"
  moderada: "glucosa_dm XOR hba1c_dm"
escalamiento:
  base: 2
  si_bandera_critica_laboratorio: 3
dispara: ["refleja NT-proBNP (COND-M1-CA-007)"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["corticoides", "ayuno_insuficiente", "anemia o hemoglobinopatía (HbA1c)", "enfermedad aguda reciente"]
guias: ["ADA Standards of Care 2026, sección 2", "GPC Colombia DM2 2016"]
por_verificar: "Diabetes tipo 1 o LADA exigen autoanticuerpos que no ofrecemos; el texto no afirma el tipo."
frase_permitida_alta: "Tu glucosa y tu HbA1c están en el rango que las guías usan para diagnosticar diabetes. Necesitas una consulta médica en las próximas semanas para confirmarlo y empezar el manejo."
frase_permitida_moderada: "Uno de tus resultados de glucosa está en el rango que las guías usan para diagnosticar diabetes. Hay que repetirlo para confirmar; te recomendamos consulta médica."
frases_prohibidas: ["tienes diabetes", "eres diabético", "necesitas insulina", "toma metformina"]
recomendaciones_sugeridas: ["consulta médica", "reducir azúcares y bebidas azucaradas", "actividad física diaria"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo alto | Glucosa 138, HbA1c 6,9 | Activa, coincidencia alta, escalamiento 2; activa NT-proBNP |
| Positivo moderado | Glucosa 128, HbA1c 6,1 | Activa, coincidencia moderada, frase de repetir |
| Negativo · PDF hombre 46 años | Glucosa 112, HbA1c 6,0 | No activa (manda EM-001) |
| Diabetes conocida | Glucosa 150, HbA1c 7,4, metformina | No activa como detección; vista médica de control |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-003 · Síndrome metabólico

**Qué detecta.** Tres o más de cinco componentes, según la declaración armonizada de 2009, con cortes de cintura para población centro y suramericana. Tres componentes salen del laboratorio y dos de la enfermera.

```yaml
id: COND-M1-EM-003
nombre: Síndrome metabólico
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D2
criterios:
  - id: cintura
    contexto: cintura_cm
    condicion: ">= 90 si hombre; >= 80 si mujer"
  - id: trigliceridos
    biomarcador: triglycerides
    condicion: ">= 150 OR medicamento para triglicéridos"
    unidad: mg/dL
  - id: hdl
    biomarcador: hdl_c
    condicion: "< 40 si hombre; < 50 si mujer; OR medicamento para HDL"
    unidad: mg/dL
  - id: presion
    contexto: presion_enfermera
    condicion: "sistólica >= 130 OR diastólica >= 85 OR antihipertensivo"
  - id: glucosa
    biomarcador: glucose
    condicion: ">= 100 OR hipoglucemiante"
    unidad: mg/dL
regla_central: "al menos 3 de [cintura, trigliceridos, hdl, presion, glucosa]"
contexto_obligatorio: ["ayuno_horas >= 8"]
excluye_si: []
coincidencia:
  alta: "regla_central con los 5 componentes medidos"
  moderada: "regla_central con algún componente sin medir"
  incompleto: "menos de 3 cumplidos pero los componentes faltantes podrían completar 3"
modificado_por: ["COND-M1-EM-A02"]
escalamiento: 1
nivel_lenguaje: patron_compatible
confusores: ["ayuno_insuficiente", "corticoides"]
guias: ["Declaración armonizada IDF/AHA/NHLBI 2009"]
reglas_especiales: ["el corte de cintura de 94 y 90 cm solo se usa dentro de FINDRISC"]
frase_permitida: "Tienes {n} de los 5 componentes que forman el síndrome metabólico, un conjunto que aumenta el riesgo de diabetes y enfermedad cardiovascular. La buena noticia es que todos mejoran con los mismos cambios de hábitos."
frases_prohibidas: ["tienes síndrome metabólico", "estás enfermo"]
recomendaciones_sugeridas: ["actividad física regular", "reducir azúcares y harinas refinadas", "control de peso y cintura", "sueño regular"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo moderado · PDF hombre 46 años sin datos de la enfermera | Triglicéridos 238, HDL 36, glucosa 112; falta cintura y presión | Activa con 3 de 5, coincidencia moderada; dice que faltan cintura y presión |
| Positivo alto | Lo anterior más cintura 98 cm y presión 128/82 | Activa con 4 de 5, coincidencia alta |
| Incompleto | Triglicéridos 170, HDL 52 (hombre), glucosa 92; falta cintura y presión | No activa; se marca incompleto |
| Negativo · PDF mujer 34 años | Triglicéridos 98, HDL 58, glucosa 86; cintura 74, presión 112/70 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-004 · Obesidad y sobrepeso

**Qué detecta.** Índice de masa corporal (peso / talla²) de 25 o más (sobrepeso) o de 30 o más (obesidad), con peso y talla medidos por la enfermera. La cintura agrega la adiposidad central.

```yaml
id: COND-M1-EM-004
nombre: Obesidad y sobrepeso
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D2
calculo: "imc = peso_kg / talla_m^2"
criterios:
  - id: sobrepeso
    condicion: "imc >= 25 AND imc < 30"
  - id: obesidad
    condicion: "imc >= 30"
  - id: obesidad_clase_3
    condicion: "imc >= 40"
  - id: adiposidad_central
    contexto: cintura_cm
    condicion: ">= 90 si hombre; >= 80 si mujer"
regla_central: "sobrepeso OR obesidad"
contexto_obligatorio: ["peso y talla medidos por la enfermera", "embarazo == false"]
excluye_si: []
coincidencia:
  alta: "regla_central con peso y talla medidos"
escalamiento:
  base: 1
  si_obesidad_clase_3: 2
nivel_lenguaje: resultado_observado
confusores: ["masa muscular alta (el IMC no distingue músculo de grasa; la cintura ayuda)"]
guias: ["OMS, obesidad y sobrepeso"]
por_verificar: "El escalamiento 2 para IMC de 40 o más es propuesta de Saludly, no sale de la guía."
frase_permitida: "Con tu peso y tu talla, tu índice de masa corporal es {imc}, que la OMS clasifica como {categoria}. Tu medida de cintura nos ayuda a entender mejor dónde se acumula la grasa."
frases_prohibidas: ["eres obeso", "estás gordo", "tienes que adelgazar"]
recomendaciones_sugeridas: ["alimentación con más vegetales y menos ultraprocesados", "actividad física diaria", "sueño regular", "nutricionista si el paciente quiere"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Obesidad | Peso 92 kg, talla 1,75 m (IMC 30,0), cintura 104 cm, hombre | Activa como obesidad con adiposidad central, escalamiento 1 |
| Sobrepeso | Peso 70 kg, talla 1,62 m (IMC 26,7) | Activa como sobrepeso, escalamiento 1 |
| Clase 3 | Peso 118 kg, talla 1,68 m (IMC 41,8) | Activa, escalamiento 2 |
| Negativo | Peso 63 kg, talla 1,68 m (IMC 22,3) | No activa |
| Sin medida | Peso o talla faltante | No interpretable |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-005 · Glucosa baja en ayunas

**Qué detecta.** Glucosa menor de 70 mg/dL (alerta) o menor de 54 mg/dL (significativa). En toma domiciliaria puede ser un falso bajo si la muestra no fue en tubo con fluoruro o tardó en procesarse; por eso el motor revisa el tubo y el tiempo antes de escalar.

```yaml
id: COND-M1-EM-005
nombre: Glucosa baja en ayunas
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D3
criterios:
  - id: glucosa_baja
    biomarcador: glucose
    condicion: "< 70"
    unidad: mg/dL
  - id: glucosa_muy_baja
    biomarcador: glucose
    condicion: "< 54"
    unidad: mg/dL
  - id: muestra_confiable
    condicion: "tubo con fluoruro AND tiempo de toma a recepción dentro del límite del protocolo"
  - id: medicamento_de_riesgo
    contexto: medicamentos
    condicion: "insulina OR sulfonilurea"
regla_central: "glucosa_baja"
contexto_obligatorio: ["ayuno_horas declarado"]
excluye_si: []
coincidencia:
  alta: "glucosa_baja AND muestra_confiable"
  moderada: "glucosa_baja AND NOT muestra_confiable (posible falso bajo)"
escalamiento:
  base: 1
  si_medicamento_de_riesgo: 2
  si_glucosa_muy_baja_y_muestra_confiable: 3
  si_glucosa_muy_baja_y_muestra_no_confiable: 2
nivel_lenguaje: resultado_observado
confusores: ["demora en el procesamiento", "tubo sin fluoruro", "ayuno muy prolongado"]
guias: ["Clasificación ADA de hipoglucemia (Standards 2024, tabla 6.4)"]
frase_permitida: "Tu glucosa en ayunas salió más baja de lo esperado. Puede deberse a cómo se procesó la muestra, así que conviene repetirla. Si has tenido mareo, sudor frío o temblor en ayunas, coméntalo con tu médico."
frase_permitida_muy_baja: "Tu glucosa salió muy baja. Nuestro equipo médico te va a llamar hoy."
frases_prohibidas: ["tienes hipoglucemia", "tienes un tumor", "tienes diabetes"]
recomendaciones_sugeridas: ["repetir la medición", "no saltarse comidas mientras se aclara"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Alerta | Glucosa 64, tubo con fluoruro, procesada a tiempo | Activa, coincidencia alta, escalamiento 1 |
| Significativa confiable | Glucosa 50, tubo con fluoruro, a tiempo | Activa, escalamiento 3 |
| Significativa dudosa | Glucosa 50, demora de 7 horas sin fluoruro | Activa, coincidencia moderada, escalamiento 2, pide repetir |
| Con medicamento | Glucosa 66, usa glibenclamida | Activa, escalamiento 2 |
| Negativo | Glucosa 86 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-A01 · Riesgo alto de diabetes por FINDRISC (apoyo)

**Qué detecta.** Puntaje FINDRISC de 12 o más en la versión adaptada a Colombia que aplica la enfermera. La GPC colombiana lo usa como tamizaje: con puntaje alto, se mide glucosa (en Saludly ya se mide siempre). Si la glucosa sale normal, el riesgo se mantiene y conviene repetir el tamizaje.

```yaml
id: COND-M1-EM-A01
nombre: Riesgo alto de diabetes por FINDRISC
modulo: M1
especialidad: endocrinologia_metabolica
tipo: apoyo
detectabilidad: D2
criterios:
  - id: findrisc_alto
    contexto: findrisc_puntaje
    condicion: ">= 12"
regla_central: "findrisc_alto"
modifica: ["COND-M1-EM-001"]
efecto: "Si EM-001 está activa, la refuerza en el texto. Si glucosa y HbA1c están en rango, se muestra como 'vigilar' con recomendación de repetir el tamizaje cuando indique el médico."
reglas_especiales: ["cintura con cortes de 94 y 90 cm solo dentro del puntaje FINDRISC"]
guias: ["GPC Colombia DM2 2016"]
frase_permitida: "Tus hábitos y antecedentes suman un riesgo alto de desarrollar diabetes, aunque tu glucosa hoy esté bien. Vale la pena empezar los cambios ahora."
frases_prohibidas: ["vas a tener diabetes"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza | FINDRISC 15, glucosa 108 | Refuerza EM-001 |
| Vigilar | FINDRISC 13, glucosa 88, HbA1c 5,4 | Se muestra como vigilar |
| Negativo | FINDRISC 7 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M1-EM-A02 · Resistencia a la insulina por HOMA-IR (apoyo)

**Qué detecta.** Insulina en ayunas alta o HOMA-IR elevado. Ninguna guía fija un umbral diagnóstico de HOMA-IR y los cortes publicados varían entre 1,6 y 3,0 según la población, así que solo refuerza prediabetes y síndrome metabólico. Al paciente nunca se le muestra un corte como si fuera consenso.

```yaml
id: COND-M1-EM-A02
nombre: Resistencia a la insulina por HOMA-IR
modulo: M1
especialidad: endocrinologia_metabolica
tipo: apoyo
detectabilidad: D1
calculo: "homa_ir = glucosa (mg/dL) x insulina (µUI/mL) / 405"
criterios:
  - id: insulina_alta
    biomarcador: insulin
    condicion: "> límite superior del laboratorio"
  - id: homa_elevado
    biomarcador: homa_ir
    condicion: "> 2.5"
    nota: "corte operativo provisional, a reemplazar por uno validado en población colombiana"
regla_central: "insulina_alta OR homa_elevado"
contexto_obligatorio: ["ayuno_horas >= 8", "no usa insulina"]
modifica: ["COND-M1-EM-001", "COND-M1-EM-003"]
efecto: "Solo refuerza condiciones activas. Sin EM-001 ni EM-003 activas, aparece como vigilar en la vista médica."
guias: ["Sin guía con umbral; ficha homa_ir del Knowledge Base"]
por_verificar: "El corte de 2,5 es una decisión operativa, no de guía. El médico puede cambiarlo o pedir que solo se use la insulina fuera de rango."
frase_permitida_medico: "HOMA-IR {valor}: compatible con resistencia a la insulina; no existe un corte universal validado."
frases_prohibidas: ["tienes resistencia a la insulina", "tu páncreas está fallando"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza · PDF hombre 46 años | Glucosa 112, insulina 19,8 (HOMA-IR 5,5) | Refuerza EM-001 y EM-003 |
| Vigilar | Glucosa 90, insulina 14 (HOMA-IR 3,1), sin condiciones activas | Vigilar en la vista médica |
| Negativo · PDF mujer 34 años | Glucosa 86, insulina 6,1 (HOMA-IR 1,3) | No activa |
| No calculable | Usa insulina | No se calcula |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Resultado esperado del módulo M1 en los PDF de ejemplo

| PDF | Activa | No activa | Incompleto o no calculable |
| --- | --- | --- | --- |
| Hombre 46 años (LCD-2026-100123) | Prediabetes (alta), dislipidemia aterogénica (alta), hipertrigliceridemia (alta), síndrome metabólico (moderada, 3 de 5); apoyos: HOMA-IR 5,5 e hs-CRP 3,4 a confirmar | Hipercolesterolemia severa, Lp(a), diabetes, glucosa baja, discordancia ApoB/LDL | Riesgo global (faltan presión y tabaquismo), hipertensión y obesidad (faltan medidas de la enfermera) |
| Mujer 34 años (LCD-2026-100124) | Lp(a) elevada (alta), dislipidemia aterogénica (moderada) | Prediabetes, diabetes, hipertrigliceridemia, síndrome metabólico, glucosa baja, apoyos | Riesgo global (fuera de 40 a 69 años), hipertensión y obesidad (faltan medidas) |

## Lo que el médico debe mirar con más cuidado

1. Cortes operativos de tamizaje de LDL (130) y no-HDL (160) en CA-001.
2. Categorías de riesgo de SCORE2-PURE en CA-005 (provisionales de la ESC 2021); la calculadora ya está implementada y verificada.
3. Umbral de presión severa (180/120) y su escalamiento 3 en CA-006.
4. Corte provisional de HOMA-IR (2,5) en EM-A02.
5. Escalamiento 2 para IMC de 40 o más en EM-004.
6. Activación de NT-proBNP también en diabetes conocida declarada, en CA-007.