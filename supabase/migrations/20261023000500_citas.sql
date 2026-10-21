-- Fase 6 · Agenda de la visita desde la PWA con el Google Calendar de saludlyco@gmail.com (21 oct 2026, con Carlos).
-- secretos: llaves que solo usan las funciones (la llave de servicio); hoy, el refresh token del calendario.
-- citas: una visita activa por paciente; una visita por día (lunes a viernes, de 7 a 11 a. m., hora de Bogotá).
create table public.secretos (
  clave text primary key,
  valor text not null,
  actualizado timestamptz not null default now()
);
alter table public.secretos enable row level security;
revoke all on public.secretos from anon, authenticated;

create table public.citas (
  id bigint generated always as identity primary key,
  paciente_id uuid not null references public.pacientes (id) on delete cascade,
  inicio timestamptz not null,
  dia date not null,
  evento_id text,
  estado text not null default 'agendada' check (estado in ('agendada', 'cancelada', 'hecha')),
  creado timestamptz not null default now()
);
create unique index citas_una_por_dia on public.citas (dia) where estado = 'agendada';
create unique index citas_una_por_paciente on public.citas (paciente_id) where estado = 'agendada';

alter table public.citas enable row level security;
revoke all on public.citas from anon, authenticated;
grant select on public.citas to authenticated;
create policy "paciente ve su cita" on public.citas for select to authenticated using (paciente_id = (select auth.uid()) or (select public.es_equipo()));
