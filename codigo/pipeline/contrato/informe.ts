/**
 * Saludly Brain · Contrato del informe para el dashboard (PWA)
 *
 * Lo produce `codigo/pipeline/saludly.py` (documento 10.5, ampliado el 10 de octubre de 2026).
 * Ejemplos reales con datos sintéticos: `codigo/pipeline/ejemplos/INF-*.json`.
 * Se puede copiar tal cual al repositorio del dashboard (por ejemplo, src/data/informe.ts).
 */

/** Clase de un resultado. "critico" solo con bandera del laboratorio o umbral de guía; nunca "óptimo". */
export type Clase = "en_rango" | "bajo" | "alto" | "limitrofe" | "critico" | "alterado" | "no_interpretable" | null;

/** 0 nada · 1 próximo control (3 meses) · 2 consulta en 2 a 4 semanas · 3 llamada del equipo médico el mismo día */
export type Escalamiento = 0 | 1 | 2 | 3;

export type EstadoInforme = "en_revision" | "requiere_revision" | "retenido_hasta_llamada";

export type ObjetivoId =
  | "salud_general" | "prevenir" | "condicion_existente" | "bajar_peso" | "masa_muscular"
  | "rendimiento" | "maraton" | "atletico" | "energia_sueno" | "envejecer_saludable";

export type TipoRecomendacion =
  | "alimentacion" | "hidratacion" | "actividad" | "sueno" | "habitos"
  | "actividades_saludables" | "vitaminas_suplementos" | "terapias" | "controles";

export interface Hallazgo {
  hallazgo_id: string;            // H-xxxxxx-01
  referencia: string;             // COND-…, REL-… o SEG-…
  tipo: "condicion" | "patron" | "patron_propio" | "seguridad";
  titulo: string;                 // en idioma paciente, sin diagnóstico
  escalamiento: Escalamiento;
  nivel_lenguaje: string | null;  // "Resultado observado", "Patrón compatible", "Riesgo potencial", "Requiere evaluación médica"
  coincidencia: "alta" | "moderada" | "baja" | null;
  que_es: string;
  por_que: string[];              // frases con los valores reales del paciente
  ejemplo: string;                // analogía cotidiana
  agrupa: { referencia: string; titulo: string | null }[];  // condiciones que un patrón agrupa
}

export interface Recomendacion {
  recomendacion_id: string;       // REC-ALI-101…
  tipo: TipoRecomendacion;
  titulo: string;
  texto: string;
  meta: string | null;            // acción medible para esta semana
  por_que: string | null;
  hallazgos: string[];            // a qué hallazgos responde
  objetivos: ObjetivoId[];        // qué metas del paciente atiende
  requiere_consulta_previa: boolean;
}

export interface Resultado {
  biomarker_id: string;
  nombre: string;
  valor: number | string | null;
  valor_original: string | null;
  unidad: string | null;
  intervalo: string | null;       // texto del laboratorio, por ejemplo "13,5 – 17,5"
  clase: Clase;
  estado: string;                 // medido | menor_que_limite | mayor_que_limite | cualitativo | invalido | no_medido
  motivo: string | null;          // por qué no se interpreta
  seccion: string | null;
  refleja: boolean;
}

export interface Nutrientes {
  kcal: number; proteina_g: number; grasa_g: number; grasa_saturada_g: number; carbohidratos_g: number;
  fibra_g: number; azucares_g: number; sodio_mg: number; potasio_mg: number; hierro_mg: number; calcio_mg: number;
}

export interface Informe {
  informe_id: string;
  paciente_ref: string;           // seudónimo P-XXXXXXXX; nunca nombre ni documento
  orden: string;
  fecha_toma: string | null;      // AAAA-MM-DD
  generado: string;
  estado: EstadoInforme;          // retenido_hasta_llamada: no mostrar nada hasta que el médico llame
  panel: "solo_sangre" | "completo";
  escalamiento_maximo: Escalamiento;
  canal: string;
  objetivos: { id: ObjetivoId; nombre: string }[];
  perfil: {
    edad: number | null; sexo: "hombre" | "mujer" | null; ciudad: string; toma_biotina: boolean | null;
    nivel_actividad: string;
    medidas_enfermera: Partial<Record<"presion_sistolica" | "presion_diastolica" | "cintura_cm" | "peso_kg" | "talla_m", number>>;
  };
  wearable: { activo: boolean };
  paciente: {
    resumen: string;
    lo_que_esta_bien: { grupo: string; nombre: string | null; texto: string }[];
    lo_que_merece_atencion: Hallazgo[];
    que_podria_significar: { hallazgo_id: string; texto: string; incertidumbre: string }[];
    que_puedes_hacer: Recomendacion[];
    cuando_consultar: { escalamiento: Escalamiento; texto: string; hallazgos: { hallazgo_id: string; titulo: string; detalle: string | null }[] }[];
    informativos: { referencia: string; titulo: string; que_es: string; por_que: string[]; texto: string }[];
  };
  resultados: Resultado[];
  edad_biologica: { phenoage: number; diferencia: number; nota: string | null } | null;
  recordatorios: string[];
  nutricion: {
    meta_diaria: { personalizada: boolean; kcal?: number; proteina_g?: number; grasa_g?: number; grasa_saturada_g_max?: number;
                   carbohidratos_g?: number; fibra_g_min: number; sodio_mg_max: number; azucar_anadida_g_max: number | null;
                   formula?: string; motivo?: string; notas: string[] };
    restricciones: { exigir: string[]; excluir: string[]; preferir: string[]; motivos: string[] };
    recetas_aptas: number;
    recetas_total: number;
    plan: { dia: number; receta_id: string; nombre: string; tiempo_comida: "desayuno" | "almuerzo" | "cena" | "merienda";
            porciones: number; tiempo_min: number | null; nutrientes_porcion: Nutrientes; etiquetas: string[] }[];
  };
  whatsapp: {
    resultado_listo: string | null;
    recordatorio_consulta: string | null;
    recomendaciones_semanales: { semana: number; recomendacion_id: string; texto: string }[];
    recetas_diarias: { dia: number; receta_id: string; texto: string }[];
  };
  /** Solo para la vista del médico (rol médico). No mostrar al paciente. */
  medico: Record<string, unknown>;
  control_salida: { ok: boolean; problemas: { ubicacion: string; regla: string; motivo: string; fragmento: string }[]; hallazgos_sin_texto: string[] };
  trazabilidad: { sha256_pdf: string; version_kb: string; version_redaccion: string; version_modelo: string | null; calculados: Record<string, number | null> };
}
