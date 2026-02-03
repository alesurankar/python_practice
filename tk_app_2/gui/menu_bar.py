import tkinter as tk


class MenuBar:
    def __init__(self, root, state):
        self.root = root
        self.state = state

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=menu)
        menu.add_command(label="Exit", command=root.quit)
       