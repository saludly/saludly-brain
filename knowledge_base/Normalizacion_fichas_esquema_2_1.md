# Normalización de las 100 fichas de biomarcador al esquema 2.1

**Saludly Brain · Knowledge Base · 6 de octubre de 2026**

Las 100 fichas de biomarcador que ya existían quedaron en el esquema 2.1, el mismo de las 33 fichas nuevas. La normalización no reescribió ni borró contenido clínico: un control automático confirmó que cada línea de texto de las fichas originales sigue presente en la versión nueva. Lo que cambió es el encabezado, el orden de las secciones y dos agregados: los campos que necesita el motor y una sección de notas de decisión.

Con esto el Knowledge Base tiene 133 fichas de biomarcador en un solo formato.

## Qué se hizo

| Cambio | Fichas |
| --- | --- |
| Encabezado unificado al esquema 2.1 (había dos formatos: 87 en el antiguo y 13 en el 2.0) | 100 |
| Secciones reordenadas de la A a la M (estaban en otro orden) | 12 |
| Secciones fusionadas porque dos encabezados originales trataban lo mismo (por ejemplo, espécimen y condiciones de toma) | 50 |
| Fichas con nota de retrofit (formato muy antiguo) | 11 |
| Campo `general_panel` (desactualizado en casi todas) reemplazado por `panel` con el catálogo aprobado | 100 |
| Campos nuevos: sinónimos, unidad canónica, tipo de resultado, espécimen, nivel en el catálogo, sexo, reglas que la usan | 100 |
| Notas de decisión por umbrales que contradicen o precisan una decisión ya tomada | 42 |

## Cómo resuelve las contradicciones

Varias fichas originales tienen umbrales distintos a los que se decidieron después en los lotes y en las fichas de condición. En vez de editar el texto original, cada una lleva al inicio una sección **Notas de decisión de Saludly** que dice cuál es el corte adoptado y en qué ficha está, más una línea con todas las reglas que usan esa ficha. La regla general es la misma en todas: si la ficha y una regla dicen cosas distintas, manda la regla. Así el RAG no le entrega al agente dos respuestas distintas.

Las contradicciones más importantes:

| Ficha | Lo que dice la ficha | Lo que se decidió |
| --- | --- | --- |
| Ferritina | Déficit con menos de 30 ng/mL | Menos de 15 (menos de 70 con inflamación); 15 a 29 es vigilar |
| Vitamina B12 | Déficit con menos de 200 pg/mL | Menos de 180; 180 a 350 indeterminado con ácido metilmalónico |
| Triglicéridos | Evaluación inmediata desde 500 mg/dL | Escalamiento 2; urgencia solo con síntomas o bandera crítica |
| Vitamina D | Deficiencia con menos de 20 ng/mL | Regla de vitaminas: bajo, en rango o alto, sin etiqueta de deficiencia |
| TSH | Zona de decisión de 4,5 a 10 | Consenso colombiano: 5,0 hasta 60 años, 6,0 después |
| Testosterona total | 240 a 950 ng/dL (Mayo 2013) | 264 ng/dL armonizado por el CDC, solo con método certificado |
| FSH | Umbral de menopausia de 30 UI/L | En menores de 40, más de 25 UI/L; desde los 45 no se usa para menopausia |
| Prolactina | Cita cortes de macroadenoma | Siempre repetir; nunca mencionar tumores al paciente |
| Relación albúmina/creatinina | Dice que la orina no está disponible en Saludly v1 | Nota obsoleta: la orina ya está en el panel estándar |
| Cortisol, ACTH, IGF-1, osmolalidad, eritroblastos | Escalar siempre | Revisión médica obligatoria; al paciente solo si el valor lo justifica |

## Huecos que quedaron a la vista

La normalización no inventa contenido, así que las secciones que faltaban siguen faltando. Ahora es fácil verlas:

| Ficha | Secciones que faltan | Qué significa |
| --- | --- | --- |
| acth | D | Sin sección propia de intervalos; los umbrales están dentro de interpretación o de fórmula |
| cortisol | D | Sin sección propia de intervalos; los umbrales están dentro de interpretación o de fórmula |
| dhea_s | E | Interpretación y umbrales venían juntas y quedaron en D |
| ferritin | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| glucose | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| hba1c | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| hdl_c | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| hemoglobin | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| hs_crp | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| hs_troponin | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| ldl_c | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| lymphocytes_pct | D, F, G, H, I, J, K | Ficha abreviada en el original por redundancia con otra; hay que completarla |
| mcv | D | Sin sección propia de intervalos; los umbrales están dentro de interpretación o de fórmula |
| non_hdl_c | D | Sin sección propia de intervalos; los umbrales están dentro de interpretación o de fórmula |
| reticulocytes_abs | F, G, H, I, J, K | Ficha abreviada en el original por redundancia con otra; hay que completarla |
| total_cholesterol | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| triglycerides | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |
| tsh | H | Sin sección de tendencias; las fichas del esquema 2.0 no la tenían |

## Inconsistencia encontrada: fósforo

Según el Consolidado, el fósforo es una prueba refleja que el laboratorio corre junto con la PTH cuando el calcio corregido sale alto. Pero los dos PDF de ejemplo lo traen en el panel estándar, porque así los armé. La ficha quedó marcada como refleja, que es lo que dice el Consolidado, con una nota. Hay que decidir cuál de las dos versiones queda: si pasa al panel estándar, el catálogo sube a 100 analitos medidos.

## Tabla completa

| Ficha | Formato original | Reordenada | Nivel en el catálogo | Panel | Notas de decisión | Reglas que la usan |
| --- | --- | --- | --- | --- | --- | --- |
| acth | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| ag_ratio | antiguo | no | solo valor y rango | calculado | 0 | 1 |
| albumin | antiguo | no | con patrón | estándar | 0 | 3 |
| alp | antiguo | no | con patrón | estándar | 0 | 2 |
| alt | antiguo | no | con patrón | estándar | 1 | 1 |
| anti_tg | antiguo | no | refleja | refleja | 0 | 1 |
| anti_tpo | antiguo | no | refleja | refleja | 0 | 1 |
| anti_ttg_iga | antiguo | no | refleja | refleja | 0 | 1 |
| apoa1 | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| apob | antiguo | no | con patrón | estándar | 1 | 1 |
| apob_apoa1_ratio | antiguo | no | solo valor y rango | calculado | 0 | 1 |
| ast | antiguo | no | con patrón | estándar | 0 | 1 |
| basophils_pct | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| bicarbonate | antiguo | no | con patrón | estándar | 0 | 1 |
| bilirubin_direct | antiguo | no | con patrón | estándar | 0 | 2 |
| bilirubin_total | antiguo | no | con patrón | estándar | 0 | 1 |
| bun | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| bun_creatinine_ratio | antiguo | no | solo valor y rango | calculado | 0 | 1 |
| c_peptide | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| calcium | antiguo | no | con patrón | estándar | 1 | 2 |
| chloride | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| ck_cpk | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| cortisol | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| creatinine | 2.0 | no | con patrón | estándar | 0 | 3 |
| cystatin_c | antiguo | no | refleja | refleja | 1 | 1 |
| dhea_s | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| egfr | 2.0 | no | con patrón | calculado | 1 | 5 |
| eosinophils_pct | antiguo | no | con patrón | estándar | 0 | 1 |
| erythrocytes | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| esr | antiguo | no | con patrón | estándar | 0 | 1 |
| estradiol | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| ferritin | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 4 |
| fibrinogen | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| folate | antiguo | no | vitamina con patrón | estándar | 1 | 2 |
| free_t3 | antiguo | no | refleja | refleja | 1 | 2 |
| free_t4 | antiguo | no | refleja | refleja | 0 | 6 |
| fructosamine | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| fsh | antiguo | no | con patrón | estándar | 1 | 1 |
| ggt | antiguo | no | con patrón | estándar | 0 | 2 |
| globulin | antiguo | no | solo valor y rango | calculado | 0 | 1 |
| glucose | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 5 |
| hba1c | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 2 |
| hdl_c | 2.0 (retrofit) | sí | con patrón | estándar | 0 | 3 |
| hematocrit | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| hemoglobin | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 4 |
| homa_ir | antiguo | no | con patrón | calculado | 1 | 1 |
| homocysteine | antiguo | no | con patrón | estándar | 1 | 1 |
| hs_crp | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 8 |
| hs_troponin | 2.0 (retrofit) | sí | solo valor y rango | estándar | 1 | 1 |
| iga | antiguo | no | refleja | refleja | 0 | 1 |
| igf1 | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| igg | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| igm | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| inr | antiguo | no | solo valor y rango | calculado | 0 | 1 |
| insulin | antiguo | no | con patrón | estándar | 0 | 1 |
| ldh | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| ldl_c | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 3 |
| lh | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| lpa | antiguo | no | con patrón | estándar | 1 | 1 |
| lymphocytes_abs | antiguo | no | con patrón | estándar | 0 | 1 |
| lymphocytes_pct | antiguo | no | con patrón | estándar | 0 | 1 |
| magnesium | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| mchc | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| mcv | antiguo | no | con patrón | estándar | 0 | 3 |
| monocytes_pct | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| mpv | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| neutrophils_abs | antiguo | no | con patrón | estándar | 0 | 1 |
| non_hdl_c | antiguo | no | con patrón | calculado | 1 | 1 |
| nrbc | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| nt_probnp | antiguo | no | refleja | refleja | 1 | 2 |
| osmolality | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| phosphorus | antiguo | no | refleja | refleja | 1 | 1 |
| platelets | antiguo | no | con patrón | estándar | 0 | 2 |
| potassium | antiguo | no | con patrón | estándar | 1 | 2 |
| progesterone | antiguo | no | solo valor y rango | estándar | 1 | 1 |
| prolactin | antiguo | no | con patrón | estándar | 1 | 1 |
| pt | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| pth | antiguo | no | refleja | refleja | 1 | 2 |
| rdw | antiguo | no | con patrón | estándar | 0 | 2 |
| reticulocytes_abs | antiguo | no | refleja | refleja | 0 | 2 |
| reticulocytes_pct | antiguo | no | refleja | refleja | 0 | 2 |
| serum_iron | antiguo | no | con patrón | estándar | 0 | 2 |
| shbg | antiguo | no | con patrón | estándar | 0 | 3 |
| sodium | antiguo | no | con patrón | estándar | 1 | 1 |
| testosterone_free | antiguo | no | con patrón | calculado | 0 | 1 |
| testosterone_total | antiguo | no | con patrón | estándar | 1 | 2 |
| total_cholesterol | 2.0 (retrofit) | sí | con patrón | estándar | 0 | 1 |
| total_protein | antiguo | no | con patrón | estándar | 0 | 2 |
| transferrin | antiguo | no | solo valor y rango | estándar | 0 | 1 |
| transferrin_saturation | antiguo | sí | con patrón | calculado | 1 | 3 |
| triglycerides | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 5 |
| tsh | 2.0 (retrofit) | sí | con patrón | estándar | 1 | 6 |
| uacr | antiguo | no | con patrón | estándar | 1 | 4 |
| uric_acid | antiguo | no | con patrón | estándar | 0 | 1 |
| vitamin_b1 | antiguo | no | vitamina | estándar | 1 | 1 |
| vitamin_b12 | antiguo | no | vitamina con patrón | estándar | 1 | 2 |
| vitamin_b6 | antiguo | no | vitamina | estándar | 1 | 1 |
| vitamin_d | antiguo | no | vitamina | estándar | 1 | 2 |
| wbc | antiguo | no | con patrón | estándar | 0 | 3 |
| zinc | antiguo | no | solo valor y rango | estándar | 0 | 1 |

## Lo que falta para que estas fichas queden COMPLETO

1. Completar las dos fichas abreviadas (linfocitos % y reticulocitos absolutos) y las secciones de intervalos que faltan en cortisol, ACTH, VCM y colesterol no-HDL.
2. Agregar la sección de tendencias en las 13 fichas que venían del esquema 2.0.
3. Que el médico revise las notas de decisión junto con las fichas de condición que ya va a firmar.
4. Decidir lo del fósforo.
