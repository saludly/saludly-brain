# Motor de análisis · Parte 1: cálculos y clasificación · Informe de pruebas

**Saludly Brain · Fase 4 · versión 1 · 6 de octubre de 2026**

La primera parte del motor toma la salida del lector del PDF y el contexto de la visita, y hace dos cosas: le pone una clase a cada resultado y calcula los valores derivados con su trazabilidad. Todavía no busca condiciones: eso es la parte 2. Todo es código determinista; el modelo de lenguaje no interviene.

## Resultado de las pruebas: 90 de 90

| Grupo de pruebas | Comprobaciones | Resultado |
| --- | --- | --- |
| Clase de los resultados clave de los dos PDF de ejemplo | 49 | Todas correctas |
| Valores calculados frente a los esperados de los casos de punta a punta | 27 | Todos correctos |
| Reglas de contexto y límites con casos sembrados | 14 | Todas correctas |

## Clases

Cada resultado recibe una de estas clases, siguiendo el documento 04:

| Clase | Cuándo | Hombre 46 años | Mujer 34 años |
| --- | --- | --- | --- |
| En rango | Dentro del intervalo del laboratorio | 102 | 110 |
| Alto | Por encima del intervalo | 11 | 6 |
| Bajo | Por debajo del intervalo | 3 | 8 |
| Alterado | Resultado cualitativo distinto del esperado (por ejemplo, positivo cuando se espera negativo) | 1 | 1 |
| No interpretable | Resultado inválido o contexto que impide leerlo | 0 | 2 |
| Solo valor | Sin intervalo de referencia del laboratorio | 10 | 10 |
| Limítrofe | Dentro del laboratorio pero fuera de un umbral clínico de una ficha (ALT, ferritina) | 0 | 0 |
| Crítico | Bandera crítica del laboratorio o umbral de urgencia de una guía (glucosa \< 54, troponina sobre el percentil 99) | 0 | 0 |

La clase **alterado** es nueva: el contrato del documento 10 no tenía cómo clasificar un resultado cualitativo anormal. Hay que agregarla a ese documento.

## Valores calculados

| Cálculo | Hombre 46 años | Mujer 34 años |
| --- | --- | --- |
| TFG estimada (CKD-EPI 2021) | 96 | 112 |
| HOMA-IR | 5.48 | 1.3 |
| Colesterol no-HDL | 192 | 156 |
| Colesterol remanente | 50 | 20 |
| Relación colesterol total/HDL | 6.33 | 3.69 |
| Saturación de transferrina | 37 | 8.8 |
| Relación ApoB/ApoA1 | 1.05 | 0.58 |
| Globulinas | 2.7 | 2.7 |
| Relación albúmina/globulina | 1.7 | 1.59 |
| Relación BUN/creatinina | 15.3 | 13.9 |
| Calcio corregido | 9.02 | 8.96 |
| Brecha osmolar | 0.4 | 1.7 |
| Eosinófilos absolutos | 0.25 | 0.21 |
| FIB-4 | 0.89 | no se calcula: no aplica: sin enzimas alteradas, diabetes ni cintura alta con otro factor |
| Hemoglobina ajustada por altitud | 14.4 | 9.4 |
| Testosterona libre (Vermeulen) | no se calcula: no indicada: testosterona total 412 ng/dL fuera de 200 a 400, SHBG en rango e IMC sin dato | no se calcula: solo en hombres; en mujeres se usa el índice de andrógenos libres |
| Índice de andrógenos libres | no se calcula: solo en mujeres | 1.79 |
| Sodio corregido por glucosa | no se calcula: glucosa menor de 200 mg/dL: no se corrige | no se calcula: glucosa menor de 200 mg/dL: no se corrige |
| PSA libre % | no se calcula: PSA libre no medido (solo se mide con PSA total entre 4 y 10) | no se calcula: PSA libre no medido (solo se mide con PSA total entre 4 y 10) |
| IMC | no se calcula: faltan peso y talla de la enfermera | no se calcula: faltan peso y talla de la enfermera |
| Edad biológica (PhenoAge) | 44.3 | 34.1 |

Cada valor calculado guarda la fórmula y los valores de los que salió. Cuando el laboratorio ya reporta el valor (TFG, saturación, globulinas, relaciones), se usa el del laboratorio; en la TFG, además, se compara con el cálculo propio y se marca si difieren en más de 2.

## Reglas de contexto probadas

| Situación sembrada | Lo que hizo el motor |
| --- | --- |
| ALT de 31 en una mujer (laboratorio hasta 35) | Limítrofe: sobre el valor sano de la ACG |
| Ferritina de 22 | Limítrofe: zona de vigilancia 15 a 29 |
| Cortisol tomado a las 11:20 | No interpretable: fuera de 6:00 a 10:00 |
| Ayuno de 4 horas | Glucosa no interpretable y HOMA-IR no calculado |
| Suplemento de biotina declarado | TSH y B12 no interpretables hasta repetir |
| Anticonceptivo hormonal | FSH no interpretable por fase; la prolactina sí se interpreta |
| Laboratorio sin transporte congelado validado | Vitamina C no interpretable |
| Troponina de 31 ng/L | Crítico |
| Glucosa de 50 mg/dL | Crítico, con aviso de confirmar que la muestra sea confiable |
| HDL exactamente en 50 con intervalo "> 50" | Bajo (el límite es estricto) |
| Colesterol exactamente en 200 con intervalo "\< 200" | Alto (el límite es estricto) |
| Residencia en Medellín | No ajusta la hemoglobina y marca la duda: esa franja de altitud no está escrita |
| Embarazo | Prolactina no interpretable y edad biológica no calculada |
| Glucosa de 420 con sodio de 131 | Sodio corregido 136,1: no hay sodio bajo real |

## Lo que encontraron las pruebas

- **Intervalos de un solo valor.** Los eritroblastos tienen intervalo "0,0" y el motor los mostraba como "solo valor". Ahora se leen como valor esperado: 0 está en rango y cualquier valor mayor es alto.
- **Límites estrictos.** "> 50" y "\< 200" no incluyen el límite. Un HDL de exactamente 50 es bajo y un colesterol de exactamente 200 es alto.

## Supuestos y pendientes

1. **Vitamina C.** Las pruebas asumen que el laboratorio de ejemplo validó el transporte congelado. Con el laboratorio real, el motor la deja no interpretable hasta que el protocolo lo confirme; está controlado por una opción de configuración.
2. **Altitud.** Solo está escrita la franja de Bogotá (2.500 a 2.999 m). Para otras ciudades en esa misma franja, como Tunja o Pasto, también ajusta. Para ciudades por encima de 1.000 m fuera de esa franja, como Medellín, Manizales, Pereira o Popayán, no ajusta y marca la duda hasta copiar la tabla completa de la OMS 2024.
3. **Tabaquismo.** El ajuste de hemoglobina por tabaquismo sigue sin valores; el motor no lo aplica y marca la duda.
4. **Testosterona libre.** Usa la fórmula de Vermeulen con sus constantes publicadas; hay que validarla contra un calculador de referencia.
5. **Contrato del documento 10.** Agregar la clase "alterado".

## Lo que sigue

**Parte 2: las condiciones de los módulos M1 y M2.** El motor lee las 34 fichas de condición de esos módulos, evalúa sus criterios sobre las clases y los cálculos de esta parte, y asigna coincidencia y escalamiento. La prueba es que reproduzca los hallazgos esperados de M1 y M2 en los dos casos de punta a punta, más los casos unitarios de esas fichas.