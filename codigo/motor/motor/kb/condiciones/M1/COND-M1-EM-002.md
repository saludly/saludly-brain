## COND-M1-EM-002 · Diabetes tipo 2 en rango diagnóstico

**Qué detecta.** Glucosa en ayunas de 126 mg/dL o más, o HbA1c de 6,5 % o más. La ADA 2026 acepta como confirmación dos pruebas distintas alteradas en la misma muestra; si solo una está en rango, hay que repetir. El tipo exacto de diabetes no se puede clasificar con este panel.

```yaml
id: COND-M1-EM-002
nombre: Diabetes tipo 2 en rango diagnóstico
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D1
criterios:
  - id: glucosa_dm
    biomarcador: glucose
    condicion: ">= 126"
    unidad: mg/dL
  - id: hba1c_dm
    biomarcador: hba1c
    condicion: ">= 6.5"
    unidad: "%"
regla_central: "glucosa_dm OR hba1c_dm"
contexto_obligatorio: ["ayuno_horas >= 8 (para glucosa)", "embarazo == false"]
excluye_si: ["diabetes conocida declarada (se lee como control de diabetes en la vista médica)"]
coincidencia:
  alta: "glucosa_dm AND hba1c_dm"
  moderada: "glucosa_dm XOR hba1c_dm"
escalamiento:
  base: 2
  si_bandera_critica_laboratorio: 3
dispara: ["refleja NT-proBNP (COND-M1-CA-007)"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["corticoides", "ayuno_insuficiente", "anemia o hemoglobinopatía (HbA1c)", "enfermedad aguda reciente"]
guias: ["ADA Standards of Care 2026, sección 2", "GPC Colombia DM2 2016"]
por_verificar: "Diabetes tipo 1 o LADA exigen autoanticuerpos que no ofrecemos; el texto no afirma el tipo."
frase_permitida_alta: "Tu glucosa y tu HbA1c están en el rango que las guías usan para diagnosticar diabetes. Necesitas una consulta médica en las próximas semanas para confirmarlo y empezar el manejo."
frase_permitida_moderada: "Uno de tus resultados de glucosa está en el rango que las guías usan para diagnosticar diabetes. Hay que repetirlo para confirmar; te recomendamos consulta médica."
frases_prohibidas: ["tienes diabetes", "eres diabético", "necesitas insulina", "toma metformina"]
recomendaciones_sugeridas: ["consulta médica", "reducir azúcares y bebidas azucaradas", "actividad física diaria"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo alto | Glucosa 138, HbA1c 6,9 | Activa, coincidencia alta, escalamiento 2; activa NT-proBNP |
| Positivo moderado | Glucosa 128, HbA1c 6,1 | Activa, coincidencia moderada, frase de repetir |
| Negativo · PDF hombre 46 años | Glucosa 112, HbA1c 6,0 | No activa (manda EM-001) |
| Diabetes conocida | Glucosa 150, HbA1c 7,4, metformina | No activa como detección; vista médica de control |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
