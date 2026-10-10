## COND-M2-NE-003 · Daño renal asociado a diabetes o hipertensión

**Qué detecta.** Albuminuria o TFG baja en una persona con diabetes o hipertensión. Cuando se activa, reemplaza a NE-001 o NE-002 en el informe del paciente y conserva su estadio. Ambas GPC colombianas exigen confirmar persistencia.

```yaml
id: COND-M2-NE-003
nombre: Daño renal asociado a diabetes o hipertensión
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D2
criterios:
  - id: hallazgo_renal
    condicion: "criterios de COND-M2-NE-001 OR COND-M2-NE-002 cumplidos"
  - id: diabetes
    condicion: "diabetes conocida declarada OR COND-M1-EM-002 activa"
  - id: hipertension
    condicion: "hipertensión conocida declarada OR COND-M1-CA-006 con coincidencia alta"
regla_central: "hallazgo_renal AND (diabetes OR hipertension)"
hereda: ["estadio G y A de NE-001 o NE-002"]
coincidencia:
  alta: "regla_central con hallazgo renal confirmado"
  moderada: "regla_central con hallazgo renal en una sola toma"
  baja: "hallazgo_renal con CA-006 de coincidencia moderada (se muestra como vigilar en la vista médica)"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["GPC Colombia DM2 2016", "GPC Colombia HTA 2025", "KDIGO 2024"]
frase_permitida: "Tu orina o tu filtración renal muestran una señal que, en personas con {diabetes o presión alta}, merece atención. Conviene confirmarla y revisarla con tu médico en las próximas semanas."
frases_prohibidas: ["la diabetes te dañó los riñones", "tienes nefropatía diabética"]
recomendaciones_sugeridas: ["consulta médica", "control estricto de presión y glucosa", "reducir sal"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Diabetes conocida, albúmina/creatinina 85, TFG 74 | Activa, coincidencia moderada, A2, escalamiento 2; NE-002 no aparece en el informe del paciente |
| Hipertensión conocida | Toma antihipertensivo, TFG 54, albúmina/creatinina 20 | Activa, G3a, escalamiento 2 |
| Vigilar · PDF hombre 46 años con presión 134/84 sin automonitoreo | Albúmina/creatinina 45, CA-006 moderada | No activa; NE-002 sigue; vista médica marca vigilar |
| Negativo | Sin diabetes ni hipertensión, albúmina/creatinina 45 | No activa (manda NE-002) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
