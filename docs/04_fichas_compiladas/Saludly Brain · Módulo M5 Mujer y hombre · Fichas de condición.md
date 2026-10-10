# Módulo M5 · Mujer y hombre — Fichas de condición

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento convierte las condiciones de Salud de la mujer y de Urología y salud del hombre (Lote 5) en reglas que el motor puede ejecutar. Son 8 fichas: 5 condiciones incluidas y 3 de apoyo. Al final están los recordatorios de tamizaje por edad y sexo, que no son pruebas sino texto del informe.

## Cómo leer y cómo firmar

Igual que en los módulos anteriores: `tipo`, `detectabilidad`, `regla_central`, `coincidencia` (alta, moderada, baja = vigilar), `escalamiento` (0 a 3) y `por_verificar`. Para firmar: leer la ficha con sus casos, marcar aprobada, aprobada con cambios o rechazada, escribir los cambios y poner nombre, registro ReTHUS y fecha.

## Reglas comunes del módulo

- **Panel estándar.** Saludly mide a todas las personas del mismo sexo pruebas que varias guías reservan para quien tiene síntomas (prolactina, testosterona, FSH, PSA). Por eso un valor alterado sin síntomas conocidos se reporta como "a confirmar con tu médico", nunca como sospecha de enfermedad.
- **Hormonas del ciclo.** FSH, LH, estradiol y progesterona se leen con el intervalo de la fase, calculada con la fecha de última menstruación que toma la enfermera. Sin esa fecha, con anticonceptivo hormonal, embarazo o menopausia declarada, se muestran como "no interpretables por fase".
- **Testosterona.** Se etiqueta como baja solo si el laboratorio declara un método certificado por el CDC; si no, es resultado observado. Nunca se sugiere reemplazo hormonal, y menos para controlar la glucosa.
- **PSA.** Requiere el consentimiento que recoge la enfermera; sin él, no se mide.
- **Todas las tomas en ayunas y en la mañana.**

## Índice

| ID | Condición | Tipo | Detectabilidad | Datos que usa | Escalamiento |
| --- | --- | --- | --- | --- | --- |
| COND-M5-MU-001 | Andrógenos altos (posible SOP) | Incluida | D3 | Testosterona total, SHBG, TSH, prolactina, ciclo, anticonceptivo | 1 o 2 |
| COND-M5-MU-002 | FSH alta en menores de 40 años | Incluida | D3 | FSH, edad, ciclo, anticonceptivo | 2 |
| COND-M5-MU-003 | Prolactina alta | Incluida | D3 | Prolactina, macroprolactina refleja, TSH, TFG, medicamentos, embarazo | 0, 1 o 2 |
| COND-M5-MU-A01 | Anemia en el embarazo | Apoyo | D2 | HE-001 con embarazo | 2 |
| COND-M5-UR-001 | PSA elevado | Incluida | D3 | PSA total, PSA libre refleja, edad, consentimiento | 1 o 2 |
| COND-M5-UR-002 | Testosterona baja | Incluida | D3 | Testosterona total, SHBG, método, hora de toma | 1 o 2 |
| COND-M5-UR-A01 | Testosterona libre calculada | Apoyo | D1 | Testosterona total, SHBG, albúmina | Modifica UR-002 |
| COND-M5-UR-A02 | Relación PSA libre / total | Apoyo | D1 | PSA libre, PSA total | Modifica UR-001 |

Descartadas en el Lote 5: VPH (exige muestra cervical; queda como recordatorio), bacteriuria en el embarazo (exige urocultivo), menopausia (se diagnostica por síntomas), CA-125 y otros marcadores tumorales, cáncer de mama (exige mamografía; queda como recordatorio), osteoporosis, hiperplasia prostática e infertilidad masculina. Estradiol, progesterona y LH volvieron al catálogo como "solo valor y rango" con la regla de fase del ciclo.

---

## COND-M5-MU-001 · Andrógenos altos (posible SOP)

**Qué detecta.** Testosterona total alta o índice de andrógenos libres alto en una mujer. El síndrome de ovario poliquístico exige además ciclos irregulares u ovarios poliquísticos y descartar otras causas, así que el agente solo señala el hallazgo y remite. Con anticonceptivo hormonal no se interpreta, porque suprime los andrógenos.

```yaml
id: COND-M5-MU-001
nombre: Andrógenos altos (posible SOP)
modulo: M5
especialidad: salud_de_la_mujer
tipo: incluida
detectabilidad: D3
calculo: "indice_androgenos_libres = testosterona total (nmol/L) x 100 / SHBG (nmol/L); testosterona en ng/dL x 0,0347 = nmol/L"
criterios:
  - id: testosterona_alta
    biomarcador: testosterone_total
    condicion: "> límite superior del laboratorio para mujeres"
  - id: fai_alto
    condicion: "indice_androgenos_libres > corte de la guía de SOP 2023 o del laboratorio"
  - id: testosterona_muy_alta
    biomarcador: testosterone_total
    condicion: "> 2 veces el límite superior"
regla_central: "sexo == mujer AND (testosterona_alta OR fai_alto)"
no_interpretable_si: ["anticonceptivo hormonal", "embarazo", "menopausia declarada"]
otras_causas_revisadas: ["TSH alterada (M2)", "prolactina alta (MU-003)"]
coincidencia:
  alta: "testosterona_alta AND fai_alto sin otras causas"
  moderada: "testosterona_alta XOR fai_alto, o con TSH o prolactina alteradas"
escalamiento:
  base: 1
  si_testosterona_muy_alta: 2
nivel_lenguaje: resultado_observado
relacion: "con resistencia a la insulina (M1 EM-A02) y síndrome metabólico (M1 EM-003), la vista médica los cruza"
guias: ["Guía internacional de SOP 2023"]
por_verificar: "Corte del índice de andrógenos libres y el escalamiento 2 con más del doble del límite (propuesta de Saludly) deben confirmarse en la guía completa."
frase_permitida: "Tus hormonas masculinas (andrógenos) están por encima del rango para mujeres. Puede tener varias explicaciones; si además tus ciclos menstruales son irregulares, coméntalo con tu médico."
frases_prohibidas: ["tienes ovario poliquístico", "tienes SOP", "tienes un tumor", "no vas a poder tener hijos"]
recomendaciones_sugeridas: ["consulta con ginecología o medicina general", "actividad física y alimentación si hay resistencia a la insulina"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Mujer 27 años, testosterona 72 ng/dL (hasta 48), SHBG 22, sin anticonceptivo | Activa, coincidencia alta, escalamiento 1 |
| Muy alta | Testosterona 140 ng/dL | Activa, escalamiento 2 |
| Anticonceptivo | Testosterona 60, toma anticonceptivo oral | No interpretable |
| Negativo · PDF mujer 34 años | Testosterona 32, SHBG 62 (índice 1,8), sin anticonceptivo | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-MU-002 · FSH alta en menores de 40 años

**Qué detecta.** FSH alta en una mujer menor de 40 años, posible señal de insuficiencia ovárica prematura. Se repite en 4 a 6 semanas con el médico. Entre 40 y 45 años es solo contexto; desde los 45 la FSH no se usa para diagnosticar menopausia (NICE).

```yaml
id: COND-M5-MU-002
nombre: FSH alta en menores de 40 años
modulo: M5
especialidad: salud_de_la_mujer
tipo: incluida
detectabilidad: D3
criterios:
  - id: fsh_alta
    biomarcador: fsh
    condicion: "> 25"
    unidad: UI/L (mUI/mL)
  - id: edad
    condicion: "< 40"
regla_central: "sexo == mujer AND edad AND fsh_alta"
no_interpretable_si: ["anticonceptivo hormonal", "embarazo", "sin fecha de última menstruación"]
lectura_por_edad:
  "40 a 44": "contexto en la vista médica, sin condición"
  "45 o más": "no se interpreta para menopausia"
coincidencia:
  alta: "regla_central confirmada en una segunda medición a 4-6 semanas"
  moderada: "regla_central en una sola medición"
escalamiento: 2
nivel_lenguaje: patron_compatible
guias: ["NICE NG23, menopausia"]
por_verificar: "El corte de 25 UI/L viene de los criterios de insuficiencia ovárica prematura de ESHRE, no citados en el Lote 5; confirmar fuente antes de la firma."
frase_permitida: "Tu FSH, una hormona que regula los ovarios, salió más alta de lo esperado para tu edad. Hay que repetirla en unas semanas; coméntalo con tu médico, sobre todo si tus ciclos han cambiado o estás pensando en un embarazo."
frases_prohibidas: ["estás entrando en la menopausia", "no vas a poder tener hijos", "tienes falla ovárica"]
recomendaciones_sugeridas: ["consulta médica", "repetir FSH en 4 a 6 semanas"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Mujer 33 años, FSH 38, sin anticonceptivo | Activa, coincidencia moderada, escalamiento 2 |
| Edad 42 | FSH 30 | Sin condición; contexto en la vista médica |
| Edad 50 | FSH 60 | No se interpreta |
| Anticonceptivo | Mujer 30 años, FSH 2, anticonceptivo oral | No interpretable |
| Negativo · PDF mujer 34 años | FSH 6,1 en fase folicular | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-MU-003 · Prolactina alta

**Qué detecta.** Prolactina por encima del intervalo del laboratorio. Como se mide sin síntomas conocidos, el laboratorio corre macroprolactina como refleja y el agente siempre pide repetir. Si predomina la macroprolactina, el hallazgo no suele tener significado clínico. Nunca se habla de tumor. Sin interpretación en embarazo o lactancia.

```yaml
id: COND-M5-MU-003
nombre: Prolactina alta
modulo: M5
especialidad: salud_de_la_mujer
tipo: incluida
detectabilidad: D3
criterios:
  - id: prl_alta
    biomarcador: prolactin
    condicion: "> límite superior del laboratorio"
  - id: macroprolactina_predominante
    biomarcador: macroprolactin
    condicion: "recuperación tras PEG por debajo del corte del laboratorio"
  - id: prl_muy_alta
    biomarcador: prolactin
    condicion: "> 100"
    unidad: ng/mL
regla_central: "prl_alta AND NOT macroprolactina_predominante"
no_interpretable_si: ["embarazo", "lactancia"]
otras_causas_revisadas: ["TSH alta (M2)", "TFG baja (M2)", "medicamentos: antipsicóticos, metoclopramida, algunos antidepresivos", "estrés de la punción"]
coincidencia:
  alta: "regla_central confirmada en una segunda medición"
  moderada: "regla_central en una sola medición"
  baja: "regla_central con medicamento que la sube o TSH alta"
escalamiento:
  macroprolactina_predominante: 0
  base: 1
  si_prl_muy_alta: 2
nivel_lenguaje: resultado_observado
guias: ["Endocrine Society 2011", "Febrasgo y SBEM 2024"]
por_verificar: "Corte de 100 ng/mL para escalamiento 2 es propuesta de Saludly; confirmar con las guías."
frase_permitida: "Tu prolactina salió por encima del rango. Muchas veces se debe al estrés de la toma o a medicamentos, así que hay que repetirla. Si tienes salida de leche por los pezones o cambios en la menstruación, coméntalo con tu médico."
frase_macroprolactina: "Tu prolactina salió alta, pero la mayor parte es una forma que normalmente no tiene efecto en el cuerpo."
frases_prohibidas: ["tienes un tumor en la hipófisis", "tienes prolactinoma"]
recomendaciones_sugeridas: ["repetir la prolactina en la mañana, en reposo", "revisar medicamentos con el médico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Prolactina 41 (hasta 23,3), macroprolactina no predominante | Activa, coincidencia moderada, escalamiento 1 |
| Macroprolactina | Prolactina 38, macroprolactina predominante | Escalamiento 0, frase de macroprolactina |
| Muy alta | Prolactina 160 | Activa, escalamiento 2 |
| Con medicamento | Prolactina 35, toma risperidona | Coincidencia baja |
| Embarazo | Prolactina 120, embarazo de 20 semanas | No interpretable |
| Negativo · PDF mujer 34 años | Prolactina 14,2 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-MU-A01 · Anemia en el embarazo (apoyo)

**Qué detecta.** Cuando el perfil dice embarazo, HE-001 (módulo M3) ya usa los cortes OMS de gestante (11,0 g/dL en primer y tercer trimestre, 10,5 en el segundo) con el ajuste por altitud. Esta ficha agrega la ruta: el hallazgo va al control prenatal con escalamiento 2.

```yaml
id: COND-M5-MU-A01
nombre: Anemia en el embarazo
modulo: M5
especialidad: salud_de_la_mujer
tipo: apoyo
detectabilidad: D2
criterios:
  - id: anemia_gestante
    condicion: "COND-M3-HE-001 activa AND embarazo == true"
regla_central: "anemia_gestante"
modifica: ["COND-M3-HE-001", "COND-M3-HE-002"]
efecto: "Escalamiento mínimo 2; el texto remite al control prenatal; las recomendaciones de hierro son solo alimentarias y el suplemento lo define el control prenatal."
guias: ["OMS 2024, cortes de hemoglobina"]
frase_permitida: "Tu hemoglobina está por debajo de lo recomendado para el embarazo. Es importante comentarlo pronto en tu control prenatal."
frases_prohibidas: ["tu bebé está en riesgo", "toma hierro"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Embarazo de 26 semanas, hemoglobina 12,0 (ajustada 10,2) | Activa, escalamiento 2, ruta prenatal |
| Negativo | Embarazo de 12 semanas, hemoglobina 13,5 (ajustada 11,7) | No activa |
| No aplica · PDF mujer 34 años | No embarazada | No aplica (va por HE-001) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-UR-001 · PSA elevado

**Qué detecta.** PSA total por encima de 4,0 ng/mL o del límite del laboratorio. La edad decide la lectura: de 50 a 75 años es el tamizaje de la Res. 3280 y el informe remite al médico para tacto rectal y evaluación; fuera de ese rango es "valor a revisar con tu médico". Entre 4 y 10 ng/mL el laboratorio corre PSA libre como refleja. Nunca se habla de cáncer.

```yaml
id: COND-M5-UR-001
nombre: PSA elevado
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: incluida
detectabilidad: D3
criterios:
  - id: psa_alto
    biomarcador: psa_total
    condicion: "> 4.0 o > límite superior del laboratorio"
    unidad: ng/mL
  - id: zona_gris
    biomarcador: psa_total
    condicion: "4.0-10.0"
  - id: psa_muy_alto
    biomarcador: psa_total
    condicion: "> 10.0"
  - id: edad_tamizaje
    condicion: "50 a 75 años"
regla_central: "sexo == hombre AND consentimiento_psa AND psa_alto"
no_medido_si: ["sin consentimiento de PSA"]
ajustes: ["finasterida o dutasterida: el PSA medido se multiplica por 2 para interpretarlo"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con eyaculación o ciclismo en 48 horas, infección urinaria o prostatitis reciente"
modificado_por: ["COND-M5-UR-A02"]
escalamiento:
  en_edad_tamizaje: 2
  fuera_de_edad: 1
  si_psa_muy_alto: 2
dispara: ["PSA libre refleja si zona_gris"]
nivel_lenguaje: resultado_observado
contexto_vista_medica: ["antecedente familiar de cáncer de próstata", "ascendencia africana (AUA sugiere PSA basal más temprano)"]
guias: ["Res. 3280 de 2018", "AUA/SUO 2026, detección temprana de cáncer de próstata"]
por_verificar: "Corte de 4,0 ng/mL y regla de duplicar con inhibidores de 5-alfa reductasa: práctica habitual, confirmar en la guía AUA/SUO completa."
frase_permitida_tamizaje: "Tu PSA, una proteína que produce la próstata, salió por encima del valor de referencia. Puede subir por varias causas benignas; conviene una consulta médica en las próximas semanas para evaluarlo."
frase_permitida_fuera_de_edad: "Tu PSA salió por encima del valor de referencia. Es un valor para revisar con tu médico."
frases_prohibidas: ["tienes cáncer de próstata", "tienes un tumor", "necesitas biopsia"]
recomendaciones_sugeridas: ["consulta médica", "evitar eyaculación y bicicleta 48 horas antes de repetirlo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Tamizaje | Hombre 58 años, PSA 5,6, con consentimiento | Activa, escalamiento 2; PSA libre refleja |
| Fuera de edad | Hombre 44 años, PSA 4,8 | Activa, escalamiento 1 |
| Muy alto | Hombre 66 años, PSA 14 | Activa, escalamiento 2 |
| Finasterida | PSA 2,6 con finasterida (equivale a 5,2) | Activa |
| Sin consentimiento | Sin consentimiento de PSA | No medido |
| Negativo · PDF hombre 46 años | PSA 1,10 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-UR-002 · Testosterona baja

**Qué detecta.** Testosterona total matutina por debajo de 264 ng/dL, el percentil 2,5 armonizado por el CDC (Endocrine Society 2018). Solo se etiqueta como baja si el laboratorio declara un método certificado por el CDC; si no, es resultado observado. Sin datos de síntomas nunca se diagnostica hipogonadismo: se pide repetir en la mañana y valorar con el médico.

```yaml
id: COND-M5-UR-002
nombre: Testosterona baja
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: incluida
detectabilidad: D3
criterios:
  - id: testosterona_baja
    biomarcador: testosterone_total
    condicion: "< 264"
    unidad: ng/dL
  - id: metodo_certificado
    condicion: "el laboratorio declara certificación CDC (programa HoST) del método"
  - id: toma_matutina
    condicion: "toma entre las 6:00 y las 10:00, en ayunas"
  - id: testosterona_muy_baja
    biomarcador: testosterone_total
    condicion: "< 150"
regla_central: "sexo == hombre AND testosterona_baja AND metodo_certificado AND toma_matutina"
si_metodo_no_certificado: "resultado observado frente al intervalo del laboratorio, sin etiqueta de baja"
modificado_por: ["COND-M5-UR-A01"]
coincidencia:
  alta: "regla_central AND testosterona libre calculada baja (UR-A01)"
  moderada: "regla_central sin testosterona libre o con confusores"
escalamiento:
  base: 1
  si_testosterona_muy_baja: 2
nivel_lenguaje: resultado_observado
confusores: ["obesidad (baja la SHBG y la testosterona total; usar la libre)", "diabetes", "opioides", "glucocorticoides", "enfermedad aguda reciente", "mal sueño (contexto del Apple Watch)"]
reglas_seguridad: ["nunca sugerir reemplazo hormonal", "nunca proponer testosterona para controlar la glucosa (Endocrine Society)"]
guias: ["Endocrine Society 2018, hipogonadismo masculino"]
por_verificar: "Corte de 150 ng/dL para escalamiento 2 es propuesta de Saludly."
frase_permitida: "Tu testosterona salió baja en esta toma. Varía mucho de un día a otro y con el sueño o el peso, así que hay que repetirla en la mañana. Si tienes cansancio, menos deseo sexual o pérdida de masa muscular, coméntalo con tu médico."
frases_prohibidas: ["tienes hipogonadismo", "tienes andropausia", "necesitas testosterona", "toma testosterona"]
recomendaciones_sugeridas: ["repetir en la mañana", "sueño suficiente", "actividad física y control de peso", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Hombre 52 años, testosterona 228 a las 7:30, método certificado, libre baja | Activa, coincidencia alta, escalamiento 1 |
| No certificado | Testosterona 230, método sin certificación declarada | Resultado observado, sin etiqueta |
| Muy baja | Testosterona 120, certificado | Activa, escalamiento 2 |
| Hora | Testosterona 240 a las 15:00 | No interpretable por hora |
| Negativo · PDF hombre 46 años | Testosterona 412 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-UR-A01 · Testosterona libre calculada (apoyo)

**Qué detecta.** Testosterona libre calculada con la fórmula de Vermeulen (testosterona total, SHBG y albúmina). Se usa sobre todo cuando la total queda cerca del límite o la SHBG está alterada (obesidad, edad, hipotiroidismo). La guía acepta total o libre baja.

```yaml
id: COND-M5-UR-A01
nombre: Testosterona libre calculada
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: apoyo
detectabilidad: D1
calculo: "fórmula de Vermeulen con testosterona total, SHBG y albúmina"
se_calcula_si: ["testosterona total entre 200 y 400 ng/dL", "SHBG fuera de rango", "IMC >= 30"]
criterios:
  - id: libre_baja
    condicion: "< límite inferior del intervalo de testosterona libre calculada del laboratorio o del calculador validado"
regla_central: "sexo == hombre AND libre_baja"
modifica: ["COND-M5-UR-002"]
efecto: "Con total baja, sube la coincidencia a alta. Con total normal y libre baja (por ejemplo, SHBG alta), la vista médica lo muestra como vigilar."
uso_en_mujeres: "en mujeres se usa el índice de andrógenos libres de MU-001"
guias: ["Endocrine Society 2018"]
por_verificar: "Intervalo de referencia de la testosterona libre calculada; depende del calculador y del laboratorio."
frase_permitida_medico: "Testosterona libre calculada {valor}: {apoya | no apoya} testosterona baja."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Apoya | Total 250, SHBG 22, albúmina 4,4; libre baja | UR-002 sube a coincidencia alta |
| SHBG alta | Total 330, SHBG 70; libre baja | Vigilar en la vista médica |
| No se calcula · PDF hombre 46 años | Total 412, SHBG 28, IMC sin dato | No se calcula salvo que el IMC sea 30 o más |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M5-UR-A02 · Relación PSA libre / total (apoyo)

**Qué detecta.** Proporción de PSA libre sobre el total, que el laboratorio mide como refleja cuando el PSA total queda entre 4 y 10 ng/mL. Una proporción baja se asocia a mayor probabilidad de enfermedad; una alta, a menor. El corte está pendiente de fuente en el Lote 5.

```yaml
id: COND-M5-UR-A02
nombre: Relación PSA libre / total
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: apoyo
detectabilidad: D1
calculo: "porcentaje = PSA libre / PSA total x 100"
se_mide_si: "PSA total entre 4,0 y 10,0 ng/mL"
criterios:
  - id: proporcion_baja
    condicion: "< corte pendiente de fuente (valor habitual en la literatura: 10 %)"
  - id: proporcion_alta
    condicion: "> corte pendiente de fuente (valor habitual en la literatura: 25 %)"
modifica: ["COND-M5-UR-001"]
efecto: "Solo vista médica: proporcion_baja refuerza la consulta; proporcion_alta la contextualiza. No cambia el escalamiento ni el texto del paciente."
guias: ["Pendiente de fuente"]
por_verificar: "Los cortes de 10 % y 25 % son valores habituales en la literatura, no verificados en las fuentes de los lotes. Sin firma, la ficha solo muestra el porcentaje."
frase_permitida_medico: "PSA libre {porcentaje} % del total."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Baja | PSA total 6,2, libre 0,5 (8 %) | Refuerza UR-001 en la vista médica |
| Alta | PSA total 5,0, libre 1,5 (30 %) | Contextualiza UR-001 |
| No aplica · PDF hombre 46 años | PSA total 1,10 | No se mide |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Recordatorios de tamizaje por edad y sexo

No son pruebas ni condiciones: son texto que el informe agrega según edad y sexo, para que el chequeo empuje los tamizajes que la Res. 3280 define y que no se hacen con sangre, orina ni heces.

| Recordatorio | A quién | Texto base |
| --- | --- | --- |
| Citología o prueba de VPH | Mujeres de 30 a 65 años | "Recuerda tu tamizaje de cuello uterino; pregunta en tu EPS cuándo te corresponde." |
| Mamografía | Mujeres de 50 a 69 años | "Las guías recomiendan mamografía cada 2 años a tu edad." |
| Tamizaje colorrectal formal | Personas de 50 a 75 años | "Tu prueba de sangre oculta en heces de hoy cuenta para el tamizaje que se repite cada 2 años." |
| Conversación sobre PSA | Hombres de 50 a 75 años | "Tu PSA hace parte del tamizaje de próstata; conviene comentar los resultados con tu médico." |

*Por verificar:* la frecuencia del tamizaje de cuello uterino según la prueba (citología o VPH) debe copiarse de la Res. 3280 antes de dar un intervalo exacto.

## Resultado esperado del módulo M5 en los PDF de ejemplo

| PDF | Activa | No activa | Recordatorios |
| --- | --- | --- | --- |
| Hombre 46 años (LCD-2026-100123) | Ninguna | PSA (1,10), testosterona baja (412) | Ninguno por edad (menor de 50) |
| Mujer 34 años (LCD-2026-100124) | Ninguna | Andrógenos (testosterona 32, índice 1,8), FSH (6,1 en fase folicular, día 9), prolactina (14,2) | Tamizaje de cuello uterino |

## Lo que el médico debe mirar con más cuidado

1. Corte del índice de andrógenos libres en MU-001.
2. Corte de FSH de 25 UI/L en MU-002, que viene de ESHRE y no de las fuentes del lote.
3. Cortes propuestos por Saludly para escalamiento 2: testosterona en mujeres por encima del doble del límite, prolactina por encima de 100 ng/mL y testosterona en hombres por debajo de 150 ng/dL.
4. Corte de PSA de 4,0 ng/mL y la regla de duplicarlo con finasterida o dutasterida.
5. Cortes de la relación PSA libre / total, pendientes de fuente.
6. Intervalo del tamizaje de cuello uterino en los recordatorios.