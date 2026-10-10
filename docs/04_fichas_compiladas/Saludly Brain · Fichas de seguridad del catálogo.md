# Fichas de seguridad del catálogo — biomarcadores "solo valor y rango"

**Saludly Brain · Knowledge Base · versión 1 · 6 de octubre de 2026**

Este documento cubre los biomarcadores del catálogo que no alimentan ninguna condición de los seis módulos. El paciente los ve con su valor, su intervalo y su clase, pero varios tienen valores peligrosos o condiciones de toma que, si se ignoran, producen alarmas falsas o tranquilidad falsa. Son 15 fichas: una regla general y 14 fichas por grupo de biomarcadores. Cada ficha trae su regla, sus casos de prueba y un espacio para la firma del médico.

Las reglas salen de la sección de seguridad de cada ficha de biomarcador del Knowledge Base. Donde la ficha no da un número, el corte es propuesta de Saludly y está marcado en `por_verificar`.

## Dos conceptos nuevos

- **Revisión médica obligatoria.** El médico ve el valor en su vista, aunque esté en rango, y puede subir el escalamiento. No le dice nada distinto al paciente. Aplica a los biomarcadores cuya ficha dice "escalar siempre" (cortisol, ACTH, osmolalidad, eritroblastos e IGF-1). Esas fichas fueron escritas para cuando un médico pide la prueba; como Saludly ahora las mide a todos, "escalar siempre" se traduce en que un médico las mira siempre, no en alarmar al paciente.
- **Escalamiento al paciente.** Es el nivel de 0 a 3 de siempre y solo sube cuando el valor o el patrón lo justifican.

## Cómo firmar

Leer cada ficha con sus casos, marcar aprobada, aprobada con cambios o rechazada, escribir los cambios y poner nombre, registro ReTHUS y fecha.

## Índice

| ID | Grupo | Biomarcadores | Revisión médica obligatoria |
| --- | --- | --- | --- |
| SEG-000 | Regla general | Todos los "solo valor y rango" | No |
| SEG-001 | Troponina de alta sensibilidad | Troponina hs | Sí |
| SEG-002 | Cortisol y ACTH | Cortisol, ACTH | Sí |
| SEG-003 | IGF-1 | IGF-1 | Sí |
| SEG-004 | Osmolalidad | Osmolalidad sérica, brecha osmolar | Sí |
| SEG-005 | Eritroblastos circulantes | NRBC | Sí |
| SEG-006 | Coagulación | Tiempo de protrombina, INR, fibrinógeno | No |
| SEG-007 | Músculo y tejidos | CK, LDH | No |
| SEG-008 | Electrolitos sin condición | Magnesio, cloro, fósforo | No |
| SEG-009 | Proteínas e inmunoglobulinas | Proteínas totales, globulinas, relación A/G, IgG, IgM | No |
| SEG-010 | Metabolismo sin condición | Péptido C, fructosamina, NT-proBNP fuera de diabetes | No |
| SEG-011 | Hormonas sin condición | DHEA-S, estradiol, LH, progesterona | No |
| SEG-012 | Hemograma sin condición | Monocitos, basófilos, VPM, HCM, CHCM, hematocrito, eritrocitos | No |
| SEG-013 | Orina y heces sin condición | Proteína, glucosa, cetonas, bilirrubina y urobilinógeno en orina; moco y sangre macroscópica en heces | No |
| SEG-014 | Contexto cardiovascular y nutricional | ApoA1, relación ApoB/ApoA1, colesterol remanente, relación colesterol/HDL, transferrina, zinc, BUN, relación BUN/creatinina | No |

---

## SEG-000 · Regla general para "solo valor y rango"

**Qué hace.** Define el comportamiento por defecto de cualquier biomarcador sin condición propia. Las fichas SEG-001 a SEG-014 solo describen lo que cambia frente a esta regla.

```yaml
id: SEG-000
nombre: Regla general para solo valor y rango
aplica_a: "todo biomarcador del catálogo que no alimenta una condición, relación o regla de vitaminas"
clasificacion: "no interpretable, crítico, bajo, limítrofe (solo si la ficha lo define), en rango, alto; sin intervalo, solo valor"
escalamiento:
  en_rango: 0
  fuera_de_rango: 1
  bandera_critica_laboratorio: 3
  muestra_invalida: "no interpretable; pedir nueva muestra si el biomarcador tiene regla de seguridad"
texto_paciente:
  en_rango: "Está dentro del rango de referencia."
  fuera_de_rango: "Está {por encima | por debajo} del rango de referencia. Por sí solo no indica una enfermedad; coméntalo con tu médico en tu próximo control."
reglas_seguridad: ["nunca nombrar una enfermedad a partir de un valor aislado", "nunca recomendar medicamentos ni suplementos con dosis", "si la ficha del biomarcador tiene una regla de seguridad, esa regla manda sobre esta"]
frases_prohibidas: ["esto indica que tienes", "es grave", "no es nada"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| En rango | Cloro 103 (98 a 107) | Escalamiento 0 |
| Fuera de rango | Cloro 110 | Escalamiento 1, texto general |
| Crítico | Cualquier valor con bandera crítica | Escalamiento 3 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-001 · Troponina de alta sensibilidad

**Qué hace.** La ficha de troponina dice que cualquier valor elevado activa evaluación profesional, siempre, y que con síntomas se deriva a urgencias sin esperar a la IA. La troponina no detecta riesgo futuro: es un marcador de lesión del corazón.

```yaml
id: SEG-001
nombre: Troponina de alta sensibilidad
biomarcador: hs_troponin
revision_medica_obligatoria: true
criterios:
  - id: elevada
    condicion: "> percentil 99 declarado por el laboratorio para el método (y por sexo si lo declara)"
  - id: menor_que_limite
    condicion: "resultado con operador '<' (no detectable)"
escalamiento:
  elevada: 3
  menor_que_limite: 0
  en_rango: 0
canal_si_elevada: "llamada del equipo médico el mismo día; el informe no se publica antes de la llamada; nunca por WhatsApp"
texto_si_elevada: "Uno de tus resultados relacionados con el corazón requiere revisión médica hoy. Nuestro equipo te va a llamar. Si tienes dolor o presión en el pecho, falta de aire o sudor frío, ve a urgencias ahora."
confusores_para_el_medico: ["enfermedad renal crónica", "ejercicio extremo reciente", "miocarditis o infección reciente"]
frases_prohibidas: ["tienes un infarto", "tuviste un infarto", "tu corazón está dañado"]
guias: ["Ficha hs_troponin del Knowledge Base (Cuarta definición universal de infarto)"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| No detectable · PDF ejemplos | Troponina "\< 3" ng/L (percentil 99: 14) | En rango, escalamiento 0; revisión médica |
| Elevada | Troponina 31 ng/L | Escalamiento 3, llamada el mismo día |
| Límite | Troponina 14 ng/L (igual al percentil 99) | En rango; revisión médica |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-002 · Cortisol y ACTH

**Qué hace.** Aplica las reglas decididas en el documento 03 (sección 03.8). El cortisol solo se interpreta con toma entre 6:00 y 10:00 (la ficha admite hasta 10:30). La ACTH se interpreta solo junto con el cortisol de la misma muestra y solo en la vista del médico; además exige refrigeración inmediata. Ninguno forma patrones ni permite nombrar Cushing o Addison.

```yaml
id: SEG-002
nombre: Cortisol y ACTH
biomarcadores: [cortisol, acth]
revision_medica_obligatoria: true
cortisol:
  interpretable_si: "hora de toma entre 6:00 y 10:00"
  no_interpretable_si: ["toma fuera de ese horario", "corticoides orales, inhalados en dosis altas o tópicos extensos", "anticonceptivo con estrógenos (sube la proteína transportadora)", "embarazo"]
  escalamiento:
    en_rango: 0
    alto: 1
    bajo_en_la_manana: 2
    bandera_critica_laboratorio: 3
acth:
  interpretable_si: ["cortisol de la misma muestra disponible", "registro de refrigeración inmediata de la muestra"]
  paciente_ve: "valor y clase, sin texto interpretativo"
  escalamiento:
    en_rango: 0
    fuera_de_rango: 1
texto_cortisol_alto: "Tu cortisol, la hormona del estrés, salió por encima del rango. El estrés de la toma lo sube con frecuencia; tu médico revisará el resultado."
texto_cortisol_bajo: "Tu cortisol de la mañana salió más bajo de lo esperado. Conviene una consulta médica en las próximas semanas para revisarlo. Si tienes mucho cansancio, mareo al ponerte de pie o pérdida de peso, consulta antes."
frases_prohibidas: ["tienes Cushing", "tienes Addison", "tienes insuficiencia suprarrenal", "tu estrés está alto"]
guias: ["Fichas cortisol y acth del Knowledge Base"]
por_verificar: "Escalamiento 2 para cortisol bajo en la mañana es propuesta de Saludly; la ficha pide evaluación endocrinológica pero no fija un corte."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| En rango · PDF hombre 46 años | Cortisol 14,2 a las 7:15; ACTH 24 | Escalamiento 0; revisión médica |
| En rango · PDF mujer 34 años | Cortisol 11,6 a las 7:40; ACTH 18 | Escalamiento 0; revisión médica |
| Fuera de horario | Cortisol 9,0 a las 11:20 | No interpretable |
| Bajo | Cortisol 4,1 a las 7:30 | Escalamiento 2 |
| ACTH sin cadena de frío | ACTH sin registro de refrigeración | No interpretable |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-003 · IGF-1

**Qué hace.** La IGF-1 depende mucho de la edad y su ficha está en estado PARCIAL: falta la tabla completa de intervalos por edad para adultos. Solo se clasifica si el laboratorio reporta el intervalo para la edad de la persona. La biotina interfiere con el ensayo.

```yaml
id: SEG-003
nombre: IGF-1
biomarcador: igf1
revision_medica_obligatoria: true
interpretable_si: ["el laboratorio reporta intervalo por edad", "sin biotina declarada en las 72 horas previas"]
escalamiento:
  en_rango: 0
  fuera_de_rango: 1
texto_fuera_de_rango: "Tu IGF-1, una hormona relacionada con el crecimiento, está fuera del rango para tu edad. Tu médico revisará el resultado."
frases_prohibidas: ["tienes acromegalia", "tienes déficit de hormona de crecimiento"]
guias: ["Ficha igf1 del Knowledge Base"]
por_verificar: "Completar la ficha (tabla por edad del método del laboratorio aliado)."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| En rango · PDF hombre 46 años | IGF-1 168 (83 a 233 para 45 a 49 años) | Escalamiento 0 |
| Sin intervalo por edad | IGF-1 210 sin intervalo | Solo valor |
| Con biotina | IGF-1 400, biotina declarada | No interpretable |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-004 · Osmolalidad

**Qué hace.** En una persona sana y en ayunas, la osmolalidad casi siempre refleja el sodio, la glucosa y el BUN. La señal de alarma es la brecha osmolar: la diferencia entre la osmolalidad medida y la calculada. Si la osmolalidad está alterada con brecha normal, se lee junto con el sodio (M2 NE-005).

```yaml
id: SEG-004
nombre: Osmolalidad
biomarcador: osmolality
revision_medica_obligatoria: true
calculo:
  osmolalidad_calculada: "2 x sodio (mmol/L) + glucosa (mg/dL) / 18 + BUN (mg/dL) / 2,8"
  brecha_osmolar: "osmolalidad medida - osmolalidad calculada"
criterios:
  - id: brecha_alta
    condicion: "brecha_osmolar > 10"
    unidad: mOsm/kg
escalamiento:
  en_rango_y_brecha_normal: 0
  fuera_de_rango_brecha_normal: "sigue la regla del sodio (M2 NE-005)"
  brecha_alta: 2
  bandera_critica_laboratorio: 3
canal_si_brecha_alta: "llamada del médico; preguntar por alcohol y otras sustancias"
texto_brecha_alta: "Uno de tus resultados de la sangre necesita revisión médica. Nuestro equipo te va a llamar."
frases_prohibidas: ["estás intoxicado", "tomaste alcohol"]
guias: ["Ficha osmolality del Knowledge Base"]
por_verificar: "Escalamiento 2 para brecha mayor de 10 es propuesta; la ficha la trata como urgencia en sospecha de intoxicación, que no es el contexto de una toma preventiva en ayunas."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF hombre 46 años | Medida 292; calculada 291,6 (sodio 140, glucosa 112, BUN 15); brecha 0,4 | Escalamiento 0 |
| Normal · PDF mujer 34 años | Medida 286; calculada 284,3; brecha 1,7 | Escalamiento 0 |
| Brecha alta | Medida 312; calculada 290; brecha 22 | Escalamiento 2, llamada |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-005 · Eritroblastos circulantes (NRBC)

**Qué hace.** En un adulto sano no debería haber eritroblastos en sangre. La ficha pide evaluación siempre, salvo esplenectomía conocida, porque pueden indicar estrés grave de la médula ósea. Antes de escalar se descarta un error del contador automático.

```yaml
id: SEG-005
nombre: Eritroblastos circulantes
biomarcador: nrbc
revision_medica_obligatoria: true
criterios:
  - id: nrbc_positivo
    condicion: "> 0 por 100 leucocitos"
regla_central: "nrbc_positivo AND NOT esplenectomía declarada"
escalamiento:
  nrbc_0: 0
  nrbc_positivo: 2
  con_anemia_severa_o_plaquetas_bajas: 3
canal_si_positivo: "llamada del médico; se sugiere frotis de sangre periférica"
texto_positivo: "En tu hemograma aparecieron unas células que normalmente no están en la sangre. Hay que confirmarlo con otra prueba; nuestro médico te va a llamar."
frases_prohibidas: ["tienes leucemia", "tienes cáncer de la sangre", "tu médula está fallando"]
guias: ["Ficha nrbc del Knowledge Base"]
por_verificar: "La ficha pide derivación inmediata; aquí se propone escalamiento 2 con llamada y 3 solo con anemia severa o plaquetas bajas."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | NRBC 0,0 | Escalamiento 0 |
| Positivo | NRBC 1,5 | Escalamiento 2, llamada |
| Grave | NRBC 3, hemoglobina ajustada 7,2 | Escalamiento 3 |
| Esplenectomía | NRBC 0,8, esplenectomía declarada | Escalamiento 1 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-006 · Coagulación (tiempo de protrombina, INR y fibrinógeno)

**Qué hace.** Sin anticoagulantes, un INR alto sugiere un problema del hígado o de la coagulación. Con warfarina, el INR se lee como control del tratamiento. El patrón fibrinógeno bajo + tiempo de protrombina prolongado + plaquetas bajas es una urgencia. La muestra exige tubo de citrato con volumen exacto; hemolizada o de más de 24 horas no sirve.

```yaml
id: SEG-006
nombre: Coagulación
biomarcadores: [pt, inr, fibrinogen]
no_interpretable_si: ["muestra hemolizada", "más de 24 horas desde la toma", "llenado insuficiente del tubo de citrato"]
criterios:
  - id: inr_alto
    condicion: "inr > límite superior AND NOT anticoagulante"
  - id: patron_coagulopatia
    condicion: "fibrinogen < límite inferior AND pt > límite superior AND platelets < 100"
  - id: fibrinogeno_alto
    condicion: "fibrinogen > límite superior"
escalamiento:
  inr_alto: 2
  patron_coagulopatia: 3
  fibrinogeno_alto: "vigilar, con la relación de inflamación (documento 03)"
  con_warfarina: "control del tratamiento en la vista médica; escalamiento 2 si el INR está fuera del rango terapéutico declarado y hay sangrado"
texto_inr_alto: "Una de tus pruebas de coagulación salió alterada. Conviene una consulta médica en las próximas semanas. Si tienes sangrados que no paran o moretones grandes sin golpes, consulta antes."
frases_prohibidas: ["tienes hemofilia", "tienes cirrosis", "suspende tu anticoagulante"]
guias: ["Fichas pt, inr y fibrinogen del Knowledge Base"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | TP 12,1 y 11,8; INR 1,02 y 0,98; fibrinógeno 360 y 310 | Escalamiento 0 |
| INR alto | INR 1,6 sin anticoagulante | Escalamiento 2 |
| Con warfarina | INR 2,6, toma warfarina | Control en la vista médica |
| Coagulopatía | Fibrinógeno 120, TP 19, plaquetas 60 | Escalamiento 3 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-007 · Músculo y tejidos (CK y LDH)

**Qué hace.** La CK sube con frecuencia por ejercicio reciente y varía por etnia; las estatinas también la suben. Una CK muy alta con orina oscura o dolor muscular intenso es una urgencia por riesgo para el riñón. La LDH aislada no se interpreta: se falsea con la hemólisis de la muestra y solo cuenta dentro de la relación de hemólisis.

```yaml
id: SEG-007
nombre: Músculo y tejidos
biomarcadores: [ck_cpk, ldh]
ck:
  criterios:
    - id: ck_alta
      condicion: "> límite superior"
    - id: ck_muy_alta
      condicion: "> 5 veces el límite superior"
    - id: sintomas_rabdomiolisis
      condicion: "orina oscura OR dolor o debilidad muscular intensa (declarado en la visita)"
    - id: ejercicio_48h
      condicion: "ejercicio intenso en las 48 horas previas"
  escalamiento:
    ck_alta: 1
    ck_muy_alta_con_ejercicio_sin_sintomas: 1
    ck_muy_alta_sin_ejercicio: 2
    ck_muy_alta_con_sintomas: 3
  relacion: "patrón muscular (CK + AST + LDH) como confusor de las pruebas hepáticas (documento 03)"
ldh:
  no_interpretable_si: ["hemólisis de la muestra"]
  escalamiento:
    aislada: 1
    con_patron_hemolisis: "relación hemólisis, escalamiento 2"
texto_ck_alta: "Tu CK, una enzima de los músculos, está alta. Lo más común es que se deba a ejercicio reciente; conviene repetirla sin entrenar fuerte los dos días anteriores."
texto_ck_urgente: "Tu CK está muy alta. Si tienes la orina oscura o dolor muscular fuerte, ve a urgencias; nuestro equipo te va a llamar hoy."
frases_prohibidas: ["tienes rabdomiólisis", "tienes una enfermedad muscular", "deja las estatinas"]
guias: ["Fichas ck_cpk y ldh del Knowledge Base"]
por_verificar: "Corte de 5 veces el límite superior, definición habitual de rabdomiólisis; la ficha dice 'varias veces'."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | CK 165 y 82; LDH 190 y 160 | Escalamiento 0 |
| Ejercicio | CK 1.600 (hasta 308), maratón hace 2 días, sin síntomas | Escalamiento 1, repetir |
| Sin ejercicio | CK 2.000, sin ejercicio | Escalamiento 2 |
| Urgente | CK 9.000, orina oscura | Escalamiento 3 |
| LDH hemolizada | LDH 420, hemólisis reportada | No interpretable |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-008 · Electrolitos sin condición (magnesio, cloro y fósforo)

**Qué hace.** Estos tres se leen con el resto del panel. El magnesio importa sobre todo cuando acompaña potasio o calcio bajos. El fósforo importa con TFG baja o calcio alterado (M2).

```yaml
id: SEG-008
nombre: Electrolitos sin condición
biomarcadores: [magnesium, chloride, phosphorus]
magnesio:
  escalamiento:
    fuera_de_rango: 1
    con_potasio_o_calcio_bajos: 2
    bandera_critica_laboratorio: 3
cloro:
  escalamiento:
    fuera_de_rango: 1
  lectura: "con sodio y bicarbonato; aislado no se interpreta"
fosforo:
  escalamiento:
    fuera_de_rango: 1
    con_tfg_baja_o_calcio_alterado: "se lee dentro de M2 (enfermedad renal o paratiroides)"
confusores: ["hemólisis (sube el fósforo y el magnesio)", "demora en procesar", "diuréticos", "inhibidores de bomba de protones (bajan el magnesio)"]
frases_prohibidas: ["tienes un desequilibrio grave", "toma magnesio"]
guias: ["Fichas magnesium, chloride y phosphorus del Knowledge Base"]
por_verificar: "Escalamiento 2 para magnesio alterado con potasio o calcio bajos; la ficha habla de alteración marcada."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | Magnesio 2,0 y 1,9; cloro 103 y 104; fósforo 3,2 y 3,6 | Escalamiento 0 |
| Magnesio con potasio bajo | Magnesio 1,4, potasio 3,1 | Escalamiento 2 |
| Fósforo con TFG baja | Fósforo 5,2, TFG 38 | Se lee en M2 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-009 · Proteínas e inmunoglobulinas

**Qué hace.** Proteínas totales, globulinas y relación albúmina/globulina dependen mucho de la hidratación. Una relación invertida (globulinas por encima de la albúmina) o una IgG o IgM muy alta sin infección pueden sugerir una proteína anormal en la sangre, que solo confirma una electroforesis. Nunca se nombra una gammapatía.

```yaml
id: SEG-009
nombre: Proteínas e inmunoglobulinas
biomarcadores: [total_protein, globulin, ag_ratio, igg, igm]
criterios:
  - id: ag_invertida
    condicion: "ag_ratio < 1,0"
  - id: inmunoglobulina_muy_alta
    condicion: "igg o igm > 2 veces el límite superior, sin infección reciente"
  - id: igg_muy_baja
    condicion: "igg < límite inferior con infecciones repetidas declaradas"
escalamiento:
  fuera_de_rango: 1
  ag_invertida: 1
  inmunoglobulina_muy_alta: 2
  igg_muy_baja: 2
vista_medica: "con ag_invertida o inmunoglobulina_muy_alta, considerar electroforesis de proteínas"
confusores: ["deshidratación (sube todo)", "infección reciente", "hepatopatía", "albúmina baja"]
texto_ag_invertida: "La proporción entre tus proteínas de la sangre está alterada. Puede tener varias causas; coméntalo con tu médico."
frases_prohibidas: ["tienes mieloma", "tienes una gammapatía", "tienes las defensas bajas"]
guias: ["Fichas total_protein, globulin, ag_ratio, igg e igm del Knowledge Base"]
por_verificar: "Cortes de 1,0 para la relación A/G y de 2 veces el límite para las inmunoglobulinas son propuesta; las fichas dicen 'marcadamente'."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | A/G 1,70 y 1,59; IgG 1.120 y 1.050; IgM 95 y 140 | Escalamiento 0 |
| Invertida | Albúmina 3,6, globulinas 4,2 (A/G 0,86) | Escalamiento 1; vista médica sugiere electroforesis |
| IgG muy alta | IgG 3.600 sin infección | Escalamiento 2 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-010 · Metabolismo sin condición (péptido C, fructosamina y NT-proBNP fuera de diabetes)

**Qué hace.** El péptido C no clasifica el tipo de diabetes por sí solo; con glucosa baja y péptido C alto se suma a la regla de glucosa baja (M1 EM-005). La fructosamina no es confiable con albúmina menor de 3,0 g/dL ni con suplementos de vitamina C. El NT-proBNP solo se mide como refleja en diabetes (M1 CA-007); si aparece fuera de ese contexto, se lee con los umbrales por edad.

```yaml
id: SEG-010
nombre: Metabolismo sin condición
biomarcadores: [c_peptide, fructosamine, nt_probnp]
peptido_c:
  escalamiento:
    fuera_de_rango: 1
    alto_con_glucosa_menor_54: "refuerza M1 EM-005; escalamiento 3"
fructosamina:
  no_interpretable_si: ["albúmina < 3,0 g/dL", "suplemento de vitamina C en las 24 horas previas"]
  escalamiento:
    fuera_de_rango: 1
  lectura: "apoya glucosa y HbA1c; útil si la HbA1c no es confiable por anemia"
nt_probnp_sin_diabetes:
  escalamiento:
    "125 o más": 1
    "sobre el umbral por edad (450 menores de 50; 900 de 50 a 75; 1.800 mayores de 75)": 2
frases_prohibidas: ["tienes diabetes tipo 1", "tienes un insulinoma", "tienes insuficiencia cardíaca"]
guias: ["Fichas c_peptide, fructosamine y nt_probnp del Knowledge Base", "ESC HFA 2023 (umbrales por edad)"]
por_verificar: "Los umbrales por edad del NT-proBNP vienen de servicios de urgencias; usarlos en una toma preventiva es propuesta."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | Péptido C 3,4 y 1,8; fructosamina 268 y 230 | Escalamiento 0 |
| Fructosamina no confiable | Fructosamina 210, albúmina 2,8 | No interpretable |
| Glucosa baja con péptido C alto | Glucosa 48, péptido C 6,2 | Escalamiento 3 (M1 EM-005) |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-011 · Hormonas sin condición (DHEA-S, estradiol, LH y progesterona)

**Qué hace.** Estradiol, LH y progesterona siguen la regla de fase del ciclo (documento 03, sección 03.8); la progesterona solo se mide en mujeres. En hombres, estradiol y LH se leen con el intervalo masculino. La DHEA-S muy alta en una mujer, sobre todo con vello o acné de aparición rápida, puede requerir estudio pronto.

```yaml
id: SEG-011
nombre: Hormonas sin condición
biomarcadores: [dhea_s, estradiol, lh, progesterone]
estradiol_lh_progesterona:
  mujeres: "intervalo de la fase calculada con la fecha de última menstruación; sin fecha, con anticonceptivo, embarazo o menopausia: no interpretable por fase"
  hombres: "intervalo masculino del laboratorio (progesterona no se mide)"
  escalamiento:
    fuera_de_rango: 1
dhea_s:
  escalamiento:
    fuera_de_rango: 1
    mujer_mayor_de_2_veces_el_limite: 2
  relacion: "con andrógenos altos (M5 MU-001), se cruza en la vista médica"
texto_fuera_de_fase: "Este valor hormonal está fuera del rango esperado para el día de tu ciclo. Varía mucho de un día a otro; si tus ciclos son irregulares, coméntalo con tu médico."
frases_prohibidas: ["tienes un tumor suprarrenal", "no estás ovulando", "tienes infertilidad", "tienes menopausia"]
guias: ["Fichas dhea_s, estradiol, lh y progesterone del Knowledge Base"]
por_verificar: "Escalamiento 2 para DHEA-S mayor del doble del límite en mujeres es propuesta; la ficha habla de elevación marcada de inicio rápido."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Fase folicular · PDF mujer 34 años | Día 9, estradiol 68, LH 5,4, progesterona 0,4; DHEA-S 180 | Todo en rango de fase, escalamiento 0 |
| Hombre · PDF hombre 46 años | Estradiol 28, LH 4,2 (intervalo masculino); DHEA-S 210 | En rango |
| Anticonceptivo | Estradiol 15, anticonceptivo oral | No interpretable por fase |
| DHEA-S muy alta | Mujer, DHEA-S 820 (hasta 340) | Escalamiento 2 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-012 · Hemograma sin condición

**Qué hace.** Monocitos, basófilos, VPM, HCM, CHCM, hematocrito y recuento de eritrocitos acompañan a las condiciones del módulo M3. Solos no forman hallazgos; alteraciones marcadas y persistentes se repiten.

```yaml
id: SEG-012
nombre: Hemograma sin condición
biomarcadores: [monocytes_pct, basophils_pct, mpv, mch, mchc, hematocrit, erythrocytes]
escalamiento:
  fuera_de_rango: 1
  con_dos_o_mas_lineas_alteradas: "regla de M3 HE-A02 (escalamiento 2)"
lectura:
  vpm: "solo con plaquetas alteradas (M3 HE-005)"
  hcm_chcm: "apoyan anemia y déficit de hierro (M3)"
  hematocrito_eritrocitos: "se leen con la hemoglobina ajustada (M3 HE-001)"
  monocitos_basofilos: "repetir si la alteración es marcada; persistentes sin causa, consulta"
frases_prohibidas: ["tienes leucemia", "tienes una infección"]
guias: ["Fichas del hemograma en el Knowledge Base"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF hombre 46 años | Monocitos 7,1 %, basófilos 0,5 %, VPM 9,8 | Escalamiento 0 |
| Apoyo de anemia · PDF mujer 34 años | HCM 26,0 (bajo), hematocrito 35,0 (bajo) | Se leen dentro de M3; no forman hallazgo propio |
| Basófilos altos | Basófilos 3,5 % | Escalamiento 1, repetir |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-013 · Orina y heces sin condición

**Qué hace.** Los campos del uroanálisis y del coprológico que no alimentan una condición tienen reglas propias. La proteína en tira se lee con la albúmina/creatinina; la glucosa en orina se lee con la glucosa en sangre y los medicamentos; las cetonas en ayunas suelen ser normales. La sangre visible en heces es distinta de la sangre oculta y requiere consulta.

```yaml
id: SEG-013
nombre: Orina y heces sin condición
biomarcadores: [urinalysis_protein, urinalysis_glucose, urinalysis_ketones, urinalysis_bilirubin, urinalysis_urobilinogen, stool_mucus, stool_visible_blood]
reglas:
  proteina_en_tira: "se lee con la albúmina/creatinina (M2 NE-002); sin ella, escalamiento 1"
  glucosa_en_orina:
    con_glucosa_en_sangre_alta: "apoya M1 EM-002"
    con_inhibidor_SGLT2: "esperada por el medicamento; escalamiento 0"
    con_glucosa_en_sangre_normal: "escalamiento 1"
  cetonas:
    en_ayunas_sin_diabetes: "esperable; escalamiento 0"
    con_glucosa_alta_o_diabetes: "escalamiento 2"
  bilirrubina_en_orina: "escalamiento 2; se lee con la función hepática (M4)"
  urobilinogeno_alto: "escalamiento 1; se lee con la función hepática y la hemólisis"
  moco_en_heces: "escalamiento 0 si es escaso"
  sangre_visible_en_heces: "escalamiento 2; se cruza con la sangre oculta (M4 GA-004)"
frases_prohibidas: ["tienes diabetes", "tienes una enfermedad del riñón", "tienes cáncer"]
guias: ["Fichas del uroanálisis y del coprológico (por escribir en la Fase 1)"]
por_verificar: "Estas fichas de biomarcador todavía no existen; las reglas son propuesta de Saludly hasta escribirlas."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | Tira negativa, urobilinógeno 0,2, heces sin moco ni sangre | Escalamiento 0 |
| Glucosa con medicamento | Glucosa en orina positiva, toma empagliflozina | Escalamiento 0 |
| Cetonas con diabetes | Cetonas positivas, glucosa 280 | Escalamiento 2 |
| Sangre visible | Sangre macroscópica en heces | Escalamiento 2 |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## SEG-014 · Contexto cardiovascular y nutricional

**Qué hace.** Estos biomarcadores dan contexto a condiciones de otros módulos sin formar hallazgos propios. El zinc exige un tubo libre de zinc; sin él, el resultado sale falsamente alto. El BUN alto con creatinina normal suele deberse a hidratación o a una dieta alta en proteína; con anemia y sangre oculta positiva, la vista médica considera sangrado digestivo.

```yaml
id: SEG-014
nombre: Contexto cardiovascular y nutricional
biomarcadores: [apoa1, apob_apoa1_ratio, remnant_cholesterol, tc_hdl_ratio, transferrin, zinc, bun, bun_creatinine_ratio]
lectura:
  apoa1_apob_apoa1: "contexto del riesgo cardiovascular (M1 CA-005), en la vista médica"
  colesterol_remanente_y_ct_hdl: "contexto de dislipidemia (M1 CA-001)"
  transferrina: "contexto del hierro (M3)"
  zinc: "no interpretable sin tubo libre de zinc; bajo: recomendación alimentaria; escalamiento 0"
  bun: "con creatinina normal: hidratación y dieta; con anemia y sangre oculta positiva: la vista médica considera sangrado digestivo (escalamiento según M4 GA-004)"
  bun_creatinina: "relación > 20: vigilar hidratación"
escalamiento:
  fuera_de_rango: "0 o 1 según el texto del grupo; nunca más que la condición a la que da contexto"
frases_prohibidas: ["tienes déficit de zinc", "toma zinc", "estás deshidratado"]
guias: ["Fichas apoa1, apob_apoa1_ratio, transferrin, zinc, bun y bun_creatinine_ratio del Knowledge Base"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Normal · PDF ejemplos | ApoA1 112 y 158; transferrina 256 y 346; zinc 82 y 71; BUN 15 y 10 | Escalamiento 0 |
| Zinc sin tubo especial | Zinc 140, tubo estándar | No interpretable |
| BUN alto | BUN 28, creatinina 0,9 (relación 31) | Vigilar hidratación |

**Firma médica**

- [ ] Aprobada - \[ \] Aprobada con cambios - \[ \] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:

---

## Resultado esperado en los PDF de ejemplo

En los dos PDF todos los biomarcadores de este documento están en rango o no detectables. El resultado esperado es escalamiento 0 en todos, con revisión médica de troponina, cortisol, ACTH, IGF-1, osmolalidad y eritroblastos en la vista del médico. No sale ninguna alarma al paciente.

## Lo que el médico debe mirar con más cuidado

1. La traducción de "escalar siempre" en revisión médica obligatoria para cortisol, ACTH, IGF-1, osmolalidad y eritroblastos.
2. Escalamiento 2 para cortisol bajo en la mañana (SEG-002) y para brecha osmolar mayor de 10 (SEG-004).
3. Eritroblastos positivos con escalamiento 2 y llamada, en vez de derivación inmediata (SEG-005).
4. Corte de 5 veces el límite de CK (SEG-007).
5. Cortes propuestos para relación A/G, inmunoglobulinas, DHEA-S y magnesio.
6. Uso de los umbrales por edad del NT-proBNP, que vienen de urgencias, en una toma preventiva.
7. Las reglas de orina y heces de SEG-013, que dependen de fichas de biomarcador que todavía no existen.