"""
Saludly Brain · RAG · Carga a Supabase

Une salida/fragmentos.jsonl con salida/vectores.jsonl y los sube a la tabla kb_fragmentos
(supabase/migrations/20261009000000_kb_fragmentos.sql) por la API REST, con upsert por id. Solo Knowledge Base: nunca datos de pacientes.

Lee SUPABASE_URL y SUPABASE_SERVICE_ROLE_KEY del .env de la raíz del proyecto (nunca del código).

Uso:  python subir.py [--borrar-viejos]     (--borrar-viejos elimina fragmentos que ya no existen en la KB)
"""
import argparse, json, os, sys, urllib.parse, urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOTE = 100


def cargar_env(ruta=os.path.join(RAIZ, ".env")):
    if os.path.exists(ruta):
        for l in open(ruta, encoding="utf-8"):
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1); os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def peticion(metodo, ruta, cuerpo=None, prefer=None):
    url = os.environ["SUPABASE_URL"].rstrip("/") + "/rest/v1/" + ruta
    clave = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
    h = {"apikey": clave, "Authorization": f"Bearer {clave}", "Content-Type": "application/json"}
    if prefer: h["Prefer"] = prefer
    datos = json.dumps(cuerpo).encode("utf-8") if cuerpo is not None else None
    with urllib.request.urlopen(urllib.request.Request(url, data=datos, headers=h, method=metodo), timeout=120) as r:
        t = r.read().decode("utf-8")
        return json.loads(t) if t else None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--borrar-viejos", action="store_true"); a = ap.parse_args()
    cargar_env()
    for k in ("SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY"):
        if not os.environ.get(k): sys.exit(f"falta {k} en el .env")
    frags = [json.loads(l) for l in open(os.path.join(AQUI, "salida", "fragmentos.jsonl"), encoding="utf-8")]
    vecs = {v["id"]: v for v in (json.loads(l) for l in open(os.path.join(AQUI, "salida", "vectores.jsonl"), encoding="utf-8"))}
    faltan = [f["id"] for f in frags if f["id"] not in vecs or vecs[f["id"]]["huella"] != f["huella"]]
    if faltan: sys.exit(f"{len(faltan)} fragmentos sin vector vigente; corre vectorizar.py primero (p. ej. {faltan[:3]})")

    filas = [dict(id=f["id"], fuente_id=f["fuente_id"], tipo=f["tipo"], orden=f["orden"], titulo=f["titulo"], contenido=f["contenido"],
                  tokens=f["tokens"], huella=f["huella"], ruta=f["ruta"], metadata=f["metadata"], version_kb=f["version_kb"],
                  modelo=vecs[f["id"]]["modelo"], embedding="[" + ",".join(f"{x:.7g}" for x in vecs[f["id"]]["vector"]) + "]")
             for f in frags]
    for i in range(0, len(filas), LOTE):
        peticion("POST", "kb_fragmentos?on_conflict=id", filas[i:i + LOTE], "resolution=merge-duplicates,return=minimal")
        print(f"  {min(i + LOTE, len(filas))}/{len(filas)}", flush=True)

    remotos = {r["id"] for r in peticion("GET", "kb_fragmentos?select=id&limit=100000")}
    viejos = sorted(remotos - {f["id"] for f in frags})
    if viejos and a.borrar_viejos:
        for i in range(0, len(viejos), LOTE):
            ids = ",".join(f'"{x}"' for x in viejos[i:i + LOTE])
            peticion("DELETE", "kb_fragmentos?id=in.(" + urllib.parse.quote(ids) + ")")
        print(f"borrados {len(viejos)} fragmentos que ya no existen en la KB")
    elif viejos:
        print(f"aviso: {len(viejos)} fragmentos en Supabase ya no existen en la KB (usa --borrar-viejos)")
    print(f"listo: {len(filas)} fragmentos en Supabase")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
