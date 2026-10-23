-- Borra los registros de prueba antes de la preventa (22 oct 2026). NO es una migración: se corre una sola vez,
-- a mano, en el SQL Editor de Supabase. No se puede deshacer.
-- Deja la cuenta del equipo (carlosdarainfo@gmail.com) para entrar a /medico, pero sin sus datos de paciente.
-- Carlos confirmó el 22 oct 2026 que todas eran pruebas suyas y de un primo.

begin;

-- 1. Cuentas de prueba completas. El borrado arrastra pacientes, autorizaciones, cuestionarios, visitas, informes,
--    pagos, citas, enlaces del médico, mensajes de WhatsApp y pre-registros.
delete from auth.users
where email in ('saludlyco@gmail.com', 'abdujarmej@gmail.com', 'carlosdaragodoy@gmail.com', 'carlosdarabrutal@gmail.com');

-- 2. La cuenta del equipo se queda, pero sin sus datos de paciente de prueba.
delete from public.preregistros   where id         = (select id from auth.users where email = 'carlosdarainfo@gmail.com');
delete from public.informes       where paciente_id = (select id from auth.users where email = 'carlosdarainfo@gmail.com');
delete from public.visitas        where paciente_id = (select id from auth.users where email = 'carlosdarainfo@gmail.com');
delete from public.cuestionarios  where paciente_id = (select id from auth.users where email = 'carlosdarainfo@gmail.com');
delete from public.autorizaciones where paciente_id = (select id from auth.users where email = 'carlosdarainfo@gmail.com');
delete from public.pacientes      where id          = (select id from auth.users where email = 'carlosdarainfo@gmail.com');

-- 3. Revisión: todo en 0, salvo auth.users = 1 (la cuenta del equipo).
select 'auth.users' tabla, count(*) from auth.users
union all select 'pacientes', count(*) from public.pacientes
union all select 'preregistros', count(*) from public.preregistros
union all select 'informes', count(*) from public.informes
union all select 'pagos', count(*) from public.pagos
union all select 'whatsapp_mensajes', count(*) from public.whatsapp_mensajes;

commit;

-- Las capturas de comprobantes de prueba quedan en el bucket "comprobantes": se borran en Storage, en el panel de Supabase.
