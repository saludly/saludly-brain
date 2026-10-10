## COND-M5-UR-002 · Testosterona baja

**Qué detecta.** Testosterona total matutina por debajo de 264 ng/dL, el percentil 2,5 armonizado por el CDC (Endocrine Society 2018). Solo se etiqueta como baja si el laboratorio declara un método certificado por el CDC; si no, es resultado observado. Sin datos de síntomas nunca se diagnostica hipogonadismo: se pide repetir en la mañana y valorar con el médico.

```yaml
id: COND-M5-UR-002
nombre: Testosterona baja
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: incluida
detectabilidad: D3
criterios:
  - id: testosterona_baja
    biomarcador: testosterone_total
    condicion: "< 264"
    unidad: ng/dL
  - id: metodo_certificado
    condicion: "el laboratorio declara certificación CDC (programa HoST) del método"
  - id: toma_matutina
    condicion: "toma entre las 6:00 y las 10:00, en ayunas"
  - id: testosterona_muy_baja
    biomarcador: testosterone_total
    condicion: "< 150"
regla_central: "sexo == hombre AND testosterona_baja AND metodo_certificado AND toma_matutina"
si_metodo_no_certificado: "resultado observado frente al intervalo del laboratorio, sin etiqueta de baja"
modificado_por: ["COND-M5-UR-A01"]
coincidencia:
  alta: "regla_central AND testosterona libre calculada baja (UR-A01)"
  moderada: "regla_central sin testosterona libre o con confusores"
escalamiento:
  base: 1
  si_testosterona_muy_baja: 2
nivel_lenguaje: resultado_observado
confusores: ["obesidad (baja la SHBG y la testosterona total; usar la libre)", "diabetes", "opioides", "glucocorticoides", "enfermedad aguda reciente", "mal sueño (contexto del Apple Watch)"]
reglas_seguridad: ["nunca sugerir reemplazo hormonal", "nunca proponer testosterona para controlar la glucosa (Endocrine Society)"]
guias: ["Endocrine Society 2018, hipogonadismo masculino"]
por_verificar: "Corte de 150 ng/dL para escalamiento 2 es propuesta de Saludly."
frase_permitida: "Tu testosterona salió baja en esta toma. Varía mucho de un día a otro y con el sueño o el peso, así que hay que repetirla en la mañana. Si tienes cansancio, menos deseo sexual o pérdida de masa muscular, coméntalo con tu médico."
frases_prohibidas: ["tienes hipogonadismo", "tienes andropausia", "necesitas testosterona", "toma testosterona"]
recomendaciones_sugeridas: ["repetir en la mañana", "sueño suficiente", "actividad física y control de peso", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Hombre 52 años, testosterona 228 a las 7:30, método certificado, libre baja | Activa, coincidencia alta, escalamiento 1 |
| No certificado | Testosterona 230, método sin certificación declarada | Resultado observado, sin etiqueta |
| Muy baja | Testosterona 120, certificado | Activa, escalamiento 2 |
| Hora | Testosterona 240 a las 15:00 | No interpretable por hora |
| Negativo · PDF hombre 46 años | Testosterona 412 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
