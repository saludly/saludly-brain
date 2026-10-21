import { createContext, useContext, useState, type ReactNode } from "react";
import { CASOS, informeDeEjemplo } from "./datos";
import type { Informe } from "./informe";
import { useSesion } from "./sesion";

interface Valor {
  informe: Informe;
  /** "propio": el informe aprobado del paciente; "revision": el que el médico está revisando; "demo": un caso de ejemplo. */
  origen: "propio" | "revision" | "demo";
  caso: string;
  cambiarCaso: (orden: string) => void;
  revisar: (informe: Informe | null) => void;
}

const Ctx = createContext<Valor | null>(null);

function casoInicial() {
  try {
    const url = new URLSearchParams(window.location.search).get("caso");
    if (url && CASOS.some((c) => c.id.endsWith(url))) return CASOS.find((c) => c.id.endsWith(url))!.id;
    const guardado = localStorage.getItem("saludly-caso");
    if (guardado && CASOS.some((c) => c.id === guardado)) return guardado;
  } catch {
    /* sin almacenamiento: se usa el primer caso */
  }
  return CASOS[0]!.id;
}

export function InformeProvider({ children }: { children: ReactNode }) {
  const s = useSesion();
  const [caso, setCaso] = useState(casoInicial);
  const [enRevision, revisar] = useState<Informe | null>(null);
  const cambiarCaso = (orden: string) => {
    setCaso(orden);
    try {
      localStorage.setItem("saludly-caso", orden);
    } catch {
      /* ignorar */
    }
  };
  const [informe, origen]: [Informe, Valor["origen"]] = enRevision
    ? [enRevision, "revision"]
    : s.informe
      ? [s.informe, "propio"]
      : [informeDeEjemplo(caso), "demo"];
  return <Ctx.Provider value={{ informe, origen, caso, cambiarCaso, revisar }}>{children}</Ctx.Provider>;
}

export function useInforme() {
  const v = useContext(Ctx);
  if (!v) throw new Error("useInforme fuera de InformeProvider");
  return v;
}
