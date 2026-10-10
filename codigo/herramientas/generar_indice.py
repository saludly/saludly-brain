"""
Genera knowledge_base/00_INDEX.json a partir de las fichas (biomarcadores, condiciones, relaciones y seguridad)
y lo copia a donde el motor y el lector tienen su copia. Nunca se edita a mano.

Uso:  python generar_indice.py            # escribe y sincroniza las copias
      python generar_indice.py --comparar # solo muestra las diferencias con el índice actual
"""
import glob, json, os, re, sys
from datetime import date
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KB = os.path.join(RAIZ, "knowledge_base")
COPIAS = [os.path.join(RAIZ, "codigo", "motor", "pruebas", "00_INDEX.json"), os.path.join(RAIZ, "codigo", "lector_pdf", "00_INDEX.json")]


def _frontmatter(t): return yaml.safe_load(re.search(r"^---\n(.*?)\n---", t, re.S).group(1))
def _bloque(t): return yaml.safe_load(re.search(r"```yaml\n(.*?)```", t, re.S).group(1))


def _esc(e):
    if e is None: return "—"
    if isinstance(e, dict):
        vals = sorted({v for v in e.values() if isinstance(v, int)})
        return ", ".join(str(v) for v in vals) if vals else "—"
    return str(e)


def construir(anterior):
    bio, cond, rel, seg = {}, {}, {}, {}
    for f in sorted(glob.glob(os.path.join(KB, "biomarcadores", "*.md"))):
        h = _frontmatter(open(f, encoding="utf-8").read())
        panel = str(h.get("panel") or "").split(",")[0].strip()   # "estándar, todas las personas" -> "estándar"
        reglas = [x for x in (h.get("alimenta") or []) if re.match(r"(COND|SEG|REL)-", str(x))]
        bio[h["biomarker_id"]] = dict(nombre=h.get("name_es"), unidad=h.get("unidad_canonica"), panel=panel,
                                      nivel=h.get("nivel_catalogo"), sinonimos=h.get("sinonimos") or [], reglas=reglas)
    for f in sorted(glob.glob(os.path.join(KB, "condiciones", "*", "*.md"))):
        y = _bloque(open(f, encoding="utf-8").read())
        usa = sorted({c["biomarcador"] for c in (y.get("criterios") or []) if isinstance(c, dict) and c.get("biomarcador") in bio})
        cond[y["id"]] = dict(id=y["id"], nombre=y.get("nombre"), modulo=y.get("modulo"), esp=y.get("especialidad"), tipo=y.get("tipo"),
                             det=y.get("detectabilidad"), esc=_esc(y.get("escalamiento")), usa=usa)
    for f in sorted(glob.glob(os.path.join(KB, "relaciones", "*.md"))):
        y = _bloque(open(f, encoding="utf-8").read())
        rel[y["id"]] = dict(nombre=y.get("nombre"), tipo=y.get("tipo"), biomarcadores=y.get("biomarcadores") or [], implementada_por=y.get("implementada_por") or [])
    for f in sorted(glob.glob(os.path.join(KB, "seguridad", "*.md"))):
        y = _bloque(open(f, encoding="utf-8").read())
        usa = y.get("biomarcadores") or ([y["biomarcador"]] if y.get("biomarcador") else [])
        seg[y["id"]] = dict(id=y["id"], nombre=y.get("nombre"), usa=usa)
    # se conservan los campos de entradas anteriores que la ficha no trae, y el orden y las reglas
    # que el índice anterior ya tenía (algunas se escribieron a mano)
    for nombre, nuevo in (("biomarcadores", bio), ("condiciones", cond), ("relaciones", rel), ("seguridad", seg)):
        for k, v in nuevo.items():
            viejo = (anterior.get(nombre) or {}).get(k) or {}
            for campo, val in viejo.items():
                if campo not in v or v[campo] in (None, [], "", "—"): v[campo] = val
                elif isinstance(val, list) and isinstance(v[campo], list) and campo in ("reglas", "usa", "implementada_por"):
                    v[campo] = list(val) + [x for x in v[campo] if x not in val]
    return dict(relaciones=rel, version=anterior.get("version", "1"), generado=str(date.today()), biomarcadores=bio, condiciones=cond, seguridad=seg)


if __name__ == "__main__":
    ruta = os.path.join(KB, "00_INDEX.json")
    anterior = json.load(open(ruta, encoding="utf-8"))
    nuevo = construir(anterior)
    if "--comparar" in sys.argv:
        for sec in ("biomarcadores", "condiciones", "relaciones", "seguridad"):
            a, b = anterior[sec], nuevo[sec]
            for k in sorted(set(a) | set(b)):
                if a.get(k) != b.get(k): print(f"{sec}/{k}:\n  antes  {json.dumps(a.get(k), ensure_ascii=False)}\n  ahora  {json.dumps(b.get(k), ensure_ascii=False)}")
            print(f"{sec}: {len(a)} -> {len(b)}")
        sys.exit(0)
    for p in [ruta] + COPIAS:
        json.dump(nuevo, open(p, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print(f"Índice escrito: {len(nuevo['biomarcadores'])} biomarcadores, {len(nuevo['condiciones'])} condiciones, "
          f"{len(nuevo['relaciones'])} relaciones, {len(nuevo['seguridad'])} de seguridad; copiado a {len(COPIAS)} lugares.")
