"""
Saludly · Publica el informe de un paciente del piloto (Fase 6).

PDF del laboratorio + datos del paciente en Supabase (cuenta, cuestionario y visita de la enfermera)
→ saludly.generar() → informe en la tabla `informes` con estado "en_revision" (o "retenido" si hay que llamar).
El médico lo aprueba en la vista /medico de la app; solo entonces el paciente lo ve.

Uso (en el PC de Saludly; lee SUPABASE_URL y SUPABASE_SERVICE_ROLE_KEY del .env, nunca las imprime):
  python codigo/pipeline/publicar.py --pdf resultado.pdf --cedula 1234567 --orden LCD-2026-100123
  Prueba con un PDF sintético (su documento no es el del paciente):
  python codigo/pipeline/publicar.py --pdf pdf_ejemplo/....pdf --cedula 1234567 --orden LCD-2026-100123 --documento-pdf "CC 0000000001"

Reglas:
- El PDF no se guarda: se lee y se descarta. El informe lleva el seudónimo del paciente, nunca nombre ni cédula.
- Si la edad o el sexo de la cuenta no coinciden con el PDF, manda el PDF y se avisa en la vista del médico.
"""
import argparse, json, os, sys, urllib.error, urllib.parse, urllib.request
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import saludly


def leer_env():
    env = {}
    for l in open(os.path.join(RAIZ, ".env"), encoding="utf-8"):
        if "=" in l and not l.lstrip().startswith("#"):
            k, v = l.split("=", 1); env[k.strip()] = v.strip()
    return env


class Supabase:
    """Cliente mínimo de la API REST de Supabase con la llave de servicio (salta las reglas RLS: solo para este PC)."""

    def __init__(self, env):
        self.url = env["SUPABASE_URL"].rstrip("/") + "/rest/v1/"
        self.cab = {"apikey": env["SUPABASE_SERVICE_ROLE_KEY"], "Authorization": f"Bearer {env['SUPABASE_SERVICE_ROLE_KEY']}", "Content-Type": "application/json"}

    def pedir(self, metodo, ruta, cuerpo=None, extra=None):
        req = urllib.request.Request(self.url + ruta, method=metodo, data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
                                     headers={**self.cab, **(extra or {})})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                t = r.read().decode()
                return json.loads(t) if t else None
        except urllib.error.HTTPError as e:
            raise SystemExit(f"Supabase respondió {e.code} en {ruta.split('?')[0]}: {e.read().decode()[:300]}")

    def uno(self, tabla, filtro):
        filas = self.pedir("GET", f"{tabla}?{filtro}&limit=1")
        return filas[0] if filas else None


def perfil_y_enfermera(c, v):
    """Arma perfil.json y enfermera.json del pipeline a partir del cuestionario y la visita."""
    perfil = {k: c.get(k) for k in ("objetivos", "toma_biotina", "nivel_actividad", "alergias", "alergias_otras", "medicamentos")}
    if c.get("dieta"): perfil["dieta"] = c["dieta"]
    perfil = {k: x for k, x in perfil.items() if x not in (None, [], "")}
    enf = {k: v.get(k) for k in ("presion_sistolica", "presion_diastolica", "cintura_cm", "peso_kg", "talla_m")} if v else {}
    for k in ("peso_kg", "talla_m"):                       # sin medida de la enfermera, se usa lo que dijo el paciente
        if enf.get(k) is None and c.get(k) is not None: enf[k] = c[k]
    enf = {k: float(x) if k in ("cintura_cm", "peso_kg", "talla_m") else x for k, x in enf.items() if x is not None}
    if c.get("fuma"): enf["tabaquismo"] = c["fuma"] == "si"
    if c.get("embarazo") in ("si", "no"): enf["embarazo"] = c["embarazo"] == "si"
    return perfil, enf


def publicar(sb, pdf, orden, paciente_id=None, cedula=None, documento_pdf=None, forzar=False):
    """PDF + datos del paciente → informe en la tabla informes. Devuelve un resumen; si algo falta, lanza SystemExit con el motivo.
    La usan este script y la función de Vercel (app/api/procesar.py) que llama la vista del médico."""
    filtro = f"cedula=eq.{urllib.parse.quote(cedula)}" if cedula else f"id=eq.{urllib.parse.quote(paciente_id)}"
    p = sb.uno("pacientes", f"{filtro}&select=id,tipo_documento,cedula,fecha_nacimiento,edad,sexo")
    if not p: raise SystemExit("No hay ningún paciente con esa cédula o id.")
    if sb.uno("informes", f"paciente_id=eq.{p['id']}&orden=eq.{urllib.parse.quote(orden)}&estado=eq.aprobado&select=id"):
        raise SystemExit(f"El informe de la orden {orden} ya está aprobado: no se reemplaza.")
    if not sb.uno("autorizaciones", f"paciente_id=eq.{p['id']}&acepta_datos=is.true&select=id"):
        raise SystemExit("El paciente no ha firmado la autorización de datos: no se puede procesar.")
    c = sb.uno("cuestionarios", f"paciente_id=eq.{p['id']}") or {}
    v = sb.uno("visitas", f"paciente_id=eq.{p['id']}")
    faltan = [n for n, ok in (("cuestionario completo", c.get("completo")), ("visita de la enfermera", v)) if not ok]
    if faltan and not forzar: raise SystemExit(f"Falta: {', '.join(faltan)}. Marca «publicar igual» para seguir.")

    perfil, enf = perfil_y_enfermera(c, v)
    if not perfil.get("objetivos"): raise SystemExit("El paciente no ha elegido sus metas.")
    documento = documento_pdf or f"{p['tipo_documento']} {p['cedula']}"
    if p.get("fecha_nacimiento"):  # la edad de la cuenta, a hoy
        n, hoy = date.fromisoformat(p["fecha_nacimiento"]), date.today()
        p["edad"] = hoy.year - n.year - ((hoy.month, hoy.day) < (n.month, n.day))
    codigo, inf = saludly.generar(pdf, documento, orden, perfil, enf)
    if codigo != 0: raise SystemExit(f"No se generó el informe ({inf.get('estado')}): {inf.get('motivo')}")

    avisos = []
    if inf["perfil"].get("sexo") and inf["perfil"]["sexo"] != p["sexo"]:
        avisos.append(f"Sexo: la cuenta dice {p['sexo']} y el PDF {inf['perfil']['sexo']}; se usó el del PDF.")
    if inf["perfil"].get("edad") and abs(inf["perfil"]["edad"] - p["edad"]) > 1:
        avisos.append(f"Edad: la cuenta dice {p['edad']} y el PDF {inf['perfil']['edad']}; se usó la del PDF.")
    if documento_pdf: avisos.append("Prueba con PDF sintético: el documento del PDF no es el del paciente.")
    if faltan: avisos.append(f"Publicado sin: {', '.join(faltan)}.")
    if c.get("medicamentos_otros"): avisos.append(f"Otros medicamentos que escribió el paciente: {c['medicamentos_otros']}.")
    inf["medico"]["avisos_publicacion"] = avisos

    estado = "retenido" if inf["estado"] == "retenido_hasta_llamada" else "en_revision"
    sb.pedir("POST", "informes?on_conflict=paciente_id,orden", dict(paciente_id=p["id"], orden=orden, informe=inf, estado=estado),
             {"Prefer": "resolution=merge-duplicates,return=minimal"})
    return dict(informe_id=inf["informe_id"], estado=estado, paciente_ref=inf["paciente_ref"], avisos=avisos)


def main():
    ap = argparse.ArgumentParser(description="PDF + datos del paciente en Supabase → informe en revisión")
    ap.add_argument("--pdf", required=True)
    quien = ap.add_mutually_exclusive_group(required=True)
    quien.add_argument("--cedula", help="cédula del paciente, como la escribió en su cuenta")
    quien.add_argument("--paciente-id", help="id del paciente en Supabase (la vista del médico lo muestra)")
    ap.add_argument("--orden", required=True, help="número de orden del laboratorio")
    ap.add_argument("--documento-pdf", help="solo para pruebas con PDF sintético: el documento que trae el PDF")
    ap.add_argument("--forzar", action="store_true", help="publicar aunque falte el cuestionario completo o la visita")
    a = ap.parse_args()
    r = publicar(Supabase(leer_env()), a.pdf, a.orden, a.paciente_id, a.cedula, a.documento_pdf, a.forzar)
    print(f"Informe {r['informe_id']} publicado como «{r['estado']}» para {r['paciente_ref']}.")
    for x in r["avisos"]: print("  aviso:", x)
    print("Revíselo y apruébelo en la vista /medico de la app.")


if __name__ == "__main__":
    main()
