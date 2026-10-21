"""
Junta en knowledge_base/fase5/frases_prohibidas.yaml todas las frases prohibidas: las de cada ficha
(condiciones, relaciones, seguridad, biomarcadores) y las reglas generales del documento 05.
El control de salida (codigo/informe/control_salida.py) usa este archivo. No se edita a mano la sección "de_fichas".

Uso:  python generar_frases_prohibidas.py
"""
import glob, os, re
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KB = os.path.join(RAIZ, "knowledge_base")

# Reglas generales (documento 05, sección 05.2, y ESQUEMAS.md). Son expresiones regulares sobre texto en minúsculas sin tildes.
PATRONES = [
    dict(id="diagnostico_tienes", patron=r"(\b(tienes|padeces|sufres de|eres|estas enfermo|estas enferma)|\busted (tiene|padece|sufre de|es|esta enferm[oa])|(?<!\bsi )(?<!\bque )\b(tiene|padece|sufre de))\s+(un[ao]?\s+)?(diabet|hipertens|anemi|hipotiroid|hipertiroid|cancer|leucemi|mieloma|lupus|artritis|cirrosis|hepatitis|chagas|insuficiencia|enfermedad|sindrome|talasemi|policitemi|trombocitemi|gammapati|sop\b|ovario poliquistico|addison|hashimoto|graves|celiac|gota|higado graso|deficiencia|deficit)", motivo="diagnóstico afirmado"),
    dict(id="diagnostico_eres", patron=r"\b(eres|usted es|es) (diabetic|hipertens|anemic|celiac)", motivo="etiqueta de enfermedad"),
    dict(id="dosis", patron=r"\b\d+([.,]\d+)?\s*(mg|mcg|µg|ug|ui|iu|tabletas?|capsulas?|gotas)\s+(de|al dia|diari)", motivo="dosis o prescripción"),
    dict(id="toma_suplemento", patron=r"\b(toma|tome)\s+(un|una|el|la)?\s*(suplemento|capsula|tableta|pastilla)", motivo="prescripción de suplemento"),
    dict(id="porcentaje_riesgo", patron=r"\b(riesgo|probabilidad)\b[^.]{0,40}\b\d+\s*%", motivo="porcentaje de riesgo sin modelo validado"),
    dict(id="falsa_tranquilidad", patron=r"\b(estas sano|estas sana|esta sano|esta sana|no es nada|no tienes nada|no tiene nada|todo esta perfecto)\b", motivo="falsa tranquilidad"),
    dict(id="alarmismo", patron=r"\b(es grave|es muy grave|peligro de muerte|vas a morir|va a morir|urgente urgente)\b", motivo="alarmismo"),
    dict(id="cura", patron=r"\b(cura|curar|garantiza|garantizado|milagro)\b", motivo="promesa de cura"),
    dict(id="wearable_diagnostico", patron=r"\b(reloj|wearable|apple watch)\b[^.]{0,40}\b(detecto|diagnostico)\b", motivo="el wearable no diagnostica"),
    dict(id="suspender_medicamento", patron=r"\b(suspende|deja de tomar|deja tu)\s+(el|la|tu|los|las)?\s*(medicamento|tratamiento|pastilla)", motivo="cambiar un tratamiento"),
]
GENERALES = ["tienes diabetes", "tienes hígado graso", "tienes hashimoto", "tienes deficiencia de hierro", "el reloj detectó una enfermedad",
             "todo está normal, estás sano", "es grave", "no es nada", "tu riesgo de infarto es del"]


def _bloque(t):
    m = re.search(r"```yaml\n(.*?)```", t, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def recolectar():
    de_fichas = {}
    for f in sorted(glob.glob(os.path.join(KB, "condiciones", "*", "*.md")) + glob.glob(os.path.join(KB, "relaciones", "*.md")) + glob.glob(os.path.join(KB, "seguridad", "*.md"))):
        y = _bloque(open(f, encoding="utf-8").read())
        fr = [x for x in (y.get("frases_prohibidas") or []) if isinstance(x, str)]
        if fr: de_fichas[y["id"]] = fr
    for f in sorted(glob.glob(os.path.join(KB, "biomarcadores", "*.md"))):
        t = open(f, encoding="utf-8").read()
        m = re.search(r"Inferencias prohibidas:\s*(.+)", t)
        if m:
            frases = re.findall(r'"([^"]+)"', m.group(1))
            if frases:
                bid = re.search(r'biomarker_id:\s*"?([a-z0-9_]+)', t).group(1)
                de_fichas[bid] = frases
    return de_fichas


if __name__ == "__main__":
    de_fichas = recolectar()
    salida = os.path.join(KB, "fase5", "frases_prohibidas.yaml")
    doc = dict(nota="Generado por codigo/herramientas/generar_frases_prohibidas.py. Los patrones se evalúan sobre texto en minúsculas y sin tildes.",
               patrones=PATRONES, generales=GENERALES, de_fichas=de_fichas)
    with open(salida, "w", encoding="utf-8", newline="\n") as fh:
        yaml.safe_dump(doc, fh, allow_unicode=True, sort_keys=False, width=200)
    print(f"{salida}: {len(PATRONES)} patrones, {len(GENERALES)} generales, frases de {len(de_fichas)} fichas ({sum(len(v) for v in de_fichas.values())} frases)")
