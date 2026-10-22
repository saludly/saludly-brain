"""
Cuarta ronda (21 de octubre de 2026): en la animación "Qué medimos" (QueMedimos.dc.html), la silueta dibujada se cambia
por la silueta real de la app (app/src/assets/body.png, copiada como web/assets/cuerpo.png), y los puntos de los sistemas
se mueven a las mismas posiciones que usa la app (SISTEMAS en app/src/lib/datos.ts). También corrige el último "120+".
La imagen va dentro del mismo <svg> de 274×404: alto útil de la figura 390 px, centrada.
Uso: python web/herramientas/ajustes_2026_10_21d.py   (una sola vez)
"""
import os, re

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta = os.path.join(WEB, "QueMedimos.dc.html")
t = open(ruta, encoding="utf-8").read()

# body.png mide 768×1280 y la figura ocupa (130, 93)–(629, 1174). Escala 390/1081 y centrada en 274 de ancho.
ESC = 390 / 1081
X0, Y0 = round(137 - (130 + 499 / 2) * ESC, 1), round(4 - 93 * ESC, 1)
W, H = round(768 * ESC, 1), round(1280 * ESC, 1)
pos = lambda top, left: (round(X0 + left * W, 1), round(Y0 + top * H, 1))

# 1. La figura: fuera la sombra, el cuerpo dibujado y las dos líneas; entra la imagen
ini = t.index('<ellipse cx="137" cy="396" rx="62" ry="7" fill="url(#qmFloor)"></ellipse>')
fin = t.index('<path d="M108 128 C120 136 154 136 166 128" stroke="#E1E6EB" stroke-width="1.2" fill="none"></path>') + len('<path d="M108 128 C120 136 154 136 166 128" stroke="#E1E6EB" stroke-width="1.2" fill="none"></path>')
t = t[:ini] + f'<image href="./assets/cuerpo.png" x="{X0}" y="{Y0}" width="{W}" height="{H}" preserveAspectRatio="xMidYMid meet"></image>' + t[fin:]

# 2. Los puntos, en las posiciones de la app (top, left como fracción de la imagen)
puntos = {
    "TIROIDES": (0.19, 0.50, "der"),
    "CARDIOVASCULAR": (0.31, 0.44, "izq"),
    "HÍGADO": (0.43, 0.56, "der"),
    "METABOLISMO": (0.50, 0.47, "izq"),
    "SANGRE": (0.64, 0.48, "der"),
}
for etiqueta, (top, left, lado) in puntos.items():
    cx, cy = pos(top, left)
    tx = round(cx + 11 if lado == "der" else cx - 11, 1)
    # cada grupo: uno o dos círculos con cx/cy y un <text x y> con la etiqueta
    patron = re.compile(r'(<g opacity="\{\{d\d\}\}"[^>]*>(?:(?!</g>\s*<g opacity="\{\{d).)*?' + re.escape(etiqueta) + r'</text>)', re.S)
    m = patron.search(t)
    assert m, etiqueta
    bloque = m.group(1)
    nuevo = re.sub(r'cx="[\d.]+" cy="[\d.]+"', f'cx="{cx}" cy="{cy}"', bloque)
    nuevo = re.sub(r'<text x="[\d.]+" y="[\d.]+"( text-anchor="end")?', (f'<text x="{tx}" y="{cy + 3}"' + (' text-anchor="end"' if lado == "izq" else "")), nuevo)
    t = t.replace(bloque, nuevo)

assert t.count("120+ biomarcadores en nueve sistemas de salud.") == 1
t = t.replace("120+ biomarcadores en nueve sistemas de salud.", "100+ biomarcadores en nueve sistemas de salud.")
open(ruta, "w", encoding="utf-8").write(t)
print("listo", X0, Y0, W, H)
