## COND-M2-TI-006 · Disfunción tiroidea en el embarazo

**Qué detecta.** En una gestante, TSH mayor de 4,0 mUI/L indica hipotiroidismo según el consenso colombiano, que pide TSH a toda gestante. Reemplaza a TI-001 y TI-002 cuando hay embarazo. Una TSH baja en el primer trimestre puede ser fisiológica: se muestra al médico como resultado observado.

```yaml
id: COND-M2-TI-006
nombre: Disfunción tiroidea en el embarazo
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D2
criterios:
  - id: embarazo
    contexto: embarazo
    condicion: "true, con semana de gestación"
  - id: tsh_alta_embarazo
    biomarcador: tsh
    condicion: "> 4.0"
    unidad: mUI/L
  - id: t4l_baja
    biomarcador: free_t4
    condicion: "< límite inferior"
regla_central: "embarazo AND tsh_alta_embarazo"
bloqueado_si: ["biotina alta o suplemento declarado"]
coincidencia:
  alta: "regla_central con semana de gestación conocida"
  moderada: "regla_central sin semana de gestación"
modificado_por: ["COND-M2-TI-A01"]
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
reglas_especiales: ["TSH baja en primer trimestre: resultado observado para el médico, sin condición"]
guias: ["Consenso colombiano de hipotiroidismo 2023"]
frase_permitida: "En el embarazo, tu TSH está por encima del valor recomendado. Es importante comentarlo pronto con tu médico o con quien lleva tu control prenatal."
frases_prohibidas: ["tu bebé está en riesgo", "tienes hipotiroidismo"]
recomendaciones_sugeridas: ["consulta con el control prenatal"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Embarazo de 10 semanas, TSH 4,8 | Activa, coincidencia alta, escalamiento 2 |
| Con T4 libre baja | Embarazo de 22 semanas, TSH 6,5, T4 libre baja | Activa; vista médica destaca la T4 libre baja |
| TSH baja | Embarazo de 9 semanas, TSH 0,2 | No activa; resultado observado para el médico |
| No embarazada | TSH 4,8 | No aplica (va por TI-001) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
