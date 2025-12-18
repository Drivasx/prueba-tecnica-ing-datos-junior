
## Prueba técnica - Ingeniero de datos junior (Procesamiento de datos)

Este repositorio contiene la solución de la prueba tecnica asignada para el puesto de ingeniero de datos junior, en la cual se implementa un pipeline de procesamiento de datos que carga, limpia, valida, transforma y exporta los dos archivos de salida .csv solicitados.

## Herramientas utilizadas

- Python 3.10.12
- Pandas 2.3.3
- Fastparquet 2024.11.0


## Estructura del proyecto

```md
prueba-tecnica-ing-datos-junior

├── data/
│   ├── raw/
|   |   └── yellow_tripdata_2025-01.parquet           # Datos de entrada
│   └── processed/                                    # Datos procesados
├── src/
│   ├── clean.py
│   ├── export.py
│   ├── load.py
|   ├── main.py
|   ├── transform.py
│   └── validate.py
├── .gitignore
├── requirements.txt
└── README.md
```
## Setup

NOTA: El proyecto fue desarrollado en un sistema opertivo Linux. Si se quiere ejecutar en Windows se recomienda hacer uso de git bash.


```bash
  
  git clone https://github.com/Drivasx/prueba-tecnica-ing-datos-junior.git
  cd prueba-tecnica-ing-datos-junior
```

Creación y activación del entorno virtual

Linux
```bash
  python -m venv venv
  source venv/bin/activate
```

Windows con Git Bash
```bash
  python -m venv venv
  source venv/Scripts/activate
```

Instalación de dependencias

```bash
  python -m pip install -r requirements.txt
```

Ejecución del proyecto

```bash
  python src/main.py
```
    
## Autor

David Mauricio Rivas Benavides

