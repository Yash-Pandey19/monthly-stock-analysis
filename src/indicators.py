import pandas as pd

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df["SMA_10"] = df["close"].rolling(window=10).mean()
    df["SMA_20"] = df["close"].rolling(window=20).mean()

    df["EMA_10"] = df["close"].ewm(span=10, adjust=False).mean()
    df["EMA_20"] = df["close"].ewm(span=20, adjust=False).mean()

    return df
