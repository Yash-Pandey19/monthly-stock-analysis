# Monthly Stock Analysis – Data Engineering Intern Assignment

##  Project Overview
This project transforms **daily stock price data** into **monthly aggregated summaries** and computes key **technical indicators** used in financial analysis.  
The solution is implemented using **Python and Pandas only**, following a **modular and scalable data engineering approach**.

The pipeline:
- Converts daily OHLC data into monthly OHLC
- Computes moving averages on monthly closing prices
- Partitions the output into separate files for each stock ticker

---

##  Dataset Details
- **Frequency:** Daily stock price data
- **Duration:** 2 years (24 months)
- **Tickers:**  
  `AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA`

### Input Schema
`date, volume, open, high, low, close, adjclose, ticker`
---

##  Processing Logic

### 1 Monthly Aggregation
Daily data is resampled to **monthly frequency (Month-End)** with the following logic:

| Column | Monthly Calculation |
|------|---------------------|
| Open | First trading day of the month |
| Close | Last trading day of the month |
| High | Maximum price in the month |
| Low | Minimum price in the month |

>  Open and Close are **not averages**; they represent exact first and last values.

---

### 2 Technical Indicators
All indicators are calculated **only on monthly closing prices**.

- **SMA 10** – Simple Moving Average (10 months)
- **SMA 20** – Simple Moving Average (20 months)
- **EMA 10** – Exponential Moving Average (10 months)
- **EMA 20** – Exponential Moving Average (20 months)

Implementation uses Pandas rolling and exponential window functions (no third-party TA libraries).

---

##  Project Directory Structure
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

##  Output Specifications
- **10 CSV files** (one per ticker)
- **Exactly 24 rows per file** (24 months)
- File naming format:  
  `result_<TICKER>.csv`

Each output file contains:

 ``date, open, close, high, low, SMA_10, SMA_20, EMA_10, EMA_20``
 ---
 
---

##  How to Run the Project

### 1 Install dependencies
```bash
pip install -r requirements.txt
```
### 2 Run the pipeline
```bash
python src/main.py
```
---
##  Practical Assumptions

1. The dataset contains valid daily stock price records with no duplicate rows per ticker and date.

2. Missing trading days (weekends and market holidays) are implicitly handled, as monthly aggregation is performed only on available trading days.

3. Month-end is defined as the **last available trading day of the month**, not necessarily the calendar month-end.

4. Monthly **Open** and **Close** prices are derived from the **first and last trading day** of each month respectively, and are not averaged.

5. Technical indicators (SMA & EMA) are calculated **only on monthly closing prices**, as required by the assignment.

6. Initial values for SMA and EMA result in `NaN` for early months where sufficient historical data is not available. This behavior is expected and aligns with standard financial practices.

7. Exponential Moving Average (EMA) values use Pandas’ default initialization method, which applies the standard recursive EMA formula with an internally computed smoothing factor.

8. The dataset spans exactly **24 consecutive months**, and no month-level gaps are present in the input data.

9. All computations are performed using **vectorized Pandas operations** without relying on third-party technical analysis libraries.

10. The dataset size is assumed to be small enough to fit in memory, making Pandas a suitable choice over distributed processing frameworks.