"""
Saludly · Exporta a la app del paciente el contenido que necesita del Knowledge Base:
objetivos (objetivos.yaml), alergias, dieta y medicamentos (filtros.yaml), el resto del cuestionario
(cuestionario.yaml) y el nombre y la unidad de los biomarcadores calculados (00_INDEX.json, panel "calculado"). Escribe app/src/lib/contenido.json. Correrlo cada vez que cambie alguno de esos archivos.

Uso: python codigo/herramientas/exportar_app.py
"""
import json, os
import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
F5 = os.path.join(RAIZ, "knowledge_base", "fase5")


def _y(nombre): return yaml.safe_load(open(os.path.join(F5, nombre), encoding="utf-8"))


def main():
    objetivos = [dict(id=o["id"], nombre=o["nombre"], enfoque=o.get("enfoque")) for o in _y("objetivos.yaml")]
    filtros = _y("filtros.yaml")["preguntas"]
    indice = json.load(open(os.path.join(RAIZ, "knowledge_base", "00_INDEX.json"), encoding="utf-8"))["biomarcadores"]
    calculados = {k: dict(nombre=v["nombre"], unidad="" if "sin unidad" in (v.get("unidad") or "") else v.get("unidad") or "")
                  for k, v in indice.items() if v.get("panel") == "calculado"}
    salida = dict(objetivos=objetivos, alergias=filtros["alergias"], dieta=filtros["dieta"], medicamentos=filtros["medicamentos"],
                  calculados=calculados, **_y("cuestionario.yaml"))
    ruta = os.path.join(RAIZ, "app", "src", "lib", "contenido.json")
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(f"{ruta}: {len(objetivos)} objetivos, {len(salida['alergias']['opciones'])} alergias, {len(salida['medicamentos']['opciones'])} medicamentos, {len(calculados)} calculados")


if __name__ == "__main__":
    main()
