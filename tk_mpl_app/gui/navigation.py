import tkinter as tk
from gui.components.button import ModernButton
from gui.components.theme import THEME


def make_navigation_buttons(root, buttons_info):
    frame = tk.Frame(root, bg=THEME["bg"], height=70)
    frame.pack(side="top", fill="x")

    canvas = tk.Canvas(frame, bg=THEME["bg"], highlightthickness=0, height=70)
    canvas.pack(fill="both", expand=True)

    buttons_list = []

    # Create buttons
    for info in buttons_info:
        btn = ModernButton(canvas, text=info["text"], command=info["command"], width=130, height=42, radius=20)
        buttons_list.append(btn)

    def update_positions(event=None):
        n = len(buttons_list)
        width = canvas.winfo_width()
        spacing = width / (n + 1)
        for i, btn in enumerate(buttons_list):
            x = spacing * (i + 1) - btn.width / 2
            btn.place(x=int(x), y=14)  # position inside canvas

    canvas.bind("<Configure>", update_positions)
    canvas.after(10, update_positions)

    # Convert list to dict keyed by button text
    return {btn.text: btn for btn in buttons_list}
