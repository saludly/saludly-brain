## COND-M6-RE-001 · Ácido úrico alto sin síntomas

**Qué detecta.** Ácido úrico por encima del intervalo del laboratorio. La ACR 2020 recomienda no iniciar medicamentos para bajarlo si no hay gota, así que el informe orienta a hábitos y lo lee junto con el contexto cardiometabólico y renal.

```yaml
id: COND-M6-RE-001
nombre: Ácido úrico alto sin síntomas
modulo: M6
especialidad: reumatologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: urico_alto
    biomarcador: uric_acid
    condicion: "> límite superior del laboratorio (por sexo)"
    unidad: mg/dL
regla_central: "urico_alto"
contexto_vista_medica: ["síndrome metabólico (M1 EM-003)", "prediabetes o diabetes (M1)", "TFG baja (M2)", "hipertensión (M1 CA-006)", "diuréticos", "alcohol"]
coincidencia:
  alta: "urico_alto"
escalamiento: 1
nivel_lenguaje: resultado_observado
confusores: ["diuréticos tiazídicos o de asa", "deshidratación", "ayuno prolongado", "ejercicio intenso reciente", "dieta muy alta en carnes rojas, vísceras o mariscos"]
reglas_seguridad: ["no sugerir medicamentos para bajar el ácido úrico", "si la persona declara dolor e hinchazón súbita de una articulación, recomendar consulta"]
guias: ["ACR 2020, gota"]
por_verificar: "Guía leída solo por resultado de búsqueda."
frase_permitida: "Tu ácido úrico está por encima del rango. Sin síntomas no necesita medicamentos, pero suele mejorar con los mismos hábitos que cuidan el corazón y el metabolismo."
frases_prohibidas: ["tienes gota", "tienes artritis", "toma alopurinol"]
recomendaciones_sugeridas: ["reducir alcohol, sobre todo cerveza", "reducir bebidas azucaradas", "moderar carnes rojas, vísceras y mariscos", "buena hidratación", "control de peso"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Ácido úrico 7,6 (hasta 7,0), con prediabetes y síndrome metabólico | Activa, escalamiento 1; la vista médica lo liga al contexto cardiometabólico |
| Con diurético | Ácido úrico 8,2, toma hidroclorotiazida | Activa; la vista médica menciona el diurético |
| Negativo · PDF mujer 34 años | Ácido úrico 4,1 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
