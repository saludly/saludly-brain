import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { supabase } from "@/lib/sesion";

/**
 * Conversaciones de WhatsApp (solo el equipo): cada número con lo que escribió la persona y lo que le mandó Saludly
 * (el bot, la semana de prueba y las plantillas), como en un chat. Lo saliente se guarda desde el 24 oct 2026.
 * De los pre-registros muestra en qué día de la semana va, si mostró interés o pidió su cupo, y lo próximo programado.
 * En vivo (Supabase Realtime). Es solo lectura: responderle a alguien se hace desde otra herramienta.
 */
interface Mensaje {
  id: number;
  celular: string;
  texto: string | null;
  opcion: string | null;
  direccion: "entrante" | "saliente";
  recibido: string;
}
interface Persona {
  id: string;
  nombre: string;
  celular_whatsapp: string;
  estado?: string;
  prueba_dia?: number;
  anticipo_estado?: string | null;
  tipo: "preregistro" | "paciente";
}
interface Programado {
  preregistro_id: string;
  dia: number;
  envio: string;
  programado: string;
  estado: string;
}

const ENVIO: Record<string, string> = { manana: "Consejos de la mañana", receta: "Receta", cortisol: "Bájale al estrés", examen: "Solo tu examen lo dice", tarde: "Consejos de la tarde" };
const hora = (t: string) => new Date(t).toLocaleString("es-CO", { timeZone: "America/Bogota", day: "numeric", month: "short", hour: "numeric", minute: "2-digit" });

/** *negrita* de WhatsApp en negrita; el resto, tal cual. */
function Texto({ t }: { t: string }) {
  return (
    <>
      {t.split(/(\*[^*\n]+\*)/g).map((p, k) => (p.startsWith("*") && p.endsWith("*") && p.length > 2 ? <b key={k}>{p.slice(1, -1)}</b> : <span key={k}>{p}</span>))}
    </>
  );
}

function Burbuja({ m }: { m: Mensaje }) {
  const sale = m.direccion === "saliente";
  const [cuerpo, botones] = sale && m.opcion?.endsWith("botones") ? [m.texto?.replace(/\n\[[^\]]*\]$/, "") ?? "", m.texto?.match(/\n\[([^\]]*)\]$/)?.[1].split(" | ") ?? []] : [m.texto ?? "", []];
  const plantilla = m.opcion?.endsWith("plantilla");
  const fallo = m.opcion?.startsWith("fallo_");
  return (
    <div className={`flex flex-col gap-1 ${sale ? "items-end" : "items-start"}`}>
      <div className={`max-w-[85%] whitespace-pre-wrap break-words rounded-2xl px-3.5 py-2 text-sm leading-relaxed ${sale ? "rounded-tr-sm bg-optimal/10 text-ink" : "rounded-tl-sm border border-rule bg-background text-ink"}`}>
        {plantilla && <p className="mb-1 text-xs text-ink-muted">Plantilla</p>}
        <Texto t={cuerpo} />
        <p className="mt-1 text-right text-[11px] text-ink-faint">
          {hora(m.recibido)}
          {fallo && <span className="ml-2 text-red-600">No se entregó</span>}
          {m.opcion === "semana" && <span className="ml-2">tocó un botón</span>}
        </p>
      </div>
      {botones.length > 0 && (
        <div className="flex max-w-[85%] flex-wrap justify-end gap-1">
          {botones.map((b) => (
            <span key={b} className="rounded-full border border-rule px-3 py-1 text-xs text-optimal">{b}</span>
          ))}
        </div>
      )}
    </div>
  );
}

export function Conversaciones() {
  const [mensajes, setMensajes] = useState<Mensaje[] | null>(null);
  const [personas, setPersonas] = useState<Persona[]>([]);
  const [programados, setProgramados] = useState<Programado[]>([]);
  const [interes, setInteres] = useState<Set<string>>(new Set());
  const [abierto, setAbierto] = useState<string | null>(null);
  const [buscar, setBuscar] = useState("");

  const cargar = useCallback(async () => {
    const [m, pr, pa, se, re] = await Promise.all([
      supabase.from("whatsapp_mensajes").select("id,celular,texto,opcion,direccion,recibido").order("recibido", { ascending: false }).limit(3000),
      supabase.from("preregistros").select("id,nombre,celular_whatsapp,estado,prueba_dia,anticipo_estado").order("creado", { ascending: false }),
      supabase.from("pacientes").select("id,nombre,celular_whatsapp"),
      supabase.from("semana_envios").select("preregistro_id,dia,envio,programado,estado").in("estado", ["pendiente", "esperando"]).order("programado"),
      supabase.from("semana_respuestas").select("preregistro_id").eq("interes", true),
    ]);
    setMensajes(((m.data as Mensaje[] | null) ?? []).reverse());
    setPersonas([
      ...((pa.data ?? []) as Persona[]).map((p) => ({ ...p, tipo: "paciente" as const })),
      ...((pr.data ?? []) as Persona[]).map((p) => ({ ...p, tipo: "preregistro" as const })),
    ]);
    setProgramados((se.data as Programado[] | null) ?? []);
    setInteres(new Set((re.data ?? []).map((r) => r.preregistro_id as string)));
  }, []);

  // En vivo: cada mensaje que entra o sale aparece al instante (Supabase Realtime); cada minuto se recarga todo
  // por si se perdió alguno o cambió el estado de la semana.
  useEffect(() => {
    void cargar();
    const canal = supabase
      .channel("whatsapp-en-vivo")
      .on("postgres_changes", { event: "INSERT", schema: "public", table: "whatsapp_mensajes" }, (c) => {
        const m = c.new as Mensaje;
        setMensajes((xs) => (xs && !xs.some((x) => x.id === m.id) ? [...xs, m] : xs));
      })
      .subscribe();
    const t = setInterval(() => void cargar(), 60_000);
    return () => {
      clearInterval(t);
      void supabase.removeChannel(canal);
    };
  }, [cargar]);

  // Al abrir un chat o llegar un mensaje, baja hasta el último
  const fondo = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (fondo.current) fondo.current.scrollTop = fondo.current.scrollHeight;
  }, [abierto, mensajes?.length]);

  // Un chat por número, el más reciente arriba. Si el número es de un paciente y de un pre-registro, manda el paciente.
  const chats = useMemo(() => {
    const por = new Map<string, Mensaje[]>();
    for (const m of mensajes ?? []) por.set(m.celular, [...(por.get(m.celular) ?? []), m]);
    const quien = (c: string) => personas.find((p) => p.celular_whatsapp === c && p.tipo === "paciente") ?? personas.find((p) => p.celular_whatsapp === c);
    return [...por.entries()]
      .map(([celular, ms]) => ({ celular, ms, persona: quien(celular), ultimo: ms[ms.length - 1] }))
      .filter((c) => !buscar || `${c.persona?.nombre ?? ""} ${c.celular}`.toLowerCase().includes(buscar.toLowerCase()))
      .sort((a, b) => b.ultimo.recibido.localeCompare(a.ultimo.recibido));
  }, [mensajes, personas, buscar]);

  const chat = chats.find((c) => c.celular === abierto) ?? null;
  const proximos = chat?.persona?.tipo === "preregistro" ? programados.filter((p) => p.preregistro_id === chat.persona!.id).slice(0, 4) : [];

  if (!mensajes) return <p className="mt-8 text-sm text-ink-muted">Cargando conversaciones…</p>;

  const Etiquetas = ({ p }: { p?: Persona }) => (
    <span className="flex flex-wrap gap-1">
      {p?.tipo === "paciente" && <span className="rounded-full bg-surface px-2 py-0.5 text-[11px] text-ink-muted">Paciente</span>}
      {p?.tipo === "preregistro" && !!p.prueba_dia && <span className="rounded-full bg-surface px-2 py-0.5 text-[11px] text-ink-muted">Día {p.prueba_dia} de 7</span>}
      {p?.tipo === "preregistro" && interes.has(p.id) && <span className="rounded-full bg-optimal/10 px-2 py-0.5 text-[11px] text-optimal">Interesado</span>}
      {p?.anticipo_estado === "pedido" && <span className="rounded-full bg-optimal px-2 py-0.5 text-[11px] text-primary-foreground">Pidió su cupo</span>}
      {p?.estado === "baja" && <span className="rounded-full bg-surface px-2 py-0.5 text-[11px] text-ink-muted">De baja</span>}
    </span>
  );

  return (
    <section className="mt-8">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h2 className="text-2xl font-light text-ink">Conversaciones de WhatsApp</h2>
          <p className="mt-1 text-sm text-ink-muted">Lo que escriben las personas y lo que les manda Saludly desde el +57 301 130 7944. En vivo: cada mensaje aparece apenas entra o sale.</p>
        </div>
        <button type="button" onClick={() => void cargar()} className="rounded-full border border-rule px-4 py-2 text-sm text-ink">Actualizar</button>
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-[minmax(0,300px)_minmax(0,1fr)]">
        <div className={`${chat ? "hidden md:block" : ""} min-w-0`}>
          <input
            id="buscar-chat"
            value={buscar}
            onChange={(e) => setBuscar(e.target.value)}
            placeholder="Buscar por nombre o número"
            className="w-full rounded-full border border-rule bg-background px-4 py-2 text-sm text-ink outline-none focus:border-optimal"
          />
          {chats.length === 0 && <p className="mt-4 text-sm text-ink-faint">Todavía no hay conversaciones.</p>}
          <ul className="mt-3 divide-y divide-rule">
            {chats.map((c) => (
              <li key={c.celular}>
                <button
                  type="button"
                  onClick={() => setAbierto(c.celular)}
                  className={`w-full px-2 py-3 text-left transition-colors ${abierto === c.celular ? "bg-surface" : "hover:bg-surface/60"}`}
                >
                  <span className="flex justify-between gap-2 text-sm text-ink">
                    <span className="truncate">{c.persona?.nombre ?? `+${c.celular}`}</span>
                    <span className="shrink-0 text-[11px] text-ink-faint">{hora(c.ultimo.recibido)}</span>
                  </span>
                  <span className="mt-0.5 block truncate text-xs text-ink-muted">
                    {c.ultimo.direccion === "saliente" ? "Saludly: " : ""}
                    {c.ultimo.texto?.split("\n")[0]}
                  </span>
                  <span className="mt-1.5 block"><Etiquetas p={c.persona} /></span>
                </button>
              </li>
            ))}
          </ul>
        </div>

        <div className={`${chat ? "" : "hidden md:block"} min-w-0 rounded-3xl border border-rule`}>
          {!chat ? (
            <p className="p-8 text-sm text-ink-faint">Elige una conversación para verla.</p>
          ) : (
            <>
              <div className="flex items-center justify-between gap-3 border-b border-rule px-5 py-4">
                <div className="min-w-0">
                  <button type="button" onClick={() => setAbierto(null)} className="mb-1 text-xs text-optimal md:hidden">← Conversaciones</button>
                  <p className="truncate text-sm text-ink">{chat.persona?.nombre ?? "Sin registro"}</p>
                  <p className="text-xs text-ink-muted">+{chat.celular}</p>
                </div>
                <Etiquetas p={chat.persona} />
              </div>
              <div ref={fondo} className="flex max-h-[65vh] flex-col gap-3 overflow-y-auto bg-surface/40 px-4 py-5">
                {chat.ms.map((m) => <Burbuja key={m.id} m={m} />)}
              </div>
              {proximos.length > 0 && (
                <div className="border-t border-rule px-5 py-4">
                  <p className="text-xs text-ink-muted">Lo próximo de su semana</p>
                  <ul className="mt-2 space-y-1 text-sm text-ink">
                    {proximos.map((p, k) => (
                      <li key={k} className="flex justify-between gap-3">
                        <span>Día {p.dia} · {ENVIO[p.envio] ?? p.envio}</span>
                        <span className="text-xs text-ink-muted">{p.estado === "esperando" ? "Esperando que responda" : hora(p.programado)}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </section>
  );
}
