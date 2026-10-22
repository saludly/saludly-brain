"""
Quinta ronda (22 de octubre de 2026): modo oscuro, portada sin botón de play, sin desenfoques y video liviano.

1. Modo oscuro automático, solo en celulares y tabletas con el modo oscuro activo (ver OSCURO; en el computador la
   página siempre se ve clara, decisión de Carlos del 22 oct 2026), sin costo al hacer scroll: cada color de los estilos se
   vuelve var(--o-<rol>-<color>, <color original>). En modo claro no hay variables definidas y queda el color de
   siempre; en modo oscuro un solo bloque :root las define. El rol sale de la propiedad (texto, fondo, borde o trazo)
   y el color oscuro se calcula con la luminosidad (ver oscuro()). Los colores de los atributos SVG se cambian con
   selectores de atributo, y los que pone el JS pasan por slC(), que devuelve el color oscuro si toca.
   Quedan como están las piezas que ya son oscuras: el menú flotante, el pie de página y las luces de la portada.
2. Portada: video oscuro (negativo del original, partículas claras sobre negro) con <source media>, póster como
   fondo del <video> (sin atributo poster), sin el botón de play de iOS (modo de bajo consumo) y, si el navegador
   bloquea la reproducción, arranca al primer toque. Videos a 1280×960: de 9 MB a menos de 2 MB.
3. Sin backdrop-filter en ninguna pantalla (antes solo en el celular): el vidrio pasa a blanco casi opaco.

Uso: python web/herramientas/ajustes_2026_10_22.py   (una sola vez, sobre la versión del commit c2c5e31)
Los videos nuevos deben estar en assets/ (se generan con ffmpeg, ver VIDEOS al final).
"""
import colorsys, os, re

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVOS = ["index.html", "Paso1Tubo.dc.html", "Paso2Agente.dc.html", "Paso3App.dc.html", "QueMedimos.dc.html"]
# Cuándo se ve oscura: modo oscuro y pantalla táctil sin mouse (celulares y tabletas, no computadores)
OSCURO = "(prefers-color-scheme: dark) and (hover: none) and (pointer: coarse)"

COLOR = re.compile(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b|rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+\s*)?\)")
ROL = {
    "color": "texto", "-webkit-text-fill-color": "texto", "caret-color": "texto",
    "background": "fondo", "background-color": "fondo", "background-image": "fondo", "fill": "fondo", "stop-color": "fondo",
    "border": "borde", "border-top": "borde", "border-bottom": "borde", "border-left": "borde", "border-right": "borde",
    "border-color": "borde", "outline": "borde", "outline-color": "borde", "text-decoration-color": "borde",
    "stroke": "trazo",
}
# Reglas de <style> que no se tocan (botones blancos del menú, que ya es negro)
SELECTORES_FIJOS = (".sl-btn-white", ".sl-link-row")
# Valores del JS con su propio color oscuro (marca en la línea -> clave para slC): la ficha activa del ciclo es
# azul marino, que sobre negro casi no se ve; en modo oscuro pasa al azul de marca.
JS_FIJOS = {"bg: on ?": "ciclo"}
JS_ESPECIALES = {"ciclo#0A2236": "#2B9EF0"}


def a_rgb(c):
    if c.startswith("#"):
        h = c[1:]
        if len(h) == 3:
            h = "".join(x * 2 for x in h)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), None
    n = re.findall(r"[\d.]+", c)
    return tuple(int(x) for x in n[:3]), (n[3] if len(n) > 3 else None)


def oscuro(rgb, rol):
    """El color equivalente en modo oscuro. Los azules, verdes y naranjas de marca se quedan; los neutros se invierten."""
    h, l, s = colorsys.rgb_to_hls(*(x / 255 for x in rgb))
    saturado = s > 0.45 and 0.25 < l < 0.75
    if rol == "js":
        rol = "fondo" if l > 0.6 else "texto"
    if rol == "trazo":
        rol = "borde" if l > 0.7 else "texto"
    if rol == "borde" and l <= 0.6:
        rol = "texto"
    if rol == "texto":
        if saturado:
            l = max(l, 0.62)
        elif l < 0.6:
            l, s = 0.95 - l * 0.5, s * 0.6
    elif rol == "fondo":
        if saturado or l <= 0.6:
            pass  # ya es oscuro o es color de marca
        elif l > 0.85:
            l = 0.075 if rgb == (255, 255, 255) else (1 - l) * 0.9
        else:
            l = 1 - l
    elif rol == "borde":
        l, s = (1 - l) * 0.8 + 0.1, s * 0.8
    return tuple(round(x * 255) for x in colorsys.hls_to_rgb(h, l, s))


def css(rgb, alfa):
    return f"rgba({rgb[0]},{rgb[1]},{rgb[2]},{alfa})" if alfa is not None else "#%02X%02X%02X" % rgb


def nombre(rol, c):
    rgb, alfa = a_rgb(c)
    return f"--o-{rol}-{'%02x%02x%02x' % rgb}" + (f"-{alfa.replace('.', '')}" if alfa is not None else "")


VARS = {}  # nombre de la variable -> color oscuro


def variable(rol, c):
    rgb, alfa = a_rgb(c)
    v = nombre(rol, c)
    VARS[v] = css(oscuro(rgb, rol), alfa)
    return f"var({v}, {c})"


def declaraciones(texto):
    """Cambia los colores de 'prop: valor; ...' por variables, según el rol de cada propiedad."""
    def una(m):
        rol = ROL.get(m.group(3).lower())
        valor = m.group(5)
        if rol and "var(" not in valor and "{{" not in valor:
            valor = COLOR.sub(lambda c: variable(rol, c.group(0)), valor)
        return m.group(1) + m.group(2) + m.group(3) + m.group(4) + valor
    return re.sub(r"(^|;)(\s*)([a-zA-Z-]+)(\s*:\s*)([^;]*)", una, texto)


def hoja(texto):
    """Una hoja de estilos: regla por regla (las de @media quedan como reglas internas)."""
    def regla(m):
        if m.group(1).strip().startswith(SELECTORES_FIJOS):
            return m.group(0)
        return m.group(1) + "{" + declaraciones(m.group(2)) + "}"
    return re.sub(r"([^{}]+)\{([^{}]*)\}", regla, texto)


ATRIBUTOS = {}  # (atributo, valor, es_texto) -> color oscuro


def zonas_fijas(t):
    """Rangos que se quedan como están: menú flotante, luces de la portada y pie de página."""
    marcas = [('<div style="position: sticky; top: 0; height: 0; z-index: 50">', '<section id="sl-hero"'),
              ('<div class="sl-glow"', '<div class="sl-hero-copy"'),
              ("<footer", "</footer>")]
    r = []
    for ini, fin in marcas:
        if ini in t:
            a = t.index(ini)
            r.append((a, t.index(fin, a)))
    return r


def procesar(t):
    fijas = zonas_fijas(t)
    libre = lambda i: not any(a <= i < b for a, b in fijas)

    # <style> … </style>
    t = re.sub(r"(<style[^>]*>)(.*?)(</style>)", lambda m: m.group(1) + hoja(m.group(2)) + m.group(3), t, flags=re.S)
    fijas = zonas_fijas(t)
    # style="…"
    t = re.sub(r'(\sstyle=")([^"]*)(")', lambda m: m.group(1) + declaraciones(m.group(2)) + m.group(3) if libre(m.start()) else m.group(0), t)
    fijas = zonas_fijas(t)
    # Atributos SVG con color fijo: se anotan para las reglas del modo oscuro
    for m in re.finditer(r"<(\w+)\b[^>]*?\s(fill|stroke|stop-color)=\"(#[0-9a-fA-F]{3,6}|rgba?\([^\"]*\))\"", t):
        if not libre(m.start()):
            continue
        etiqueta, attr, valor = m.group(1).lower(), m.group(2), m.group(3)
        es_texto = etiqueta in ("text", "tspan")
        rol = "texto" if es_texto else {"fill": "fondo", "stroke": "trazo", "stop-color": "fondo"}[attr]
        rgb, alfa = a_rgb(valor)
        nuevo = css(oscuro(rgb, rol), alfa)
        if nuevo.upper() != valor.upper():
            ATRIBUTOS[(attr, valor, es_texto)] = nuevo
    # Colores que pone el JS: '#xxxxxx' -> slC('#xxxxxx')
    mapa_js = {}

    def js(m):
        def lit(x):
            linea = m.group(2)[m.group(2).rfind("\n", 0, x.start()) + 1: m.group(2).find("\n", x.start())]
            c = x.group(1)
            clave = next((v for k, v in JS_FIJOS.items() if k in linea), None)
            if clave:
                return f"slC('{c}', '{clave}')" if f"{clave}{c.upper()}" in JS_ESPECIALES else x.group(0)
            rgb, _ = a_rgb(c)
            nuevo = css(oscuro(rgb, "js"), None)
            if nuevo == c.upper() or len(c) == 4 and nuevo == css(rgb, None):
                return x.group(0)
            mapa_js[c.upper()] = nuevo
            return f"slC('{c}')"
        return m.group(1) + re.sub(r"'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'", lit, m.group(2)) + m.group(3)
    t = re.sub(r'(<script type="text/x-dc"[^>]*>)(.*?)(</script>)', js, t, flags=re.S)
    return t, mapa_js


def bloque_oscuro(extra=""):
    vars_ = "".join(f"{k}:{v};" for k, v in sorted(VARS.items()))
    attrs = []
    for (attr, valor, es_texto), nuevo in sorted(ATRIBUTOS.items()):
        sel = f'[{attr}="{valor}"]'
        attrs.append(f"{'text' + sel + ',tspan' + sel if es_texto else sel + ':not(text):not(tspan)'}{{{attr}:{nuevo}}}")
    return ("<style>/* Modo oscuro (generado por herramientas/ajustes_2026_10_22.py) */\n"
            "@media " + OSCURO + "{\n:root{color-scheme:dark;" + vars_ + "}\n" + "\n".join(attrs) + extra + "\n}\n</style>\n")


def ayudante_js(mapa):
    pares = ",".join(f"'{k}':'{v}'" for k, v in sorted(mapa.items()))
    return ("<script>/* Colores del JS en modo oscuro (generado por herramientas/ajustes_2026_10_22.py) */\n"
            "window.slC=(function(){var m={" + pares + "},q=window.matchMedia?matchMedia('" + OSCURO + "'):{matches:false};"
            "return function(c,k){return q.matches&&m[(k||'')+c.toUpperCase()]||c;};})();</script>\n")


# Lo propio del modo oscuro que no sale de la conversión automática
EXTRA_INDEX = """
body,#sl-hero{background:#000000 !important}
#sl-island{background:#111418 !important;border-color:rgba(255,255,255,0.14) !important;box-shadow:0 12px 32px rgba(0,0,0,0.6) !important}
#sl-hero #sl-video{background-image:url(./assets/portada-poster-oscura-1280.jpg)}
.sl-glow{mix-blend-mode:screen !important;opacity:.42}
.sl-btn-black{background:#FFFFFF !important;color:#0A0F14 !important}
.sl-btn-black:hover{background:#E6EDF3 !important}
.sl-btn-outline:hover{background:rgba(255,255,255,0.08) !important}
footer{background:#0A0D11 !important;border-top:1px solid rgba(255,255,255,0.08)}"""


def ajustar_index(t):
    # Portada: videos livianos, versión oscura, póster como fondo y sin el botón de play
    viejo = ('<video id="sl-video" poster="./assets/portada-poster.jpg" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" preload="auto"',
             '<source src="./assets/portada.webm" type="video/webm">\n<source src="./assets/portada.mp4" type="video/mp4">')
    assert all(v in t for v in viejo)
    t = t.replace(viejo[0], '<video id="sl-video" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" preload="auto" disablepictureinpicture="disablepictureinpicture"')
    t = t.replace(viejo[1],
                  '<source src="./assets/portada-oscura-1280.mp4" type="video/mp4" media="' + OSCURO + '">\n'
                  '<source src="./assets/portada-1280.webm" type="video/webm">\n<source src="./assets/portada-1280.mp4" type="video/mp4">')
    # Si el navegador no deja reproducir sola (iPhone en bajo consumo), arranca con el primer toque
    viejo = "      else { const p = v.play(); if (p && p.catch) p.catch(() => {}); }"
    assert viejo in t
    t = t.replace(viejo, """      else {
        const p = v.play();
        if (p && p.catch) p.catch(() => {
          const otraVez = () => { v.play().catch(() => {}); ['touchend', 'click', 'keydown'].forEach((e) => document.removeEventListener(e, otraVez)); };
          ['touchend', 'click', 'keydown'].forEach((e) => document.addEventListener(e, otraVez, { passive: true }));
        });
      }""")
    # Sin desenfoque en ninguna pantalla: el vidrio pasa a blanco casi opaco (antes solo en el celular)
    viejo = "/* Celular y tabletas: el desenfoque del vidrio es caro al hacer scroll; se cambia por blanco casi opaco */\n@media (max-width:900px),(hover:none){"
    assert viejo in t
    t = t.replace(viejo, "/* En todas las pantallas: el desenfoque del vidrio es caro al hacer scroll (y sobre el video); se cambia por blanco casi opaco */\n@media all{")
    t = re.sub(r"\s*-webkit-backdrop-filter:\s*[^;\"}]*;?", "", t)
    t = re.sub(r"\s*backdrop-filter:\s*[^;\"}]*;?", "", t)
    t = t.replace("{;", "{").replace('style=" ', 'style="')
    # El póster va como fondo del video y el botón de play de iOS no aparece
    viejo = ".sl-hero-media{aspect-ratio:16/9}"
    assert viejo in t
    t = t.replace(viejo, viejo + "\n#sl-video{background:url(./assets/portada-poster-1280.jpg) 0 0/100% 100% no-repeat}"
                  "\n#sl-video::-webkit-media-controls,#sl-video::-webkit-media-controls-panel,"
                  "#sl-video::-webkit-media-controls-start-playback-button,#sl-video::-webkit-media-controls-overlay-play-button"
                  "{display:none !important;-webkit-appearance:none;opacity:0 !important}")
    # Barra del navegador y fondo del sistema en los dos modos
    viejo = '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
    assert viejo in t
    # (sin <meta name="color-scheme">: el color-scheme oscuro lo pone el bloque de OSCURO, así el computador no cambia)
    t = t.replace(viejo, viejo + '\n<meta name="theme-color" content="#000000" media="' + OSCURO + '">'
                  '\n<meta name="theme-color" content="#FDFDFD">')
    return t


# Las animaciones (.dc.html) primero: index.html no carga la cabecera de cada una, así que su bloque lleva todo junto
TODAS_VARS, TODOS_ATRIBUTOS, TODO_JS = {}, {}, {}
for archivo in ARCHIVOS[1:] + ARCHIVOS[:1]:
    ruta = os.path.join(WEB, archivo)
    t = open(ruta, encoding="utf-8").read()
    if archivo == "index.html":
        t = ajustar_index(t)
    VARS.clear()
    ATRIBUTOS.clear()
    t, mapa_js = procesar(t)
    if archivo == "index.html":
        VARS.update(TODAS_VARS)
        ATRIBUTOS.update(TODOS_ATRIBUTOS)
        mapa_js.update(TODO_JS)
        mapa_js.update(JS_ESPECIALES)
    TODAS_VARS.update(VARS)
    TODOS_ATRIBUTOS.update(ATRIBUTOS)
    TODO_JS.update(mapa_js)
    cabeza = bloque_oscuro(EXTRA_INDEX if archivo == "index.html" else "") + ayudante_js(mapa_js)
    # Antes de support.js, para que slC exista cuando corra el JS de la plantilla
    marca = '<script src="./support.js"></script>'
    assert marca in t, archivo
    t = t.replace(marca, cabeza + marca, 1)
    open(ruta, "w", encoding="utf-8", newline="").write(t)
    print(f"{archivo}: {len(VARS)} variables, {len(ATRIBUTOS)} atributos SVG, {len(mapa_js)} colores del JS")

# VIDEOS (en web/assets, con ffmpeg):
#   ESC="scale=1280:960:flags=lanczos"; OSC="negate,hue=h=180,curves=all='0/0 0.06/0 1/1',$ESC"   (fondo en negro puro)
#   ffmpeg -i portada.mp4 -an -vf "$ESC" -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -movflags +faststart portada-1280.mp4
#   ffmpeg -i portada.mp4 -an -vf "$OSC" -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -movflags +faststart portada-oscura-1280.mp4
#   ffmpeg -i portada.mp4 -an -vf "$ESC" -c:v libvpx-vp9 -b:v 0 -crf 40 -row-mt 1 portada-1280.webm
#   (la oscura va solo en mp4: en webm pesaba más del doble)
#   ffmpeg -i portada.mp4 -frames:v 1 -vf "$ESC" -q:v 4 portada-poster-1280.jpg   (y la oscura con "$OSC")
