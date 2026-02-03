import tkinter as tk
from othr.bar import Bar


class ToolBar(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.tool_bar = Bar(self, self.state, 50, 0, self.theme.get("tool_bg"))
        self.tool_bar.pack(side="left", fill="y")

        self._build_ui()
    
    def _build_ui(self):
        c = self.tool_bar.canvas

        size = 36
        pad = 8

        def make_btn(text):
            btn = tk.Button(
                c,
                text=text,
                bg=self.theme.get("tool_bg"),
                fg="gray",
                bd=0,
                relief="flat",
                activebackground=self.theme.get("tool_bg"),
                width=2,
                height=1,
            )

            def on_enter(e):
                btn.config(fg="white")
                btn.config(cursor="hand2")

            def on_leave(e):
                btn.config(fg="gray")
                btn.config(cursor="")

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            return btn

        self.btn1 = make_btn("Abcde")
        self.btn2 = make_btn("B")
        self.btn3 = make_btn("C")

        c.create_window(25, pad + size * 0 + pad * 0, window=self.btn1, anchor="n")
        c.create_window(25, pad + size * 1 + pad * 1, window=self.btn2, anchor="n")
        c.create_window(25, pad + size * 2 + pad * 2, window=self.btn3, anchor="n")