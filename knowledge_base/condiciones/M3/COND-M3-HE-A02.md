## COND-M3-HE-A02 · Leucocitos, neutrófilos o linfocitos fuera de rango (apoyo)

**Qué detecta.** Recuentos de glóbulos blancos fuera del intervalo del laboratorio. No hay umbral de guía para tamizaje, así que se muestran como valores fuera de rango, se repiten y solo escalan por bandera crítica del laboratorio.

```yaml
id: COND-M3-HE-A02
nombre: Leucocitos, neutrófilos o linfocitos fuera de rango
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: fuera_de_rango
    biomarcadores: [wbc, neutrophils_abs, lymphocytes_abs]
    condicion: "fuera del intervalo del laboratorio"
regla_central: "fuera_de_rango"
escalamiento:
  base: 1
  bandera_critica_laboratorio: 3
  mas_de_una_linea_alterada_con_anemia_o_plaquetas_bajas: 2
efecto: "Valor fuera de rango con sugerencia de repetir; si hay alteración de dos o más líneas (glóbulos rojos, blancos, plaquetas), la vista médica lo destaca."
confusores: ["infección reciente", "corticoides (suben neutrófilos, bajan linfocitos)", "ejercicio intenso", "tabaquismo"]
guias: ["Intervalo del laboratorio"]
por_verificar: "Escalamiento 2 para alteración de varias líneas es propuesta de Saludly."
frase_permitida: "Tus {glóbulos blancos o tipo de célula} están {por encima o por debajo} del rango. Es frecuente tras una infección; conviene repetirlo."
frases_prohibidas: ["tienes leucemia", "tienes las defensas bajas", "tienes una infección"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Leve | Neutrófilos 1,6 (laboratorio desde 1,8) | Valor fuera de rango, escalamiento 1 |
| Varias líneas | Leucocitos 2,9, plaquetas 95, anemia | Escalamiento 2 |
| Negativo · PDF ejemplos | Leucocitos 7,8 y 6,1 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
