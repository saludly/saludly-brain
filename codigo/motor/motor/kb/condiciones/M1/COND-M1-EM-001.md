## COND-M1-EM-001 · Prediabetes

**Qué detecta.** Glucosa en ayunas entre 100 y 125 mg/dL o HbA1c entre 5,7 y 6,4 %. Si las dos están en ese rango en la misma muestra, la coincidencia es alta.

```yaml
id: COND-M1-EM-001
nombre: Prediabetes
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D1
criterios:
  - id: glucosa
    biomarcador: glucose
    condicion: "entre 100 y 125"
    unidad: mg/dL
  - id: hba1c
    biomarcador: hba1c
    condicion: "entre 5.7 y 6.4"
    unidad: "%"
regla_central: "glucosa OR hba1c"
contexto_obligatorio: ["ayuno_horas >= 8 (para glucosa)", "embarazo == false"]
excluye_si: ["COND-M1-EM-002", "diabetes conocida declarada"]
coincidencia:
  alta: "glucosa AND hba1c"
  moderada: "glucosa XOR hba1c"
modificado_por: ["COND-M1-EM-A01", "COND-M1-EM-A02"]
escalamiento: 1
nivel_lenguaje: riesgo_potencial
confusores: ["corticoides", "ayuno_insuficiente", "anemia o hemoglobinopatía (baja la confianza en HbA1c; manda la glucosa)", "HbA1c sin método certificado NGSP"]
guias: ["ADA Standards of Care 2026, sección 2", "GPC Colombia DM2 2016"]
frase_permitida: "Tus resultados de glucosa están en un rango que las guías asocian con mayor riesgo de desarrollar diabetes. Es el mejor momento para actuar: pequeños cambios hacen una diferencia grande."
frases_prohibidas: ["tienes prediabetes", "eres prediabético", "vas a ser diabético"]
recomendaciones_sugeridas: ["caminata de 15 minutos después de las comidas principales", "cambiar bebidas azucaradas por agua", "más fibra", "sueño regular"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | Glucosa 112, HbA1c 6,0, ayuno 11 h | Activa, coincidencia alta, escalamiento 1; HOMA-IR 5,5 como apoyo |
| Positivo moderado | Glucosa 94, HbA1c 5,9 | Activa, coincidencia moderada |
| Negativo · PDF mujer 34 años | Glucosa 86, HbA1c 5,2 | No activa |
| Con anemia | Glucosa 92, HbA1c 5,8, hemoglobina 10,9 | Activa con coincidencia baja ("vigilar"): la HbA1c pierde confianza con anemia |
| Diabetes | Glucosa 131, HbA1c 6,7 | No activa (manda EM-002) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
