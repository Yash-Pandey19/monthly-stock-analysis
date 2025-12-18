import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df
