## COND-M2-NE-006 · Hematuria microscópica

**Qué detecta.** Más de 3 hematíes por campo en el sedimento urinario. La tira reactiva sola no basta. En bajo riesgo se repite el uroanálisis en 6 meses; con albuminuria, TFG baja o muchos hematíes sube el escalamiento.

```yaml
id: COND-M2-NE-006
nombre: Hematuria microscópica
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: hematies
    biomarcador: urinalysis_rbc_hpf
    condicion: "> 3"
    unidad: hematíes por campo
  - id: hematies_muchos
    biomarcador: urinalysis_rbc_hpf
    condicion: "> 25"
  - id: marcador_glomerular
    condicion: "uacr >= 30 OR egfr < 60"
regla_central: "hematies (por microscopía)"
no_interpretable_si: ["menstruación actual o en los últimos 3 días", "sondaje o procedimiento urológico reciente"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con ejercicio intenso 48 h o infección urinaria"
escalamiento:
  base: 1
  si_marcador_glomerular: 2
  si_hematies_muchos: 2
nivel_lenguaje: resultado_observado
confusores: ["ejercicio intenso 48 h", "infección urinaria (nitritos o esterasa positivos)", "actividad sexual reciente"]
guias: ["AUA/SUFU 2020, enmendada 2025", "KDIGO 2024"]
por_verificar: "La estratificación completa de riesgo de la AUA (edad, sexo, tabaquismo, número de hematíes) debe tomarse de la guía para decidir quién va directo a urología."
frase_permitida: "En tu orina aparecieron más glóbulos rojos de lo esperado, aunque no se ven a simple vista. Hay varias causas posibles y la mayoría no son graves; conviene repetir el examen y comentarlo con tu médico."
frases_prohibidas: ["tienes cáncer", "tienes cálculos", "tienes una enfermedad renal"]
recomendaciones_sugeridas: ["repetir uroanálisis", "consulta si hay albuminuria o TFG baja"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Bajo riesgo | 6 hematíes por campo, sin albuminuria | Activa, escalamiento 1 |
| Glomerular | 10 hematíes por campo, albúmina/creatinina 140 | Activa, escalamiento 2 |
| Menstruación | 15 hematíes por campo, menstruación actual | No interpretable |
| Solo tira | Tira con sangre positiva, sedimento 0 a 2 | No activa |
| Negativo · PDF ejemplos | Sedimento 0 a 2 por campo | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
