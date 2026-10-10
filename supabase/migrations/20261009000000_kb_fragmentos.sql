-- Saludly Brain · RAG · Esquema en Supabase
-- Solo Knowledge Base: aquí NUNCA van datos de pacientes.
-- La dimensión 1024 corresponde a bge-m3 (codigo/rag/vectorizar.py). Si se cambia de modelo, cambia aquí y se vectoriza todo.

create extension if not exists vector;

create table if not exists kb_fragmentos (
  id          text primary key,             -- "ferritin#03", "COND-M3-HE-002#00"
  fuente_id   text not null,                -- ficha o documento de origen
  tipo        text not null,                -- biomarcador | condicion | relacion | seguridad | documento_producto | evidencia
  orden       int  not null,
  titulo      text not null,
  contenido   text not null,
  tokens      int,
  huella      text not null,                -- sha256 del contenido: permite cargas incrementales
  ruta        text,
  metadata    jsonb not null default '{}'::jsonb,
  version_kb  text,
  modelo      text not null,
  embedding   vector(1024) not null,
  fts         tsvector generated always as (to_tsvector('spanish', titulo || ' ' || contenido)) stored,
  actualizado timestamptz not null default now()
);

create index if not exists kb_fragmentos_embedding on kb_fragmentos using hnsw (embedding vector_cosine_ops);
create index if not exists kb_fragmentos_fts on kb_fragmentos using gin (fts);
create index if not exists kb_fragmentos_fuente on kb_fragmentos (fuente_id, orden);
create index if not exists kb_fragmentos_tipo on kb_fragmentos (tipo);
create index if not exists kb_fragmentos_metadata on kb_fragmentos using gin (metadata);

-- Seguridad: RLS activo y sin políticas públicas. Solo el servidor (service_role) lee y escribe.
alter table kb_fragmentos enable row level security;

-- 1) Traer fichas exactas por identificador (para redactar: lo que nombran los hallazgos del motor)
create or replace function traer_fichas(ids text[])
returns setof kb_fragmentos
language sql stable
set search_path = public
as $$
  select * from kb_fragmentos where fuente_id = any(ids) order by fuente_id, orden;
$$;

-- 2) Búsqueda híbrida (significado + palabras) con fusión por rangos recíprocos (RRF)
create or replace function buscar_kb(
  consulta_texto  text,
  consulta_vector vector(1024),
  n               int     default 8,
  tipos           text[]  default null,   -- filtrar por tipo de fragmento
  fuentes         text[]  default null,   -- limitar a ciertas fichas
  peso_semantico  float   default 1.0,
  peso_palabras   float   default 1.0,
  k_rrf           int     default 50
)
returns table (id text, fuente_id text, tipo text, titulo text, contenido text, metadata jsonb, puntaje float)
language sql stable
set search_path = public
as $$
  with candidatos as (
    select * from kb_fragmentos f
    where (tipos is null or f.tipo = any(tipos)) and (fuentes is null or f.fuente_id = any(fuentes))
  ),
  semantica as (
    select c.id, row_number() over (order by c.embedding <=> consulta_vector) as rango
    from candidatos c order by c.embedding <=> consulta_vector limit n * 4
  ),
  palabras as (
    select c.id, row_number() over (order by ts_rank_cd(c.fts, q) desc) as rango
    from candidatos c, websearch_to_tsquery('spanish', consulta_texto) q
    where c.fts @@ q
    order by ts_rank_cd(c.fts, q) desc limit n * 4
  )
  select c.id, c.fuente_id, c.tipo, c.titulo, c.contenido, c.metadata,
         coalesce(peso_semantico / (k_rrf + s.rango), 0) + coalesce(peso_palabras / (k_rrf + p.rango), 0) as puntaje
  from semantica s
  full outer join palabras p on p.id = s.id
  join candidatos c on c.id = coalesce(s.id, p.id)
  order by puntaje desc
  limit n;
$$;

revoke execute on function traer_fichas(text[]) from public, anon, authenticated;
revoke execute on function buscar_kb(text, vector, int, text[], text[], float, float, int) from public, anon, authenticated;
