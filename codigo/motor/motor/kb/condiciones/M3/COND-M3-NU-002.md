## COND-M3-NU-002 · Déficit de folato

**Qué detecta.** Folato sérico menor de 4 ng/mL (posible déficit) o menor de 3 ng/mL (déficit con impacto en la sangre). Los cortes dependen del método del laboratorio, y una sola comida rica en folato puede normalizar el valor sérico.

```yaml
id: COND-M3-NU-002
nombre: Déficit de folato
modulo: M3
especialidad: nutricion_y_micronutrientes
tipo: incluida
detectabilidad: D1
criterios:
  - id: folato_posible
    biomarcador: folate
    condicion: "3-3,9"
    unidad: ng/mL
  - id: folato_bajo
    biomarcador: folate
    condicion: "< 3"
    unidad: ng/mL
regla_central: "folato_posible OR folato_bajo"
contexto_obligatorio: ["ayuno >= 8 horas"]
excluye_si: ["COND-M3-HE-004 activa por folato"]
coincidencia:
  alta: "folato_bajo"
  moderada: "folato_posible"
modificado_por: ["COND-M3-NU-A01"]
escalamiento:
  base: 1
  embarazo: 2
nivel_lenguaje: riesgo_potencial
confusores: ["alcohol", "metotrexato y otros medicamentos", "comida reciente (sube el valor)"]
guias: ["OMS, folato"]
por_verificar: "El laboratorio debe declarar el método; los cortes cambian con él."
frase_permitida: "Tu folato está bajo. Es importante para la sangre y, en mujeres que pueden quedar embarazadas, para el desarrollo del bebé. Conviene mejorarlo con la alimentación y comentarlo con tu médico."
frases_prohibidas: ["toma ácido fólico", "tu bebé tendrá problemas"]
recomendaciones_sugeridas: ["hojas verdes, leguminosas y frutas cítricas", "reducir alcohol", "si busca embarazo, hablar con el médico sobre ácido fólico"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Folato 2,6 | Activa, coincidencia alta, escalamiento 1 |
| Posible | Folato 3,6 | Activa, coincidencia moderada |
| Embarazo | Folato 3,2, embarazo de 8 semanas | Activa, escalamiento 2 |
| Negativo · PDF ejemplos | Folato 9,8 y 6,2 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
