-- Fase 6B · La doctora también registra el peso y la cintura de su paciente (por ejemplo, en la consulta).
-- registrado_por: correo de quien lo registró si no fue la paciente (null = la paciente).
alter table public.registros_peso add column registrado_por text;

create policy "doctora registra" on public.registros_peso for insert to authenticated
  with check ((select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));
create policy "doctora corrige el registro" on public.registros_peso for update to authenticated
  using ((select public.es_doctora_de(paciente_id)) or (select public.es_equipo()))
  with check ((select public.es_doctora_de(paciente_id)) or (select public.es_equipo()));
