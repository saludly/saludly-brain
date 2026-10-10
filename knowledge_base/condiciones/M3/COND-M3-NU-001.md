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

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
