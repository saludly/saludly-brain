## COND-M2-TI-005 · Hipertiroidismo manifiesto o T3-toxicosis

**Qué detecta.** TSH suprimida con T4 libre o T3 elevadas. T3 elevada con T4 libre normal es T3-toxicosis. Se usa T3 total, como prefiere la ATA; T4 libre y T3 total van en el panel estándar (decisión del 22 de octubre de 2026).

```yaml
id: COND-M2-TI-005
nombre: Hipertiroidismo manifiesto o T3-toxicosis
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_baja
    biomarcador: tsh
    condicion: "< límite inferior del laboratorio"
  - id: t4l_alta
    biomarcador: free_t4
    condicion: "> límite superior"
  - id: t3_alta
    biomarcador: total_t3
    condicion: "> límite superior"
regla_central: "tsh_baja AND (t4l_alta OR t3_alta)"
variante: "t3_toxicosis si t3_alta AND NOT t4l_alta"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (posible sobredosificación)"]
excluye_si: ["COND-M2-TI-004"]
coincidencia:
  alta: "regla_central sin confusores"
escalamiento:
  base: 2
  bandera_critica_laboratorio: 3
contexto_wearable: "frecuencia cardíaca en reposo alta en el Apple Watch refuerza la recomendación de consulta"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["ATA 2016"]
frase_permitida: "Tu TSH está baja y tus hormonas tiroideas están altas. Ese patrón indica que la tiroides podría estar trabajando de más; necesitas una consulta médica en las próximas semanas. Si tienes palpitaciones fuertes, falta de aire o temblor intenso, consulta antes."
frases_prohibidas: ["tienes hipertiroidismo", "tienes Graves", "tienes una tormenta tiroidea"]
recomendaciones_sugeridas: ["consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Manifiesto | TSH < 0,01, T4 libre 2,9 | Activa, escalamiento 2 |
| T3-toxicosis | TSH 0,02, T4 libre 1,5 (normal), T3 total 245 (alta) | Activa, variante T3-toxicosis |
| Con levotiroxina | TSH 0,03, T4 libre 2,1, toma levotiroxina | Bloqueada; vista médica: posible sobredosificación |
| Negativo | TSH 1,8 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
