-- Fase 6 · Datos de los pacientes del piloto (5 primeros, con autorización firmada).
-- Identidad y salud en tablas separadas. Cada paciente solo ve y escribe lo suyo (RLS).
-- Las autorizaciones solo se agregan: son la prueba de consentimiento (Ley 1581).

create table public.pacientes (
  id uuid primary key references auth.users (id) on delete cascade,
  nombre text not null check (length(trim(nombre)) >= 3),
  cedula text not null check (cedula ~ '^[0-9]{5,12}$'),
  celular_whatsapp text not null check (celular_whatsapp ~ '^57[0-9]{10}$'),
  direccion text not null check (length(trim(direccion)) >= 5),
  edad int not null check (edad between 18 and 110),
  sexo text not null check (sexo in ('hombre', 'mujer')),
  creado timestamptz not null default now(),
  actualizado timestamptz not null default now()
);

create table public.autorizaciones (
  id bigint generated always as identity primary key,
  paciente_id uuid not null default auth.uid() references auth.users (id) on delete cascade,
  version text not null,
  acepta_datos boolean not null check (acepta_datos),
  acepta_whatsapp boolean not null,
  aceptada timestamptz not null default now(),
  agente text
);

create table public.cuestionarios (
  paciente_id uuid primary key default auth.uid() references auth.users (id) on delete cascade,
  objetivos text[] not null default '{}' check (cardinality(objetivos) <= 3),
  peso_kg numeric(5, 1) check (peso_kg between 25 and 300),
  talla_m numeric(3, 2) check (talla_m between 1.0 and 2.3),
  nivel_actividad text check (nivel_actividad in ('sedentario', 'ligero', 'moderado', 'alto')),
  toma_biotina boolean,
  alergias text[] not null default '{}',
  alergias_otras text,
  dieta text check (dieta in ('normal', 'vegetariana', 'vegana')),
  medicamentos text[] not null default '{}',
  medicamentos_otros text,
  fuma text check (fuma in ('nunca', 'antes', 'si')),
  alcohol text check (alcohol in ('no', 'ocasional', 'semanal', 'diario')),
  antecedentes text[] not null default '{}',
  embarazo text check (embarazo in ('no', 'si', 'no_se')),
  completo boolean not null default false,
  actualizado timestamptz not null default now()
);

alter table public.pacientes enable row level security;
alter table public.autorizaciones enable row level security;
alter table public.cuestionarios enable row level security;

revoke all on public.pacientes, public.autorizaciones, public.cuestionarios from anon;
revoke all on public.pacientes, public.autorizaciones, public.cuestionarios from authenticated;
grant select, insert, update on public.pacientes to authenticated;
grant select, insert on public.autorizaciones to authenticated;
grant select, insert, update on public.cuestionarios to authenticated;

create policy "paciente lee sus datos" on public.pacientes for select to authenticated using (id = (select auth.uid()));
create policy "paciente crea sus datos" on public.pacientes for insert to authenticated with check (id = (select auth.uid()));
create policy "paciente edita sus datos" on public.pacientes for update to authenticated
  using (id = (select auth.uid())) with check (id = (select auth.uid()));

create policy "paciente lee sus autorizaciones" on public.autorizaciones for select to authenticated using (paciente_id = (select auth.uid()));
create policy "paciente firma su autorización" on public.autorizaciones for insert to authenticated with check (paciente_id = (select auth.uid()));

create policy "paciente lee su cuestionario" on public.cuestionarios for select to authenticated using (paciente_id = (select auth.uid()));
create policy "paciente crea su cuestionario" on public.cuestionarios for insert to authenticated with check (paciente_id = (select auth.uid()));
create policy "paciente edita su cuestionario" on public.cuestionarios for update to authenticated
  using (paciente_id = (select auth.uid())) with check (paciente_id = (select auth.uid()));

create or replace function public.tocar_actualizado() returns trigger language plpgsql set search_path = '' as $$
begin
  new.actualizado := now();
  return new;
end;
$$;

create trigger pacientes_actualizado before update on public.pacientes for each row execute function public.tocar_actualizado();
create trigger cuestionarios_actualizado before update on public.cuestionarios for each row execute function public.tocar_actualizado();
