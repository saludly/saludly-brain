-- Preventa · Los menores de edad también pueden pre-registrarse (Carlos, 24 oct 2026).
-- Antes la fecha de nacimiento exigía 18 años o más; ahora solo que no sea futura.
-- Los términos de la app les piden confirmar que su mamá, papá o acudiente está de acuerdo.

alter table public.preregistros drop constraint preregistros_fecha_nacimiento_check;
alter table public.preregistros add constraint preregistros_fecha_nacimiento_check
  check (fecha_nacimiento between '1900-01-01' and current_date);
