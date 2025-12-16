import pandas as pd
from pathlib import Path

def load_data(path: str) -> pd.DataFrame:


    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {path}")
    
    return pd.read_parquet(path)