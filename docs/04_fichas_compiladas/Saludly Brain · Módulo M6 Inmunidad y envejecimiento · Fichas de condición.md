# Módulo M6 · Inmunidad y envejecimiento — Fichas de condición

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento convierte las condiciones de Reumatología y de Medicina interna y envejecimiento (Lote 6) en reglas que el motor puede ejecutar. Son 6 fichas: 2 condiciones incluidas y 4 de apoyo. Con este módulo quedan escritas las fichas de condición de los seis módulos.

## Cómo leer y cómo firmar

Igual que en los módulos anteriores: `tipo`, `detectabilidad`, `regla_central`, `coincidencia` (alta, moderada, baja = vigilar), `escalamiento` (0 a 3) y `por_verificar`. Para firmar: leer la ficha con sus casos, marcar aprobada, aprobada con cambios o rechazada, escribir los cambios y poner nombre, registro ReTHUS y fecha.

## Reglas comunes del módulo

- **ANA y VSG** se alteran con frecuencia en personas sin enfermedad. Entran como apoyo con reglas de lectura estrictas, nunca como condiciones.
- **Edad biológica** se muestra en una pantalla aparte del informe clínico, como estimación de un modelo publicado. No cambia hallazgos ni escalamientos.
- **Riesgo de desnutrición** se reporta solo como riesgo; GLIM fue diseñado para entornos clínicos.

## Índice

| ID | Condición | Tipo | Detectabilidad | Datos que usa | Escalamiento |
| --- | --- | --- | --- | --- | --- |
| COND-M6-RE-001 | Ácido úrico alto sin síntomas | Incluida | D1 | Ácido úrico, TFG, contexto cardiometabólico | 1 |
| COND-M6-RE-A01 | ANA positivo | Apoyo | D3 | ANA por IFI en HEp-2 con título y patrón | 1 o 2 |
| COND-M6-RE-A02 | VSG alta | Apoyo | D1 | VSG, hs-CRP, hemoglobina, edad, sexo | 1 o 2 |
| COND-M6-MI-001 | Riesgo de desnutrición | Incluida | D2 | Peso, talla, edad, hs-CRP, pérdida de peso, ingesta | 1 o 2 |
| COND-M6-MI-A01 | Lectura por edad del panel | Apoyo | D1 | Edad y todo el panel | Regla transversal |
| COND-M6-MI-A02 | Edad biológica (PhenoAge) | Apoyo | D1 | Edad y 9 analitos | 0 |

Descartadas en el Lote 6: gota (se define por crisis articulares), artritis reumatoide (exige sinovitis clínica), longitud de telómeros, sarcopenia probable (exige dinamómetro, que no entra en la versión 1), fragilidad y osteoporosis.

---

## COND-M6-RE-001 · Ácido úrico alto sin síntomas

**Qué detecta.** Ácido úrico por encima del intervalo del laboratorio. La ACR 2020 recomienda no iniciar medicamentos para bajarlo si no hay gota, así que el informe orienta a hábitos y lo lee junto con el contexto cardiometabólico y renal.

```yaml
id: COND-M6-RE-001
nombre: Ácido úrico alto sin síntomas
modulo: M6
especialidad: reumatologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: urico_alto
    biomarcador: uric_acid
    condicion: "> límite superior del laboratorio (por sexo)"
    unidad: mg/dL
regla_central: "urico_alto"
contexto_vista_medica: ["síndrome metabólico (M1 EM-003)", "prediabetes o diabetes (M1)", "TFG baja (M2)", "hipertensión (M1 CA-006)", "diuréticos", "alcohol"]
coincidencia:
  alta: "urico_alto"
escalamiento: 1
nivel_lenguaje: resultado_observado
confusores: ["diuréticos tiazídicos o de asa", "deshidratación", "ayuno prolongado", "ejercicio intenso reciente", "dieta muy alta en carnes rojas, vísceras o mariscos"]
reglas_seguridad: ["no sugerir medicamentos para bajar el ácido úrico", "si la persona declara dolor e hinchazón súbita de una articulación, recomendar consulta"]
guias: ["ACR 2020, gota"]
por_verificar: "Guía leída solo por resultado de búsqueda."
frase_permitida: "Tu ácido úrico está por encima del rango. Sin síntomas no necesita medicamentos, pero suele mejorar con los mismos hábitos que cuidan el corazón y el metabolismo."
frases_prohibidas: ["tienes gota", "tienes artritis", "toma alopurinol"]
recomendaciones_sugeridas: ["reducir alcohol, sobre todo cerveza", "reducir bebidas azucaradas", "moderar carnes rojas, vísceras y mariscos", "buena hidratación", "control de peso"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Ácido úrico 7,6 (hasta 7,0), con prediabetes y síndrome metabólico | Activa, escalamiento 1; la vista médica lo liga al contexto cardiometabólico |
| Con diurético | Ácido úrico 8,2, toma hidroclorotiazida | Activa; la vista médica menciona el diurético |
| Negativo · PDF mujer 34 años | Ácido úrico 4,1 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M6-RE-A01 · ANA positivo (apoyo)

**Qué detecta.** Anticuerpos antinucleares positivos por inmunofluorescencia en células HEp-2, con título y patrón. Cerca del 14 % de la población general tiene ANA positivo sin enfermedad, y los criterios EULAR/ACR 2019 usan 1:80 o más solo como puerta de entrada que exige criterios clínicos. El informe explica que es frecuente y nunca habla de lupus ni de enfermedad autoinmune.

**Corrección a la regla del documento 03.** La regla anterior trataba el patrón moteado fino (AC-4) como el más benigno. En la literatura, el patrón que más se asocia a personas sanas es el moteado fino denso (AC-2, anticuerpos DFS70). Esta ficha usa el título como regla principal y deja el AC-2 como nota en la vista médica. El médico decide cuál de las dos reglas queda.

```yaml
id: COND-M6-RE-A01
nombre: ANA positivo
modulo: M6
especialidad: reumatologia
tipo: apoyo
detectabilidad: D3
criterios:
  - id: ana_1_80
    biomarcador: ana_hep2
    condicion: "título 1:80"
  - id: ana_1_160_o_mas
    biomarcador: ana_hep2
    condicion: "título >= 1:160"
  - id: patron
    biomarcador: ana_hep2_patron
    condicion: "patrón ICAP (AC-xx) reportado"
regla_central: "ana_1_80 OR ana_1_160_o_mas"
no_interpretable_si: ["positivo sin título o sin patrón"]
escalamiento:
  ana_1_80: 1
  ana_1_160_o_mas: 2
nota_vista_medica: ["patrón AC-2 (moteado fino denso): frecuente en personas sanas", "anti-TPO positivo o TSH alta (M2): la autoinmunidad tiroidea se asocia a ANA positivo"]
nivel_lenguaje: resultado_observado
guias: ["Satoh 2012 (prevalencia en población general)", "Criterios EULAR/ACR 2019 para lupus"]
por_verificar: "Regla de patrón: AC-4 (regla anterior) o AC-2 (literatura). El médico define desde qué título y patrón se recomienda consulta."
frase_permitida: "Tus anticuerpos antinucleares (ANA) salieron positivos con un título de {titulo}. Es un resultado frecuente en personas sanas y por sí solo no indica ninguna enfermedad; conviene comentarlo con tu médico, sobre todo si tienes dolor en las articulaciones, manchas en la piel o fiebre sin causa."
frases_prohibidas: ["tienes lupus", "tienes una enfermedad autoinmune", "tu sistema inmune te está atacando"]
recomendaciones_sugeridas: ["consulta médica si el título es 1:160 o más o si hay síntomas"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | ANA positivo 1:160, patrón moteado fino (AC-4), anti-TPO 186 | Escalamiento 2; la vista médica anota la autoinmunidad tiroidea |
| Título bajo | ANA 1:80, AC-2 | Escalamiento 1; nota de patrón frecuente en sanos |
| Sin título | "ANA positivo" sin título | No interpretable; pedir título y patrón al laboratorio |
| Negativo · PDF hombre 46 años | ANA negativo (menor de 1:80) | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M6-RE-A02 · VSG alta (apoyo)

**Qué detecta.** Velocidad de sedimentación por encima del intervalo del laboratorio. Es una señal inflamatoria inespecífica que se lee siempre junto con la hs-CRP; la anemia, el embarazo y la edad la suben. Aislada, se sugiere repetir, sin asociarla a ninguna enfermedad.

```yaml
id: COND-M6-RE-A02
nombre: VSG alta
modulo: M6
especialidad: reumatologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: vsg_alta
    biomarcador: esr
    condicion: "> límite superior del laboratorio (por sexo y edad)"
    unidad: mm/h
  - id: vsg_muy_alta
    biomarcador: esr
    condicion: ">= 100"
    unidad: mm/h
  - id: hscrp_alta
    biomarcador: hs_crp
    condicion: "> 5"
    unidad: mg/L
regla_central: "vsg_alta"
efecto: "Con hscrp_alta, refuerza la relación de inflamación (vigilar, documento 03). Con anemia (M3), la vista médica anota que la anemia sube la VSG."
escalamiento:
  base: 1
  si_vsg_muy_alta: 2
confusores: ["anemia", "embarazo", "edad avanzada", "infección reciente", "obesidad"]
guias: ["ACR/EULAR 2010 (como reactante de fase aguda solo con sinovitis clínica)"]
por_verificar: "Escalamiento 2 con 100 mm/h o más es propuesta de Saludly."
frase_permitida: "Tu velocidad de sedimentación, una señal general de inflamación, está por encima del rango. Puede subir por muchas causas, incluso pasajeras; conviene repetirla."
frases_prohibidas: ["tienes artritis", "tienes una enfermedad reumática", "tienes cáncer"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Aislada | VSG 28 (hasta 15), hs-CRP 1,2 | Escalamiento 1, repetir |
| Con inflamación | VSG 35, hs-CRP 14 | Refuerza la relación de inflamación |
| Muy alta | VSG 110 | Escalamiento 2 |
| Negativo · PDF ejemplos | VSG 12 y 18 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M6-MI-001 · Riesgo de desnutrición

**Qué detecta.** Un criterio fenotípico (IMC bajo para la edad o pérdida de peso no intencional) con un criterio etiológico (inflamación por hs-CRP alta o ingesta reducida). GLIM exige uno de cada tipo y fue diseñado para entornos clínicos, así que el informe habla de riesgo, nunca de desnutrición.

```yaml
id: COND-M6-MI-001
nombre: Riesgo de desnutrición
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: incluida
detectabilidad: D2
calculo: "imc = peso_kg / talla_m^2 (medidos por la enfermera)"
criterios_fenotipicos:
  - id: imc_bajo
    condicion: "imc < 20 si edad < 70; imc < 22 si edad >= 70"
  - id: perdida_peso
    contexto: cuestionario
    condicion: "pérdida de peso no intencional > 5 % en 6 meses"
criterios_etiologicos:
  - id: inflamacion
    biomarcador: hs_crp
    condicion: "> 5"
    unidad: mg/L
  - id: ingesta_reducida
    contexto: cuestionario
    condicion: "come menos de lo habitual desde hace más de una semana"
regla_central: "(imc_bajo OR perdida_peso) AND (inflamacion OR ingesta_reducida)"
coincidencia:
  alta: "regla_central"
  baja: "criterio fenotípico sin criterio etiológico (vigilar)"
escalamiento:
  base: 1
  edad_70_o_mas: 2
nivel_lenguaje: riesgo_potencial
relacion: ["albúmina baja y anemia se muestran como contexto en la vista médica, no como criterios GLIM"]
guias: ["GLIM 2019"]
por_verificar: "La pérdida de peso y la ingesta dependen de que la enfermera las pregunte; confirmar que estén en el formulario de la visita. El corte de hs-CRP de 5 mg/L sigue la regla del módulo M3."
frase_permitida: "Tu peso y algunos resultados sugieren que tu cuerpo podría no estar recibiendo toda la energía y la proteína que necesita. Conviene revisarlo con tu médico o con un nutricionista."
frases_prohibidas: ["estás desnutrido", "estás muy flaco", "tienes desnutrición"]
recomendaciones_sugeridas: ["consulta con nutricionista", "comidas frecuentes con proteína", "consulta médica si la pérdida de peso no es buscada"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo mayor | Edad 74, IMC 20,8, hs-CRP 9 | Activa, coincidencia alta, escalamiento 2 |
| Positivo joven | Edad 40, IMC 18,6, come menos hace un mes | Activa, escalamiento 1 |
| Vigilar | Edad 30, IMC 19,2, hs-CRP 0,6, ingesta normal | Vigilar |
| Sin medidas · PDF ejemplos | Peso y talla aún no registrados | No interpretable |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M6-MI-A01 · Lectura por edad del panel (apoyo)

**Qué detecta.** No es una condición: reúne en un solo lugar las reglas por edad que ya están repartidas en los módulos, para que el motor las aplique siempre igual. La edad entra en la interpretación, nunca en la selección de pruebas.

```yaml
id: COND-M6-MI-A01
nombre: Lectura por edad del panel
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: apoyo
detectabilidad: D1
reglas:
  - "menores de 18 años: fuera del alcance de la versión 1"
  - "SCORE2-PURE solo entre 40 y 69 años (M1 CA-005)"
  - "TSH: corte de decisión 5,0 de 18 a 60 años y 6,0 desde los 61 (M2 TI-001)"
  - "FSH: condición solo en menores de 40; contexto de 40 a 44; sin uso para menopausia desde los 45 (M5 MU-002)"
  - "PSA: tamizaje formal de 50 a 75; fuera de ese rango, valor a revisar (M5 UR-001)"
  - "Sangre oculta: tamizaje formal de 50 a 75; positivo a cualquier edad remite (M4 GA-004)"
  - "FIB-4: menos confiable en menores de 35; un valor bajo no descarta fibrosis desde los 65 (M4 GA-001)"
  - "Desnutrición: IMC < 22 desde los 70 años (M6 MI-001)"
  - "Hemoglobina: la OMS advierte que faltan datos en mayores de 65; la vista médica lo anota (M3 HE-001)"
  - "Recordatorios: cuello uterino 30-65, mamografía 50-69, colorrectal 50-75 (M5)"
  - "PhenoAge: solo dentro del rango de edad del modelo (MI-A02)"
efecto: "Cada ficha consulta esta tabla; si una regla cambia aquí, cambia en todo el motor."
guias: ["Reglas de los Lotes 1 a 6", "OMS 2024, cortes de hemoglobina"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Hombre 46 años | — | SCORE2-PURE aplica; PSA y sangre oculta fuera de franja formal; sin recordatorios |
| Mujer 34 años | — | Sin SCORE2-PURE; FSH interpretable como condición; recordatorio de cuello uterino |
| Persona de 17 años | — | Fuera del alcance; no se procesa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M6-MI-A02 · Edad biológica (PhenoAge) (apoyo)

**Qué detecta.** Estima la edad cuyo riesgo de mortalidad corresponde al de la persona, combinando la edad con 9 analitos que ya están en el panel. Es un modelo publicado (Levine y colaboradores, 2018), entrenado en población de EE. UU. y sin validación conocida en Colombia. Se muestra aparte del informe clínico, como indicador de bienestar para seguir en el tiempo.

```yaml
id: COND-M6-MI-A02
nombre: Edad biológica (PhenoAge)
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: apoyo
detectabilidad: D1
entradas_y_unidades_del_modelo:
  albumina: "g/L (g/dL x 10)"
  creatinina: "µmol/L (mg/dL x 88,4)"
  glucosa: "mmol/L (mg/dL / 18,016), en ayunas"
  pcr: "mg/dL (hs-CRP en mg/L / 10), en logaritmo natural"
  linfocitos: "%"
  vcm: "fL"
  rdw: "%"
  fosfatasa_alcalina: "U/L"
  leucocitos: "10^3/µL"
  edad: "años"
calculo:
  xb: "-19,907 - 0,0336 x albúmina + 0,0095 x creatinina + 0,1953 x glucosa + 0,0954 x ln(PCR) - 0,0120 x linfocitos + 0,0268 x VCM + 0,3306 x RDW + 0,00188 x fosfatasa alcalina + 0,0554 x leucocitos + 0,0804 x edad"
  mortalidad: "M = 1 - exp(-exp(xb) x (exp(120 x 0,0076927) - 1) / 0,0076927)"
  phenoage: "141,50225 + ln(-0,00553 x ln(1 - M)) / 0,090165"
se_calcula_si: ["los 9 analitos en estado medido", "glucosa en ayunas", "edad de 20 años o más"]
reglas_especiales:
  - "PCR menor que el límite de detección: se usa el límite y se marca en la vista médica"
  - "Anemia, infección reciente o hs-CRP > 10: se calcula, pero se advierte que el valor puede estar inflado temporalmente"
  - "No se calcula con embarazo"
escalamiento: 0
presentacion: ["pantalla aparte del informe clínico", "edad biológica, edad cronológica y diferencia", "explicación del modelo y su limitación poblacional", "tendencia cuando haya una segunda toma"]
guias: ["Levine et al. 2018, Aging 10(4):573-591"]
por_verificar: "Los coeficientes se tomaron de una implementación pública que cita el artículo; antes de producción, verificarlos contra el artículo original y su ejemplo publicado. Confirmar también el rango de edad del modelo."
frase_permitida: "Con 9 de tus resultados, un modelo científico estima tu edad biológica en {phenoage} años, frente a tus {edad} años. Es una estimación para seguir en el tiempo, no un diagnóstico."
frases_prohibidas: ["vas a vivir menos", "tu cuerpo tiene X años", "estás envejeciendo más rápido (sin una segunda medición)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| PDF hombre 46 años | Albúmina 4,6, creatinina 0,98, glucosa 112, hs-CRP 3,4, linfocitos 31,0 %, VCM 89,9, RDW 13,1, fosfatasa alcalina 88, leucocitos 7,8 | PhenoAge 44,3 años (1,7 menos que su edad) |
| PDF mujer 34 años | Albúmina 4,3, creatinina 0,72, glucosa 86, hs-CRP 0,8, linfocitos 35,0 %, VCM 78,2, RDW 16,4, fosfatasa alcalina 62, leucocitos 6,1 | PhenoAge 34,1 años; advertencia: la anemia sube el RDW y puede inflar el valor |
| Falta un analito | Sin fosfatasa alcalina | No se calcula; se dice qué falta |
| Sin ayuno | Ayuno de 4 horas | No se calcula |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Resultado esperado del módulo M6 en los PDF de ejemplo

| PDF | Activa | No activa | Edad biológica |
| --- | --- | --- | --- |
| Hombre 46 años (LCD-2026-100123) | Ácido úrico alto (escalamiento 1, ligado al contexto cardiometabólico) | ANA, VSG, desnutrición (sin medidas aún) | 44,3 años |
| Mujer 34 años (LCD-2026-100124) | ANA positivo 1:160 (escalamiento 2, con nota de autoinmunidad tiroidea) | Ácido úrico, VSG, desnutrición (sin medidas aún) | 34,1 años, con advertencia por anemia |

## Lo que el médico debe mirar con más cuidado

1. Regla de patrón del ANA: la del documento 03 (AC-4) o la de la literatura (AC-2), y desde qué título se recomienda consulta.
2. Escalamiento 2 con VSG de 100 mm/h o más.
3. Que la enfermera pregunte pérdida de peso e ingesta, necesarias para el riesgo de desnutrición.
4. Coeficientes y rango de edad de PhenoAge, a verificar contra el artículo original.
5. Advertencia de PhenoAge con anemia o inflamación.