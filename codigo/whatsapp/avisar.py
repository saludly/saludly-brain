"""
Saludly · Avisa por WhatsApp a los pacientes con informe aprobado que aún no tienen aviso (Fase 6).

Toma de Supabase los informes con estado "aprobado" y sin "avisado", revisa que el paciente aceptó WhatsApp
en su autorización, envía la plantilla "resultados_listos" (Meta solo deja escribir primero con plantilla aprobada),
después el aviso de consulta del informe, si lo hay, y marca "avisado".
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

PLANTILLA = "resultados_listos"


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
        if not wa.get("resultado_listo"):
            print(f"{x['orden']}: el informe no trae aviso de WhatsApp (puede ser un informe retenido); no se envía nada.")
            continue
        consulta = wa.get("recordatorio_consulta")
        if a.simular:
            print(f"[simulado] a …{p['celular_whatsapp'][-4:]}: plantilla {PLANTILLA}({nombre})" + (f" y luego: {consulta}" if consulta else ""))
        else:
            enviar.enviar_plantilla(p["celular_whatsapp"], PLANTILLA, [nombre or "hola"], env)
            # El texto libre solo llega si el paciente ya escribió en las últimas 24 horas; si no, se le avisa a Carlos.
            if consulta:
                try: enviar.enviar_texto(p["celular_whatsapp"], consulta, env)
                except SystemExit as e: print(f"{x['orden']}: no salió el aviso de consulta ({e}); llama al paciente.")
        if not a.simular:
            sb.pedir("PATCH", f"informes?id=eq.{x['id']}", {"avisado": datetime.now(timezone.utc).isoformat()}, {"Prefer": "return=minimal"})
            print(f"{x['orden']}: aviso enviado a {nombre} (…{p['celular_whatsapp'][-4:]}).")


if __name__ == "__main__":
    main()
