"""
Ajustes de la landing del 21 de octubre de 2026, pedidos por Carlos:
- "Empezar" lleva a crear la cuenta en la app (app.saludly.online/entrar).
- "100+ biomarcadores" (el panel estándar medido más los calculados) en vez de 120+.
- Fuera los textos de relleno entre corchetes y lo que todavía no existe: relojes, familia, hábitos,
  logos y médicos de ejemplo, puntaje Saludly y "Agendar medicina general".
- Sin promesas que no se pueden sostener: nada de "prevenir 100+ enfermedades" (Saludly no diagnostica).
- Tarjetas de beneficios más simples, en estilo vidrio (glassmorphism), con un solo color de acento.
- Membresía: lanzamiento en Bogotá con 10 cupos; el valor se ve en la app al registrarse.
Uso: python web/herramientas/ajustes_2026_10_21.py   (desde la raíz; se puede correr una sola vez)
"""
import os, re

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = "https://app.saludly.online/entrar"


def editar(nombre, cambios):
    ruta = os.path.join(WEB, nombre)
    t = open(ruta, encoding="utf-8").read()
    for viejo, nuevo, veces in cambios:
        n = t.count(viejo) if isinstance(viejo, str) else len(viejo.findall(t))
        assert n == veces, f"{nombre}: se esperaban {veces} y hay {n} de {viejo if isinstance(viejo, str) else viejo.pattern}"
        t = t.replace(viejo, nuevo) if isinstance(viejo, str) else viejo.sub(nuevo, t)
    open(ruta, "w", encoding="utf-8").write(t)


# ---------- index.html ----------
cambios = [
    # Botones "Empezar" del menú → crear la cuenta en la app
    ('<a href="#agendar" class="sl-btn-white"', f'<a href="{APP}" class="sl-btn-white"', 2),
    ('<a href="#agendar" onClick="{{close}}" class="sl-btn-white"', f'<a href="{APP}" onClick="{{{{close}}}}" class="sl-btn-white"', 1),
    # Portada: promesa sin diagnóstico y botón Empezar junto a "Ver demo"
    ("Una muestra de sangre y una superinteligencia médica pueden prevenir 100+ condiciones o enfermedades, mejorar tu salud y aumentar tu longevidad.",
     "Una muestra de sangre en tu casa y una IA médica que lee más de 100 biomarcadores en conjunto, para encontrar a tiempo lo que puedes prevenir con tu médico.", 1),
    ('<a href="#sl-medimos" class="sl-btn-outline"',
     f'<a href="{APP}" class="sl-btn-black" style="display: inline-flex; align-items: center; justify-content: center; min-width: 180px; height: 52px; padding: 0 28px; box-sizing: border-box; border-radius: 26px; background: #0A2236; color: #FFFFFF; font-size: 16px; font-weight: 600; text-decoration: none; margin-right: 12px">Empezar</a><a href="#sl-medimos" class="sl-btn-outline"', 1),
    # Cifra de biomarcadores
    ("120+ biomarcadores", "100+ biomarcadores", 4),
    # Textos de relleno
    ("El laboratorio aliado [NOMBRE] procesa tu panel.", "Un laboratorio clínico aliado en Bogotá procesa tu panel.", 1),
    ("En la app, en [X DÍAS HÁBILES], con prioridades claras", "En la app, en pocos días hábiles, con prioridades claras", 1),
    ("12 especialidades médicas detrás de tu informe", "Guías de 12 especialidades detrás de tu informe", 1),
    # Lo que todavía no existe: relojes y conexiones, logos y médicos de ejemplo
    ('<section id="sl-wear" class="sl-sec"', '<section id="sl-wear" hidden class="sl-sec"', 1),
    ('<section id="sl-respaldo" class="sl-sec"', '<section id="sl-respaldo" hidden class="sl-sec"', 1),
    # Puntaje Saludly (no existe) → resultados en rango (sí existe)
    (">Puntaje Saludly<", ">Resultados en rango<", 1),
    ("Resumen de tus sistemas cardiovascular, metabólico, renal, hepático y hormonal.",
     "Cuántos de tus biomarcadores están dentro del rango de referencia de tu laboratorio.", 1),
    ("Metodología: guías clínicas certificadas.", "Metodología: PhenoAge, con los resultados de tu laboratorio.", 1),
    # Membresía: lanzamiento con 10 cupos
    ('>[PRECIO]</span><span style="font-size: 15px; color: #52667A">/año</span>',
     '>10 cupos</span><span style="font-size: 15px; color: #52667A">de lanzamiento en Bogotá</span>', 1),
    ("100+ biomarcadores en [N.º DE TOMAS] tomas al año", "100+ biomarcadores en tu panel de sangre", 1),
    ("Edad biológica y puntaje Saludly", "Edad biológica y plan en 3 pasos", 1),
    ("Resultados en [X DÍAS HÁBILES]", "Resultados en pocos días hábiles, revisados por un médico", 1),
    ('<a href="#agendar" class="sl-btn-black"', f'<a href="{APP}" class="sl-btn-black"', 1),
    (">Agendar mi primera toma</a>", ">Empezar</a>", 1),
    ("Disponible en Bogotá. [CONDICIONES DE LA MEMBRESÍA]",
     'Solo en Bogotá. El valor lo ves en la app al crear tu cuenta. <a href="https://app.saludly.online/privacidad" style="color: inherit">Política de datos</a>', 1),
    # Pie de página: política de datos
    ("No diagnostica ni reemplaza la consulta con un profesional de salud. © 2026 Saludly.</p>",
     'No diagnostica ni reemplaza la consulta con un profesional de salud. © 2026 Saludly. <a href="https://app.saludly.online/privacidad" style="color: #FFFFFF">Política de tratamiento de datos</a></p>', 1),
]
editar("index.html", cambios)

# ---------- Beneficios: sin hábitos ni familia, y en estilo vidrio ----------
ruta = os.path.join(WEB, "index.html")
t = open(ruta, encoding="utf-8").read()
ini, fin = t.index('<section id="sl-beneficios"'), t.index("</section>", t.index('<section id="sl-beneficios"')) + len("</section>")
b = t[ini:fin]
articulos = re.findall(r"<article .*?</article>", b, flags=re.S)
assert len(articulos) == 8
for a in articulos:
    if "Hábitos saludables" in a or "Cuida a tu familia" in a:
        b = b.replace(a + "\n", "").replace(a, "")
# Fondo de la sección con dos luces suaves para que se note el vidrio
b = b.replace('style="background: #FDFDFD; padding: 112px 24px; border-top: 1px solid #EDF1F5"',
              'style="background: radial-gradient(38% 45% at 12% 18%, rgba(43,158,240,0.12), rgba(43,158,240,0) 70%), radial-gradient(40% 50% at 88% 85%, rgba(43,158,240,0.10), rgba(43,158,240,0) 70%), #F7FAFD; padding: 112px 24px; border-top: 1px solid #EDF1F5"', 1)
# Tarjeta de vidrio: blanco translúcido, desenfoque y borde claro
b = b.replace("background: #FFFFFF; border: 1px solid #E3EBF2; box-shadow: 0 18px 40px rgba(10,34,54,0.06);",
              "background: rgba(255,255,255,0.55); -webkit-backdrop-filter: blur(18px) saturate(140%); backdrop-filter: blur(18px) saturate(140%); border: 1px solid rgba(255,255,255,0.85); box-shadow: 0 18px 40px rgba(10,34,54,0.06);")
# Sin degradados de colores detrás de cada vista previa
b = re.sub(r"background: radial-gradient\(60% 70% at 0% 0%[^;]*?\), #F4F8FC", "background: rgba(255,255,255,0.25)", b)
b = b.replace("display: flex; gap: 14px; align-items: flex-start; background: #FFFFFF", "display: flex; gap: 14px; align-items: flex-start; background: transparent")
# Íconos con un solo color de acento
b = b.replace("background: #FFEDE4;", "background: rgba(22,112,184,0.08);").replace("background: #E6F2FD;", "background: rgba(22,112,184,0.08);")
b = b.replace('stroke="#C24A17"', 'stroke="#1670B8"')
t = t[:ini] + b + t[fin:]
open(ruta, "w", encoding="utf-8").write(t)

# ---------- Animaciones de los pasos ----------
editar("Paso2Agente.dc.html", [
    ("Revisé tus más de 120 biomarcadores", "Revisé tus más de 100 biomarcadores", 1),
    ("'conectando 120+ biomarcadores'", "'conectando 100+ biomarcadores'", 1),
    ("count: Math.round(120 * clamp(", "count: Math.round(100 * clamp(", 1),
])
editar("Paso3App.dc.html", [
    ("Más de 120 biomarcadores leídos en conjunto", "Más de 100 biomarcadores leídos en conjunto", 1),
    (">Agendar medicina general</span>", ">Compartir con mi médico</span>", 1),
])
editar("QueMedimos.dc.html", [("120+ biomarcadores, ordenados por sistema", "100+ biomarcadores, ordenados por sistema", 1)])
print("listo")
