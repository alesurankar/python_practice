import pandas as pd


############################################
# my data
############################################
my_title = 'Sunny Days per Month'
my_label = 'Sunny Days'
my_xLabel = 'Month'
my_yLabel = 'Sunny Days'

my_candlestick_df = pd.DataFrame({
    "Date": pd.date_range("2025-01-01", periods=12, freq="ME"),
    "Open":  [7, 9, 11, 6, 15, 21, 17, 26, 18, 17, 13, 11],
    "Close": [9, 11, 6, 15, 21, 17, 26, 18, 17, 13, 11, 6],
    "High":  [12, 14, 14, 18, 24, 24, 29, 29, 21, 20, 16, 14],
    "Low":   [4, 6, 3, 3, 12, 14, 14, 15, 9, 8, 6, 1],
}).set_index("Date")

my_x = [d.strftime("%b") for d in my_candlestick_df.index]
my_y = my_candlestick_df['Close'].tolist()

my_avg = False
my_avg_label = 'Average Sunny Days'
############################################


class Data:
    title = my_title
    label = my_label
    xLabel = my_xLabel
    yLabel = my_yLabel

    x = my_x
    y = my_y

    avg = my_avg
    avg_label = my_avg_label
    avg_value = sum(y) / len(y)

    # Candlestick data
    candlestick_df = my_candlestick_df