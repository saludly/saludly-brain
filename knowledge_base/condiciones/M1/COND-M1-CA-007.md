## COND-M1-CA-007 · Riesgo de insuficiencia cardíaca en personas con diabetes

**Qué detecta.** NT-proBNP de 125 pg/mL o más en una persona con diabetes. Es una señal parcial: confirmar o descartar insuficiencia cardíaca exige un ecocardiograma, que Saludly no hace. Solo se mide en personas con diabetes.

```yaml
id: COND-M1-CA-007
nombre: Riesgo de insuficiencia cardíaca en personas con diabetes
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D3
criterios:
  - id: ntprobnp_alto
    biomarcador: nt_probnp
    condicion: ">= 125"
    unidad: pg/mL
  - id: diabetes
    condicion: "diabetes conocida declarada OR COND-M1-EM-002 activa"
regla_central: "ntprobnp_alto AND diabetes"
activacion_de_la_prueba: "refleja cuando glucosa o HbA1c están en rango de diabetes; propuesta: también cuando la enfermera registra diabetes conocida"
contexto_obligatorio: ["diabetes"]
excluye_si: []
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con TFG < 60, fibrilación auricular declarada o edad >= 75"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["edad avanzada", "fibrilación auricular", "enfermedad renal (TFG baja)", "obesidad (puede bajar el valor)"]
guias: ["ADA Standards of Care (vía Diabetes Care 2025)"]
por_verificar: "Diabetes Care 2025 cuestiona la evidencia del tamizaje; por eso queda como señal parcial."
frase_permitida: "En personas con diabetes, un valor de NT-proBNP como el tuyo es una señal para revisar la función del corazón. No es un diagnóstico: el médico puede pedir un ecocardiograma."
frases_prohibidas: ["tienes insuficiencia cardíaca", "tu corazón está fallando"]
recomendaciones_sugeridas: ["consulta médica", "control de la diabetes y la presión"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | HbA1c 7,2, glucosa 148, NT-proBNP 210 | Activa, coincidencia alta, escalamiento 2 |
| Con confusor | Diabetes conocida, NT-proBNP 180, TFG 48 | Activa, coincidencia moderada |
| Negativo | Diabetes conocida, NT-proBNP 60 | No activa |
| Sin diabetes | Sin diabetes; la prueba no se pidió | No aplica |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
