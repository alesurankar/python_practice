import tkinter as tk


class Bar(tk.Frame):
    def __init__(self, root, state, dim, border):
        super().__init__(root, height=dim, width=dim)
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["nav_bg"])

        # Canvas to handle flexible button placement
        self.canvas = tk.Canvas(self, bg=self.theme["nav_bg"], highlightthickness=border, height=dim, width=dim)
        self.canvas.pack(fill="both", expand=True)