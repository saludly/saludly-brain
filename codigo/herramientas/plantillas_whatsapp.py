"""
Saludly · Plantillas de WhatsApp en Meta (por cuenta de WhatsApp Business, WABA, no por número).

Las plantillas son lo único que se puede enviar cuando la persona lleva más de 24 horas sin escribir. Esta herramienta
las lista, crea las de la semana de prueba (knowledge_base/fase5/semana_prueba.yaml > plantillas) y copia todas las de
una WABA a otra, para cuando el número real quede en una cuenta nueva. Meta revisa cada plantilla nueva (PENDING → APPROVED).
La llave sale de WHATSAPP_TOKEN (variable de entorno o .env de la raíz) y nunca se imprime.

Uso:
  python codigo/herramientas/plantillas_whatsapp.py --listar WABA
  python codigo/herramientas/plantillas_whatsapp.py --semana WABA
  python codigo/herramientas/plantillas_whatsapp.py --copiar WABA_ORIGEN WABA_DESTINO
"""
import argparse, json, os, re, sys, urllib.error, urllib.request

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
API = "https://graph.facebook.com/v25.0/"
# Plantillas de ejemplo que Meta crea en las cuentas de prueba: no se copian
EJEMPLOS = re.compile(r"^(hello_world|jaspers_market_)")


def leer_token():
    t = os.environ.get("WHATSAPP_TOKEN")
    ruta = os.path.join(RAIZ, ".env")
    if not t and os.path.exists(ruta):
        t = next((l.split("=", 1)[1].strip() for l in open(ruta, encoding="utf-8") if l.startswith("WHATSAPP_TOKEN=")), None)
    if not t: raise SystemExit("Falta WHATSAPP_TOKEN en el .env de la raíz.")
    return t


def pedir(ruta, datos=None):
    req = urllib.request.Request(API + ruta, data=json.dumps(datos).encode() if datos else None,
                                 headers={"Authorization": f"Bearer {leer_token()}", "Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        err = json.load(e).get("error", {})
        return {"error": err.get("error_user_msg") or err.get("message")}


def plantillas(waba):
    r = pedir(f"{waba}/message_templates?fields=name,status,category,language,components,rejected_reason&limit=200")
    if "error" in r: raise SystemExit(f"Meta respondió: {r['error']}")
    return r["data"]


def crear(waba, datos, existentes):
    if (datos["name"], datos["language"]) in existentes: return "ya existe"
    r = pedir(f"{waba}/message_templates", datos)
    return r.get("status") or f"ERROR {r.get('error')}"


def de_la_semana():
    S = yaml.safe_load(open(os.path.join(RAIZ, "knowledge_base", "fase5", "semana_prueba.yaml"), encoding="utf-8"))
    for p in S["plantillas"]:
        cuerpo = {"type": "BODY", "text": p["cuerpo"]}
        if re.search(r"\{\{\d+\}\}", p["cuerpo"]): cuerpo["example"] = {"body_text": [p["ejemplo"]]}
        yield {"name": p["nombre"], "language": "es", "category": p["categoria"],
               "components": [cuerpo, {"type": "BUTTONS", "buttons": [{"type": "QUICK_REPLY", "text": b} for b in p["botones"]]}]}


def main():
    ap = argparse.ArgumentParser(description="Plantillas de WhatsApp en Meta")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--listar", metavar="WABA")
    g.add_argument("--semana", metavar="WABA")
    g.add_argument("--copiar", nargs=2, metavar=("ORIGEN", "DESTINO"))
    a = ap.parse_args()
    if a.listar:
        for t in plantillas(a.listar):
            print(f"{t['name']:28} {t['status']:9} {t['category']:10} {t['language']:6} {t.get('rejected_reason') or ''}")
        return
    destino = a.semana or a.copiar[1]
    existentes = {(t["name"], t["language"]) for t in plantillas(destino)}
    if a.semana:
        lista = list(de_la_semana())
    else:
        # Se copian las aprobadas o en revisión; los ids de los ejemplos no se pueden reusar y Meta los vuelve a pedir
        lista = [dict(name=t["name"], language=t["language"], category=t["category"], components=t["components"])
                 for t in plantillas(a.copiar[0]) if t["status"] in ("APPROVED", "PENDING") and not EJEMPLOS.match(t["name"])]
    for d in lista:
        print(f"{d['name']:28} → {crear(destino, d, existentes)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
