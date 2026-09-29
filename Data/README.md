# /data — Datos del proyecto

Aquí van los archivos de datos del proyecto **Búsqueda de Empleo Sin Experiencia**.

## Contenido actual

| Archivo | Descripción | Estado |
|---|---|---|
| `datos_simulados_empleo_sin_experiencia.csv` | 1.200 jóvenes de 18 a 28 años con 17 variables. **Datos simulados** (`fuente = SIMULADO`) para practicar mientras se descargan las fuentes reales. | Temporal |

## Fuentes reales (por descargar)

| Fuente | Qué contiene | Dónde se consigue |
|---|---|---|
| GEIH 2025 — DANE | Encuesta del mercado laboral: edad, educación, ciudad, ocupación, jóvenes que buscan su primer empleo | https://microdatos.dane.gov.co/index.php/catalog/853 |
| Vacantes del Servicio Público de Empleo (SPE) | Vacantes por sector, ocupación, ciudad, educación y experiencia exigida, tipo de contrato y salario | https://www.serviciodeempleo.gov.co (datos abiertos) y https://dataempleo.serviciodeempleo.gov.co |

## Organización sugerida

```
data/
├── raw/        # archivos originales descargados, sin modificar
├── processed/  # datos limpios generados por los notebooks
└── README.md
```

## Reglas

- Nunca modificar los archivos de `raw/`; los cambios se hacen en los notebooks y se guardan en `processed/`.
- Si un archivo pesa más de 100 MB (GitHub no lo acepta), no se sube: se deja aquí el enlace de descarga.
- No subir datos personales sin anonimizar.
