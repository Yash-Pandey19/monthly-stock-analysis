from data_loader import load_data
from aggregator import monthly_aggregate
from indicators import calculate_indicators
from writer import write_to_csv

INPUT_FILE = "data/input/stock_prices.csv"

def main():
    df = load_data(INPUT_FILE)

    for ticker, group in df.groupby("ticker"):
        monthly_df = monthly_aggregate(group)
        monthly_df = calculate_indicators(monthly_df)
        write_to_csv(monthly_df, ticker)

if __name__ == "__main__":
    main()
