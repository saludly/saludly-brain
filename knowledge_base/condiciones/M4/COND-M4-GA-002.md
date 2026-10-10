## COND-M4-GA-002 · Alteración hepatocelular

**Qué detecta.** ALT por encima del valor sano de la ACG (33 UI/L en hombres, 25 en mujeres), aunque esté dentro del rango del laboratorio. Entre ambos valores es limítrofe; por encima del laboratorio es alto. La causa más común es metabólica, pero también alcohol, hepatitis virales, medicamentos y suplementos. Siempre se repite antes de evaluar.

```yaml
id: COND-M4-GA-002
nombre: Alteración hepatocelular
modulo: M4
especialidad: gastroenterologia_hepatologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: alt_limitrofe
    biomarcador: alt
    condicion: "> 33 si hombre; > 25 si mujer; y <= límite superior del laboratorio"
    unidad: UI/L
  - id: alt_alta
    biomarcador: alt
    condicion: "> límite superior del laboratorio"
  - id: alt_muy_alta
    biomarcador: alt
    condicion: "> 3 veces el límite superior del laboratorio"
  - id: ast_alta
    biomarcador: ast
    condicion: "> límite superior del laboratorio"
regla_central: "alt_alta OR (ast_alta AND NOT patrón muscular)"
coincidencia:
  alta: "regla_central confirmada en una segunda medición"
  moderada: "regla_central en una sola medición"
  baja: "alt_limitrofe (vigilar)"
escalamiento:
  base: 1
  si_alt_muy_alta: 2
  bandera_critica_laboratorio: 3
dispara: ["IgA total y anti-tTG IgA reflejas (GA-006)", "lectura conjunta con hepatitis B y C (IN-001, IN-002)", "FIB-4 (GA-001)"]
modificado_por: ["COND-M4-GA-A02", "relación hepática metabólica (documento 03)"]
nivel_lenguaje: patron_compatible
confusores: ["ejercicio intenso 48 h (AST y ALT de músculo)", "patrón muscular CK alta", "hemólisis de la muestra", "medicamentos, suplementos y productos herbales", "alcohol"]
guias: ["ACG 2017, evaluación de pruebas hepáticas alteradas"]
regla_seguridad: "nunca recomendar 'desintoxicación hepática' ni atribuir el hallazgo a hígado graso o alcohol de forma automática"
frase_permitida: "Una de tus enzimas del hígado (ALT) está por encima de lo esperado. Hay varias causas posibles, la mayoría relacionadas con hábitos; conviene repetirla y revisarla con tu médico."
frase_vigilar: "Tu ALT está dentro del rango del laboratorio, pero por encima del valor que las guías consideran plenamente sano. Lo vigilamos."
frases_prohibidas: ["tienes hígado graso", "tienes hepatitis", "tu hígado está dañado", "haz un detox"]
recomendaciones_sugeridas: ["reducir alcohol", "revisar suplementos y productos herbales con el médico", "repetir en unas semanas", "actividad física y menos azúcar"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF hombre 46 años | ALT 58 (laboratorio hasta 50), AST 39, CK normal | Activa, coincidencia moderada, escalamiento 1; ligada a la relación hepática metabólica |
| Limítrofe | Mujer, ALT 31 (laboratorio hasta 35) | Vigilar |
| Muy alta | ALT 190 (laboratorio hasta 50) | Activa, escalamiento 2 |
| Muscular | ALT 48, AST 85, CK 2.400, ejercicio el día anterior | No activa; patrón muscular |
| Negativo · PDF mujer 34 años | ALT 18 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
