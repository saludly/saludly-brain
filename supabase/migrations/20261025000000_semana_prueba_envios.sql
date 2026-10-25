-- Preventa · Programador de la semana de prueba por WhatsApp (24 oct 2026, con Carlos).
-- Cuando una persona del pre-registro escribe "hola" (o toca "Empezar mi semana"), el webhook arma sus 7 días con
-- _compartido/semana.ts y los guarda aquí, cada uno con su hora. La función semana-programador corre cada 5 minutos
-- (pg_cron) y manda lo que ya toca:
--   - si la persona escribió o tocó un botón en las últimas 24 horas, el mensaje tal cual (con sus botones);
--   - si no, una plantilla (recordatorio_dia, o cierre_semana el día 7), máximo una al día, y el envío queda
--     "esperando" hasta que responda; entonces el webhook le entrega lo pendiente.
-- Un día después del pre-registro, si todavía no escribió, le llega la plantilla bienvenida_semana (una sola vez).
-- Solo el servicio (las funciones) escribe; el equipo lee desde el panel.

alter table public.preregistros
  add column ultimo_mensaje timestamptz,      -- último mensaje o toque de la persona: abre la ventana de 24 horas
  add column ultima_plantilla date,           -- fecha (Bogotá) de la última plantilla enviada: máximo una al día
  add column bienvenida_enviada timestamptz;  -- plantilla bienvenida_semana

create table public.semana_envios (
  id bigint generated always as identity primary key,
  preregistro_id uuid not null references public.preregistros (id) on delete cascade,
  dia int not null check (dia between 1 and 7),
  orden int not null,
  envio text not null check (envio in ('manana', 'receta', 'cortisol', 'examen', 'tarde')),
  programado timestamptz not null,
  texto text not null,
  botones text[] not null default '{}',
  resumen text not null,                      -- {{2}} de recordatorio_dia si la ventana está cerrada
  estado text not null default 'pendiente' check (estado in ('pendiente', 'enviando', 'esperando', 'enviado', 'error', 'cancelado')),
  enviado timestamptz,
  unique (preregistro_id, dia, orden)
);
create index semana_envios_por_enviar on public.semana_envios (programado) where estado in ('pendiente', 'esperando');

-- Lo que responde cada persona con los botones: para saber quién quiere el estudio (interes) y quién pidió su cupo.
create table public.semana_respuestas (
  id bigint generated always as identity primary key,
  preregistro_id uuid not null references public.preregistros (id) on delete cascade,
  dia int not null,
  boton text not null,
  interes boolean not null default false,
  recibido timestamptz not null default now()
);
create index semana_respuestas_persona on public.semana_respuestas (preregistro_id);

alter table public.semana_envios enable row level security;
alter table public.semana_respuestas enable row level security;
revoke all on public.semana_envios, public.semana_respuestas from anon, authenticated;
grant select on public.semana_envios, public.semana_respuestas to authenticated;
create policy "equipo lee los envíos" on public.semana_envios for select to authenticated using ((select public.es_equipo()));
create policy "equipo lee las respuestas" on public.semana_respuestas for select to authenticated using ((select public.es_equipo()));

-- Lo que escriben las personas del pre-registro también queda en whatsapp_mensajes (sin paciente).
alter table public.whatsapp_mensajes add column preregistro_id uuid references public.preregistros (id) on delete cascade;

-- El botón de WhatsApp de la app (pre-registro y pago) pasa al número real de Saludly (+57 301 130 7944, desde el 24 oct 2026).
update public.configuracion set valor = '573011307944' where clave = 'whatsapp_saludly';

-- Reloj: cada 5 minutos llama a semana-programador con una llave propia guardada en Vault (no la del servicio).
-- Antes de aplicar: select vault.create_secret('<llave>', 'semana_cron'); y el mismo valor en el secreto
-- SEMANA_CRON_SECRET de las funciones.
create extension if not exists pg_cron;
create extension if not exists pg_net;
select cron.schedule('semana-programador', '*/5 * * * *', $$
  select net.http_post(
    url := 'https://hyzpxmtatchgklfbipnk.supabase.co/functions/v1/semana-programador',
    headers := jsonb_build_object('Content-Type', 'application/json',
      'x-semana-cron', (select decrypted_secret from vault.decrypted_secrets where name = 'semana_cron')),
    body := '{}'::jsonb, timeout_milliseconds := 55000)
$$);
