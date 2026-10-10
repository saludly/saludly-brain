## COND-M5-MU-001 · Andrógenos altos (posible SOP)

**Qué detecta.** Testosterona total alta o índice de andrógenos libres alto en una mujer. El síndrome de ovario poliquístico exige además ciclos irregulares u ovarios poliquísticos y descartar otras causas, así que el agente solo señala el hallazgo y remite. Con anticonceptivo hormonal no se interpreta, porque suprime los andrógenos.

```yaml
id: COND-M5-MU-001
nombre: Andrógenos altos (posible SOP)
modulo: M5
especialidad: salud_de_la_mujer
tipo: incluida
detectabilidad: D3
calculo: "indice_androgenos_libres = testosterona total (nmol/L) x 100 / SHBG (nmol/L); testosterona en ng/dL x 0,0347 = nmol/L"
criterios:
  - id: testosterona_alta
    biomarcador: testosterone_total
    condicion: "> límite superior del laboratorio para mujeres"
  - id: fai_alto
    condicion: "indice_androgenos_libres > corte de la guía de SOP 2023 o del laboratorio"
  - id: testosterona_muy_alta
    biomarcador: testosterone_total
    condicion: "> 2 veces el límite superior"
regla_central: "sexo == mujer AND (testosterona_alta OR fai_alto)"
no_interpretable_si: ["anticonceptivo hormonal", "embarazo", "menopausia declarada"]
otras_causas_revisadas: ["TSH alterada (M2)", "prolactina alta (MU-003)"]
coincidencia:
  alta: "testosterona_alta AND fai_alto sin otras causas"
  moderada: "testosterona_alta XOR fai_alto, o con TSH o prolactina alteradas"
escalamiento:
  base: 1
  si_testosterona_muy_alta: 2
nivel_lenguaje: resultado_observado
relacion: "con resistencia a la insulina (M1 EM-A02) y síndrome metabólico (M1 EM-003), la vista médica los cruza"
guias: ["Guía internacional de SOP 2023"]
por_verificar: "Corte del índice de andrógenos libres y el escalamiento 2 con más del doble del límite (propuesta de Saludly) deben confirmarse en la guía completa."
frase_permitida: "Tus hormonas masculinas (andrógenos) están por encima del rango para mujeres. Puede tener varias explicaciones; si además tus ciclos menstruales son irregulares, coméntalo con tu médico."
frases_prohibidas: ["tienes ovario poliquístico", "tienes SOP", "tienes un tumor", "no vas a poder tener hijos"]
recomendaciones_sugeridas: ["consulta con ginecología o medicina general", "actividad física y alimentación si hay resistencia a la insulina"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Mujer 27 años, testosterona 72 ng/dL (hasta 48), SHBG 22, sin anticonceptivo | Activa, coincidencia alta, escalamiento 1 |
| Muy alta | Testosterona 140 ng/dL | Activa, escalamiento 2 |
| Anticonceptivo | Testosterona 60, toma anticonceptivo oral | No interpretable |
| Negativo · PDF mujer 34 años | Testosterona 32, SHBG 62 (índice 1,8), sin anticonceptivo | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
