# Propuesta: más condiciones solo con sangre

> **Aprobada por Carlos el 10 de octubre de 2026 y construida el mismo día.** Aprobó las condiciones nuevas, los índices, las pruebas nuevas, sacar las 10 vitaminas y dejar la B6 opcional, y la pregunta "¿tomas biotina?". Los complementos pagados quedan aplazados. Lo construido: 10 fichas de condición, 4 relaciones, 11 fichas de biomarcador, sus evaluadores y 114 comprobaciones en `codigo/motor/pruebas/probar_parte5.py`. Dos ajustes al construir: los n.º 9, 11 y 12 quedaron como relaciones (REL-028, REL-029, REL-030) y el factor reumatoide alimenta una cuarta (REL-031, solo vigilar); la transición a la menopausia es un apoyo que además se le muestra a la paciente como dato informativo.

**10 de octubre de 2026.** Las decisiones clínicas (umbrales, coincidencias, escalamientos) quedan marcadas como **propuesta** hasta verificar cada fuente.

Contexto: el MVP usa solo pruebas de sangre; orina y heces quedan en pausa. Se comparó el panel de Saludly con el de Function Health y el de Superpower (consultados el 10 de octubre de 2026) y se revisó qué ofrece ECOFAM como referencia de un laboratorio clínico común en Colombia.

## Resumen

1. **¿Nuestras pruebas se parecen a las de la competencia?** Sí, el núcleo es el mismo: hemograma, química, lípidos con ApoB, tiroides, hormonas, hierro, vitamina D y PCR ultrasensible. Saludly mide **más análisis reales** que los dos. Ellos llegan a "100+" o "160+" contando cocientes calculados (Superpower calcula unos 40 de sus 101) y orina.
2. **¿Se pueden cubrir más condiciones sin más pruebas?** Sí. Hay **12 condiciones o patrones nuevos** que salen de biomarcadores que ya medimos, más **4 índices calculados** con evidencia. No suben el costo.
3. **Vitaminas.** De las 14 "vitaminas" del panel, 5 se justifican (D, B12, folato, magnesio y zinc). Las otras 9 son pruebas especializadas que ni Function ni Superpower incluyen en su panel base, y que ECOFAM en su mayoría no ofrece. Propongo **sacar 10 fichas del panel base** y dejar la B6 como opcional.
4. **Pruebas nuevas.** Solo propongo **2 baratas en el panel base** (factor reumatoide y grupo sanguíneo) y **5 reflejas** que solo se corren cuando un resultado las pide. Descarto todo lo especializado que usa la competencia (partículas de LDL, LDL oxidada, metales, genética, Galleri, leptina).
5. **Balance.** El panel base queda **más barato y más fácil de tomar**, con unas 12 condiciones más, y sigue sumando más de 100 valores si se cuentan los calculados, como lo hace la competencia.

## 1. Comparación de biomarcadores

✓ en el panel base · ＋ con costo extra · — no lo tiene

| Grupo | Saludly (MVP, sangre) | Function Health | Superpower |
|---|---|---|---|
| Hemograma completo con diferencial | ✓ | ✓ | ✓ |
| Glucosa, HbA1c, insulina | ✓ | ✓ | glucosa y HbA1c ✓; insulina — |
| Péptido C, fructosamina | ✓ | — | ＋ |
| Perfil lipídico, ApoB | ✓ | ✓ | ✓ |
| Lp(a) | ✓ | ✓ | ＋ |
| Partículas de LDL (NMR) | — | ✓ | — |
| PCR ultrasensible | ✓ | ✓ | ✓ |
| Homocisteína | ✓ | ✓ | ＋ |
| Hígado (ALT, AST, ALP, GGT, bilirrubinas, albúmina, proteínas) | ✓ | ✓ | ✓ |
| Riñón y electrolitos (creatinina, BUN, Na, K, Cl, CO2, Ca) | ✓ | ✓ | ✓ |
| Magnesio, zinc | ✓ | ✓ | ＋ (en eritrocito) |
| Amilasa, lipasa | — | ✓ | — |
| Hierro, TIBC, ferritina, transferrina | ✓ | ✓ (sin transferrina) | ✓ (sin transferrina) |
| Vitamina D | ✓ | ✓ | ✓ |
| B12 y folato | ✓ | solo ácido metilmalónico | ＋ |
| Vitaminas A, E, K1, C, B1, B6, biotina, niacina y CoQ10 | ✓ | ＋ | ＋ (algunas) |
| Ácidos grasos omega-3 y omega-6 | ✓ | ✓ | — |
| TSH, T4 libre | ✓ (T4 refleja) | ✓ | TSH, T4 total ✓ |
| T3 libre, anti-TPO, anti-Tg | refleja | ✓ | ＋ |
| Testosterona, SHBG, estradiol, DHEA-S | ✓ | ✓ | ✓ |
| FSH, LH, prolactina | ✓ | ✓ | prolactina ＋; FSH y LH — |
| Progesterona | ✓ (mujeres) | ＋ | ＋ |
| AMH (reserva ovárica) | — | ✓ (mujeres) | ＋ |
| PSA total | ✓ | ✓ | ＋ |
| PSA libre | refleja | ✓ | — |
| Cortisol | ✓ | ✓ | ✓ |
| ACTH, IGF-1 | ✓ | IGF-1 posiblemente | IGF-1 ＋ |
| ANA | ✓ | ✓ | ＋ |
| Factor reumatoide | — | ✓ | ＋ |
| Troponina de alta sensibilidad | ✓ | — | — |
| Coagulación (TP/INR, fibrinógeno) | ✓ | — | — |
| IgG, IgM | ✓ | — | — |
| CK, LDH, osmolalidad | ✓ | — | — |
| Hepatitis B y C, Chagas | ✓ | ＋ (virales) | — |
| Grupo sanguíneo ABO/Rh | — | ✓ | — |
| Plomo, mercurio | — | ✓ | ＋ (en orina) |
| Leptina | — | ✓ | ＋ |
| Edad biológica (PhenoAge) | ✓ | ✓ | ✓ |
| Cocientes calculados (NLR, TyG, AIP, Castelli y otros) | pocos | pocos | unos 40 |

**Conclusiones de la comparación**

- **Lo que solo tiene Saludly:** troponina, coagulación, inmunoglobulinas, serologías de hepatitis y Chagas, CK, LDH, péptido C, fructosamina y B12/folato directos. Son fortalezas para el mercado colombiano y para el argumento con las EPS (hepatitis y Chagas).
- **Lo que tienen ellos y vale la pena copiar barato:** factor reumatoide, grupo sanguíneo e índices calculados con evidencia (TyG, TG/HDL).
- **Lo que tienen y no conviene copiar:** partículas de LDL (la ApoB da la misma información y es barata), leptina, LDL oxidada, metales, genética, Galleri y microbioma. Son caros, especializados o sin guía.
- **Su forma de vender "100+":** cuentan cada cociente como un biomarcador. Saludly puede hacer lo mismo de forma honesta: la promesa "más de 100 biomarcadores" se cumple sumando los calculados, siempre que se diga cuáles son medidos y cuáles calculados.

## 2. Condiciones nuevas solo con sangre, sin pruebas nuevas

Todas usan biomarcadores que ya están en el panel. Los umbrales son **propuesta** y hay que confirmarlos en la fuente antes de escribir la ficha.

| # | Condición o patrón | Biomarcadores | Regla propuesta | Fuente a verificar | Tipo propuesto | Valor |
|---|---|---|---|---|---|---|
| 1 | **Eritrocitosis (glóbulos rojos altos) ajustada por altitud** | Hemoglobina, hematocrito; tabaquismo, testosterona | Hb ajustada por altitud > 16,5 g/dL en hombres o > 16,0 en mujeres, o Hct > 52 % / 48 %; se lee con tabaquismo y testosterona alta | OMS 2024 (altitud), BSH 2019 (eritrocitosis), OMS 2016 (policitemia vera) | Incluida | Alto. Hoy solo detectamos Hb baja, y en Bogotá la alta es frecuente (tabaquismo, apnea, testosterona) |
| 2 | **Plaquetas altas (trombocitosis)** | Plaquetas; ferritina, PCR | > 450 × 10³/µL; si hay déficit de hierro o inflamación, se lee como reactiva | BSH, criterios OMS de trombocitemia | Incluida | Medio-alto. Hoy solo detectamos las bajas |
| 3 | **Rasgo talasémico probable** | VCM, eritrocitos, ferritina, RDW | VCM bajo con ferritina normal e índice de Mentzer (VCM ÷ eritrocitos) < 13 | BSH, tamizaje de hemoglobinopatías | Apoyo, con refleja | Alto. Evita que se recomiende hierro a quien no le falta |
| 4 | **Glóbulos rojos grandes sin anemia (macrocitosis)** | VCM, GGT, B12, folato, TSH | VCM > 100 fL sin anemia; el patrón dice cuál explicación encaja (alcohol, B12/folato, tiroides) | BSH, macrocitosis | Patrón | Medio. Une módulos y es muy "Saludly" |
| 5 | **Dos o más líneas de la sangre bajas** | Hemoglobina, neutrófilos, plaquetas | Al menos dos de: anemia ajustada, neutrófilos < 1,5 × 10³/µL y plaquetas < 150 × 10³/µL | Criterio hematológico general | Patrón, escalamiento alto | Alto. Hoy se ven por separado |
| 6 | **Posible proteína anormal en sangre (gammapatía)** | Proteínas totales, albúmina, globulinas, A/G, IgG, IgM, calcio, creatinina, hemoglobina | Globulinas altas o A/G < 1, o IgG/IgM muy altas, más una señal adicional (anemia, calcio alto o TFG baja) | IMWG; NCCN | Patrón, con refleja | Medio. Hoy está disperso en SEG-009; en mayores de 50 tiene peso |
| 7 | **Cortisol de la mañana bajo (posible insuficiencia suprarrenal)** | Cortisol, ACTH, sodio, potasio | Cortisol entre 6:00 y 10:00 < 5 µg/dL; ACTH alta y sodio bajo o potasio alto lo refuerzan | Endocrine Society 2016 | Incluida, revisión médica | Medio. Hoy solo está en la regla de seguridad SEG-002 |
| 8 | **Diabetes con posible falta de insulina (tipo 1 o LADA)** | Glucosa, HbA1c, péptido C, insulina | Glucosa o HbA1c en rango de diabetes con péptido C bajo (< 0,6 ng/mL, por verificar) | ADA, Standards of Care 2025 | Apoyo de EM-002 | Medio. Cambia el tratamiento |
| 9 | **SOP con perfil metabólico** | Andrógenos (MU-001), HOMA-IR, glucosa, lípidos | MU-001 activa con resistencia a la insulina, prediabetes o dislipidemia | Guía internacional de SOP 2023 | Patrón | Alto en mujeres jóvenes; comercialmente atractivo |
| 10 | **Transición a la menopausia** | FSH, estradiol, edad | 45 años o más con FSH alta y estradiol bajo para la fase | STRAW+10 | Apoyo informativo | Medio-alto comercialmente. Hoy solo detectamos FSH alta en menores de 40 |
| 11 | **Glóbulos rojos altos con testosterona alta** | Hemoglobina, hematocrito, testosterona | Eritrocitosis (n.º 1) con testosterona sobre el rango, sobre todo si declara suplementos o terapia | Endocrine Society 2018 (testosterona) | Patrón | Medio. Frecuente en usuarios de gimnasio |
| 12 | **Inflamación sistémica por glóbulos blancos (NLR)** | Neutrófilos y linfocitos absolutos, PCR | Cociente neutrófilos/linfocitos alto junto con PCR alta | Asociación, no guía | Solo vigilar | Bajo clínicamente; da contexto a la inflamación |

**Índices calculados con evidencia** (cero costo, salen de lo que ya se mide):

| Índice | Fórmula | Para qué | Propuesta |
|---|---|---|---|
| **TyG** (triglicéridos y glucosa) | ln(TG × glucosa ÷ 2) | Resistencia a la insulina sin depender de la insulina; validado en población latinoamericana | Apoyo junto a HOMA-IR |
| **TG/HDL** | TG ÷ HDL (mg/dL) | Resistencia a la insulina y LDL pequeña | Apoyo |
| **Índice de Mentzer** | VCM ÷ eritrocitos | Separa déficit de hierro de rasgo talasémico | Lo usa la condición n.º 3 |
| **NLR** | Neutrófilos ÷ linfocitos | Inflamación | Solo vigilar (n.º 12) |

No recomiendo copiar los cocientes "de marketing" de Superpower (Castelli I y II, LDL/colesterol total, GGT/HDL, SII, SIRI y otros). Repiten información, no tienen guía y van contra la regla de no inventar umbrales.

**Dos ideas que necesitan datos que hoy no tenemos:** el índice de hígado graso (HSI o FLI) necesita peso, talla y cintura, y el riesgo cardiovascular SCORE2 necesita la presión. En el MVP nadie toma esos datos. Si el paciente los escribe, se activan.

## 3. Pruebas nuevas propuestas (pocas y baratas)

| Prueba | Dónde | Por qué | ¿Es común? (catálogo ECOFAM) | Recomendación |
|---|---|---|---|---|
| **Factor reumatoide** | Panel base | Function lo tiene; con ANA, VSG y PCR da un "panel autoinmune" vendible | Sí, cód. 627 ($8.000 referencial) | **Sí, pero solo como vigilar.** En personas sin síntomas su valor clínico es bajo |
| **Grupo sanguíneo ABO y Rh** | Panel base, una sola vez | Muy valorado por los usuarios; Function lo incluye | Sí, cód. 83 y 630 | **Sí.** Es dato, no condición |
| Electroforesis de hemoglobina | Refleja | Confirma el rasgo talasémico (n.º 3) | Sí, cód. 564 | Sí |
| Electroforesis de proteínas | Refleja | Confirma la gammapatía (n.º 6) | Sí, cód. 568 | Sí |
| 17-hidroxiprogesterona | Refleja | La guía de SOP 2023 pide descartar hiperplasia suprarrenal no clásica | Sí, cód. 754 | Sí |
| Haptoglobina | Refleja | Completa el patrón de hemólisis REL-009 | Sí, cód. 709 | Sí |
| Anti-CCP (péptido citrulinado) | Refleja | Solo si el factor reumatoide sale positivo | Sí, cód. 940 ($56.000 referencial) | Opcional |
| AMH (reserva ovárica) | Opcional pagada | Muy atractiva para mujeres; Function la incluye, Superpower la vende aparte | Sí, cód. 769 ($108.000 referencial) | Como complemento pagado, no en la base |

**Descartadas por caras o especializadas:** partículas de LDL (NMR), LDL oxidada, ADMA/SDMA, leptina, plomo y mercurio, metales en orina, ApoE, amiloide y pTau, Galleri, microbioma, ácidos orgánicos, micotoxinas, amilasa y lipasa (sin valor de tamizaje en personas sanas).

## 4. Las vitaminas: cuáles valen la pena

Para cada una se miró si una guía respalda medirla en personas sanas, si la ofrece un laboratorio común (ECOFAM como referencia) y si la incluyen los competidores en su panel base.

| Vitamina o nutriente | Guía para medirla en sanos | En ECOFAM | Function / Superpower (base) | Recomendación |
|---|---|---|---|---|
| **Vitamina D** | Parcial (Endocrine Society 2024 no recomienda medirla de rutina en sanos menores de 75 años) | Sí ($62.000 referencial) | ✓ / ✓ | **Mantener.** Es la más pedida por los usuarios. El texto de la recomendación lo aprueba el médico |
| **B12** | Sí, en grupos de riesgo: vegetarianos, metformina, mayores | Sí | MMA / ＋ | **Mantener**, con ácido metilmalónico como refleja |
| **Folato** | Sí, con anemia o macrocitosis | Sí | — / ＋ | **Mantener** (alimenta 3 condiciones) |
| **Magnesio** | Contexto; barato | Sí | ✓ / ＋ | **Mantener** |
| **Zinc** | Sin guía de tamizaje; requiere tubo libre de zinc | Sí | ✓ / ＋ | **Mantener por valor comercial**, sin condición propia |
| Vitamina B6 | Sin guía de tamizaje | Sí | ＋ / ＋ | **Opcional** (paquete de vitaminas pagado) |
| Vitamina B1 | Solo en riesgo (alcohol, cirugía bariátrica) | No (solo en ampolla) | ＋ / ＋ | **Quitar** |
| Vitamina A | Sin guía de tamizaje | No | ＋ / — | **Quitar** |
| Vitamina E | Sin guía de tamizaje | No | ＋ / — | **Quitar** |
| Vitamina K1 | Sin guía; el TP/INR ya refleja su función | Sí | ＋ / — | **Quitar** |
| Vitamina C | Sin guía; exige transporte congelado | Sí | ＋ / — | **Quitar.** Es el mayor problema logístico de la toma |
| Biotina | Se medía para detectar interferencias | No | — / — | **Quitar.** La regla se mantiene preguntando si toma el suplemento |
| Niacina | Sin guía | No | — / — | **Quitar** |
| Coenzima Q10 | Sin guía | No | — / — | **Quitar** |
| Índice omega-3 y relación omega-6/omega-3 | Sin guía; es una prueba especializada | No | ✓ / — | **Quitar de la base.** Opcional pagado si un laboratorio especializado lo ofrece |

**Consecuencias de quitar estas vitaminas**

- La ficha COND-M3-NU-A04 (vitaminas informativas) se reduce o desaparece.
- La regla de biotina, que bloquea TSH, T4, B12 y folato, ya no se puede activar por el valor medido. **Hay que preguntarle al paciente si toma biotina.** En el MVP el paciente solo da sus 3 objetivos, así que esa pregunta tiene que entrar en lo que llena.
- El protocolo de toma se simplifica: sin vitamina C no hay transporte congelado, y sin las vitaminas sensibles a la luz no hacen falta tubos ámbar.

## 5. El panel después de los cambios (estimado)

| | Hoy (MVP) | Con la propuesta |
|---|---|---|
| Biomarcadores medidos en el panel base | 96 | 87 (−11 vitaminas, +2 pruebas) |
| Valores calculados | 13 | 17 (+TyG, TG/HDL, Mentzer y NLR) |
| **Total en la promesa comercial** | 109 | **104** |
| Pruebas reflejas | 18 | 22 (+electroforesis de Hb y de proteínas, 17-OHP, haptoglobina) |
| Condiciones y patrones | 76 (6 en pausa) | unas 88 |
| Pruebas especializadas o congeladas | 11 | 0 |

## 6. Lo que se puede aprender de las recomendaciones de Superpower

- **Lo que hacen bien:** el plan dice qué hacer y cuándo volver a medir (repetición a los 3–6 meses con un panel más pequeño), muestra la tendencia entre tomas y usa wearables y objetivos. Es lo mismo que ya planea Saludly con los 3 objetivos y el Apple Watch.
- **Lo que Saludly no debe copiar:** su protocolo lo arma una IA y un clínico solo revisa "los casos límite"; además venden los suplementos que recomiendan, con un conflicto de interés que las reseñas critican. Usan "rangos óptimos" que no publican. Las reglas de Saludly van al revés: umbrales en código con guía, el médico decide y no se prescriben dosis. **Esa es la diferencia que hay que vender.**
- **Una idea para evaluar:** un puntaje por sistema (corazón, metabolismo, hígado…) como el "Superpower Score", pero calculado solo con las clases del motor (en rango, limítrofe, fuera de rango). Así no se inventan rangos óptimos.
- **Repetición a los 6 meses** con un panel corto (hemograma, química, lípidos, HbA1c y PCR). Function y Superpower lo hacen y es un ingreso recurrente.

## 7. Lo que necesito que apruebes

1. Las condiciones nuevas de la sección 2: todas o cuáles. Mi orden sugerido es 1, 3, 5, 9, 2, 10, 7, 6, 4, 8, 11 y 12.
2. Los índices calculados: TyG, TG/HDL, Mentzer y NLR.
3. Las pruebas nuevas: factor reumatoide y grupo sanguíneo en la base, y las 4 reflejas (más el anti-CCP opcional).
4. Sacar de la base las 10 fichas especializadas de la sección 4 y dejar la B6 como opcional.
5. Agregar la pregunta "¿tomas biotina?" a lo que llena el paciente en el MVP.
6. Si quieres ofrecer complementos pagados (AMH, paquete de vitaminas, omega-3) como hacen los competidores.

Con tu aprobación escribo las fichas, los evaluadores y sus pruebas, actualizo el PDF de solicitud al laboratorio y el documento de costos.

## Fuentes

- Function Health: functionhealth.com/what-we-test, /faq, /how-it-works y la portada.
- Superpower: superpower.com/marketplace/products/baseline-panel, /biomarkers, /blood-panel, /pricing, /how-it-works y su comparación con Function.
- Reseñas de terceros, solo como apoyo y con cifras no verificadas: healnourishgrow.com, millennialhawk.com, crowncounseling.com y bloodtestcomparison.com.
- ECOFAM: anexo de tarifas 2025, usado solo para saber si una prueba es común; los precios son referenciales.
- Las guías clínicas citadas en las secciones 2 a 4 se verifican una por una al escribir cada ficha.
