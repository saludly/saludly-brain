## COND-M4-IN-A02 · Parasitosis intestinal (apoyo)

**Qué detecta.** Parásitos en el coprológico. Se separan los patógenos de los comensales (que no requieren tratamiento) y se cruza con la eosinofilia del módulo M3. La fuente colombiana sigue pendiente.

```yaml
id: COND-M4-IN-A02
nombre: Parasitosis intestinal
modulo: M4
especialidad: infectologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: parasito_patogeno
    biomarcador: stool_parasites
    condicion: "Giardia, Entamoeba histolytica/dispar, helmintos u otro patógeno según la lista firmada por el médico"
  - id: parasito_comensal
    biomarcador: stool_parasites
    condicion: "comensal según la lista firmada por el médico"
regla_central: "parasito_patogeno"
modificado_por: ["COND-M3-HE-A03"]
escalamiento:
  parasito_patogeno: 1
  parasito_comensal: 0
guias: ["Pendiente de fuente colombiana"]
por_verificar: "Lista de parásitos patógenos y comensales; algunos (por ejemplo, Blastocystis) tienen significado discutido. El médico debe firmar la lista."
frase_permitida: "En tu muestra de heces se encontró un parásito que suele requerir tratamiento. Consulta con tu médico."
frase_comensal: "En tu muestra apareció un microorganismo que normalmente no causa enfermedad ni necesita tratamiento."
frases_prohibidas: ["toma antiparasitario", "desparasítate"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Patógeno | Quistes de Giardia | Activa, escalamiento 1 |
| Con eosinofilia | Huevos de helminto, eosinófilos 0,9 × 10³/µL | Activa, reforzada por HE-A03 |
| Comensal | Quistes de Entamoeba coli | Informativo, escalamiento 0 |
| Negativo · PDF ejemplos | No se observaron parásitos | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
