import pandas as pd

def get_last_locations(df: pd.DataFrame, day: int) -> pd.DataFrame:

    if(day < 1 or day > 31):
        raise RuntimeError("El dia ingresado no es valido en el mes")
    
    df = df.copy()

    df["day"] = df["tpep_pickup_datetime"].dt.day

    df = df[df["day"] == day]

    df = df.groupby("PULocationID").agg(ultimo_timestamp=("tpep_pickup_datetime", "max")).reset_index()

    df = df.rename(columns={"PULocationID":"vehicle_id"})

    return df



def get_trips_per_hour(df: pd.DataFrame, day: int) -> pd.DataFrame:

    if(day < 1 or day > 31):
        raise RuntimeError("El dia ingresado no es valido en el mes")
    
    df = df.copy()

    df["day"] = df["tpep_pickup_datetime"].dt.day

    df = df[df["day"] == day]

    df["hora_del_dia"] = df["tpep_pickup_datetime"].dt.hour

    df = df.groupby("hora_del_dia").agg(total_viajes = ("PULocationID", "count")).reset_index()

    return df
    