## COND-M4-GA-001 · Riesgo de fibrosis por hígado graso metabólico (FIB-4)

**Qué detecta.** El índice FIB-4 estima el riesgo de fibrosis hepática avanzada en personas con factores metabólicos o enzimas hepáticas alteradas. Menor de 1,3 la descarta; mayor de 2,67 la sugiere; entre ambos es indeterminado y se discute elastografía. No diagnostica hígado graso: eso exige imagen.

```yaml
id: COND-M4-GA-001
nombre: Riesgo de fibrosis por hígado graso metabólico (FIB-4)
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D2
calculo: "fib4 = (edad x AST) / (plaquetas en 10^9/L x raíz cuadrada de ALT)"
aplica_si: ["diabetes tipo 2 (conocida o COND-M1-EM-002)", "cintura alta (>= 90 H, >= 80 M) con otro factor metabólico", "ALT, AST o GGT por encima del valor sano o del laboratorio"]
criterios:
  - id: fib4_bajo
    condicion: "< 1,3"
  - id: fib4_indeterminado
    condicion: "1,3-2,67"
  - id: fib4_alto
    condicion: "> 2,67"
regla_central: "aplica AND (fib4_indeterminado OR fib4_alto)"
reglas_especiales:
  - "edad < 35: FIB-4 menos confiable; se muestra con advertencia"
  - "edad > 65 o diabetes: un FIB-4 bajo no descarta fibrosis; se marca como no concluyente en la vista médica"
coincidencia:
  alta: "fib4_alto sin confusores"
  moderada: "fib4_indeterminado, o fib4_alto con ejercicio intenso reciente (AST muscular)"
escalamiento:
  fib4_indeterminado: 1
  fib4_alto: 2
modificado_por: ["COND-M4-GA-A02", "relación patrón muscular (documento 03)"]
nivel_lenguaje: riesgo_potencial
confusores: ["patrón muscular (CK alta): la AST puede ser de músculo", "plaquetas bajas por otra causa", "hepatitis viral activa"]
guias: ["EASL-EASD-EASO 2024, hígado graso metabólico"]
por_verificar: "Fuente leída solo por resultado de búsqueda. Confirmar los cortes 1,3 y 2,67 y la regla para mayores de 65 en la guía completa."
frase_permitida_indeterminado: "Con tus resultados, el índice que estima la salud del hígado (FIB-4) quedó en una zona intermedia. No dice que haya daño, pero conviene revisarlo con tu médico, que puede pedir una prueba de elasticidad del hígado."
frase_permitida_alto: "El índice que estima la salud del hígado (FIB-4) salió alto. Conviene una consulta médica en las próximas semanas para estudiarlo mejor."
frases_prohibidas: ["tienes hígado graso", "tienes cirrosis", "tienes fibrosis"]
recomendaciones_sugeridas: ["reducir alcohol, azúcar y ultraprocesados", "actividad física regular", "control de peso"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Bajo · PDF hombre 46 años | Edad 46, AST 39, ALT 58, plaquetas 265 (FIB-4 0,89) | No activa; la vista médica muestra FIB-4 bajo |
| Indeterminado | Edad 58, AST 48, ALT 52, plaquetas 190, diabetes (FIB-4 2,03) | Activa, coincidencia moderada, escalamiento 1 |
| Alto | Edad 62, AST 70, ALT 45, plaquetas 140 (FIB-4 4,62) | Activa, escalamiento 2 |
| Mayor de 65 | Edad 70, FIB-4 1,1, diabetes | No activa; vista médica: no concluyente |
| No aplica · PDF mujer 34 años | Sin factores metabólicos, enzimas normales | No se calcula |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
