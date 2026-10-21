-- Fase 6 · WhatsApp: BAJA del paciente y registro de los mensajes que llegan (21 oct 2026).
-- whatsapp_baja: si el paciente escribió BAJA, no se le envía nada más (las funciones lo revisan). ALTA lo quita.
-- whatsapp_mensajes: lo que escriben los pacientes, para que el equipo lo vea y le responda una persona si pide la opción 3.
alter table public.pacientes add column whatsapp_baja timestamptz;

create table public.whatsapp_mensajes (
  id bigint generated always as identity primary key,
  paciente_id uuid references public.pacientes (id) on delete cascade,
  celular text not null,
  texto text,
  opcion text,
  recibido timestamptz not null default now()
);

alter table public.whatsapp_mensajes enable row level security;
revoke all on public.whatsapp_mensajes from anon, authenticated;
grant select on public.whatsapp_mensajes to authenticated;
create policy "equipo lee los mensajes" on public.whatsapp_mensajes for select to authenticated using ((select public.es_equipo()));
