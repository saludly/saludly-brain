## COND-M1-EM-A04 · Resistencia a la insulina por TyG y TG/HDL

**Qué detecta.** Índice triglicéridos-glucosa (TyG) mayor de 8,8 o relación triglicéridos/HDL mayor de 3,0 (cortes provisionales). Se calculan con lo que ya se mide, sin depender de la insulina; el TyG se validó en población latinoamericana. Refuerza la prediabetes y el síndrome metabólico. En diabetes no aporta.

> Agregada el 10 de octubre de 2026 por aprobación de Carlos (propuesta de ampliación de condiciones solo con sangre). Umbrales en propuesta: se marcan "por verificar" hasta leer la fuente completa.

```yaml
id: COND-M1-EM-A04
nombre: Resistencia a la insulina por TyG y TG/HDL
modulo: M1
especialidad: endocrinologia_metabolica
tipo: apoyo
detectabilidad: D1
criterios:
  - id: tyg_alto
    biomarcador: tyg_index
    condicion: "> 8,8"
  - id: tg_hdl_alta
    biomarcador: tg_hdl_ratio
    condicion: "> 3,0"
regla_central: "tyg_alto OR tg_hdl_alta"
contexto_obligatorio: ["ayuno_horas >= 8"]
no_aplica_si: ["COND-M1-EM-002 activa o diabetes conocida"]
escalamiento: modifica
modifica: ["COND-M1-EM-001", "COND-M1-EM-003"]
nivel_lenguaje: patron_compatible
confusores: ["ayuno insuficiente", "alcohol reciente (triglicéridos)"]
guias: ["Simental-Mendía 2008; Guerrero-Romero 2010 (TyG)", "McLaughlin 2003 (TG/HDL)"]
por_verificar: "Cortes de 8,8 (TyG) y 3,0 (TG/HDL); buscar cortes en población colombiana."
frase_permitida: "Dos cálculos con tus triglicéridos y tu glucosa sugieren que tu cuerpo usa la insulina con más esfuerzo de lo ideal. La actividad física y la alimentación ayudan mucho."
frases_prohibidas: ["tienes diabetes", "tienes resistencia a la insulina (dicho como diagnóstico)"]
recomendaciones_sugeridas: ["caminar después de las comidas", "reducir azúcares y harinas refinadas"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Ambos | TG 210, glucosa 104, HDL 38 | Apoyo (TyG 9,3 y TG/HDL 5,5) |
| Solo TG/HDL | TG 160, glucosa 82, HDL 45 | Apoyo |
| Negativo | TG 90, glucosa 85, HDL 60 | No activa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
