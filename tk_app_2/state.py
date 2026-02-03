import tkinter as tk


class AppState:
    def __init__(self, root):
        self.show_tool_expand = tk.BooleanVar(root, True)
        self.theme_name: str = "dark"
        self.themes: dict[str, dict[str, str]] = {
            "dark": {
                "body_bg": "#1e1e1e",
                "body_text": "#ffffff",
                "tool_bg": "#333333",
                "tool_expand_bg": "#252526",
                "tool_bar_text": "#657885",
                "tool_bar_text_hover": "#ffffff",
                "nav_bg": "#363636",
                "footer_bg": "#2e2e2e",
                "footer_text": "white",
            }
        }

    @property
    def theme(self):
        return self.themes[self.theme_name]