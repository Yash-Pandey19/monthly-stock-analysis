import pandas as pd

def monthly_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("date")
    df = df.set_index("date")

    monthly_df = df.resample("M").agg({
        "open": "first",
        "close": "last",
        "high": "max",
        "low": "min"
    })

    return monthly_df.reset_index()
