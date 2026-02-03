import tkinter as tk
from state import AppState
from gui.menu_bar import MenuBar
from gui.body_frame import BodyFrame
from gui.footer_bar import FooterBar


root = tk.Tk()
root.title("Analysis App")
root.geometry("800x600")
root.minsize(width=400, height=220)

state = AppState(root)
menu = MenuBar(root, state)  
footer = FooterBar(root, state, 30) 
footer.pack(side="bottom", fill="x")  
body = BodyFrame(root, state)  
body.pack(fill="both", expand=True)


root.mainloop()
