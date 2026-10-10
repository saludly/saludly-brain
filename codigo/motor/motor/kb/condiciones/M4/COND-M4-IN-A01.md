## COND-M4-IN-A01 · Infección urinaria con síntomas (apoyo)

**Qué detecta.** Uroanálisis alterado (nitritos, esterasa leucocitaria o leucocitos en el sedimento) solo cuenta si hay síntomas: ardor, urgencia o fiebre, que pregunta la enfermera. Sin síntomas no se reporta como infección, salvo en el embarazo. El urocultivo no está entre las 18 reflejas: lo pide el médico.

```yaml
id: COND-M4-IN-A01
nombre: Infección urinaria con síntomas
modulo: M4
especialidad: infectologia
tipo: apoyo
detectabilidad: D2
criterios:
  - id: uroanalisis_alterado
    condicion: "nitritos positivos OR esterasa leucocitaria positiva OR leucocitos > 5 por campo"
  - id: sintomas
    contexto: visita
    condicion: "ardor al orinar OR urgencia OR fiebre"
  - id: embarazo
    contexto: perfil
    condicion: "true"
regla_central: "uroanalisis_alterado AND sintomas"
reglas_especiales:
  - "uroanalisis_alterado sin sintomas y sin embarazo: no se reporta como infección (IDSA 2019)"
  - "uroanalisis_alterado con embarazo: vista médica, escalamiento 1 (requiere urocultivo)"
modifica: ["COND-M2-NE-002 (la infección eleva la albuminuria)", "COND-M2-NE-006 (la infección explica hematuria)"]
escalamiento: 1
guias: ["IDSA 2019, bacteriuria asintomática"]
frase_permitida: "Tu examen de orina y tus síntomas sugieren una posible infección urinaria. Consulta para confirmarlo con un urocultivo."
frases_prohibidas: ["tienes una infección", "toma antibiótico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Con síntomas | Nitritos positivos, ardor al orinar | Activa, escalamiento 1 |
| Sin síntomas | Esterasa positiva, sin síntomas, no embarazada | No se reporta |
| Embarazo | Nitritos positivos, embarazo de 14 semanas | Vista médica, escalamiento 1 |
| Negativo · PDF ejemplos | Uroanálisis normal | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
