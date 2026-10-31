-- Fase 6B · Línea GLP-1: pacientes en tratamiento para bajar de peso que llegan por su doctora (docs/07_linea_glp1/).
-- La paciente registra su tratamiento y cada semana su peso, cintura y síntomas; sube su PDF del laboratorio.
-- La doctora ve solo a sus pacientes (las que se vincularon con su código), aprueba el informe y la semana.
-- El equipo de Saludly (tabla equipo) ve todo, como en el resto de la Fase 6.

-- Doctoras aliadas. El código es lo que la paciente escribe (o trae en el enlace ?dra=) para vincularse.
create table public.doctoras (
  correo text primary key check (correo = lower(correo)),
  nombre text not null,
  codigo text not null unique check (codigo ~ '^[A-Z0-9]{3,20}$'),
  limite_semanal numeric(3, 1) not null default 1.5 check (limite_semanal between 0.5 and 5),  -- % del peso por semana (supuesto provisional)
  semanas_meseta int not null default 4 check (semanas_meseta between 2 and 12),
  creado timestamptz not null default now()
);

-- Tratamiento de la paciente: lo llena ella; queda como "dato de la paciente" hasta que la doctora lo confirma.
create table public.tratamientos_peso (
  paciente_id uuid primary key default auth.uid() references auth.users (id) on delete cascade,
  doctora_codigo text references public.doctoras (codigo),
  fecha_inicio date not null check (fecha_inicio >= date '2015-01-01'),
  peso_inicio numeric(5, 1) not null check (peso_inicio between 30 and 300),
  peso_meta numeric(5, 1) not null check (peso_meta between 30 and 300),
  cintura_inicio numeric(5, 1) check (cintura_inicio between 40 and 200),
  cintura_meta numeric(5, 1) check (cintura_meta between 40 and 200),
  talla_m numeric(3, 2) not null check (talla_m between 1.0 and 2.3),
  medicamento text check (length(medicamento) <= 80),
  dosis text check (length(dosis) <= 40),
  dia_aplicacion text check (dia_aplicacion in ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')),
  confirmado_por text,
  confirmado timestamptz,
  creado timestamptz not null default now(),
  actualizado timestamptz not null default now(),
  check (peso_meta < peso_inicio)
);

-- Registros de la paciente (uno por día; el último de la semana es el que cuenta).
create table public.registros_peso (
  id bigint generated always as identity primary key,
  paciente_id uuid not null default auth.uid() references auth.users (id) on delete cascade,
  fecha date not null default current_date,
  peso numeric(5, 1) check (peso between 30 and 300),
  cintura numeric(5, 1) check (cintura between 40 and 200),
  sintomas text[] not null default '{}',
  aplicada boolean,
  metas_cumplidas int check (metas_cumplidas between 0 and 10),
  metas_total int check (metas_total between 0 and 10),
  pregunta text check (length(pregunta) <= 300),
  creado timestamptz not null default now(),
  unique (paciente_id, fecha)
);

-- Recomendaciones de la semana: las arma codigo/informe/recomendar_peso.py (borrador) y la doctora las publica.
create table public.semanas_peso (
  id bigint generated always as identity primary key,
  paciente_id uuid not null references auth.users (id) on delete cascade,
  semana date not null,                       -- lunes de la semana
  items jsonb not null default '[]',          -- [{id, tipo, titulo, texto, por_que, fuente}]
  mensaje_doctora text check (length(mensaje_doctora) <= 600),
  estado text not null default 'borrador' check (estado in ('borrador', 'publicada')),
  revisado_por text,
  publicada timestamptz,
  creado timestamptz not null default now(),
  unique (paciente_id, semana)
);

-- Autorización: casilla aparte para mensajes comerciales (exámenes a domicilio) por WhatsApp.
alter table public.autorizaciones add column acepta_comerciales boolean not null default false;

-- ¿La sesión es de una doctora? ¿Es la doctora de esta paciente?
create or replace function public.es_doctora() returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.doctoras d where d.correo = lower((select auth.jwt()) ->> 'email'));
$$;
create or replace function public.es_doctora_de(p uuid) returns boolean
language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.tratamientos_peso t join public.doctoras d on d.codigo = t.doctora_codigo
                 where t.paciente_id = p and d.correo = lower((select auth.jwt()) ->> 'email'));
$$;
-- Nombre de la doctora a partir de su código (para que la paciente confirme a quién se vincula), sin exponer correos.
create or replace function public.doctora_por_codigo(c text) returns text
language sql stable security definer set search_path = '' as $$
  select d.nombre from public.doctoras d where d.codigo = upper(trim(c));
$$;
-- Datos de la doctora que tiene la sesión (su nombre, código y límites).
create or replace function public.mi_doctora() returns table (nombre text, codigo text, limite_semanal numeric, semanas_meseta int)
language sql stable security definer set search_path = '' as $$
  select d.nombre, d.codigo, d.limite_semanal, d.semanas_meseta from public.doctoras d where d.correo = lower((select auth.jwt()) ->> 'email');
$$;
revoke all on function public.es_doctora(), public.es_doctora_de(uuid), public.doctora_por_codigo(text), public.mi_doctora() from public, anon;
grant execute on function public.es_doctora(), public.es_doctora_de(uuid), public.doctora_por_codigo(text), public.mi_doctora() to authenticated;

alter table public.doctoras enable row level security;
alter table public.tratamientos_peso enable row level security;
alter table public.registros_peso enable row level security;
alter table public.semanas_peso enable row level security;

revoke all on public.doctoras, public.tratamientos_peso, public.registros_peso, public.semanas_peso from anon, authenticated;
grant select on public.doctoras to authenticated;
grant select, insert, update on public.tratamientos_peso to authenticated;
grant select, insert, update on public.registros_peso to authenticated;
grant select, update on public.semanas_peso to authenticated;

create policy "equipo ve doctoras" on public.doctoras for select to authenticated using ((select public.es_equipo()));

-- Tratamiento: la paciente el suyo; la doctora y el equipo lo leen y lo confirman.
create policy "paciente lee su tratamiento" on public.tratamientos_peso for select to authenticated
  using (paciente_id = (select auth.uid()) or (select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));
create policy "paciente crea su tratamiento" on public.tratamientos_peso for insert to authenticated with check (paciente_id = (select auth.uid()));
create policy "paciente o doctora editan el tratamiento" on public.tratamientos_peso for update to authenticated
  using (paciente_id = (select auth.uid()) or (select public.es_doctora_de(paciente_id)) or (select public.es_equipo()))
  with check (paciente_id = (select auth.uid()) or (select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));

-- Registros: los escribe la paciente; la doctora y el equipo los leen.
create policy "paciente lee sus registros" on public.registros_peso for select to authenticated
  using (paciente_id = (select auth.uid()) or (select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));
create policy "paciente registra" on public.registros_peso for insert to authenticated with check (paciente_id = (select auth.uid()));
create policy "paciente corrige su registro" on public.registros_peso for update to authenticated
  using (paciente_id = (select auth.uid())) with check (paciente_id = (select auth.uid()));

-- Semanas: la paciente solo ve las publicadas; la doctora y el equipo editan y publican.
create policy "paciente lee su semana publicada" on public.semanas_peso for select to authenticated
  using ((paciente_id = (select auth.uid()) and estado = 'publicada') or (select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));
create policy "doctora publica la semana" on public.semanas_peso for update to authenticated
  using ((select public.es_doctora_de(paciente_id)) or (select public.es_equipo()))
  with check ((select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));

-- La doctora lee los datos y aprueba los informes de sus pacientes (el equipo ya podía).
create policy "doctora lee sus pacientes" on public.pacientes for select to authenticated using ((select public.es_doctora_de(id)));
create policy "doctora lee cuestionarios" on public.cuestionarios for select to authenticated using ((select public.es_doctora_de(paciente_id)));
create policy "doctora lee informes" on public.informes for select to authenticated using ((select public.es_doctora_de(paciente_id)));
create policy "doctora aprueba informes" on public.informes for update to authenticated
  using ((select public.es_doctora_de(paciente_id))) with check ((select public.es_doctora_de(paciente_id)));
