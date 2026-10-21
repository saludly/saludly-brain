import { useEffect, useState } from "react";
import { useNavigate } from "@tanstack/react-router";
import { Campo, Opcion, Pantalla, Titulo, claseEntrada } from "@/components/Formulario";
import { VERSION_AUTORIZACION, siguientePaso, supabase, useSesion } from "@/lib/sesion";

/** Datos de la cuenta y autorización de tratamiento de datos (docs/06_legal/Autorizacion_tratamiento_datos.md). */
export function Registro() {
  const s = useSesion();
  const navigate = useNavigate();
  const [paso, setPaso] = useState(1);
  const [nombre, setNombre] = useState("");
  const [cedula, setCedula] = useState("");
  const [celular, setCelular] = useState("");
  const [direccion, setDireccion] = useState("");
  const [edad, setEdad] = useState("");
  const [sexo, setSexo] = useState<"hombre" | "mujer" | "">("");
  const [aceptaDatos, setAceptaDatos] = useState(false);
  const [aceptaWhatsapp, setAceptaWhatsapp] = useState(false);
  const [ocupado, setOcupado] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (s.cargando) return;
    if (!s.sesion) void navigate({ to: "/entrar" });
    else if (s.paciente && s.autorizado) void navigate({ to: siguientePaso(s) });
    else if (s.paciente) {
      setNombre(s.paciente.nombre);
      setCedula(s.paciente.cedula);
      setCelular(s.paciente.celular_whatsapp.slice(2));
      setDireccion(s.paciente.direccion);
      setEdad(String(s.paciente.edad));
      setSexo(s.paciente.sexo);
      setPaso(2);
    }
  }, [s, navigate]);

  const datosValidos =
    nombre.trim().length >= 3 && /^\d{5,12}$/.test(cedula) && /^3\d{9}$/.test(celular) && direccion.trim().length >= 5 && Number(edad) >= 18 && Number(edad) <= 110 && sexo !== "";

  const guardarDatos = async () => {
    setError(null);
    setOcupado(true);
    const { error } = await supabase.from("pacientes").upsert({
      id: s.sesion!.user.id,
      nombre: nombre.trim(),
      cedula,
      celular_whatsapp: `57${celular}`,
      direccion: direccion.trim(),
      edad: Number(edad),
      sexo,
    });
    setOcupado(false);
    if (error) return setError("No pudimos guardar tus datos. Revísalos e intenta de nuevo.");
    setPaso(2);
  };

  const firmar = async () => {
    setError(null);
    setOcupado(true);
    const { error } = await supabase.from("autorizaciones").insert({
      version: VERSION_AUTORIZACION,
      acepta_datos: aceptaDatos,
      acepta_whatsapp: aceptaWhatsapp,
      agente: navigator.userAgent.slice(0, 200),
    });
    if (error) {
      setOcupado(false);
      return setError("No pudimos registrar tu autorización. Intenta de nuevo.");
    }
    await s.recargar();
    setOcupado(false);
    void navigate({ to: "/cuestionario" });
  };

  if (paso === 1)
    return (
      <Pantalla paso={1} total={2} etiqueta="Tus datos" boton="Continuar" puedeSeguir={datosValidos} ocupado={ocupado} onSeguir={guardarDatos} error={error}>
        <Titulo texto="Los necesitamos para agendar tu visita y para que el laboratorio identifique tu muestra.">Cuéntanos quién eres.</Titulo>
        <div className="mt-8 space-y-5">
          <Campo etiqueta="Nombre completo">
            <input autoComplete="name" value={nombre} onChange={(e) => setNombre(e.target.value)} className={claseEntrada} />
          </Campo>
          <Campo etiqueta="Número de cédula" ayuda="Solo números, sin puntos.">
            <input inputMode="numeric" value={cedula} onChange={(e) => setCedula(e.target.value.replace(/\D/g, ""))} className={claseEntrada} />
          </Campo>
          <Campo etiqueta="Celular con WhatsApp" ayuda="Ahí te avisaremos cuando estén tus resultados.">
            <div className="flex gap-2">
              <span className="rounded-2xl border border-rule bg-surface px-4 py-3.5 text-base text-ink-muted">+57</span>
              <input inputMode="tel" autoComplete="tel-national" value={celular} onChange={(e) => setCelular(e.target.value.replace(/\D/g, "").slice(0, 10))} className={claseEntrada} placeholder="300 123 4567" />
            </div>
          </Campo>
          <Campo etiqueta="Dirección para la visita en Bogotá">
            <input autoComplete="street-address" value={direccion} onChange={(e) => setDireccion(e.target.value)} className={claseEntrada} placeholder="Calle, número, apartamento" />
          </Campo>
          <Campo etiqueta="Edad">
            <input inputMode="numeric" value={edad} onChange={(e) => setEdad(e.target.value.replace(/\D/g, "").slice(0, 3))} className={`${claseEntrada} max-w-[8rem]`} />
          </Campo>
          <div>
            <span className="text-[11px] uppercase tracking-[0.16em] text-ink-faint">Sexo</span>
            <p className="mt-1 text-xs text-ink-muted">El que usa el laboratorio para comparar tus resultados.</p>
            <div className="mt-2 grid grid-cols-2 gap-3">
              <Opcion activa={sexo === "mujer"} onClick={() => setSexo("mujer")} texto="Mujer" />
              <Opcion activa={sexo === "hombre"} onClick={() => setSexo("hombre")} texto="Hombre" />
            </div>
          </div>
        </div>
      </Pantalla>
    );

  return (
    <Pantalla paso={2} total={2} etiqueta="Tus datos son privados" boton="Acepto y continúo" puedeSeguir={aceptaDatos} ocupado={ocupado} onSeguir={firmar} onAtras={() => setPaso(1)} error={error}>
      <Titulo>Antes de empezar: tus datos.</Titulo>
      <div className="mt-6 space-y-4 text-sm leading-relaxed text-ink-muted">
        <p>
          En Saludly tus datos son privados: <strong className="font-medium text-ink">solo los ve el equipo de salud de Saludly</strong> y los proveedores que necesitamos para prestarte el servicio. No los vendemos ni los usamos para publicidad.
        </p>
        <p>
          <strong className="font-medium text-ink">Qué datos.</strong> Tu nombre, cédula, edad, sexo, correo, celular y dirección. Y datos de salud: tus objetivos, peso, talla, actividad física, tus respuestas al cuestionario, las medidas que toma la enfermera y los resultados de tu laboratorio.
        </p>
        <p>
          <strong className="font-medium text-ink">Para qué.</strong> Para agendar tu visita, analizar tus resultados con las reglas clínicas de Saludly y entregarte un informe preventivo que revisa un médico. El informe no es un diagnóstico. También para contactarte si un resultado necesita atención pronta.
        </p>
        <p>
          <strong className="font-medium text-ink">Tus datos de salud son sensibles.</strong> No estás obligado a darlos, pero sin ellos no podemos preparar tu informe.
        </p>
        <p>
          <strong className="font-medium text-ink">Servidores fuera de Colombia.</strong> Usamos proveedores con servidores en Brasil, Estados Unidos y otros países (Supabase, Vercel, Google y Meta). Ellos guardan y procesan tus datos solo por cuenta de Saludly, con contrato y medidas de seguridad.
        </p>
        <p>
          <strong className="font-medium text-ink">Tus derechos.</strong> Puedes conocer, corregir y borrar tus datos, y retirar esta autorización, escribiendo a carlos@saludly.online. Lee la{" "}
          <a href="/privacidad" target="_blank" rel="noreferrer" className="text-primary underline">
            Política de tratamiento de datos
          </a>
          .
        </p>
      </div>
      <div className="mt-8 grid gap-3">
        <Opcion
          multiple
          activa={aceptaDatos}
          onClick={() => setAceptaDatos((v) => !v)}
          texto="Tengo 18 años o más y autorizo a Saludly a tratar mis datos personales y mis datos de salud para lo descrito, incluida su transmisión a servidores fuera de Colombia."
          nota="Obligatoria para crear tu informe."
        />
        <Opcion
          multiple
          activa={aceptaWhatsapp}
          onClick={() => setAceptaWhatsapp((v) => !v)}
          texto="Quiero recibir por WhatsApp el aviso de mis resultados y recomendaciones de cuidado, prevención y alimentación."
          nota="Opcional. Puedes darte de baja escribiendo «BAJA»."
        />
      </div>
    </Pantalla>
  );
}
