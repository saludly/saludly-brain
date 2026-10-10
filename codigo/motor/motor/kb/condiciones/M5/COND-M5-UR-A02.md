## COND-M5-UR-A02 · Relación PSA libre / total (apoyo)

**Qué detecta.** Proporción de PSA libre sobre el total, que el laboratorio mide como refleja cuando el PSA total queda entre 4 y 10 ng/mL. Una proporción baja se asocia a mayor probabilidad de enfermedad; una alta, a menor. El corte está pendiente de fuente en el Lote 5.

```yaml
id: COND-M5-UR-A02
nombre: Relación PSA libre / total
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: apoyo
detectabilidad: D1
calculo: "porcentaje = PSA libre / PSA total x 100"
se_mide_si: "PSA total entre 4,0 y 10,0 ng/mL"
criterios:
  - id: proporcion_baja
    condicion: "< corte pendiente de fuente (valor habitual en la literatura: 10 %)"
  - id: proporcion_alta
    condicion: "> corte pendiente de fuente (valor habitual en la literatura: 25 %)"
modifica: ["COND-M5-UR-001"]
efecto: "Solo vista médica: proporcion_baja refuerza la consulta; proporcion_alta la contextualiza. No cambia el escalamiento ni el texto del paciente."
guias: ["Pendiente de fuente"]
por_verificar: "Los cortes de 10 % y 25 % son valores habituales en la literatura, no verificados en las fuentes de los lotes. Sin firma, la ficha solo muestra el porcentaje."
frase_permitida_medico: "PSA libre {porcentaje} % del total."
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Baja | PSA total 6,2, libre 0,5 (8 %) | Refuerza UR-001 en la vista médica |
| Alta | PSA total 5,0, libre 1,5 (30 %) | Contextualiza UR-001 |
| No aplica · PDF hombre 46 años | PSA total 1,10 | No se mide |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
