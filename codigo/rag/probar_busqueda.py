"""
Saludly Brain · RAG · Prueba de calidad de la búsqueda semántica (local, sin Supabase)

Cada consulta tiene las fichas que deberían aparecer entre los primeros resultados.
Mide en cuántas aparece al menos una de ellas en el top 5.

Uso:  python probar_busqueda.py              local, solo semántica (salida/vectores.jsonl + Ollama)
      python probar_busqueda.py --supabase   búsqueda híbrida real en Supabase (buscar_kb)
"""
import json, math, os, sys
from vectorizar import embeber, MODELO
from subir import cargar_env, peticion

AQUI = os.path.dirname(os.path.abspath(__file__))
TOP = 5

CONSULTAS = [
    ("¿Qué significa tener la ferritina baja si la PCR está alta?", {"ferritin", "COND-M3-HE-002", "COND-M3-HE-003", "REL-013"}),
    ("La troponina salió elevada, ¿qué hace Saludly?", {"SEG-001", "hs_troponin", "REL-005"}),
    ("¿La biotina altera la TSH y la T4 libre?", {"biotin", "tsh", "free_t4"}),
    ("Corte de hemoglobina para anemia en Bogotá por la altura", {"COND-M3-HE-001", "hemoglobin"}),
    ("Riesgo de fibrosis por hígado graso con FIB-4", {"COND-M4-GA-001", "fib4"}),
    ("Lipoproteína(a) alta y riesgo cardiovascular", {"COND-M1-CA-004", "lpa"}),
    ("Hierro bajo con anticuerpos antitiroideos positivos", {"REL-016", "REL-019", "COND-M2-TI-A01"}),
    ("PSA elevado en un hombre de 55 años", {"COND-M5-UR-001", "psa_total", "COND-M5-UR-A02"}),
    ("Glucosa en ayunas de 110 y hemoglobina glicosilada de 5,9", {"COND-M1-EM-001", "glucose", "hba1c", "REL-001"}),
    ("Vitamina D baja, ¿se recomienda suplementar?", {"COND-M3-NU-A03", "vitamin_d"}),
    ("TSH alta con T4 libre normal", {"COND-M2-TI-001", "tsh", "REL-017"}),
    ("Anticuerpos antinucleares ANA 1:160", {"COND-M6-RE-A01", "ana_hep2"}),
    ("Serología positiva para Chagas", {"COND-M4-IN-003", "chagas_elisa_total", "chagas_elisa_recombinante"}),
    ("Anti-HBs no protector después de la vacuna de hepatitis B", {"COND-M4-IN-002", "anti_hbs"}),
    ("Cortisol tomado por la tarde, ¿se puede interpretar?", {"cortisol", "SEG-002"}),
    ("Triglicéridos mayores de 500", {"COND-M1-CA-003", "triglycerides"}),
    ("Creatinina alta y tasa de filtración glomerular baja", {"COND-M2-NE-001", "creatinine", "egfr"}),
    ("Ácido úrico alto sin síntomas de gota", {"COND-M6-RE-001", "uric_acid"}),
    ("Frases prohibidas: no decir que la persona tiene diabetes", {"DOC-05-SALUDLY-BRAIN-Seguridad-y-escalamiento", "COND-M1-EM-002"}),
    ("Conflicto entre guías sobre el corte de ferritina 15 o 30", {"ferritin", "COND-M3-HE-002", "COND-M3-HE-003", "DOC-Lote-3-Hematologia-y-Nutricion"}),
]


def coseno(a, b):
    return sum(x * y for x, y in zip(a, b)) / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def fuentes_supabase(q, v):
    filas = peticion("POST", "rpc/buscar_kb", dict(consulta_texto=q, consulta_vector="[" + ",".join(map(str, v)) + "]", n=20))
    fuentes = []
    for f in filas:
        if f["fuente_id"] not in fuentes: fuentes.append(f["fuente_id"])
    return fuentes[:TOP]


def main_supabase():
    cargar_env()
    qv = embeber([q for q, _ in CONSULTAS], MODELO, os.environ.get("OLLAMA_URL", "http://localhost:11434"))
    aciertos = 0
    for (q, esperadas), v in zip(CONSULTAS, qv):
        fuentes = fuentes_supabase(q, v)
        ok = bool(esperadas & set(fuentes)); aciertos += ok
        print(f"{'OK   ' if ok else 'FALLA'} {q}\n       → {', '.join(fuentes)}")
    print(f"\nAciertos en top {TOP} (Supabase, híbrida): {aciertos} de {len(CONSULTAS)}")


def main():
    frags = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(AQUI, "salida", "fragmentos.jsonl"), encoding="utf-8")}
    vecs = [json.loads(l) for l in open(os.path.join(AQUI, "salida", "vectores.jsonl"), encoding="utf-8")]
    modelo = vecs[0]["modelo"]
    qv = embeber([q for q, _ in CONSULTAS], modelo, os.environ.get("OLLAMA_URL", "http://localhost:11434"))
    aciertos = 0
    for (q, esperadas), v in zip(CONSULTAS, qv):
        orden = sorted(vecs, key=lambda x: -coseno(v, x["vector"]))
        fuentes = []
        for x in orden:   # top 5 de fuentes distintas
            f = frags[x["id"]]["fuente_id"]
            if f not in fuentes: fuentes.append(f)
            if len(fuentes) == TOP: break
        ok = bool(esperadas & set(fuentes)); aciertos += ok
        print(f"{'OK   ' if ok else 'FALLA'} {q}\n       → {', '.join(fuentes)}")
    print(f"\nAciertos en top {TOP}: {aciertos} de {len(CONSULTAS)} ({modelo})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main_supabase() if "--supabase" in sys.argv else main()
