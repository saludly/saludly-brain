## COND-M3-NU-A04 · Vitaminas informativas (apoyo)

**Qué detecta.** Aplica la regla de vitaminas a las 11 vitaminas sin guía de tamizaje: B1, B6, A, E, K1, C, biotina, niacina, índice omega-3, relación omega-6/omega-3 y CoQ10. Cada una se clasifica con el intervalo del laboratorio; sin intervalo ("No establecido"), solo se muestra el valor. Tiene tres reglas de seguridad propias: biotina alta, vitaminas A y E altas, y tiamina baja con síntomas neurológicos.

```yaml
id: COND-M3-NU-A04
nombre: Vitaminas informativas
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: apoyo
detectabilidad: D1
biomarcadores: [vitamin_b1, vitamin_b6, vitamin_a, vitamin_e, vitamin_k1, vitamin_c, biotin, niacin, omega3_index, omega6_omega3_ratio, coq10]
clasificacion: "intervalo del laboratorio: bajo, limítrofe (si la ficha lo define), en rango, alto; sin intervalo, solo valor"
reglas:
  bajo: "recomendación de alimentos que la aportan; suplemento solo como opción general para hablar con el médico, sin dosis"
  alto: "preguntar por suplementos"
  vitamina_a_o_e_alta: "sugerir consulta (se acumulan); escalamiento 1"
  biotina_alta: "bloquear TSH, T4 libre, T3 total, anticuerpos tiroideos, B12 y folato hasta repetir sin el suplemento; escalamiento 1"
  vitamina_c: "solo se clasifica con transporte congelado validado; si no, no interpretable"
  tiamina_baja_con_sintomas: "tiamina baja con confusión, alteraciones de la vista o de la marcha y factor de riesgo (alcohol, cirugía bariátrica, desnutrición): escalamiento 3, sospecha de urgencia"
  tiamina_baja_sin_sintomas: "recomendación alimentaria; con alcohol o cirugía bariátrica, escalamiento 1"
escalamiento_base: 0
guias: ["Regla de vitaminas (documento 07)", "FDA, interferencia de biotina en inmunoensayos", "ficha vitamin_b1 (Wernicke)"]
por_verificar: "El laboratorio debe dar intervalo para biotina; sin él la regla de biotina alta solo funciona con el suplemento declarado en el cuestionario."
frase_permitida_baja: "Tu {vitamina} está por debajo del rango. Te contamos qué alimentos la aportan; si quieres suplementarla, consúltalo con tu médico."
frase_permitida_sin_intervalo: "Este es tu valor de {vitamina}. El laboratorio no tiene un rango de referencia establecido, así que lo mostramos solo como información."
frases_prohibidas: ["tienes deficiencia de", "toma {dosis}", "compra este suplemento"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Sin intervalo · PDF ejemplos | Biotina, niacina, índice omega-3, omega-6/omega-3 y CoQ10 con "No establecido" | Solo valor, sin clase |
| No apta · PDF mujer 34 años | Vitamina C "Muestra no apta" | No interpretable |
| En rango · PDF hombre 46 años | B1, B6, A, E, K1, C en rango | Sin recomendación específica |
| Biotina declarada | Suplemento de biotina para el cabello, TSH 0,08 | Bloquea tiroides y B12; pide repetir sin el suplemento |
| Vitamina A alta | Vitamina A 112 (30 a 80) | Marcada alta, escalamiento 1 |
| Tiamina con síntomas | B1 45, alcohol diario, confusión reciente | Escalamiento 3 |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
