---
name: Saludly
colors:
  ink: "oklch(0.24 0.02 255)"        # texto principal y botón principal
  ink-muted: "oklch(0.5 0.015 255)"  # texto secundario (contraste ≥ 4,5:1 sobre blanco)
  ink-faint: "oklch(0.66 0.012 255)" # solo placeholders, nunca texto que haya que leer
  rule: "oklch(0.24 0.02 255 / 9%)"  # líneas y bordes
  ficha: "#f2f4f7"                   # fondo de fichas, búsqueda y botones grises
  marca: "#2793ff"                   # azul del logo (la "y" animada)
  whatsapp: "#25d366"                # solo botones que abren WhatsApp
  optimal: "oklch(0.58 0.19 253)"    # en rango / selección
  attention: "naranja claro"         # fuera de rango (ver styles.css)
  critical: "naranja oscuro"         # atención pronta y errores
typography:
  family: Manrope
  titulo: 32px / 1.12, peso normal
  texto: 17px / relajado
  minimo: 16px
rounded:
  ficha: 22px
  boton: full
spacing:
  gutter: 24px
  boton-alto: 56px
---

# Sistema de diseño de Saludly (app del paciente)

Fuente de verdad de los tokens: `src/styles.css` (`:root` y `@theme`). Este archivo dice **cuándo** usar cada uno.
Si agregas un color, agrégalo primero a `styles.css` y aquí; en los componentes, nunca un `#hex` suelto.

## Carácter

Blanco, mínimo y clínico, con la calidez de un onboarding de celular (referencia: Morse). Una pregunta por pantalla,
título grande a la izquierda, fichas grises y un botón grande abajo. Se usa en el celular, de día y con una mano.

## Reglas

1. **Texto de 16 px o más** en todo lo que la persona tiene que leer (etiquetas, ayudas, errores, enlaces legales).
2. **Un solo acento por pantalla**: el botón negro (`ink`). El verde de WhatsApp solo en botones que abren WhatsApp.
3. **Nada que "parezca IA"** (Carlos, 22 y 24 oct 2026): sin letras pequeñas en mayúsculas separadas, sin monoespaciada
   de adorno, sin avatares falsos con iniciales, sin cuadrículas de tarjetas con íconos en círculos de color, sin emojis
   como diseño (en WhatsApp sí van).
4. **Selección**: lista simple con su círculo (una opción) o su casilla (varias). El círculo o la casilla es el único indicador.
5. **Botón deshabilitado**: siempre con una línea encima que dice qué falta para seguir.
6. **Estados**: cada pantalla con formulario guarda su avance; los errores dicen qué pasó y qué hacer, en tú.
7. **Accesibilidad**: áreas táctiles de 44 px o más, foco visible, casillas y radios reales (no solo `aria-pressed`).

## Componentes

- `PantallaPre` (`src/components/FlujoPre.tsx`): marco de cada paso del pre-registro (atrás, barra de pasos, título,
  contenido y botón fijo abajo con su motivo).
- `Ficha`: campo gris con la etiqueta adentro, arriba del valor (la etiqueta nunca desaparece).
- `Opcion` (`src/components/Formulario.tsx`): opción de una lista con casilla o círculo.
- La "y" animada (`src/lib/trazo_y.ts`) es el único movimiento de marca: pantalla final y espera de resultados.
