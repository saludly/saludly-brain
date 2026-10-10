## COND-M2-TI-008 · Hiperaldosteronismo primario (tamizaje en hipertensos)

**Qué detecta.** Renina suprimida con aldosterona alta y relación aldosterona/renina elevada, en personas con presión de 130/80 o más. La Endocrine Society 2025 sugiere tamizarlo en toda persona hipertensa y la GPC colombiana 2025 lo incluye en el estudio inicial. La muestra es en la mañana, sentado, y no exige suspender antihipertensivos, pero algunos cambian el resultado.

```yaml
id: COND-M2-TI-008
nombre: Hiperaldosteronismo primario (tamizaje en hipertensos)
modulo: M2
especialidad: tiroides_paratiroides_suprarrenal
tipo: incluida
detectabilidad: D2
activa_refleja_si: ["COND-M1-CA-006 activa (presión >= 130/80)", "hipertensión conocida declarada"]
criterios:
  - id: renina_suprimida
    biomarcador: renin
    condicion: "actividad (ARP) <= 1 ng/mL/h, o concentración directa (DRC) <= 8,2 mU/L"
  - id: aldosterona_alta
    biomarcador: aldosterone
    condicion: ">= 10 ng/dL (277 pmol/L) por inmunoensayo, o >= 7,5 ng/dL (208 pmol/L) por LC-MS/MS"
  - id: arr_alta
    calculo: "aldosterona / renina"
    condicion: "con aldosterona por inmunoensayo: > 20 (ng/dL sobre ng/mL/h) o > 70 (pmol/L sobre mU/L); con LC-MS/MS, cerca de 25 % más bajo"
  - id: zona_repetir
    condicion: "renina suprimida con aldosterona de 5 a 10 ng/dL por inmunoensayo"
regla_central: "renina_suprimida AND aldosterona_alta AND arr_alta"
cortes_locales: "la guía pide preferir los cortes del laboratorio local cuando existan"
repetir_si: ["zona_repetir", "tamizaje negativo con potasio bajo (corregir el potasio y repetir)", "tamizaje positivo con betabloqueador, clonidina o metildopa y aldosterona de 10 a 15 ng/dL por inmunoensayo"]
contexto_obligatorio: ["toma en la mañana, sentado", "lista de antihipertensivos"]
coincidencia:
  alta: "regla_central sin medicamentos que confundan"
  moderada: "regla_central con betabloqueador, IECA, ARA II, diurético o espironolactona, o con TFG < 60 (más falsos positivos)"
modificado_por: ["COND-M2-NE-A01"]
escalamiento: 2
nivel_lenguaje: patron_compatible
confusores: ["betabloqueadores (bajan la renina: falso positivo)", "IECA, ARA II y diuréticos (suben la renina: falso negativo)", "espironolactona o eplerenona", "potasio bajo (baja la aldosterona)"]
guias: ["Endocrine Society 2025, hiperaldosteronismo primario", "GPC Colombia HTA 2025"]
por_verificar: "Cortes tomados del resumen oficial de recomendaciones de la Endocrine Society 2025 en endocrine.org (6 de octubre de 2026); falta leer el texto completo y su tabla de cortes por método. Preferir los cortes del laboratorio aliado si los tiene."
frase_permitida: "En el estudio de tu presión, las hormonas que regulan la sal y el agua (aldosterona y renina) muestran un patrón que vale la pena revisar con tu médico. Es una causa tratable de presión alta."
frases_prohibidas: ["tienes hiperaldosteronismo", "tienes un tumor suprarrenal", "suspende tu medicamento"]
recomendaciones_sugeridas: ["consulta médica", "no suspender medicamentos por cuenta propia"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Presión 148/94; aldosterona 18 ng/dL (inmunoensayo); ARP 0,4 ng/mL/h (relación 45); potasio 3,3 | Activa, coincidencia alta, escalamiento 2; refuerzo por NE-A01 |
| Con betabloqueador | Aldosterona 12 ng/dL; ARP 0,5 (relación 24); toma metoprolol | Activa, coincidencia moderada; repetir tras retirar el betabloqueador si el médico lo considera seguro |
| Zona para repetir | Aldosterona 7 ng/dL; ARP 0,3 | No activa; repetir otro día |
| Negativo | Presión 136/86; aldosterona 9 ng/dL; ARP 2,1 (relación 4,3) | No activa |
| Unidades de concentración | Aldosterona 450 pmol/L; DRC 4 mU/L (relación 112) | Activa |
| Sin presión elevada · PDF ejemplos sin datos de la enfermera | Aldosterona y renina no se pidieron | No aplica |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
