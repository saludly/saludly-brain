## COND-M5-UR-A01 · Testosterona libre calculada (apoyo)

**Qué detecta.** Testosterona libre calculada con la fórmula de Vermeulen (testosterona total, SHBG y albúmina). Se usa sobre todo cuando la total queda cerca del límite o la SHBG está alterada (obesidad, edad, hipotiroidismo). La guía acepta total o libre baja.

```yaml
id: COND-M5-UR-A01
nombre: Testosterona libre calculada
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: apoyo
detectabilidad: D1
calculo: "fórmula de Vermeulen con testosterona total, SHBG y albúmina"
se_calcula_si: ["testosterona total entre 200 y 400 ng/dL", "SHBG fuera de rango", "IMC >= 30"]
criterios:
  - id: libre_baja
    condicion: "< límite inferior del intervalo de testosterona libre calculada del laboratorio o del calculador validado"
regla_central: "sexo == hombre AND libre_baja"
modifica: ["COND-M5-UR-002"]
efecto: "Con total baja, sube la coincidencia a alta. Con total normal y libre baja (por ejemplo, SHBG alta), la vista médica lo muestra como vigilar."
uso_en_mujeres: "en mujeres se usa el índice de andrógenos libres de MU-001"
guias: ["Endocrine Society 2018"]
por_verificar: "Intervalo de referencia de la testosterona libre calculada; depende del calculador y del laboratorio."
frase_permitida_medico: "Testosterona libre calculada {valor}: {apoya | no apoya} testosterona baja."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Apoya | Total 250, SHBG 22, albúmina 4,4; libre baja | UR-002 sube a coincidencia alta |
| SHBG alta | Total 330, SHBG 70; libre baja | Vigilar en la vista médica |
| No se calcula · PDF hombre 46 años | Total 412, SHBG 28, IMC sin dato | No se calcula salvo que el IMC sea 30 o más |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
