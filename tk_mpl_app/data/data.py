import pandas as pd


class Data:
    # -----------------------------
    # Metadata
    # -----------------------------
    title = "Sunny Days per Month"
    label = "Sunny Days"
    xLabel = "Month"
    yLabel = "Sunny Days"

    avg = False
    avg_label = "Average Sunny Days"

    # -----------------------------
    # Load candlestick data
    # -----------------------------
    candlestick_df = pd.read_csv(
        "data/candles.csv",
        index_col="Date",
        parse_dates=True
    )

    # -----------------------------
    # Derived series (used by other charts)
    # -----------------------------
    x = candlestick_df.index.strftime("%b").tolist()   
    y = candlestick_df["Close"].tolist()        

    avg_value = sum(y) / len(y)