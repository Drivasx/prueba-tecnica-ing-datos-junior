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

    df = df[df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]]

    df = df.dropna(subset=["VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime"])


    df = df[df["passenger_count"].notna()]
    df = df[df["passenger_count"] > 0]

    df = df[df["trip_distance"].notna()]
    df = df[df["trip_distance"] >= 0]

    df = df[df["RatecodeID"].notna()]

    df = df[df["store_and_fwd_flag"].notna()]

    df = df[df["PULocationID"].notna()]

    df = df[df["DOLocationID"].notna()]

    df = df[df["payment_type"].notna()]

    df = df[df["fare_amount"].notna()]
    df = df[df["fare_amount"] >= 0]

    df = df[df["extra"] >= 0]

    df = df[df["mta_tax"] >= 0]

    df = df[df["tip_amount"] >= 0]

    df = df[df["tolls_amount"] >= 0]

    df = df[df["improvement_surcharge"] >= 0]

    df = df[df["total_amount"].notna()]
    df = df[df["total_amount"] >= 0]

    df = df[df["congestion_surcharge"] >= 0]

    df = df[df["Airport_fee"] >= 0]

    df = df[df["cbd_congestion_fee"] >= 0]

    return df.reset_index(drop=True)
