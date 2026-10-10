# Matriz de cobertura · Lote 1: Cardiología y Endocrinología metabólica

Oct 3, 2026 · @onova pro

## Resumen

El lote 1 deja 12 condiciones incluidas (7 de cardiología y 5 de endocrinología metabólica), 4 de apoyo y 5 descartadas, cada una con su guía identificada. La fuente de mayor peso es colombiana y reciente: la GPC de hipertensión 2025 del Ministerio y el IETS.

Lo que necesito de ti:

- **Aprobar fila por fila** la columna Decisión de las tablas de Cardiología y Endocrinología; es un desplegable que puedes cambiar.
- **Confirmar que la enfermera mide presión arterial, peso, talla y cintura** en cada visita. Sin eso se pierden 4 de las 12 condiciones.
- **Agregar el cuestionario FINDRISC a la app.** La GPC colombiana lo recomienda como tamizaje de diabetes y cuesta cero.
- **Asignar el médico revisor** para los 6 conflictos entre guías de la última sección.

Dos oportunidades de negocio salieron de las guías. La ADA 2026 confirma diabetes con glucosa y HbA1c alteradas en la misma muestra, así que el informe puede llegar al médico con el criterio de laboratorio ya cumplido. Y la GPC de hipertensión sugiere prestar tensiómetros validados para confirmar el diagnóstico en casa, un servicio que encaja con el modelo de Saludly.

## Método

Una condición entra al RAG solo si pasa los cuatro filtros; si falla uno, queda descartada con su razón escrita.

1. **Carga de enfermedad en Colombia:** es frecuente o grave en la población adulta.
2. **Detectable por Saludly:** el patrón central se arma con muestras de sangre, orina o heces, más mediciones de la enfermera o el cuestionario. No depende de ECG, imágenes ni pruebas que no ofrecemos.
3. **Guía oficial con criterio verificable:** existe un umbral o algoritmo publicado y verificado en la fuente oficial (ver Registro de fuentes).
4. **Accionable en prevención:** detectarla cambia lo que el paciente o su médico hacen.

**Jerarquía de guías (aprobada):** normativa colombiana (Resolución 3280, GPC del Ministerio e IETS), luego la guía vigente de la sociedad colombiana, luego la guía internacional de referencia. Si dos difieren, el RAG muestra ambas con su fuente.

**Escala de detectabilidad:**

| Nivel | Significado | Qué hace Saludly |
| --- | --- | --- |
| D1 Directa | El laboratorio basta para el patrón central | Nombra la condición y su nivel de coincidencia |
| D2 Con contexto | Necesita además presión arterial, medidas corporales o cuestionario | Igual que D1, solo si el contexto está completo |
| D3 Señal parcial | Confirmarla exige una prueba que no hacemos | Alerta y recomienda la prueba al médico |
| D4 Fuera de alcance | No se puede detectar con nuestras muestras | No se reporta |

**Decisión por candidata:** Incluida (condición propia en el informe), Apoyo (modifica otra condición, no aparece sola) o Descartada.

**Nivel de coincidencia (reemplaza "probabilidad"):** alta = todos los criterios centrales y datos completos; moderada = criterios centrales con datos incompletos, o uno central más apoyo; baja = solo criterios de apoyo, se muestra como "vigilar", nunca como condición. El informe ordena por escalamiento (0 a 3), luego coincidencia, luego fuerza de la evidencia.

**Alertas urgentes:** salen solo de los valores críticos que marque el laboratorio o de umbrales de urgencia escritos en una guía. Saludly no inventa umbrales de urgencia.

## Cardiología

Cardiología queda con 7 condiciones incluidas, 2 de apoyo y 3 descartadas. El hallazgo clave: la GPC colombiana de hipertensión 2025 cambia la calculadora oficial de riesgo a SCORE2 recalibrado para Colombia (SCORE2-PURE).

| Condición | Patrón central | Biomarcadores y contexto | Guía | Detectabilidad | Decisión |
| --- | --- | --- | --- | --- | --- |
| Dislipidemia aterogénica | LDL-C o no-HDL elevados, con o sin HDL bajo | Colesterol total, HDL, triglicéridos, LDL, no-HDL; ayuno, embarazo, medicamentos | [GPC Colombia dislipidemias 2014](https://www.elsevier.es/es-revista-revista-colombiana-cardiologia-203-articulo-guia-practica-clinica-prevencion-deteccion-S0120563315001059), [ACC/AHA 2026](https://professional.heart.org/en/science-news/2026-guideline-on-the-management-of-dyslipidemia/top-things-to-know) | D1 Directa | Incluida |
| Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar | LDL-C mayor de 190 mg/dL (la GPC colombiana lo trata como riesgo alto sin calculadora) | LDL-C; antecedente familiar de evento cardiovascular temprano | [GPC Colombia dislipidemias 2014](https://www.elsevier.es/es-revista-revista-colombiana-cardiologia-203-articulo-guia-practica-clinica-prevencion-deteccion-S0120563315001059) | D2 Con contexto | Incluida |
| Hipertrigliceridemia | Triglicéridos persistentemente elevados; desde 1.000 mg/dL la guía añade prevención de pancreatitis | Triglicéridos; ayuno confirmado; alcohol | [ACC/AHA 2026](https://professional.heart.org/en/science-news/2026-guideline-on-the-management-of-dyslipidemia/top-things-to-know) | D1 Directa | Incluida |
| Lipoproteína(a) elevada | Mayor de 50 mg/dL o 105 nmol/L (ESC/EAS); desde 125 nmol/L (ACC/AHA). Se mide una vez en la vida | Lp(a); antecedente familiar | [ESC/EAS 2025](https://www.escardio.org/news/news-room/congress-news/2025-focused-update-dyslipidaemias/), [ACC/AHA 2026](https://professional.heart.org/en/science-news/2026-guideline-on-the-management-of-dyslipidemia/top-things-to-know) | D1 Directa | Incluida |
| Riesgo cardiovascular global elevado a 10 años | Puntaje SCORE2-PURE; la GPC 2014 usaba Framingham × 0,75 | Edad, sexo, presión arterial, tabaquismo, colesterol total, HDL, diabetes | [GPC Colombia HTA 2025](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/CA/gpc-actualizacion-parcial-hta-primaria-vc.pdf), [GPC dislipidemias 2014](https://www.elsevier.es/es-revista-revista-colombiana-cardiologia-203-articulo-guia-practica-clinica-prevencion-deteccion-S0120563315001059) | D2 Con contexto | Incluida |
| Hipertensión arterial o presión elevada (sospecha) | Desde 130/80 mmHg en la toma de la enfermera; la guía exige confirmar con automonitoreo (AMPA) o MAPA | Presión arterial con tensiómetro validado; medicamentos | [GPC Colombia HTA 2025](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/CA/gpc-actualizacion-parcial-hta-primaria-vc.pdf), [AHA/ACC 2025](https://www.ahajournals.org/doi/10.1161/HYP.0000000000000249) | D3 Señal parcial | Incluida |
| Riesgo de insuficiencia cardiaca en personas con diabetes | NT-proBNP desde 125 pg/mL; confirmar requiere ecocardiograma. Solo se mide si hay diabetes | NT-proBNP; diagnóstico de diabetes | ADA Standards of Care (vía [Diabetes Care 2025](https://diabetesjournals.org/care/article/48/9/1465/158257/Is-Screening-for-Heart-Failure-and-Peripheral)) | D3 Señal parcial | Incluida |
| Discordancia ApoB / LDL | ApoB alta con LDL controlado; útil con triglicéridos mayores de 200 mg/dL o diabetes | ApoB, triglicéridos, LDL-C | [ACC/AHA 2026](https://professional.heart.org/en/science-news/2026-guideline-on-the-management-of-dyslipidemia/top-things-to-know) | D1 Directa | Apoyo |
| Inflamación de bajo grado | hs-CRP persistentemente mayor de 2 mg/L; modifica el riesgo, exige segunda medición sin infección | hs-CRP; infección reciente | ESC/EAS 2025 (modificador de riesgo) | D3 Señal parcial | Apoyo |
| Homocisteína como riesgo cardiovascular | Evidencia insuficiente para uso cardiovascular aislado; pasa al lote de Nutrición | Homocisteína, B12, folato | KB actual, RISK-008 | D1 Directa | Descartada |
| Lesión miocárdica (troponina) | Marcador de evento agudo, no de prevención; sale del kit | Troponina hs | KB actual, Tier 4 | D4 Fuera de alcance | Descartada |
| Fibrilación auricular | Exige ECG; los wearables solo aportan contexto | ECG (no ofrecido) | No aplica | D4 Fuera de alcance | Descartada |

La toma de presión de la enfermera vuelve D2 lo que hoy es invisible: sin presión arterial no hay riesgo global ni síndrome metabólico. La GPC de hipertensión 2025 sugiere prestar tensiómetros validados para AMPA; Saludly puede ofrecerlo como servicio.

## Endocrinología metabólica

Endocrinología metabólica queda con 5 condiciones incluidas, 2 de apoyo y 2 descartadas. La ADA 2026 acepta como confirmación dos pruebas distintas alteradas en la misma muestra, así que glucosa y HbA1c elevadas juntas dan coincidencia alta sin esperar otra toma.

| Condición | Patrón central | Biomarcadores y contexto | Guía | Detectabilidad | Decisión |
| --- | --- | --- | --- | --- | --- |
| Prediabetes | Glucosa en ayunas 100–125 mg/dL o HbA1c 5,7–6,4 % | Glucosa en ayunas, HbA1c; horas de ayuno, embarazo, corticoides | [ADA 2026, sección 2](https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes), [GPC Colombia DM2](https://colombiamedica.univalle.edu.co/index.php/comedica/article/download/2207/7056?inline=1) | D1 Directa | Incluida |
| Diabetes tipo 2 en rango diagnóstico | Glucosa en ayunas desde 126 mg/dL o HbA1c desde 6,5 %. Ambas alteradas en la misma muestra cumplen el criterio ADA; una sola exige repetir | Glucosa, HbA1c; síntomas clásicos | [ADA 2026, sección 2](https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes), [GPC Colombia DM2](https://colombiamedica.univalle.edu.co/index.php/comedica/article/download/2207/7056?inline=1) | D1 Directa | Incluida |
| Síndrome metabólico | 3 de 5 componentes; cintura desde 90 cm en hombres y 80 cm en mujeres para población centro y suramericana | Triglicéridos, HDL, glucosa; presión arterial y cintura medidas por la enfermera | [Declaración armonizada IDF/AHA/NHLBI 2009](https://www.ahajournals.org/doi/10.1161/circulationaha.109.192644) | D2 Con contexto | Incluida |
| Obesidad y sobrepeso | IMC desde 30 (obesidad) o desde 25 (sobrepeso); la cintura añade adiposidad central | Peso y talla medidos por la enfermera; cintura | [OMS](https://www.who.int/News-Room/Fact-Sheets/Detail/Obesity-and-Overweight) | D2 Con contexto | Incluida |
| Glucosa baja en ayunas | Menor de 70 mg/dL (alerta) y menor de 54 mg/dL (significativa). En muestra a domicilio puede ser un falso bajo por demora en procesar | Glucosa en tubo con fluoruro; síntomas, medicamentos | [Clasificación ADA de hipoglucemia](https://pmc.ncbi.nlm.nih.gov/articles/PMC10725808/table/T6.4) | D3 Señal parcial | Incluida |
| Riesgo alto de diabetes (FINDRISC) | Puntaje desde 12 obliga a medir glucosa en ayunas; con resultados normales, repetir tamizaje | Cuestionario FINDRISC adaptado a Colombia en la app | [GPC Colombia DM2](https://colombiamedica.univalle.edu.co/index.php/comedica/article/download/2207/7056?inline=1) | D2 Con contexto | Apoyo |
| Resistencia a la insulina | Ninguna guía fija umbral diagnóstico para HOMA-IR; solo refuerza síndrome metabólico y prediabetes | Insulina y glucosa en ayunas | Sin guía con umbral | D1 Directa | Apoyo |
| Diabetes tipo 1 o LADA | Clasificarla exige autoanticuerpos (anti-GAD) que no ofrecemos | Péptido C, autoanticuerpos | [ADA 2026, sección 2](https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes) | D4 Fuera de alcance | Descartada |
| Diabetes gestacional | Exige curva de tolerancia en el embarazo; fuera del alcance del chequeo | No aplica | [ADA 2026, sección 2](https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes) | D4 Fuera de alcance | Descartada |

Hígado graso metabólico y enfermedad renal diabética se evalúan en los lotes de Gastroenterología y Nefrología, con referencia cruzada a estas condiciones.

## Biomarcadores, mediciones y contexto del lote

El lote 1 necesita 11 analitos de sangre, 4 mediciones de la enfermera y un cuestionario corto. Sin las mediciones de la enfermera se pierden 4 de las 12 condiciones incluidas.

| Elemento | Tipo | Alimenta | Requisito operativo |
| --- | --- | --- | --- |
| Glucosa en ayunas | Sangre | Prediabetes, diabetes, síndrome metabólico, glucosa baja | Ayuno de 8 horas o más; tubo con fluoruro para evitar falsos bajos por demora |
| HbA1c | Sangre | Prediabetes, diabetes | Método certificado NGSP, como exige la GPC colombiana de diabetes |
| Colesterol total, HDL, triglicéridos | Sangre | Dislipidemia, síndrome metabólico, riesgo global | Ayuno confirmado para triglicéridos |
| LDL y no-HDL | Calculados o medidos | Dislipidemia, hipercolesterolemia severa | Si el laboratorio reporta LDL, ese valor manda sobre el cálculo |
| Lp(a) | Sangre | Lp(a) elevada | Una vez en la vida; el informe debe decir si es mg/dL o nmol/L |
| ApoB | Sangre | Discordancia ApoB/LDL (apoyo) | Solo con triglicéridos mayores de 200 mg/dL o diabetes |
| hs-CRP | Sangre | Inflamación de bajo grado (apoyo) | Repetir si sale alta; excluir infección reciente |
| Insulina en ayunas | Sangre | Resistencia a la insulina (apoyo) | Misma muestra que la glucosa |
| NT-proBNP | Sangre | Riesgo de insuficiencia cardiaca | Solo en personas con diabetes |
| Presión arterial | Enfermera | Hipertensión, riesgo global, síndrome metabólico | Tensiómetro oscilométrico validado y protocolo estandarizado |
| Peso, talla, cintura | Enfermera | Obesidad, síndrome metabólico, FINDRISC | Báscula calibrada y cinta con técnica estandarizada |
| Edad, sexo, embarazo, tabaquismo | Cuestionario | Todas | Obligatorios antes de interpretar |
| Antecedente familiar cardiovascular temprano | Cuestionario | Hipercolesterolemia severa, Lp(a) | Hombres menores de 55 años o mujeres menores de 65 en familiares de primer grado |
| Medicamentos y diagnósticos previos | Cuestionario | Todas | Estatinas, antihipertensivos, hipoglucemiantes, corticoides |
| FINDRISC | Cuestionario | Riesgo alto de diabetes | Versión adaptada a Colombia |
| Frecuencia cardiaca en reposo, pasos, sueño | Wearable | Contexto y lenguaje | Nunca como umbral; varía entre dispositivos |

Si la enfermera detecta presión de 130/80 mmHg o más, la GPC de hipertensión 2025 pide un estudio inicial que incluye creatinina con eGFR, uroanálisis, relación albúmina/creatinina, sodio, potasio, TSH y ácido úrico. Esos analitos se definen en los lotes de Nefrología y Tiroides.

**Candidatos a salir del kit (decisión final después de los 12 lotes):** troponina hs, mieloperoxidasa, número de partículas LDL, LDL pequeñas y densas, colesterol remanente, relación colesterol/HDL, adiponectina, leptina, lactato, fructosamina, péptido C, relación cortisol/DHEA, IL-6, TNF-alfa y longitud de telómeros. Ninguno alimenta una condición de este lote con criterio de guía.

## Registro de fuentes

Cinco de las 12 fuentes las leí completas en esta sesión; las otras 7 están confirmadas por resultados de búsqueda del sitio oficial. Las 7 se leen completas antes de escribir las fichas clínicas, y lo que no se pueda leer queda PENDIENTE.

| Fuente | Organización y año | Identificador | Verificación |
| --- | --- | --- | --- |
| [GPC hipertensión arterial primaria, actualización parcial](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/CA/gpc-actualizacion-parcial-hta-primaria-vc.pdf) | Minsalud e IETS, 2025 | Guía No. 18, tercera edición | Leída completa |
| [GPC dislipidemias, evaluación del riesgo cardiovascular](https://www.elsevier.es/es-revista-revista-colombiana-cardiologia-203-articulo-guia-practica-clinica-prevencion-deteccion-S0120563315001059) | Minsalud y CINETS, 2014 | DOI 10.1016/j.rccar.2015.04.009 | Leída completa |
| [GPC diabetes mellitus tipo 2](https://colombiamedica.univalle.edu.co/index.php/comedica/article/download/2207/7056?inline=1) | Minsalud y CINETS, 2016 | Colombia Médica 47(2) | Leída completa |
| [Focused Update de dislipidemias](https://www.escardio.org/news/news-room/congress-news/2025-focused-update-dyslipidaemias/) | ESC y EAS, 2025 | DOI 10.1093/eurheartj/ehaf190 | Leída completa |
| [Guía de manejo de dislipidemia](https://professional.heart.org/en/science-news/2026-guideline-on-the-management-of-dyslipidemia/top-things-to-know) | ACC, AHA y 9 sociedades, 2026 | DOI 10.1161/CIR.0000000000001423 | Leída completa |
| [Guía de presión arterial alta](https://www.ahajournals.org/doi/10.1161/HYP.0000000000000249) | AHA, ACC y otras, 2025 | DOI 10.1161/HYP.0000000000000249 | Solo resultado de búsqueda |
| [Standards of Care, sección 2](https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes) | ADA, 2026 | Diabetes Care 49(Supl 1):S27 | Solo resultado de búsqueda |
| [Clasificación de hipoglucemia](https://pmc.ncbi.nlm.nih.gov/articles/PMC10725808/table/T6.4) | ADA, Standards 2024, tabla 6.4 | DOI 10.2337/dc24-S006 | Solo resultado de búsqueda |
| [Perspectiva sobre tamizaje de insuficiencia cardiaca en diabetes](https://diabetesjournals.org/care/article/48/9/1465/158257/Is-Screening-for-Heart-Failure-and-Peripheral) | Diabetes Care, 2025 | Diabetes Care 48(9):1465 | Solo resultado de búsqueda |
| [Armonización del síndrome metabólico](https://www.ahajournals.org/doi/10.1161/circulationaha.109.192644) | IDF, NHLBI, AHA y otras, 2009 | DOI 10.1161/CIRCULATIONAHA.109.192644 | Solo resultado de búsqueda |
| [Obesidad y sobrepeso](https://www.who.int/News-Room/Fact-Sheets/Detail/Obesity-and-Overweight) | OMS | Nota descriptiva | Solo resultado de búsqueda |
| [Resolución 3280 de 2018](https://www.icbf.gov.co/cargues/avance/compilacion/docs/resolucion_minsaludps_3280_2018.htm) | Minsalud, 2018 | Ruta de promoción y mantenimiento de la salud | Solo resultado de búsqueda |

El umbral de hs-CRP mayor de 2 mg/L viene del texto del Focused Update ESC/EAS citado en publicaciones de la ESC; se confirma en el documento completo antes de la ficha.

## Conflictos entre guías y próximos pasos

El lote deja 6 conflictos que debe resolver el médico revisor; mi propuesta va en cada fila, y el RAG mostrará ambas posturas mientras no se decida.

| Tema | Postura A | Postura B | Propuesta |
| --- | --- | --- | --- |
| Calculadora de riesgo cardiovascular | SCORE2-PURE con factor 0,75 en mujeres y 0,61 en hombres (GPC HTA 2025) | Framingham × 0,75 (GPC dislipidemias 2014) | SCORE2-PURE como principal por ser la colombiana más reciente; válida sobre todo entre 40 y 69 años |
| Umbral de hipertensión | 130/80 mmHg confirmado con AMPA o MAPA (GPC 2025, AHA/ACC 2025) | 140/90 mmHg (criterio histórico) | 130/80, siempre como sospecha hasta confirmar |
| Lp(a) elevada | Mayor de 50 mg/dL o 105 nmol/L (ESC/EAS 2025) | Desde 125 nmol/L (ACC/AHA 2026) | Mostrar ambas; el informe declara la unidad del laboratorio |
| Cintura abdominal | 90 cm hombres y 80 cm mujeres (armonizada 2009) | 94 cm y 90 cm (FINDRISC adaptado a Colombia) | Cada umbral solo dentro de su herramienta |
| Triglicéridos y urgencia | La regla actual del KB marca urgencia desde 500 mg/dL | ACC/AHA 2026 señala 1.000 mg/dL para prevenir pancreatitis | Escalamiento 2, no urgencia; urgencia solo con síntomas o bandera crítica del laboratorio |
| Tamizaje con NT-proBNP | ADA lo recomienda en diabetes desde 125 pg/mL | Diabetes Care 2025 cuestiona su evidencia | Incluido solo en personas con diabetes y con lenguaje de señal parcial |

Requisitos para el laboratorio aliado que salen de este lote: HbA1c certificada NGSP, glucosa en tubo con fluoruro y tiempos de transporte controlados, Lp(a) con unidad explícita y LDL indicando si es medido o calculado.

- [ ] Carlos revisa la columna Decisión de cada fila y la cambia donde no esté de acuerdo
- [ ] El médico revisor resuelve los 6 conflictos de la tabla
- [ ] Leer completas las 7 fuentes marcadas como solo resultado de búsqueda
- [ ] Lote 2: Nefrología y Endocrinología de tiroides, que completan el estudio inicial de hipertensión
- [ ] Al cerrar los 12 lotes: catálogo final del kit y contrato de salida para el dashboard
