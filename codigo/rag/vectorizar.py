"""
Saludly Brain · RAG · Vectorización de los fragmentos

Lee salida/fragmentos.jsonl (de fragmentar.py), calcula el vector de cada fragmento
con un modelo local de Ollama y escribe salida/vectores.jsonl.

Es incremental: si un fragmento conserva su huella y su modelo, no se vuelve a calcular.
Cada lote se agrega al archivo apenas termina, así que si se interrumpe, al volver a correrlo sigue donde iba.
Las consultas del agente deben usar el MISMO modelo; si se cambia, se vectoriza todo de nuevo.

Uso:  python vectorizar.py [--modelo bge-m3] [--ollama http://localhost:11434]
"""
import argparse, json, os, sys, time, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
MODELO = "bge-m3"          # multilingüe, 1.024 dimensiones, hasta 8.192 tokens por texto
LOTE = 8


def embeber(textos, modelo, url):
    datos = json.dumps(dict(model=modelo, input=textos)).encode("utf-8")
    req = urllib.request.Request(f"{url}/api/embed", data=datos, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)["embeddings"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo", default=MODELO)
    ap.add_argument("--ollama", default=os.environ.get("OLLAMA_URL", "http://localhost:11434"))
    ap.add_argument("--entrada", default=os.path.join(AQUI, "salida", "fragmentos.jsonl"))
    ap.add_argument("--salida", default=os.path.join(AQUI, "salida", "vectores.jsonl"))
    a = ap.parse_args()

    frags = [json.loads(l) for l in open(a.entrada, encoding="utf-8")]
    previos = {}
    if os.path.exists(a.salida):
        for l in open(a.salida, encoding="utf-8"):
            v = json.loads(l); previos[v["id"]] = v
    pendientes = [f for f in frags if not (f["id"] in previos and previos[f["id"]]["huella"] == f["huella"] and previos[f["id"]]["modelo"] == a.modelo)]
    print(f"{len(frags)} fragmentos; {len(frags) - len(pendientes)} ya vectorizados; {len(pendientes)} por calcular con {a.modelo}")

    nuevos, t0 = {}, time.time()
    os.makedirs(os.path.dirname(a.salida), exist_ok=True)
    with open(a.salida, "a", encoding="utf-8", newline="\n") as avance:
        for i in range(0, len(pendientes), LOTE):
            lote = pendientes[i:i + LOTE]
            # El título va delante del contenido para que el vector sepa de qué ficha y sección es
            vecs = embeber([f"{f['titulo']}\n\n{f['contenido']}" for f in lote], a.modelo, a.ollama)
            for f, v in zip(lote, vecs):
                nuevos[f["id"]] = dict(id=f["id"], huella=f["huella"], modelo=a.modelo, dimension=len(v), vector=v)
                avance.write(json.dumps(nuevos[f["id"]]) + "\n")
            avance.flush()   # guarda el avance de cada lote
            hechos, seg = min(i + LOTE, len(pendientes)), time.time() - t0
            print(f"  {hechos}/{len(pendientes)}  ({seg:.0f} s, faltan ~{seg / hechos * (len(pendientes) - hechos) / 60:.0f} min)", flush=True)

    vigentes = {f["id"] for f in frags}
    final = {k: v for k, v in previos.items() if k in vigentes}; final.update(nuevos)
    # Reescribe el archivo compacto, en el orden de los fragmentos y sin repetidos
    with open(a.salida, "w", encoding="utf-8", newline="\n") as fh:
        for f in frags:
            fh.write(json.dumps(final[f["id"]]) + "\n")
    dims = {v["dimension"] for v in final.values()}
    print(f"listo: {len(final)} vectores, dimensión {dims}, en {a.salida}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
