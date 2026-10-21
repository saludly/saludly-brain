-- Fase 6 · Tipo de documento y fecha de nacimiento en el registro (21 oct 2026, con Carlos).
-- El paciente elige cédula de ciudadanía (CC), cédula de extranjería (CE), PPT o pasaporte (PA)
-- y escribe su fecha de nacimiento; la edad la calcula la base, ya no la escribe el paciente.
-- La columna sigue llamándose "cedula" (la usan publicar.py y la vista del médico): guarda el número del documento.

alter table public.pacientes
  add column tipo_documento text not null default 'CC' check (tipo_documento in ('CC', 'CE', 'PPT', 'PA')),
  add column fecha_nacimiento date check (fecha_nacimiento >= date '1900-01-01');

-- CC y PPT: solo números. CE y pasaporte: letras mayúsculas y números.
alter table public.pacientes drop constraint pacientes_cedula_check;
alter table public.pacientes add constraint pacientes_cedula_check check (
  case when tipo_documento in ('CC', 'PPT') then cedula ~ '^[0-9]{5,12}$' else cedula ~ '^[A-Z0-9]{4,15}$' end
);

-- La edad sale de la fecha de nacimiento cada vez que se guardan los datos (el check de 18 a 110 años sigue).
create or replace function public.pacientes_edad() returns trigger
language plpgsql set search_path = '' as $$
begin
  if new.fecha_nacimiento is not null then
    new.edad := extract(year from age(current_date, new.fecha_nacimiento))::int;
  end if;
  return new;
end;
$$;

create trigger pacientes_edad before insert or update on public.pacientes
  for each row execute function public.pacientes_edad();
