# 00_INDEX — Índice maestro del Knowledge Base de Saludly Brain

**Versión 1 · 6 de octubre de 2026 · generado automáticamente desde los archivos del Knowledge Base**

Este índice une en un solo mapa los biomarcadores, las condiciones, las reglas de seguridad y las relaciones entre módulos. Se genera con un script a partir de los encabezados de cada ficha, así que no se edita a mano: si una ficha cambia, se vuelve a generar.

## Resumen

| Pieza | Cantidad | Carpeta |
| --- | --- | --- |
| Fichas de biomarcador | 144 | `biomarcadores/` |
| Fichas de condición incluidas | 56 | `condiciones/M1` a `condiciones/M6` |
| Fichas de condición de apoyo | 30 | `condiciones/M1` a `condiciones/M6` |
| Fichas de seguridad | 15 | `seguridad/` |
| Relaciones entre módulos | 31 | `relaciones/` |
| Reglas transversales | 6 | Ver sección "Reglas transversales" |

Fichas por panel (10 de octubre de 2026): 92 del panel estándar, 24 reflejas, 17 calculadas, 10 fuera del panel base y 1 opcional. El MVP usa solo sangre: las 5 fichas de orina y heces siguen en el panel estándar, pero el motor las pone en pausa. El índice JSON ya no se edita a mano: lo genera `codigo/herramientas/generar_indice.py`. Antes del 10 de octubre: Son más fichas que analitos porque algunos analitos tienen dos fichas (por ejemplo, linfocitos absolutos y porcentaje) y algunas fichas agrupan varios campos (uroanálisis, coprológico). El catálogo sigue siendo de 99 analitos medidos, 12 calculados y la edad biológica, más 18 pruebas reflejas.

## Cambios del 10 de octubre de 2026 (aprobados por Carlos)

Detalle y razones en `docs/02_plan_y_decisiones/Propuesta_ampliacion_condiciones_sangre.md`. Todos los umbrales nuevos están marcados "por verificar" en sus fichas.

**Condiciones nuevas (10)**

| ID | Condición | Tipo | Biomarcadores que usa |
| --- | --- | --- | --- |
| COND-M1-EM-A03 | Diabetes con posible falta de insulina | apoyo | c_peptide, hba1c |
| COND-M1-EM-A04 | Resistencia a la insulina por TyG y TG/HDL | apoyo | tyg_index, tg_hdl_ratio |
| COND-M2-TI-009 | Cortisol de la mañana bajo (posible insuficiencia suprarrenal) | incluida | cortisol, acth, sodium |
| COND-M3-HE-007 | Glóbulos rojos altos (eritrocitosis) ajustados por altitud | incluida | hemoglobin, hematocrit |
| COND-M3-HE-008 | Plaquetas altas (trombocitosis) | incluida | platelets, ferritin |
| COND-M3-HE-009 | Glóbulos rojos grandes sin anemia (macrocitosis) | incluida | mcv, hemoglobin, ggt |
| COND-M3-HE-010 | Dos o más líneas de la sangre bajas | incluida | hemoglobin, neutrophils_abs, platelets |
| COND-M3-HE-A04 | Rasgo talasémico probable | apoyo | mcv, ferritin, mentzer_index, hb_electrophoresis |
| COND-M5-MU-004 | Transición a la menopausia | apoyo (informativa para la paciente) | fsh, estradiol |
| COND-M6-MI-002 | Posible proteína anormal en la sangre (gammapatía) | incluida | globulin, calcium, serum_protein_electrophoresis |

**Relaciones nuevas (4):** REL-028 SOP con perfil metabólico (patrón) · REL-029 Glóbulos rojos altos con testosterona alta (patrón) · REL-030 Inflamación por glóbulos blancos y PCR (vigilar) · REL-031 Señal autoinmune por factor reumatoide (vigilar).

**Biomarcadores nuevos (11):** factor reumatoide y grupo sanguíneo ABO/Rh (panel estándar); electroforesis de hemoglobina, electroforesis de proteínas, 17-hidroxiprogesterona, haptoglobina y anti-CCP opcional (reflejas); TyG, TG/HDL, índice de Mentzer y NLR (calculados).

**Fuera del panel base (10):** vitaminas A, E, K1, C y B1, biotina, niacina, CoQ10, índice omega-3 y relación omega-6/omega-3. La vitamina B6 queda opcional. Las fichas se conservan.

**Ajustes:** SEG-002 ya no repite el cortisol bajo cuando COND-M2-TI-009 está activa; SEG-009 no repite las proteínas alteradas cuando COND-M6-MI-002 está activa; REL-009 suma la haptoglobina; COND-M5-MU-001 pide la 17-OHP como refleja. La biotina se controla con la pregunta "¿tomas biotina?" (contexto `toma_biotina`).

## Cómo lo usa el motor

1. Lee los encabezados de las fichas de condición y de seguridad para cargar las reglas.
2. Con los resultados de un paciente, busca en la tabla de biomarcadores qué reglas usa cada valor medido.
3. Evalúa esas reglas, primero por módulo y después las relaciones entre módulos.
4. Para redactar, trae el texto de las fichas por su identificador, no por búsqueda.

## Módulos y condiciones

### M1 · Cardiometabólico

| ID | Condición | Especialidad | Tipo | Detect. | Escalamiento | Biomarcadores que usa |
| --- | --- | --- | --- | --- | --- | --- |
| COND-M1-CA-001 | Dislipidemia aterogénica | Cardiología | incluida | D1 | 1 | hdl_c, ldl_c, non_hdl_c, triglycerides |
| COND-M1-CA-002 | Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar | Cardiología | incluida | D2 | 2 | ldl_c |
| COND-M1-CA-003 | Hipertrigliceridemia | Cardiología | incluida | D1 | 1, 2, 3 | triglycerides |
| COND-M1-CA-004 | Lipoproteína(a) elevada | Cardiología | incluida | D1 | 1 | lpa |
| COND-M1-CA-005 | Riesgo cardiovascular global elevado | Cardiología | incluida | D2 | 1, 2 | hdl_c, total_cholesterol |
| COND-M1-CA-006 | Hipertensión arterial o presión elevada (sospecha) | Cardiología | incluida | D3 | 1, 2, 3 | contexto de la visita |
| COND-M1-CA-007 | Riesgo de insuficiencia cardíaca en personas con diabetes | Cardiología | incluida | D3 | 2 | nt_probnp |
| COND-M1-CA-A01 | Discordancia ApoB / LDL | Cardiología | apoyo | D1 | modifica | apob, ldl_c, triglycerides |
| COND-M1-CA-A02 | Inflamación de bajo grado | Cardiología | apoyo | D3 | modifica | hs_crp |
| COND-M1-EM-001 | Prediabetes | Endocrinología metabólica | incluida | D1 | 1 | glucose, hba1c |
| COND-M1-EM-002 | Diabetes tipo 2 en rango diagnóstico | Endocrinología metabólica | incluida | D1 | 2, 3 | glucose, hba1c |
| COND-M1-EM-003 | Síndrome metabólico | Endocrinología metabólica | incluida | D2 | 1 | glucose, hdl_c, triglycerides |
| COND-M1-EM-004 | Obesidad y sobrepeso | Endocrinología metabólica | incluida | D2 | 1, 2 | contexto de la visita |
| COND-M1-EM-005 | Glucosa baja en ayunas | Endocrinología metabólica | incluida | D3 | 1, 2, 3 | glucose |
| COND-M1-EM-A01 | Riesgo alto de diabetes por FINDRISC | Endocrinología metabólica | apoyo | D2 | modifica | contexto de la visita |
| COND-M1-EM-A02 | Resistencia a la insulina por HOMA-IR | Endocrinología metabólica | apoyo | D1 | modifica | homa_ir, insulin |

### M2 · Riñón y glándulas

| ID | Condición | Especialidad | Tipo | Detect. | Escalamiento | Biomarcadores que usa |
| --- | --- | --- | --- | --- | --- | --- |
| COND-M2-NE-001 | Enfermedad renal crónica (sospecha y estadio) | Nefrología | incluida | D1 | 1, 2, 3 | egfr, uacr |
| COND-M2-NE-002 | Albuminuria con TFG normal | Nefrología | incluida | D1 | 1, 2 | egfr, uacr |
| COND-M2-NE-003 | Daño renal asociado a diabetes o hipertensión | Nefrología | incluida | D2 | 2 | contexto de la visita |
| COND-M2-NE-004 | Potasio alto | Nefrología | incluida | D1 | 1, 2, 3 | potassium |
| COND-M2-NE-005 | Sodio bajo | Nefrología | incluida | D1 | 1, 2, 3 | sodium, total_protein, triglycerides |
| COND-M2-NE-006 | Hematuria microscópica | Nefrología | incluida | D1 | 1, 2 | egfr, uacr |
| COND-M2-NE-A01 | Potasio bajo | Nefrología | apoyo | D1 | modifica | potassium |
| COND-M2-NE-A02 | Confirmación de TFG con cistatina C | Nefrología | apoyo | D1 | modifica | egfr, uacr |
| COND-M2-NE-A03 | Bicarbonato bajo | Nefrología | apoyo | D1 | modifica | bicarbonate |
| COND-M2-TI-001 | Hipotiroidismo subclínico | Tiroides, paratiroides y suprarrenal | incluida | D1 | 1, 2 | free_t4, tsh |
| COND-M2-TI-002 | Hipotiroidismo primario | Tiroides, paratiroides y suprarrenal | incluida | D1 | 2 | free_t4, tsh |
| COND-M2-TI-003 | Sospecha de hipotiroidismo central | Tiroides, paratiroides y suprarrenal | incluida | D1 | 2 | free_t4, tsh |
| COND-M2-TI-004 | Hipertiroidismo subclínico | Tiroides, paratiroides y suprarrenal | incluida | D1 | 1, 2 | free_t3, free_t4, tsh |
| COND-M2-TI-005 | Hipertiroidismo manifiesto o T3-toxicosis | Tiroides, paratiroides y suprarrenal | incluida | D1 | 2, 3 | free_t3, free_t4, tsh |
| COND-M2-TI-006 | Disfunción tiroidea en el embarazo | Tiroides, paratiroides y suprarrenal | incluida | D2 | 2 | free_t4, tsh |
| COND-M2-TI-007 | Hiperparatiroidismo primario | Tiroides, paratiroides y suprarrenal | incluida | D1 | 2, 3 | pth |
| COND-M2-TI-008 | Hiperaldosteronismo primario (tamizaje en hipertensos) | Tiroides, paratiroides y suprarrenal | incluida | D2 | 2 | aldosterone, renin |
| COND-M2-TI-A01 | Autoinmunidad tiroidea | Tiroides, paratiroides y suprarrenal | apoyo | D1 | modifica | anti_tg, anti_tpo |

### M3 · Sangre y nutrición

| ID | Condición | Especialidad | Tipo | Detect. | Escalamiento | Biomarcadores que usa |
| --- | --- | --- | --- | --- | --- | --- |
| COND-M3-HE-001 | Anemia ajustada por altitud y tabaquismo | Hematología | incluida | D2 | 1, 2, 3 | contexto de la visita |
| COND-M3-HE-002 | Anemia por déficit de hierro | Hematología | incluida | D1 | 2 | ferritin, hs_crp, mcv, rdw, transferrin_saturation |
| COND-M3-HE-003 | Déficit de hierro sin anemia | Nutrición y micronutrientes | incluida | D1 | 1, 2 | ferritin, hs_crp |
| COND-M3-HE-004 | Anemia por déficit de B12 o folato | Hematología | incluida | D1 | 2 | folate, mcv, vitamin_b12 |
| COND-M3-HE-005 | Plaquetas bajas | Hematología | incluida | D1 | 1, 2, 3 | platelets |
| COND-M3-HE-006 | Posible sobrecarga de hierro | Hematología | incluida | D3 | 2 | ferritin, hs_crp, transferrin_saturation |
| COND-M3-HE-A01 | Anemia con perfil inflamatorio | Hematología | apoyo | D3 | modifica | ferritin, hs_crp, transferrin_saturation |
| COND-M3-HE-A02 | Leucocitos, neutrófilos o linfocitos fuera de rango | Hematología | apoyo | D1 | 1, 2, 3 | lymphocytes_abs, neutrophils_abs, wbc |
| COND-M3-HE-A03 | Eosinofilia | Hematología | apoyo | D1 | 1, 2 | eosinophils_pct, wbc |
| COND-M3-NU-001 | Déficit de vitamina B12 | Nutrición y micronutrientes | incluida | D2 | 1, 2 | methylmalonic_acid, vitamin_b12 |
| COND-M3-NU-002 | Déficit de folato | Nutrición y micronutrientes | incluida | D1 | 1, 2 | folate |
| COND-M3-NU-A01 | Homocisteína alta | Nutrición y micronutrientes | apoyo | D1 | modifica | homocysteine |
| COND-M3-NU-A02 | PTH alta con calcio normal | Nutrición y micronutrientes | apoyo | D3 | 1 | egfr, pth, vitamin_d |
| COND-M3-NU-A03 | Vitamina D baja | Nutrición y micronutrientes | apoyo | D1 | 0, 1 | vitamin_d |
| COND-M3-NU-A04 | Vitaminas informativas | Nutrición y micronutrientes | apoyo | D1 | — | biotin, coq10, niacin, omega3_index, omega6_omega3_ratio, vitamin_a, vitamin_b1, vitamin_b6, vitamin_c, vitamin_e, vitamin_k1 |

### M4 · Digestivo e infecciones

| ID | Condición | Especialidad | Tipo | Detect. | Escalamiento | Biomarcadores que usa |
| --- | --- | --- | --- | --- | --- | --- |
| COND-M4-GA-001 | Riesgo de fibrosis por hígado graso metabólico (FIB-4) | Gastroenterología y hepatología | incluida | D2 | 1, 2 | contexto de la visita |
| COND-M4-GA-002 | Alteración hepatocelular | Gastroenterología y hepatología | incluida | D1 | 1, 2, 3 | alt, ast |
| COND-M4-GA-003 | Alteración colestásica | Gastroenterología y hepatología | incluida | D1 | 1, 2 | alp, bilirubin_direct, ggt |
| COND-M4-GA-004 | Sangre oculta en heces positiva | Gastroenterología y hepatología | incluida | D3 | 2 | fit_stool |
| COND-M4-GA-005 | Infección por H. pylori | Gastroenterología y hepatología | incluida | D1 | 2 | hpylori_stool_ag |
| COND-M4-GA-006 | Enfermedad celíaca (prueba dirigida) | Gastroenterología y hepatología | incluida | D3 | 2 | anti_ttg_iga, iga |
| COND-M4-GA-A01 | Bilirrubina indirecta elevada aislada | Gastroenterología y hepatología | apoyo | D1 | — | bilirubin_direct, bilirubin_total |
| COND-M4-GA-A02 | Alteración hepática con consumo de alcohol | Gastroenterología y hepatología | apoyo | D2 | modifica | ggt |
| COND-M4-IN-001 | Hepatitis C | Infectología | incluida | D3 | 2 | anti_hcv, hcv_rna |
| COND-M4-IN-002 | Hepatitis B y estado frente a la vacuna | Infectología | incluida | D3 | — | contexto de la visita |
| COND-M4-IN-003 | Enfermedad de Chagas crónica | Infectología | incluida | D2 | 2 | chagas_elisa_recombinante, chagas_elisa_total |
| COND-M4-IN-A01 | Infección urinaria con síntomas | Infectología | apoyo | D2 | 1 | contexto de la visita |
| COND-M4-IN-A02 | Parasitosis intestinal | Infectología | apoyo | D1 | 0, 1 | contexto de la visita |

### M5 · Mujer y hombre

| ID | Condición | Especialidad | Tipo | Detect. | Escalamiento | Biomarcadores que usa |
| --- | --- | --- | --- | --- | --- | --- |
| COND-M5-MU-001 | Andrógenos altos (posible SOP) | Salud de la mujer | incluida | D3 | 1, 2 | testosterone_total |
| COND-M5-MU-002 | FSH alta en menores de 40 años | Salud de la mujer | incluida | D3 | 2 | fsh |
| COND-M5-MU-003 | Prolactina alta | Salud de la mujer | incluida | D3 | 0, 1, 2 | macroprolactin, prolactin |
| COND-M5-MU-A01 | Anemia en el embarazo | Salud de la mujer | apoyo | D2 | modifica | contexto de la visita |
| COND-M5-UR-001 | PSA elevado | Urología y salud del hombre | incluida | D3 | 1, 2 | psa_total |
| COND-M5-UR-002 | Testosterona baja | Urología y salud del hombre | incluida | D3 | 1, 2 | testosterone_total |
| COND-M5-UR-A01 | Testosterona libre calculada | Urología y salud del hombre | apoyo | D1 | modifica | contexto de la visita |
| COND-M5-UR-A02 | Relación PSA libre / total | Urología y salud del hombre | apoyo | D1 | modifica | contexto de la visita |

### M6 · Inmunidad y envejecimiento

| ID | Condición | Especialidad | Tipo | Detect. | Escalamiento | Biomarcadores que usa |
| --- | --- | --- | --- | --- | --- | --- |
| COND-M6-MI-001 | Riesgo de desnutrición | Medicina interna y envejecimiento | incluida | D2 | 1, 2 | hs_crp |
| COND-M6-MI-A01 | Lectura por edad del panel | Medicina interna y envejecimiento | apoyo | D1 | — | contexto de la visita |
| COND-M6-MI-A02 | Edad biológica (PhenoAge) | Medicina interna y envejecimiento | apoyo | D1 | 0 | phenoage, rdw |
| COND-M6-RE-001 | Ácido úrico alto sin síntomas | Reumatología | incluida | D1 | 1 | uric_acid |
| COND-M6-RE-A01 | ANA positivo | Reumatología | apoyo | D3 | 1, 2 | ana_hep2 |
| COND-M6-RE-A02 | VSG alta | Reumatología | apoyo | D1 | 1, 2 | esr, hs_crp |

## Reglas de seguridad

| ID | Grupo | Biomarcadores |
| --- | --- | --- |
| SEG-000 | Regla general para solo valor y rango | todos los de solo valor y rango |
| SEG-001 | Troponina de alta sensibilidad | hs_troponin |
| SEG-002 | Cortisol y ACTH | acth, cortisol |
| SEG-003 | IGF-1 | igf1 |
| SEG-004 | Osmolalidad | osmolality |
| SEG-005 | Eritroblastos circulantes | nrbc |
| SEG-006 | Coagulación | fibrinogen, inr, platelets, pt |
| SEG-007 | Músculo y tejidos | ck_cpk, ldh |
| SEG-008 | Electrolitos sin condición | chloride, magnesium, phosphorus |
| SEG-009 | Proteínas e inmunoglobulinas | ag_ratio, globulin, igg, igm, total_protein |
| SEG-010 | Metabolismo sin condición | c_peptide, fructosamine, nt_probnp |
| SEG-011 | Hormonas sin condición | dhea_s, estradiol, lh, progesterone |
| SEG-012 | Hemograma sin condición | basophils_pct, erythrocytes, hematocrit, mch, mchc, monocytes_pct, mpv |
| SEG-013 | Orina y heces sin condición | stool_mucus, stool_visible_blood, urinalysis_bilirubin, urinalysis_glucose, urinalysis_ketones, urinalysis_protein, urinalysis_urobilinogen |
| SEG-014 | Contexto cardiovascular y nutricional | apoa1, apob_apoa1_ratio, bun, bun_creatinine_ratio, remnant_cholesterol, tc_hdl_ratio, transferrin, zinc |

## Biomarcadores

Ordenados por panel y nombre. "Reglas" son las fichas de condición y de seguridad que usan ese biomarcador.

| biomarker_id | Nombre | Unidad | Panel | Nivel | Sexo | Estado | Reglas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| vitamin_d | 25-Hidroxivitamina D | ng/mL | estándar | vitamina | ambos | COMPLETO | COND-M3-NU-A02, COND-M3-NU-A03 |
| acth | ACTH | pg/mL | estándar | solo valor y rango | ambos | COMPLETO | SEG-002 |
| albumin | Albúmina | g/dL | estándar | con patrón | ambos | COMPLETO | COND-M2-TI-007, COND-M5-UR-A01, COND-M6-MI-A02 |
| alt | ALT (Alanina Aminotransferasa) | U/L | estándar | con patrón | ambos | COMPLETO | COND-M4-GA-002 |
| ana_hep2 | Anticuerpos antinucleares por inmunofluorescencia indirecta en células HEp-2 | título (1:x) y patrón (AC-xx) | estándar | con patrón | ambos | BORRADOR | COND-M6-RE-A01 |
| anti_hbs | Anticuerpos contra el antígeno de superficie de hepatitis B | mUI/mL | estándar | con patrón | ambos | BORRADOR | COND-M4-IN-002 |
| anti_hcv | Anticuerpos contra el virus de la hepatitis C | índice (S/CO) | estándar | con patrón | ambos | BORRADOR | COND-M4-IN-001 |
| chagas_elisa_total | Anticuerpos IgG contra Trypanosoma cruzi (ELISA de antígenos totales) | índice | estándar | con patrón | ambos | BORRADOR | COND-M4-IN-003 |
| anti_hbc | Anticuerpos totales contra el antígeno core de hepatitis B | índice | estándar | con patrón | ambos | BORRADOR | COND-M4-IN-002 |
| hpylori_stool_ag | Antígeno de Helicobacter pylori en heces | cualitativo | estándar | con patrón | ambos | BORRADOR | COND-M4-GA-005 |
| hbsag | Antígeno de superficie del virus de la hepatitis B | índice | estándar | con patrón | ambos | BORRADOR | COND-M4-IN-002 |
| psa_total | Antígeno prostático específico total | ng/mL | estándar | con patrón | hombres | BORRADOR | COND-M5-UR-001 |
| apoa1 | Apolipoproteína A1 | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-014 |
| apob | Apolipoproteína B | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-A01 |
| ast | AST (Aspartato Aminotransferasa) | U/L | estándar | con patrón | ambos | COMPLETO | COND-M4-GA-002 |
| basophils_pct | Basófilos % | % | estándar | solo valor y rango | ambos | COMPLETO | SEG-012 |
| bicarbonate | Bicarbonato / CO2 | mmol/L | estándar | con patrón | ambos | COMPLETO | COND-M2-NE-A03 |
| bilirubin_direct | Bilirrubina Directa | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M4-GA-003, COND-M4-GA-A01 |
| bilirubin_total | Bilirrubina Total | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M4-GA-A01 |
| biotin | Biotina (vitamina B7) | ng/L | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| bun | BUN / Urea | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-014 |
| calcium | Calcio Sérico | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M2-TI-007, COND-M3-NU-A02 |
| tibc | Capacidad total de fijación de hierro | µg/dL | estándar | con patrón | ambos | BORRADOR | COND-M3-HE-002, COND-M3-HE-006 |
| mchc | CHCM | g/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-012 |
| chloride | Cloro | mmol/L | estándar | solo valor y rango | ambos | COMPLETO | SEG-008 |
| coq10 | Coenzima Q10 | µg/mL | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| hdl_c | Colesterol HDL (HDL-C) | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-001, COND-M1-CA-005, COND-M1-EM-003 |
| ldl_c | Colesterol LDL (LDL-C) | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-001, COND-M1-CA-002, COND-M1-CA-A01 |
| total_cholesterol | Colesterol total | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-005 |
| stool_exam | Coprológico | cualitativo | estándar | con patrón (parásitos) y solo valor (resto) | ambos | BORRADOR | COND-M4-IN-A02, SEG-013 |
| cortisol | Cortisol | µg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-002 |
| ck_cpk | Creatina Quinasa | U/L | estándar | solo valor y rango | ambos | COMPLETO | SEG-007 |
| creatinine | Creatinina Sérica | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M2-NE-001, COND-M2-NE-A02, COND-M6-MI-A02 |
| dhea_s | DHEA-S | µg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-011 |
| eosinophils_pct | Eosinófilos % | % | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-A03 |
| erythrocytes | Eritrocitos | x10⁶/µL | estándar | solo valor y rango | ambos | COMPLETO | SEG-012 |
| estradiol | Estradiol | pg/mL | estándar | solo valor y rango | ambos | COMPLETO | SEG-011 |
| ferritin | Ferritina | ng/mL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-002, COND-M3-HE-003, COND-M3-HE-006, COND-M3-HE-A01 |
| fibrinogen | Fibrinógeno | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-006 |
| folate | Folato Sérico | ng/mL | estándar | vitamina con patrón | ambos | COMPLETO | COND-M3-HE-004, COND-M3-NU-002 |
| alp | Fosfatasa Alcalina | U/L | estándar | con patrón | ambos | COMPLETO | COND-M4-GA-003, COND-M6-MI-A02 |
| fructosamine | Fructosamina | µmol/L | estándar | solo valor y rango | ambos | COMPLETO | SEG-010 |
| fsh | FSH | mUI/mL | estándar | con patrón | mujeres | COMPLETO | COND-M5-MU-002 |
| ggt | Gamma-Glutamil Transferasa | U/L | estándar | con patrón | ambos | COMPLETO | COND-M4-GA-003, COND-M4-GA-A02 |
| glucose | Glucosa en ayunas | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M1-EM-001, COND-M1-EM-002, COND-M1-EM-003, COND-M1-EM-005, COND-M6-MI-A02 |
| hematocrit | Hematocrito | % | estándar | solo valor y rango | ambos | COMPLETO | SEG-012 |
| hemoglobin | Hemoglobina | g/dL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-001, COND-M3-HE-002, COND-M3-HE-004, COND-M5-MU-A01 |
| hba1c | Hemoglobina A1c (HbA1c) | % | estándar | con patrón | ambos | COMPLETO | COND-M1-EM-001, COND-M1-EM-002 |
| mch | Hemoglobina corpuscular media | pg | estándar | solo valor y rango (apoyo de condiciones) | ambos | BORRADOR | COND-M3-HE-002, SEG-012 |
| serum_iron | Hierro sérico | µg/dL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-002, COND-M3-HE-006 |
| homocysteine | Homocisteína | µmol/L | estándar | con patrón | ambos | COMPLETO | COND-M3-NU-A01 |
| igf1 | IGF-1 | ng/mL | estándar | solo valor y rango | ambos | PARCIAL | SEG-003 |
| igg | Inmunoglobulina G | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-009 |
| igm | Inmunoglobulina M | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-009 |
| insulin | Insulina | µUI/mL | estándar | con patrón | ambos | COMPLETO | COND-M1-EM-A02 |
| ldh | Lactato Deshidrogenasa | U/L | estándar | solo valor y rango | ambos | COMPLETO | SEG-007 |
| wbc | Leucocitos (conteo total) | x10³/µL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-A02, COND-M3-HE-A03, COND-M6-MI-A02 |
| lh | LH | mUI/mL | estándar | solo valor y rango | ambos | COMPLETO | SEG-011 |
| lymphocytes_pct | Linfocitos % | % | estándar | con patrón | ambos | COMPLETO | COND-M6-MI-A02 |
| lymphocytes_abs | Linfocitos Absolutos | x10³/µL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-A02 |
| lpa | Lipoproteína(a) | mg/dL o nmol/L (se guarda con la unidad del laboratorio, sin convertir) | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-004 |
| magnesium | Magnesio Sérico | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-008 |
| monocytes_pct | Monocitos % | % | estándar | solo valor y rango | ambos | COMPLETO | SEG-012 |
| neutrophils_pct | Neutrófilos (porcentaje) | % | estándar | solo valor y rango (apoyo de condiciones) | ambos | BORRADOR | COND-M3-HE-A02, SEG-012 |
| neutrophils_abs | Neutrófilos Absolutos | x10³/µL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-A02 |
| niacin | Niacina (vitamina B3) | µg/mL | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| nrbc | NRBC (Eritroblastos circulantes) | /100 leucocitos | estándar | solo valor y rango | ambos | COMPLETO | SEG-005 |
| osmolality | Osmolalidad Sérica | mOsm/kg | estándar | solo valor y rango | ambos | COMPLETO | SEG-004 |
| platelets | Plaquetas | x10³/µL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-005, SEG-006 |
| potassium | Potasio | mmol/L | estándar | con patrón | ambos | COMPLETO | COND-M2-NE-004, COND-M2-NE-A01 |
| progesterone | Progesterona | ng/mL | estándar | solo valor y rango | mujeres | COMPLETO | SEG-011 |
| prolactin | Prolactina | ng/mL | estándar | con patrón | mujeres | COMPLETO | COND-M5-MU-003 |
| hs_crp | Proteína C Reactiva ultrasensible (hs-CRP) | mg/L | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-A02, COND-M3-HE-002, COND-M3-HE-003, COND-M3-HE-006, COND-M3-HE-A01, COND-M6-MI-001, COND-M6-MI-A02, COND-M6-RE-A02 |
| total_protein | Proteínas totales | g/dL | estándar | con patrón | ambos | COMPLETO | COND-M2-NE-005, SEG-009 |
| c_peptide | Péptido C | ng/mL | estándar | solo valor y rango | ambos | COMPLETO | SEG-010 |
| rdw | RDW | % | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-002, COND-M6-MI-A02 |
| omega6_omega3_ratio | Relación omega-6/omega-3 | sin unidad | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| fit_stool | Sangre oculta en heces inmunoquímica | cualitativo | estándar | con patrón | ambos | BORRADOR | COND-M4-GA-004 |
| shbg | SHBG | nmol/L | estándar | con patrón | ambos | COMPLETO | COND-M5-MU-001, COND-M5-UR-002, COND-M5-UR-A01 |
| sodium | Sodio | mmol/L | estándar | con patrón | ambos | COMPLETO | COND-M2-NE-005 |
| testosterone_total | Testosterona Total | ng/dL | estándar | con patrón | ambos | COMPLETO | COND-M5-MU-001, COND-M5-UR-002 |
| pt | Tiempo de Protrombina | s | estándar | solo valor y rango | ambos | COMPLETO | SEG-006 |
| transferrin | Transferrina | mg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-014 |
| triglycerides | Triglicéridos | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M1-CA-001, COND-M1-CA-003, COND-M1-CA-A01, COND-M1-EM-003, COND-M2-NE-005 |
| hs_troponin | Troponina cardíaca de alta sensibilidad | ng/L | estándar | solo valor y rango | ambos | COMPLETO | SEG-001 |
| tsh | TSH (Hormona Estimulante de Tiroides) | µUI/mL | estándar | con patrón | ambos | COMPLETO | COND-M2-TI-001, COND-M2-TI-002, COND-M2-TI-003, COND-M2-TI-004, COND-M2-TI-005, COND-M2-TI-006 |
| uacr | UACR | mg/g | estándar | con patrón | ambos | COMPLETO | COND-M2-NE-001, COND-M2-NE-002, COND-M2-NE-006, COND-M2-NE-A02 |
| urinalysis | Uroanálisis | por campo (ver D) | estándar | con patrón (hematíes) y solo valor (resto de campos) | ambos | BORRADOR | COND-M2-NE-006, COND-M4-IN-A01, SEG-013 |
| mcv | VCM (Volumen Corpuscular Medio) | fL | estándar | con patrón | ambos | COMPLETO | COND-M3-HE-002, COND-M3-HE-004, COND-M6-MI-A02 |
| vitamin_a | Vitamina A (retinol sérico) | µg/dL | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| vitamin_b1 | Vitamina B1 (Tiamina) | nmol/L | estándar | vitamina | ambos | COMPLETO | COND-M3-NU-A04 |
| vitamin_b12 | Vitamina B12 | pg/mL | estándar | vitamina con patrón | ambos | COMPLETO | COND-M3-HE-004, COND-M3-NU-001 |
| vitamin_b6 | Vitamina B6 (PLP) | µg/L | estándar | vitamina | ambos | COMPLETO | COND-M3-NU-A04 |
| vitamin_c | Vitamina C (ácido ascórbico) | mg/dL | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| vitamin_e | Vitamina E (alfa-tocoferol) | mg/L | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| vitamin_k1 | Vitamina K1 (filoquinona) | ng/mL | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| mpv | VPM | fL | estándar | solo valor y rango | ambos | COMPLETO | SEG-012 |
| esr | VSG | mm/h | estándar | con patrón | ambos | COMPLETO | COND-M6-RE-A02 |
| zinc | Zinc Sérico | µg/dL | estándar | solo valor y rango | ambos | COMPLETO | SEG-014 |
| uric_acid | Ácido úrico | mg/dL | estándar | con patrón | ambos | COMPLETO | COND-M6-RE-001 |
| omega3_index | Índice omega-3 | % | estándar | vitamina | ambos | BORRADOR | COND-M3-NU-A04 |
| aldosterone | Aldosterona sérica o plasmática | ng/dL | refleja | refleja | ambos | BORRADOR | COND-M2-TI-008 |
| anti_ttg_iga | Anti-tTG IgA | U/mL | refleja | refleja | ambos | COMPLETO | COND-M4-GA-006 |
| anti_tpo | Anticuerpos Anti-Peroxidasa Tiroidea | UI/mL | refleja | refleja | ambos | COMPLETO | COND-M2-TI-A01 |
| anti_tg | Anticuerpos Antitiroglobulina | UI/mL | refleja | refleja | ambos | COMPLETO | COND-M2-TI-A01 |
| psa_free | Antígeno prostático específico libre | ng/mL | refleja | refleja | hombres | BORRADOR | COND-M5-UR-A02 |
| hcv_rna | ARN del virus de la hepatitis C | UI/mL | refleja | refleja | ambos | BORRADOR | COND-M4-IN-001 |
| cystatin_c | Cistatina C | mg/L | refleja | refleja | ambos | COMPLETO | COND-M2-NE-A02 |
| chagas_elisa_recombinante | ELISA de Trypanosoma cruzi con antígenos recombinantes | índice | refleja | refleja | ambos | BORRADOR | COND-M4-IN-003 |
| phosphorus | Fósforo | mg/dL | refleja | refleja | ambos | COMPLETO | SEG-008 |
| iga | Inmunoglobulina A | mg/dL | refleja | refleja | ambos | COMPLETO | COND-M4-GA-006 |
| macroprolactin | Macroprolactina (prolactina tras precipitación con PEG) | % de recuperación; prolactina monomérica en ng/mL | refleja | refleja | mujeres | BORRADOR | COND-M5-MU-003 |
| nt_probnp | NT-proBNP (Fracción N-terminal del propéptido natriurético tipo B) | pg/mL | refleja | refleja | ambos | COMPLETO | COND-M1-CA-007, SEG-010 |
| pth | PTH (Hormona Paratiroidea) | pg/mL | refleja | refleja | ambos | COMPLETO | COND-M2-TI-007, COND-M3-NU-A02 |
| renin | Renina plasmática (actividad o concentración directa) | ng/mL/h (actividad) o mU/L (concentración); se guarda con su tipo | refleja | refleja | ambos | BORRADOR | COND-M2-TI-008 |
| reticulocytes_pct | Reticulocitos % | % | refleja | refleja | ambos | COMPLETO | COND-M3-HE-001, COND-M4-GA-A01 |
| reticulocytes_abs | Reticulocitos Absolutos | x10³/µL | refleja | refleja | ambos | COMPLETO | COND-M3-HE-001, COND-M4-GA-A01 |
| free_t3 | T3 Libre (Triyodotironina libre) | pg/mL | refleja | refleja | ambos | COMPLETO | COND-M2-TI-004, COND-M2-TI-005 |
| free_t4 | T4 libre | ng/dL | refleja | refleja | ambos | COMPLETO | COND-M2-TI-001, COND-M2-TI-002, COND-M2-TI-003, COND-M2-TI-004, COND-M2-TI-005, COND-M2-TI-006 |
| methylmalonic_acid | Ácido metilmalónico sérico | µmol/L | refleja | refleja | ambos | BORRADOR | COND-M3-HE-004, COND-M3-NU-001 |
| non_hdl_c | Colesterol no-HDL | mg/dL | calculado | con patrón | ambos | COMPLETO | COND-M1-CA-001 |
| remnant_cholesterol | Colesterol remanente | mg/dL | calculado | solo valor y rango (contexto) | ambos | BORRADOR | COND-M1-CA-001, COND-M1-CA-003, SEG-014 |
| phenoage | Edad biológica (PhenoAge) | años | calculado | solo valor (pantalla aparte) | ambos | BORRADOR | COND-M6-MI-A02 |
| egfr | eGFR | mL/min/1,73 m² | calculado | con patrón | ambos | COMPLETO | COND-M2-NE-001, COND-M2-NE-002, COND-M2-NE-006, COND-M2-NE-A02, COND-M3-NU-A02 |
| globulin | Globulinas | g/dL | calculado | solo valor y rango | ambos | COMPLETO | SEG-009 |
| homa_ir | HOMA-IR | sin unidad | calculado | con patrón | ambos | COMPLETO | COND-M1-EM-A02 |
| inr | INR | sin unidad | calculado | solo valor y rango | ambos | COMPLETO | SEG-006 |
| ag_ratio | Relación Albúmina/Globulina | sin unidad | calculado | solo valor y rango | ambos | COMPLETO | SEG-009 |
| apob_apoa1_ratio | Relación ApoB/ApoA1 | sin unidad | calculado | solo valor y rango | ambos | COMPLETO | SEG-014 |
| bun_creatinine_ratio | Relación BUN/Creatinina | sin unidad | calculado | solo valor y rango | ambos | COMPLETO | SEG-014 |
| tc_hdl_ratio | Relación colesterol total/HDL | sin unidad | calculado | solo valor y rango (contexto) | ambos | BORRADOR | COND-M1-CA-001, COND-M1-CA-005, SEG-014 |
| transferrin_saturation | Saturación de transferrina | % | calculado | con patrón | ambos | COMPLETO | COND-M3-HE-002, COND-M3-HE-006, COND-M3-HE-A01 |
| testosterone_free | Testosterona Libre | pg/mL | calculado | con patrón | ambos | COMPLETO | COND-M5-UR-A01 |

## Relaciones entre módulos

| ID | Relación | Módulos | Tipo | Biomarcadores | Implementada por |
| --- | --- | --- | --- | --- | --- |
| REL-001 | Patrón cardiometabólico | M1 | patron | glucose, hba1c, insulin, homa_ir, triglycerides, hdl_c | COND-M1-EM-001, COND-M1-EM-002, COND-M1-EM-003, COND-M1-CA-003, COND-M1-EM-A02 |
| REL-002 | Patrón cardiometabólico con inflamación | M1 | vigilar | hs_crp | COND-M1-CA-A02 |
| REL-003 | Patrón aterogénico | M1 | patron | apob, ldl_c, non_hdl_c, lpa | COND-M1-CA-001, COND-M1-CA-002, COND-M1-CA-004, COND-M1-CA-A01 |
| REL-004 | Inflamación cardiovascular inespecífica | M1, M3 | vigilar | hs_crp, fibrinogen, homocysteine | — |
| REL-005 | NT-proBNP o troponina altas | M1 | fuera_de_patrones | nt_probnp, hs_troponin | COND-M1-CA-007, SEG-001, SEG-010 |
| REL-006 | Patrón hepático metabólico | M1, M4 | patron | alt, ggt, triglycerides, homa_ir, hba1c | COND-M4-GA-002, COND-M4-GA-001, COND-M1-EM-001, COND-M1-CA-003 |
| REL-007 | Inflamación sistémica inespecífica | M4, M6 | vigilar | hs_crp, esr, fibrinogen | COND-M6-RE-A02 |
| REL-008 | Patrón muscular | M4 | patron | ck_cpk, ast, ldh | SEG-007, COND-M4-GA-002 |
| REL-009 | Patrón de hemólisis | M3, M4 | patron | bilirubin_total, bilirubin_direct, ldh, hemoglobin, reticulocytes_pct, reticulocytes_abs | COND-M3-HE-001, COND-M4-GA-A01 |
| REL-010 | Daño renal: albuminuria con TFG baja | M2 | patron | uacr, egfr | COND-M2-NE-001, COND-M2-NE-003 |
| REL-011 | TFG discordante entre creatinina y cistatina C | M2 | patron | egfr, cystatin_c, creatinine | COND-M2-NE-A02 |
| REL-012 | PTH alta con TFG baja | M2, M3 | patron | pth, egfr | COND-M2-NE-001, COND-M3-NU-A02 |
| REL-013 | Patrón de déficit de hierro | M3 | patron | transferrin_saturation, ferritin, rdw, mcv, mch | COND-M3-HE-002, COND-M3-HE-003 |
| REL-014 | Anemia con perfil inflamatorio | M3 | patron | ferritin, transferrin_saturation, hs_crp, hemoglobin | COND-M3-HE-A01 |
| REL-015 | B12 o folato bajos con homocisteína alta | M3 | patron | vitamin_b12, folate, homocysteine, methylmalonic_acid | COND-M3-NU-001, COND-M3-NU-002, COND-M3-NU-A01, COND-M3-HE-004 |
| REL-016 | Hierro bajo con anticuerpos tiroideos | M2, M3 | vigilar | ferritin, anti_tpo, anti_tg | — |
| REL-017 | Patrón tiroideo autoinmune | M2 | patron | tsh, free_t4, anti_tpo, anti_tg | COND-M2-TI-001, COND-M2-TI-002, COND-M2-TI-A01 |
| REL-018 | TSH alta con colesterol, CK u homocisteína altos | M1, M2, M3 | vigilar | tsh, total_cholesterol, ldl_c, ck_cpk, homocysteine | — |
| REL-019 | TSH alterada con hierro bajo | M2, M3 | vigilar | tsh, ferritin, transferrin_saturation | — |
| REL-020 | Vitamina D baja con PTH alta y calcio o fósforo alterados | M2, M3 | patron | vitamin_d, pth, calcium, phosphorus | COND-M3-NU-A02, COND-M3-NU-A03 |
| REL-021 | Vitamina D baja con hs-CRP alta | M1, M3 | vigilar | vitamin_d, hs_crp | — |
| REL-022 | Vitamina D baja con ferritina o hemoglobina bajas | M3 | vigilar | vitamin_d, ferritin, hemoglobin | — |
| REL-023 | Cortisol alto con glucosa, presión y frecuencia cardíaca altas | M1, M2 | vigilar | cortisol, glucose, hba1c | — |
| REL-024 | Testosterona baja con SHBG y gonadotropinas alteradas | M5 | patron | testosterone_total, testosterone_free, shbg, lh | COND-M5-UR-002, COND-M5-UR-A01 |
| REL-025 | Estradiol o progesterona alterados con temperatura de muñeca | M5 | vigilar | estradiol, progesterone | — |
| REL-026 | TSH alterada con frecuencia cardíaca, sueño o actividad alterados | M2 | vigilar | tsh | — |
| REL-027 | Prolactina alta con TSH alterada o medicamentos | M2, M5 | patron | prolactin, tsh, macroprolactin | COND-M5-MU-003, COND-M2-TI-001 |

## Reglas transversales

| Regla | Dónde vive |
| --- | --- |
| Regla de vitaminas | Documento 07 y COND-M3-NU-A04 |
| Objetivos de salud | Documento 07 (sección 07.4) |
| Confusores | Documento 04 (sección 04.6) |
| Uso de wearables (Apple Watch) | Documento 08 (sección 08.3) y plan de implementación |
| Lectura por edad | COND-M6-MI-A01 |
| Frases prohibidas y escalamiento | Documento 05 |

## Controles del índice

- Biomarcadores sin ninguna regla que los use: ninguno.
- Fichas con secciones faltantes: ver el reporte de normalización.
- Decisión pendiente: el fósforo figura como refleja (Consolidado); los PDF de ejemplo lo traen en el panel estándar.
