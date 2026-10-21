import { createContext, useContext, useState, type ReactNode } from "react";
import { CASOS, informeDeEjemplo } from "./datos";
import type { Informe } from "./informe";

interface Valor {
  informe: Informe;
  caso: string;
  cambiarCaso: (orden: string) => void;
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
  const [caso, setCaso] = useState(casoInicial);
  const cambiarCaso = (orden: string) => {
    setCaso(orden);
    try {
      localStorage.setItem("saludly-caso", orden);
    } catch {
      /* ignorar */
    }
  };
  return <Ctx.Provider value={{ informe: informeDeEjemplo(caso), caso, cambiarCaso }}>{children}</Ctx.Provider>;
}

export function useInforme() {
  const v = useContext(Ctx);
  if (!v) throw new Error("useInforme fuera de InformeProvider");
  return v;
}
