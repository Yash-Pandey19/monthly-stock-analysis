import os
import pandas as pd

def write_to_csv(df: pd.DataFrame, ticker: str, output_dir: str = "output"):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"result_{ticker}.csv")
    df.to_csv(file_path, index=False)
