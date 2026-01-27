import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from charts.graphs import draw_graph, get_graph_types
from gui.navigation import make_navigation_buttons
from gui.menus import create_menus
from data.data import Data


def create_gui(root):
    # Plot frame
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.Figure(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    GRAPH_TYPES = get_graph_types()
    current_graph_index = 0

    def show_graph(graph_type):
        context["current_graph"] = graph_type
        draw_graph(fig, graph_type)
        canvas.draw()

    def show_next():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index + 1) % len(GRAPH_TYPES)
        show_graph(GRAPH_TYPES[current_graph_index])

    def show_prev():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index - 1) % len(GRAPH_TYPES)
        show_graph(GRAPH_TYPES[current_graph_index])

    # Menus
    context = {
        "root": root,
        "fig": fig,
        "canvas": canvas,
        "current_graph": GRAPH_TYPES[0],
        "data": Data("data/candles.csv")  # initial default data
    }
    create_menus(root, context)
        
    # Navigation buttons
    top_frame = ttk.Frame(root, padding=5)
    top_frame.pack(side="top", fill="x")
    make_navigation_buttons(top_frame, show_next, show_prev)

    # Initial graph
    show_graph(GRAPH_TYPES[0])

    return fig, canvas