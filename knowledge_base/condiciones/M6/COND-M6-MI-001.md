## COND-M6-MI-001 · Riesgo de desnutrición

**Qué detecta.** Un criterio fenotípico (IMC bajo para la edad o pérdida de peso no intencional) con un criterio etiológico (inflamación por hs-CRP alta o ingesta reducida). GLIM exige uno de cada tipo y fue diseñado para entornos clínicos, así que el informe habla de riesgo, nunca de desnutrición.

```yaml
id: COND-M6-MI-001
nombre: Riesgo de desnutrición
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: incluida
detectabilidad: D2
calculo: "imc = peso_kg / talla_m^2 (medidos por la enfermera)"
criterios_fenotipicos:
  - id: imc_bajo
    condicion: "imc < 20 si edad < 70; imc < 22 si edad >= 70"
  - id: perdida_peso
    contexto: cuestionario
    condicion: "pérdida de peso no intencional > 5 % en 6 meses"
criterios_etiologicos:
  - id: inflamacion
    biomarcador: hs_crp
    condicion: "> 5"
    unidad: mg/L
  - id: ingesta_reducida
    contexto: cuestionario
    condicion: "come menos de lo habitual desde hace más de una semana"
regla_central: "(imc_bajo OR perdida_peso) AND (inflamacion OR ingesta_reducida)"
coincidencia:
  alta: "regla_central"
  baja: "criterio fenotípico sin criterio etiológico (vigilar)"
escalamiento:
  base: 1
  edad_70_o_mas: 2
nivel_lenguaje: riesgo_potencial
relacion: ["albúmina baja y anemia se muestran como contexto en la vista médica, no como criterios GLIM"]
guias: ["GLIM 2019"]
por_verificar: "La pérdida de peso y la ingesta dependen de que la enfermera las pregunte; confirmar que estén en el formulario de la visita. El corte de hs-CRP de 5 mg/L sigue la regla del módulo M3."
frase_permitida: "Tu peso y algunos resultados sugieren que tu cuerpo podría no estar recibiendo toda la energía y la proteína que necesita. Conviene revisarlo con tu médico o con un nutricionista."
frases_prohibidas: ["estás desnutrido", "estás muy flaco", "tienes desnutrición"]
recomendaciones_sugeridas: ["consulta con nutricionista", "comidas frecuentes con proteína", "consulta médica si la pérdida de peso no es buscada"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo mayor | Edad 74, IMC 20,8, hs-CRP 9 | Activa, coincidencia alta, escalamiento 2 |
| Positivo joven | Edad 40, IMC 18,6, come menos hace un mes | Activa, escalamiento 1 |
| Vigilar | Edad 30, IMC 19,2, hs-CRP 0,6, ingesta normal | Vigilar |
| Sin medidas · PDF ejemplos | Peso y talla aún no registrados | No interpretable |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
