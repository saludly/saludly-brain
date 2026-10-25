-- WhatsApp · Personas con nombre de usuario (@) de WhatsApp (24 oct 2026).
-- A ellas Meta no les manda el número en el webhook (`from`), sino un identificador propio de la empresa
-- (from_user_id / contacts[].user_id, por ejemplo "CO.2548721515610901"). La primera vez se las reconoce por el código
-- del pre-registro que trae el mensaje del botón de la app; desde ahí se guarda aquí y se las reconoce siempre.
-- Los mensajes se les siguen enviando a su número del pre-registro.
alter table public.preregistros add column whatsapp_user_id text;
create unique index preregistros_whatsapp_user_id on public.preregistros (whatsapp_user_id) where whatsapp_user_id is not null;
