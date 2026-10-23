"""
Saludly · Consulta web con fuentes (Perplexity Agent API)

Herramienta interna para Carlos y el médico revisor: responde una pregunta clínica o regulatoria
con búsqueda web y devuelve las fuentes. Sirve, por ejemplo, para revisar los umbrales marcados
"por verificar" contra las guías colombianas. No forma parte del flujo del paciente: el motor y el
informe no la usan, y lo que responde no cambia ninguna ficha (eso lo decide el médico revisor).

Nunca envíes datos de pacientes: solo preguntas generales. Si el texto parece traer un documento
de identidad (6 o más dígitos seguidos), la consulta no sale.

La llave sale de PERPLEXITY_API_KEY (variable de entorno o .env de la raíz). Nunca se imprime.

Uso:
  python codigo/herramientas/consultar_web.py "¿Qué punto de corte de TSH usan las guías colombianas?"
  python codigo/herramientas/consultar_web.py --dominios minsalud.gov.co,iets.org.co "…"
  python codigo/herramientas/consultar_web.py --anterior resp_… "¿Y para embarazadas?"
  python codigo/herramientas/consultar_web.py --json "…"      # salida JSON (respuesta, fuentes, id, costo)
"""
import argparse, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INSTRUCCIONES = (
    "Responde en español, de forma breve y precisa, para un médico en Bogotá, Colombia. "
    "Prioriza las guías de práctica clínica colombianas (Ministerio de Salud, IETS) y, después, guías internacionales "
    "reconocidas. Da los valores con sus unidades y di de qué guía y de qué año sale cada uno. "
    "Si las fuentes no coinciden o no encuentras el dato, dilo; no inventes cifras."
)


def leer_llave():
    llave = os.environ.get("PERPLEXITY_API_KEY")
    ruta = os.path.join(RAIZ, ".env")
    if not llave and os.path.exists(ruta):
        for l in open(ruta, encoding="utf-8"):
            if l.strip().startswith("PERPLEXITY_API_KEY="):
                llave = l.split("=", 1)[1].strip()
    if not llave:
        raise SystemExit("Falta PERPLEXITY_API_KEY. Créala en https://console.perplexity.ai y ponla en el .env "
                         "de la raíz o expórtala en tu terminal (no la pegues en el chat).")
    return llave


def consultar(pregunta, dominios=None, anterior=None, effort="low", modelo=None):
    """Hace la consulta y devuelve {respuesta, fuentes, id, costo_usd}."""
    if re.search(r"\d{6,}", pregunta):
        raise SystemExit("La pregunta parece traer un documento de identidad. No se envían datos de pacientes.")
    from perplexity import Perplexity, APIStatusError, APIConnectionError

    busqueda = {"type": "web_search", "user_location": {"country": "CO", "city": "Bogotá"}}
    if dominios: busqueda["filters"] = {"search_domain_filter": dominios}
    args = dict(input=pregunta, instructions=INSTRUCCIONES, tools=[busqueda, {"type": "fetch_url"}], language_preference="es")
    if modelo: args["model"] = modelo
    else: args["effort"] = effort
    if anterior: args["previous_response_id"] = anterior

    cliente = Perplexity(api_key=leer_llave(), timeout=120)
    try:
        r = cliente.responses.create(**args)
    except APIStatusError as e:
        espera = e.response.headers.get("retry-after")
        pista = {401: "llave inválida o revocada", 429: f"límite de uso; reintenta en {espera or '?'} s"}.get(e.status_code, "")
        raise SystemExit(f"Perplexity respondió {e.status_code} {pista}".strip())
    except APIConnectionError as e:
        raise SystemExit(f"No se pudo conectar con Perplexity: {e}")
    if r.status != "completed":
        raise SystemExit(f"La consulta terminó en estado {r.status}: {r.error}")

    fuentes, vistas = [], set()
    for item in r.output:
        if item.type == "search_results":
            pares = [(x.title, x.url) for x in item.results]
        elif item.type == "message":
            pares = [(a.title, a.url) for c in item.content for a in (c.annotations or []) if a.type == "url_citation"]
        else:
            continue
        for titulo, url in pares:
            if url not in vistas:
                vistas.add(url); fuentes.append(dict(titulo=titulo, url=url))
    costo = r.usage.cost.total_cost if r.usage and r.usage.cost else None
    return dict(respuesta=r.output_text, fuentes=fuentes, id=r.id, costo_usd=costo)


def main():
    p = argparse.ArgumentParser(description="Consulta web con fuentes (Perplexity Agent API)")
    p.add_argument("pregunta")
    p.add_argument("--dominios", help="limita la búsqueda a estos dominios, separados por coma (máx. 20)")
    p.add_argument("--anterior", help="id de una respuesta anterior para seguir la conversación")
    p.add_argument("--effort", default="low", choices=["fast", "low", "medium", "high", "xhigh"])
    p.add_argument("--modelo", help="modelo explícito (p. ej. openai/gpt-6-luna) en vez de --effort")
    p.add_argument("--json", action="store_true", help="imprime la salida en JSON")
    a = p.parse_args()
    dominios = [d.strip() for d in a.dominios.split(",") if d.strip()] if a.dominios else None
    res = consultar(a.pregunta, dominios, a.anterior, a.effort, a.modelo)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2)); return
    print(res["respuesta"], "\n\nFuentes:")
    for i, f in enumerate(res["fuentes"], 1): print(f"  {i}. {f['titulo']} · {f['url']}")
    print(f"\nid: {res['id']}" + (f" · costo: US${res['costo_usd']:.4f}" if res["costo_usd"] is not None else ""))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
    main()
