import os
import tkinter as tk
from gui.gui import CreateGui


def main():
    root = tk.Tk()
    root.title("Analysis App")
    root.geometry("800x600")
    icon_path = os.path.join("assets", 'icon.ico')
    root.iconbitmap(icon_path)

    CreateGui(root)

    root.mainloop()

if __name__ == "__main__":
    main()