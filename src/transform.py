import pandas as pd

def get_last_locations(df: pd.DataFrame, aux_csv: pd.DataFrame, day: int) -> pd.DataFrame:

    if(day < 1 or day > 31):
        raise RuntimeError("El dia ingresado no es valido en el mes")
    
    df = df.copy()

    df = df[df["tpep_pickup_datetime"].dt.day == day]

    df = df.groupby("PULocationID").agg(ultimo_timestamp=("tpep_pickup_datetime", "max")).reset_index()

    df = df.rename(columns={"PULocationID":"vehicle_id"})

    df = df.merge(
        aux_csv,
        how="left",
        left_on="vehicle_id",
        right_on="LocationID"
    )

    df = df.drop(columns="LocationID")

    df = df.rename(columns={"Borough":"ciudad", "Zone":"zona", "service_zone":"zona_servicio"})

    return df



def get_trips_per_hour(df: pd.DataFrame, day: int) -> pd.DataFrame:

    if(day < 1 or day > 31):
        raise RuntimeError("El dia ingresado no es valido en el mes")
    
    df = df.copy()

    df = df[df["tpep_pickup_datetime"].dt.day == day]

    df["hora_del_dia"] = df["tpep_pickup_datetime"].dt.hour

    df = df.groupby("hora_del_dia").agg(total_viajes = ("PULocationID", "count")).reset_index()

    return df
    