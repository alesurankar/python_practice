

class AppState:
    def __init__(self):
        self.theme_name = "dark"
        self.themes = {
            "dark": {
                "body_bg": "#1e1e1e",
                "body_text": "white",
                "nav_bg": "#463f3f",
                "footer_bg": "#2e2e2e",
                "footer_text": "white",
            },
            "light": {
                "body_bg": "white",
                "body_text": "black",
                "nav_bg": "#c2b6b6",
                "footer_bg": "#e0e0e0",
                "footer_text": "black",
            },
            "blue": {
                "body_bg": "#1e3d7c",
                "body_text": "white",
                "nav_bg": "#355491",
                "footer_bg": "#102147",
                "footer_text": "white",
            }
        }

    @property
    def theme(self):
        return self.themes[self.theme_name]