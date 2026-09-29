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
│   ├── raw/geih_2025/        # CSV originales del DANE (4 módulos por mes, ene–dic 2025)
│   ├── processed/            # Datos limpios generados por los notebooks
│   ├── diccionario/          # Diccionario de datos oficial de la GEIH 2025
│   ├── datos_simulados_empleo_sin_experiencia.csv   # Datos de práctica (simulados)
│   └── README.md
├── notebooks/
│   ├── 01_exploracion.ipynb  # Exploración inicial (datos simulados)
│   └── 02_limpieza.ipynb     # Unión y limpieza de la GEIH 2025
├── docs/
│   └── Ficha_Proyecto_Busqueda_Empleo_Sin_Experiencia.pdf
└── README.md
```

## Fuentes de datos

| # | Fuente | Estado |
|---|---|---|
| 1 | **GEIH 2025 — DANE** (Gran Encuesta Integrada de Hogares). [Microdatos](https://microdatos.dane.gov.co/index.php/catalog/853) | Descargada y limpia |
| 2 | **Vacantes del Servicio Público de Empleo (SPE)**. [Datos abiertos](https://www.serviciodeempleo.gov.co/transparencia-e-informacion/informes-de-interes/publicacion-de-datos-abiertos/) · [DATAEMPLEO](https://dataempleo.serviciodeempleo.gov.co/dataempleo/) | Pendiente |

## Cómo ejecutar

1. Clonar el repositorio: `git clone https://github.com/samuelvelez1003/Busqueda-Empleo.git`
2. Instalar librerías: `pip install pandas numpy matplotlib jupyter`
3. Abrir los notebooks en orden desde la carpeta `notebooks/` (VS Code, Jupyter o Google Colab).

## Avance

- [x] Ficha del proyecto (`docs/`)
- [x] Estructura del repositorio
- [x] Exploración inicial con datos simulados (`01_exploracion`)
- [x] Descarga y limpieza de la GEIH 2025 (`02_limpieza`)
- [ ] Descarga de vacantes del SPE
- [ ] Análisis descriptivo con datos reales (`03_analisis_descriptivo`)
- [ ] Modelo predictivo (`04_modelo`)
