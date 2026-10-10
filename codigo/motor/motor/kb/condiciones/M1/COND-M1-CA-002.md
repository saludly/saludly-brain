## COND-M1-CA-002 · Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar

**Qué detecta.** LDL mayor o igual a 190 mg/dL. La GPC colombiana trata este nivel como riesgo alto sin necesidad de calculadora. El antecedente familiar de evento cardiovascular temprano refuerza la sospecha de origen familiar.

```yaml
id: COND-M1-CA-002
nombre: Hipercolesterolemia severa o sospecha de hipercolesterolemia familiar
modulo: M1
especialidad: cardiologia
tipo: incluida
detectabilidad: D2
criterios:
  - id: ldl_muy_alto
    biomarcador: ldl_c
    condicion: ">= 190"
    unidad: mg/dL
  - id: antecedente_familiar
    contexto: antecedente_familiar_cv_temprano
    condicion: "familiar de primer grado: hombre < 55 años o mujer < 65 años"
regla_central: "ldl_muy_alto"
contexto_obligatorio: ["embarazo == false"]
excluye_si: []
coincidencia:
  alta: "ldl_muy_alto AND antecedente_familiar"
  moderada: "ldl_muy_alto AND (NOT antecedente_familiar OR antecedente_familiar desconocido)"
escalamiento: 2
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["tsh_alta (hipotiroidismo como causa secundaria)", "albuminuria importante (causa renal secundaria)", "estatina_en_uso"]
guias: ["GPC Colombia dislipidemias 2014"]
por_verificar: "Criterios diagnósticos formales de hipercolesterolemia familiar (por ejemplo, Dutch Lipid Clinic) no se aplican en la versión 1."
frase_permitida: "Tu colesterol LDL está en un nivel que las guías consideran alto por sí solo. Conviene una consulta médica en las próximas semanas, y que tus familiares cercanos también se lo revisen."
frases_prohibidas: ["tienes hipercolesterolemia familiar", "es genético", "vas a tener un infarto"]
recomendaciones_sugeridas: ["consulta médica", "revisión del perfil lipídico en familiares de primer grado", "alimentación baja en grasa saturada"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo alto | LDL 205, padre con infarto a los 50 años | Activa, coincidencia alta, escalamiento 2; desplaza a CA-001 |
| Positivo moderado | LDL 196, sin dato de antecedente | Activa, coincidencia moderada, escalamiento 2 |
| Negativo | LDL 175 | No activa (CA-001 sí puede activarse) |
| Con confusor | LDL 198, TSH 9,5 | Activa; la vista médica muestra hipotiroidismo como posible causa secundaria |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
