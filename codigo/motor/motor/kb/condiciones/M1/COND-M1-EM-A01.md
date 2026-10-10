## COND-M1-EM-A01 · Riesgo alto de diabetes por FINDRISC (apoyo)

**Qué detecta.** Puntaje FINDRISC de 12 o más en la versión adaptada a Colombia que aplica la enfermera. La GPC colombiana lo usa como tamizaje: con puntaje alto, se mide glucosa (en Saludly ya se mide siempre). Si la glucosa sale normal, el riesgo se mantiene y conviene repetir el tamizaje.

```yaml
id: COND-M1-EM-A01
nombre: Riesgo alto de diabetes por FINDRISC
modulo: M1
especialidad: endocrinologia_metabolica
tipo: apoyo
detectabilidad: D2
criterios:
  - id: findrisc_alto
    contexto: findrisc_puntaje
    condicion: ">= 12"
regla_central: "findrisc_alto"
modifica: ["COND-M1-EM-001"]
efecto: "Si EM-001 está activa, la refuerza en el texto. Si glucosa y HbA1c están en rango, se muestra como 'vigilar' con recomendación de repetir el tamizaje cuando indique el médico."
reglas_especiales: ["cintura con cortes de 94 y 90 cm solo dentro del puntaje FINDRISC"]
guias: ["GPC Colombia DM2 2016"]
frase_permitida: "Tus hábitos y antecedentes suman un riesgo alto de desarrollar diabetes, aunque tu glucosa hoy esté bien. Vale la pena empezar los cambios ahora."
frases_prohibidas: ["vas a tener diabetes"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza | FINDRISC 15, glucosa 108 | Refuerza EM-001 |
| Vigilar | FINDRISC 13, glucosa 88, HbA1c 5,4 | Se muestra como vigilar |
| Negativo | FINDRISC 7 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
