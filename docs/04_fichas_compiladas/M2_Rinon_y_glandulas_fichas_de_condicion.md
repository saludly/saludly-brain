# Módulo M2 · Riñón y glándulas — Fichas de condición

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento convierte las condiciones de Nefrología y de Tiroides, paratiroides y suprarrenal (Lote 2) en reglas que el motor puede ejecutar. Son 18 fichas: 14 condiciones incluidas y 4 de apoyo. Cada una trae su regla en formato estructurado, el texto que el paciente puede leer, las frases prohibidas, sus casos de prueba y un espacio para la firma del médico.

Ninguna ficha produce un diagnóstico. El Lote 2 es el único con los conflictos entre guías ya resueltos; esas resoluciones están aplicadas aquí.

## Cómo leer una ficha

Igual que en el módulo M1:

| Campo | Qué significa |
| --- | --- |
| `tipo` | **incluida**: aparece en el informe con su nombre. **apoyo**: modifica otra condición y no aparece sola |
| `detectabilidad` | **D1**: el laboratorio basta. **D2**: necesita medidas de la enfermera o cuestionario. **D3**: señal parcial |
| `regla_central` | Qué combinación de criterios activa la condición |
| `coincidencia` | **alta**: criterios centrales con datos completos. **moderada**: datos incompletos o falta confirmar. **baja**: se muestra como "vigilar" |
| `escalamiento` | **0** informativo · **1** próximo control · **2** consulta en las próximas semanas · **3** llamada del equipo médico el mismo día hábil |
| `por_verificar` | Lo que el médico debe mirar con más cuidado |

## Cómo firmar

1. Lee cada ficha, incluidos sus casos de prueba.
2. Marca aprobada, aprobada con cambios o rechazada.
3. Escribe los cambios; el equipo los aplica y vuelve a correr los casos.
4. Nombre, registro ReTHUS y fecha.

## Reglas comunes del módulo

- **Persistencia.** La enfermedad renal y la albuminuria exigen dos mediciones separadas 3 meses o más. Con una sola toma, el hallazgo queda "a confirmar".
- **Potasio.** Nunca se escala con un valor aislado o hemolizado; se repite primero, salvo bandera crítica del laboratorio.
- **TSH.** Fuera del intervalo del laboratorio se marca como alta o baja. Para decidir, se usa el rango del consenso colombiano por edad (0,4 a 5,0 mUI/L de 18 a 60 años; 0,4 a 6,0 después de 60) cuando el laboratorio no ajusta por edad.
- **Biotina.** Biotina alta o suplemento declarado bloquea la interpretación de TSH, T4 libre, T3 libre y anticuerpos tiroideos hasta repetir sin el suplemento. La biotina puede imitar un hipertiroidismo.
- **Microhematuria.** Más de 3 hematíes por campo en microscopía (enmienda AUA 2025); nunca con menstruación declarada.
- **Hiperaldosteronismo.** Aldosterona y renina solo se miden con presión de 130/80 o más.
- **T3.** El panel usa T3 libre como refleja (Consolidado), aunque la ATA prefiere la T3 total; el médico decide si se cambia.

## Índice

| ID | Condición | Tipo | Detectabilidad | Datos que usa | Escalamiento |
| --- | --- | --- | --- | --- | --- |
| COND-M2-NE-001 | Enfermedad renal crónica (sospecha y estadio) | Incluida | D1 | TFG, albúmina/creatinina | 1, 2 o 3 |
| COND-M2-NE-002 | Albuminuria con TFG normal | Incluida | D1 | Albúmina/creatinina, TFG | 1 o 2 |
| COND-M2-NE-003 | Daño renal asociado a diabetes o hipertensión | Incluida | D2 | NE-001 o NE-002, diabetes, hipertensión | 2 |
| COND-M2-NE-004 | Potasio alto | Incluida | D1 | Potasio, hemólisis, tiempo de proceso, medicamentos | 1, 2 o 3 |
| COND-M2-NE-005 | Sodio bajo | Incluida | D1 | Sodio, glucosa, triglicéridos, proteínas | 1, 2 o 3 |
| COND-M2-NE-006 | Hematuria microscópica | Incluida | D1 | Sedimento urinario, menstruación, edad, tabaquismo | 1 o 2 |
| COND-M2-NE-A01 | Potasio bajo | Apoyo | D1 | Potasio, diuréticos | Modifica TI-008 y CA-006 |
| COND-M2-NE-A02 | Confirmación de TFG con cistatina C | Apoyo | D1 | Cistatina C refleja | Modifica NE-001 |
| COND-M2-NE-A03 | Bicarbonato bajo | Apoyo | D1 | Bicarbonato, TFG | Modifica NE-001 |
| COND-M2-TI-001 | Hipotiroidismo subclínico | Incluida | D1 | TSH, T4 libre | 1 o 2 |
| COND-M2-TI-002 | Hipotiroidismo primario | Incluida | D1 | TSH, T4 libre | 2 |
| COND-M2-TI-003 | Sospecha de hipotiroidismo central | Incluida | D1 | TSH, T4 libre | 2 |
| COND-M2-TI-004 | Hipertiroidismo subclínico | Incluida | D1 | TSH, T4 libre, T3 libre | 1 o 2 |
| COND-M2-TI-005 | Hipertiroidismo manifiesto o T3-toxicosis | Incluida | D1 | TSH, T4 libre, T3 libre | 2 |
| COND-M2-TI-006 | Disfunción tiroidea en el embarazo | Incluida | D2 | TSH, T4 libre, embarazo | 2 |
| COND-M2-TI-007 | Hiperparatiroidismo primario | Incluida | D1 | Calcio corregido, PTH refleja | 2 o 3 |
| COND-M2-TI-008 | Hiperaldosteronismo primario (tamizaje en hipertensos) | Incluida | D2 | Aldosterona, renina, potasio, presión, medicamentos | 2 |
| COND-M2-TI-A01 | Autoinmunidad tiroidea | Apoyo | D1 | Anti-TPO, anti-Tg | Modifica TI-001 y TI-002 |

Descartadas en el Lote 2: lesión renal aguda (exige creatinina seriada), litiasis renal (exige imagen), insuficiencia suprarrenal (exige prueba de estimulación), síndrome de Cushing (exige pruebas que no ofrecemos) e hiperparatiroidismo secundario por déficit de vitamina D (pasa a Nutrición). Cortisol y ACTH quedan como "solo valor y rango" con las reglas del documento 03.

---

## COND-M2-NE-001 · Enfermedad renal crónica (sospecha y estadio)

**Qué detecta.** TFG estimada menor de 60 mL/min/1,73 m², o albuminuria de 30 mg/g o más que persiste 3 meses o más. Con una sola toma es sospecha. Se informa el estadio KDIGO (G y A) para el médico.

```yaml
id: COND-M2-NE-001
nombre: Enfermedad renal crónica (sospecha y estadio)
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: tfg_baja
    biomarcador: egfr
    condicion: "< 60"
    unidad: mL/min/1,73 m²
    calculo: "CKD-EPI 2021 con creatinina; si hay cistatina C, CKD-EPI 2021 creatinina-cistatina (NE-A02)"
  - id: albuminuria_persistente
    biomarcador: uacr
    condicion: ">= 30 en dos mediciones separadas 3 meses o más"
    unidad: mg/g
estadios:
  G: {G1: ">= 90", G2: "60-89", G3a: "45-59", G3b: "30-44", G4: "15-29", G5: "< 15"}
  A: {A1: "< 30", A2: "30-300", A3: "> 300"}
regla_central: "tfg_baja OR albuminuria_persistente"
contexto_obligatorio: ["edad", "sexo"]
excluye_si: ["COND-M2-NE-003"]
coincidencia:
  alta: "tfg_baja confirmada a 3 meses OR albuminuria_persistente"
  moderada: "tfg_baja en una sola toma (a confirmar)"
  baja: "tfg_baja en 45-59 sin albuminuria y cistatina C combinada >= 60 (NE-A02 no confirma)"
escalamiento:
  G3a_con_A1: 1
  G3a_con_A2_o_A3: 2
  G3b: 2
  G4_o_G5: 3
  bandera_critica_creatinina: 3
modificado_por: ["COND-M2-NE-A02", "COND-M2-NE-A03"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["masa muscular extrema (NE-A02)", "deshidratación", "ejercicio intenso 48 h", "suplementos de creatina", "dieta muy alta en proteína"]
guias: ["KDIGO 2024", "GPC Colombia HTA 2025"]
por_verificar: "Los niveles de escalamiento por estadio son propuesta de Saludly basada en el mapa de riesgo de KDIGO, no una regla de la guía."
frase_permitida: "Tu filtración renal estimada está por debajo de 60. Un solo resultado no confirma enfermedad renal crónica: hay que repetirlo y revisarlo con tu médico."
frases_prohibidas: ["tienes enfermedad renal", "tus riñones están fallando", "vas a necesitar diálisis"]
recomendaciones_sugeridas: ["repetir creatinina y albúmina/creatinina en 3 meses", "reducir sal", "evitar antiinflamatorios sin indicación médica", "control de presión y glucosa"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Sospecha G3a | TFG 52, albúmina/creatinina 12 | Activa, coincidencia moderada, G3a A1, escalamiento 1; activa cistatina C refleja |
| Sospecha G3b | TFG 38, albúmina/creatinina 80 | Activa, G3b A2, escalamiento 2 |
| Avanzada | TFG 22 | Activa, G4, escalamiento 3 |
| No confirmada | TFG 55 sin albuminuria; TFG combinada con cistatina 68 | Coincidencia baja ("vigilar") |
| Negativo · PDF hombre 46 años | TFG 96, albúmina/creatinina 45 (una toma) | No activa (pasa a NE-002) |
| Negativo · PDF mujer 34 años | TFG 112, albúmina/creatinina 8 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-002 · Albuminuria con TFG normal

**Qué detecta.** Albúmina/creatinina en orina de 30 mg/g o más con TFG de 60 o más: posible daño renal temprano. KDIGO pide confirmar con primera orina de la mañana; un solo valor puede ser transitorio.

```yaml
id: COND-M2-NE-002
nombre: Albuminuria con TFG normal
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: a2
    biomarcador: uacr
    condicion: "30-300"
    unidad: mg/g
  - id: a3
    biomarcador: uacr
    condicion: "> 300"
    unidad: mg/g
  - id: tfg_normal
    biomarcador: egfr
    condicion: ">= 60"
regla_central: "(a2 OR a3) AND tfg_normal"
contexto_obligatorio: ["muestra de primera orina de la mañana"]
excluye_si: ["COND-M2-NE-003", "COND-M2-NE-001 (si la albuminuria ya está confirmada a 3 meses)"]
coincidencia:
  alta: "regla_central confirmada en una segunda muestra"
  moderada: "regla_central en una sola muestra (a confirmar)"
escalamiento:
  a2: 1
  a3: 2
nivel_lenguaje: patron_compatible
confusores: ["ejercicio intenso 48 h", "fiebre o infección reciente", "infección urinaria (nitritos o leucocitos en el uroanálisis)", "menstruación", "glucosa muy alta"]
guias: ["KDIGO 2024"]
frase_permitida: "En tu orina apareció más albúmina de lo esperado. Puede ser transitorio, así que hay que repetirlo; si se confirma, es una señal temprana que conviene cuidar."
frases_prohibidas: ["tienes daño renal", "tus riñones están fallando"]
recomendaciones_sugeridas: ["repetir albúmina/creatinina en primera orina de la mañana", "reducir sal", "control de presión y glucosa"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Albúmina/creatinina 45, TFG 96, una toma | Activa, coincidencia moderada, A2, escalamiento 1 |
| A3 | Albúmina/creatinina 420, TFG 88 | Activa, escalamiento 2 |
| Con confusor | Albúmina/creatinina 60, ejercicio intenso el día anterior | Activa con coincidencia baja; sugiere repetir |
| Negativo · PDF mujer 34 años | Albúmina/creatinina 8 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-003 · Daño renal asociado a diabetes o hipertensión

**Qué detecta.** Albuminuria o TFG baja en una persona con diabetes o hipertensión. Cuando se activa, reemplaza a NE-001 o NE-002 en el informe del paciente y conserva su estadio. Ambas GPC colombianas exigen confirmar persistencia.

```yaml
id: COND-M2-NE-003
nombre: Daño renal asociado a diabetes o hipertensión
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D2
criterios:
  - id: hallazgo_renal
    condicion: "criterios de COND-M2-NE-001 OR COND-M2-NE-002 cumplidos"
  - id: diabetes
    condicion: "diabetes conocida declarada OR COND-M1-EM-002 activa"
  - id: hipertension
    condicion: "hipertensión conocida declarada OR COND-M1-CA-006 con coincidencia alta"
regla_central: "hallazgo_renal AND (diabetes OR hipertension)"
hereda: ["estadio G y A de NE-001 o NE-002"]
coincidencia:
  alta: "regla_central con hallazgo renal confirmado"
  moderada: "regla_central con hallazgo renal en una sola toma"
  baja: "hallazgo_renal con CA-006 de coincidencia moderada (se muestra como vigilar en la vista médica)"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["GPC Colombia DM2 2016", "GPC Colombia HTA 2025", "KDIGO 2024"]
frase_permitida: "Tu orina o tu filtración renal muestran una señal que, en personas con {diabetes o presión alta}, merece atención. Conviene confirmarla y revisarla con tu médico en las próximas semanas."
frases_prohibidas: ["la diabetes te dañó los riñones", "tienes nefropatía diabética"]
recomendaciones_sugeridas: ["consulta médica", "control estricto de presión y glucosa", "reducir sal"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Diabetes conocida, albúmina/creatinina 85, TFG 74 | Activa, coincidencia moderada, A2, escalamiento 2; NE-002 no aparece en el informe del paciente |
| Hipertensión conocida | Toma antihipertensivo, TFG 54, albúmina/creatinina 20 | Activa, G3a, escalamiento 2 |
| Vigilar · PDF hombre 46 años con presión 134/84 sin automonitoreo | Albúmina/creatinina 45, CA-006 moderada | No activa; NE-002 sigue; vista médica marca vigilar |
| Negativo | Sin diabetes ni hipertensión, albúmina/creatinina 45 | No activa (manda NE-002) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-004 · Potasio alto

**Qué detecta.** Potasio por encima del intervalo del laboratorio. Desde 5,5 mmol/L KDIGO plantea acciones. En toma domiciliaria el riesgo de falso alto es grande (hemólisis, puño apretado, demora en separar el plasma), así que nunca se escala con un valor aislado: se repite primero, salvo bandera crítica del laboratorio.

```yaml
id: COND-M2-NE-004
nombre: Potasio alto
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: k_alto
    biomarcador: potassium
    condicion: "> límite superior del laboratorio"
    unidad: mmol/L
  - id: k_accion
    biomarcador: potassium
    condicion: ">= 5.5"
    unidad: mmol/L
  - id: muestra_confiable
    condicion: "sin hemólisis AND plasma separado en menos de 30 minutos (centrífuga en domicilio)"
regla_central: "k_alto AND muestra_confiable"
no_interpretable_si: ["hemólisis reportada", "resultado no procesado", "sin registro de centrifugado a tiempo"]
coincidencia:
  alta: "k_accion AND muestra_confiable AND (TFG < 60 OR medicamento que retiene potasio)"
  moderada: "k_alto AND muestra_confiable"
escalamiento:
  k_alto_menor_5_5: 1
  k_accion: 2
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
confusores: ["hemólisis", "demora en separar el plasma", "puño apretado durante la toma", "leucocitos o plaquetas muy altos", "IECA, ARA II, espironolactona, suplementos de potasio"]
guias: ["KDIGO 2024"]
reglas_especiales: ["nunca pedir suspender medicamentos desde la app"]
frase_permitida: "Tu potasio salió por encima del rango. Muchas veces es un efecto de la toma de la muestra, así que lo vamos a repetir antes de sacar conclusiones."
frases_prohibidas: ["tienes hiperpotasemia", "suspende tu medicamento", "riesgo de arritmia (sin bandera crítica del laboratorio)"]
recomendaciones_sugeridas: ["repetir el potasio", "no tomar suplementos de potasio sin indicación"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| No interpretable · PDF mujer 34 años | Potasio "No procesado", muestra hemolizada | No interpretable; pide nueva muestra; no activa |
| Leve | Potasio 5,3, centrifugado a tiempo | Activa, coincidencia moderada, escalamiento 1; repetir |
| Accionable | Potasio 5,8, sin hemólisis, TFG 48, toma losartán | Activa, coincidencia alta, escalamiento 2 |
| Crítico | Potasio 6,6 con bandera crítica del laboratorio | Escalamiento 3 |
| Negativo · PDF hombre 46 años | Potasio 4,3 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-005 · Sodio bajo

**Qué detecta.** Sodio menor de 135 mmol/L, clasificado como leve (130 a 135), moderado (125 a 129) o profundo (menor de 125). Antes de activarse descarta los falsos bajos: glucosa muy alta (se corrige) y triglicéridos o proteínas muy altos con método de electrodo indirecto (pseudohiponatremia).

```yaml
id: COND-M2-NE-005
nombre: Sodio bajo
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: na_leve
    biomarcador: sodium
    condicion: "130-134.9"
    unidad: mmol/L
  - id: na_moderado
    biomarcador: sodium
    condicion: "125-129.9"
  - id: na_profundo
    biomarcador: sodium
    condicion: "< 125"
correccion: "si glucosa >= 200 mg/dL: sodio corregido = sodio + 1,6 x (glucosa - 100) / 100; se evalúa el sodio corregido"
no_interpretable_si: ["triglycerides >= 1000 con método ISE indirecto", "total_protein > 10 g/dL con método ISE indirecto"]
regla_central: "na_leve OR na_moderado OR na_profundo (sobre el sodio corregido)"
coincidencia:
  alta: "regla_central sin causas de falso bajo"
escalamiento:
  na_leve: 1
  na_moderado: 2
  na_profundo: 3
nivel_lenguaje: resultado_observado
confusores: ["diuréticos tiazídicos", "antidepresivos ISRS", "consumo muy alto de agua (por ejemplo, tras ejercicio prolongado)", "edad mayor de 65"]
guias: ["Guía europea de hiponatremia 2014"]
por_verificar: "Factor de corrección por glucosa de 1,6 (Katz); otros autores usan 2,4. El médico elige."
frase_permitida: "Tu sodio salió un poco bajo. Puede relacionarse con medicamentos o con cuánta agua tomas; conviene repetirlo y comentarlo con tu médico."
frases_prohibidas: ["tienes hiponatremia", "deja de tomar agua"]
recomendaciones_sugeridas: ["repetir el sodio", "revisar medicamentos con el médico", "en deportistas de resistencia: hidratación con sales, no solo agua"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Leve | Sodio 132, glucosa 95 | Activa, escalamiento 1 |
| Moderado con tiazida | Sodio 127, toma hidroclorotiazida | Activa, escalamiento 2 |
| Profundo | Sodio 121 | Activa, escalamiento 3 |
| Corregido | Sodio 131, glucosa 420 (corregido 136,1) | No activa |
| Pseudohiponatremia | Sodio 129, triglicéridos 1.400, ISE indirecto | No interpretable |
| Negativo · PDF ejemplos | Sodio 140 y 138 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-006 · Hematuria microscópica

**Qué detecta.** Más de 3 hematíes por campo en el sedimento urinario. La tira reactiva sola no basta. En bajo riesgo se repite el uroanálisis en 6 meses; con albuminuria, TFG baja o muchos hematíes sube el escalamiento.

```yaml
id: COND-M2-NE-006
nombre: Hematuria microscópica
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: hematies
    biomarcador: urinalysis_rbc_hpf
    condicion: "> 3"
    unidad: hematíes por campo
  - id: hematies_muchos
    biomarcador: urinalysis_rbc_hpf
    condicion: "> 25"
  - id: marcador_glomerular
    condicion: "uacr >= 30 OR egfr < 60"
regla_central: "hematies (por microscopía)"
no_interpretable_si: ["menstruación actual o en los últimos 3 días", "sondaje o procedimiento urológico reciente"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con ejercicio intenso 48 h o infección urinaria"
escalamiento:
  base: 1
  si_marcador_glomerular: 2
  si_hematies_muchos: 2
nivel_lenguaje: resultado_observado
confusores: ["ejercicio intenso 48 h", "infección urinaria (nitritos o esterasa positivos)", "actividad sexual reciente"]
guias: ["AUA/SUFU 2020, enmendada 2025", "KDIGO 2024"]
por_verificar: "La estratificación completa de riesgo de la AUA (edad, sexo, tabaquismo, número de hematíes) debe tomarse de la guía para decidir quién va directo a urología."
frase_permitida: "En tu orina aparecieron más glóbulos rojos de lo esperado, aunque no se ven a simple vista. Hay varias causas posibles y la mayoría no son graves; conviene repetir el examen y comentarlo con tu médico."
frases_prohibidas: ["tienes cáncer", "tienes cálculos", "tienes una enfermedad renal"]
recomendaciones_sugeridas: ["repetir uroanálisis", "consulta si hay albuminuria o TFG baja"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Bajo riesgo | 6 hematíes por campo, sin albuminuria | Activa, escalamiento 1 |
| Glomerular | 10 hematíes por campo, albúmina/creatinina 140 | Activa, escalamiento 2 |
| Menstruación | 15 hematíes por campo, menstruación actual | No interpretable |
| Solo tira | Tira con sangre positiva, sedimento 0 a 2 | No activa |
| Negativo · PDF ejemplos | Sedimento 0 a 2 por campo | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-A01 · Potasio bajo (apoyo)

**Qué detecta.** Potasio por debajo del intervalo del laboratorio. Con hipertensión orienta a hiperaldosteronismo primario o a efecto de diuréticos. Refuerza TI-008 y aparece en la vista médica de CA-006.

```yaml
id: COND-M2-NE-A01
nombre: Potasio bajo
modulo: M2
especialidad: nefrologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: k_bajo
    biomarcador: potassium
    condicion: "< límite inferior del laboratorio"
  - id: k_muy_bajo
    biomarcador: potassium
    condicion: "< 3.0"
    unidad: mmol/L
regla_central: "k_bajo"
modifica: ["COND-M2-TI-008", "COND-M1-CA-006"]
efecto: "Con hipertensión, la vista médica sugiere tamizaje de hiperaldosteronismo si no se hizo. Si k_muy_bajo, aparece como resultado observado con escalamiento 2 aunque sea apoyo."
confusores: ["diuréticos de asa o tiazídicos", "vómito o diarrea recientes", "laxantes"]
guias: ["Endocrine Society 2025, hiperaldosteronismo primario"]
por_verificar: "Mostrar k_muy_bajo con escalamiento 2 es propuesta de Saludly."
frase_permitida_medico: "Potasio bajo con presión elevada: considerar hiperaldosteronismo primario o efecto de diuréticos."
frases_prohibidas: ["tienes hiperaldosteronismo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza | Potasio 3,3, presión 146/92 | Refuerza TI-008 y CA-006 |
| Muy bajo | Potasio 2,8 | Resultado observado, escalamiento 2 |
| Con diurético | Potasio 3,4, toma hidroclorotiazida | Refuerza con nota de diurético |
| Negativo | Potasio 4,3 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-A02 · Confirmación de TFG con cistatina C (apoyo)

**Qué detecta.** Cuando la TFG por creatinina está entre 45 y 59 sin albuminuria, o la creatinina es poco confiable por masa muscular extrema, KDIGO sugiere confirmar con la ecuación combinada creatinina-cistatina C. Si la combinada es de 60 o más, la enfermedad renal no se confirma.

```yaml
id: COND-M2-NE-A02
nombre: Confirmación de TFG con cistatina C
modulo: M2
especialidad: nefrologia
tipo: apoyo
detectabilidad: D1
activa_refleja_si:
  - "egfr 45-59 AND uacr < 30"
  - "obesidad clase 3 (IMC >= 40)"
  - "masa muscular extrema: objetivo de masa muscular o atleta declarado, amputación, desnutrición"
calculo: "CKD-EPI 2021 creatinina-cistatina C, coeficientes de la publicación original"
criterios:
  - id: tfg_combinada_baja
    condicion: "egfr_combinada < 60"
  - id: tfg_combinada_normal
    condicion: "egfr_combinada >= 60"
modifica: ["COND-M2-NE-001"]
efecto: "Si tfg_combinada_baja, NE-001 usa la TFG combinada para el estadio. Si tfg_combinada_normal, NE-001 baja a coincidencia baja."
guias: ["KDIGO 2024"]
frase_permitida_medico: "TFG combinada creatinina-cistatina C {valor}: {confirma | no confirma} enfermedad renal crónica."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| No confirma | TFG creatinina 54, albúmina/creatinina 10, TFG combinada 66 | NE-001 baja a vigilar |
| Confirma | TFG creatinina 52, TFG combinada 49 | NE-001 se mantiene con G3a |
| Masa muscular | Objetivo "aumentar mi masa muscular", creatinina 1,35, TFG 68 | Se pide cistatina C; se usa la combinada |
| No aplica | TFG 96 | No se pide |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-NE-A03 · Bicarbonato bajo (apoyo)

**Qué detecta.** Bicarbonato bajo como complicación de la enfermedad renal crónica. Solo se interpreta si NE-001 o NE-003 están activas; sin ellas, se muestra como valor fuera de rango.

```yaml
id: COND-M2-NE-A03
nombre: Bicarbonato bajo
modulo: M2
especialidad: nefrologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: hco3_bajo
    biomarcador: bicarbonate
    condicion: "< 22"
    unidad: mmol/L
  - id: hco3_muy_bajo
    biomarcador: bicarbonate
    condicion: "< 18"
    unidad: mmol/L
regla_central: "hco3_bajo AND (COND-M2-NE-001 OR COND-M2-NE-003 activa)"
modifica: ["COND-M2-NE-001", "COND-M2-NE-003"]
efecto: "Vista médica: complicación metabólica de la enfermedad renal; si hco3_muy_bajo, se destaca."
confusores: ["demora en procesar la muestra (puede bajar el bicarbonato)", "diarrea reciente"]
guias: ["KDIGO 2024"]
por_verificar: "Corte de 18 mmol/L para destacar; confirmar en KDIGO 2024."
frase_permitida_medico: "Bicarbonato {valor} mmol/L en contexto de TFG baja: posible acidosis metabólica asociada a ERC."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Bicarbonato 19, NE-001 activa (G3b) | Activa como apoyo |
| Sin ERC | Bicarbonato 20, TFG 95 | No activa; valor fuera de rango |
| Negativo · PDF ejemplos | Bicarbonato 25 y 24 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-001 · Hipotiroidismo subclínico

**Qué detecta.** TSH por encima del rango de decisión con T4 libre normal. Se usa el rango del consenso colombiano por edad cuando el laboratorio no ajusta por edad. TSH entre el límite del laboratorio y el corte del consenso queda como "vigilar". Con TSH de 10 o más, o anti-TPO positivo, la guía considera tratamiento.

```yaml
id: COND-M2-TI-001
nombre: Hipotiroidismo subclínico
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_sobre_lab
    biomarcador: tsh
    condicion: "> límite superior del laboratorio"
  - id: tsh_sobre_consenso
    biomarcador: tsh
    condicion: "> 5.0 si edad 18-60; > 6.0 si edad > 60"
    unidad: mUI/L
  - id: tsh_10
    biomarcador: tsh
    condicion: ">= 10"
  - id: t4l_normal
    biomarcador: free_t4
    condicion: "dentro del intervalo del laboratorio"
regla_central: "tsh_sobre_consenso AND t4l_normal"
contexto_obligatorio: ["embarazo == false", "toma en la mañana"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (se lee como control en la vista médica)"]
excluye_si: ["COND-M2-TI-006"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con enfermedad aguda reciente o medicamento que altera la tiroides"
  baja: "tsh_sobre_lab AND NOT tsh_sobre_consenso AND t4l_normal"
modificado_por: ["COND-M2-TI-A01"]
escalamiento:
  base: 1
  si_tsh_10: 2
nivel_lenguaje: patron_compatible
confusores: ["enfermedad aguda reciente", "amiodarona", "litio", "recuperación de una enfermedad grave"]
guias: ["Consenso colombiano de hipotiroidismo 2023", "AACE/ATA (anti-TPO y TSH >= 10 como criterios de tratamiento)"]
por_verificar: "Intervalo para repetir la TSH; la práctica habitual es 2 a 3 meses."
frase_permitida: "Tu TSH, la hormona que regula la tiroides, está un poco alta, mientras que tu hormona tiroidea (T4 libre) está normal. Es un hallazgo frecuente; conviene repetirlo y revisarlo con tu médico."
frase_adicional_mujer_edad_fertil: "Si estás buscando un embarazo, coméntalo pronto con tu médico."
frases_prohibidas: ["tienes hipotiroidismo", "tienes Hashimoto", "necesitas levotiroxina"]
recomendaciones_sugeridas: ["repetir TSH y T4 libre", "consulta médica", "no tomar suplementos de biotina antes de la próxima toma"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | TSH 6,90, T4 libre 1,02 (0,93 a 1,70), anti-TPO 186 | Activa, coincidencia alta, escalamiento 1; refuerzo autoinmune por TI-A01; frase para mujer en edad fértil |
| TSH 10 o más | TSH 11,4, T4 libre normal | Activa, escalamiento 2 |
| Vigilar | TSH 4,6 (laboratorio hasta 4,2), edad 40 | Coincidencia baja (vigilar) |
| Mayor de 60 | TSH 5,6, edad 68 | No activa (corte 6,0) |
| Biotina | TSH 7,2, suplemento de biotina | Bloqueada; pide repetir sin biotina |
| Negativo · PDF hombre 46 años | TSH 2,10 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-002 · Hipotiroidismo primario

**Qué detecta.** TSH alta con T4 libre baja. La tiroides produce poca hormona y la hipófisis lo compensa subiendo la TSH.

```yaml
id: COND-M2-TI-002
nombre: Hipotiroidismo primario
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_alta
    biomarcador: tsh
    condicion: "> límite superior del laboratorio"
  - id: t4l_baja
    biomarcador: free_t4
    condicion: "< límite inferior del laboratorio"
regla_central: "tsh_alta AND t4l_baja"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (control)"]
excluye_si: ["COND-M2-TI-006", "COND-M2-TI-001"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con enfermedad aguda reciente o amiodarona o litio"
modificado_por: ["COND-M2-TI-A01"]
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["enfermedad aguda reciente", "amiodarona", "litio"]
guias: ["Consenso colombiano de hipotiroidismo 2023"]
frase_permitida: "Tu TSH está alta y tu hormona tiroidea está baja. Ese patrón indica que la tiroides podría estar trabajando menos de lo necesario; conviene una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes hipotiroidismo", "necesitas levotiroxina", "toma esta dosis"]
recomendaciones_sugeridas: ["consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | TSH 14,2, T4 libre 0,71 | Activa, coincidencia alta, escalamiento 2; desplaza a TI-001 |
| Con amiodarona | TSH 9,8, T4 libre 0,85, amiodarona | Activa, coincidencia moderada |
| Negativo · PDF mujer 34 años | TSH 6,90, T4 libre 1,02 | No activa (es TI-001) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-003 · Sospecha de hipotiroidismo central

**Qué detecta.** T4 libre baja con TSH baja o inapropiadamente normal. Orienta a un problema en la hipófisis y va siempre a endocrinología. Es poco frecuente; los falsos patrones por interferencias son una causa importante a descartar.

```yaml
id: COND-M2-TI-003
nombre: Sospecha de hipotiroidismo central
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: t4l_baja
    biomarcador: free_t4
    condicion: "< límite inferior del laboratorio"
  - id: tsh_no_alta
    biomarcador: tsh
    condicion: "<= límite superior del laboratorio"
regla_central: "t4l_baja AND tsh_no_alta"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con enfermedad aguda reciente o corticoides"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["enfermedad aguda grave reciente", "corticoides en dosis altas", "interferencia del ensayo"]
guias: ["Consenso colombiano de hipotiroidismo 2023"]
frase_permitida: "Tu hormona tiroidea está baja sin que la TSH haya subido como se esperaría. Ese patrón poco común merece una consulta con endocrinología para revisarlo."
frases_prohibidas: ["tienes un tumor en la hipófisis", "tienes hipotiroidismo central"]
recomendaciones_sugeridas: ["consulta con endocrinología", "repetir TSH y T4 libre"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | T4 libre 0,68, TSH 1,4 | Activa, escalamiento 2 |
| Con corticoides | T4 libre 0,80, TSH 0,9, prednisona | Activa, coincidencia moderada |
| Negativo | T4 libre 1,20, TSH 1,8 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-004 · Hipertiroidismo subclínico

**Qué detecta.** TSH baja con T4 libre y T3 libre normales. El riesgo es mayor con TSH menor de 0,1 que entre 0,1 y el límite inferior. Hay que repetir para confirmar. La biotina puede producir exactamente este patrón, por eso la bloquea.

```yaml
id: COND-M2-TI-004
nombre: Hipertiroidismo subclínico
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_baja
    biomarcador: tsh
    condicion: "< límite inferior del laboratorio"
  - id: tsh_suprimida
    biomarcador: tsh
    condicion: "< 0.1"
    unidad: mUI/L
  - id: t4l_normal
    biomarcador: free_t4
    condicion: "dentro del intervalo"
  - id: t3l_normal
    biomarcador: free_t3
    condicion: "dentro del intervalo"
regla_central: "tsh_baja AND t4l_normal AND t3l_normal"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (posible sobredosificación; se lee como control)"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con corticoides, enfermedad aguda o dopamina"
escalamiento:
  base: 1
  si_tsh_suprimida: 2
contexto_wearable: "frecuencia cardíaca en reposo del Apple Watch como contexto; no cambia la coincidencia"
nivel_lenguaje: patron_compatible
confusores: ["corticoides", "enfermedad aguda reciente", "biotina"]
guias: ["ATA 2016"]
frase_permitida: "Tu TSH está más baja de lo esperado, aunque tus hormonas tiroideas están normales. Conviene repetir el examen y revisarlo con tu médico."
frases_prohibidas: ["tienes hipertiroidismo", "tienes Graves", "tienes bocio"]
recomendaciones_sugeridas: ["repetir TSH, T4 libre y T3", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Leve | TSH 0,18, T4 libre y T3 libre normales | Activa, escalamiento 1 |
| Suprimida | TSH 0,05, T4 libre y T3 libre normales | Activa, escalamiento 2 |
| Biotina | TSH 0,08, biotina en el cuestionario | Bloqueada; pide repetir sin biotina |
| Negativo · PDF ejemplos | TSH 2,10 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-005 · Hipertiroidismo manifiesto o T3-toxicosis

**Qué detecta.** TSH suprimida con T4 libre o T3 elevadas. T3 elevada con T4 libre normal es T3-toxicosis. La ATA prefiere T3 total; el panel usa T3 libre como refleja.

```yaml
id: COND-M2-TI-005
nombre: Hipertiroidismo manifiesto o T3-toxicosis
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_baja
    biomarcador: tsh
    condicion: "< límite inferior del laboratorio"
  - id: t4l_alta
    biomarcador: free_t4
    condicion: "> límite superior"
  - id: t3l_alta
    biomarcador: free_t3
    condicion: "> límite superior"
regla_central: "tsh_baja AND (t4l_alta OR t3l_alta)"
variante: "t3_toxicosis si t3l_alta AND NOT t4l_alta"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (posible sobredosificación)"]
excluye_si: ["COND-M2-TI-004"]
coincidencia:
  alta: "regla_central sin confusores"
escalamiento:
  base: 2
  bandera_critica_laboratorio: 3
contexto_wearable: "frecuencia cardíaca en reposo alta en el Apple Watch refuerza la recomendación de consulta"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["ATA 2016"]
por_verificar: "Uso de T3 libre en vez de T3 total como refleja."
frase_permitida: "Tu TSH está baja y tus hormonas tiroideas están altas. Ese patrón indica que la tiroides podría estar trabajando de más; necesitas una consulta médica en las próximas semanas. Si tienes palpitaciones fuertes, falta de aire o temblor intenso, consulta antes."
frases_prohibidas: ["tienes hipertiroidismo", "tienes Graves", "tienes una tormenta tiroidea"]
recomendaciones_sugeridas: ["consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Manifiesto | TSH \< 0,01, T4 libre 2,9 | Activa, escalamiento 2 |
| T3-toxicosis | TSH 0,02, T4 libre 1,5 (normal), T3 libre 6,1 (alta) | Activa, variante T3-toxicosis |
| Con levotiroxina | TSH 0,03, T4 libre 2,1, toma levotiroxina | Bloqueada; vista médica: posible sobredosificación |
| Negativo | TSH 1,8 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-006 · Disfunción tiroidea en el embarazo

**Qué detecta.** En una gestante, TSH mayor de 4,0 mUI/L indica hipotiroidismo según el consenso colombiano, que pide TSH a toda gestante. Reemplaza a TI-001 y TI-002 cuando hay embarazo. Una TSH baja en el primer trimestre puede ser fisiológica: se muestra al médico como resultado observado.

```yaml
id: COND-M2-TI-006
nombre: Disfunción tiroidea en el embarazo
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D2
criterios:
  - id: embarazo
    contexto: embarazo
    condicion: "true, con semana de gestación"
  - id: tsh_alta_embarazo
    biomarcador: tsh
    condicion: "> 4.0"
    unidad: mUI/L
  - id: t4l_baja
    biomarcador: free_t4
    condicion: "< límite inferior"
regla_central: "embarazo AND tsh_alta_embarazo"
bloqueado_si: ["biotina alta o suplemento declarado"]
coincidencia:
  alta: "regla_central con semana de gestación conocida"
  moderada: "regla_central sin semana de gestación"
modificado_por: ["COND-M2-TI-A01"]
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
reglas_especiales: ["TSH baja en primer trimestre: resultado observado para el médico, sin condición"]
guias: ["Consenso colombiano de hipotiroidismo 2023"]
frase_permitida: "En el embarazo, tu TSH está por encima del valor recomendado. Es importante comentarlo pronto con tu médico o con quien lleva tu control prenatal."
frases_prohibidas: ["tu bebé está en riesgo", "tienes hipotiroidismo"]
recomendaciones_sugeridas: ["consulta con el control prenatal"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Embarazo de 10 semanas, TSH 4,8 | Activa, coincidencia alta, escalamiento 2 |
| Con T4 libre baja | Embarazo de 22 semanas, TSH 6,5, T4 libre baja | Activa; vista médica destaca la T4 libre baja |
| TSH baja | Embarazo de 9 semanas, TSH 0,2 | No activa; resultado observado para el médico |
| No embarazada | TSH 4,8 | No aplica (va por TI-001) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-007 · Hiperparatiroidismo primario

**Qué detecta.** Calcio corregido por albúmina alto con PTH alta o inapropiadamente normal (no suprimida). La guía pide confirmarlo en dos ocasiones separadas por 2 semanas o más; con una toma queda "a confirmar". La PTH es refleja: el laboratorio la corre si el calcio corregido sale alto.

```yaml
id: COND-M2-TI-007
nombre: Hiperparatiroidismo primario
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
calculo: "calcio corregido = calcio total + 0,8 x (4,0 - albúmina en g/dL)"
criterios:
  - id: calcio_alto
    condicion: "calcio corregido > límite superior del laboratorio"
  - id: pth_no_suprimida
    biomarcador: pth
    condicion: "> mitad del intervalo del laboratorio, o alta"
  - id: calcio_muy_alto
    condicion: "calcio corregido >= 12"
    unidad: mg/dL
regla_central: "calcio_alto AND pth_no_suprimida"
coincidencia:
  alta: "regla_central confirmada en dos ocasiones separadas 2 semanas o más"
  moderada: "regla_central en una sola toma"
escalamiento:
  base: 2
  si_calcio_muy_alto: 3
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["tiazidas", "litio", "suplementos de calcio o vitamina D en dosis altas", "deshidratación", "TFG < 60 (orienta a causa renal secundaria)"]
guias: ["Quinto Taller Internacional de hiperparatiroidismo primario 2022"]
por_verificar: "Definición operativa de PTH 'inapropiadamente normal' (mitad superior del intervalo) y el corte de 12 mg/dL para escalamiento 3."
frase_permitida: "Tu calcio está alto y la hormona que lo regula (PTH) no bajó como se esperaría. Ese patrón merece confirmarse y revisarse con tu médico en las próximas semanas."
frases_prohibidas: ["tienes un tumor en la paratiroides", "necesitas cirugía"]
recomendaciones_sugeridas: ["repetir calcio y PTH", "hidratación adecuada", "no tomar suplementos de calcio o vitamina D sin indicación mientras se aclara"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Calcio 10,9, albúmina 4,2 (corregido 10,7), PTH 78 (15 a 65) | Activa, coincidencia moderada, escalamiento 2 |
| Muy alto | Calcio corregido 12,4, PTH 140 | Activa, escalamiento 3 |
| Corregido normal | Calcio 10,4, albúmina 4,9 (corregido 9,7) | No activa; no se pide PTH |
| PTH suprimida | Calcio corregido 11,0, PTH 8 | No activa; vista médica: buscar otra causa de calcio alto |
| Negativo · PDF ejemplos | Calcio 9,5 y 9,2 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-008 · Hiperaldosteronismo primario (tamizaje en hipertensos)

**Qué detecta.** Renina suprimida con aldosterona alta y relación aldosterona/renina elevada, en personas con presión de 130/80 o más. La Endocrine Society 2025 sugiere tamizarlo en toda persona hipertensa y la GPC colombiana 2025 lo incluye en el estudio inicial. La muestra es en la mañana, sentado, y no exige suspender antihipertensivos, pero algunos cambian el resultado.

```yaml
id: COND-M2-TI-008
nombre: Hiperaldosteronismo primario (tamizaje en hipertensos)
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D2
activa_refleja_si: ["COND-M1-CA-006 activa (presión >= 130/80)", "hipertensión conocida declarada"]
criterios:
  - id: renina_suprimida
    biomarcador: renin
    condicion: "actividad (ARP) <= 1 ng/mL/h, o concentración directa (DRC) <= 8,2 mU/L"
  - id: aldosterona_alta
    biomarcador: aldosterone
    condicion: ">= 10 ng/dL (277 pmol/L) por inmunoensayo, o >= 7,5 ng/dL (208 pmol/L) por LC-MS/MS"
  - id: arr_alta
    calculo: "aldosterona / renina"
    condicion: "con aldosterona por inmunoensayo: > 20 (ng/dL sobre ng/mL/h) o > 70 (pmol/L sobre mU/L); con LC-MS/MS, cerca de 25 % más bajo"
  - id: zona_repetir
    condicion: "renina suprimida con aldosterona de 5 a 10 ng/dL por inmunoensayo"
regla_central: "renina_suprimida AND aldosterona_alta AND arr_alta"
cortes_locales: "la guía pide preferir los cortes del laboratorio local cuando existan"
repetir_si: ["zona_repetir", "tamizaje negativo con potasio bajo (corregir el potasio y repetir)", "tamizaje positivo con betabloqueador, clonidina o metildopa y aldosterona de 10 a 15 ng/dL por inmunoensayo"]
contexto_obligatorio: ["toma en la mañana, sentado", "lista de antihipertensivos"]
coincidencia:
  alta: "regla_central sin medicamentos que confundan"
  moderada: "regla_central con betabloqueador, IECA, ARA II, diurético o espironolactona, o con TFG < 60 (más falsos positivos)"
modificado_por: ["COND-M2-NE-A01"]
escalamiento: 2
nivel_lenguaje: patron_compatible
confusores: ["betabloqueadores (bajan la renina: falso positivo)", "IECA, ARA II y diuréticos (suben la renina: falso negativo)", "espironolactona o eplerenona", "potasio bajo (baja la aldosterona)"]
guias: ["Endocrine Society 2025, hiperaldosteronismo primario", "GPC Colombia HTA 2025"]
por_verificar: "Cortes tomados del resumen oficial de recomendaciones de la Endocrine Society 2025 en endocrine.org (6 de octubre de 2026); falta leer el texto completo y su tabla de cortes por método. Preferir los cortes del laboratorio aliado si los tiene."
frase_permitida: "En el estudio de tu presión, las hormonas que regulan la sal y el agua (aldosterona y renina) muestran un patrón que vale la pena revisar con tu médico. Es una causa tratable de presión alta."
frases_prohibidas: ["tienes hiperaldosteronismo", "tienes un tumor suprarrenal", "suspende tu medicamento"]
recomendaciones_sugeridas: ["consulta médica", "no suspender medicamentos por cuenta propia"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Presión 148/94; aldosterona 18 ng/dL (inmunoensayo); ARP 0,4 ng/mL/h (relación 45); potasio 3,3 | Activa, coincidencia alta, escalamiento 2; refuerzo por NE-A01 |
| Con betabloqueador | Aldosterona 12 ng/dL; ARP 0,5 (relación 24); toma metoprolol | Activa, coincidencia moderada; repetir tras retirar el betabloqueador si el médico lo considera seguro |
| Zona para repetir | Aldosterona 7 ng/dL; ARP 0,3 | No activa; repetir otro día |
| Negativo | Presión 136/86; aldosterona 9 ng/dL; ARP 2,1 (relación 4,3) | No activa |
| Unidades de concentración | Aldosterona 450 pmol/L; DRC 4 mU/L (relación 112) | Activa |
| Sin presión elevada · PDF ejemplos sin datos de la enfermera | Aldosterona y renina no se pidieron | No aplica |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M2-TI-A01 · Autoinmunidad tiroidea (apoyo)

**Qué detecta.** Anti-TPO positivo, o anti-Tg positivo si anti-TPO sale negativo. Clasifica la causa de una TSH alta como autoinmune (tiroiditis de Hashimoto) y aumenta la probabilidad de progresar a hipotiroidismo. Las dos son reflejas: el laboratorio las corre si la TSH sale alta.

```yaml
id: COND-M2-TI-A01
nombre: Autoinmunidad tiroidea
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: apoyo
detectabilidad: D1
criterios:
  - id: anti_tpo_positivo
    biomarcador: anti_tpo
    condicion: "> límite superior del laboratorio"
  - id: anti_tg_positivo
    biomarcador: anti_tg
    condicion: "> límite superior del laboratorio (solo si anti-TPO negativo)"
regla_central: "anti_tpo_positivo OR anti_tg_positivo"
bloqueado_si: ["biotina alta o suplemento declarado"]
modifica: ["COND-M2-TI-001", "COND-M2-TI-002", "COND-M2-TI-006"]
efecto: "Agrega al texto que la causa probable es autoinmune; en TI-001 la vista médica recuerda que la guía AACE/ATA considera tratamiento con anti-TPO positivo."
relacion_vigilar: "hierro bajo + anticuerpos positivos: vigilar (documento 03, 03.7)"
guias: ["Consenso colombiano de hipotiroidismo 2023", "AACE/ATA"]
frase_permitida: "Tus anticuerpos tiroideos están positivos, lo que sugiere que la causa es autoinmune, es decir, que el propio sistema de defensa afecta a la tiroides. Es la causa más común y se maneja bien con seguimiento."
frases_prohibidas: ["tienes Hashimoto", "tienes una enfermedad autoinmune grave"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | Anti-TPO 186 (menor de 34), con TSH 6,90 | Refuerza TI-001; se marca relación vigilar con ferritina baja |
| Anti-Tg | Anti-TPO negativo, anti-Tg 210 (menor de 115), TSH 7,0 | Refuerza TI-001 |
| Negativo | Anti-TPO 12 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Resultado esperado del módulo M2 en los PDF de ejemplo

| PDF | Activa | No activa | No interpretable o no aplica |
| --- | --- | --- | --- |
| Hombre 46 años (LCD-2026-100123) | Albuminuria con TFG normal (A2, coincidencia moderada, a confirmar, escalamiento 1) | Enfermedad renal, potasio, sodio, hematuria, todas las tiroideas, hiperparatiroidismo | Daño renal por hipertensión e hiperaldosteronismo dependen de la presión que tome la enfermera |
| Mujer 34 años (LCD-2026-100124) | Hipotiroidismo subclínico (coincidencia alta, escalamiento 1) con autoinmunidad tiroidea como apoyo | Riñón, sodio, hematuria, hipertiroidismo, hiperparatiroidismo | Potasio no interpretable (hemolizado; pide nueva muestra); hiperaldosteronismo no aplica |

## Lo que el médico debe mirar con más cuidado

1. Escalamiento por estadio de enfermedad renal en NE-001, basado en el mapa de riesgo de KDIGO pero propuesto por Saludly.
2. Factor de corrección de sodio por glucosa (1,6 o 2,4) en NE-005.
3. Estratificación de riesgo de la AUA para hematuria en NE-006.
4. Uso de T3 libre en vez de T3 total en TI-004 y TI-005.
5. Definición de PTH "inapropiadamente normal" y el corte de calcio de 12 mg/dL en TI-007.
6. Cortes de aldosterona, renina y relación aldosterona/renina en TI-008, tomados del resumen oficial de la Endocrine Society 2025; confirmar con el texto completo y con los cortes del laboratorio aliado.
7. Mostrar potasio menor de 3,0 con escalamiento 2 en NE-A01.