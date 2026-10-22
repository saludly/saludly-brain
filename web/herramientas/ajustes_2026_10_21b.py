"""
Segunda ronda de ajustes de la landing (21 de octubre de 2026), pedidos por Carlos:
- Pantalla de carga: fondo blanco con la "y" de Saludly dibujándose de punta a punta (el trazo del video de marca),
  una vez por visita; después se abre la página.
- Menú flotante: en vez de las partículas, la "y"; cada minuto aparece el logo completo unos segundos y vuelve a la "y".
  Arriba, el menú abierto muestra el logo completo en blanco.
- Sin la animación de conteo de la edad biológica (volvía a pintar toda la página en cada cuadro y la ponía lenta).
- Sección nueva "Te acompañamos por WhatsApp": recomendaciones, recetas y cuándo ver al médico, personalizado.
- Membresía: en vez de la foto, una tarjeta con el camino del paciente (de la cuenta al WhatsApp).
Uso: python web/herramientas/ajustes_2026_10_21b.py   (una sola vez; trazo de la "y" en app/src/lib/trazo_y.ts)
"""
import os, re

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(WEB)
TRAZO = re.search(r'"(M[^"]+)"', open(os.path.join(RAIZ, "app", "src", "lib", "trazo_y.ts"), encoding="utf-8").read()).group(1)
APP = "https://app.saludly.online/entrar"

ruta = os.path.join(WEB, "index.html")
t = open(ruta, encoding="utf-8").read()


def cambiar(viejo, nuevo, veces=1):
    global t
    assert t.count(viejo) == veces, f"se esperaban {veces} y hay {t.count(viejo)} de: {viejo[:80]}"
    t = t.replace(viejo, nuevo)


# ---------- Estilos (en el <head>, fuera de la plantilla) ----------
ESTILOS = """<style>
/* Pantalla de carga: la "y" se dibuja de punta a punta y luego se abre la página */
#sl-carga{position:fixed;inset:0;z-index:9999;background:#FFFFFF;display:flex;align-items:center;justify-content:center;animation:sl-carga-fuera .5s ease 1.9s forwards}
#sl-carga svg{height:140px;width:auto}
#sl-carga path{stroke-dasharray:1 3;stroke-dashoffset:1.03;animation:sl-carga-trazo 1.5s cubic-bezier(.65,0,.35,1) .15s forwards}
@keyframes sl-carga-trazo{to{stroke-dashoffset:0}}
@keyframes sl-carga-fuera{to{opacity:0;visibility:hidden}}
/* Logo del menú flotante: la "y"; cada minuto, el logo completo unos segundos */
.sl-logo{position:relative;flex-shrink:0;display:block;height:34px;width:22px;animation:sl-logo-ancho 60s cubic-bezier(.32,.72,0,1) -52s infinite}
.sl-logo img{position:absolute;left:0;top:50%;transform:translateY(-50%);width:auto;max-width:none}
.sl-logo .sl-logo-y{height:28px;animation:sl-logo-y 60s ease -52s infinite}
.sl-logo .sl-logo-palabra{height:34px;opacity:0;animation:sl-logo-palabra 60s ease -52s infinite}
@keyframes sl-logo-ancho{0%,90%{width:22px}92%,98%{width:68px}100%{width:22px}}
@keyframes sl-logo-y{0%,90%{opacity:1}91%,98.5%{opacity:0}100%{opacity:1}}
@keyframes sl-logo-palabra{0%,90.5%{opacity:0}92%,98%{opacity:1}99%,100%{opacity:0}}
/* WhatsApp */
.sl-wa-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:center}
.sl-wa-item{display:flex;gap:14px;align-items:flex-start;padding:18px;border-radius:22px;background:rgba(255,255,255,.6);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.85);box-shadow:0 12px 30px rgba(10,34,54,.05)}
.sl-wa-burbuja{max-width:86%;padding:10px 12px 8px;border-radius:14px;font-size:13.5px;line-height:1.45;color:#111B21;background:#FFFFFF;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.sl-wa-burbuja small{display:block;text-align:right;font-size:10.5px;color:#667781;margin-top:2px}
@media (max-width:900px){.sl-wa-grid{grid-template-columns:minmax(0,1fr);gap:40px}}
@media (prefers-reduced-motion:reduce){#sl-carga{display:none}.sl-logo,.sl-logo img{animation:none}}
</style>
"""
cambiar("</head>", ESTILOS + "</head>")
cambiar("con más de 120 biomarcadores y un informe claro.", "con más de 100 biomarcadores, un informe claro y acompañamiento por WhatsApp.")

# ---------- Pantalla de carga (antes de la plantilla; solo la primera vez en la visita) ----------
CARGA = f"""<div id="sl-carga" aria-hidden="true"><svg viewBox="0 0 981.45 1248.02"><path d="{TRAZO}" pathLength="1" fill="none" stroke="#2793ff" stroke-width="99" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
<script>
// Fuera del <body>: la plantilla vuelve a pintar el body y la borraría.
document.documentElement.appendChild(document.getElementById('sl-carga'));
try {{ if (sessionStorage.getItem('sl-carga')) document.getElementById('sl-carga').remove(); else sessionStorage.setItem('sl-carga', '1'); }} catch (e) {{}}
setTimeout(function () {{ var c = document.getElementById('sl-carga'); if (c) c.remove(); }}, 2600);
</script>
"""
cambiar("<body>\n<x-dc>", "<body>\n" + CARGA + "<x-dc>")

# ---------- Menú flotante ----------
cambiar('<a href="#sl-hero" class="sl-display" style="font-size: 20px; font-weight: 600; letter-spacing: -0.01em; color: #FFFFFF; text-decoration: none">Saludly</a>',
        '<a href="#sl-hero" aria-label="Saludly, inicio" style="display: flex; align-items: center"><img src="./assets/marca/saludly-blanco.svg" alt="Saludly" style="height: 34px; width: auto"></a>')
cambiar('<span class="sl-parts" aria-hidden="true" style="flex-shrink: 0"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>',
        '<span class="sl-logo" aria-hidden="true"><img class="sl-logo-y" src="./assets/marca/y-blanco.svg" alt=""><img class="sl-logo-palabra" src="./assets/marca/saludly-blanco.svg" alt=""></span>', 2)

# ---------- Sin conteo animado en la edad biológica ----------
cambiar("  _wireCount() {\n", "  _wireCount() {\n    return; // sin conteo animado: volvía a pintar toda la página en cada cuadro y la ponía lenta (21 oct 2026)\n")

# ---------- Sección de WhatsApp (antes de la membresía) ----------
def item(icono, titulo, texto):
    return f"""<div class="sl-wa-item"><span aria-hidden="true" style="flex-shrink: 0; width: 40px; height: 40px; border-radius: 12px; background: rgba(37,211,102,0.12); display: flex; align-items: center; justify-content: center; font-size: 20px">{icono}</span><div><h3 class="sl-display" style="margin: 0; font-size: 18px; font-weight: 600; color: #0A2236">{titulo}</h3><p style="margin: 4px 0 0; font-size: 14.5px; line-height: 1.5; color: #52667A">{texto}</p></div></div>"""

def burbuja(texto, hora):
    return f'<div class="sl-wa-burbuja">{texto}<small>{hora}</small></div>'

WHATSAPP = f"""<section id="sl-whatsapp" class="sl-sec" aria-labelledby="sl-wa-t" style="background: radial-gradient(40% 50% at 85% 20%, rgba(37,211,102,0.10), rgba(37,211,102,0) 70%), radial-gradient(40% 50% at 10% 85%, rgba(43,158,240,0.10), rgba(43,158,240,0) 70%), #F7FAFD; padding: 112px 24px; border-top: 1px solid #EDF1F5">
<div class="sl-wa-grid" style="max-width: 1100px; margin: 0 auto">
<div style="display: flex; flex-direction: column; gap: 22px">
<p style="margin: 0; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #128C7E">Por WhatsApp</p>
<h2 id="sl-wa-t" class="sl-display" style="margin: 0; font-size: clamp(34px, 3.8vw, 54px); line-height: 1.04; font-weight: 600; letter-spacing: -0.03em; max-width: 16ch">Te acompañamos todos los días.</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #3E5266; max-width: 46ch">Tu informe no se queda en la app. Por WhatsApp te escribimos lo que necesitas, pensado con tus resultados, tus metas, tus alergias y tu dieta.</p>
<div style="display: flex; flex-direction: column; gap: 12px">
{item("💡", "Recomendaciones para ti", "Cambios concretos de alimentación, actividad y sueño, elegidos según lo que salió en tu informe.")}
{item("🥗", "Una receta cada día", "Recetas colombianas fáciles, con sus nutrientes calculados y sin lo que no puedes o no quieres comer.")}
{item("🩺", "Cuándo ver a tu médico", "Si algo merece consulta, te lo decimos con un plazo claro y un enlace con tu resumen para tu médico.")}
</div>
<p style="margin: 0; font-size: 13px; color: #52667A">Solo si lo autorizas. Escribe BAJA cuando quieras y dejamos de escribirte.</p>
</div>
<div style="justify-self: center; width: 100%; max-width: 340px">
<div style="border-radius: 40px; padding: 10px; background: #0A0F14; box-shadow: 0 30px 60px rgba(10,34,54,0.22)">
<div style="border-radius: 31px; overflow: hidden; background: #EFE7DE">
<div style="display: flex; align-items: center; gap: 10px; padding: 14px 16px; background: #075E54; color: #FFFFFF">
<span style="width: 34px; height: 34px; border-radius: 50%; background: #FFFFFF; display: flex; align-items: center; justify-content: center"><img src="./assets/marca/y-azul.svg" alt="" style="height: 22px; width: auto"></span>
<div><div style="font-size: 15px; font-weight: 600">Saludly</div><div style="font-size: 11.5px; opacity: 0.8">Cuenta de empresa</div></div>
</div>
<div style="display: flex; flex-direction: column; gap: 10px; padding: 16px 12px 20px">
{burbuja("¡Hola, Ana! 👋 Tus resultados ya están listos y un médico los revisó. Entra a tu app para ver tu informe y tu plan.", "7:02 a. m.")}
{burbuja("🥗 <b>Receta de hoy:</b> ensalada tibia de lentejas con espinaca y limón. Rica en hierro y fibra, sin maní, como pediste.", "12:15 p. m.")}
{burbuja("💡 <b>Tu reto de la semana:</b> camina 30 minutos después del almuerzo, 5 días.", "6:30 p. m.")}
{burbuja("🩺 Según tu informe, te recomendamos una consulta de medicina general en las próximas 2 a 4 semanas. Lleva el enlace con tu resumen para tu médico.", "6:31 p. m.")}
</div>
</div>
</div>
</div>
</div>
</section>

"""
cambiar('<section id="agendar" class="sl-sec"', WHATSAPP + '<section id="agendar" class="sl-sec"')

# ---------- Membresía: el camino del paciente en vez de la foto ----------
m = re.search(r'<div class="sl-memb-photo"[^>]*>.*?</div>', t, flags=re.S)
assert m and "membresia.jpg" in m.group(0)
pasos = [
    ("1", "Creas tu cuenta y pagas", "Con Google, en un minuto. Pagas por transferencia Bre-B."),
    ("2", "Respondes tus preguntas", "Tus metas, tu actividad, tus alergias y tus medicamentos."),
    ("3", "La enfermera va a tu casa", "Eliges día y hora en la app. Toma de muestra en ayunas."),
    ("4", "Recibes tu informe", "Revisado por un médico, con tu plan en 3 pasos."),
    ("5", "Te acompañamos por WhatsApp", "Recomendaciones, recetas y cuándo ver a tu médico."),
]
lista = "\n".join(
    f'<li style="display: flex; gap: 14px; align-items: flex-start"><span class="sl-display" style="flex-shrink: 0; width: 32px; height: 32px; border-radius: 50%; background: #1670B8; color: #FFFFFF; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center">{n}</span><div><div style="font-size: 16px; font-weight: 600; color: #0A2236">{a}</div><div style="font-size: 14px; line-height: 1.45; color: #52667A">{b}</div></div></li>'
    for n, a, b in pasos)
CAMINO = f"""<div class="sl-memb-photo" style="position: relative; border-radius: 36px; overflow: hidden; padding: clamp(28px, 4vw, 44px); background: radial-gradient(50% 50% at 15% 10%, rgba(43,158,240,0.16), rgba(43,158,240,0) 70%), radial-gradient(45% 45% at 90% 90%, rgba(37,211,102,0.12), rgba(37,211,102,0) 70%), #F4F8FC">
<div style="border-radius: 28px; padding: clamp(22px, 3vw, 32px); background: rgba(255,255,255,0.62); -webkit-backdrop-filter: blur(18px); backdrop-filter: blur(18px); border: 1px solid rgba(255,255,255,0.9); box-shadow: 0 18px 40px rgba(10,34,54,0.06)">
<img src="./assets/marca/saludly-azul.svg" alt="Saludly" style="height: 40px; width: auto">
<p style="margin: 14px 0 22px; font-size: 13px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #3E5266">Tu camino en Saludly</p>
<ol style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 18px">
{lista}
</ol>
</div>
</div>"""
t = t[:m.start()] + CAMINO + t[m.end():]

open(ruta, "w", encoding="utf-8").write(t)
print("listo")
