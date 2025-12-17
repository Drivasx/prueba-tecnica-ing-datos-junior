import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.drop_duplicates()

    df = df.dropna(subset=["tpep_pickup_datetime", "tpep_dropoff_datetime", "store_and_fwd_flag", "payment_type", "RatecodeID", "PULocationID", "DOLocationID", "trip_distance", "total_amount", "mta_tax", "fare_amount", "passenger_count"])

    df["tpep_pickup_datetime"] = pd.to_datetime(
        df["tpep_pickup_datetime"], 
        errors="coerce"
    )

    df["tpep_dropoff_datetime"] = pd.to_datetime(
        df["tpep_dropoff_datetime"], 
        errors="coerce"
    )

    df["passenger_count"] = pd.to_numeric(
        df["passenger_count"],
        errors="coerce",
        downcast="integer"
    )

    df["trip_distance"] = pd.to_numeric(
        df["trip_distance"],
        errors="coerce"
    )

    df["RatecodeID"] = pd.to_numeric(
        df["RatecodeID"],
        errors="coerce"
    )


    df["PULocationID"] = pd.to_numeric(
        df["PULocationID"],
        errors="coerce"
    )

    df["DOLocationID"] = pd.to_numeric(
        df["DOLocationID"],
        errors="coerce"
    )

    df["fare_amount"] = pd.to_numeric(
        df["fare_amount"],
        errors="coerce"
    )


    df["mta_tax"] = pd.to_numeric(
        df["mta_tax"],
        errors="coerce"
    )


    df["total_amount"] = pd.to_numeric(
        df["total_amount"], 
        errors="coerce"
    )

    return df.reset_index(drop=True)
