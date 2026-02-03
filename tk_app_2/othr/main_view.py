import tkinter as tk
from othr.matplotlib_widget import MatplotlibWidget
from othr.pygame_widget import PygameWidget


class MainView(tk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent, bg="black")
        self.pack(fill="both", expand=True)
        self.state = state

        self.graph = MatplotlibWidget(self, state)
        self.game = PygameWidget(self, state)

        self.update_visibility()

    def update_visibility(self):
        self.graph.pack_forget()
        self.game.pack_forget()

        if self.state.show_game:
            self.game.pack(fill="both", expand=True)
        else:
            self.graph.pack(fill="both", expand=True)