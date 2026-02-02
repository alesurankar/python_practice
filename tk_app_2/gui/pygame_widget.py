import tkinter as tk


class PygameWidget(tk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent, bg="lightcoral", width=400, height=300)
        self.pack(fill="both", expand=True)
        self.state = state
