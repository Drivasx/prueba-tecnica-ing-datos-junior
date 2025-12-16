from pathlib import Path
from loading import load_data
from cleaning import clean_data

BASE_DIR = Path(__file__).resolve().parent.parent

def main():

    data_path = BASE_DIR / "data" / "raw" / "yellow_tripdata_2025-01.parquet"

    df = load_data(data_path)

    cleaned_df = clean_data(df)
    print(cleaned_df)

    



if __name__ == "__main__":
    main()