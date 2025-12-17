
import pandas as pd
from pathlib import Path

def export_file(df: pd.DataFrame, path: str | Path) -> None:

    export_path = Path(path)

    df.to_csv(export_path, index=False)