import pandas as pd

def validate_data(df : pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df[df["trip_distance"] > 0]

    df = df[df["total_amount"] >= 0]

    df = df[df["fare_amount"] >= 0]

    df = df[df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]]

    df = df[df["VendorID"].isin([1,2,6,7])]

    df = df[df["store_and_fwd_flag"].isin(["Y","N"])]

    df = df[df["RatecodeID"].isin([1,2,3,4,5,6,99])]

    df = df[df["payment_type"].isin([0,1,2,3,4,5,6])]

    df = df[df["mta_tax"].isin([0,0.5])]


    return df.reset_index(drop=True)