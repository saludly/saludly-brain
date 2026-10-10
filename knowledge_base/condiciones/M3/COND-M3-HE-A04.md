## COND-M3-HE-A04 · Rasgo talasémico probable

**Qué detecta.** Glóbulos rojos pequeños (VCM menor de 80 fL) sin déficit de hierro (ferritina de 30 ng/mL o más) e índice de Mentzer (VCM ÷ eritrocitos) menor de 13. Es un rasgo heredado que casi nunca da síntomas, pero importa: evita que se recomiende hierro a quien no le falta. Lo confirma la electroforesis de hemoglobina, que corre como refleja.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M3-HE-A04
nombre: Rasgo talasémico probable
modulo: M3
especialidad: hematologia
tipo: apoyo
detectabilidad: D1
criterios:
  - id: microcitosis
    biomarcador: mcv
    condicion: "< 80"
    unidad: fL
  - id: hierro_normal
    biomarcador: ferritin
    condicion: ">= 30"
    unidad: ng/mL
  - id: mentzer_bajo
    biomarcador: mentzer_index
    condicion: "< 13"
  - id: electroforesis
    biomarcador: hb_electrophoresis
    condicion: "HbA2 >= 3,5 % o informe compatible con talasemia"
regla_central: "microcitosis AND hierro_normal AND mentzer_bajo"
estados: {sin_electroforesis: "pendiente_refleja", electroforesis_compatible: "apoyo (confirmado)", electroforesis_normal: "apoyo (no descarta rasgo alfa)"}
escalamiento: modifica
efecto: "Quita las recomendaciones de hierro de COND-M3-HE-002 y HE-003 si estuvieran activas."
nivel_lenguaje: patron_compatible
confusores: ["déficit de hierro asociado (baja la HbA2)", "transfusión reciente"]
guias: ["BSH, tamizaje de hemoglobinopatías", "Mentzer 1973"]
frase_permitida: "Tus glóbulos rojos son pequeños, pero tu hierro está bien. Esto suele deberse a un rasgo heredado que no da síntomas; un examen adicional lo confirma."
frases_prohibidas: ["tienes talasemia", "tienes una enfermedad de la sangre"]
recomendaciones_sugeridas: ["no tomar hierro sin indicación médica", "contarlo antes de un embarazo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Probable sin electroforesis | VCM 68, eritrocitos 6,1, ferritina 80 | Pendiente de refleja (electroforesis de hemoglobina) |
| Confirmado | Lo mismo con HbA2 5,1 % | Apoyo confirmado |
| Déficit de hierro | VCM 72, eritrocitos 4,1, ferritina 7 | No activa (manda el déficit de hierro) |
| Negativo · PDF ejemplos | VCM normal (hombre) y ferritina baja (mujer) | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
