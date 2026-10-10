## COND-M2-TI-002 · Hipotiroidismo primario

**Qué detecta.** TSH alta con T4 libre baja. La tiroides produce poca hormona y la hipófisis lo compensa subiendo la TSH.

```yaml
id: COND-M2-TI-002
nombre: Hipotiroidismo primario
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_alta
    biomarcador: tsh
    condicion: "> límite superior del laboratorio"
  - id: t4l_baja
    biomarcador: free_t4
    condicion: "< límite inferior del laboratorio"
regla_central: "tsh_alta AND t4l_baja"
contexto_obligatorio: ["embarazo == false"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (control)"]
excluye_si: ["COND-M2-TI-006", "COND-M2-TI-001"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con enfermedad aguda reciente o amiodarona o litio"
modificado_por: ["COND-M2-TI-A01"]
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["enfermedad aguda reciente", "amiodarona", "litio"]
guias: ["Consenso colombiano de hipotiroidismo 2023"]
frase_permitida: "Tu TSH está alta y tu hormona tiroidea está baja. Ese patrón indica que la tiroides podría estar trabajando menos de lo necesario; conviene una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes hipotiroidismo", "necesitas levotiroxina", "toma esta dosis"]
recomendaciones_sugeridas: ["consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | TSH 14,2, T4 libre 0,71 | Activa, coincidencia alta, escalamiento 2; desplaza a TI-001 |
| Con amiodarona | TSH 9,8, T4 libre 0,85, amiodarona | Activa, coincidencia moderada |
| Negativo · PDF mujer 34 años | TSH 6,90, T4 libre 1,02 | No activa (es TI-001) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
