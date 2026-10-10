## COND-M6-RE-A01 · ANA positivo (apoyo)

**Qué detecta.** Anticuerpos antinucleares positivos por inmunofluorescencia en células HEp-2, con título y patrón. Cerca del 14 % de la población general tiene ANA positivo sin enfermedad, y los criterios EULAR/ACR 2019 usan 1:80 o más solo como puerta de entrada que exige criterios clínicos. El informe explica que es frecuente y nunca habla de lupus ni de enfermedad autoinmune.

**Corrección a la regla del documento 03.** La regla anterior trataba el patrón moteado fino (AC-4) como el más benigno. En la literatura, el patrón que más se asocia a personas sanas es el moteado fino denso (AC-2, anticuerpos DFS70). Esta ficha usa el título como regla principal y deja el AC-2 como nota en la vista médica. El médico decide cuál de las dos reglas queda.

```yaml
id: COND-M6-RE-A01
nombre: ANA positivo
modulo: M6
especialidad: reumatologia
tipo: apoyo
detectabilidad: D3
criterios:
  - id: ana_1_80
    biomarcador: ana_hep2
    condicion: "título 1:80"
  - id: ana_1_160_o_mas
    biomarcador: ana_hep2
    condicion: "título >= 1:160"
  - id: patron
    biomarcador: ana_hep2_patron
    condicion: "patrón ICAP (AC-xx) reportado"
regla_central: "ana_1_80 OR ana_1_160_o_mas"
no_interpretable_si: ["positivo sin título o sin patrón"]
escalamiento:
  ana_1_80: 1
  ana_1_160_o_mas: 2
nota_vista_medica: ["patrón AC-2 (moteado fino denso): frecuente en personas sanas", "anti-TPO positivo o TSH alta (M2): la autoinmunidad tiroidea se asocia a ANA positivo"]
nivel_lenguaje: resultado_observado
guias: ["Satoh 2012 (prevalencia en población general)", "Criterios EULAR/ACR 2019 para lupus"]
por_verificar: "Regla de patrón: AC-4 (regla anterior) o AC-2 (literatura). El médico define desde qué título y patrón se recomienda consulta."
frase_permitida: "Tus anticuerpos antinucleares (ANA) salieron positivos con un título de {titulo}. Es un resultado frecuente en personas sanas y por sí solo no indica ninguna enfermedad; conviene comentarlo con tu médico, sobre todo si tienes dolor en las articulaciones, manchas en la piel o fiebre sin causa."
frases_prohibidas: ["tienes lupus", "tienes una enfermedad autoinmune", "tu sistema inmune te está atacando"]
recomendaciones_sugeridas: ["consulta médica si el título es 1:160 o más o si hay síntomas"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | ANA positivo 1:160, patrón moteado fino (AC-4), anti-TPO 186 | Escalamiento 2; la vista médica anota la autoinmunidad tiroidea |
| Título bajo | ANA 1:80, AC-2 | Escalamiento 1; nota de patrón frecuente en sanos |
| Sin título | "ANA positivo" sin título | No interpretable; pedir título y patrón al laboratorio |
| Negativo · PDF hombre 46 años | ANA negativo (menor de 1:80) | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
