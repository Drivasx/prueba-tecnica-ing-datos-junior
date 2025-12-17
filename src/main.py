from pathlib import Path
from load import load_data
from clean import clean_data
from validate import validate_data
from transform import get_last_locations, get_trips_per_hour
from export import export_file

BASE_DIR = Path(__file__).resolve().parent.parent

def main():

    data_path = BASE_DIR / "data" / "raw" / "yellow_tripdata_2025-01.parquet"

    exports_path = BASE_DIR / "data" / "processed"

    df = load_data(data_path)
    print(df.columns)

    cleaned_df = clean_data(df)

    validated_df = validate_data(cleaned_df)

    last_locations = get_last_locations(validated_df)
    trips_per_hour = get_trips_per_hour(validated_df)
    
    export_file(last_locations, exports_path / "ultima_ubicacion.csv")

    export_file(trips_per_hour, exports_path / "viajes_por_hora.csv")

    print("Archivos exportados satisfactioriamente")


if __name__ == "__main__":
    main()