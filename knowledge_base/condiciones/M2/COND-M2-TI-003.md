## COND-M2-TI-003 · Sospecha de hipotiroidismo central

**Qué detecta.** T4 libre baja con TSH baja o inapropiadamente normal. Orienta a un problema en la hipófisis y va siempre a endocrinología. Es poco frecuente; los falsos patrones por interferencias son una causa importante a descartar.

```yaml
id: COND-M2-TI-003
nombre: Sospecha de hipotiroidismo central
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: t4l_baja
    biomarcador: free_t4
    condicion: "< límite inferior del laboratorio"
  - id: tsh_no_alta
    biomarcador: tsh
    condicion: "<= límite superior del laboratorio"
regla_central: "t4l_baja AND tsh_no_alta"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con enfermedad aguda reciente o corticoides"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["enfermedad aguda grave reciente", "corticoides en dosis altas", "interferencia del ensayo"]
guias: ["Consenso colombiano de hipotiroidismo 2023"]
frase_permitida: "Tu hormona tiroidea está baja sin que la TSH haya subido como se esperaría. Ese patrón poco común merece una consulta con endocrinología para revisarlo."
frases_prohibidas: ["tienes un tumor en la hipófisis", "tienes hipotiroidismo central"]
recomendaciones_sugeridas: ["consulta con endocrinología", "repetir TSH y T4 libre"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | T4 libre 0,68, TSH 1,4 | Activa, escalamiento 2 |
| Con corticoides | T4 libre 0,80, TSH 0,9, prednisona | Activa, coincidencia moderada |
| Negativo | T4 libre 1,20, TSH 1,8 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
