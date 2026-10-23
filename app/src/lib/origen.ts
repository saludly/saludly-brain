/**
 * De dónde llegó la persona: el ?ref= del enlace (un grupo de Facebook, LinkedIn, un afiche…).
 * Se guarda el primer clic en el navegador para que no se pierda al pasar por Google.
 * Los enlaces de invitación de un amigo usan ref=amigo-<código de 6 letras>.
 */
const CLAVE = "saludly-ref";

export function guardarOrigen() {
  try {
    const ref = new URLSearchParams(window.location.search).get("ref")?.toLowerCase().replace(/[^a-z0-9_-]/g, "").slice(0, 60);
    if (ref && !localStorage.getItem(CLAVE)) localStorage.setItem(CLAVE, ref);
  } catch {
    /* sin almacenamiento: el registro queda sin origen */
  }
}

/** fuente: el ref tal cual; referido_por: el código del amigo, si el ref es una invitación. */
export function leerOrigen(): { fuente: string | null; referido_por: string | null } {
  let fuente: string | null = null;
  try {
    fuente = localStorage.getItem(CLAVE);
  } catch {
    /* ignorar */
  }
  const amigo = fuente?.match(/^amigo-([a-z0-9]{6})$/)?.[1] ?? null;
  return { fuente, referido_por: amigo };
}
