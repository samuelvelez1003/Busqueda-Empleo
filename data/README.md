# data/ — Datos del proyecto

## Contenido

| Ruta | Descripción |
|---|---|
| `raw/geih_2025/MM_mes/` | CSV **originales** de la GEIH 2025 del DANE (enero a diciembre). Solo se guardan los 4 módulos que usa el proyecto. **No se modifican.** |
| `raw/spe/11-Anexo-Demanda-Laboral-Ano-2023.xlsx` | Archivo **original** del SPE: vacantes registradas por mes y departamento según experiencia, nivel educativo, sector, etc. (2015–2023). Se usan las hojas *Experiencia* y *Educación*, año 2023. |
| `processed/geih2025_jovenes_18_28.csv` | Jóvenes de 18 a 28 años en la fuerza de trabajo (ocupados y desocupados), con variables traducidas y la variable objetivo. Lo genera `notebooks/02_limpieza.ipynb`. |
| `processed/dataset_cruzado_sin_experiencia.csv` | Jóvenes sin experiencia (41.785) con variables de la GEIH + indicadores de vacantes del SPE de su departamento. Lo genera `notebooks/03_adquisicion_cruce.ipynb`. |
| `processed/resumen_departamentos_geih_spe.csv` | Una fila por departamento (33) con indicadores de ambas fuentes. |
| `diccionario/diccionario_dataset_cruzado.csv` | Diccionario del dataset cruzado: columna, tipo, significado, fuente y variable original. |
| `diccionario/diccionario_datos_geih_2025.xlsx` | Diccionario de datos oficial del DANE: significado y códigos de cada variable. |
| `datos_simulados_empleo_sin_experiencia.csv` | Base **simulada** (`fuente = SIMULADO`) usada solo para practicar en `01_exploracion.ipynb`. No es información real. |

## Módulos de la GEIH usados (por mes)

| Archivo | Módulo del DANE | Variables principales |
|---|---|---|
| `caracteristicas_generales.csv` | Características generales, seguridad social en salud y educación | `P6040` edad, `P3271` sexo, `P3042` nivel educativo, `P6170` estudia, `AREA` ciudad, `DPTO`, `CLASE`, `FEX_C18` factor de expansión |
| `fuerza_de_trabajo.csv` | Fuerza de trabajo | `FT`, `FFT` |
| `ocupados.csv` | Ocupados | `P6426` meses en el empleo, `P6430` posición, `P6440` contrato, `P6460` tipo de contrato, `P6920` pensión, `INGLABO` ingreso, `RAMA2D_R4` sector |
| `no_ocupados.csv` | No ocupados | `DSI` desocupado, `P7430` ¿ha trabajado antes?, `P7250` semanas buscando |

Llave para unir módulos: `MES` + `DIRECTORIO` + `SECUENCIA_P` + `ORDEN`.

## Variable objetivo (`processed/`)

- `sin_experiencia = 1` si el joven es **aspirante** (desocupado que nunca ha trabajado, `P7430 = 2`) o **recién insertado** (ocupado con 12 meses o menos en su empleo, `P6426 ≤ 12`).
- `consiguio_empleo`: 1 = recién insertado, 0 = aspirante. Vacío para el resto.
- Para porcentajes poblacionales usar `factor_expansion` (ya dividido entre 12 por unir 12 meses).

## Fuentes

- DANE — Gran Encuesta Integrada de Hogares (GEIH) 2025. https://microdatos.dane.gov.co/index.php/catalog/853
- Servicio Público de Empleo — Anexo Estadístico de Demanda Laboral (Vacantes). https://www.serviciodeempleo.gov.co/dataempleo-spe/demanda-laboral/anexo-estadistico-de-demanda-laboral-vacantes/

**Llave del cruce:** `codigo_departamento` (código DIVIPOLA de 2 dígitos), presente en ambas fuentes.
