import tkinter as tk


class PygameWidget(tk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent, bg="lightcoral", width=400, height=300)
        self.state = state

    def update_visibility(self):
        if self.state.show_game:
            self.pack(fill="both", expand=True)
        else:
            self.pack_forget()