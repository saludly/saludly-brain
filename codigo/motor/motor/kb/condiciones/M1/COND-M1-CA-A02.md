## COND-M1-CA-A02 · Inflamación de bajo grado (apoyo)

**Qué detecta.** hs-CRP mayor de 2 mg/L sin infección reciente: modifica el riesgo cardiovascular. Una sola medición no basta; la guía pide una segunda sin infección. Por encima de 10 mg/L sugiere un proceso agudo y no se usa como riesgo cardiovascular.

```yaml
id: COND-M1-CA-A02
nombre: Inflamación de bajo grado
modulo: M1
especialidad: cardiologia
tipo: apoyo
detectabilidad: D3
criterios:
  - id: hscrp_alta
    biomarcador: hs_crp
    condicion: "> 2 AND <= 10"
    unidad: mg/L
  - id: hscrp_aguda
    biomarcador: hs_crp
    condicion: "> 10"
    unidad: mg/L
regla_central: "hscrp_alta AND NOT infeccion_reciente_2_semanas"
modifica: ["COND-M1-CA-005"]
efecto: "Vista médica: modificador de riesgo a confirmar con una segunda medición. Si hscrp_aguda, no modifica y se sugiere repetir."
confusores: ["infección o fiebre en 2 semanas", "ejercicio intenso en 48 horas", "obesidad", "tabaquismo"]
guias: ["ESC/EAS 2025 (modificador de riesgo)"]
por_verificar: "El corte de 2 mg/L viene del texto del Focused Update citado por la ESC; confirmar en el documento completo."
frase_permitida_medico: "hs-CRP de {valor} mg/L sin infección declarada: posible modificador de riesgo; repetir para confirmar."
frases_prohibidas: ["tienes inflamación", "tienes una infección"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | hs-CRP 3,4, sin infección declarada | Activa como apoyo, a confirmar |
| Con confusor | hs-CRP 4,1, infección respiratoria hace 1 semana | No activa; se sugiere repetir |
| Proceso agudo | hs-CRP 18 | No activa; se sugiere repetir |
| Negativo · PDF mujer 34 años | hs-CRP 0,8 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
