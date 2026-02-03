import tkinter as tk
from othr.bar import Bar


class Footer(tk.Frame):
    def __init__(self, root, state, dim):
        super().__init__(root)
        self.state = state
        self.theme = state.theme

        # Canvas to handle flexible button placement
        self.canvas = tk.Canvas(self, bg=self.theme["footer_bg"], highlightthickness=0, height=dim, width=dim)
        self.canvas.pack(fill="both", expand=True)
    