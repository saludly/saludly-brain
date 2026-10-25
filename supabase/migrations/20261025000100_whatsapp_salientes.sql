-- WhatsApp · También se guarda lo que envía Saludly (24 oct 2026), para ver cada conversación como un chat en /medico.
-- direccion: 'entrante' (lo que escribe la persona) o 'saliente' (lo que manda el bot o una plantilla).
-- En los salientes, opcion dice el tipo (texto, botones, plantilla) y si Meta lo rechazó (fallo).
alter table public.whatsapp_mensajes
  add column direccion text not null default 'entrante' check (direccion in ('entrante', 'saliente'));
create index whatsapp_mensajes_chat on public.whatsapp_mensajes (celular, recibido);
