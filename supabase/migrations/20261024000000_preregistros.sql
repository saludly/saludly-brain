-- Preventa · Pre-registro gratis con semana de prueba por WhatsApp (22 oct 2026, con Carlos).
-- Separado de pacientes: no pide documento ni dirección ni datos clínicos, y no toca el flujo de los clientes.
-- Cada persona ve y edita lo suyo; el equipo ve a todos y cambia el estado con preregistro_estado().
-- fuente: el ?ref= con el que llegó (primer clic). referido_por: el código del amigo que lo invitó.

create table public.preregistros (
  id uuid primary key default auth.uid() references auth.users (id) on delete cascade,
  nombre text not null check (length(trim(nombre)) >= 3),
  correo text,
  celular_whatsapp text not null check (celular_whatsapp ~ '^57[0-9]{10}$'),
  fecha_nacimiento date not null check (fecha_nacimiento between '1900-01-01' and current_date - interval '18 years'),
  sexo text check (sexo in ('hombre', 'mujer')),
  localidad text not null check (length(localidad) between 2 and 60),
  objetivos text[] not null check (cardinality(objetivos) between 1 and 3),
  objetivo_otro text check (length(objetivo_otro) <= 200),
  alergias text[] not null default '{}',
  dieta text check (dieta in ('normal', 'vegetariana', 'vegana')),
  quiere_prueba boolean not null default true,
  acepta_datos boolean not null check (acepta_datos),
  acepta_contacto boolean not null default false,
  version_autorizacion text not null,
  agente text,
  fuente text check (fuente ~ '^[a-z0-9_-]{1,60}$'),
  referido_por text check (referido_por ~ '^[a-z0-9]{6}$'),
  codigo text not null unique default substr(md5(gen_random_uuid()::text), 1, 6),
  estado text not null default 'registrado' check (estado in ('registrado', 'cliente', 'baja')),
  -- Los llena el flujo de WhatsApp (semana de prueba y anticipo).
  prueba_inicio timestamptz,
  prueba_dia int not null default 0,
  anticipo_estado text check (anticipo_estado in ('pedido', 'pagado', 'devuelto')),
  creado timestamptz not null default now(),
  actualizado timestamptz not null default now()
);

create index preregistros_creado on public.preregistros (creado);

alter table public.preregistros enable row level security;
revoke all on public.preregistros from anon, authenticated;
grant select, insert on public.preregistros to authenticated;
grant update (nombre, celular_whatsapp, fecha_nacimiento, sexo, localidad, objetivos, objetivo_otro, alergias, dieta, quiere_prueba, acepta_contacto, actualizado)
  on public.preregistros to authenticated;

create policy "persona o equipo ven el preregistro" on public.preregistros for select to authenticated
  using (id = (select auth.uid()) or (select public.es_equipo()));
create policy "persona crea su preregistro" on public.preregistros for insert to authenticated
  with check (id = (select auth.uid()) and estado = 'registrado' and prueba_dia = 0 and prueba_inicio is null and anticipo_estado is null);
create policy "persona edita su preregistro" on public.preregistros for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));

-- El equipo pasa a alguien a cliente (sigue el flujo completo con pago) o lo marca de baja.
create or replace function public.preregistro_estado(p_id uuid, p_estado text) returns void
language plpgsql security definer set search_path = '' as $$
begin
  if not public.es_equipo() then raise exception 'solo el equipo'; end if;
  if p_estado not in ('registrado', 'cliente', 'baja') then raise exception 'estado inválido'; end if;
  update public.preregistros set estado = p_estado, actualizado = now() where id = p_id;
end $$;
revoke all on function public.preregistro_estado(uuid, text) from public, anon;
grant execute on function public.preregistro_estado(uuid, text) to authenticated;

-- preventa = 'si': quien no es paciente ni cliente hace el pre-registro en vez del registro completo.
insert into public.configuracion (clave, valor) values ('preventa', 'si'), ('anticipo_valor', null)
  on conflict (clave) do nothing;
