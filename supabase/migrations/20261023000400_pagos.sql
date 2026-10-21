-- Fase 6 · Pago por transferencia Bre-B con comprobante por WhatsApp (21 oct 2026, con Carlos).
-- configuracion: valores que Carlos edita desde el panel (llave Bre-B, valor del paquete, WhatsApp de Saludly).
-- pagos: un pago por paciente. estado: pendiente → comprobante (llegó la captura) → confirmado | rechazado.
-- Las capturas viven en el bucket privado "comprobantes"; solo el equipo las ve (con enlaces firmados).

create table public.configuracion (
  clave text primary key,
  valor text,
  actualizado timestamptz not null default now()
);
insert into public.configuracion (clave, valor) values
  ('pago_llave_breb', null),
  ('pago_valor', null),
  ('pago_titular', 'Carlos Daniel Araujo Godoy'),
  ('whatsapp_saludly', '15556767919');

create table public.pagos (
  paciente_id uuid primary key references public.pacientes (id) on delete cascade,
  codigo text not null unique default ('S-' || lpad((floor(random() * 10000))::int::text, 4, '0')),
  estado text not null default 'pendiente' check (estado in ('pendiente', 'comprobante', 'confirmado', 'rechazado')),
  comprobante text,
  comprobante_recibido timestamptz,
  confirmado timestamptz,
  confirmado_por text,
  nota text,
  creado timestamptz not null default now()
);

alter table public.configuracion enable row level security;
alter table public.pagos enable row level security;
revoke all on public.configuracion, public.pagos from anon, authenticated;
grant select on public.configuracion to authenticated;
grant update (valor, actualizado) on public.configuracion to authenticated;
grant select, insert on public.pagos to authenticated;
grant update (estado, confirmado, confirmado_por, nota) on public.pagos to authenticated;

create policy "todos leen la configuracion" on public.configuracion for select to authenticated using (true);
create policy "equipo edita la configuracion" on public.configuracion for update to authenticated using ((select public.es_equipo())) with check ((select public.es_equipo()));
create policy "paciente ve su pago" on public.pagos for select to authenticated using (paciente_id = (select auth.uid()) or (select public.es_equipo()));
create policy "paciente crea su pago" on public.pagos for insert to authenticated with check (paciente_id = (select auth.uid()) and estado = 'pendiente');
create policy "equipo confirma pagos" on public.pagos for update to authenticated using ((select public.es_equipo())) with check ((select public.es_equipo()));

insert into storage.buckets (id, name, public) values ('comprobantes', 'comprobantes', false) on conflict (id) do nothing;
create policy "equipo ve comprobantes" on storage.objects for select to authenticated using (bucket_id = 'comprobantes' and (select public.es_equipo()));

-- Cuándo salió el WhatsApp de registro completo (plantilla registro_completo), para no repetirlo.
alter table public.pagos add column aviso_registro timestamptz;
