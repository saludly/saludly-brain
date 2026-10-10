# Módulo M3 · Sangre y nutrición — Fichas de condición

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento convierte las condiciones de Hematología y de Nutrición y micronutrientes (Lote 3) en reglas que el motor puede ejecutar, y aplica por primera vez la regla de vitaminas aprobada. Son 15 fichas: 8 condiciones incluidas y 7 de apoyo. Cada una trae su regla, el texto que el paciente puede leer, las frases prohibidas, sus casos de prueba y un espacio para la firma del médico.

Ninguna ficha produce un diagnóstico.

## Cómo leer y cómo firmar

Igual que en los módulos M1 y M2: `tipo` (incluida o apoyo), `detectabilidad` (D1, D2, D3), `regla_central`, `coincidencia` (alta, moderada, baja = vigilar), `escalamiento` (0 a 3) y `por_verificar`. Para firmar: leer la ficha con sus casos, marcar aprobada, aprobada con cambios o rechazada, escribir los cambios y poner nombre, registro ReTHUS y fecha.

## Reglas comunes del módulo

- **Hemoglobina ajustada por altitud.** La OMS 2024 ajusta por la altitud de residencia. Entre 2.500 y 2.999 metros (Bogotá) se restan 18 g/L (1,8 g/dL) a la hemoglobina medida antes de compararla con el corte. La ciudad de residencia sale del perfil que toma la enfermera. Si un laboratorio declara que su intervalo ya es de población bogotana, no se ajusta dos veces. El laboratorio del PDF de ejemplo usa intervalos generales, así que se ajusta.
- **Cortes OMS de anemia (adultos).** Hombres: menos de 13,0 g/dL. Mujeres no gestantes: menos de 12,0. Gestantes: menos de 11,0 en primer y tercer trimestre, y menos de 10,5 en el segundo.
- **Ferritina siempre con hs-CRP.** Déficit con ferritina menor de 15 ng/mL; si hs-CRP es mayor de 5 mg/L, el corte sube a 70.
- **B12.** Menor de 180 ng/L (pg/mL) confirma déficit; entre 180 y 350 es indeterminado y activa ácido metilmalónico.
- **Vitaminas.** Regla aprobada del documento 07: se clasifican con el intervalo del laboratorio; las recomendaciones son alimentarias y el suplemento solo se menciona como opción general para hablar con el médico, sin dosis.

## Índice

| ID | Condición | Tipo | Detectabilidad | Datos que usa | Escalamiento |
| --- | --- | --- | --- | --- | --- |
| COND-M3-HE-001 | Anemia ajustada por altitud y tabaquismo | Incluida | D2 | Hemoglobina, ciudad, tabaquismo, sexo, embarazo | 1, 2 o 3 |
| COND-M3-HE-002 | Anemia por déficit de hierro | Incluida | D1 | HE-001, ferritina, hs-CRP, saturación, VCM, RDW | 2 |
| COND-M3-HE-003 | Déficit de hierro sin anemia | Incluida | D1 | Ferritina, hs-CRP, hemoglobina ajustada | 1 o 2 |
| COND-M3-HE-004 | Anemia por déficit de B12 o folato | Incluida | D1 | HE-001, VCM, B12, folato, ácido metilmalónico | 2 |
| COND-M3-HE-005 | Plaquetas bajas | Incluida | D1 | Plaquetas, comentarios del laboratorio | 1, 2 o 3 |
| COND-M3-HE-006 | Posible sobrecarga de hierro | Incluida | D3 | Ferritina, saturación de transferrina, hs-CRP | 2 |
| COND-M3-HE-A01 | Anemia con perfil inflamatorio | Apoyo | D3 | HE-001, ferritina, saturación, hs-CRP | Modifica HE-001 |
| COND-M3-HE-A02 | Leucocitos, neutrófilos o linfocitos fuera de rango | Apoyo | D1 | Hemograma con diferencial | 1 o 3 |
| COND-M3-HE-A03 | Eosinofilia | Apoyo | D1 | Eosinófilos, leucocitos, coprológico | Cruce con M4 |
| COND-M3-NU-001 | Déficit de vitamina B12 | Incluida | D2 | B12, ácido metilmalónico, factores de riesgo | 1 o 2 |
| COND-M3-NU-002 | Déficit de folato | Incluida | D1 | Folato, embarazo | 1 o 2 |
| COND-M3-NU-A01 | Homocisteína alta | Apoyo | D1 | Homocisteína, B12, folato, TFG | Modifica NU-001 y NU-002 |
| COND-M3-NU-A02 | PTH alta con calcio normal | Apoyo | D3 | PTH, calcio corregido, vitamina D, TFG | 1 |
| COND-M3-NU-A03 | Vitamina D baja | Apoyo | D1 | 25-OH vitamina D | 0 |
| COND-M3-NU-A04 | Vitaminas informativas | Apoyo | D1 | B1, B6, A, E, K1, C, biotina, niacina, omega-3, omega-6/omega-3, CoQ10 | 0 a 3 según vitamina |

Descartadas en el Lote 3: hemólisis como condición (exige haptoglobina; queda como relación en el documento 03), rasgo talásemico, hemoglobina alta, alteración de la coagulación como hallazgo preventivo y déficit de zinc, magnesio, selenio, cobre o yodo. Zinc y magnesio quedan como "solo valor y rango". La desnutrición se evalúa en el módulo M6.

---

## COND-M3-HE-001 · Anemia ajustada por altitud y tabaquismo

**Qué detecta.** Hemoglobina por debajo del corte OMS después de restar los ajustes por altitud de residencia y por tabaquismo. No se ajusta por inflamación ni por etnia. Es la base de HE-002 y HE-004, que explican la causa.

```yaml
id: COND-M3-HE-001
nombre: Anemia ajustada por altitud y tabaquismo
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D2
calculo:
  hemoglobina_ajustada: "hemoglobina - ajuste_altitud - ajuste_tabaquismo"
  ajuste_altitud: "según tabla OMS 2024 por metros de la ciudad de residencia; 2.500 a 2.999 m = 1,8 g/dL"
  ajuste_tabaquismo: "según tabla OMS 2024 por cigarrillos al día"
criterios:
  - id: anemia
    condicion: "hemoglobina_ajustada < 13,0 si hombre; < 12,0 si mujer no gestante; < 11,0 gestante en 1.er o 3.er trimestre; < 10,5 gestante en 2.º trimestre"
    unidad: g/dL
severidad_oms:
  mujer_no_gestante: {leve: "11,0-11,9", moderada: "8,0-10,9", severa: "< 8,0"}
  hombre: {leve: "11,0-12,9", moderada: "8,0-10,9", severa: "< 8,0"}
regla_central: "anemia"
contexto_obligatorio: ["sexo", "ciudad de residencia", "embarazo y semana de gestación en mujeres en edad fértil", "edad >= 15"]
coincidencia:
  alta: "anemia con ciudad y tabaquismo conocidos"
  moderada: "anemia sin dato de tabaquismo"
escalamiento:
  leve: 1
  moderada: 2
  severa: 3
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
causas_que_se_evaluan: ["COND-M3-HE-002", "COND-M3-HE-004", "COND-M3-HE-A01", "relación hemólisis (documento 03)"]
guias: ["OMS 2024, cortes de hemoglobina para definir anemia"]
por_verificar: "Los valores del ajuste por tabaquismo deben copiarse de la tabla OMS 2024. Las categorías de severidad en hombres (leve hasta 12,9) siguen la OMS; confirmar en la guía 2024."
frase_permitida: "Tu hemoglobina, ajustada a la altura de {ciudad}, está por debajo del valor recomendado. Eso se llama anemia y tiene varias causas posibles; abajo te contamos qué muestran tus otros resultados."
frases_prohibidas: ["tienes leucemia", "tienes una enfermedad de la sangre"]
recomendaciones_sugeridas: ["depende de la causa (HE-002, HE-004, HE-A01)"]
```

**Casos de prueba** (residencia en Bogotá)

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | Hemoglobina 11,2; ajustada 9,4; no fuma | Activa, anemia moderada, coincidencia alta, escalamiento 2 |
| Positivo oculto por la altura | Mujer, hemoglobina 13,1; ajustada 11,3 | Activa como leve, escalamiento 1 (sin ajuste habría salido normal) |
| Negativo · PDF hombre 46 años | Hemoglobina 16,2; ajustada 14,4 | No activa |
| Severa | Hombre, hemoglobina 9,4; ajustada 7,6 | Activa, severa, escalamiento 3 |
| Embarazo | 2.º trimestre, hemoglobina 12,0; ajustada 10,2 | Activa (corte 10,5) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-002 · Anemia por déficit de hierro

**Qué detecta.** Anemia (HE-001) con ferritina menor de 15 ng/mL, o menor de 70 si hay inflamación. VCM bajo, RDW alto y saturación de transferrina baja la refuerzan. Siempre se busca la causa: en hombres y en mujeres posmenopáusicas, la pérdida de sangre digestiva es la que más preocupa.

```yaml
id: COND-M3-HE-002
nombre: Anemia por déficit de hierro
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: anemia
    condicion: "COND-M3-HE-001 activa"
  - id: ferritina_baja
    biomarcador: ferritin
    condicion: "< 15 si hs_crp <= 5 mg/L; < 70 si hs_crp > 5 mg/L"
    unidad: ng/mL
  - id: saturacion_baja
    biomarcador: transferrin_saturation
    condicion: "< 20"
    unidad: "%"
  - id: vcm_bajo
    biomarcador: mcv
    condicion: "< límite inferior"
  - id: rdw_alto
    biomarcador: rdw
    condicion: "> límite superior"
regla_central: "anemia AND ferritina_baja"
coincidencia:
  alta: "regla_central AND (saturacion_baja OR vcm_bajo OR rdw_alto)"
  moderada: "regla_central sin señales de apoyo"
  baja: "anemia AND saturacion_baja AND vcm_bajo AND ferritina entre el corte y 30 (vigilar)"
excluye_si: []
escalamiento: 2
dispara: ["reflejas IgA total y anti-transglutaminasa IgA si no hay causa evidente (menstruación abundante, embarazo, dieta)", "COND-M4 sangre oculta en heces se lee junto con este hallazgo"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["suplementos de hierro recientes (pueden subir la ferritina sin corregir el déficit)", "inflamación (manejada con el corte de 70)"]
contexto_causa: ["menstruación abundante", "embarazo", "dieta vegana o vegetariana", "cirugía bariátrica", "donación de sangre frecuente", "sangre oculta positiva (M4)", "H. pylori positivo (M4)", "celiaquía (refleja)"]
guias: ["OMS 2020, ferritina", "OMS 2024, cortes de hemoglobina"]
por_verificar: "La ficha de ferritina cita evidencia reciente con corte de 30 ng/mL; aquí se usa 15 (OMS) y la zona 15 a 30 queda como vigilar."
frase_permitida: "Tu hemoglobina está baja y tus reservas de hierro también. Es la causa más frecuente de anemia y tiene tratamiento, pero hay que encontrar por qué falta el hierro: conviene una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes anemia ferropénica", "toma hierro", "toma sulfato ferroso", "es por la menstruación (sin evaluación médica)"]
recomendaciones_sugeridas: ["consulta médica", "alimentos ricos en hierro con una fruta con vitamina C", "evitar té o café con las comidas principales"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | HE-001 activa; ferritina 7, hs-CRP 0,8, saturación 8,8 %, VCM 78,2, RDW 16,4 | Activa, coincidencia alta, escalamiento 2; IgA y anti-tTG reflejas (negativas: sin señal de celiaquía) |
| Con inflamación | Anemia, ferritina 45, hs-CRP 12, saturación 12 % | Activa (corte 70), coincidencia alta |
| Hombre | Hombre 55 años, anemia, ferritina 9 | Activa, escalamiento 2; la vista médica destaca descartar pérdida digestiva |
| Sin anemia | Hemoglobina ajustada normal, ferritina 9 | No activa (va a HE-003) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-003 · Déficit de hierro sin anemia

**Qué detecta.** Ferritina baja con hemoglobina ajustada normal. La OMS indica usar la ferritina para detectar el déficit en personas aparentemente sanas: es la etapa en que se puede corregir antes de que aparezca la anemia.

```yaml
id: COND-M3-HE-003
nombre: Déficit de hierro sin anemia
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: incluida
detectabilidad: D1
criterios:
  - id: ferritina_baja
    biomarcador: ferritin
    condicion: "< 15 si hs_crp <= 5; < 70 si hs_crp > 5"
    unidad: ng/mL
  - id: ferritina_limite
    biomarcador: ferritin
    condicion: "15-29 con hs_crp <= 5"
  - id: sin_anemia
    condicion: "COND-M3-HE-001 no activa"
regla_central: "ferritina_baja AND sin_anemia"
coincidencia:
  alta: "regla_central"
  baja: "ferritina_limite AND sin_anemia (vigilar)"
escalamiento:
  base: 1
  hombre_o_mujer_posmenopausica: 2
nivel_lenguaje: resultado_observado
contexto_objetivo: "objetivos de maratón, rendimiento y energía: se destaca en 'Qué puedes hacer'"
guias: ["OMS 2020, ferritina"]
por_verificar: "Escalamiento 2 en hombres y mujeres posmenopáusicas (para buscar pérdida digestiva) es propuesta de Saludly."
frase_permitida: "Tus reservas de hierro están bajas, aunque todavía no tienes anemia. Es un buen momento para corregirlo con la alimentación y revisar con tu médico por qué pasa."
frases_prohibidas: ["tienes deficiencia de hierro", "toma hierro"]
recomendaciones_sugeridas: ["alimentos ricos en hierro con vitamina C", "evitar té o café con las comidas", "consulta si es hombre o mujer posmenopáusica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Mujer 28 años, hemoglobina ajustada 12,6, ferritina 11 | Activa, escalamiento 1 |
| Hombre | Hombre 50 años, hemoglobina ajustada 13,8, ferritina 12 | Activa, escalamiento 2 |
| Vigilar | Mujer, ferritina 22, hs-CRP 1 | Coincidencia baja (vigilar) |
| Con anemia · PDF mujer 34 años | Ferritina 7 con anemia | No activa (manda HE-002) |
| Negativo · PDF hombre 46 años | Ferritina 310 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-004 · Anemia por déficit de B12 o folato

**Qué detecta.** Anemia (HE-001) con glóbulos rojos grandes (VCM alto) y B12 menor de 180 ng/L o folato menor de 4 ng/mL. Si la B12 está entre 180 y 350, decide el ácido metilmalónico.

```yaml
id: COND-M3-HE-004
nombre: Anemia por déficit de B12 o folato
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: anemia
    condicion: "COND-M3-HE-001 activa"
  - id: vcm_alto
    biomarcador: mcv
    condicion: "> límite superior"
  - id: b12_baja
    biomarcador: vitamin_b12
    condicion: "< 180, o 180-350 con ácido metilmalónico sobre el límite"
    unidad: ng/L (pg/mL)
  - id: folato_bajo
    biomarcador: folate
    condicion: "< 4"
    unidad: ng/mL
regla_central: "anemia AND vcm_alto AND (b12_baja OR folato_bajo)"
excluye_si: []
excluye_a: ["COND-M3-NU-001 y COND-M3-NU-002 en el informe del paciente (quedan en la vista médica)"]
coincidencia:
  alta: "regla_central"
  moderada: "anemia AND (b12_baja OR folato_bajo) con VCM normal (déficit combinado posible)"
modificado_por: ["COND-M3-NU-A01"]
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["suplementos de B12 o folato recientes", "alcohol (sube el VCM)", "hipotiroidismo (sube el VCM)", "metformina o inhibidores de bomba de protones (factor de riesgo, no confusor)"]
guias: ["NICE NG239 2024", "OMS, folato"]
frase_permitida: "Tu hemoglobina está baja, tus glóbulos rojos son más grandes de lo normal y tu {B12 o folato} está bajo. Ese patrón merece una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes anemia perniciosa", "toma B12", "inyéctate B12"]
recomendaciones_sugeridas: ["consulta médica", "alimentos de origen animal (B12) u hojas verdes y leguminosas (folato)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| B12 | Anemia, VCM 108, B12 140 | Activa, coincidencia alta, escalamiento 2 |
| Indeterminada | Anemia, VCM 104, B12 260, ácido metilmalónico alto | Activa |
| Folato | Anemia, VCM 103, folato 2,8 | Activa |
| Negativo · PDF mujer 34 años | Anemia con VCM 78,2; B12 262 con ácido metilmalónico normal | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-005 · Plaquetas bajas

**Qué detecta.** Plaquetas menores de 100 × 10³/µL, el corte del consenso internacional. Antes de escalar se descarta la pseudotrombocitopenia (agrupación de plaquetas en el tubo, que el laboratorio suele comentar) y se repite. Entre 100 y el límite inferior del laboratorio se muestra como valor fuera de rango.

```yaml
id: COND-M3-HE-005
nombre: Plaquetas bajas
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: plaquetas_bajas
    biomarcador: platelets
    condicion: "< 100"
    unidad: x10³/µL
  - id: plaquetas_leves
    biomarcador: platelets
    condicion: "100 a límite inferior del laboratorio"
regla_central: "plaquetas_bajas"
no_interpretable_si: ["comentario del laboratorio de agregados plaquetarios o coágulo en la muestra"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con infección reciente, alcohol o medicamentos que bajan plaquetas"
escalamiento:
  plaquetas_leves: 1
  plaquetas_bajas: 2
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
confusores: ["infección viral reciente", "alcohol", "heparina y otros medicamentos", "embarazo", "hígado (relación con FIB-4 en M4)"]
guias: ["Consenso internacional de PTI 2019"]
frase_permitida: "Tus plaquetas, las células que ayudan a coagular la sangre, están más bajas de lo esperado. Hay causas pasajeras; conviene repetir el examen y revisarlo con tu médico. Si tienes sangrados o moretones sin golpes, consulta antes."
frases_prohibidas: ["tienes púrpura", "tienes leucemia", "tienes una enfermedad autoinmune"]
recomendaciones_sugeridas: ["repetir hemograma", "evitar antiinflamatorios y aspirina sin indicación mientras se aclara"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Plaquetas 82 | Activa, escalamiento 2; repetir |
| Leve | Plaquetas 128 (laboratorio 150 a 450) | Valor fuera de rango, escalamiento 1 |
| Seudotrombocitopenia | Plaquetas 64 con comentario de agregados | No interpretable; repetir con citrato |
| Crítico | Plaquetas 14 con bandera crítica | Escalamiento 3 |
| Negativo · PDF ejemplos | Plaquetas 265 y 330 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-006 · Posible sobrecarga de hierro

**Qué detecta.** Saturación de transferrina mayor de 45 % con ferritina mayor de 200 ng/mL en mujeres premenopáusicas, o mayor de 50 % con ferritina mayor de 300 en hombres y mujeres posmenopáusicas (EASL 2022). Confirmar hemocromatosis exige una prueba genética. La ferritina alta sola es una alerta ("vigilar"), porque la inflamación, el alcohol y el hígado graso también la suben.

```yaml
id: COND-M3-HE-006
nombre: Posible sobrecarga de hierro
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: patron_mujer
    condicion: "mujer premenopáusica AND transferrin_saturation > 45 AND ferritin > 200"
  - id: patron_hombre
    condicion: "(hombre OR mujer posmenopáusica) AND transferrin_saturation > 50 AND ferritin > 300"
  - id: ferritina_sola
    condicion: "ferritin > 200 (mujer premenopáusica) o > 300 (resto) con saturación normal"
regla_central: "patron_mujer OR patron_hombre"
contexto_obligatorio: ["ayuno (el hierro sérico varía con la comida)"]
coincidencia:
  alta: "regla_central sin inflamación (hs_crp <= 5) y sin suplementos de hierro"
  moderada: "regla_central con hs_crp > 5, alcohol o patrón hepático metabólico"
  baja: "ferritina_sola (vigilar)"
escalamiento: 2
nivel_lenguaje: patron_compatible
confusores: ["inflamación", "alcohol", "hígado graso (relación hepática del documento 03)", "suplementos de hierro", "transfusiones"]
guias: ["EASL 2022, hemocromatosis", "OMS 2020, ferritina"]
frase_permitida: "Tu hierro y tus reservas de hierro están más altos de lo esperado. Puede deberse a varias causas; conviene revisarlo con tu médico, que puede pedir una prueba genética."
frase_vigilar: "Tu ferritina está alta. Muchas veces se debe a inflamación o al hígado más que a exceso de hierro; lo tenemos en cuenta junto con tus otros resultados."
frases_prohibidas: ["tienes hemocromatosis", "tienes exceso de hierro", "dona sangre"]
recomendaciones_sugeridas: ["no tomar suplementos de hierro ni vitamina C en dosis altas", "reducir alcohol", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Hombre, saturación 62 %, ferritina 640, hs-CRP 1 | Activa, coincidencia alta, escalamiento 2 |
| Vigilar · PDF hombre 46 años | Ferritina 310, saturación 37 %, patrón hepático metabólico | Coincidencia baja (vigilar); la vista médica liga la ferritina al patrón hepático |
| Mujer | Mujer 32 años, saturación 51 %, ferritina 260 | Activa |
| Negativo · PDF mujer 34 años | Ferritina 7 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-A01 · Anemia con perfil inflamatorio (apoyo)

**Qué detecta.** Anemia con ferritina normal o alta, saturación de transferrina baja y hs-CRP alta. Orienta a una enfermedad de fondo, no a falta de hierro. Cuando se cumple, cambia el texto de HE-001: la recomendación es buscar la causa, no comer más hierro.

```yaml
id: COND-M3-HE-A01
nombre: Anemia con perfil inflamatorio
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D3
criterios:
  - id: anemia
    condicion: "COND-M3-HE-001 activa"
  - id: ferritina_no_baja
    condicion: "ferritin >= 70 con hs_crp > 5"
  - id: saturacion_baja
    condicion: "transferrin_saturation < 20"
  - id: inflamacion
    condicion: "hs_crp > 5"
regla_central: "anemia AND ferritina_no_baja AND saturacion_baja AND inflamacion"
modifica: ["COND-M3-HE-001"]
efecto: "HE-001 sube a escalamiento 2 y su texto cambia a 'buscar causa de fondo'; no se activan recomendaciones de hierro."
guias: ["OMS 2020, ferritina"]
frase_permitida: "Tu anemia no parece deberse a falta de hierro sino a una inflamación de fondo. Por eso es importante revisarla con tu médico."
frases_prohibidas: ["tienes una enfermedad crónica", "tienes cáncer"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Anemia, ferritina 180, saturación 14 %, hs-CRP 22 | Activa; HE-001 con escalamiento 2 y sin recomendaciones de hierro |
| Negativo · PDF mujer 34 años | Anemia, ferritina 7, hs-CRP 0,8 | No activa (manda HE-002) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-A02 · Leucocitos, neutrófilos o linfocitos fuera de rango (apoyo)

**Qué detecta.** Recuentos de glóbulos blancos fuera del intervalo del laboratorio. No hay umbral de guía para tamizaje, así que se muestran como valores fuera de rango, se repiten y solo escalan por bandera crítica del laboratorio.

```yaml
id: COND-M3-HE-A02
nombre: Leucocitos, neutrófilos o linfocitos fuera de rango
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: fuera_de_rango
    biomarcadores: [wbc, neutrophils_abs, lymphocytes_abs]
    condicion: "fuera del intervalo del laboratorio"
regla_central: "fuera_de_rango"
escalamiento:
  base: 1
  bandera_critica_laboratorio: 3
  mas_de_una_linea_alterada_con_anemia_o_plaquetas_bajas: 2
efecto: "Valor fuera de rango con sugerencia de repetir; si hay alteración de dos o más líneas (glóbulos rojos, blancos, plaquetas), la vista médica lo destaca."
confusores: ["infección reciente", "corticoides (suben neutrófilos, bajan linfocitos)", "ejercicio intenso", "tabaquismo"]
guias: ["Intervalo del laboratorio"]
por_verificar: "Escalamiento 2 para alteración de varias líneas es propuesta de Saludly."
frase_permitida: "Tus {glóbulos blancos o tipo de célula} están {por encima o por debajo} del rango. Es frecuente tras una infección; conviene repetirlo."
frases_prohibidas: ["tienes leucemia", "tienes las defensas bajas", "tienes una infección"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Leve | Neutrófilos 1,6 (laboratorio desde 1,8) | Valor fuera de rango, escalamiento 1 |
| Varias líneas | Leucocitos 2,9, plaquetas 95, anemia | Escalamiento 2 |
| Negativo · PDF ejemplos | Leucocitos 7,8 y 6,1 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-HE-A03 · Eosinofilia (apoyo)

**Qué detecta.** Eosinófilos absolutos de 500 por µL o más (leucocitos × porcentaje de eosinófilos). Se cruza con el coprológico del módulo M4: si hay parásitos, refuerza la parasitosis; si no, se muestra como valor fuera de rango.

```yaml
id: COND-M3-HE-A03
nombre: Eosinofilia
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D1
calculo: "eosinofilos_abs = wbc x eosinophils_pct / 100"
criterios:
  - id: eosinofilia
    condicion: "eosinofilos_abs >= 0,5"
    unidad: x10³/µL
regla_central: "eosinofilia"
modifica: ["parasitosis intestinal (módulo M4)"]
escalamiento:
  base: 1
  si_eosinofilos_abs_mayor_1_5: 2
confusores: ["alergias y asma", "medicamentos"]
guias: ["Intervalo del laboratorio"]
por_verificar: "Corte de 500/µL y escalamiento 2 desde 1.500/µL son definiciones habituales, no de una guía citada en los lotes."
frase_permitida: "Un tipo de glóbulo blanco relacionado con alergias y parásitos (eosinófilos) está alto. Lo cruzamos con tu examen de heces."
frases_prohibidas: ["tienes parásitos", "tienes una alergia"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Leucocitos 8,0, eosinófilos 9 % (0,72) | Activa, escalamiento 1 |
| Con parásitos | Lo anterior y coprológico con parásitos | Refuerza parasitosis (M4) |
| Negativo · PDF hombre 46 años | Leucocitos 7,8, eosinófilos 3,2 % (0,25) | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-NU-001 · Déficit de vitamina B12

**Qué detecta.** B12 total menor de 180 ng/L, o entre 180 y 350 con ácido metilmalónico alto. La ausencia de anemia no lo descarta: el déficit de B12 puede afectar los nervios antes que la sangre. Los anticonceptivos orales bajan la B12 total sin déficit real.

```yaml
id: COND-M3-NU-001
nombre: Déficit de vitamina B12
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: incluida
detectabilidad: D2
criterios:
  - id: b12_baja
    biomarcador: vitamin_b12
    condicion: "< 180"
    unidad: ng/L (pg/mL)
  - id: b12_indeterminada
    biomarcador: vitamin_b12
    condicion: "180-350"
  - id: mma_alto
    biomarcador: methylmalonic_acid
    condicion: "> límite superior del laboratorio"
  - id: factor_riesgo
    contexto: cuestionario
    condicion: "metformina OR inhibidor de bomba de protones OR anti-H2 OR dieta vegana OR cirugía bariátrica o gástrica OR enfermedad autoinmune"
regla_central: "b12_baja OR (b12_indeterminada AND mma_alto)"
excluye_si: ["COND-M3-HE-004 activa por B12"]
coincidencia:
  alta: "regla_central AND (factor_riesgo OR mma_alto)"
  moderada: "b12_baja sin factor de riesgo, o con anticonceptivo oral"
  baja: "b12_indeterminada sin ácido metilmalónico disponible (vigilar)"
modificado_por: ["COND-M3-NU-A01"]
escalamiento:
  base: 1
  con_sintomas_neurologicos: 2
nivel_lenguaje: riesgo_potencial
confusores: ["suplementos de B12 recientes", "anticonceptivos orales", "embarazo"]
guias: ["NICE NG239 2024"]
frase_permitida: "Tu vitamina B12 está baja. Es importante para los nervios y la sangre; conviene revisarlo con tu médico, sobre todo si tomas metformina o medicamentos para la acidez, o si no comes productos de origen animal."
frases_prohibidas: ["tienes anemia perniciosa", "inyéctate B12", "toma 1.000 µg de B12"]
recomendaciones_sugeridas: ["alimentos de origen animal (huevo, lácteos, carnes, pescado)", "en dieta vegana, hablar con el médico sobre suplementar", "consulta si hay hormigueo o adormecimiento"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | B12 150, toma metformina | Activa, coincidencia alta, escalamiento 1 |
| Funcional | B12 240, ácido metilmalónico alto | Activa, coincidencia alta |
| Negativo · PDF mujer 34 años | B12 262, ácido metilmalónico 0,28 (normal) | No activa |
| Negativo · PDF hombre 46 años | B12 410 | No activa |
| Anticonceptivo | B12 165, anticonceptivo oral, sin factor de riesgo | Activa, coincidencia moderada |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-NU-002 · Déficit de folato

**Qué detecta.** Folato sérico menor de 4 ng/mL (posible déficit) o menor de 3 ng/mL (déficit con impacto en la sangre). Los cortes dependen del método del laboratorio, y una sola comida rica en folato puede normalizar el valor sérico.

```yaml
id: COND-M3-NU-002
nombre: Déficit de folato
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: incluida
detectabilidad: D1
criterios:
  - id: folato_posible
    biomarcador: folate
    condicion: "3-3,9"
    unidad: ng/mL
  - id: folato_bajo
    biomarcador: folate
    condicion: "< 3"
    unidad: ng/mL
regla_central: "folato_posible OR folato_bajo"
contexto_obligatorio: ["ayuno >= 8 horas"]
excluye_si: ["COND-M3-HE-004 activa por folato"]
coincidencia:
  alta: "folato_bajo"
  moderada: "folato_posible"
modificado_por: ["COND-M3-NU-A01"]
escalamiento:
  base: 1
  embarazo: 2
nivel_lenguaje: riesgo_potencial
confusores: ["alcohol", "metotrexato y otros medicamentos", "comida reciente (sube el valor)"]
guias: ["OMS, folato"]
por_verificar: "El laboratorio debe declarar el método; los cortes cambian con él."
frase_permitida: "Tu folato está bajo. Es importante para la sangre y, en mujeres que pueden quedar embarazadas, para el desarrollo del bebé. Conviene mejorarlo con la alimentación y comentarlo con tu médico."
frases_prohibidas: ["toma ácido fólico", "tu bebé tendrá problemas"]
recomendaciones_sugeridas: ["hojas verdes, leguminosas y frutas cítricas", "reducir alcohol", "si busca embarazo, hablar con el médico sobre ácido fólico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Folato 2,6 | Activa, coincidencia alta, escalamiento 1 |
| Posible | Folato 3,6 | Activa, coincidencia moderada |
| Embarazo | Folato 3,2, embarazo de 8 semanas | Activa, escalamiento 2 |
| Negativo · PDF ejemplos | Folato 9,8 y 6,2 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-NU-A01 · Homocisteína alta (apoyo)

**Qué detecta.** Homocisteína por encima del intervalo del laboratorio como marcador funcional de déficit de B12 o folato. No se usa como riesgo cardiovascular aislado (descartado en el Lote 1). La función renal baja y el hipotiroidismo también la suben.

```yaml
id: COND-M3-NU-A01
nombre: Homocisteína alta
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D1
criterios:
  - id: hcy_alta
    biomarcador: homocysteine
    condicion: "> límite superior del laboratorio"
regla_central: "hcy_alta"
contexto_obligatorio: ["ayuno >= 8 horas", "muestra refrigerada y procesada en 4 a 6 horas"]
modifica: ["COND-M3-NU-001", "COND-M3-NU-002", "COND-M3-HE-004"]
efecto: "Sube la coincidencia de déficit de B12 o folato. Sin esos déficits, se muestra como vigilar y la vista médica sugiere revisar TFG y TSH."
confusores: ["TFG < 60", "hipotiroidismo", "suplementos de B12, folato o B6 recientes (la normalizan)"]
relacion_vigilar: "TSH alta + colesterol + CK + homocisteína (documento 03)"
guias: ["NICE NG239 2024"]
frase_permitida_medico: "Homocisteína {valor} µmol/L: apoyo funcional a déficit de B12 o folato; descartar TFG baja e hipotiroidismo."
frases_prohibidas: ["riesgo de infarto por homocisteína"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza | B12 220, homocisteína 19 | NU-001 sube a coincidencia alta |
| Vigilar | Homocisteína 17, B12 y folato normales, TFG 58 | Vigilar; vista médica menciona TFG |
| Negativo · PDF ejemplos | Homocisteína 11,8 y 13,9 | No activa |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-NU-A02 · PTH alta con calcio normal (apoyo)

**Qué detecta.** PTH alta con calcio corregido normal. Antes de pensar en hiperparatiroidismo normocalcémico se descartan causas secundarias: vitamina D baja y TFG baja. Con la regla refleja actual (PTH solo cuando el calcio corregido sale alto), esta ficha solo se activa si el médico pide PTH o si el panel cambia.

```yaml
id: COND-M3-NU-A02
nombre: PTH alta con calcio normal
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D3
criterios:
  - id: pth_alta
    biomarcador: pth
    condicion: "> límite superior del laboratorio"
  - id: calcio_normal
    condicion: "calcio corregido dentro del intervalo"
  - id: secundaria
    condicion: "vitamin_d < 20 ng/mL OR egfr < 60 OR tiazidas OR litio"
regla_central: "pth_alta AND calcio_normal"
efecto: "Si secundaria: vigilar, con la causa probable en la vista médica. Si no: resultado observado para el médico (posible hiperparatiroidismo normocalcémico), escalamiento 1."
escalamiento: 1
relacion: "vitamina D baja + PTH alta + calcio o fósforo alterados (patrón, documento 03)"
guias: ["Quinto Taller Internacional de hiperparatiroidismo primario 2022"]
por_verificar: "Corte de vitamina D de 20 ng/mL para considerar causa secundaria."
frase_permitida_medico: "PTH alta con calcio corregido normal; {causa secundaria probable | sin causa secundaria evidente}."
frases_prohibidas: ["tienes hiperparatiroidismo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Secundaria | PTH 88, calcio corregido 9,4, vitamina D 14 | Vigilar; causa probable: vitamina D baja |
| Sin causa | PTH 82, calcio 9,8, vitamina D 34, TFG 95 | Resultado observado para el médico, escalamiento 1 |
| No aplica · PDF ejemplos | PTH no medida (calcio normal) | No aplica |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-NU-A03 · Vitamina D baja (apoyo)

**Qué detecta.** 25-OH vitamina D por debajo del intervalo del laboratorio. Por la regla de vitaminas aprobada, se marca como baja y genera recomendaciones alimentarias y de sol, sin dosis. No se etiqueta como deficiencia, porque la Endocrine Society 2024 no fija un nivel de suficiencia ni respalda medirla de rutina; el texto de la recomendación lo aprueba el médico.

```yaml
id: COND-M3-NU-A03
nombre: Vitamina D baja
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D1
criterios:
  - id: vitd_baja
    biomarcador: vitamin_d
    condicion: "< límite inferior del laboratorio"
  - id: vitd_alta
    biomarcador: vitamin_d
    condicion: "> límite superior del laboratorio"
regla_central: "vitd_baja"
escalamiento:
  vitd_baja: 0
  vitd_alta: 1
efecto: "Recomendación alimentaria y de sol. Participa en relaciones: con PTH alta y calcio o fósforo alterados (patrón); con hs-CRP alta o con ferritina o hemoglobina bajas (vigilar)."
modulo_reglas: "regla de vitaminas, documento 07"
guias: ["Endocrine Society 2024"]
por_verificar: "Texto de recomendación sujeto a aprobación médica; ¿mencionar suplemento general o solo alimentos y sol?"
frase_permitida: "Tu vitamina D está por debajo del rango del laboratorio. Puedes mejorarla con alimentos como pescados grasos, huevo y lácteos fortificados, y con exposición prudente al sol. Si quieres suplementarla, consúltalo con tu médico."
frase_alta: "Tu vitamina D está por encima del rango. Si tomas suplementos, coméntalo con tu médico."
frases_prohibidas: ["tienes deficiencia de vitamina D", "toma 2.000 UI", "toma vitamina D3"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Baja · PDF hombre 46 años | Vitamina D 21,4 (laboratorio 30 a 100) | Marcada baja, escalamiento 0, recomendación alimentaria |
| Baja · PDF mujer 34 años | Vitamina D 17,8 | Marcada baja; relación vigilar con ferritina y hemoglobina bajas |
| Alta | Vitamina D 140 | Marcada alta, escalamiento 1 |
| En rango | Vitamina D 42 | Sin recomendación específica |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## COND-M3-NU-A04 · Vitaminas informativas (apoyo)

**Qué detecta.** Aplica la regla de vitaminas a las 11 vitaminas sin guía de tamizaje: B1, B6, A, E, K1, C, biotina, niacina, índice omega-3, relación omega-6/omega-3 y CoQ10. Cada una se clasifica con el intervalo del laboratorio; sin intervalo ("No establecido"), solo se muestra el valor. Tiene tres reglas de seguridad propias: biotina alta, vitaminas A y E altas, y tiamina baja con síntomas neurológicos.

```yaml
id: COND-M3-NU-A04
nombre: Vitaminas informativas
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D1
biomarcadores: [vitamin_b1, vitamin_b6, vitamin_a, vitamin_e, vitamin_k1, vitamin_c, biotin, niacin, omega3_index, omega6_omega3_ratio, coq10]
clasificacion: "intervalo del laboratorio: bajo, limítrofe (si la ficha lo define), en rango, alto; sin intervalo, solo valor"
reglas:
  bajo: "recomendación de alimentos que la aportan; suplemento solo como opción general para hablar con el médico, sin dosis"
  alto: "preguntar por suplementos"
  vitamina_a_o_e_alta: "sugerir consulta (se acumulan); escalamiento 1"
  biotina_alta: "bloquear TSH, T4 libre, T3 libre, anticuerpos tiroideos, B12 y folato hasta repetir sin el suplemento; escalamiento 1"
  vitamina_c: "solo se clasifica con transporte congelado validado; si no, no interpretable"
  tiamina_baja_con_sintomas: "tiamina baja con confusión, alteraciones de la vista o de la marcha y factor de riesgo (alcohol, cirugía bariátrica, desnutrición): escalamiento 3, sospecha de urgencia"
  tiamina_baja_sin_sintomas: "recomendación alimentaria; con alcohol o cirugía bariátrica, escalamiento 1"
escalamiento_base: 0
guias: ["Regla de vitaminas (documento 07)", "FDA, interferencia de biotina en inmunoensayos", "ficha vitamin_b1 (Wernicke)"]
por_verificar: "El laboratorio debe dar intervalo para biotina; sin él la regla de biotina alta solo funciona con el suplemento declarado en el cuestionario."
frase_permitida_baja: "Tu {vitamina} está por debajo del rango. Te contamos qué alimentos la aportan; si quieres suplementarla, consúltalo con tu médico."
frase_permitida_sin_intervalo: "Este es tu valor de {vitamina}. El laboratorio no tiene un rango de referencia establecido, así que lo mostramos solo como información."
frases_prohibidas: ["tienes deficiencia de", "toma {dosis}", "compra este suplemento"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Sin intervalo · PDF ejemplos | Biotina, niacina, índice omega-3, omega-6/omega-3 y CoQ10 con "No establecido" | Solo valor, sin clase |
| No apta · PDF mujer 34 años | Vitamina C "Muestra no apta" | No interpretable |
| En rango · PDF hombre 46 años | B1, B6, A, E, K1, C en rango | Sin recomendación específica |
| Biotina declarada | Suplemento de biotina para el cabello, TSH 0,08 | Bloquea tiroides y B12; pide repetir sin el suplemento |
| Vitamina A alta | Vitamina A 112 (30 a 80) | Marcada alta, escalamiento 1 |
| Tiamina con síntomas | B1 45, alcohol diario, confusión reciente | Escalamiento 3 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Resultado esperado del módulo M3 en los PDF de ejemplo

Ambos casos suponen residencia en Bogotá.

| PDF | Activa | No activa | Vigilar o no interpretable |
| --- | --- | --- | --- |
| Hombre 46 años (LCD-2026-100123) | Vitamina D baja (escalamiento 0, recomendación alimentaria) | Anemia (hemoglobina ajustada 14,4), déficit de hierro, B12, folato, plaquetas, leucocitos, eosinofilia | Ferritina 310 como vigilar (sobrecarga de hierro con coincidencia baja, ligada al patrón hepático); vitaminas sin intervalo solo con su valor |
| Mujer 34 años (LCD-2026-100124) | Anemia moderada ajustada por altitud (hemoglobina ajustada 9,4) y anemia por déficit de hierro (coincidencia alta, escalamiento 2); vitamina D baja | Déficit de B12 (ácido metilmalónico normal), folato, plaquetas, sobrecarga de hierro, perfil inflamatorio | Vitamina C no interpretable; relación vigilar entre vitamina D baja y ferritina o hemoglobina bajas; sin señal de celiaquía en las reflejas |

## Lo que el médico debe mirar con más cuidado

1. Valores del ajuste de hemoglobina por tabaquismo, que deben copiarse de la tabla OMS 2024.
2. Corte de ferritina: 15 ng/mL (OMS, adoptado) frente a 30 de la evidencia reciente que cita la ficha; la zona 15 a 30 queda como vigilar.
3. Escalamiento 2 para déficit de hierro sin anemia en hombres y mujeres posmenopáusicas.
4. Escalamiento 2 para alteración de varias líneas del hemograma y los cortes de eosinofilia.
5. Corte de vitamina D de 20 ng/mL para considerar causa secundaria de PTH alta.
6. Texto de la recomendación de vitamina D baja: solo alimentos y sol, o mencionar también el suplemento.
7. Escalamiento 3 para tiamina baja con síntomas neurológicos.