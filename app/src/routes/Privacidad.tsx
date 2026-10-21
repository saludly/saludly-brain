import { Fragment, type ReactNode } from "react";
import { Marca } from "@/components/Comunes";
import POLITICA from "../../../docs/06_legal/Politica_tratamiento_datos.md?raw";

/**
 * Política de tratamiento de datos, pública (la enlaza la pantalla de consentimiento de Google).
 * Se lee de docs/06_legal/Politica_tratamiento_datos.md, de la sección 1 a la 10: el título, la nota de borrador
 * y los "Puntos para el abogado" no se muestran. El lector de Markdown cubre solo lo que usa ese archivo.
 */
const texto = POLITICA.replace(/\r\n/g, "\n");
const cuerpo = texto.slice(texto.indexOf("## 1.")).split("\n---\n")[0]!;

function enLinea(texto: string): ReactNode[] {
  return texto.split(/(\*\*[^*]+\*\*)/).map((t, i) =>
    t.startsWith("**") ? (
      <strong key={i} className="font-medium text-ink">
        {t.slice(2, -2)}
      </strong>
    ) : (
      <Fragment key={i}>{t}</Fragment>
    ),
  );
}

function celdas(fila: string) {
  return fila.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
}

function bloques(md: string): ReactNode[] {
  return md
    .split(/\n\s*\n/)
    .map((b) => b.trim())
    .filter(Boolean)
    .map((b, i) => {
      const lineas = b.split("\n");
      if (b.startsWith("## "))
        return (
          <h2 key={i} className="mt-10 text-xl font-light tracking-tight text-ink">
            {b.slice(3)}
          </h2>
        );
      if (b.startsWith("|")) {
        const [cabeza, , ...filas] = lineas;
        return (
          <div key={i} className="mt-4 overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-rule text-ink">
                  {celdas(cabeza!).map((c) => (
                    <th key={c} className="py-2 pr-4 font-medium">
                      {c}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="text-ink-muted">
                {filas.map((f, j) => (
                  <tr key={j} className="border-b border-rule align-top">
                    {celdas(f).map((c, k) => (
                      <td key={k} className="py-2 pr-4">
                        {enLinea(c)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        );
      }
      if (/^(- |\d+\. )/.test(b)) {
        const numerada = /^\d/.test(b);
        const Lista = numerada ? "ol" : "ul";
        return (
          <Lista key={i} className={`mt-4 space-y-2 pl-5 text-sm leading-relaxed text-ink-muted ${numerada ? "list-decimal" : "list-disc"}`}>
            {lineas.map((l, j) => (
              <li key={j}>{enLinea(l.replace(/^(- |\d+\. )/, ""))}</li>
            ))}
          </Lista>
        );
      }
      return (
        <p key={i} className="mt-4 text-sm leading-relaxed text-ink-muted">
          {enLinea(b)}
        </p>
      );
    });
}

export function Privacidad() {
  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-2xl px-6 py-8">
        <Marca />
        <h1 className="mt-12 text-3xl font-light tracking-tight text-ink">Política de tratamiento de datos personales</h1>
        <p className="mt-3 text-sm text-ink-muted">Ley 1581 de 2012 y Decreto 1074 de 2015.</p>
        {bloques(cuerpo)}
      </div>
    </main>
  );
}
