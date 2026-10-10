# Matriz de cobertura · Lote 3: Hematología y Nutrición

Oct 3, 2026 · @onova pro

Mismo método, escala de detectabilidad y jerarquía de guías del Lote 1.

## Resumen

El lote 3 deja 8 condiciones incluidas (6 de hematología y 2 de nutrición), 5 de apoyo y 7 descartadas. Con los lotes anteriores, el RAG suma 34 condiciones incluidas en 6 de las 12 especialidades.

Lo que necesito de ti:

- **Aprobar fila por fila** la columna Decisión de las dos tablas.
- **Decidir sacar la vitamina D** del kit base y su recomendación del protocolo del dashboard; la Endocrine Society 2024 no respalda ni el tamizaje ni la suplementación por encima de la ingesta recomendada en adultos sanos menores de 75 años.
- **Preguntar al laboratorio** si su intervalo de hemoglobina es de población bogotana, qué método usa para B12 y folato, y si mide TIBC directo.
- **Agregar al perfil y al cuestionario** la ciudad de residencia, cigarrillos por día, dieta, cirugías digestivas y medicamentos que bajan la B12.

Dos oportunidades de negocio. El ajuste de hemoglobina por altitud es una diferencia visible: "tu resultado, ajustado a la altura de Bogotá" es algo que un laboratorio no entrega. Y sacar los micronutrientes sin guía baja el costo del kit y deja un mensaje defendible frente a la competencia: solo medimos lo que tiene respaldo clínico.

## Hematología

Hematología queda con 6 condiciones incluidas, 3 de apoyo y 4 descartadas. El hallazgo que más pesa para Saludly: la OMS 2024 recomienda ajustar la hemoglobina por la altitud de residencia, y entre 2.500 y 2.999 metros (Bogotá) el ajuste es de 18 g/L. Sin ese ajuste, una persona bogotana con anemia puede salir "normal".

| Condición | Patrón central | Biomarcadores y contexto | Guía | Detectabilidad | Decisión |
| --- | --- | --- | --- | --- | --- |
| Anemia ajustada por altitud y tabaquismo | Hemoglobina bajo el corte OMS (130 g/L en hombres, 120 g/L en mujeres no gestantes) después de restar el ajuste por altitud y tabaquismo. No se ajusta por inflamación ni por etnia | Hemoglobina en sangre venosa; ciudad de residencia, tabaquismo, embarazo | [OMS 2024, cortes de hemoglobina](https://www.ncbi.nlm.nih.gov/books/NBK602185/) | D2 Con contexto | Incluida |
| Anemia por déficit de hierro | Anemia con ferritina menor de 15 µg/L, o menor de 70 µg/L si hay inflamación; VCM bajo y RDW alto la refuerzan | Hemograma, ferritina, hs-CRP, saturación de transferrina; menstruación, dieta | [OMS 2020, ferritina](https://www.who.int/tools/elena/interventions/ferritin-concentrations) | D1 Directa | Incluida |
| Déficit de hierro sin anemia | Ferritina baja con hemoglobina normal; la OMS indica usar ferritina para diagnosticar déficit en personas aparentemente sanas | Ferritina, hs-CRP, hemoglobina | [OMS 2020, ferritina](https://www.who.int/tools/elena/interventions/ferritin-concentrations) | D1 Directa | Incluida |
| Anemia por déficit de B12 o folato | Anemia con VCM alto y B12 total menor de 180 ng/L o folato sérico menor de 4 ng/mL | Hemograma, B12, folato | [NICE NG239 2024](https://www.nice.org.uk/guidance/ng239/resources/vitamin-b12-deficiency-in-over-16s-diagnosis-and-management-pdf-66143904531397), [OMS, folato](https://extranet.who.int/indcat/TemplateView.aspx?id=32) | D1 Directa | Incluida |
| Plaquetas bajas | Menos de 100 × 10⁹/L sin otra causa define trombocitopenia inmune; repetir antes de escalar | Plaquetas; medicamentos, infección reciente | [Consenso internacional de PTI 2019](https://experts.mcmaster.ca/scholarly-works/1680471) | D1 Directa | Incluida |
| Posible sobrecarga de hierro (hemocromatosis) | Saturación de transferrina mayor de 45 % con ferritina mayor de 200 µg/L en mujeres, o mayor de 50 % con ferritina mayor de 300 µg/L en hombres y posmenopáusicas. Confirmar exige prueba genética | Ferritina, hierro sérico, transferrina o TIBC | [EASL 2022](https://easl.eu/wp-content/uploads/2022/06/PIIS01688278220021121.pdf), [OMS 2020, ferritina](https://www.who.int/tools/elena/interventions/ferritin-concentrations) | D3 Señal parcial | Incluida |
| Anemia con perfil inflamatorio | Anemia con ferritina normal o alta, saturación de transferrina baja y hs-CRP alta; orienta a una enfermedad de fondo, no a falta de hierro | Hemograma, ferritina, saturación de transferrina, hs-CRP | [OMS 2020, ferritina](https://www.who.int/tools/elena/interventions/ferritin-concentrations) | D3 Señal parcial | Apoyo |
| Leucocitos, neutrófilos o linfocitos fuera de rango | Sin umbral de guía verificado para tamizaje; se interpreta con el intervalo del laboratorio y su bandera crítica | Hemograma con diferencial | Intervalo del laboratorio | D1 Directa | Apoyo |
| Eosinofilia | Se cruza con parasitosis del coprológico (lote de Gastroenterología e Infectología) | Eosinófilos | Intervalo del laboratorio | D1 Directa | Apoyo |
| Hemólisis | Exige haptoglobina, que el catálogo no tiene | No ofrecido | KB actual, RISK-012 | D3 Señal parcial | Descartada |
| Rasgo talásemico o hemoglobinopatía | Exige electroforesis de hemoglobina; sin umbral de tamizaje verificado | No ofrecido | Pendiente de fuente | D3 Señal parcial | Descartada |
| Hemoglobina alta (eritrocitosis) | En Bogotá la altitud la eleva; confirmar exige pruebas que no ofrecemos | Hemoglobina; altitud, tabaquismo | [OMS 2024, cortes de hemoglobina](https://www.ncbi.nlm.nih.gov/books/NBK602185/) | D3 Señal parcial | Descartada |
| Alteración de la coagulación (TP, INR) | No es un hallazgo preventivo; sale del kit | TP, INR | KB actual, RISK-015 | D4 Fuera de alcance | Descartada |

La OMS también pide sangre venosa y analizador automatizado para medir hemoglobina; los dispositivos de punción capilar no son equivalentes. Eso descarta las pruebas rápidas en casa como sustituto del hemograma.

## Nutrición y micronutrientes

Nutrición queda con solo 2 condiciones incluidas, 2 de apoyo y 3 descartadas, y es a propósito: la mayoría de micronutrientes que venden los paneles tipo Function Health no tienen una guía que respalde su tamizaje en adultos sanos. La Endocrine Society 2024 recomienda no medir vitamina D de rutina y no define un nivel de suficiencia.

| Condición | Patrón central | Biomarcadores y contexto | Guía | Detectabilidad | Decisión |
| --- | --- | --- | --- | --- | --- |
| Déficit de vitamina B12 (con o sin anemia) | B12 total menor de 180 ng/L confirma; 180–350 es indeterminado. Se mide si hay al menos un síntoma y un factor de riesgo; la ausencia de anemia no lo descarta | B12 total; metformina, inhibidores de bomba de protones, dieta vegana, cirugía bariátrica, autoinmunidad, síntomas | [NICE NG239 2024](https://www.nice.org.uk/guidance/ng239/resources/vitamin-b12-deficiency-in-over-16s-diagnosis-and-management-pdf-66143904531397) | D2 Con contexto | Incluida |
| Déficit de folato | Folato sérico menor de 4 ng/mL (10 nmol/L) indica posible déficit; menor de 3 ng/mL, déficit con impacto hematológico. Los cortes dependen del método del laboratorio | Folato sérico; dieta, alcohol, embarazo | [OMS, folato](https://extranet.who.int/indcat/TemplateView.aspx?id=32) | D1 Directa | Incluida |
| Homocisteína alta | Marcador funcional de déficit de B12 o folato; NICE pide interpretarla con el intervalo del laboratorio y descartar déficit de folato | Homocisteína, B12, folato, creatinina | [NICE NG239 2024](https://www.nice.org.uk/guidance/ng239/resources/vitamin-b12-deficiency-in-over-16s-diagnosis-and-management-pdf-66143904531397) | D1 Directa | Apoyo |
| PTH alta con calcio normal | Antes de pensar en hiperparatiroidismo normocalcémico hay que descartar causas secundarias como el déficit de vitamina D: la vitamina D entra solo aquí, como prueba refleja | PTH, calcio, vitamina D refleja, creatinina | [Quinto Taller Internacional 2022](https://academic.oup.com/jbmr/article/37/11/2293/7512381) | D3 Señal parcial | Apoyo |
| Déficit de vitamina D como tamizaje | La Endocrine Society 2024 recomienda no medirla de rutina en ninguna población estudiada y no fija niveles de suficiencia | Vitamina D | [Endocrine Society 2024](https://endocrine.org/news-and-advocacy/news-room/2024/endocrine-society-recommends-healthy-adults-take-the-recommended-daily-allowance-of-vitamin-d) | D1 Directa | Apoyo |
| Déficit de zinc, magnesio, selenio, cobre o yodo | Sin guía verificada que respalde su tamizaje en adultos sanos | No se incluyen en el kit | Sin guía de tamizaje | D1 Directa | Descartada |
| Desnutrición | Se evalúa en el lote de Medicina interna y envejecimiento con criterios clínicos (peso, IMC, pérdida de peso) | Peso y talla de la enfermera; cuestionario | Lote de Medicina interna | D2 Con contexto | Apoyo |

Esta sección tiene una consecuencia directa en el producto: el protocolo de ejemplo del dashboard recomienda 2.000 UI de vitamina D3 con su producto a la venta. La Endocrine Society 2024 desaconseja suplementar por encima de la ingesta diaria recomendada en adultos sanos menores de 75 años, así que esa recomendación debe salir. Actualización del 3 de octubre: por decisión de Carlos, las vitaminas B1, B6, A, E, K1, C, biotina, niacina, omega-3 y CoQ10 entran al panel como informativas, sin etiqueta de deficiencia ni recomendación de suplementos (ver Lote 6); la homocisteína también entra, porque la cadena de frío a 2 °C cubre su requisito. Los minerales de la fila anterior siguen fuera.

## Biomarcadores, muestras y contexto del lote

El lote 3 se resuelve con un hemograma, un perfil de hierro y dos vitaminas; la mayor ganancia viene del contexto (ciudad, tabaquismo, medicamentos y dieta), no de agregar analitos.

| Elemento | Tipo | Alimenta | Requisito operativo |
| --- | --- | --- | --- |
| Hemograma completo con diferencial | Sangre venosa (EDTA) | Anemias, plaquetas, leucocitos | Analizador automatizado; la OMS no acepta punción capilar como equivalente |
| Ferritina | Sangre | Déficit y sobrecarga de hierro | Siempre junto con hs-CRP de la misma muestra |
| Hierro sérico y transferrina o TIBC | Sangre | Saturación de transferrina, sobrecarga de hierro | El laboratorio debe decir si mide TIBC directo o lo calcula desde transferrina |
| hs-CRP | Sangre | Interpretación de ferritina; ya entra por el lote 1 | Doble uso, sin costo adicional |
| Vitamina B12 total | Sangre, condicional | Déficit de B12 | Solo con síntoma y factor de riesgo, como pide NICE |
| Folato sérico | Sangre | Déficit de folato | El laboratorio debe declarar el método, porque el corte cambia con él |
| Homocisteína | Sangre, apoyo | Confirmación funcional de B12 o folato | Muestra refrigerada y procesada en pocas horas; difícil en toma domiciliaria |
| Reticulocitos | Sangre, refleja | Clasificación de anemia | Solo si hay anemia |
| Ácido metilmalónico | Sangre, refleja | B12 indeterminada con síntomas | Solo si el laboratorio lo ofrece |
| Vitamina D | Sangre, refleja | PTH alta con calcio normal | Nunca como tamizaje |
| Ciudad de residencia | Perfil de la app | Ajuste de hemoglobina por altitud | La OMS ajusta por la residencia, no por el lugar de la toma; confirmar en el perfil |
| Tabaquismo y cigarrillos por día | Cuestionario | Ajuste de hemoglobina | La OMS ajusta por cantidad diaria |
| Embarazo, menstruación abundante, dieta vegana o vegetariana | Cuestionario | Anemia, hierro, B12 | Obligatorios en mujeres en edad fértil |
| Metformina, inhibidores de bomba de protones, anti-H2, anticonceptivos orales | Cuestionario | B12 | Los anticonceptivos bajan la B12 total sin déficit real (NICE) |
| Suplementos de B12 o hierro | Cuestionario | B12, ferritina | Pueden subir el valor sin corregir el déficit |
| Cirugía bariátrica o gástrica previa | Cuestionario | B12, hierro | Factor de riesgo directo |

La altitud debe vivir en el perfil del paciente: la app ya conoce la dirección de la visita, así que el ajuste de hemoglobina puede ser automático y es una diferencia visible frente a un laboratorio que entrega el resultado sin contexto.

**Candidatos a salir del kit:** vitamina D como tamizaje, zinc, magnesio eritrocitario, vitaminas B1, B6, A, E, K1 y C, biotina, niacina, selenio, cobre, yodo, índice omega-3, relación omega-6/omega-3, coenzima Q10, NRBC, basófilos y VPM como hallazgos aislados. Ninguno alimenta una condición de este lote con criterio de guía.

## Registro de fuentes

Tres de las 8 fuentes las abrí en el documento oficial; las otras 5 están confirmadas por resultados de búsqueda. Mismo criterio de "leída" que en el Lote 2.

| Fuente | Organización y año | Identificador | Verificación |
| --- | --- | --- | --- |
| [Cortes de hemoglobina para definir anemia](https://www.ncbi.nlm.nih.gov/books/NBK602185/) | OMS, 2024 | NCBI Bookshelf NBK602185 | Leída completa |
| [Uso de ferritina para evaluar el estado de hierro](https://www.who.int/tools/elena/interventions/ferritin-concentrations) | OMS, 2020 | Biblioteca eLENA | Leída completa |
| [Déficit de vitamina B12 en mayores de 16 años](https://www.nice.org.uk/guidance/ng239/resources/vitamin-b12-deficiency-in-over-16s-diagnosis-and-management-pdf-66143904531397) | NICE, 2024 | NG239 | Leída completa |
| [Folato sérico como indicador del estado de folato](https://extranet.who.int/indcat/TemplateView.aspx?id=32) | OMS | Catálogo de indicadores de micronutrientes | Solo resultado de búsqueda |
| [Vitamina D para la prevención de enfermedades](https://endocrine.org/news-and-advocacy/news-room/2024/endocrine-society-recommends-healthy-adults-take-the-recommended-daily-allowance-of-vitamin-d) | Endocrine Society, 2024 | JCEM 109(8):1907–1947 | Solo resultado de búsqueda |
| [Guías de práctica clínica de hemocromatosis](https://easl.eu/wp-content/uploads/2022/06/PIIS01688278220021121.pdf) | EASL, 2022 | DOI 10.1016/j.jhep.2022.03.033 | Solo resultado de búsqueda |
| [Consenso internacional de trombocitopenia inmune primaria](https://experts.mcmaster.ca/scholarly-works/1680471) | Panel internacional, 2019 | DOI 10.1182/bloodadvances.2019000812 | Solo resultado de búsqueda |
| [Hiperparatiroidismo primario, Quinto Taller Internacional](https://academic.oup.com/jbmr/article/37/11/2293/7512381) | Taller Internacional, 2022 | DOI 10.1002/jbmr.4677 | Solo resultado de búsqueda |

## Conflictos entre guías y próximos pasos

El lote deja 5 conflictos para el médico revisor; el más urgente es el de la altitud, porque cambia quién sale con anemia en Bogotá.

| Tema | Postura A | Postura B | Propuesta |
| --- | --- | --- | --- |
| Anemia en altura | Ajuste OMS 2024 de 18 g/L entre 2.500 y 2.999 metros | Intervalo de referencia del laboratorio, que puede estar derivado de población bogotana | Si el intervalo del laboratorio es propio de Bogotá, usarlo sin ajustar dos veces; si no, aplicar el ajuste OMS |
| Inflamación y ferritina | Ferritina menor de 15 µg/L en personas sanas | Menor de 70 µg/L si hay inflamación; la OMS no fija el corte de hs-CRP que la define | Usar hs-CRP mayor de 5 mg/L como bandera de inflamación hasta que el médico lo valide |
| Cortes de B12 | NICE: 180 y 350 ng/L | Cortes validados por el laboratorio para su método; NICE advierte que personas de etnia negra pueden tener rangos más altos | Cortes NICE salvo que el laboratorio valide los suyos |
| Vitamina D | El dashboard de ejemplo usa 30–80 ng/mL como rango "óptimo" | Endocrine Society 2024: no medir de rutina y sin nivel de suficiencia | Sacarla del kit base y del protocolo; solo prueba refleja con PTH alta |
| Sobrecarga de hierro | OMS 2020: ferritina mayor de 150 o 200 µg/L como riesgo | EASL 2022: ferritina más saturación de transferrina para indicar prueba genética | Ferritina sola como alerta; ferritina más saturación para remitir |

- [x] Carlos revisa la columna Decisión de Hematología y de Nutrición
- [ ] Decidir sacar la vitamina D del kit base y su recomendación del protocolo del dashboard
- [ ] Preguntar al laboratorio si su intervalo de hemoglobina es de población bogotana, qué método usa para B12 y folato, y si mide TIBC directo
- [ ] El médico revisor resuelve los 5 conflictos
- [ ] Leer completas las 5 fuentes marcadas como solo resultado de búsqueda
- [ ] Lote 4: Gastroenterología y hepatología con Infectología, que comparten heces, orina y hepatitis
