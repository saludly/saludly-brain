-- WhatsApp · Conversaciones en vivo en /medico (24 oct 2026).
-- Los mensajes de la semana que ya se enviaron antes de guardar los salientes pasan a whatsapp_mensajes.
-- (Las respuestas del bot anteriores a las 8:38 p. m. del 24 oct no quedaron guardadas en ningún lado.)
insert into public.whatsapp_mensajes (preregistro_id, celular, texto, opcion, direccion, recibido)
select e.preregistro_id, p.celular_whatsapp,
       case when cardinality(e.botones) > 0 then e.texto || E'\n[' || array_to_string(e.botones, ' | ') || ']' else e.texto end,
       case when cardinality(e.botones) > 0 then 'botones' else 'texto' end, 'saliente', e.enviado
from public.semana_envios e join public.preregistros p on p.id = e.preregistro_id
where e.estado = 'enviado' and e.enviado is not null;

-- En vivo: el panel recibe cada mensaje nuevo al instante (Realtime respeta la política "equipo lee los mensajes").
alter publication supabase_realtime add table public.whatsapp_mensajes;
