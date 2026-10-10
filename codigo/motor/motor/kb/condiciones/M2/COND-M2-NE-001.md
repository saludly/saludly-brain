## COND-M2-NE-001 · Enfermedad renal crónica (sospecha y estadio)

**Qué detecta.** TFG estimada menor de 60 mL/min/1,73 m², o albuminuria de 30 mg/g o más que persiste 3 meses o más. Con una sola toma es sospecha. Se informa el estadio KDIGO (G y A) para el médico.

```yaml
id: COND-M2-NE-001
nombre: Enfermedad renal crónica (sospecha y estadio)
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: tfg_baja
    biomarcador: egfr
    condicion: "< 60"
    unidad: mL/min/1,73 m²
    calculo: "CKD-EPI 2021 con creatinina; si hay cistatina C, CKD-EPI 2021 creatinina-cistatina (NE-A02)"
  - id: albuminuria_persistente
    biomarcador: uacr
    condicion: ">= 30 en dos mediciones separadas 3 meses o más"
    unidad: mg/g
estadios:
  G: {G1: ">= 90", G2: "60-89", G3a: "45-59", G3b: "30-44", G4: "15-29", G5: "< 15"}
  A: {A1: "< 30", A2: "30-300", A3: "> 300"}
regla_central: "tfg_baja OR albuminuria_persistente"
contexto_obligatorio: ["edad", "sexo"]
excluye_si: ["COND-M2-NE-003"]
coincidencia:
  alta: "tfg_baja confirmada a 3 meses OR albuminuria_persistente"
  moderada: "tfg_baja en una sola toma (a confirmar)"
  baja: "tfg_baja en 45-59 sin albuminuria y cistatina C combinada >= 60 (NE-A02 no confirma)"
escalamiento:
  G3a_con_A1: 1
  G3a_con_A2_o_A3: 2
  G3b: 2
  G4_o_G5: 3
  bandera_critica_creatinina: 3
modificado_por: ["COND-M2-NE-A02", "COND-M2-NE-A03"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["masa muscular extrema (NE-A02)", "deshidratación", "ejercicio intenso 48 h", "suplementos de creatina", "dieta muy alta en proteína"]
guias: ["KDIGO 2024", "GPC Colombia HTA 2025"]
por_verificar: "Los niveles de escalamiento por estadio son propuesta de Saludly basada en el mapa de riesgo de KDIGO, no una regla de la guía."
frase_permitida: "Tu filtración renal estimada está por debajo de 60. Un solo resultado no confirma enfermedad renal crónica: hay que repetirlo y revisarlo con tu médico."
frases_prohibidas: ["tienes enfermedad renal", "tus riñones están fallando", "vas a necesitar diálisis"]
recomendaciones_sugeridas: ["repetir creatinina y albúmina/creatinina en 3 meses", "reducir sal", "evitar antiinflamatorios sin indicación médica", "control de presión y glucosa"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Sospecha G3a | TFG 52, albúmina/creatinina 12 | Activa, coincidencia moderada, G3a A1, escalamiento 1; activa cistatina C refleja |
| Sospecha G3b | TFG 38, albúmina/creatinina 80 | Activa, G3b A2, escalamiento 2 |
| Avanzada | TFG 22 | Activa, G4, escalamiento 3 |
| No confirmada | TFG 55 sin albuminuria; TFG combinada con cistatina 68 | Coincidencia baja ("vigilar") |
| Negativo · PDF hombre 46 años | TFG 96, albúmina/creatinina 45 (una toma) | No activa (pasa a NE-002) |
| Negativo · PDF mujer 34 años | TFG 112, albúmina/creatinina 8 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
