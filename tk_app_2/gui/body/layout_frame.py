import tkinter as tk
from othr.bar import Bar
from othr.main_view import MainView


class Layout(tk.PanedWindow):
    def __init__(self, root, state):
        super().__init__(root, orient="horizontal")
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        self.DEFAULT_WIDTH = 60
        self.last_expand_width = self.DEFAULT_WIDTH

        # Expandable toolbar
        self.tool_expand = Bar(self, self.state, 120, 0, self.theme.get("tool_expand_bg"))
        self.add(self.tool_expand, minsize=60)

        self.main_view = MainView(self, self.state)
        self.add(self.main_view)

    def show_expand(self):
        if not self.state.show_tool_expand.get():
            width = max(self.last_expand_width, self.DEFAULT_WIDTH)
            self.paneconfigure(self.tool_expand, minsize=60)
            self.sash_place(0, width, 0)
            self.state.show_tool_expand.set(True)

    def hide_expand(self):
        if self.state.show_tool_expand.get():
            self.last_expand_width = self.sash_coord(0)[0]
            self.paneconfigure(self.tool_expand, minsize=0)
            self.sash_place(0, 0, 0)
            self.state.show_tool_expand.set(False)