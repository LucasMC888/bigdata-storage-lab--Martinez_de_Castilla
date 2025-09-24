import pandas as pd
from typing import Dict


def normalize_columns(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Normaliza columnas según el esquema canónico:
    - Renombra columnas usando un mapping origen→{date, partner, amount}.
    - Convierte date a datetime ISO (YYYY-MM-DD).
    - Limpia partner (espacios extra).
    - Normaliza amount (quita símbolos €, separadores europeos, convierte a float).
    """
    # Renombrar columnas
    df = df.rename(columns=mapping)

    # Normalizar fechas
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.normalize()

    # Normalizar partner
    if "partner" in df.columns:
        df["partner"] = df["partner"].astype(str).str.strip()

    # Normalizar amount
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace("€", "", regex=False)
            .str.replace(".", "", regex=False)  # quitar separadores miles estilo europeo
            .str.replace(",", ".", regex=False)  # convertir coma decimal en punto
        )
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df


def to_silver(bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega datos de bronze → silver:
    - Agrupa por partner y mes.
    - Suma amounts.
    - Columna month: primer día del mes (timestamp).
    """
    if "date" not in bronze.columns or "partner" not in bronze.columns or "amount" not in bronze.columns:
        raise ValueError("Bronze DataFrame no tiene las columnas canónicas necesarias.")

    silver = bronze.copy()
    silver["month"] = silver["date"].dt.to_period("M").dt.to_timestamp()

    agg = (
        silver.groupby(["partner", "month"], as_index=False)
        .agg({"amount": "sum"})
    )
    return agg
