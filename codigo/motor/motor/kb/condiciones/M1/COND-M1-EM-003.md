## COND-M1-EM-003 · Síndrome metabólico

**Qué detecta.** Tres o más de cinco componentes, según la declaración armonizada de 2009, con cortes de cintura para población centro y suramericana. Tres componentes salen del laboratorio y dos de la enfermera.

```yaml
id: COND-M1-EM-003
nombre: Síndrome metabólico
modulo: M1
especialidad: endocrinologia_metabolica
tipo: incluida
detectabilidad: D2
criterios:
  - id: cintura
    contexto: cintura_cm
    condicion: ">= 90 si hombre; >= 80 si mujer"
  - id: trigliceridos
    biomarcador: triglycerides
    condicion: ">= 150 OR medicamento para triglicéridos"
    unidad: mg/dL
  - id: hdl
    biomarcador: hdl_c
    condicion: "< 40 si hombre; < 50 si mujer; OR medicamento para HDL"
    unidad: mg/dL
  - id: presion
    contexto: presion_enfermera
    condicion: "sistólica >= 130 OR diastólica >= 85 OR antihipertensivo"
  - id: glucosa
    biomarcador: glucose
    condicion: ">= 100 OR hipoglucemiante"
    unidad: mg/dL
regla_central: "al menos 3 de [cintura, trigliceridos, hdl, presion, glucosa]"
contexto_obligatorio: ["ayuno_horas >= 8"]
excluye_si: []
coincidencia:
  alta: "regla_central con los 5 componentes medidos"
  moderada: "regla_central con algún componente sin medir"
  incompleto: "menos de 3 cumplidos pero los componentes faltantes podrían completar 3"
modificado_por: ["COND-M1-EM-A02"]
escalamiento: 1
nivel_lenguaje: patron_compatible
confusores: ["ayuno_insuficiente", "corticoides"]
guias: ["Declaración armonizada IDF/AHA/NHLBI 2009"]
reglas_especiales: ["el corte de cintura de 94 y 90 cm solo se usa dentro de FINDRISC"]
frase_permitida: "Tienes {n} de los 5 componentes que forman el síndrome metabólico, un conjunto que aumenta el riesgo de diabetes y enfermedad cardiovascular. La buena noticia es que todos mejoran con los mismos cambios de hábitos."
frases_prohibidas: ["tienes síndrome metabólico", "estás enfermo"]
recomendaciones_sugeridas: ["actividad física regular", "reducir azúcares y harinas refinadas", "control de peso y cintura", "sueño regular"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo moderado · PDF hombre 46 años sin datos de la enfermera | Triglicéridos 238, HDL 36, glucosa 112; falta cintura y presión | Activa con 3 de 5, coincidencia moderada; dice que faltan cintura y presión |
| Positivo alto | Lo anterior más cintura 98 cm y presión 128/82 | Activa con 4 de 5, coincidencia alta |
| Incompleto | Triglicéridos 170, HDL 52 (hombre), glucosa 92; falta cintura y presión | No activa; se marca incompleto |
| Negativo · PDF mujer 34 años | Triglicéridos 98, HDL 58, glucosa 86; cintura 74, presión 112/70 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
