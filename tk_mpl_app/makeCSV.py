import os
import pandas as pd

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

my_candlestick_df = pd.DataFrame({
    "Date": pd.date_range("2025-01-01", periods=12, freq="ME"),
    "Open":  [7, 9, 11, 6, 15, 21, 17, 26, 18, 17, 13, 11],
    "Close": [9, 11, 6, 15, 21, 17, 26, 18, 17, 13, 11, 6],
    "High":  [12, 14, 14, 18, 24, 24, 29, 29, 21, 20, 16, 14],
    "Low":   [4, 6, 3, 3, 12, 14, 14, 15, 9, 8, 6, 1],
}).set_index("Date")

# Export to CSV
my_candlestick_df.to_csv("data/candles.csv")
