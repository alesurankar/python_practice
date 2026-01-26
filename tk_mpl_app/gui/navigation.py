import tkinter as ttk

def MakeNavigationButtons(top_frame, ShowNext, ShowPrev):
    next_button = ttk.Button(top_frame, text="Next", command=ShowNext)
    next_button.pack(side="right", padx=5)
    prev_button = ttk.Button(top_frame, text="Previous", command=ShowPrev)
    prev_button.pack(side="right", padx=5)