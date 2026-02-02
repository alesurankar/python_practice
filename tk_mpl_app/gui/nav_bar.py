import tkinter as tk
from gui.components.button import ModernButton
from gui.components.theme import THEME


class NavigationBar(tk.Frame):
    """Encapsulates navigation buttons and exposes a simple interface to App."""
    def __init__(self, parent, button_config: list[dict]):
        super().__init__(parent, bg=THEME["bg"], height=70)
        self.pack(side="top", fill="x")

        # Canvas to handle flexible button placement
        self.canvas = tk.Canvas(self, bg=THEME["bg"], highlightthickness=0, height=70)
        self.canvas.pack(fill="both", expand=True)

        # Store buttons in a dict
        self.buttons: dict[str, ModernButton] = {}
        self._create_buttons(button_config)
        self._update_positions()
        self.canvas.bind("<Configure>", lambda e: self._update_positions())


    def _create_buttons(self, button_config: list[dict]):
        for info in button_config:
            key = info.get("key")
            if not key:
                raise ValueError("Button config missing 'key'")
            btn = ModernButton(
                self.canvas,
                text=info["text"],
                command=info.get("command"),
                width=130,
                height=42,
                radius=20,
            )
            self.buttons[key] = btn

    def _update_positions(self):
        n = len(self.buttons)
        width = self.canvas.winfo_width()
        spacing = width / (n + 1)
        for i, btn in enumerate(self.buttons.values()):
            x = spacing * (i + 1) - btn.width / 2
            btn.place(x=int(x), y=14)
            btn._pos = (int(x), 14) 

    # --- Public API for App ---
    def show_avg_button(self):
        if "avg" in self.buttons:
            self.buttons["avg"].show()

    def hide_avg_button(self):
        if "avg" in self.buttons:
            self.buttons["avg"].hide()