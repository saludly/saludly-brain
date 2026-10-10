## COND-M5-UR-001 · PSA elevado

**Qué detecta.** PSA total por encima de 4,0 ng/mL o del límite del laboratorio. La edad decide la lectura: de 50 a 75 años es el tamizaje de la Res. 3280 y el informe remite al médico para tacto rectal y evaluación; fuera de ese rango es "valor a revisar con tu médico". Entre 4 y 10 ng/mL el laboratorio corre PSA libre como refleja. Nunca se habla de cáncer.

```yaml
id: COND-M5-UR-001
nombre: PSA elevado
modulo: M5
especialidad: urologia_y_salud_del_hombre
tipo: incluida
detectabilidad: D3
criterios:
  - id: psa_alto
    biomarcador: psa_total
    condicion: "> 4.0 o > límite superior del laboratorio"
    unidad: ng/mL
  - id: zona_gris
    biomarcador: psa_total
    condicion: "4.0-10.0"
  - id: psa_muy_alto
    biomarcador: psa_total
    condicion: "> 10.0"
  - id: edad_tamizaje
    condicion: "50 a 75 años"
regla_central: "sexo == hombre AND consentimiento_psa AND psa_alto"
no_medido_si: ["sin consentimiento de PSA"]
ajustes: ["finasterida o dutasterida: el PSA medido se multiplica por 2 para interpretarlo"]
coincidencia:
  alta: "regla_central sin confusores"
  moderada: "regla_central con eyaculación o ciclismo en 48 horas, infección urinaria o prostatitis reciente"
modificado_por: ["COND-M5-UR-A02"]
escalamiento:
  en_edad_tamizaje: 2
  fuera_de_edad: 1
  si_psa_muy_alto: 2
dispara: ["PSA libre refleja si zona_gris"]
nivel_lenguaje: resultado_observado
contexto_vista_medica: ["antecedente familiar de cáncer de próstata", "ascendencia africana (AUA sugiere PSA basal más temprano)"]
guias: ["Res. 3280 de 2018", "AUA/SUO 2026, detección temprana de cáncer de próstata"]
por_verificar: "Corte de 4,0 ng/mL y regla de duplicar con inhibidores de 5-alfa reductasa: práctica habitual, confirmar en la guía AUA/SUO completa."
frase_permitida_tamizaje: "Tu PSA, una proteína que produce la próstata, salió por encima del valor de referencia. Puede subir por varias causas benignas; conviene una consulta médica en las próximas semanas para evaluarlo."
frase_permitida_fuera_de_edad: "Tu PSA salió por encima del valor de referencia. Es un valor para revisar con tu médico."
frases_prohibidas: ["tienes cáncer de próstata", "tienes un tumor", "necesitas biopsia"]
recomendaciones_sugeridas: ["consulta médica", "evitar eyaculación y bicicleta 48 horas antes de repetirlo"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Tamizaje | Hombre 58 años, PSA 5,6, con consentimiento | Activa, escalamiento 2; PSA libre refleja |
| Fuera de edad | Hombre 44 años, PSA 4,8 | Activa, escalamiento 1 |
| Muy alto | Hombre 66 años, PSA 14 | Activa, escalamiento 2 |
| Finasterida | PSA 2,6 con finasterida (equivale a 5,2) | Activa |
| Sin consentimiento | Sin consentimiento de PSA | No medido |
| Negativo · PDF hombre 46 años | PSA 1,10 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
