# Proyecto de Minería de Datos — Búsqueda de Empleo Sin Experiencia

## Problema

¿Qué características de los jóvenes de 18 a 28 años **sin experiencia laboral** (edad, sexo, nivel educativo, si estudian actualmente y ciudad o departamento donde viven) están asociadas con una mayor probabilidad de conseguir empleo en Colombia, y cómo se relacionan con la demanda de vacantes de su departamento (porcentaje de vacantes que no exigen experiencia y nivel educativo requerido), para decidir qué formación recomendarles y hacia qué sectores y regiones orientarlos?

**Hipótesis inicial:** la formación técnica o tecnológica está relacionada con una mayor probabilidad de conseguir el primer empleo, porque muchas vacantes de nivel de entrada (comercio, servicios, atención al cliente, logística) valoran más la formación práctica que un título universitario. El sector se analiza de forma descriptiva, porque en la GEIH solo existe para quienes ya tienen empleo.

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
│   ├── 03_adquisicion_cruce.ipynb  # Lectura de las 2 fuentes, cruce, diccionario + Checkpoint 1 (secciones 6-8)
│   ├── preparacion.py        # Pipeline del Checkpoint 1 (mismas funciones del 03) para usarlo en el 04 y el 05
│   ├── 04_segmentacion_modelo_anomalias.ipynb  # Checkpoint 2: segmentación, modelo predictivo y anomalías
│   └── 05_producto_final.ipynb     # Checkpoint 3: informe final (resumen, hallazgos, documentación, ética)
├── docs/
│   ├── Ficha_Proyecto_Busqueda_Empleo_Sin_Experiencia.pdf
│   └── Informe_Final_Busqueda_Empleo.html   # El 05 exportado, para leerlo sin ejecutar nada
└── README.md
```

## Recorrido por unidades

| Unidad | Tema | Dónde está |
|---|---|---|
| 1 | Problema de negocio, datos y ciclo de minería | `docs/Ficha_Proyecto_...pdf` y este README |
| 2 | Adquisición y preparación inicial | `02_limpieza` y `03_adquisicion_cruce` (secciones 1-5) |
| 3 | Calidad, limpieza y análisis exploratorio | `01_exploracion` (práctica) y `03_adquisicion_cruce` (secciones 6-7) |
| 4 | Ingeniería de características y pipeline | `03_adquisicion_cruce` (sección 8) y `preparacion.py` |
| 5 | Segmentación | `04_segmentacion_modelo_anomalias` (sección 1) |
| 6 | Modelo predictivo y evaluación | `04_segmentacion_modelo_anomalias` (sección 2) |
| 7 | Técnica complementaria: anomalías | `04_segmentacion_modelo_anomalias` (sección 3) |
| 8 | Producto analítico y proyecto integrador | `05_producto_final` y `docs/Informe_Final_Busqueda_Empleo.html` |

## Fuentes de datos

| # | Fuente | Estado |
|---|---|---|
| 1 | **GEIH 2025 — DANE** (Gran Encuesta Integrada de Hogares). [Microdatos](https://microdatos.dane.gov.co/index.php/catalog/853) | Descargada y limpia |
| 2 | **Vacantes del Servicio Público de Empleo (SPE)**: Anexo Estadístico de Demanda Laboral 2015–2023, hojas *Experiencia*, *Educación*, *Sectores* y *Municipios*. [Descarga](https://www.serviciodeempleo.gov.co/dataempleo-spe/demanda-laboral/anexo-estadistico-de-demanda-laboral-vacantes/) | Descargada y cruzada (se usa 2023, el año más reciente publicado) |

**Cruce:** `pd.merge` por `codigo_departamento` (código DIVIPOLA), relación muchos a uno (jóvenes → departamento). 85.422 filas antes y después, 33 de 33 departamentos con pareja. Además, cada una de las 32 ciudades se compara con las vacantes de su municipio capital (hoja *Municipios*) y los sectores de la GEIH con las secciones CIIU del SPE (hoja *Sectores*).

## Cómo ejecutar

1. Clonar el repositorio: `git clone https://github.com/samuelvelez1003/Busqueda-Empleo.git`
2. Instalar librerías: `pip install pandas numpy matplotlib openpyxl scikit-learn scipy jupyter`
3. Ejecutar los notebooks en orden desde la carpeta `notebooks/` (VS Code, Jupyter o Colab): `02_limpieza` genera `data/processed/geih2025_jovenes_18_28.csv`, `03_adquisicion_cruce` genera el dataset cruzado, `04_segmentacion_modelo_anomalias` guarda segmentos, métricas y anomalías, y `05_producto_final` arma el informe.

**Checkpoint 1** (`03_adquisicion_cruce`, secciones 6-8):

- **6. Calidad de datos:** tipos corregidos (código DIVIPOLA como texto, fecha de encuesta, Sí/No a booleano, categorías ordenadas) y valores atípicos tratados con la justificación de cada decisión.
- **7. Análisis exploratorio:** estadísticas descriptivas, 5 gráficos e historia de 5 hallazgos conectados con la pregunta de negocio.
- **8. Ingeniería de características y pipeline:** 5 variables derivadas, codificación ordinal y one-hot, escalado estándar y la función `preparar_datos()` que hace todo el proceso de forma reproducible.

**Checkpoint 2** (`04_segmentacion_modelo_anomalias`):

- **Sección 1 — Segmentación:** K-means sobre los 33 departamentos (inserción y formalidad del primer empleo), k = 3 por el método del codo, comparado con jerárquico (coincide en 29 de 33) y DBSCAN (marca a San Andrés, Amazonas y Guainía como atípicos).
- **Sección 2 — Modelo predictivo:** árbol de decisión y regresión logística para `consiguio_empleo`, con train/test, clases balanceadas, revisión de fuga de datos (con fuga daba 99,8 %) y de sobreajuste. Mejor modelo: árbol de profundidad 8, AUC 0,71.
- **Sección 3 — Anomalías:** Isolation Forest sobre los recién insertados (edad, nivel educativo e ingreso), 4 configuraciones comparadas y ficha de riesgos.

**Checkpoint 3 / proyecto final** (`05_producto_final` y `docs/Informe_Final_Busqueda_Empleo.html`): resumen ejecutivo, 4 hallazgos que juntan todo el proyecto, recomendaciones, documentación del proceso y ficha de limitaciones, riesgos y ética.

## Avance

- [x] Ficha del proyecto (`docs/`)
- [x] Estructura del repositorio
- [x] Exploración inicial con datos simulados (`01_exploracion`)
- [x] Descarga y limpieza de la GEIH 2025 (`02_limpieza`)
- [x] Descarga de vacantes del SPE
- [x] Notebook de adquisición: lectura de las 2 fuentes, cruce y diccionario de datos (`03_adquisicion_cruce`)
- [x] Checkpoint 1: calidad de datos, EDA con datos reales e ingeniería de características (`03_adquisicion_cruce`, secciones 6-8)
- [x] Checkpoint 2: segmentación, modelo predictivo y anomalías (`04_segmentacion_modelo_anomalias`)
- [x] Checkpoint 3: producto final (`05_producto_final` y `docs/Informe_Final_Busqueda_Empleo.html`)
