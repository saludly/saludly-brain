-- Fase 6 · Visita de la enfermera, informes y equipo (médico revisor y administración).
-- El paciente ve su informe solo cuando el médico lo aprueba. El equipo ve y revisa todo.
-- Los informes los crea codigo/pipeline/publicar.py con la llave de servicio (nunca el navegador).

create table public.equipo (
  correo text primary key,
  rol text not null check (rol in ('medico', 'admin')),
  nombre text
);

insert into public.equipo (correo, rol, nombre) values ('carlosdarainfo@gmail.com', 'medico', 'Carlos');

-- ¿La sesión actual es del equipo? (security definer para no exponer la tabla equipo)
create or replace function public.es_equipo() returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.equipo e where e.correo = lower((select auth.jwt()) ->> 'email'));
$$;
revoke all on function public.es_equipo() from public, anon;
grant execute on function public.es_equipo() to authenticated;

create table public.visitas (
  paciente_id uuid primary key default auth.uid() references auth.users (id) on delete cascade,
  presion_sistolica int check (presion_sistolica between 60 and 260),
  presion_diastolica int check (presion_diastolica between 30 and 160),
  cintura_cm numeric(5, 1) check (cintura_cm between 40 and 200),
  cadera_cm numeric(5, 1) check (cadera_cm between 40 and 220),
  peso_kg numeric(5, 1) check (peso_kg between 25 and 300),
  talla_m numeric(3, 2) check (talla_m between 1.0 and 2.3),
  enfermera text,
  tomada timestamptz not null default now()
);

create table public.informes (
  id bigint generated always as identity primary key,
  paciente_id uuid not null references auth.users (id) on delete cascade,
  orden text not null,
  informe jsonb not null,
  estado text not null default 'en_revision' check (estado in ('en_revision', 'aprobado', 'retenido')),
  creado timestamptz not null default now(),
  aprobado timestamptz,
  aprobado_por text,
  avisado timestamptz,
  unique (paciente_id, orden)
);

alter table public.equipo enable row level security;
alter table public.visitas enable row level security;
alter table public.informes enable row level security;

revoke all on public.equipo, public.visitas, public.informes from anon, authenticated;
grant select, insert, update on public.visitas to authenticated;
grant select, update on public.informes to authenticated;

-- Visita: la llena la enfermera desde el celular del paciente (sesión del paciente).
create policy "paciente lee su visita" on public.visitas for select to authenticated using (paciente_id = (select auth.uid()) or (select public.es_equipo()));
create policy "paciente registra su visita" on public.visitas for insert to authenticated with check (paciente_id = (select auth.uid()));
create policy "paciente corrige su visita" on public.visitas for update to authenticated
  using (paciente_id = (select auth.uid())) with check (paciente_id = (select auth.uid()));

-- Informes: el paciente solo ve el suyo aprobado; el equipo ve todos y los aprueba.
create policy "paciente lee su informe aprobado" on public.informes for select to authenticated
  using ((paciente_id = (select auth.uid()) and estado = 'aprobado') or (select public.es_equipo()));
create policy "equipo revisa informes" on public.informes for update to authenticated
  using ((select public.es_equipo())) with check ((select public.es_equipo()));

-- El equipo también lee los datos de los pacientes para revisar.
create policy "equipo lee pacientes" on public.pacientes for select to authenticated using ((select public.es_equipo()));
create policy "equipo lee cuestionarios" on public.cuestionarios for select to authenticated using ((select public.es_equipo()));
create policy "equipo lee autorizaciones" on public.autorizaciones for select to authenticated using ((select public.es_equipo()));
