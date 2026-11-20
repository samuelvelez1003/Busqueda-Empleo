"""Preparación de datos del Checkpoint 1 (copiada de 03_adquisicion_cruce.ipynb, secciones 6 a 8).

Se deja en un archivo aparte para que los notebooks 04 y 05 usen exactamente
el mismo pipeline sin copiar y pegar las celdas.
"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

ORDEN_EDUCACION = ["Básica o menos", "Bachiller", "Técnico", "Tecnólogo", "Universitario", "Posgrado"]
SI_NO = {"Sí": True, "No": False}

def corregir_tipos(df):
    """Corrige los tipos de dato del dataset cruzado. No cambia filas, solo tipos."""
    df = df.copy()
    df["codigo_departamento"] = df["codigo_departamento"].astype(int).astype(str).str.zfill(2)
    df["fecha_encuesta"] = pd.to_datetime(dict(year=2025, month=df["mes"], day=1))
    for col in ["estudia_actualmente", "tiene_contrato", "empleo_formal"]:
        df[col] = df[col].map(SI_NO).astype("boolean")          # boolean admite vacíos (desocupados)
    df["consiguio_empleo"] = df["consiguio_empleo"].astype(int)
    for col in ["sexo", "zona", "departamento", "ciudad", "condicion", "nivel_educativo",
                "posicion_ocupacional", "tipo_contrato", "cotiza_pension", "sector"]:
        df[col] = df[col].astype("category")
    df["nivel_educativo_grupo"] = pd.Categorical(df["nivel_educativo_grupo"], categories=ORDEN_EDUCACION, ordered=True)
    return df


def tratar_atipicos(df):
    """Aplica las decisiones de la sección 6.2 del notebook 03. Devuelve una copia con marcas y sin la fila sin educación."""
    df = df.copy()
    ingreso = df["ingreso_laboral_mensual"]
    p99 = ingreso.quantile(.99)
    df["ingreso_cero"] = ingreso.eq(0)
    df["ingreso_no_informa"] = df["condicion"].eq("Ocupado") & ingreso.isna()
    df["ingreso_atipico"] = ingreso.gt(p99)
    df["ingreso_recortado"] = ingreso.clip(upper=p99)
    df["busqueda_muy_larga"] = df["semanas_buscando"].gt(104)
    df["cotiza_pension"] = df["cotiza_pension"].replace({"Ya es pensionado": "Sí"}).astype("category")
    df = df[df["nivel_educativo_grupo"].notna()].reset_index(drop=True)
    return df


EDUCACION_A_VACANTE = {      # nivel del joven → columna del SPE con el % de vacantes que piden ese nivel
    "Básica o menos": "pct_vacantes_bachillerato",   # el SPE no separa básica; el mínimo publicado es bachillerato
    "Bachiller": "pct_vacantes_bachillerato",
    "Técnico": "pct_vacantes_tecnico_tecnologo",
    "Tecnólogo": "pct_vacantes_tecnico_tecnologo",
    "Universitario": "pct_vacantes_universitario",
    "Posgrado": "pct_vacantes_universitario",
}

def crear_variables(df):
    """Agrega las 5 variables derivadas de la sección 8.1 del notebook 03."""
    df = df.copy()
    df["formacion_practica"] = (df["nivel_educativo_grupo"].isin(["Técnico", "Tecnólogo"])
                                | df["nivel_educativo"].eq("Media técnica")).astype(int)
    columna_spe = df["nivel_educativo_grupo"].astype(str).map(EDUCACION_A_VACANTE)
    df["pct_vacantes_su_nivel"] = [df.at[i, c] for i, c in zip(df.index, columna_spe)]
    jovenes_depto = df.groupby("codigo_departamento", observed=True)["factor_expansion"].transform("sum")
    df["vacantes_sin_exp_por_1000"] = (df["vacantes_sin_experiencia_2023"] / jovenes_depto * 1000).round(2)
    df["grupo_edad"] = pd.cut(df["edad"], bins=[17, 20, 24, 28], labels=["18-20", "21-24", "25-28"])
    df["vive_en_capital"] = (df["ciudad"] != "Resto del país").astype(int)
    return df


NUMERICAS = ["pct_vacantes_su_nivel", "edad", "log_vacantes_sin_exp_por_1000", "pct_vacantes_sin_experiencia"]
ORDINAL = ["nivel_educativo_grupo"]
NOMINALES = ["sexo", "zona", "grupo_edad", "estudia_actualmente"]
BINARIAS = ["formacion_practica", "vive_en_capital"]

def construir_transformador():
    return ColumnTransformer([
        ("escalado", StandardScaler(), NUMERICAS),
        ("ordinal", OrdinalEncoder(categories=[ORDEN_EDUCACION]), ORDINAL),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False), NOMINALES),
        ("binarias", "passthrough", BINARIAS),
    ], verbose_feature_names_out=False)

def preparar_entrada(df):
    """Deja las columnas en el formato que espera el transformador."""
    entrada = df[["pct_vacantes_su_nivel", "edad", "pct_vacantes_sin_experiencia"] + ORDINAL + NOMINALES + BINARIAS].copy()
    entrada["log_vacantes_sin_exp_por_1000"] = np.log1p(df["vacantes_sin_exp_por_1000"])
    for col in NOMINALES + ORDINAL:
        entrada[col] = entrada[col].astype(str)
    return entrada


def preparar_datos(ruta_csv):
    """CSV del cruce GEIH + SPE  →  (X, y, pesos, datos_limpios, transformador). Mismo resultado en cada ejecución."""
    crudo = pd.read_csv(ruta_csv, low_memory=False)
    datos = crear_variables(tratar_atipicos(corregir_tipos(crudo)))
    pipeline = Pipeline([("transformar", construir_transformador())]).set_output(transform="pandas")
    X = pipeline.fit_transform(preparar_entrada(datos))
    y = datos["consiguio_empleo"]
    pesos = datos["factor_expansion"]
    return X, y, pesos, datos, pipeline
