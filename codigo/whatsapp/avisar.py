"""
Saludly · Avisa por WhatsApp a los pacientes con informe aprobado que aún no tienen aviso (Fase 6).

Toma de Supabase los informes con estado "aprobado" y sin "avisado", revisa que el paciente aceptó WhatsApp
en su autorización, envía el mensaje "resultado_listo" del informe (y el aviso de consulta, si lo hay) y marca "avisado".
Nunca envía resultados ni valores: solo el aviso para que abra la app.

Uso: python codigo/whatsapp/avisar.py            (envía)
     python codigo/whatsapp/avisar.py --simular  (muestra qué enviaría, sin enviar)
"""
import argparse, os, sys
from datetime import datetime, timezone

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "codigo", "pipeline"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from publicar import Supabase
import enviar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    env = enviar.leer_env()
    sb = Supabase(env)
    pendientes = sb.pedir("GET", "informes?estado=eq.aprobado&avisado=is.null&select=id,paciente_id,orden,informe->whatsapp")
    if not pendientes: return print("No hay informes aprobados pendientes de aviso.")
    for x in pendientes:
        p = sb.uno("pacientes", f"id=eq.{x['paciente_id']}&select=nombre,celular_whatsapp")
        ok = sb.uno("autorizaciones", f"paciente_id=eq.{x['paciente_id']}&acepta_whatsapp=is.true&select=id")
        nombre = (p or {}).get("nombre", "").split(" ")[0]
        if not p or not ok:
            print(f"{x['orden']}: {nombre or 'paciente'} no aceptó WhatsApp; avísale por otro medio.")
            continue
        wa = x.get("whatsapp") or {}
        textos = [t for t in (wa.get("resultado_listo"), wa.get("recordatorio_consulta")) if t]
        if not textos:
            print(f"{x['orden']}: el informe no trae aviso de WhatsApp (puede ser un informe retenido); no se envía nada.")
            continue
        textos[0] = textos[0].replace("Hola 👋", f"Hola, {nombre} 👋", 1) if nombre else textos[0]
        for t in textos:
            if a.simular: print(f"[simulado] a …{p['celular_whatsapp'][-4:]}: {t}")
            else: enviar.enviar_texto(p["celular_whatsapp"], t, env)
        if not a.simular:
            sb.pedir("PATCH", f"informes?id=eq.{x['id']}", {"avisado": datetime.now(timezone.utc).isoformat()}, {"Prefer": "return=minimal"})
            print(f"{x['orden']}: aviso enviado a {nombre} (…{p['celular_whatsapp'][-4:]}).")


if __name__ == "__main__":
    main()
