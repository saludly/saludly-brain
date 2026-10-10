## COND-M2-NE-A01 · Potasio bajo (apoyo)

**Qué detecta.** Potasio por debajo del intervalo del laboratorio. Con hipertensión orienta a hiperaldosteronismo primario o a efecto de diuréticos. Refuerza TI-008 y aparece en la vista médica de CA-006.

```yaml
id: COND-M2-NE-A01
nombre: Potasio bajo
modulo: M2
especialidad: nefrologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: k_bajo
    biomarcador: potassium
    condicion: "< límite inferior del laboratorio"
  - id: k_muy_bajo
    biomarcador: potassium
    condicion: "< 3.0"
    unidad: mmol/L
regla_central: "k_bajo"
modifica: ["COND-M2-TI-008", "COND-M1-CA-006"]
efecto: "Con hipertensión, la vista médica sugiere tamizaje de hiperaldosteronismo si no se hizo. Si k_muy_bajo, aparece como resultado observado con escalamiento 2 aunque sea apoyo."
confusores: ["diuréticos de asa o tiazídicos", "vómito o diarrea recientes", "laxantes"]
guias: ["Endocrine Society 2025, hiperaldosteronismo primario"]
por_verificar: "Mostrar k_muy_bajo con escalamiento 2 es propuesta de Saludly."
frase_permitida_medico: "Potasio bajo con presión elevada: considerar hiperaldosteronismo primario o efecto de diuréticos."
frases_prohibidas: ["tienes hiperaldosteronismo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Refuerza | Potasio 3,3, presión 146/92 | Refuerza TI-008 y CA-006 |
| Muy bajo | Potasio 2,8 | Resultado observado, escalamiento 2 |
| Con diurético | Potasio 3,4, toma hidroclorotiazida | Refuerza con nota de diurético |
| Negativo | Potasio 4,3 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
