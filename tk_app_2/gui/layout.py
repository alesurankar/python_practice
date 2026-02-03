import tkinter as tk
from othr.bar import Bar
from othr.main_view import MainView


class Layout(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])
        
        self.nav_bar = Bar(self, self.state, 40, 1)
        self.nav_bar.pack(side="top", fill="x")
        
        self.info_bar = Bar(self, self.state, 10, 1)
        self.info_bar.pack(side="top", fill="x")
        
        self.log_bar = Bar(self, self.state, 100, 2)
        self.log_bar.pack(side="bottom", fill="x")

        self.scroll_bar = Bar(self, self.state, 10, 1)
        self.scroll_bar.pack(side="right", fill="y")

        #self.main_view = MainView(self, self.state)
        