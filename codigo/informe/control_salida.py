"""
Saludly Brain · Control de salida (documentos 04.10 y 05)

Revisa cualquier texto que vaya al paciente (dashboard o WhatsApp) contra las frases prohibidas del
Knowledge Base (knowledge_base/fase5/frases_prohibidas.yaml) y contra las reglas de canal:
ningún escalamiento 3 ni serología reactiva sale por WhatsApp.
Se usa igual con las plantillas de hoy que con el texto que redacte DeepSeek después.
"""
import os, re, unicodedata
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_FP = yaml.safe_load(open(os.path.join(RAIZ, "knowledge_base", "fase5", "frases_prohibidas.yaml"), encoding="utf-8"))


def normalizar(t):
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", t).strip()


_PATRONES = [(p["id"], re.compile(p["patron"]), p["motivo"]) for p in _FP["patrones"]]
# Frases literales: las generales y las de las fichas con al menos dos palabras (una sola palabra daría falsos positivos)
_FRASES = [(normalizar(f), "general") for f in _FP["generales"]] + \
          [(normalizar(f), fid) for fid, fs in _FP["de_fichas"].items() for f in fs if len(normalizar(f).split()) >= 2]
_FRASES = [(f.strip(" .\"'"), o) for f, o in _FRASES if f.strip(" .\"'")]


def revisar(texto):
    """Devuelve la lista de problemas encontrados en un texto (vacía si está bien)."""
    n = normalizar(texto)
    problemas = []
    for pid, rx, motivo in _PATRONES:
        m = rx.search(n)
        if m: problemas.append(dict(regla=pid, motivo=motivo, fragmento=m.group(0)))
    for frase, origen in _FRASES:
        if frase and frase in n:
            problemas.append(dict(regla="frase_prohibida", motivo=f"frase prohibida ({origen})", fragmento=frase))
    return problemas


def revisar_todo(textos):
    """textos: lista de (ubicacion, texto). Devuelve [(ubicacion, problema), ...]."""
    out = []
    for ubic, t in textos:
        for p in revisar(t or ""):
            out.append((ubic, p))
    return out


SEROLOGIAS = ("COND-M4-IN-001", "COND-M4-IN-002", "COND-M4-IN-003")

def permitido_por_whatsapp(hallazgo):
    """Regla del documento 05.3: nada de escalamiento 3 ni serologías reactivas por WhatsApp; nivel 2 solo como aviso general.
    Una serología es reactiva cuando el motor le pone canal "llamada del médico" (anti-HBs no protector, por ejemplo, no lo es)."""
    if (hallazgo.get("escalamiento") or 0) >= 3: return False
    if hallazgo.get("id") in SEROLOGIAS and hallazgo.get("canal") == "llamada del médico": return False
    return True
