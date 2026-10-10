## COND-M3-HE-A03 · Eosinofilia (apoyo)

**Qué detecta.** Eosinófilos absolutos de 500 por µL o más (leucocitos × porcentaje de eosinófilos). Se cruza con el coprológico del módulo M4: si hay parásitos, refuerza la parasitosis; si no, se muestra como valor fuera de rango.

```yaml
id: COND-M3-HE-A03
nombre: Eosinofilia
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D1
calculo: "eosinofilos_abs = wbc x eosinophils_pct / 100"
criterios:
  - id: eosinofilia
    condicion: "eosinofilos_abs >= 0,5"
    unidad: x10³/µL
regla_central: "eosinofilia"
modifica: ["parasitosis intestinal (módulo M4)"]
escalamiento:
  base: 1
  si_eosinofilos_abs_mayor_1_5: 2
confusores: ["alergias y asma", "medicamentos"]
guias: ["Intervalo del laboratorio"]
por_verificar: "Corte de 500/µL y escalamiento 2 desde 1.500/µL son definiciones habituales, no de una guía citada en los lotes."
frase_permitida: "Un tipo de glóbulo blanco relacionado con alergias y parásitos (eosinófilos) está alto. Lo cruzamos con tu examen de heces."
frases_prohibidas: ["tienes parásitos", "tienes una alergia"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Leucocitos 8,0, eosinófilos 9 % (0,72) | Activa, escalamiento 1 |
| Con parásitos | Lo anterior y coprológico con parásitos | Refuerza parasitosis (M4) |
| Negativo · PDF hombre 46 años | Leucocitos 7,8, eosinófilos 3,2 % (0,25) | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
