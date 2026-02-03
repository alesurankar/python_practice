import tkinter as tk
from state import AppState
from gui.menu_bar import MenuBar
from gui.body import Body
from gui.footer import Footer


root = tk.Tk()
root.title("Analysis App")
root.geometry("800x600")
root.minsize(width=400, height=220)

state = AppState()
menu = MenuBar(root, state)  
footer = Footer(root, state, 30) 
footer.pack(side="bottom", fill="x")  
body = Body(root, state)  
body.pack(fill="both", expand=True)


root.mainloop()
