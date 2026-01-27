import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from graphs.graphs import draw_graph, get_graph_types
from gui.navigation import make_navigation_buttons
from gui.menus import create_menus
from data.data import Data


def create_gui(root):
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.Figure(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    GRAPH_TYPES = get_graph_types()
    AVG_SUPPORTED = {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}
    current_graph_index = 0

    def update_frame():  
        show_graph(GRAPH_TYPES[current_graph_index])
        update_ui()

    def show_graph(graph_type=None, data=None):
        graph_type = graph_type or context["current_graph"]
        data = data or context["data"]
        context["current_graph"] = graph_type
        draw_graph(fig, graph_type, data=data)
        canvas.draw()

    def update_ui():
        if context["current_graph"] in AVG_SUPPORTED:
            avg_button.pack(side="left", padx=5)
        else:
            avg_button.pack_forget()

    def next_graph():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index + 1) % len(GRAPH_TYPES)
        update_frame()

    def prev_graph():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index - 1) % len(GRAPH_TYPES)
        update_frame()

    def toggle_avg():
        context["data"].avg = not context["data"].avg
        show_graph()

    default_csv = "data/candles.csv"
    default_meta = default_csv.replace(".csv", ".meta.json")
    context = {
        "root": root,
        "fig": fig,
        "canvas": canvas,
        "current_graph": GRAPH_TYPES[0],
        "data": Data(default_csv, default_meta),
        "show_graph": show_graph
    }

    # Menus
    create_menus(root, context)
        
    # Navigation buttons
    button_config = [
        {"text": "Previous", "command": prev_graph, "side": "left"},
        {"text": "Toggle Avg", "command": toggle_avg, "side": "left"},
        {"text": "Next", "command": next_graph, "side": "right"},
    ]
    buttons = make_navigation_buttons(root, button_config)
    avg_button = buttons["Toggle Avg"]

    # Initial graph
    update_frame()

    return fig, canvas