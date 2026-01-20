import pandas as pd
import mplfinance as mpf

data = {
    "Date": pd.date_range("2024-01-01", periods=5, freq="D"),
    "Open":  [100, 102, 101, 103, 104],
    "Close": [102, 101, 103, 104, 106],
    "High":  [105, 106, 105, 108, 107],
    "Low":   [99, 100, 100, 103, 102],
}

df = pd.DataFrame(data)
df.set_index("Date", inplace=True)

mpf.plot(df, type='candle')
