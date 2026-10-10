## COND-M4-GA-006 · Enfermedad celíaca (prueba dirigida)

**Qué detecta.** Anti-transglutaminasa IgA positiva con IgA total normal. No se tamiza a toda la población: el laboratorio corre las reflejas solo con déficit de hierro sin causa, transaminasas altas, enfermedad tiroidea o familiar de primer grado celíaco. La persona debe estar comiendo gluten. La biopsia confirma.

```yaml
id: COND-M4-GA-006
nombre: Enfermedad celíaca (prueba dirigida)
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D3
activa_refleja_si: ["COND-M3-HE-002 o HE-003 sin causa evidente", "COND-M4-GA-002 activa", "condición tiroidea activa en M2", "familiar de primer grado con celiaquía"]
criterios:
  - id: ttg_positivo
    biomarcador: anti_ttg_iga
    condicion: "> límite superior del laboratorio"
  - id: iga_normal
    biomarcador: iga
    condicion: "dentro del intervalo"
  - id: iga_baja
    biomarcador: iga
    condicion: "< límite inferior del laboratorio"
  - id: dieta_con_gluten
    contexto: cuestionario
    condicion: "come gluten de forma habitual"
regla_central: "ttg_positivo AND iga_normal"
no_interpretable_si: ["iga_baja (el anti-tTG IgA puede salir falsamente negativo; la vista médica sugiere pruebas basadas en IgG)", "dieta sin gluten"]
coincidencia:
  alta: "regla_central AND dieta_con_gluten"
  moderada: "regla_central sin dato de dieta"
escalamiento: 2
nivel_lenguaje: patron_compatible
guias: ["ACG 2023, enfermedad celíaca"]
por_verificar: "Guía leída solo por resumen; confirmar indicaciones de prueba dirigida."
frase_permitida: "Una prueba relacionada con la intolerancia al gluten (anti-transglutaminasa) salió positiva. Sigue comiendo como siempre y pide una consulta médica: confirmarlo requiere otros estudios."
frases_prohibidas: ["tienes celiaquía", "deja el gluten"]
recomendaciones_sugeridas: ["no dejar el gluten antes de la evaluación médica", "consulta médica"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo | Déficit de hierro, anti-tTG 48 (menor de 7), IgA normal, come gluten | Activa, coincidencia alta, escalamiento 2 |
| Déficit de IgA | Anti-tTG 2, IgA 5 (bajo) | No interpretable; sugiere pruebas basadas en IgG |
| Negativo · PDF mujer 34 años | Anti-tTG 2,1, IgA 210 | No activa: sin señal de celiaquía |
| Sin gluten | Anti-tTG 3, dieta sin gluten | No interpretable |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
