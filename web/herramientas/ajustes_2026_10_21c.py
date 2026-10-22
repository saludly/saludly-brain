"""
Tercera ronda de ajustes de la landing (21 de octubre de 2026), pedidos por Carlos:
- Más fluida en el celular:
  · El ciclo de "Prevención que se repite" volvía a pintar TODA la página cada 3,2 s aunque no se viera;
    ahora solo avanza cuando esa sección está en pantalla.
  · Edad biológica: sin luces animadas detrás de las tarjetas de vidrio (el desenfoque se recalculaba en cada cuadro).
  · En el celular, las tarjetas de vidrio son blancas casi opacas, sin desenfoque (beneficios, WhatsApp, edad, camino).
- Portada y edad biológica: el degradado pasa entre tonos de azul (sin el beige/naranja) y cubre toda la pantalla.
- "Tu camino en Saludly" en el celular: sin doble margen, para que el texto respire.
Uso: python web/herramientas/ajustes_2026_10_21c.py   (una sola vez)
"""
import os

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta = os.path.join(WEB, "index.html")
t = open(ruta, encoding="utf-8").read()


def cambiar(viejo, nuevo, veces=1):
    global t
    assert t.count(viejo) == veces, f"se esperaban {veces} y hay {t.count(viejo)} de: {viejo[:90]}"
    t = t.replace(viejo, nuevo)


# ---------- Ciclo: solo cuando la sección está en pantalla ----------
cambiar("    this._cyc = setInterval(() => this.setState({ cycle: (this.state.cycle + 1) % 5 }), 3200);",
        "    // Solo avanza con la sección en pantalla: cada avance vuelve a pintar toda la página.\n"
        "    this._cyc = setInterval(() => { if (this._cicloVisible) this.setState({ cycle: (this.state.cycle + 1) % 5 }); }, 3200);")
cambiar("      this._io.observe(sentinel);\n",
        "      this._io.observe(sentinel);\n"
        "      const ciclo = document.getElementById('sl-ciclo');\n"
        "      if (ciclo) { this._cio2 = new IntersectionObserver((es) => { this._cicloVisible = es[0].isIntersecting; }); this._cio2.observe(ciclo); }\n")

# ---------- Portada: tonos de azul en toda la pantalla ----------
cambiar('<div class="sl-glow" aria-hidden="true" style="position: absolute; left: 0; top: 0; bottom: 0; width: 64%;',
        '<div class="sl-glow" aria-hidden="true" style="position: absolute; left: 0; top: 0; bottom: 0; width: 100%;')
cambiar('<div class="sl-glow-warm" style="position: absolute; inset: 0; background: radial-gradient(42% 46% at 30% 56%, rgba(232,206,150,0.72) 0%, rgba(240,222,182,0.38) 45%, rgba(253,253,253,0) 100%), radial-gradient(30% 34% at 58% 30%, rgba(238,214,168,0.42) 0%, rgba(253,253,253,0) 100%)"></div>',
        '<div class="sl-glow-warm" style="position: absolute; inset: 0; background: radial-gradient(55% 60% at 22% 58%, rgba(120,192,248,0.62) 0%, rgba(170,214,250,0.32) 45%, rgba(253,253,253,0) 100%), radial-gradient(45% 50% at 78% 28%, rgba(150,205,250,0.45) 0%, rgba(253,253,253,0) 100%)"></div>')
cambiar('<div class="sl-glow-cool" style="position: absolute; inset: 0; opacity: 0; background: radial-gradient(42% 46% at 30% 56%, rgba(43,158,240,0.36) 0%, rgba(140,200,246,0.22) 45%, rgba(253,253,253,0) 100%), radial-gradient(30% 34% at 58% 30%, rgba(43,158,240,0.22) 0%, rgba(253,253,253,0) 100%)"></div>',
        '<div class="sl-glow-cool" style="position: absolute; inset: 0; opacity: 0; background: radial-gradient(55% 60% at 28% 52%, rgba(22,112,184,0.42) 0%, rgba(43,158,240,0.24) 45%, rgba(253,253,253,0) 100%), radial-gradient(45% 50% at 72% 32%, rgba(43,158,240,0.34) 0%, rgba(253,253,253,0) 100%)"></div>')

# ---------- Edad biológica: azul fijo, sin animación detrás del vidrio ----------
cambiar('<div class="sl-glow-warm" style="position: absolute; inset: -6%; background: radial-gradient(38% 42% at 22% 30%, rgba(228,196,128,0.85) 0%, rgba(236,212,160,0.42) 45%, rgba(250,251,253,0) 100%), radial-gradient(34% 40% at 80% 72%, rgba(232,200,138,0.72) 0%, rgba(250,251,253,0) 100%), radial-gradient(28% 32% at 56% 18%, rgba(240,214,166,0.55) 0%, rgba(250,251,253,0) 100%)"></div>',
        '<div style="position: absolute; inset: -6%; background: radial-gradient(38% 42% at 22% 30%, rgba(120,192,248,0.55) 0%, rgba(170,214,250,0.28) 45%, rgba(250,251,253,0) 100%), radial-gradient(34% 40% at 80% 72%, rgba(43,158,240,0.32) 0%, rgba(250,251,253,0) 100%), radial-gradient(28% 32% at 56% 18%, rgba(150,205,250,0.4) 0%, rgba(250,251,253,0) 100%)"></div>')
cambiar('<div class="sl-glow-cool" style="position: absolute; inset: -6%; opacity: 0; background: radial-gradient(38% 42% at 22% 30%, rgba(43,158,240,0.5) 0%, rgba(120,190,245,0.28) 45%, rgba(250,251,253,0) 100%), radial-gradient(34% 40% at 80% 72%, rgba(43,158,240,0.45) 0%, rgba(250,251,253,0) 100%), radial-gradient(28% 32% at 56% 18%, rgba(43,158,240,0.32) 0%, rgba(250,251,253,0) 100%)"></div>\n',
        '')

# ---------- Celular: vidrio sin desenfoque y el camino sin doble margen ----------
cambiar("@media (prefers-reduced-motion:reduce){#sl-carga{display:none}",
        """/* Celular y tabletas: el desenfoque del vidrio es caro al hacer scroll; se cambia por blanco casi opaco */
@media (max-width:900px),(hover:none){
.sl-glass,.sl-ben-card,.sl-wa-item,.sl-camino-vidrio{-webkit-backdrop-filter:none !important;backdrop-filter:none !important}
.sl-ben-card,.sl-wa-item,.sl-camino-vidrio{background:rgba(255,255,255,.88) !important}
.sl-glass{background:rgba(255,255,255,.82) !important}
}
@media (max-width:600px){
.sl-memb-photo.sl-camino{padding:10px !important;border-radius:28px !important}
.sl-camino-vidrio{padding:22px 20px !important;border-radius:22px !important}
.sl-camino-vidrio li{gap:12px !important}
.sl-camino-vidrio li > span{width:28px !important;height:28px !important;font-size:13px !important}
}
@media (prefers-reduced-motion:reduce){#sl-carga{display:none}""")
cambiar('<div class="sl-memb-photo" style="position: relative; border-radius: 36px; overflow: hidden; padding: clamp(28px, 4vw, 44px);',
        '<div class="sl-memb-photo sl-camino" style="position: relative; border-radius: 36px; overflow: hidden; padding: clamp(28px, 4vw, 44px);')
cambiar('<div style="border-radius: 28px; padding: clamp(22px, 3vw, 32px); background: rgba(255,255,255,0.62); -webkit-backdrop-filter: blur(18px);',
        '<div class="sl-camino-vidrio" style="border-radius: 28px; padding: clamp(22px, 3vw, 32px); background: rgba(255,255,255,0.62); -webkit-backdrop-filter: blur(18px);')

open(ruta, "w", encoding="utf-8").write(t)
print("listo")
