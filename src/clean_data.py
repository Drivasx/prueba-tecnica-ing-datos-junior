import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.drop_duplicates()

    df["tpep_pickup_datetime"] = pd.to_datetime(
        df["tpep_pickup_datetime"], errors="coerce"
    )

    df["tpep_dropoff_datetime"] = pd.to_datetime(
        df["tpep_dropoff_datetime"], errors="coerce"
    )

    df["passenger_count"] = pd.to_numeric(
        df["passenger_count"],
        errors="coerce",
        downcast="integer"
    )

    df = df[df["passenger_count"].notna()]
    df = df[df["passenger_count"] >= 0]

    df = df[df["trip_distance"].notna()]
    df = df[df["trip_distance"] >= 0]
    
    df = df[df["PULocationID"].notna()]


    df = df[df["total_amount"].notna()]
    df = df[df["total_amount"] >= 0]