## COND-M4-GA-A02 · Alteración hepática con consumo de alcohol (apoyo)

**Qué detecta.** Transaminasas o GGT alteradas en una persona que declara consumo de alcohol. Una AST que supera claramente a la ALT con GGT alta orienta a alcohol. Refuerza GA-001 y GA-002 y cambia el foco de las recomendaciones.

```yaml
id: COND-M4-GA-A02
nombre: Alteración hepática con consumo de alcohol
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: apoyo
detectabilidad: D2
criterios:
  - id: alcohol
    contexto: cuestionario
    condicion: "consumo de alcohol declarado por encima del límite que defina el médico"
  - id: ast_mayor_alt
    condicion: "AST / ALT >= 2"
  - id: ggt_alta
    biomarcador: ggt
    condicion: "> límite superior"
regla_central: "alcohol AND (ggt_alta OR COND-M4-GA-002 activa)"
modifica: ["COND-M4-GA-001", "COND-M4-GA-002", "COND-M1-CA-003"]
efecto: "La recomendación principal pasa a reducir el alcohol; si ast_mayor_alt, la vista médica lo destaca."
guias: ["ACG 2017"]
por_verificar: "Falta definir con el médico el cuestionario de alcohol y el límite de consumo."
frase_permitida: "Tus pruebas del hígado muestran cambios que se relacionan con el consumo de alcohol. Reducirlo es lo que más le ayuda a tu hígado."
frases_prohibidas: ["eres alcohólico", "tienes cirrosis", "tienes hepatitis alcohólica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Alcohol diario, AST 92, ALT 40, GGT 210 | Activa; destaca AST/ALT de 2,3 |
| Solo GGT | Alcohol los fines de semana, GGT 88 | Activa |
| Sin alcohol · PDF hombre 46 años | Sin dato de alcohol (lo pregunta la enfermera), GGT 72 | No activa hasta tener el dato |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
