-- Saludly Brain · RAG · Defensa en profundidad
-- Además de RLS sin políticas, las llaves públicas (anon, authenticated) no tienen ningún permiso sobre la tabla.
revoke all on table kb_fragmentos from anon, authenticated;
