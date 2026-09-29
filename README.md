# Proyecto de Minería de Datos — Búsqueda de Empleo Sin Experiencia

## Problema

¿Qué características de los jóvenes (edad, nivel educativo, ciudad, sexo) y de los empleos (sector, tipo de contrato, formalidad) aumentan la probabilidad de que una persona **sin experiencia laboral** consiga su primer empleo en Colombia, para decidir hacia qué sectores orientar a estos jóvenes y qué formación recomendarles?

**Hipótesis inicial:** la formación técnica o tecnológica y el sector económico están relacionados con la probabilidad de conseguir el primer empleo, porque muchas vacantes de nivel de entrada (comercio, servicios, atención al cliente, logística) valoran más la formación práctica que un título universitario.

## Integrantes

- Bryan Samuel Vélez Velásquez
- Jhon Jairo Melo Largo

**Asignatura:** Minería de Datos · **Docente:** Paola Andrea Ortiz

## Estructura del repositorio

```
Busqueda-Empleo/
├── data/
│   ├── raw/
│   │   ├── geih_2025/        # Fuente 1: CSV originales del DANE (4 módulos por mes, ene–dic 2025)
│   │   └── spe/              # Fuente 2: Anexo de Demanda Laboral (vacantes) del SPE
│   ├── processed/            # Datos limpios y cruzados generados por los notebooks
│   ├── diccionario/          # Diccionario oficial GEIH + diccionario del dataset cruzado
│   ├── datos_simulados_empleo_sin_experiencia.csv   # Datos de práctica (simulados)
│   └── README.md
├── notebooks/
│   ├── 01_exploracion.ipynb  # Exploración inicial (datos simulados)
│   ├── 02_limpieza.ipynb     # Unión y limpieza de la GEIH 2025
│   └── 03_adquisicion_cruce.ipynb  # Lectura de las 2 fuentes, cruce (pd.merge) y diccionario
├── docs/
│   └── Ficha_Proyecto_Busqueda_Empleo_Sin_Experiencia.pdf
└── README.md
```

## Fuentes de datos

| # | Fuente | Estado |
|---|---|---|
| 1 | **GEIH 2025 — DANE** (Gran Encuesta Integrada de Hogares). [Microdatos](https://microdatos.dane.gov.co/index.php/catalog/853) | Descargada y limpia |
| 2 | **Vacantes del Servicio Público de Empleo (SPE)**: Anexo Estadístico de Demanda Laboral 2015–2023, hojas *Experiencia* y *Educación*. [Descarga](https://www.serviciodeempleo.gov.co/dataempleo-spe/demanda-laboral/anexo-estadistico-de-demanda-laboral-vacantes/) | Descargada y cruzada (se usa 2023, el año más reciente publicado) |

**Cruce:** `pd.merge` por `codigo_departamento` (código DIVIPOLA), relación muchos a uno (jóvenes → departamento). 85.422 filas antes y después, 33 de 33 departamentos con pareja.

## Cómo ejecutar

1. Clonar el repositorio: `git clone https://github.com/samuelvelez1003/Busqueda-Empleo.git`
2. Instalar librerías: `pip install pandas numpy matplotlib openpyxl jupyter`
3. Ejecutar los notebooks en orden desde la carpeta `notebooks/` (VS Code o Jupyter): `02_limpieza` genera `data/processed/geih2025_jovenes_18_28.csv` y `03_adquisicion_cruce` genera el dataset cruzado.

**Estado actual (Corte 1):** las dos fuentes están descargadas, limpias y cruzadas; el diccionario del dataset cruzado está en `data/diccionario/diccionario_dataset_cruzado.csv`.

## Avance

- [x] Ficha del proyecto (`docs/`)
- [x] Estructura del repositorio
- [x] Exploración inicial con datos simulados (`01_exploracion`)
- [x] Descarga y limpieza de la GEIH 2025 (`02_limpieza`)
- [x] Descarga de vacantes del SPE
- [x] Notebook de adquisición: lectura de las 2 fuentes, cruce y diccionario de datos (`03_adquisicion_cruce`)
- [ ] Análisis descriptivo con datos reales (`04_analisis_descriptivo`)
- [ ] Modelo predictivo (`05_modelo`)
