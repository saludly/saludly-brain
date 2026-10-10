## COND-M1-CA-005 · Riesgo cardiovascular global elevado

**Qué detecta.** Riesgo a 10 años de un evento cardiovascular fatal o no fatal, con SCORE2 recalibrado para Colombia (SCORE2-PURE), la calculadora que adopta la GPC colombiana de hipertensión de 2025. Se usa el algoritmo SCORE2 de la región de riesgo alto y el resultado se multiplica por 0,61 en hombres y 0,75 en mujeres, los factores del estudio PURE-Colombia (2025). Solo se calcula entre 40 y 69 años, sin diabetes ni enfermedad cardiovascular, y con todos los datos. Fuera de eso se muestran los factores de riesgo sin porcentaje.

```yaml
id: COND-M1-CA-005
nombre: Riesgo cardiovascular global elevado
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D2
entradas:
  - edad (40 a 69 años)
  - sexo
  - presion_sistolica (enfermera)
  - tabaquismo actual (enfermera)
  - total_cholesterol (mg/dL; se convierte a mmol/L dividiendo por 38,67)
  - hdl_c (mg/dL; misma conversión)
calculadora:
  modelo: "SCORE2 (SCORE2 working group, Eur Heart J 2021), coeficientes por sexo con interacciones por edad"
  region: "riesgo alto (la que usó PURE-Colombia según la mortalidad cardiovascular colombiana)"
  recalibracion_colombia: {hombres: 0.61, mujeres: 0.75, fuente: "Lopez-Lopez et al., PURE-Colombia, Eur J Prev Cardiol 2025;32:564-72"}
  verificacion: "reproduce exactamente el ejemplo publicado del artículo SCORE2 (5,9 % y 14,0 % en hombres; 4,2 % y 13,7 % en mujeres)"
  implementacion: "motor/score2.py"
categorias_provisionales:
  menores_de_50: {bajo_moderado: "< 2,5 %", alto: "2,5 a < 7,5 %", muy_alto: ">= 7,5 %"}
  de_50_a_69: {bajo_moderado: "< 5 %", alto: "5 a < 10 %", muy_alto: ">= 10 %"}
regla_central: "categoria in [alto, muy_alto]"
contexto_obligatorio: ["todas las entradas presentes", "edad entre 40 y 69"]
no_calcular_si: ["enfermedad cardiovascular establecida declarada", "diabetes conocida o HbA1c >= 6,5", "COND-M1-CA-002 activa (LDL >= 190)", "embarazo"]
coincidencia:
  alta: "regla_central con todas las entradas"
modificado_por: ["COND-M1-CA-A01", "COND-M1-CA-A02", "COND-M1-CA-004"]
escalamiento:
  alto: 1
  muy_alto: 2
nivel_lenguaje: riesgo_potencial
guias: ["GPC Colombia HTA 2025 (Minsalud e IETS)", "SCORE2 working group, Eur Heart J 2021", "PURE-Colombia, Eur J Prev Cardiol 2025"]
por_verificar: "Las categorías de riesgo son las de la ESC 2021 por edad; falta confirmar si la GPC HTA 2025 usa las mismas. En diabetes, la calculadora no aplica y decide el médico (SCORE2-Diabetes no está implementado)."
frase_permitida: "Con tu edad, presión, colesterol y hábitos, tu riesgo estimado de un evento cardiovascular en los próximos 10 años es de {riesgo} %, en la categoría {categoria}. Es una estimación de un modelo ajustado a población colombiana, no una predicción segura."
frases_prohibidas: ["vas a tener un infarto", "porcentaje de riesgo fuera de 40 a 69 años o sin datos completos"]
recomendaciones_sugeridas: ["dejar de fumar si aplica", "control de presión", "actividad física", "consulta para definir metas de colesterol"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Incompleto · PDF hombre 46 años sin datos de la enfermera | Edad 46, colesterol 228, HDL 36; falta presión y tabaquismo | No se calcula; se listan los factores y lo que falta |
| Bajo · PDF hombre 46 años con datos de la enfermera | Presión 128, no fumador, colesterol 228, HDL 36 | 2,2 %, bajo a moderado; no activa |
| Fuera de edad · PDF mujer 34 años | Edad 34 | No se calcula; se muestran factores sin porcentaje |
| Con diabetes | Edad 58, HbA1c 7,1 | No se calcula; la vista médica lo explica |
| Muy alto | Hombre 62 años, presión 152, fumador, colesterol 245, HDL 38 | 13,1 % (21,5 % antes de recalibrar), muy alto, escalamiento 2 |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
