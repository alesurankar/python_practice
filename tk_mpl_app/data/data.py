import os
import json
import pandas as pd

class Data:
    def __init__(self, csv_path, meta_path=None):

        # Load metadata from JSON
        if meta_path and os.path.exists(meta_path):
            with open(meta_path, "r") as f:
                meta = json.load(f)
        else:
            meta = {}

        self.title = meta.get("title", "Untitled")
        self.label = meta.get("label", "Y")
        self.x_label = meta.get("x_label", "X")
        self.y_label = meta.get("y_label", "Y")
        self.avg = meta.get("avg", False)
        self.avg_label = meta.get("avg_label", "Average")

        # Load candlestick data
        self.df = pd.read_csv(
            csv_path, 
            index_col="Date", 
            parse_dates=True
        )


        # -----------------------------
        # Derived series (used by other charts)
        # -----------------------------
        self.x = self.df.index.strftime("%b").tolist()   
        self.y = self.df["Close"].tolist()        

        self.avg_val = sum(self.y) / len(self.y)