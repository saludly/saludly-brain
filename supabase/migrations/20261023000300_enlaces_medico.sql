-- Fase 6 · Enlace "muéstrale esto a tu médico" (21 oct 2026, con Carlos).
-- Al aprobar el informe se crea un enlace app.saludly.online/m/<nombre>-<últimos 4 del documento>-<código>, y se envía al
-- paciente por WhatsApp. El médico lo abre sin cuenta. El código aleatorio evita que se pueda adivinar (Ley 1581).
-- Solo la función vista-medico (llave de servicio) lee el informe a partir del enlace; el paciente ve su propio enlace.
create table public.enlaces_medico (
  slug text primary key check (slug ~ '^[a-z0-9-]{8,80}$'),
  paciente_id uuid not null references public.pacientes (id) on delete cascade,
  informe_id bigint not null references public.informes (id) on delete cascade,
  creado timestamptz not null default now(),
  revocado timestamptz
);
create unique index enlaces_medico_un_informe on public.enlaces_medico (informe_id) where revocado is null;

alter table public.enlaces_medico enable row level security;
revoke all on public.enlaces_medico from anon, authenticated;
grant select on public.enlaces_medico to authenticated;
create policy "paciente ve su enlace" on public.enlaces_medico for select to authenticated using (paciente_id = (select auth.uid()));
create policy "equipo ve los enlaces" on public.enlaces_medico for select to authenticated using ((select public.es_equipo()));
