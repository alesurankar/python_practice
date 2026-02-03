import tkinter as tk


class AppState:
    def __init__(self, root):
        self.show_tool_expand = tk.BooleanVar(root, True)
        self.theme_name: str = "dark"
        self.themes: dict[str, dict[str, str]] = {
            "dark": {
                "body_bg": "#1e1e1e",
                "body_text": "white",
                "tool_bg": "#4f4f4f",
                "tool_expand_bg": "#363636",
                "footer_bg": "#2e2e2e",
                "footer_text": "white",
            },
            "light": {
                "body_bg": "white",
                "body_text": "black",
                "tool_bg": "#979797",
                "tool_expand_bg": "#C9C9C9",
                "footer_bg": "#e0e0e0",
                "footer_text": "black",
            },
            "blue": {
                "body_bg": "#1e3d7c",
                "body_text": "white",
                "tool_bg": "#3264c8",
                "tool_expand_bg": "#2a55ab",
                "footer_bg": "#102147",
                "footer_text": "white",
            }
        }

    @property
    def theme(self):
        return self.themes[self.theme_name]