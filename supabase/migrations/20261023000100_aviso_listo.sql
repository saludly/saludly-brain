-- Fase 6 · Aviso por WhatsApp al terminar el cuestionario, para agendar la visita (21 oct 2026, con Carlos).
-- Lo envía la función avisar-listo (supabase/functions) una sola vez y marca la hora aquí.
alter table public.cuestionarios add column aviso_listo timestamptz;
