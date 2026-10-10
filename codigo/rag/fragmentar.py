"""
Saludly Brain · RAG · Fragmentador de la Knowledge Base

Lee knowledge_base/ (y los documentos de producto e investigación que sirven de
contexto) y produce fragmentos listos para vectorizar y subir a Supabase.

Cada fragmento sirve para dos usos:
  1. Traer el texto exacto de una ficha por su identificador (lo que pide 00_INDEX.md
     para redactar: los hallazgos del motor nombran fichas y secciones).
  2. Búsqueda por significado o por palabras para preguntas abiertas (médico, operaciones).

El RAG nunca decide umbrales: eso lo hace el motor. Aquí solo se organiza texto.

Uso:  python fragmentar.py [--salida salida/fragmentos.jsonl]
"""
import argparse, glob, hashlib, json, os, re, subprocess, sys, unicodedata
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KB = os.path.join(RAIZ, "knowledge_base")
DOCS = os.path.join(RAIZ, "docs")

MIN_TOKENS, MAX_TOKENS = 150, 800   # agrupación de secciones pequeñas y corte de las grandes


def tokens(s):
    """Aproximación para español (unos 3,6 caracteres por token)."""
    return round(len(s) / 3.6)


def sin_tildes(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()


def huella(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def version_kb():
    v = json.load(open(os.path.join(KB, "00_INDEX.json"), encoding="utf-8")).get("version")
    try:
        commit = subprocess.run(["git", "-C", RAIZ, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = ""
    return f"{v}+{commit}" if commit else str(v)


def nivel_catalogo(t):
    """Normaliza las variantes de nivel_catalogo de las fichas a cuatro valores."""
    t = sin_tildes(str(t or "")).lower()
    if "refleja" in t: return "refleja"
    if "vitamina" in t: return "vitamina"
    if "con patron" in t: return "con_patron"
    if "solo valor" in t: return "solo_valor"
    return None


def fragmento(fuente_id, tipo, orden, titulo, contenido, ruta, meta):
    contenido = contenido.strip()
    return dict(id=f"{fuente_id}#{orden:02d}", fuente_id=fuente_id, tipo=tipo, orden=orden, titulo=titulo,
                contenido=contenido, tokens=tokens(contenido), huella=huella(contenido),
                ruta=os.path.relpath(ruta, RAIZ).replace("\\", "/"), metadata=meta)


def quitar_firma(s):
    """La plantilla de firma médica no aporta al RAG."""
    return re.split(r"\n\*\*Firma médica\*\*", s)[0]


def partir_largo(texto, max_t=MAX_TOKENS):
    """Corta por párrafos un texto que supera max_t tokens."""
    if tokens(texto) <= max_t: return [texto]
    partes, actual = [], ""
    for p in re.split(r"\n\s*\n", texto):
        if actual and tokens(actual + "\n\n" + p) > max_t:
            partes.append(actual); actual = p
        else:
            actual = f"{actual}\n\n{p}" if actual else p
    if actual: partes.append(actual)
    return partes


def agrupar(secciones, min_t=MIN_TOKENS, max_t=MAX_TOKENS):
    """Une secciones consecutivas pequeñas hasta min_t sin pasar de max_t. Cada sección es (titulo, texto)."""
    grupos, actual = [], []
    for tit, txt in secciones:
        for pedazo in partir_largo(txt, max_t):
            if actual and (tokens("".join(t for _, t in actual)) >= min_t or tokens("".join(t for _, t in actual) + pedazo) > max_t):
                grupos.append(actual); actual = []
            actual.append((tit, pedazo))
    if actual: grupos.append(actual)
    return grupos


# =============================================================== biomarcadores
def biomarcadores():
    out = []
    for ruta in sorted(glob.glob(os.path.join(KB, "biomarcadores", "*.md"))):
        s = open(ruta, encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n(.*)", s, re.S)
        y, cuerpo = yaml.safe_load(m.group(1)), m.group(2)
        bid = y["biomarker_id"]
        meta = dict(biomarker_id=bid, nombre=y.get("name_es"), sinonimos=y.get("sinonimos") or [],
                    unidad_canonica=y.get("unidad_canonica"), nivel_catalogo=nivel_catalogo(y.get("nivel_catalogo")),
                    nivel_catalogo_original=y.get("nivel_catalogo"), panel=y.get("panel"), sexo=y.get("sexo"),
                    estado_ficha=str(y.get("status") or "").lower() or None, alimenta=y.get("alimenta") or [],
                    requiere_revision_profesional=y.get("requires_professional_review"))
        cab = f"Ficha de biomarcador: {y.get('name_es')} ({bid})"
        secciones = [(p.splitlines()[0].strip(), "## " + p) for p in re.split(r"^## ", cuerpo, flags=re.M)[1:]]
        orden = 0
        # Las notas de decisión de Saludly mandan sobre el resto de la ficha: van solas y marcadas
        for tit, txt in secciones:
            if tit.startswith("Notas de decisión") or tit.startswith("⚠️"):
                out.append(fragmento(bid, "biomarcador", orden, f"{cab} · {tit}", f"{cab}\n\n{txt}", ruta,
                                     dict(meta, secciones=[tit], prioridad="decision_saludly")))
                orden += 1
        resto = [(t, x) for t, x in secciones if not (t.startswith("Notas de decisión") or t.startswith("⚠️"))]
        for g in agrupar(resto):
            tits = list(dict.fromkeys(t for t, _ in g))
            letras = [re.match(r"([A-N])\.", t).group(1) for t in tits if re.match(r"[A-N]\.", t)]
            out.append(fragmento(bid, "biomarcador", orden, f"{cab} · {' / '.join(tits)}",
                                 f"{cab}\n\n" + "\n\n".join(x for _, x in g), ruta,
                                 dict(meta, secciones=tits, letras=letras)))
            orden += 1
    return out


# =============================================================== condiciones, relaciones, seguridad
def fichas_con_yaml(carpeta, tipo):
    out = []
    for ruta in sorted(glob.glob(os.path.join(KB, carpeta, "**", "*.md"), recursive=True)):
        s = quitar_firma(open(ruta, encoding="utf-8").read())
        y = yaml.safe_load(re.search(r"```yaml\n(.*?)```", s, re.S).group(1))
        meta = {k: y.get(k) for k in ("nombre", "modulo", "modulos", "especialidad", "tipo", "detectabilidad", "escalamiento",
                                      "nivel_lenguaje", "biomarcador", "biomarcadores", "guias", "fuerza_evidencia",
                                      "implementada_por", "revision_medica_obligatoria", "frases_prohibidas", "por_verificar") if y.get(k) is not None}
        meta["tipo_ficha"] = meta.pop("tipo", None)
        for i, parte in enumerate(partir_largo(s, 1200)):   # las fichas caben enteras; 1200 es solo un tope de seguridad
            out.append(fragmento(y["id"], tipo, i, f"{y['id']} · {y.get('nombre')}", parte, ruta, meta))
    return out


# =============================================================== documentos
DOCUMENTOS = [
    # (carpeta, tipo, incluir). docs/04 son copias compiladas de las fichas: se excluyen para no traer versiones viejas.
    ("01_serie_saludly_brain", "documento_producto"),
    ("03_investigacion_clinica", "evidencia"),
]

def documentos():
    out = []
    for carpeta, tipo in DOCUMENTOS:
        for ruta in sorted(glob.glob(os.path.join(DOCS, carpeta, "*.md"))):
            s = open(ruta, encoding="utf-8").read()
            nombre = os.path.splitext(os.path.basename(ruta))[0]
            fid = "DOC-" + re.sub(r"[^A-Za-z0-9]+", "-", sin_tildes(nombre)).strip("-")[:60]
            partes = re.split(r"^(?=#{1,3} )", s, flags=re.M)
            secciones = [((p.splitlines()[0].lstrip("#").strip() if p.startswith("#") else "Introducción"), p) for p in partes if p.strip()]
            for i, g in enumerate(agrupar(secciones, 200, MAX_TOKENS)):
                tits = list(dict.fromkeys(t for t, _ in g))
                out.append(fragmento(fid, tipo, i, f"{nombre} · {' / '.join(tits)[:200]}",
                                     f"Documento: {nombre}\n\n" + "\n\n".join(x for _, x in g), ruta,
                                     dict(documento=nombre, secciones=tits)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "salida", "fragmentos.jsonl"))
    a = ap.parse_args()
    v = version_kb()
    todos = biomarcadores() + fichas_con_yaml("condiciones", "condicion") + fichas_con_yaml("relaciones", "relacion") \
        + fichas_con_yaml("seguridad", "seguridad") + documentos()
    ids = [f["id"] for f in todos]
    assert len(ids) == len(set(ids)), "identificadores de fragmento repetidos"
    os.makedirs(os.path.dirname(a.salida), exist_ok=True)
    with open(a.salida, "w", encoding="utf-8", newline="\n") as fh:
        for f in todos:
            f["version_kb"] = v
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    resumen = {}
    for f in todos:
        r = resumen.setdefault(f["tipo"], dict(fuentes=set(), fragmentos=0, tokens=0, max=0))
        r["fuentes"].add(f["fuente_id"]); r["fragmentos"] += 1; r["tokens"] += f["tokens"]; r["max"] = max(r["max"], f["tokens"])
    print(f"versión KB {v} → {a.salida}")
    for t, r in resumen.items():
        print(f"  {t:20s} fuentes {len(r['fuentes']):4d}  fragmentos {r['fragmentos']:5d}  tokens {r['tokens']:7d}  máx {r['max']:5d}")
    print(f"  {'TOTAL':20s} fragmentos {len(todos)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
