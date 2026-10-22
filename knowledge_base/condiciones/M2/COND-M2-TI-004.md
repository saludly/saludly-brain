## COND-M2-TI-004 · Hipertiroidismo subclínico

**Qué detecta.** TSH baja con T4 libre y T3 total normales. El riesgo es mayor con TSH menor de 0,1 que entre 0,1 y el límite inferior. Hay que repetir para confirmar. La biotina puede producir exactamente este patrón, por eso la bloquea.

```yaml
id: COND-M2-TI-004
nombre: Hipertiroidismo subclínico
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_baja
    biomarcador: tsh
    condicion: "< límite inferior del laboratorio"
  - id: tsh_suprimida
    biomarcador: tsh
    condicion: "< 0.1"
    unidad: mUI/L
  - id: t4l_normal
    biomarcador: free_t4
    condicion: "dentro del intervalo"
  - id: t3_normal
    biomarcador: total_t3
    condicion: "dentro del intervalo"
regla_central: "tsh_baja AND t4l_normal AND t3_normal"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (posible sobredosificación; se lee como control)"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con corticoides, enfermedad aguda o dopamina"
escalamiento:
  base: 1
  si_tsh_suprimida: 2
contexto_wearable: "frecuencia cardíaca en reposo del Apple Watch como contexto; no cambia la coincidencia"
nivel_lenguaje: patron_compatible
confusores: ["corticoides", "enfermedad aguda reciente", "biotina"]
guias: ["ATA 2016"]
frase_permitida: "Tu TSH está más baja de lo esperado, aunque tus hormonas tiroideas están normales. Conviene repetir el examen y revisarlo con tu médico."
frases_prohibidas: ["tienes hipertiroidismo", "tienes Graves", "tienes bocio"]
recomendaciones_sugeridas: ["repetir TSH, T4 libre y T3", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Leve | TSH 0,18, T4 libre y T3 total normales | Activa, escalamiento 1 |
| Suprimida | TSH 0,05, T4 libre y T3 total normales | Activa, escalamiento 2 |
| Biotina | TSH 0,08, biotina en el cuestionario | Bloqueada; pide repetir sin biotina |
| Negativo · PDF ejemplos | TSH 2,10 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
