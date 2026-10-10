## COND-M1-EM-004 · Obesidad y sobrepeso

**Qué detecta.** Índice de masa corporal (peso / talla²) de 25 o más (sobrepeso) o de 30 o más (obesidad), con peso y talla medidos por la enfermera. La cintura agrega la adiposidad central.

```yaml
id: COND-M1-EM-004
nombre: Obesidad y sobrepeso
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D2
calculo: "imc = peso_kg / talla_m^2"
criterios:
  - id: sobrepeso
    condicion: "imc >= 25 AND imc < 30"
  - id: obesidad
    condicion: "imc >= 30"
  - id: obesidad_clase_3
    condicion: "imc >= 40"
  - id: adiposidad_central
    contexto: cintura_cm
    condicion: ">= 90 si hombre; >= 80 si mujer"
regla_central: "sobrepeso OR obesidad"
contexto_obligatorio: ["peso y talla medidos por la enfermera", "embarazo == false"]
excluye_si: []
coincidencia:
  alta: "regla_central con peso y talla medidos"
escalamiento:
  base: 1
  si_obesidad_clase_3: 2
nivel_lenguaje: resultado_observado
confusores: ["masa muscular alta (el IMC no distingue músculo de grasa; la cintura ayuda)"]
guias: ["OMS, obesidad y sobrepeso"]
por_verificar: "El escalamiento 2 para IMC de 40 o más es propuesta de Saludly, no sale de la guía."
frase_permitida: "Con tu peso y tu talla, tu índice de masa corporal es {imc}, que la OMS clasifica como {categoria}. Tu medida de cintura nos ayuda a entender mejor dónde se acumula la grasa."
frases_prohibidas: ["eres obeso", "estás gordo", "tienes que adelgazar"]
recomendaciones_sugeridas: ["alimentación con más vegetales y menos ultraprocesados", "actividad física diaria", "sueño regular", "nutricionista si el paciente quiere"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Obesidad | Peso 92 kg, talla 1,75 m (IMC 30,0), cintura 104 cm, hombre | Activa como obesidad con adiposidad central, escalamiento 1 |
| Sobrepeso | Peso 70 kg, talla 1,62 m (IMC 26,7) | Activa como sobrepeso, escalamiento 1 |
| Clase 3 | Peso 118 kg, talla 1,68 m (IMC 41,8) | Activa, escalamiento 2 |
| Negativo | Peso 63 kg, talla 1,68 m (IMC 22,3) | No activa |
| Sin medida | Peso o talla faltante | No interpretable |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
