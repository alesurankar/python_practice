import tkinter as tk
from gui.layout import Layout
from gui.tools import Tools


class Body(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        self.left_side = Tools(self, self.state)
        self.left_side.pack(side="left", fill="y")
        self.right_side = Layout(self, self.state)
        self.right_side.pack(side="right", fill="both", expand=True)
        