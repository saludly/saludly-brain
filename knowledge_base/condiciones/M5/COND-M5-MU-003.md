## COND-M5-MU-003 · Prolactina alta

**Qué detecta.** Prolactina por encima del intervalo del laboratorio. Como se mide sin síntomas conocidos, el laboratorio corre macroprolactina como refleja y el agente siempre pide repetir. Si predomina la macroprolactina, el hallazgo no suele tener significado clínico. Nunca se habla de tumor. Sin interpretación en embarazo o lactancia.

```yaml
id: COND-M5-MU-003
nombre: Prolactina alta
modulo: M5
especialidad: salud_de_la_mujer
tipo: incluida
detectabilidad: D3
criterios:
  - id: prl_alta
    biomarcador: prolactin
    condicion: "> límite superior del laboratorio"
  - id: macroprolactina_predominante
    biomarcador: macroprolactin
    condicion: "recuperación tras PEG por debajo del corte del laboratorio"
  - id: prl_muy_alta
    biomarcador: prolactin
    condicion: "> 100"
    unidad: ng/mL
regla_central: "prl_alta AND NOT macroprolactina_predominante"
no_interpretable_si: ["embarazo", "lactancia"]
otras_causas_revisadas: ["TSH alta (M2)", "TFG baja (M2)", "medicamentos: antipsicóticos, metoclopramida, algunos antidepresivos", "estrés de la punción"]
coincidencia:
  alta: "regla_central confirmada en una segunda medición"
  moderada: "regla_central en una sola medición"
  baja: "regla_central con medicamento que la sube o TSH alta"
escalamiento:
  macroprolactina_predominante: 0
  base: 1
  si_prl_muy_alta: 2
nivel_lenguaje: resultado_observado
guias: ["Endocrine Society 2011", "Febrasgo y SBEM 2024"]
por_verificar: "Corte de 100 ng/mL para escalamiento 2 es propuesta de Saludly; confirmar con las guías."
frase_permitida: "Tu prolactina salió por encima del rango. Muchas veces se debe al estrés de la toma o a medicamentos, así que hay que repetirla. Si tienes salida de leche por los pezones o cambios en la menstruación, coméntalo con tu médico."
frase_macroprolactina: "Tu prolactina salió alta, pero la mayor parte es una forma que normalmente no tiene efecto en el cuerpo."
frases_prohibidas: ["tienes un tumor en la hipófisis", "tienes prolactinoma"]
recomendaciones_sugeridas: ["repetir la prolactina en la mañana, en reposo", "revisar medicamentos con el médico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Prolactina 41 (hasta 23,3), macroprolactina no predominante | Activa, coincidencia moderada, escalamiento 1 |
| Macroprolactina | Prolactina 38, macroprolactina predominante | Escalamiento 0, frase de macroprolactina |
| Muy alta | Prolactina 160 | Activa, escalamiento 2 |
| Con medicamento | Prolactina 35, toma risperidona | Coincidencia baja |
| Embarazo | Prolactina 120, embarazo de 20 semanas | No interpretable |
| Negativo · PDF mujer 34 años | Prolactina 14,2 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
