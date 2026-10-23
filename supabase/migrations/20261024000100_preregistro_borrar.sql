-- Preventa · El equipo elimina un pre-registro de prueba desde /medico (22 oct 2026, pedido de Carlos).
-- Borra la cuenta completa (auth.users), que arrastra el pre-registro; así el conteo vuelve a ser real.
-- No toca cuentas del equipo ni de pacientes (esas tienen datos clínicos y siguen otro camino).

create or replace function public.preregistro_borrar(p_id uuid) returns void
language plpgsql security definer set search_path = '' as $$
declare
  v_correo text;
begin
  if not public.es_equipo() then raise exception 'solo el equipo'; end if;
  if not exists (select 1 from public.preregistros where id = p_id) then raise exception 'no existe ese pre-registro'; end if;
  select lower(email) into v_correo from auth.users where id = p_id;
  if exists (select 1 from public.equipo where correo = v_correo) then raise exception 'es una cuenta del equipo'; end if;
  if exists (select 1 from public.pacientes where id = p_id) then
    -- Ya es paciente: solo se quita el pre-registro, la cuenta y sus datos clínicos se quedan.
    delete from public.preregistros where id = p_id;
  else
    delete from auth.users where id = p_id;
  end if;
end $$;
revoke all on function public.preregistro_borrar(uuid) from public, anon;
grant execute on function public.preregistro_borrar(uuid) to authenticated;
