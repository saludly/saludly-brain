## COND-M4-GA-005 · Infección por *H. pylori*

**Qué detecta.** Antígeno de *H. pylori* positivo en heces. La guía colombiana de 2025 recomienda tratar a todo adulto con infección activa, tenga o no síntomas. La prueba de aliento con urea C13 es la referencia no invasiva; el antígeno fecal es la única opción de la toma domiciliaria y su limitación se escribe en el informe. Un resultado negativo puede ser falso si la persona tomó inhibidores de bomba o antibióticos en las semanas previas.

```yaml
id: COND-M4-GA-005
nombre: Infección por H. pylori
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: antigeno_positivo
    biomarcador: hpylori_stool_ag
    condicion: "positivo"
  - id: falso_negativo_posible
    contexto: medicamentos
    condicion: "inhibidor de bomba de protones en 2 semanas OR antibiótico o bismuto en 4 semanas"
regla_central: "antigeno_positivo"
coincidencia:
  alta: "antigeno_positivo"
escalamiento: 2
negativo_con_medicamentos: "resultado negativo no concluyente; se informa en la vista médica"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["Asociación Colombiana de Gastroenterología 2025, H. pylori"]
por_verificar: "Guía leída solo por resultado de búsqueda; confirmar la recomendación de tratar a todo adulto y las ventanas sin medicamentos (2 y 4 semanas) en el texto completo."
frase_permitida: "En tu muestra de heces se detectó la bacteria H. pylori, que vive en el estómago y es muy común. Las guías colombianas recomiendan tratarla aunque no tengas síntomas: pide una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes úlcera", "tienes gastritis", "tienes cáncer de estómago", "toma antibióticos"]
recomendaciones_sugeridas: ["consulta médica para tratamiento", "no automedicarse con antibióticos"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Antígeno positivo | Activa, escalamiento 2; el informe incluye la limitación del método |
| Negativo con omeprazol | Antígeno negativo, omeprazol diario | No activa; vista médica: negativo no concluyente |
| Negativo · PDF mujer 34 años | Antígeno negativo, sin medicamentos | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
