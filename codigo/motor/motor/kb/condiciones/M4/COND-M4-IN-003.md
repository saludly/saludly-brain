## COND-M4-IN-003 · Enfermedad de Chagas crónica

**Qué detecta.** Primera ELISA (antígenos totales) reactiva, confirmada con una segunda ELISA de antígenos recombinantes que corre el laboratorio como refleja. Si las dos discrepan, se necesita una tercera prueba. La infección crónica puede afectar el corazón años después, por eso se remite. La indicación fuera del embarazo sigue pendiente de fuente (lineamiento del INS para adultos).

```yaml
id: COND-M4-IN-003
nombre: Enfermedad de Chagas crónica
modulo: M4
especialidad: infectologia
tipo: incluida
detectabilidad: D2
criterios:
  - id: elisa_1_reactiva
    biomarcador: chagas_elisa_total
    condicion: "reactivo"
  - id: elisa_2_reactiva
    biomarcador: chagas_elisa_recombinante
    condicion: "reactivo"
  - id: procedencia_endemica
    contexto: cuestionario
    condicion: "nació, vivió o vive en municipio endémico (lista por definir con el médico)"
regla_central: "elisa_1_reactiva AND elisa_2_reactiva"
variantes:
  discordante: "elisa_1_reactiva AND NOT elisa_2_reactiva (tercera prueba; informe en espera)"
coincidencia:
  alta: "regla_central AND procedencia_endemica"
  moderada: "regla_central sin procedencia endémica conocida"
escalamiento: 2
canal: "llamada del médico; nunca por WhatsApp"
nivel_lenguaje: condicion_requiere_evaluacion
guias: ["Minsalud, algoritmo de Chagas (pieza para gestantes)"]
por_verificar: "Lineamiento del INS para adultos fuera del embarazo y lista de municipios endémicos. Sin ellos, la ficha no debería usarse con pacientes reales."
frase_permitida: "Tus dos pruebas para la enfermedad de Chagas salieron reactivas. Es una infección que puede no dar síntomas por años y que tiene manejo; nuestro médico te va a llamar para explicarte los pasos, que incluyen una revisión del corazón."
frases_prohibidas: ["tienes daño en el corazón", "es mortal", "es incurable"]
recomendaciones_sugeridas: ["consulta médica", "evaluación cardíaca según indique el médico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Dos ELISA reactivas, nacido en municipio endémico | Activa, coincidencia alta, escalamiento 2, llamada |
| Discordante | ELISA total reactiva, recombinante no reactiva | Informe en espera de tercera prueba |
| Negativo · PDF ejemplos | ELISA total no reactiva | No activa; no se corre la segunda |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
