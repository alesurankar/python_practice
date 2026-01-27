from tkinter import ttk

def make_navigation_buttons(top_frame, toggle_avg, show_next, show_prev):
    avg_button = ttk.Button(top_frame, text="Toggle Avg", command=toggle_avg)
    avg_button.pack(side="top", padx=5)

    prev_button = ttk.Button(top_frame, text="Previous", command=show_prev)
    prev_button.pack(side="left", padx=5)
    next_button = ttk.Button(top_frame, text="Next", command=show_next)
    next_button.pack(side="right", padx=5)