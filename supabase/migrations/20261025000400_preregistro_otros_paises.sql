-- Preventa · Pre-registro desde otros países (24 oct 2026, Carlos: familiares en el exterior no podían inscribirse).
-- El celular se guarda con su indicativo y sin "+": Colombia sigue siendo 57 + 10 dígitos que empiezan por 3;
-- otros países, de 8 a 15 dígitos en total (formato internacional E.164).
alter table public.preregistros drop constraint preregistros_celular_whatsapp_check;
alter table public.preregistros add constraint preregistros_celular_whatsapp_check
  check (celular_whatsapp ~ '^573[0-9]{9}$' or (celular_whatsapp !~ '^57' and celular_whatsapp ~ '^[1-9][0-9]{7,14}$'));
