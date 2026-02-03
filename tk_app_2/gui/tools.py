import tkinter as tk
from othr.bar import Bar


class Tools(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.tool_bar = Bar(self, self.state, 50, 1)
        self.tool_bar.pack(side="left", fill="y")

        self.tool_expand = Bar(self, self.state, 60, 1)
        self.tool_expand.pack(side="left", fill="y")
