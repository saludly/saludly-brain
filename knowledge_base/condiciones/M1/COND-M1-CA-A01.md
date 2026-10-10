## COND-M1-CA-A01 · Discordancia ApoB / LDL (apoyo)

**Qué detecta.** ApoB alta con LDL controlado: hay más partículas aterogénicas de las que el LDL sugiere. Es más útil con triglicéridos mayores de 200 mg/dL o con diabetes. No aparece sola: refuerza CA-001 y CA-005 en la vista médica.

```yaml
id: COND-M1-CA-A01
nombre: Discordancia ApoB / LDL
modulo: M1
especialidad: cardiologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: apob_alta
    biomarcador: apob
    condicion: ">= 130"
    unidad: mg/dL
    nota: "percentil 90 aproximado en adultos no tratados (NLA 2024)"
  - id: ldl_no_alto
    biomarcador: ldl_c
    condicion: "< 130"
    unidad: mg/dL
  - id: contexto_util
    condicion: "triglycerides > 200 OR diabetes"
regla_central: "apob_alta AND ldl_no_alto"
modifica: ["COND-M1-CA-001", "COND-M1-CA-005"]
efecto: "Si CA-001 no está activa, se muestra como vigilar en la vista médica. Si contexto_util se cumple, se destaca."
guias: ["ACC/AHA 2026", "NLA 2024 (consenso de expertos)"]
por_verificar: "Corte de discordancia operativo; las guías no fijan uno único."
frase_permitida_medico: "ApoB por encima del percentil 90 con LDL menor de 130 mg/dL: posible subestimación del riesgo por LDL."
frases_prohibidas: ["tu colesterol engaña", "tienes enfermedad cardiovascular"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | ApoB 138, LDL 118, triglicéridos 240 | Activa como apoyo destacado |
| Negativo · PDF hombre 46 años | ApoB 118, LDL 142 | No activa (no hay discordancia: ambos altos) |
| Negativo | ApoB 95, LDL 110 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
