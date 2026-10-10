**SALUDLY BRAIN**

**03 — Knowledge Base / RAG clínico**

*Qué conocimiento usa el motor, cómo está organizado y qué decisiones clínicas lo rigen · versión 1 · 6 de octubre de 2026*

> Las decisiones clínicas de este documento (conflictos entre guías, relaciones que entran como patrón y forma de mostrar hormonas) las tomó Claude por encargo del equipo de Saludly, siguiendo las propuestas de los lotes. Antes de usarse con pacientes reales necesitan la firma de un médico.

# **03.1 — Qué es el Knowledge Base**

Es la única fuente de conocimiento clínico del motor. Tiene cuatro tipos de pieza, todas en archivos Markdown con un encabezado estructurado (YAML) que el motor lee como datos:

| Pieza | Cuántas | Qué contiene |
| :---- | :---- | :---- |
| Ficha de biomarcador | 100 existentes más 34 por escribir | Definición, unidades, umbrales separados (laboratorio, decisión clínica, tamizaje), interpretación, confusores, seguridad y bloque RAG_INSTRUCTIONS |
| Ficha de condición | 50 incluidas y 27 de apoyo | Regla estructurada: criterios, contexto obligatorio, coincidencia, escalamiento, guía y frases permitidas y prohibidas |
| Relación entre módulos | Una por relación decidida en 03.7 | Biomarcadores, dirección, mecanismo, fuerza de evidencia, confusores, acción permitida y prohibida, fuente |
| Regla transversal | Vitaminas, objetivos, confusores, wearables, seguridad | Reglas que aplican a muchos biomarcadores a la vez |

Las 34 fichas por escribir son: 22 analitos del panel sin ficha (HCM, vitaminas A, E, K1, C, biotina, niacina, índice omega-3, relación omega-6/omega-3, CoQ10, TIBC, ANA, PSA total, anti-VHC, HBsAg, anti-HBs, anti-HBc, ELISA de Chagas, uroanálisis, sangre oculta en heces, antígeno de H. pylori y coprológico), 7 reflejas (aldosterona, renina, ARN de hepatitis C, segunda ELISA de Chagas, macroprolactina, PSA libre y ácido metilmalónico), 3 calculados (colesterol remanente, relación colesterol/HDL y PhenoAge), más neutrófilos % y la relación albúmina/creatinina como pieza propia si se separa del uroanálisis.

# **03.2 — Los 6 módulos**

| Módulo | Especialidades | Condiciones incluidas |
| :---- | :---- | :---- |
| M1 · Cardiometabólico | Cardiología; Endocrinología metabólica | 7 + 5 |
| M2 · Riñón y glándulas | Nefrología; Tiroides, paratiroides y suprarrenal | 6 + 8 |
| M3 · Sangre y nutrición | Hematología; Nutrición y micronutrientes | 6 + 2 |
| M4 · Digestivo e infecciones | Gastroenterología y hepatología; Infectología | 6 + 3 |
| M5 · Mujer y hombre | Salud de la mujer; Urología y salud del hombre | 3 + 2 |
| M6 · Inmunidad y envejecimiento | Reumatología; Medicina interna y envejecimiento | 1 + 1 |

Infectología queda con hepatitis C, hepatitis B y enfermedad de Chagas crónica. VIH, sífilis, clamidia y gonorrea salen del producto. Total: 50 condiciones incluidas.

# **03.3 — Nivel de cada biomarcador**

Cada ficha declara uno de cuatro niveles, que decide qué hace el motor con ella:

- **Con patrón:** alimenta al menos una condición o relación.
- **Solo valor y rango:** se muestra con su clasificación; respeta las reglas de escalamiento de su ficha.
- **Vitamina:** se clasifica y genera recomendaciones según la regla de vitaminas (documento 07).
- **Refleja:** solo existe cuando el laboratorio la corre; se interpreta junto con el resultado que la activó.

# **03.4 — Formato de una ficha de condición**

```yaml
id: COND-M1-EM-001
nombre: Prediabetes
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida            # incluida | apoyo
detectabilidad: D1        # D1 directa | D2 con contexto | D3 señal parcial
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
contexto_obligatorio: ["ayuno_horas >= 8", "embarazo == false"]
excluye_si: ["COND-M1-EM-002"]          # diabetes en rango diagnóstico
coincidencia:
  alta: "glucosa AND hba1c"
  moderada: "glucosa XOR hba1c"
escalamiento: 1
nivel_lenguaje: riesgo_potencial
confusores: ["corticoides", "ayuno_insuficiente"]
guias: ["ADA Standards of Care 2026, sección 2", "GPC Colombia DM2 2016"]
frase_permitida: "Tus resultados de glucosa están en un rango que las guías asocian con mayor riesgo de diabetes."
frases_prohibidas: ["tienes prediabetes", "eres diabético"]
recomendaciones: ["REC-ALI-012", "REC-ACT-004", "REC-SUE-002"]
```

# **03.5 — Formato de una relación**

```yaml
id: REL-M1M4-001
biomarcadores: [alt, ggt, triglycerides, homa_ir, hba1c]
direccion: "ALT o GGT altas con triglicéridos altos y HOMA-IR o HbA1c alterados"
mecanismo: "resistencia a la insulina y depósito de grasa hepática"
resultado: "patrón compatible con alteración hepática metabólica"
tipo: patron              # patron | vigilar
fuerza_evidencia: guia    # guia | metaanalisis | cohorte | asociacion | mecanismo
minimo_senales: 2
confusores: ["alcohol_48h", "ejercicio_intenso_48h", "medicamentos_hepatotoxicos"]
repeticion: "persistencia en 6 a 12 meses antes de hablar de daño hepático persistente"
accion_permitida: ["educación", "seguimiento", "FIB-4", "derivación"]
accion_prohibida: ["diagnóstico de hígado graso", "detox hepático", "dosis de suplementos"]
fuente: ["ACG 2017", "EASL 2024 (por verificar)"]
```

# **03.6 — Conflictos entre guías: postura adoptada**

Se adopta la propuesta de cada lote, salvo donde una decisión posterior del equipo la cambió (vitamina D y medición universal).

| Lote | Tema | Postura adoptada |
| :---- | :---- | :---- |
| 1 | Calculadora de riesgo cardiovascular | SCORE2-PURE (GPC HTA 2025) entre 40 y 69 años; fuera de ese rango se muestran los factores de riesgo sin porcentaje |
| 1 | Umbral de hipertensión | 130/80 mmHg en la toma de la enfermera, siempre como sospecha hasta confirmar con automonitoreo |
| 1 | Lp(a) elevada | Más de 50 mg/dL o 105 nmol/L; se menciona el corte de 125 nmol/L de ACC/AHA y se declara la unidad del laboratorio |
| 1 | Cintura | 90 cm hombres y 80 cm mujeres para síndrome metabólico; 94 y 90 cm solo dentro de FINDRISC |
| 1 | Triglicéridos | Desde 500 mg/dL, escalamiento 2; urgencia solo con síntomas o bandera crítica del laboratorio; desde 1.000 mg/dL se menciona riesgo de pancreatitis |
| 1 | NT-proBNP | Solo en personas con diabetes, como señal parcial |
| 2 | Persistencia de albuminuria | Enfermedad renal con dos mediciones separadas 3 meses o más; un valor aislado es "a confirmar" |
| 2 | Rango de TSH | Intervalo del laboratorio para "fuera de referencia"; rango del consenso colombiano por edad como umbral de decisión |
| 2 | Microhematuria | Más de 3 hematíes por campo; nunca con menstruación declarada |
| 2 | Potasio alto | Nunca escalar con un valor aislado o hemolizado; repetir primero, salvo bandera crítica del laboratorio |
| 2 | Hiperaldosteronismo | Aldosterona y renina solo con presión de 130/80 o más |
| 3 | Anemia en altura | El laboratorio de ejemplo usa intervalos generales, así que se aplica el ajuste OMS por altitud de Bogotá; si un laboratorio declara intervalo bogotano, no se ajusta dos veces |
| 3 | Ferritina e inflamación | Déficit con ferritina menor de 15 ng/mL; menor de 70 si hay hs-CRP mayor de 5 mg/L |
| 3 | Cortes de B12 | NICE: menor de 180 ng/L déficit; entre 180 y 350 se activa ácido metilmalónico |
| 3 | Vitamina D | En el panel; se clasifica por el intervalo del laboratorio y su recomendación es solo alimentaria y de sol, sin dosis |
| 3 | Sobrecarga de hierro | Ferritina sola como alerta; ferritina más saturación de transferrina mayor de 45 % para remitir |
| 4 | Cáncer colorrectal | Sangre oculta positiva a cualquier edad, remisión para colonoscopia (escalamiento 2); el informe menciona el tamizaje formal de 50 a 75 años de la Res. 3280 |
| 4 | Transaminasas | Entre el valor sano de la ACG y el límite del laboratorio, "limítrofe"; por encima del laboratorio, "alto" |
| 4 | H. pylori | Antígeno fecal monoclonal con su limitación escrita en el informe |
| 4 | Hepatitis B y C | Se miden a todos con el consentimiento de la visita; un reactivo lo comunica el médico por llamada |
| 4 | Chagas fuera del embarazo | Dos ELISA; reactivo en ambas, remisión para confirmación. El lineamiento del INS para adultos sigue por verificar |
| 4 | FIB-4 | Se usa, pero en mayores de 65 años o con diabetes no se descarta fibrosis solo con FIB-4 |
| 5 | Medición universal de hormonas | Se miden a todos; sin síntomas, el agente no nombra condiciones hormonales, solo resultados observados |
| 5 | PSA | Se mide a todos los hombres con consentimiento; tamizaje formal de 50 a 75 años; fuera de esa edad, "valor a revisar con tu médico" |
| 5 | Testosterona | Se etiqueta como baja solo si el laboratorio declara método certificado por el CDC; si no, solo resultado observado |
| 5 | Prolactina | Siempre se repite antes de hablar de prolactina alta; sin interpretación en embarazo |
| 6 | ANA | Título y patrón obligatorios; desde 1:160, o con patrón distinto al moteado fino, se recomienda consulta; 1:80 se muestra como resultado observado |
| 6 | Edad biológica | PhenoAge en pantalla aparte, como estimación de un modelo publicado |
| 6 | Riesgo de desnutrición | Solo "riesgo" y remisión, nunca diagnóstico |

# **03.7 — Relaciones entre módulos: patrón o vigilar**

Regla para decidir: entra como **patrón** si la relación está en una guía o ya existe como condición en los lotes; entra como **vigilar** si es una asociación sin guía; si depende de síntomas que Saludly no pregunta, se muestra como incompleta.

| Grupo | Relación | Decisión |
| :---- | :---- | :---- |
| Cardiometabólico | Glucosa o HbA1c alteradas + insulina o HOMA-IR altos + triglicéridos altos + HDL bajo | Patrón |
| Cardiometabólico | Lo anterior + hs-CRP alta | Vigilar (la hs-CRP solo refuerza) |
| Aterogénico | ApoB alta + LDL o no-HDL altos, con o sin Lp(a) alta | Patrón |
| Aterogénico | hs-CRP + fibrinógeno + homocisteína altos | Vigilar |
| Aterogénico | NT-proBNP o troponina altas | Fuera de patrones: regla de seguridad de su ficha |
| Hígado | ALT o GGT altas + triglicéridos altos + HOMA-IR o HbA1c alterados | Patrón, con FIB-4 |
| Hígado | hs-CRP + VSG + fibrinógeno altos | Vigilar |
| Músculo | CK + AST + LDH altas | Patrón de origen muscular, usado como confusor: si se cumple, AST y LDH no se leen como hepáticas |
| Hemólisis | Bilirrubina indirecta + LDH altas + hemoglobina baja + reticulocitos altos | Patrón con escalamiento 2 |
| Riñón | Albuminuria + TFG estimada baja | Patrón de mayor prioridad del módulo |
| Riñón | TFG por creatinina discordante con cistatina C | Patrón técnico: revisar masa muscular y ejercicio |
| Riñón | PTH alta + TFG baja | Patrón de apoyo dentro de enfermedad renal |
| Hierro | Saturación baja + ferritina baja o límite + RDW alto | Patrón |
| Hierro | Ferritina normal + saturación baja + inflamación | Patrón de apoyo (anemia con perfil inflamatorio) |
| Hierro | B12 o folato bajos + homocisteína alta | Patrón |
| Hierro | Hierro bajo + anticuerpos tiroideos | Vigilar |
| Tiroides | TSH alta + T4 libre baja o límite + anti-TPO o anti-Tg positivos | Patrón |
| Tiroides | TSH alta + colesterol alto + CK alta + homocisteína alta | Vigilar |
| Tiroides | TSH alterada + ferritina o saturación bajas | Vigilar |
| Vitamina D | Vitamina D baja + PTH alta + calcio o fósforo alterados | Patrón |
| Vitamina D | Vitamina D baja + hs-CRP alta | Vigilar |
| Vitamina D | Vitamina D baja + ferritina o hemoglobina bajas | Vigilar |
| Hormonas | Cortisol alto + glucosa o HbA1c altas + presión alta + frecuencia en reposo alta | Vigilar; nunca se nombra hipercortisolismo |
| Hormonas | Testosterona baja + SHBG alterada + LH o FSH alteradas | Patrón solo con método certificado; sin síntomas, resultado observado |
| Hormonas | Estradiol o progesterona alterados + temperatura de muñeca alterada | Vigilar; incompleto sin regularidad del ciclo |
| Hormonas | TSH alterada + frecuencia en reposo, sueño o actividad alterados (Apple Watch) | Vigilar, como contexto |
| Hormonas | Prolactina alta + TSH alterada + medicamentos | Patrón de la condición prolactina alta; siempre repetir |

# **03.8 — Cómo se muestran cortisol, ACTH y hormonas del ciclo**

Todas las tomas son en ayunas y en la mañana, y la hora de toma viaja en los metadatos del PDF.

| Biomarcador | Regla |
| :---- | :---- |
| Cortisol | Se clasifica con el intervalo matutino solo si la toma fue entre las 6:00 y las 10:00; fuera de esa hora, "no interpretable". Nunca forma un patrón por sí solo ni se nombran Cushing o Addison. Fuera de rango, escalamiento 1 con texto prudente; bandera crítica del laboratorio, escalamiento 3 |
| ACTH | El paciente ve el valor y la clasificación; la interpretación solo aparece en la vista del médico |
| FSH, LH, estradiol, progesterona | Se calcula el día del ciclo con la fecha de última menstruación y se usa el intervalo de esa fase. Sin fecha, con anticonceptivo hormonal, embarazo o menopausia declarada: valor visible y "no interpretable por fase" |
| Progesterona | Solo en mujeres |
| Prolactina | Clasificación con el intervalo del laboratorio; alta se repite con macroprolactina refleja; sin interpretación en embarazo |
| Estradiol y LH en hombres | Intervalo masculino del laboratorio; resultado observado, sin condición propia |

# **03.9 — Jerarquía de fuentes y versionado**

1. Normativa colombiana (Resolución 3280, GPC del Ministerio e IETS).
2. Guía vigente de la sociedad colombiana.
3. Guía internacional de referencia (ADA, KDIGO, AHA/ACC, ESC/EAS, Endocrine Society, EASL, NICE, OMS).
4. Revisiones sistemáticas y metaanálisis.
5. Cohortes y estudios de validación.
6. Artículos de mecanismo, solo como apoyo.

Cada fuente se registra como "leída completa" o "solo resultado de búsqueda"; nada de la segunda categoría pasa a producción. Cada pieza lleva versión y fecha; un cambio de umbral exige firma médica y vuelve a correr todos los casos de prueba.

# **03.10 — Cómo lo usa el motor**

El motor no "busca" las reglas: las carga por identificador desde el repositorio, de forma determinista. El índice de búsqueda de OpenClaw (palabra clave y vectorial, embeddings locales) se usa solo para que el agente traiga el texto de las fichas que explican cada hallazgo y para preguntas del médico. Así una búsqueda que falla no cambia un resultado clínico.
