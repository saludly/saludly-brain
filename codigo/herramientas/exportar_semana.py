"""
Saludly · Exporta la semana de prueba a las funciones de Supabase (supabase/functions/_compartido/semana.json).

El programador de envíos (Deno) arma los mensajes de cada persona con el mismo contenido aprobado que
codigo/informe/semana_prueba.py: semana_prueba.yaml, consejos_objetivos.yaml, los nombres de los objetivos y las
recetas del catálogo con su texto de WhatsApp ya redactado (nutricion.mensaje_receta). Correrlo cada vez que cambie
alguno de esos archivos o las recetas, y volver a publicar las funciones.

Uso:
  python codigo/herramientas/exportar_semana.py
  python codigo/herramientas/exportar_semana.py --esperado salida.json   además, los mensajes que arma el Python
                                                                         para las personas de prueba (los compara probar_semana.ts)
"""
import argparse, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "codigo", "informe"))
import nutricion, semana_prueba as sp

SALIDA = os.path.join(RAIZ, "supabase", "functions", "_compartido", "semana.json")
CLAVES = ["anticipo_valor", "horarios", "dias_cortisol", "familias", "bienvenida", "cortisol_general", "respuesta_boton", "respuesta_interes",
          "botones_interes", "respuesta_boton_dia7", "respuestas_cierre", "respuesta_hola_en_curso", "respuesta_otro", "recordatorio_que",
          "preguntas_receta", "ganchos", "cierre", "cierre_botones", "aviso_condicion_existente"]

# Personas de prueba: cada objetivo solo, grupos de 3, "Otro" solo, alergias y nombres compuestos
PERSONAS = [dict(nombre="Ana María", objetivos=[o], alergias=[], codigo=f"t{k:05d}") for k, o in enumerate(
    ["salud_general", "prevenir", "condicion_existente", "bajar_peso", "masa_muscular", "rendimiento", "maraton", "atletico", "energia_sueno", "envejecer_saludable"])]
PERSONAS += [
    dict(nombre="Carlos", objetivos=["bajar_peso", "prevenir", "salud_general"], alergias=["mani"], codigo="a1b2c3"),
    dict(nombre="Lucía Fernanda", objetivos=["envejecer_saludable", "condicion_existente", "atletico"], alergias=[], codigo="ff00aa"),
    dict(nombre="Andrés", objetivos=["rendimiento", "energia_sueno", "bajar_peso"], alergias=["lactosa", "huevo", "gluten"], codigo="9z8y7x"),
    dict(nombre="Paula", objetivos=["otro"], alergias=list(sp.ALERGIA), codigo="000001"),
    dict(nombre="Juan", objetivos=["maraton", "maraton", "masa_muscular"], alergias=["pescado", "mariscos"], codigo="123abc"),
]


def contenido(C, S):
    recetas = [dict(id=r["id"], nombre=r["nombre"], tiempo_comida=r["tiempo_comida"], etiquetas=r["etiquetas_calculadas"],
                    alergenos=r["alergenos"], texto=nutricion.mensaje_receta(r, C["alimentos"], {})) for r in C["catalogo"]]
    return dict(fuente="knowledge_base/fase5 (semana_prueba.yaml, consejos_objetivos.yaml, objetivos.yaml, recetas)", estado_revision=S["estado_revision"],
                **{k: S[k] for k in CLAVES},
                objetivos={k: dict(nombre=v["nombre"]) for k, v in C["objetivos"].items()},
                por_objetivo={k: dict(emoji=v["emoji"], cortisol=v["cortisol"]["texto"],
                                      consejos=[dict(id=c["id"], turno=c["turno"], texto=c["texto"]) for c in v["consejos"]])
                              for k, v in S["por_objetivo"].items()},
                recetas=recetas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--esperado")
    a = ap.parse_args()
    C, S = sp.cargar()
    errores = sp.validar(C, S)
    if errores: raise SystemExit(f"semana_prueba.py --validar tiene {len(errores)} errores: corrígelos antes de exportar")
    with open(SALIDA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(contenido(C, S), f, ensure_ascii=False, separators=(",", ":"))
    print(f"{SALIDA}: {len(C['catalogo'])} recetas, {len(S['por_objetivo'])} objetivos")
    if a.esperado:
        esperado = [dict(persona=p, dias=[sp.mensajes(C, S, p, d) for d in range(1, sp.DIAS + 1)]) for p in PERSONAS]
        json.dump(esperado, open(a.esperado, "w", encoding="utf-8"), ensure_ascii=False)
        print(f"{a.esperado}: {len(esperado)} personas")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
