import pandas as pd
from typing import List


def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Realiza validaciones básicas sobre el DataFrame:
    - Verifica columnas canónicas (date, partner, amount).
    - Revisa que amount sea numérico y >= 0.
    - Revisa que date sea datetime.
    Devuelve lista de errores (vacía si todo está bien).
    """
    errors: List[str] = []

    # Validar columnas
    required_cols = {"date", "partner", "amount"}
    missing = required_cols - set(df.columns)
    if missing:
        errors.append(f"Faltan columnas canónicas: {', '.join(missing)}")

    # Validar amount
    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append("La columna 'amount' no es numérica.")
        elif (df["amount"] < 0).any():
            errors.append("Existen valores negativos en 'amount'.")

    # Validar date
    if "date" in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df["date"]):
            errors.append("La columna 'date' no es datetime.")

    return errors
