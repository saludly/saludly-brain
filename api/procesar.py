"""
Saludly · Función de Vercel: el médico sube el PDF del laboratorio en /medico y aquí se analiza (Fase 6).
En la línea GLP-1 (Fase 6B) también lo sube la paciente desde /peso (el suyo) o su doctora desde /doctora (el de una paciente suya).

POST /api/procesar con la sesión del médico (Authorization: Bearer <token de Supabase>) y un JSON:
  {"pdf_base64": "...", "paciente_id": null, "documento_pdf": null, "forzar": false}
La orden y el documento se leen del PDF; sin paciente_id se busca al paciente por el documento.
Revisa que quien llama esté en la tabla `equipo`, guarda el PDF solo en /tmp mientras se lee, corre
codigo/pipeline/publicar.publicar() (lector → motor → informe) y lo borra. El informe queda "en_revision".
El código del análisis viaja en saludly_lib/ (lo copia app/desplegar.sh); las llaves vienen de las variables
de entorno de Vercel (SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY).
"""
import base64, json, os, sys, tempfile, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler

LIB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "saludly_lib")
sys.path.insert(0, os.path.join(LIB, "codigo", "pipeline"))
import publicar as P

MAX_PDF = 3 * 1024 * 1024  # Vercel acepta hasta 4,5 MB por petición; en base64 el PDF crece un tercio


def quien_llama(token, env):
    """Correo e id del usuario de la sesión, si el token es válido."""
    req = urllib.request.Request(env["SUPABASE_URL"].rstrip("/") + "/auth/v1/user",
                                 headers={"apikey": env["SUPABASE_SERVICE_ROLE_KEY"], "Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            u = json.load(r)
            return (u.get("email") or "").lower(), u.get("id") or ""
    except Exception:
        return "", ""


class handler(BaseHTTPRequestHandler):
    def responder(self, codigo, cuerpo):
        datos = json.dumps(cuerpo, ensure_ascii=False).encode()
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    def do_POST(self):
        env = dict(os.environ)
        token = (self.headers.get("Authorization") or "").removeprefix("Bearer ").strip()
        correo, uid = quien_llama(token, env) if token else ("", "")
        sb = P.Supabase(env)
        try:
            d = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            pdf = base64.b64decode(d.get("pdf_base64") or "", validate=True)
        except Exception:
            return self.responder(400, {"error": "No llegó un PDF válido."})
        q = urllib.parse.quote
        equipo = bool(correo) and bool(sb.uno("equipo", f"correo=eq.{q(correo)}&select=correo"))
        if not equipo:
            # Línea GLP-1 (Fase 6B): la paciente sube su propio PDF; la doctora, el de una paciente suya.
            # Sin las opciones de prueba del equipo: el documento del PDF tiene que ser el de la paciente.
            dra = sb.uno("doctoras", f"correo=eq.{q(correo)}&select=codigo") if correo else None
            pid = d.get("paciente_id") if dra else uid
            t = sb.uno("tratamientos_peso", f"paciente_id=eq.{q(pid or '')}&select=doctora_codigo") if pid else None
            if not t or (dra and t.get("doctora_codigo") != dra["codigo"]):
                return self.responder(403, {"error": "No tienes permiso para subir este resultado."})
            d = {"pdf_base64": None, "paciente_id": pid, "orden": None, "documento_pdf": None, "forzar": False}
        if not pdf.startswith(b"%PDF") or len(pdf) > MAX_PDF:
            return self.responder(400, {"error": "El archivo no es un PDF o pesa más de 3 MB."})

        # El PDF no se guarda: vive en /tmp solo mientras se lee.
        f = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        try:
            f.write(pdf)
            f.close()
            r = P.publicar(sb, f.name, (d.get("orden") or "").strip() or None, paciente_id=d.get("paciente_id") or None,
                           documento_pdf=(d.get("documento_pdf") or None), forzar=bool(d.get("forzar")))
            return self.responder(200, r)
        except SystemExit as e:
            return self.responder(422, {"error": str(e)})
        except Exception as e:  # sin datos del paciente en el mensaje
            return self.responder(500, {"error": f"Falló el análisis ({type(e).__name__})."})
        finally:
            os.unlink(f.name)
