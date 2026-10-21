"""Carga el contenido de la Fase 5 (knowledge_base/fase5) y el índice del Knowledge Base."""
import glob, json, os
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KB = os.path.join(RAIZ, "knowledge_base")
F5 = os.path.join(KB, "fase5")


def _y(p): return yaml.safe_load(open(p, encoding="utf-8"))


def cargar():
    idx = json.load(open(os.path.join(KB, "00_INDEX.json"), encoding="utf-8"))
    red = {}
    for f in glob.glob(os.path.join(F5, "redaccion", "*.yaml")):
        if os.path.basename(f) == "modulos.yaml": continue
        d = _y(f); red[d["id"]] = d
    mod_p = os.path.join(F5, "redaccion", "modulos.yaml")
    modulos = _y(mod_p) if os.path.exists(mod_p) else []
    recs = []
    for f in sorted(glob.glob(os.path.join(F5, "recomendaciones", "*.yaml"))):
        recs += _y(f) or []
    al_p = os.path.join(F5, "recetas", "alimentos.yaml")
    alimentos = {a["id"]: a for a in (_y(al_p) or [])} if os.path.exists(al_p) else {}
    recetas = []
    for f in sorted(glob.glob(os.path.join(F5, "recetas", "*.yaml"))):
        if os.path.basename(f) != "alimentos.yaml": recetas += _y(f) or []
    objetivos = {o["id"]: o for o in _y(os.path.join(F5, "objetivos.yaml"))}
    fil_p = os.path.join(F5, "filtros.yaml")
    filtros = _y(fil_p) if os.path.exists(fil_p) else {}
    return dict(indice=idx, redaccion=red, modulos=modulos, recomendaciones=recs, alimentos=alimentos, recetas=recetas, objetivos=objetivos, filtros=filtros,
                criterios=criterios_de_condiciones(), version_kb=f"{idx.get('version')}·{idx.get('generado')}")


def criterios_de_condiciones():
    """{condición: {id de criterio: biomarcador}} desde el bloque yaml de cada ficha de condición."""
    out = {}
    for f in glob.glob(os.path.join(KB, "condiciones", "*", "*.md")):
        s = open(f, encoding="utf-8").read()
        i = s.find("```yaml")
        if i < 0: continue
        y = yaml.safe_load(s[i + 7:s.find("```", i + 7)]) or {}
        out[y.get("id")] = {c["id"]: c.get("biomarcador") for c in y.get("criterios") or [] if c.get("id") and c.get("biomarcador")}
    return out
