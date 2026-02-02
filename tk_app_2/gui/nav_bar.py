import tkinter as tk


class NavigationBar(tk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent, height=50, bg="lightgreen")
        self.pack(side="top", fill="x")
        self.state = state