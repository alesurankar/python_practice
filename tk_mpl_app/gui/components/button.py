import tkinter as tk
from gui.components.theme import THEME


class ModernButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=120, height=40, radius=18):
        super().__init__(parent, width=width, height=height, bg=THEME["bg"], highlightthickness=0)
        self.command = command
        self.text = text
        self.width = width
        self.height = height
        self.radius = radius

        self.draw_button(THEME["btn_bg"])

        # hover + press events
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)

    def draw_button(self, color):
        self.delete("all")
        r = self.radius
        w = self.width
        h = self.height

        # rounded rectangle
        self.create_arc(0, 0, 2*r, 2*r, start=90, extent=90, fill=color, outline=color)
        self.create_arc(w-2*r, 0, w, 2*r, start=0, extent=90, fill=color, outline=color)
        self.create_arc(0, h-2*r, 2*r, h, start=180, extent=90, fill=color, outline=color)
        self.create_arc(w-2*r, h-2*r, w, h, start=270, extent=90, fill=color, outline=color)
        self.create_rectangle(r, 0, w-r, h, fill=color, outline=color)
        self.create_rectangle(0, r, w, h-r, fill=color, outline=color)

        # text
        self.create_text(w/2, h/2, text=self.text, fill=THEME["text"], font=("Segoe UI", 11, "bold"))

    def on_hover(self, event):
        self.draw_button(THEME["btn_hover"])

    def on_leave(self, event):
        self.draw_button(THEME["btn_bg"])

    def on_press(self, event):
        self.draw_button(THEME["btn_press"])

    def on_release(self, event):
        self.draw_button(THEME["btn_hover"])
        if self.command:
            self.command()

    def show(self):
        self.place_forget()  # remove if already placed
        self.place(x=self.winfo_x(), y=self.winfo_y()) 

    def hide(self):
        self.place_forget()
