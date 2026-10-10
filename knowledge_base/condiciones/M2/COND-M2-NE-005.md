## COND-M2-NE-005 · Sodio bajo

**Qué detecta.** Sodio menor de 135 mmol/L, clasificado como leve (130 a 135), moderado (125 a 129) o profundo (menor de 125). Antes de activarse descarta los falsos bajos: glucosa muy alta (se corrige) y triglicéridos o proteínas muy altos con método de electrodo indirecto (pseudohiponatremia).

```yaml
id: COND-M2-NE-005
nombre: Sodio bajo
modulo: M2
especialidad: nefrologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: na_leve
    biomarcador: sodium
    condicion: "130-134.9"
    unidad: mmol/L
  - id: na_moderado
    biomarcador: sodium
    condicion: "125-129.9"
  - id: na_profundo
    biomarcador: sodium
    condicion: "< 125"
correccion: "si glucosa >= 200 mg/dL: sodio corregido = sodio + 1,6 x (glucosa - 100) / 100; se evalúa el sodio corregido"
no_interpretable_si: ["triglycerides >= 1000 con método ISE indirecto", "total_protein > 10 g/dL con método ISE indirecto"]
regla_central: "na_leve OR na_moderado OR na_profundo (sobre el sodio corregido)"
coincidencia:
  alta: "regla_central sin causas de falso bajo"
escalamiento:
  na_leve: 1
  na_moderado: 2
  na_profundo: 3
nivel_lenguaje: resultado_observado
confusores: ["diuréticos tiazídicos", "antidepresivos ISRS", "consumo muy alto de agua (por ejemplo, tras ejercicio prolongado)", "edad mayor de 65"]
guias: ["Guía europea de hiponatremia 2014"]
por_verificar: "Factor de corrección por glucosa de 1,6 (Katz); otros autores usan 2,4. El médico elige."
frase_permitida: "Tu sodio salió un poco bajo. Puede relacionarse con medicamentos o con cuánta agua tomas; conviene repetirlo y comentarlo con tu médico."
frases_prohibidas: ["tienes hiponatremia", "deja de tomar agua"]
recomendaciones_sugeridas: ["repetir el sodio", "revisar medicamentos con el médico", "en deportistas de resistencia: hidratación con sales, no solo agua"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Leve | Sodio 132, glucosa 95 | Activa, escalamiento 1 |
| Moderado con tiazida | Sodio 127, toma hidroclorotiazida | Activa, escalamiento 2 |
| Profundo | Sodio 121 | Activa, escalamiento 3 |
| Corregido | Sodio 131, glucosa 420 (corregido 136,1) | No activa |
| Pseudohiponatremia | Sodio 129, triglicéridos 1.400, ISE indirecto | No interpretable |
| Negativo · PDF ejemplos | Sodio 140 y 138 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
