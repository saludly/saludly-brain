## COND-M2-TI-001 · Hipotiroidismo subclínico

**Qué detecta.** TSH por encima del rango de decisión con T4 libre normal. Se usa el rango del consenso colombiano por edad cuando el laboratorio no ajusta por edad. TSH entre el límite del laboratorio y el corte del consenso queda como "vigilar". Con TSH de 10 o más, o anti-TPO positivo, la guía considera tratamiento.

```yaml
id: COND-M2-TI-001
nombre: Hipotiroidismo subclínico
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D1
criterios:
  - id: tsh_sobre_lab
    biomarcador: tsh
    condicion: "> límite superior del laboratorio"
  - id: tsh_sobre_consenso
    biomarcador: tsh
    condicion: "> 5.0 si edad 18-60; > 6.0 si edad > 60"
    unidad: mUI/L
  - id: tsh_10
    biomarcador: tsh
    condicion: ">= 10"
  - id: t4l_normal
    biomarcador: free_t4
    condicion: "dentro del intervalo del laboratorio"
regla_central: "tsh_sobre_consenso AND t4l_normal"
contexto_obligatorio: ["embarazo == false", "toma en la mañana"]
bloqueado_si: ["biotina alta o suplemento declarado", "levotiroxina en uso (se lee como control en la vista médica)"]
excluye_si: ["COND-M2-TI-006"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con enfermedad aguda reciente o medicamento que altera la tiroides"
  baja: "tsh_sobre_lab AND NOT tsh_sobre_consenso AND t4l_normal"
modificado_por: ["COND-M2-TI-A01"]
escalamiento:
  base: 1
  si_tsh_10: 2
nivel_lenguaje: patron_compatible
confusores: ["enfermedad aguda reciente", "amiodarona", "litio", "recuperación de una enfermedad grave"]
guias: ["Consenso colombiano de hipotiroidismo 2023", "AACE/ATA (anti-TPO y TSH >= 10 como criterios de tratamiento)"]
por_verificar: "Intervalo para repetir la TSH; la práctica habitual es 2 a 3 meses."
frase_permitida: "Tu TSH, la hormona que regula la tiroides, está un poco alta, mientras que tu hormona tiroidea (T4 libre) está normal. Es un hallazgo frecuente; conviene repetirlo y revisarlo con tu médico."
frase_adicional_mujer_edad_fertil: "Si estás buscando un embarazo, coméntalo pronto con tu médico."
frases_prohibidas: ["tienes hipotiroidismo", "tienes Hashimoto", "necesitas levotiroxina"]
recomendaciones_sugeridas: ["repetir TSH y T4 libre", "consulta médica", "no tomar suplementos de biotina antes de la próxima toma"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | TSH 6,90, T4 libre 1,02 (0,93 a 1,70), anti-TPO 186 | Activa, coincidencia alta, escalamiento 1; refuerzo autoinmune por TI-A01; frase para mujer en edad fértil |
| TSH 10 o más | TSH 11,4, T4 libre normal | Activa, escalamiento 2 |
| Vigilar | TSH 4,6 (laboratorio hasta 4,2), edad 40 | Coincidencia baja (vigilar) |
| Mayor de 60 | TSH 5,6, edad 68 | No activa (corte 6,0) |
| Biotina | TSH 7,2, suplemento de biotina | Bloqueada; pide repetir sin biotina |
| Negativo · PDF hombre 46 años | TSH 2,10 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
