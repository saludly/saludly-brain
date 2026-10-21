import { Phone } from "lucide-react";
import { Marca } from "@/components/Comunes";

/** Escalamiento 3 o serología reactiva: el informe no se muestra hasta que el equipo médico llame (documento 05.3). */
export function Retenido() {
  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto flex min-h-screen max-w-xl flex-col px-6 py-8">
        <Marca />
        <div className="rise mt-24 rounded-3xl border border-rule p-8 text-center">
          <span className="mx-auto grid h-12 w-12 place-items-center rounded-2xl bg-optimal-soft text-optimal">
            <Phone className="h-5 w-5" strokeWidth={1.6} />
          </span>
          <h1 className="mt-6 text-2xl font-light tracking-tight text-ink">Nuestro equipo médico lo va a llamar hoy.</h1>
          <p className="mt-3 text-sm leading-relaxed text-ink-muted">
            Uno de sus resultados necesita que un médico se lo explique con calma. Su informe completo aparecerá aquí después de esa llamada.
          </p>
          <p className="mt-6 text-xs leading-relaxed text-ink-faint">
            Si se siente mal, con dolor en el pecho, falta de aire, confusión o desmayo, vaya a urgencias.
          </p>
        </div>
      </div>
    </main>
  );
}
