import pandas as pd
from datetime import datetime, timezone
from typing import List


def tag_lineage(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Añade metadata de linaje:
    - source_file: nombre de archivo de origen.
    - ingested_at: timestamp UTC ISO.
    """
    df = df.copy()
    df["source_file"] = source_name
    df["ingested_at"] = datetime.now(timezone.utc).isoformat()
    return df


def concat_bronze(frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatena múltiples DataFrames en un esquema canónico:
    - Columnas esperadas: date, partner, amount, source_file, ingested_at.
    """
    if not frames:
        return pd.DataFrame(columns=["date", "partner", "amount", "source_file", "ingested_at"])

    bronze = pd.concat(frames, ignore_index=True)

    # Reordenar columnas
    cols = ["date", "partner", "amount", "source_file", "ingested_at"]
    bronze = bronze[[c for c in cols if c in bronze.columns]]

    return bronze
