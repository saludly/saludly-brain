## COND-M3-HE-002 · Anemia por déficit de hierro

**Qué detecta.** Anemia (HE-001) con ferritina menor de 15 ng/mL, o menor de 70 si hay inflamación. VCM bajo, RDW alto y saturación de transferrina baja la refuerzan. Siempre se busca la causa: en hombres y en mujeres posmenopáusicas, la pérdida de sangre digestiva es la que más preocupa.

```yaml
id: COND-M3-HE-002
nombre: Anemia por déficit de hierro
modulo: M3
especialidad: hematologia
tipo: incluida
detectabilidad: D1
criterios:
  - id: anemia
    condicion: "COND-M3-HE-001 activa"
  - id: ferritina_baja
    biomarcador: ferritin
    condicion: "< 15 si hs_crp <= 5 mg/L; < 70 si hs_crp > 5 mg/L"
    unidad: ng/mL
  - id: saturacion_baja
    biomarcador: transferrin_saturation
    condicion: "< 20"
    unidad: "%"
  - id: vcm_bajo
    biomarcador: mcv
    condicion: "< límite inferior"
  - id: rdw_alto
    biomarcador: rdw
    condicion: "> límite superior"
regla_central: "anemia AND ferritina_baja"
coincidencia:
  alta: "regla_central AND (saturacion_baja OR vcm_bajo OR rdw_alto)"
  moderada: "regla_central sin señales de apoyo"
  baja: "anemia AND saturacion_baja AND vcm_bajo AND ferritina entre el corte y 30 (vigilar)"
excluye_si: []
escalamiento: 2
dispara: ["reflejas IgA total y anti-transglutaminasa IgA si no hay causa evidente (menstruación abundante, embarazo, dieta)", "COND-M4 sangre oculta en heces se lee junto con este hallazgo"]
nivel_lenguaje: condicion_requiere_evaluacion
confusores: ["suplementos de hierro recientes (pueden subir la ferritina sin corregir el déficit)", "inflamación (manejada con el corte de 70)"]
contexto_causa: ["menstruación abundante", "embarazo", "dieta vegana o vegetariana", "cirugía bariátrica", "donación de sangre frecuente", "sangre oculta positiva (M4)", "H. pylori positivo (M4)", "celiaquía (refleja)"]
guias: ["OMS 2020, ferritina", "OMS 2024, cortes de hemoglobina"]
por_verificar: "La ficha de ferritina cita evidencia reciente con corte de 30 ng/mL; aquí se usa 15 (OMS) y la zona 15 a 30 queda como vigilar."
frase_permitida: "Tu hemoglobina está baja y tus reservas de hierro también. Es la causa más frecuente de anemia y tiene tratamiento, pero hay que encontrar por qué falta el hierro: conviene una consulta médica en las próximas semanas."
frases_prohibidas: ["tienes anemia ferropénica", "toma hierro", "toma sulfato ferroso", "es por la menstruación (sin evaluación médica)"]
recomendaciones_sugeridas: ["consulta médica", "alimentos ricos en hierro con una fruta con vitamina C", "evitar té o café con las comidas principales"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Positivo · PDF mujer 34 años | HE-001 activa; ferritina 7, hs-CRP 0,8, saturación 8,8 %, VCM 78,2, RDW 16,4 | Activa, coincidencia alta, escalamiento 2; IgA y anti-tTG reflejas (negativas: sin señal de celiaquía) |
| Con inflamación | Anemia, ferritina 45, hs-CRP 12, saturación 12 % | Activa (corte 70), coincidencia alta |
| Hombre | Hombre 55 años, anemia, ferritina 9 | Activa, escalamiento 2; la vista médica destaca descartar pérdida digestiva |
| Sin anemia | Hemoglobina ajustada normal, ferritina 9 | No activa (va a HE-003) |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
