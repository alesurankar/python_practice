import tkinter as tk
from gui.menu_bar import MenuBar
from gui.nav_bar import NavigationBar
from gui.matplotlib_widget import MatplotlibWidget
from gui.pygame_widget import PygameWidget
from state import AppState


root = tk.Tk()
root.title("Analysis App")
root.geometry("800x600")

# shared state
state = AppState()

# create widgets
menu = MenuBar(root, state)
nav = NavigationBar(root, state)
graph = MatplotlibWidget(root, state)
game = PygameWidget(root, state)

root.mainloop()
