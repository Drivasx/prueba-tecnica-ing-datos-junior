import pandas as pd

def get_last_locations(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.groupby("PULocationID").agg(ultimo_timestamp=("tpep_pickup_datetime", "max")).reset_index()

    return df.rename(columns={"PULocationID":"vehicle_id"})



def get_trips_per_hour(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["hora_del_dia"] = df["tpep_pickup_datetime"].dt.hour

    df = df.groupby("hora_del_dia").agg(total_viajes = ("PULocationID", "count")).reset_index()

    return df
    