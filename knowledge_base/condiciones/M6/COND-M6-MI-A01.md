## COND-M6-MI-A01 · Lectura por edad del panel (apoyo)

**Qué detecta.** No es una condición: reúne en un solo lugar las reglas por edad que ya están repartidas en los módulos, para que el motor las aplique siempre igual. La edad entra en la interpretación, nunca en la selección de pruebas.

```yaml
id: COND-M6-MI-A01
nombre: Lectura por edad del panel
modulo: M6
especialidad: medicina_interna_y_envejecimiento
tipo: apoyo
detectabilidad: D1
reglas:
  - "menores de 18 años: fuera del alcance de la versión 1"
  - "SCORE2-PURE solo entre 40 y 69 años (M1 CA-005)"
  - "TSH: corte de decisión 5,0 de 18 a 60 años y 6,0 desde los 61 (M2 TI-001)"
  - "FSH: condición solo en menores de 40; contexto de 40 a 44; sin uso para menopausia desde los 45 (M5 MU-002)"
  - "PSA: tamizaje formal de 50 a 75; fuera de ese rango, valor a revisar (M5 UR-001)"
  - "Sangre oculta: tamizaje formal de 50 a 75; positivo a cualquier edad remite (M4 GA-004)"
  - "FIB-4: menos confiable en menores de 35; un valor bajo no descarta fibrosis desde los 65 (M4 GA-001)"
  - "Desnutrición: IMC < 22 desde los 70 años (M6 MI-001)"
  - "Hemoglobina: la OMS advierte que faltan datos en mayores de 65; la vista médica lo anota (M3 HE-001)"
  - "Recordatorios: cuello uterino 30-65, mamografía 50-69, colorrectal 50-75 (M5)"
  - "PhenoAge: solo dentro del rango de edad del modelo (MI-A02)"
efecto: "Cada ficha consulta esta tabla; si una regla cambia aquí, cambia en todo el motor."
guias: ["Reglas de los Lotes 1 a 6", "OMS 2024, cortes de hemoglobina"]
```

**Casos de prueba**

| Caso | Datos | Resultado esperado |
| --- | --- | --- |
| Hombre 46 años | — | SCORE2-PURE aplica; PSA y sangre oculta fuera de franja formal; sin recordatorios |
| Mujer 34 años | — | Sin SCORE2-PURE; FSH interpretable como condición; recordatorio de cuello uterino |
| Persona de 17 años | — | Fuera del alcance; no se procesa |

**Firma médica**

- [ ] Aprobada  - [ ] Aprobada con cambios  - [ ] Rechazada
- Cambios:
- Nombre y registro ReTHUS:
- Fecha:
