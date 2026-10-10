# Módulo M4 · Digestivo e infecciones — Fichas de condición

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento convierte las condiciones de Gastroenterología y hepatología y de Infectología (Lote 4) en reglas que el motor puede ejecutar. Son 13 fichas: 9 condiciones incluidas y 4 de apoyo. VIH, sífilis, clamidia y gonorrea salieron del producto el 6 de octubre de 2026.

**Advertencia de fuentes.** El Lote 4 es el que tiene menos fuentes leídas completas: 1 de 14. Por eso este módulo trae más campos `por_verificar` que los anteriores. Antes de la firma conviene leer completas al menos la guía colombiana de *H. pylori* de 2025, el lineamiento de hepatitis C del Ministerio y el lineamiento del INS para Chagas en adultos.

## Cómo leer y cómo firmar

Igual que en los módulos anteriores: `tipo`, `detectabilidad`, `regla_central`, `coincidencia` (alta, moderada, baja = vigilar), `escalamiento` (0 a 3) y `por_verificar`. Para firmar: leer la ficha con sus casos, marcar aprobada, aprobada con cambios o rechazada, escribir los cambios y poner nombre, registro ReTHUS y fecha.

## Reglas comunes del módulo

- **Transaminasas.** Por encima del valor sano de la ACG (33 UI/L en hombres, 25 en mujeres) pero dentro del rango del laboratorio: limítrofe. Por encima del laboratorio: alto. Una sola medición se repite antes de evaluar.
- **Alcohol, suplementos y productos herbales.** La enfermera los pregunta siempre; ante cualquier alteración hepática, la vista médica los muestra como posibles causas, incluidos los productos que Saludly llegue a vender.
- **Serologías reactivas.** Hepatitis B, hepatitis C y Chagas reactivos tienen escalamiento 2 y los comunica el médico por llamada. Nunca llegan primero por WhatsApp.
- **Heces.** Una sola muestra sirve para sangre oculta, antígeno de *H. pylori* y coprológico.
- **Bacteria en orina sin síntomas.** No se reporta como infección fuera del embarazo (IDSA 2019).

## Índice

| ID | Condición | Tipo | Detectabilidad | Datos que usa | Escalamiento |
| --- | --- | --- | --- | --- | --- |
| COND-M4-GA-001 | Riesgo de fibrosis por hígado graso metabólico (FIB-4) | Incluida | D2 | Edad, AST, ALT, plaquetas, diabetes, cintura | 1 o 2 |
| COND-M4-GA-002 | Alteración hepatocelular | Incluida | D1 | ALT, AST, alcohol, suplementos | 1 o 2 |
| COND-M4-GA-003 | Alteración colestásica | Incluida | D1 | Fosfatasa alcalina, GGT, bilirrubina, ALT | 1 o 2 |
| COND-M4-GA-004 | Sangre oculta en heces positiva | Incluida | D3 | FIT, edad, colonoscopia previa | 2 |
| COND-M4-GA-005 | Infección por *H. pylori* | Incluida | D1 | Antígeno en heces, inhibidores de bomba, antibióticos | 2 |
| COND-M4-GA-006 | Enfermedad celíaca (prueba dirigida) | Incluida | D3 | Anti-tTG IgA, IgA total, dieta con gluten | 2 |
| COND-M4-GA-A01 | Bilirrubina indirecta elevada aislada | Apoyo | D1 | Bilirrubina total y directa | 0 o modifica hemólisis |
| COND-M4-GA-A02 | Alteración hepática con consumo de alcohol | Apoyo | D2 | AST, ALT, GGT, alcohol | Modifica GA-001 y GA-002 |
| COND-M4-IN-001 | Hepatitis C | Incluida | D3 | Anti-VHC, ARN VHC refleja | 2 |
| COND-M4-IN-002 | Hepatitis B y estado frente a la vacuna | Incluida | D3 | HBsAg, anti-HBs, anti-HBc total | 0, 1 o 2 |
| COND-M4-IN-003 | Enfermedad de Chagas crónica | Incluida | D2 | Dos ELISA, procedencia | 2 |
| COND-M4-IN-A01 | Infección urinaria con síntomas | Apoyo | D2 | Uroanálisis, síntomas, embarazo | 1 |
| COND-M4-IN-A02 | Parasitosis intestinal | Apoyo | D1 | Coprológico, eosinofilia | 0 o 1 |

Descartadas: enfermedad inflamatoria intestinal, pancreatitis, diagnóstico de hígado graso (exige imagen), bacteriuria sin síntomas en no gestantes, tuberculosis latente, virus del papiloma humano (pasa al M5), VIH, sífilis, clamidia y gonorrea.

---

## COND-M4-GA-001 · Riesgo de fibrosis por hígado graso metabólico (FIB-4)

**Qué detecta.** El índice FIB-4 estima el riesgo de fibrosis hepática avanzada en personas con factores metabólicos o enzimas hepáticas alteradas. Menor de 1,3 la descarta; mayor de 2,67 la sugiere; entre ambos es indeterminado y se discute elastografía. No diagnostica hígado graso: eso exige imagen.

```yaml
id: COND-M4-GA-001
nombre: Riesgo de fibrosis por hígado graso metabólico (FIB-4)
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D2
calculo: "fib4 = (edad x AST) / (plaquetas en 10^9/L x raíz cuadrada de ALT)"
aplica_si: ["diabetes tipo 2 (conocida o COND-M1-EM-002)", "cintura alta (>= 90 H, >= 80 M) con otro factor metabólico", "ALT, AST o GGT por encima del valor sano o del laboratorio"]
criterios:
  - id: fib4_bajo
    condicion: "< 1,3"
  - id: fib4_indeterminado
    condicion: "1,3-2,67"
  - id: fib4_alto
    condicion: "> 2,67"
regla_central: "aplica AND (fib4_indeterminado OR fib4_alto)"
reglas_especiales:
  - "edad < 35: FIB-4 menos confiable; se muestra con advertencia"
  - "edad > 65 o diabetes: un FIB-4 bajo no descarta fibrosis; se marca como no concluyente en la vista médica"
coincidencia:
  alta: "fib4_alto sin confusores"
  moderada: "fib4_indeterminado, o fib4_alto con ejercicio intenso reciente (AST muscular)"
escalamiento:
  fib4_indeterminado: 1
  fib4_alto: 2
modificado_por: ["COND-M4-GA-A02", "relación patrón muscular (documento 03)"]
nivel_lenguaje: riesgo_potencial
confusores: ["patrón muscular (CK alta): la AST puede ser de músculo", "plaquetas bajas por otra causa", "hepatitis viral activa"]
guias: ["EASL-EASD-EASO 2024, hígado graso metabólico"]
por_verificar: "Fuente leída solo por resultado de búsqueda. Confirmar los cortes 1,3 y 2,67 y la regla para mayores de 65 en la guía completa."
frase_permitida_indeterminado: "Con tus resultados, el índice que estima la salud del hígado (FIB-4) quedó en una zona intermedia. No dice que haya daño, pero conviene revisarlo con tu médico, que puede pedir una prueba de elasticidad del hígado."
frase_permitida_alto: "El índice que estima la salud del hígado (FIB-4) salió alto. Conviene una consulta médica en las próximas semanas para estudiarlo mejor."
frases_prohibidas: ["tienes hígado graso", "tienes cirrosis", "tienes fibrosis"]
recomendaciones_sugeridas: ["reducir alcohol, azúcar y ultraprocesados", "actividad física regular", "control de peso"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Bajo · PDF hombre 46 años | Edad 46, AST 39, ALT 58, plaquetas 265 (FIB-4 0,89) | No activa; la vista médica muestra FIB-4 bajo |
| Indeterminado | Edad 58, AST 48, ALT 52, plaquetas 190, diabetes (FIB-4 2,03) | Activa, coincidencia moderada, escalamiento 1 |
| Alto | Edad 62, AST 70, ALT 45, plaquetas 140 (FIB-4 4,62) | Activa, escalamiento 2 |
| Mayor de 65 | Edad 70, FIB-4 1,1, diabetes | No activa; vista médica: no concluyente |
| No aplica · PDF mujer 34 años | Sin factores metabólicos, enzimas normales | No se calcula |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-002 · Alteración hepatocelular

**Qué detecta.** ALT por encima del valor sano de la ACG (33 UI/L en hombres, 25 en mujeres), aunque esté dentro del rango del laboratorio. Entre ambos valores es limítrofe; por encima del laboratorio es alto. La causa más común es metabólica, pero también alcohol, hepatitis virales, medicamentos y suplementos. Siempre se repite antes de evaluar.

```yaml
id: COND-M4-GA-002
nombre: Alteración hepatocelular
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: alt_limitrofe
    biomarcador: alt
    condicion: "> 33 si hombre; > 25 si mujer; y <= límite superior del laboratorio"
    unidad: UI/L
  - id: alt_alta
    biomarcador: alt
    condicion: "> límite superior del laboratorio"
  - id: alt_muy_alta
    biomarcador: alt
    condicion: "> 3 veces el límite superior del laboratorio"
  - id: ast_alta
    biomarcador: ast
    condicion: "> límite superior del laboratorio"
regla_central: "alt_alta OR (ast_alta AND NOT patrón muscular)"
coincidencia:
  alta: "regla_central confirmada en una segunda medición"
  moderada: "regla_central en una sola medición"
  baja: "alt_limitrofe (vigilar)"
escalamiento:
  base: 1
  si_alt_muy_alta: 2
  bandera_critica_laboratorio: 3
dispara: ["IgA total y anti-tTG IgA reflejas (GA-006)", "lectura conjunta con hepatitis B y C (IN-001, IN-002)", "FIB-4 (GA-001)"]
modificado_por: ["COND-M4-GA-A02", "relación hepática metabólica (documento 03)"]
nivel_lenguaje: patron_compatible
confusores: ["ejercicio intenso 48 h (AST y ALT de músculo)", "patrón muscular CK alta", "hemólisis de la muestra", "medicamentos, suplementos y productos herbales", "alcohol"]
guias: ["ACG 2017, evaluación de pruebas hepáticas alteradas"]
regla_seguridad: "nunca recomendar 'desintoxicación hepática' ni atribuir el hallazgo a hígado graso o alcohol de forma automática"
frase_permitida: "Una de tus enzimas del hígado (ALT) está por encima de lo esperado. Hay varias causas posibles, la mayoría relacionadas con hábitos; conviene repetirla y revisarla con tu médico."
frase_vigilar: "Tu ALT está dentro del rango del laboratorio, pero por encima del valor que las guías consideran plenamente sano. Lo vigilamos."
frases_prohibidas: ["tienes hígado graso", "tienes hepatitis", "tu hígado está dañado", "haz un detox"]
recomendaciones_sugeridas: ["reducir alcohol", "revisar suplementos y productos herbales con el médico", "repetir en unas semanas", "actividad física y menos azúcar"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | ALT 58 (laboratorio hasta 50), AST 39, CK normal | Activa, coincidencia moderada, escalamiento 1; ligada a la relación hepática metabólica |
| Limítrofe | Mujer, ALT 31 (laboratorio hasta 35) | Vigilar |
| Muy alta | ALT 190 (laboratorio hasta 50) | Activa, escalamiento 2 |
| Muscular | ALT 48, AST 85, CK 2.400, ejercicio el día anterior | No activa; patrón muscular |
| Negativo · PDF mujer 34 años | ALT 18 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-003 · Alteración colestásica

**Qué detecta.** Fosfatasa alcalina alta de forma desproporcionada frente a las transaminasas, con GGT alta que confirma el origen hepático. Si la fosfatasa alcalina sube sola con GGT normal, el origen probable es óseo y no se activa.

```yaml
id: COND-M4-GA-003
nombre: Alteración colestásica
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D1
calculo: "R = (ALT / límite superior de ALT) / (ALP / límite superior de ALP)"
criterios:
  - id: alp_alta
    biomarcador: alp
    condicion: "> límite superior del laboratorio"
  - id: ggt_alta
    biomarcador: ggt
    condicion: "> límite superior del laboratorio"
  - id: patron_colestasico
    condicion: "R < 2"
  - id: bilirrubina_directa_alta
    biomarcador: bilirubin_direct
    condicion: "> límite superior"
  - id: alp_doble
    biomarcador: alp
    condicion: "> 2 veces el límite superior"
regla_central: "alp_alta AND ggt_alta AND patron_colestasico"
coincidencia:
  alta: "regla_central"
  baja: "alp_alta con GGT normal (origen óseo probable; vigilar)"
escalamiento:
  base: 1
  si_alp_doble_o_bilirrubina_directa_alta: 2
nivel_lenguaje: patron_compatible
confusores: ["embarazo (la fosfatasa alcalina sube por la placenta)", "crecimiento óseo en menores de 25", "medicamentos"]
guias: ["ACG 2017"]
por_verificar: "Uso del factor R y de 2 veces el límite para escalar; confirmar en la guía completa."
frase_permitida: "Algunas pruebas del hígado relacionadas con la bilis (fosfatasa alcalina y GGT) están altas. Conviene revisarlas con tu médico."
frases_prohibidas: ["tienes cálculos en la vesícula", "tienes un tumor", "tienes cirrosis biliar"]
recomendaciones_sugeridas: ["consulta médica", "revisar medicamentos y suplementos"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | ALP 260 (hasta 129), GGT 180, ALT 40 (R 0,4) | Activa, escalamiento 2 (más del doble) |
| Leve | ALP 160, GGT 95, ALT 35 | Activa, escalamiento 1 |
| Óseo | ALP 170, GGT 30 | Vigilar; origen óseo probable |
| Negativo · PDF hombre 46 años | ALP 88, GGT 72 (hasta 71) | No activa (falta ALP alta) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-004 · Sangre oculta en heces positiva

**Qué detecta.** Prueba inmunoquímica (FIT) positiva. Exige colonoscopia; no es un diagnóstico de cáncer. Por decisión del equipo, un FIT positivo se remite a cualquier edad. El informe menciona que el tamizaje formal en Colombia es de 50 a 75 años cada 2 años (Res. 3280).

```yaml
id: COND-M4-GA-004
nombre: Sangre oculta en heces positiva
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: fit_positivo
    biomarcador: fit_stool
    condicion: "positivo"
regla_central: "fit_positivo"
coincidencia:
  alta: "fit_positivo"
escalamiento: 2
contexto_vista_medica: ["edad y si está en la franja de tamizaje 50-75", "colonoscopia previa", "antecedente familiar de cáncer colorrectal", "anemia o déficit de hierro (M3)"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["sangrado por hemorroides o menstruación (no anulan el resultado; se informan al médico)"]
guias: ["Res. 3280 de 2018", "USPSTF 2021"]
regla_seguridad: "no repetir el FIT para 'confirmar': un positivo va a colonoscopia"
frase_permitida: "En tu muestra de heces se encontró sangre que no se ve a simple vista. Tiene varias causas posibles, y la manera de saber cuál es una colonoscopia. Te recomendamos consulta médica en las próximas semanas para pedirla."
frases_prohibidas: ["tienes cáncer", "tienes un tumor", "tienes pólipos", "repite la prueba"]
recomendaciones_sugeridas: ["consulta médica para colonoscopia"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo en edad | Edad 58, FIT positivo | Activa, escalamiento 2 |
| Positivo joven | Edad 34, FIT positivo | Activa, escalamiento 2; la vista médica anota que está fuera de la franja formal |
| Con anemia | FIT positivo y anemia por déficit de hierro (M3) | Activa; la vista médica los cruza |
| Negativo · PDF ejemplos | FIT negativo | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-005 · Infección por *H. pylori*

**Qué detecta.** Antígeno de *H. pylori* positivo en heces. La guía colombiana de 2025 recomienda tratar a todo adulto con infección activa, tenga o no síntomas. La prueba de aliento con urea C13 es la referencia no invasiva; el antígeno fecal es la única opción de la toma domiciliaria y su limitación se escribe en el informe. Un resultado negativo puede ser falso si la persona tomó inhibidores de bomba o antibióticos en las semanas previas.

```yaml
id: COND-M4-GA-005
nombre: Infección por H. pylori
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: antigeno_positivo
    biomarcador: hpylori_stool_ag
    condicion: "positivo"
  - id: falso_negativo_posible
    contexto: medicamentos
    condicion: "inhibidor de bomba de protones en 2 semanas OR antibiótico o bismuto en 4 semanas"
regla_central: "antigeno_positivo"
coincidencia:
  alta: "antigeno_positivo"
escalamiento: 2
negativo_con_medicamentos: "resultado negativo no concluyente; se informa en la vista médica"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["Asociación Colombiana de Gastroenterología 2025, H. pylori"]
por_verificar: "Guía leída solo por resultado de búsqueda; confirmar la recomendación de tratar a todo adulto y las ventanas sin medicamentos (2 y 4 semanas) en el texto completo."
frase_permitida: "En tu muestra de heces se detectó la bacteria H. pylori, que vive en el estómago y es muy común. Las guías colombianas recomiendan tratarla aunque no tengas síntomas: pide una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes úlcera", "tienes gastritis", "tienes cáncer de estómago", "toma antibióticos"]
recomendaciones_sugeridas: ["consulta médica para tratamiento", "no automedicarse con antibióticos"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Antígeno positivo | Activa, escalamiento 2; el informe incluye la limitación del método |
| Negativo con omeprazol | Antígeno negativo, omeprazol diario | No activa; vista médica: negativo no concluyente |
| Negativo · PDF mujer 34 años | Antígeno negativo, sin medicamentos | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-006 · Enfermedad celíaca (prueba dirigida)

**Qué detecta.** Anti-transglutaminasa IgA positiva con IgA total normal. No se tamiza a toda la población: el laboratorio corre las reflejas solo con déficit de hierro sin causa, transaminasas altas, enfermedad tiroidea o familiar de primer grado celíaco. La persona debe estar comiendo gluten. La biopsia confirma.

```yaml
id: COND-M4-GA-006
nombre: Enfermedad celíaca (prueba dirigida)
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D3
activa_refleja_si: ["COND-M3-HE-002 o HE-003 sin causa evidente", "COND-M4-GA-002 activa", "condición tiroidea activa en M2", "familiar de primer grado con celiaquía"]
criterios:
  - id: ttg_positivo
    biomarcador: anti_ttg_iga
    condicion: "> límite superior del laboratorio"
  - id: iga_normal
    biomarcador: iga
    condicion: "dentro del intervalo"
  - id: iga_baja
    biomarcador: iga
    condicion: "< límite inferior del laboratorio"
  - id: dieta_con_gluten
    contexto: cuestionario
    condicion: "come gluten de forma habitual"
regla_central: "ttg_positivo AND iga_normal"
no_interpretable_si: ["iga_baja (el anti-tTG IgA puede salir falsamente negativo; la vista médica sugiere pruebas basadas en IgG)", "dieta sin gluten"]
coincidencia:
  alta: "regla_central AND dieta_con_gluten"
  moderada: "regla_central sin dato de dieta"
escalamiento: 2
nivel_lenguaje: patron_compatible
guias: ["ACG 2023, enfermedad celíaca"]
por_verificar: "Guía leída solo por resumen; confirmar indicaciones de prueba dirigida."
frase_permitida: "Una prueba relacionada con la intolerancia al gluten (anti-transglutaminasa) salió positiva. Sigue comiendo como siempre y pide una consulta médica: confirmarlo requiere otros estudios."
frases_prohibidas: ["tienes celiaquía", "deja el gluten"]
recomendaciones_sugeridas: ["no dejar el gluten antes de la evaluación médica", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Déficit de hierro, anti-tTG 48 (menor de 7), IgA normal, come gluten | Activa, coincidencia alta, escalamiento 2 |
| Déficit de IgA | Anti-tTG 2, IgA 5 (bajo) | No interpretable; sugiere pruebas basadas en IgG |
| Negativo · PDF mujer 34 años | Anti-tTG 2,1, IgA 210 | No activa: sin señal de celiaquía |
| Sin gluten | Anti-tTG 3, dieta sin gluten | No interpretable |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-A01 · Bilirrubina indirecta elevada aislada (apoyo)

**Qué detecta.** Bilirrubina total alta con directa normal y el resto de pruebas hepáticas normales. Sin anemia ni signos de hemólisis, suele ser un patrón benigno y frecuente. Con anemia, reticulocitos altos y LDH alta, se lee junto con la relación de hemólisis del documento 03.

```yaml
id: COND-M4-GA-A01
nombre: Bilirrubina indirecta elevada aislada
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: apoyo
detectabilidad: D1
calculo: "bilirrubina indirecta = bilirrubina total - bilirrubina directa"
criterios:
  - id: bt_alta
    biomarcador: bilirubin_total
    condicion: "> límite superior"
  - id: bd_normal
    biomarcador: bilirubin_direct
    condicion: "dentro del intervalo"
  - id: resto_hepatico_normal
    condicion: "ALT, AST, ALP y GGT dentro del intervalo"
  - id: signos_hemolisis
    condicion: "anemia (HE-001) AND reticulocitos altos AND LDH alta"
regla_central: "bt_alta AND bd_normal AND resto_hepatico_normal"
efecto: "Sin signos_hemolisis: resultado observado, escalamiento 0. Con signos_hemolisis: activa la relación hemólisis (escalamiento 2)."
confusores: ["ayuno prolongado (sube la bilirrubina indirecta)", "hemólisis de la muestra"]
guias: ["ACG 2017"]
frase_permitida: "Tu bilirrubina está un poco alta, con el resto del hígado normal. Es un patrón frecuente y casi siempre benigno; puede subir con el ayuno."
frases_prohibidas: ["tienes síndrome de Gilbert", "tienes ictericia", "tienes una enfermedad del hígado"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Aislada | Bilirrubina total 1,9, directa 0,3, resto normal, hemoglobina normal | Resultado observado, escalamiento 0 |
| Con hemólisis | Bilirrubina total 2,4, directa 0,3, anemia, reticulocitos altos, LDH alta | Activa relación hemólisis, escalamiento 2 |
| Negativo · PDF ejemplos | Bilirrubina total 0,80 y 0,50 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-GA-A02 · Alteración hepática con consumo de alcohol (apoyo)

**Qué detecta.** Transaminasas o GGT alteradas en una persona que declara consumo de alcohol. Una AST que supera claramente a la ALT con GGT alta orienta a alcohol. Refuerza GA-001 y GA-002 y cambia el foco de las recomendaciones.

```yaml
id: COND-M4-GA-A02
nombre: Alteración hepática con consumo de alcohol
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: apoyo
detectabilidad: D2
criterios:
  - id: alcohol
    contexto: cuestionario
    condicion: "consumo de alcohol declarado por encima del límite que defina el médico"
  - id: ast_mayor_alt
    condicion: "AST / ALT >= 2"
  - id: ggt_alta
    biomarcador: ggt
    condicion: "> límite superior"
regla_central: "alcohol AND (ggt_alta OR COND-M4-GA-002 activa)"
modifica: ["COND-M4-GA-001", "COND-M4-GA-002", "COND-M1-CA-003"]
efecto: "La recomendación principal pasa a reducir el alcohol; si ast_mayor_alt, la vista médica lo destaca."
guias: ["ACG 2017"]
por_verificar: "Falta definir con el médico el cuestionario de alcohol y el límite de consumo."
frase_permitida: "Tus pruebas del hígado muestran cambios que se relacionan con el consumo de alcohol. Reducirlo es lo que más le ayuda a tu hígado."
frases_prohibidas: ["eres alcohólico", "tienes cirrosis", "tienes hepatitis alcohólica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Alcohol diario, AST 92, ALT 40, GGT 210 | Activa; destaca AST/ALT de 2,3 |
| Solo GGT | Alcohol los fines de semana, GGT 88 | Activa |
| Sin alcohol · PDF hombre 46 años | Sin dato de alcohol (lo pregunta la enfermera), GGT 72 | No activa hasta tener el dato |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-IN-001 · Hepatitis C

**Qué detecta.** Anti-VHC reactivo. El laboratorio corre ARN viral como refleja: detectable indica infección activa; no detectable indica infección resuelta o un falso positivo del anticuerpo. Por decisión del equipo se mide a todos con el consentimiento de la visita. Un reactivo lo comunica el médico por llamada.

```yaml
id: COND-M4-IN-001
nombre: Hepatitis C
modulo: M4
especialidad: infectologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: anti_vhc_reactivo
    biomarcador: anti_hcv
    condicion: "reactivo"
  - id: arn_detectable
    biomarcador: hcv_rna
    condicion: "detectable"
  - id: arn_no_detectable
    biomarcador: hcv_rna
    condicion: "no detectable"
regla_central: "anti_vhc_reactivo"
variantes:
  infeccion_activa: "anti_vhc_reactivo AND arn_detectable"
  resuelta_o_falso_positivo: "anti_vhc_reactivo AND arn_no_detectable"
  pendiente: "anti_vhc_reactivo AND ARN aún no reportado"
coincidencia:
  alta: "infeccion_activa"
  moderada: "pendiente"
  baja: "resuelta_o_falso_positivo"
escalamiento: 2
canal: "llamada del médico; el informe no se publica antes de la llamada; nunca por WhatsApp"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["Minsalud, tamización de hepatitis C", "USPSTF 2020"]
por_verificar: "Lineamiento del Ministerio leído solo por resultado de búsqueda."
frase_permitida_activa: "Tu prueba de hepatitis C salió positiva y el virus está activo. Hoy existe tratamiento que la cura en la mayoría de personas. Nuestro médico te explicará los pasos a seguir."
frase_permitida_resuelta: "Tu prueba de anticuerpos de hepatitis C salió reactiva, pero el virus no está activo. Puede ser una infección pasada ya resuelta; tu médico te explicará qué significa."
frases_prohibidas: ["tienes cirrosis", "es incurable", "contagias a tu familia"]
recomendaciones_sugeridas: ["consulta con el médico tratante para tratamiento", "no compartir objetos con sangre (cuchillas, cepillos)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Activa | Anti-VHC reactivo, ARN detectable | Activa, coincidencia alta, escalamiento 2, llamada |
| Resuelta | Anti-VHC reactivo, ARN no detectable | Activa, coincidencia baja, llamada con texto de resuelta |
| Pendiente | Anti-VHC reactivo, ARN en proceso | Informe en espera; llamada cuando llegue el ARN |
| Negativo · PDF ejemplos | Anti-VHC no reactivo | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-IN-002 · Hepatitis B y estado frente a la vacuna

**Qué detecta.** Interpreta el panel triple (HBsAg, anti-HBc total y anti-HBs) en cinco estados, de infección activa a persona susceptible que necesita vacuna. Por decisión del equipo se mide a todos con el consentimiento de la visita. Los estados con infección los comunica el médico por llamada.

```yaml
id: COND-M4-IN-002
nombre: Hepatitis B y estado frente a la vacuna
modulo: M4
especialidad: infectologia
tipo: incluida
detectabilidad: D3
estados:
  infeccion_activa:
    regla: "HBsAg reactivo"
    escalamiento: 2
    canal: "llamada del médico"
  infeccion_pasada_resuelta:
    regla: "HBsAg no reactivo AND anti-HBc reactivo AND anti-HBs >= 10"
    escalamiento: 1
    nota: "riesgo de reactivación con inmunosupresión o quimioterapia; la vista médica lo destaca"
  anti_hbc_aislado:
    regla: "HBsAg no reactivo AND anti-HBc reactivo AND anti-HBs < 10"
    escalamiento: 2
    canal: "llamada del médico"
    nota: "varias interpretaciones posibles; el médico puede pedir carga viral"
  inmune_por_vacuna:
    regla: "HBsAg no reactivo AND anti-HBc no reactivo AND anti-HBs >= 10"
    escalamiento: 0
  susceptible:
    regla: "HBsAg no reactivo AND anti-HBc no reactivo AND anti-HBs < 10"
    escalamiento: 1
    nota: "recomendar vacuna; oferta de vacunación domiciliaria pendiente de validar con el esquema del PAI para adultos"
regla_central: "infeccion_activa OR anti_hbc_aislado OR infeccion_pasada_resuelta"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["CDC 2023, interpretación serológica de hepatitis B", "Res. 1314 de 2020"]
por_verificar: "Fuentes leídas solo por resultado de búsqueda; confirmar la tabla de interpretación y el esquema del PAI para adultos."
frase_permitida_activa: "Tu prueba de hepatitis B muestra una infección. Nuestro médico te va a llamar para explicarte qué significa y los siguientes pasos."
frase_permitida_susceptible: "No tienes defensas contra la hepatitis B. La buena noticia es que existe una vacuna segura y efectiva; pregúntale a tu médico o a nosotros cómo aplicártela."
frase_permitida_inmune: "Tienes defensas contra la hepatitis B, probablemente por la vacuna."
frases_prohibidas: ["tienes hepatitis crónica", "tienes cirrosis", "es incurable"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Susceptible · PDF hombre 46 años | HBsAg no reactivo, anti-HBc no reactivo, anti-HBs 4,2 | Estado susceptible, escalamiento 1, recomendación de vacuna |
| Inmune · PDF mujer 34 años | HBsAg y anti-HBc no reactivos, anti-HBs 85 | Inmune por vacuna, escalamiento 0 |
| Activa | HBsAg reactivo | Escalamiento 2, llamada |
| Resuelta | HBsAg no reactivo, anti-HBc reactivo, anti-HBs 120 | Escalamiento 1, nota de reactivación |
| Anti-HBc aislado | HBsAg no reactivo, anti-HBc reactivo, anti-HBs 3 | Escalamiento 2, llamada |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-IN-003 · Enfermedad de Chagas crónica

**Qué detecta.** Primera ELISA (antígenos totales) reactiva, confirmada con una segunda ELISA de antígenos recombinantes que corre el laboratorio como refleja. Si las dos discrepan, se necesita una tercera prueba. La infección crónica puede afectar el corazón años después, por eso se remite. La indicación fuera del embarazo sigue pendiente de fuente (lineamiento del INS para adultos).

```yaml
id: COND-M4-IN-003
nombre: Enfermedad de Chagas crónica
modulo: M4
especialidad: infectologia
tipo: incluida
detectabilidad: D2
criterios:
  - id: elisa_1_reactiva
    biomarcador: chagas_elisa_total
    condicion: "reactivo"
  - id: elisa_2_reactiva
    biomarcador: chagas_elisa_recombinante
    condicion: "reactivo"
  - id: procedencia_endemica
    contexto: cuestionario
    condicion: "nació, vivió o vive en municipio endémico (lista por definir con el médico)"
regla_central: "elisa_1_reactiva AND elisa_2_reactiva"
variantes:
  discordante: "elisa_1_reactiva AND NOT elisa_2_reactiva (tercera prueba; informe en espera)"
coincidencia:
  alta: "regla_central AND procedencia_endemica"
  moderada: "regla_central sin procedencia endémica conocida"
escalamiento: 2
canal: "llamada del médico; nunca por WhatsApp"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["Minsalud, algoritmo de Chagas (pieza para gestantes)"]
por_verificar: "Lineamiento del INS para adultos fuera del embarazo y lista de municipios endémicos. Sin ellos, la ficha no debería usarse con pacientes reales."
frase_permitida: "Tus dos pruebas para la enfermedad de Chagas salieron reactivas. Es una infección que puede no dar síntomas por años y que tiene manejo; nuestro médico te va a llamar para explicarte los pasos, que incluyen una revisión del corazón."
frases_prohibidas: ["tienes daño en el corazón", "es mortal", "es incurable"]
recomendaciones_sugeridas: ["consulta médica", "evaluación cardíaca según indique el médico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Dos ELISA reactivas, nacido en municipio endémico | Activa, coincidencia alta, escalamiento 2, llamada |
| Discordante | ELISA total reactiva, recombinante no reactiva | Informe en espera de tercera prueba |
| Negativo · PDF ejemplos | ELISA total no reactiva | No activa; no se corre la segunda |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-IN-A01 · Infección urinaria con síntomas (apoyo)

**Qué detecta.** Uroanálisis alterado (nitritos, esterasa leucocitaria o leucocitos en el sedimento) solo cuenta si hay síntomas: ardor, urgencia o fiebre, que pregunta la enfermera. Sin síntomas no se reporta como infección, salvo en el embarazo. El urocultivo no está entre las 18 reflejas: lo pide el médico.

```yaml
id: COND-M4-IN-A01
nombre: Infección urinaria con síntomas
modulo: M4
especialidad: infectologia
tipo: apoyo
detectabilidad: D2
criterios:
  - id: uroanalisis_alterado
    condicion: "nitritos positivos OR esterasa leucocitaria positiva OR leucocitos > 5 por campo"
  - id: sintomas
    contexto: visita
    condicion: "ardor al orinar OR urgencia OR fiebre"
  - id: embarazo
    contexto: perfil
    condicion: "true"
regla_central: "uroanalisis_alterado AND sintomas"
reglas_especiales:
  - "uroanalisis_alterado sin sintomas y sin embarazo: no se reporta como infección (IDSA 2019)"
  - "uroanalisis_alterado con embarazo: vista médica, escalamiento 1 (requiere urocultivo)"
modifica: ["COND-M2-NE-002 (la infección eleva la albuminuria)", "COND-M2-NE-006 (la infección explica hematuria)"]
escalamiento: 1
guias: ["IDSA 2019, bacteriuria asintomática"]
frase_permitida: "Tu examen de orina y tus síntomas sugieren una posible infección urinaria. Consulta para confirmarlo con un urocultivo."
frases_prohibidas: ["tienes una infección", "toma antibiótico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Con síntomas | Nitritos positivos, ardor al orinar | Activa, escalamiento 1 |
| Sin síntomas | Esterasa positiva, sin síntomas, no embarazada | No se reporta |
| Embarazo | Nitritos positivos, embarazo de 14 semanas | Vista médica, escalamiento 1 |
| Negativo · PDF ejemplos | Uroanálisis normal | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M4-IN-A02 · Parasitosis intestinal (apoyo)

**Qué detecta.** Parásitos en el coprológico. Se separan los patógenos de los comensales (que no requieren tratamiento) y se cruza con la eosinofilia del módulo M3. La fuente colombiana sigue pendiente.

```yaml
id: COND-M4-IN-A02
nombre: Parasitosis intestinal
modulo: M4
especialidad: infectologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: parasito_patogeno
    biomarcador: stool_parasites
    condicion: "Giardia, Entamoeba histolytica/dispar, helmintos u otro patógeno según la lista firmada por el médico"
  - id: parasito_comensal
    biomarcador: stool_parasites
    condicion: "comensal según la lista firmada por el médico"
regla_central: "parasito_patogeno"
modificado_por: ["COND-M3-HE-A03"]
escalamiento:
  parasito_patogeno: 1
  parasito_comensal: 0
guias: ["Pendiente de fuente colombiana"]
por_verificar: "Lista de parásitos patógenos y comensales; algunos (por ejemplo, Blastocystis) tienen significado discutido. El médico debe firmar la lista."
frase_permitida: "En tu muestra de heces se encontró un parásito que suele requerir tratamiento. Consulta con tu médico."
frase_comensal: "En tu muestra apareció un microorganismo que normalmente no causa enfermedad ni necesita tratamiento."
frases_prohibidas: ["toma antiparasitario", "desparasítate"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Patógeno | Quistes de Giardia | Activa, escalamiento 1 |
| Con eosinofilia | Huevos de helminto, eosinófilos 0,9 × 10³/µL | Activa, reforzada por HE-A03 |
| Comensal | Quistes de Entamoeba coli | Informativo, escalamiento 0 |
| Negativo · PDF ejemplos | No se observaron parásitos | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Resultado esperado del módulo M4 en los PDF de ejemplo

| PDF | Activa | No activa | No calculable o pendiente |
| --- | --- | --- | --- |
| Hombre 46 años (LCD-2026-100123) | *H. pylori* positivo (escalamiento 2, con la limitación del método); alteración hepatocelular (ALT 58, coincidencia moderada, escalamiento 1); hepatitis B en estado susceptible (recomendación de vacuna) | FIB-4 (0,89, bajo; se muestra en la vista médica), colestasis, sangre oculta, hepatitis C, Chagas, orina, parásitos | Apoyo por alcohol pendiente del dato de la enfermera; celiaquía: el laboratorio no corrió la refleja aunque la ALT está alta (ver nota) |
| Mujer 34 años (LCD-2026-100124) | Hepatitis B: inmune por vacuna (escalamiento 0) | Hígado, sangre oculta, *H. pylori*, hepatitis C, Chagas, orina, parásitos | Celiaquía: refleja corrida por déficit de hierro, sin señal (anti-tTG negativo con IgA normal) |

**Nota sobre el caso del hombre.** Según el Consolidado, la ALT alta también activa la refleja de celiaquía. El PDF de ejemplo del hombre no la incluye. Hay que decidir si se corrige el PDF de ejemplo o si la ALT apenas por encima del laboratorio no debe activarla.

## Lo que el médico debe mirar con más cuidado

1. Todas las guías del módulo están leídas solo por resultado de búsqueda, salvo una: leer completas al menos la de *H. pylori* 2025, el lineamiento de hepatitis C y el del INS para Chagas.
2. Chagas no debería usarse con pacientes reales hasta tener el lineamiento del INS para adultos y la lista de municipios endémicos.
3. Regla de FIB-4 en mayores de 65 y en personas con diabetes.
4. Factor R y el doble del límite para escalar la alteración colestásica.
5. Cuestionario y límite de consumo de alcohol que usará la enfermera.
6. Lista de parásitos patógenos y comensales.
7. Si la ALT apenas alta debe activar la refleja de celiaquía.