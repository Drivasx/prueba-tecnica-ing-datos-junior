import pandas as pd
from pathlib import Path

def load_data(path: str) -> pd.DataFrame:

    path = Path(path)

    columns = [
        "VendorID",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "store_and_fwd_flag",
        "payment_type",
        "RatecodeID",
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "total_amount",
        "mta_tax",
        "fare_amount",
        "passenger_count"
    ]

    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {path}")
    
    return pd.read_parquet(path, columns=columns)


def load_taxi_zone_lookups(path: str | Path) -> pd.DataFrame:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {path}")
    
    return pd.read_csv(path)