"""
Saludly · Envío de mensajes por la API oficial de WhatsApp (WhatsApp Cloud API de Meta)

Lee del .env de la raíz: WHATSAPP_TOKEN y WHATSAPP_PHONE_NUMBER_ID. El token nunca se imprime.
- Texto libre: solo dentro de las 24 horas siguientes al último mensaje del paciente (regla de Meta).
- Fuera de esa ventana, solo plantillas aprobadas por Meta.
Todo texto pasa por el control de salida antes de salir.

Uso:
  python codigo/whatsapp/enviar.py --a 573005207995 --bienvenida --nombre Carlos
  python codigo/whatsapp/enviar.py --a 573005207995 --texto "Hola"
"""
import argparse, json, os, sys, urllib.error, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "codigo", "informe"))
import control_salida as CS

API = "https://graph.facebook.com/v25.0/{}/messages"
BIENVENIDA = ("¡Bienvenido a Saludly, {nombre}! 🌱 Ya es saludable e inteligente: tomó la decisión de conocer su cuerpo para cuidarlo. "
              "Abra su app y cuéntenos sus objetivos para empezar.")


def leer_env():
    env = {}
    ruta = os.path.join(RAIZ, ".env")
    if os.path.exists(ruta):
        for l in open(ruta, encoding="utf-8"):
            if "=" in l and not l.lstrip().startswith("#"):
                k, v = l.split("=", 1); env[k.strip()] = v.strip()
    return env


def enviar_texto(a, texto, env=None):
    """Envía un texto libre. Devuelve el id del mensaje de Meta."""
    env = env or leer_env()
    token, numero = env.get("WHATSAPP_TOKEN"), env.get("WHATSAPP_PHONE_NUMBER_ID")
    if not token or not numero: raise SystemExit("Falta WHATSAPP_TOKEN o WHATSAPP_PHONE_NUMBER_ID en el .env")
    problemas = CS.revisar(texto)
    if problemas: raise SystemExit(f"El control de salida bloqueó el mensaje: {problemas}")
    cuerpo = json.dumps(dict(messaging_product="whatsapp", to=a, type="text", text=dict(body=texto))).encode()
    req = urllib.request.Request(API.format(numero), data=cuerpo, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=20))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Meta respondió {e.code}: {e.read().decode()[:400]}")
    return r["messages"][0]["id"]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="número con indicativo, sin +, por ejemplo 573005207995")
    ap.add_argument("--texto")
    ap.add_argument("--bienvenida", action="store_true")
    ap.add_argument("--nombre", default="")
    x = ap.parse_args()
    texto = BIENVENIDA.format(nombre=x.nombre) if x.bienvenida else x.texto
    if not texto: raise SystemExit("Indique --texto o --bienvenida")
    print("enviado:", enviar_texto(x.a, texto))
