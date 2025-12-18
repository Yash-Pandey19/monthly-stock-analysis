# Monthly Stock Analysis – Data Engineering Intern Assignment

## 📌 Project Overview
This project transforms **daily stock price data** into **monthly aggregated summaries** and computes key **technical indicators** used in financial analysis.  
The solution is implemented using **Python and Pandas only**, following a **modular and scalable data engineering approach**.

The pipeline:
- Converts daily OHLC data into monthly OHLC
- Computes moving averages on monthly closing prices
- Partitions the output into separate files for each stock ticker

---

## 📊 Dataset Details
- **Frequency:** Daily stock price data
- **Duration:** 2 years (24 months)
- **Tickers:**  
  `AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA`

### Input Schema
`date, volume, open, high, low, close, adjclose, ticker`
---

## 🧠 Processing Logic

### 1️⃣ Monthly Aggregation
Daily data is resampled to **monthly frequency (Month-End)** with the following logic:

| Column | Monthly Calculation |
|------|---------------------|
| Open | First trading day of the month |
| Close | Last trading day of the month |
| High | Maximum price in the month |
| Low | Minimum price in the month |

> ❗ Open and Close are **not averages**; they represent exact first and last values.

---

### 2️⃣ Technical Indicators
All indicators are calculated **only on monthly closing prices**.

- **SMA 10** – Simple Moving Average (10 months)
- **SMA 20** – Simple Moving Average (20 months)
- **EMA 10** – Exponential Moving Average (10 months)
- **EMA 20** – Exponential Moving Average (20 months)

Implementation uses Pandas rolling and exponential window functions (no third-party TA libraries).

---

## 📂 Project Directory Structure
```
monthly-stock-analysis/
│
├── data/
│ └── input/
│        └── stock_prices.csv # Input daily stock dataset
│
├── src/
│       ├── data_loader.py # Loads CSV & parses dates
│       ├── aggregator.py # Daily → Monthly OHLC aggregation
│       ├── indicators.py # SMA & EMA calculations
│       ├── writer.py # Writes output CSV files
│       └── main.py # Pipeline orchestration
│
├── output/
│       ├── result_AAPL.csv
│       ├── result_AMD.csv
│       ├── result_AMZN.csv
│       ├── result_AVGO.csv
│       ├── result_CSCO.csv
│       ├── result_MSFT.csv
│       ├── result_NFLX.csv
│       ├── result_PEP.csv
│       ├── result_TMUS.csv
│       └── result_TSLA.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```
---

## 📁 Output Specifications
- **10 CSV files** (one per ticker)
- **Exactly 24 rows per file** (24 months)
- File naming format:  
  `result_<TICKER>.csv`

Each output file contains:

 ``date, open, close, high, low, SMA_10, SMA_20, EMA_10, EMA_20``
 ---
 
---

## ⚙️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Run the pipeline
```bash
python src/main.py
```
---
## 🧪Assumptions Made

- Dataset contains no missing trading months

- Market holidays are implicitly handled by available trading days

- Month-end is considered the last available trading day

- Initial EMA values use Pandas default initialization

- Missing indicator values at the beginning are expected (NaN)



