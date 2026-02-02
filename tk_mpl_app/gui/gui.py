import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from graphs.graphs import draw_graph, get_graph_types
from gui.navigation import make_navigation_buttons
from gui.menus import create_menus
from data.data import Data
from gui.actions import toggle_avg, next_graph, prev_graph


def create_gui(root):
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.Figure(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    GRAPH_TYPES = get_graph_types()
    AVG_SUPPORTED = {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}


    def update_frame():  
        index = context["current_graph_index"]
        show_graph(GRAPH_TYPES[index])
        update_ui()

    def show_graph(graph_type=None, data=None):
        graph_type = graph_type or context["current_graph"]
        data = data or context["data"]
        context["current_graph"] = graph_type
        draw_graph(fig, graph_type, data=data)
        canvas.draw()

    def update_ui():
        if context["current_graph"] in AVG_SUPPORTED:
            avg_button.show()
        else:
            avg_button.hide()


    default_csv = "data/candles.csv"
    default_meta = default_csv.replace(".csv", ".meta.json")
    context = {
        "root": root,
        "fig": fig,
        "canvas": canvas,
        "current_graph_index": 0,
        "current_graph": GRAPH_TYPES[0],
        "data": Data(default_csv, default_meta),
        "show_graph": show_graph,
        "update_frame": update_frame
    }

    # Menus
    create_menus(root, context)
        
    # Navigation buttons
    button_config = [
    {"text": "Previous", "command": lambda: prev_graph(context, GRAPH_TYPES), "side": "left"},
    {"text": "Toggle Avg", "command": lambda: toggle_avg(context), "side": "left"},
    {"text": "Next", "command": lambda: next_graph(context, GRAPH_TYPES), "side": "right"},
    ]
    buttons = make_navigation_buttons(root, button_config)
    avg_button = buttons["Toggle Avg"]

    # Initial graph
    update_frame()

    return fig, canvas