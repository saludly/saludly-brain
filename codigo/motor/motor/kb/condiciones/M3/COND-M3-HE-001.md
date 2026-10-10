## COND-M3-HE-001 · Anemia ajustada por altitud y tabaquismo

**Qué detecta.** Hemoglobina por debajo del corte OMS después de restar los ajustes por altitud de residencia y por tabaquismo. No se ajusta por inflamación ni por etnia. Es la base de HE-002 y HE-004, que explican la causa.

```yaml
id: COND-M3-HE-001
nombre: Anemia ajustada por altitud y tabaquismo
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D2
calculo:
  hemoglobina_ajustada: "hemoglobina - ajuste_altitud - ajuste_tabaquismo"
  ajuste_altitud: "según tabla OMS 2024 por metros de la ciudad de residencia; 2.500 a 2.999 m = 1,8 g/dL"
  ajuste_tabaquismo: "según tabla OMS 2024 por cigarrillos al día"
criterios:
  - id: anemia
    condicion: "hemoglobina_ajustada < 13,0 si hombre; < 12,0 si mujer no gestante; < 11,0 gestante en 1.er o 3.er trimestre; < 10,5 gestante en 2.º trimestre"
    unidad: g/dL
severidad_oms:
  mujer_no_gestante: {leve: "11,0-11,9", moderada: "8,0-10,9", severa: "< 8,0"}
  hombre: {leve: "11,0-12,9", moderada: "8,0-10,9", severa: "< 8,0"}
regla_central: "anemia"
contexto_obligatorio: ["sexo", "ciudad de residencia", "embarazo y semana de gestación en mujeres en edad fértil", "edad >= 15"]
coincidencia:
  alta: "anemia con ciudad y tabaquismo conocidos"
  moderada: "anemia sin dato de tabaquismo"
escalamiento:
  leve: 1
  moderada: 2
  severa: 3
  bandera_critica_laboratorio: 3
nivel_lenguaje: resultado_observado
causas_que_se_evaluan: ["COND-M3-HE-002", "COND-M3-HE-004", "COND-M3-HE-A01", "relación hemólisis (documento 03)"]
guias: ["OMS 2024, cortes de hemoglobina para definir anemia"]
por_verificar: "Los valores del ajuste por tabaquismo deben copiarse de la tabla OMS 2024. Las categorías de severidad en hombres (leve hasta 12,9) siguen la OMS; confirmar en la guía 2024."
frase_permitida: "Tu hemoglobina, ajustada a la altura de {ciudad}, está por debajo del valor recomendado. Eso se llama anemia y tiene varias causas posibles; abajo te contamos qué muestran tus otros resultados."
frases_prohibidas: ["tienes leucemia", "tienes una enfermedad de la sangre"]
recomendaciones_sugeridas: ["depende de la causa (HE-002, HE-004, HE-A01)"]
```

**Casos de prueba** (residencia en Bogotá)

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | Hemoglobina 11,2; ajustada 9,4; no fuma | Activa, anemia moderada, coincidencia alta, escalamiento 2 |
| Positivo oculto por la altura | Mujer, hemoglobina 13,1; ajustada 11,3 | Activa como leve, escalamiento 1 (sin ajuste habría salido normal) |
| Negativo · PDF hombre 46 años | Hemoglobina 16,2; ajustada 14,4 | No activa |
| Severa | Hombre, hemoglobina 9,4; ajustada 7,6 | Activa, severa, escalamiento 3 |
| Embarazo | 2.º trimestre, hemoglobina 12,0; ajustada 10,2 | Activa (corte 10,5) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
