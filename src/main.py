from pathlib import Path
from load_data import load_data

BASE_DIR = Path(__file__).resolve().parent.parent

def main():

    data_path = BASE_DIR / "data" / "raw" / "yellow_tripdata_2025-01.parquet"

    df = load_data(data_path)
    print(df.head())
    



if __name__ == "__main__":
    main()