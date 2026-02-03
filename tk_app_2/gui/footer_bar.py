import tkinter as tk


class FooterBar(tk.Frame):
    def __init__(self, root, state, dim):
        super().__init__(root, height=dim, width=dim)
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["footer_bg"])
        self.pack_propagate(False)
        
        self.label = tk.Label(
            self,
            bg=self.theme["footer_bg"],
            fg=self.theme["footer_text"],
            anchor="w"
        )
        self.label.pack(fill="x", padx=20)
        self.state.show_tool_expand.trace_add("write", self.update_status)

        self.update_status()  # initial text

    def update_status(self, *args):
        self.label.config(text=f"Tool Expand: {self.state.show_tool_expand.get()}")
