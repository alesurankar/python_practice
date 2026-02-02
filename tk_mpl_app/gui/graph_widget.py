import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from graphs.graphs import draw_graph, get_graph_types
from data.data import Data
from gui.components.theme import THEME

GRAPH_THEME = {
    'facecolor': THEME['bg'],
    'textcolor': THEME['text'],
    'tick_color': THEME['text'],
    'legend_text': THEME['text']
}

AVG_SUPPORTED = {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}

class GraphWidget(tk.Frame):
    def __init__(self, parent, context, default_csv="data/candles.csv"):
        super().__init__(parent, bg=THEME["bg"])
        self.pack(fill=tk.BOTH, expand=True)

        # Matplotlib figure
        self.fig = plt.Figure(figsize=(8, 5), facecolor=THEME["bg"])
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.get_tk_widget().config(bg=THEME["bg"])

        # Graph types
        self.GRAPH_TYPES = get_graph_types()
        self.context = context

        # Load data
        default_meta = default_csv.replace(".csv", ".meta.json")
        self.context["data"] = Data(default_csv, default_meta)
        self.context["current_graph_index"] = 0
        self.context["current_graph"] = self.GRAPH_TYPES[0]

        # Put figure and canvas into context
        self.context["fig"] = self.fig
        self.context["canvas"] = self.canvas
        self.context["show_graph"] = self.show_graph
        self.context["update_frame"] = self.update_frame

        # Initial draw
        self.update_frame()

    def apply_theme(self):
        for ax in self.fig.get_axes():
            ax.set_facecolor(GRAPH_THEME['facecolor'])
            ax.title.set_color(GRAPH_THEME['textcolor'])
            ax.xaxis.label.set_color(GRAPH_THEME['textcolor'])
            ax.yaxis.label.set_color(GRAPH_THEME['textcolor'])
            ax.tick_params(colors=GRAPH_THEME['tick_color'])
            legend = ax.get_legend()
            if legend:
                for text in legend.get_texts():
                    text.set_color(GRAPH_THEME['legend_text'])

    def update_frame(self):
        index = self.context["current_graph_index"]
        self.show_graph(self.GRAPH_TYPES[index])
        self.update_ui()

    def show_graph(self, graph_type=None, data=None):
        graph_type = graph_type or self.context["current_graph"]
        data = data or self.context["data"]
        self.context["current_graph"] = graph_type
        draw_graph(self.fig, graph_type, data=data)
        self.apply_theme()
        self.canvas.draw()

    def update_ui(self):
        avg_button = self.context.get("avg_button")
        if avg_button:
            if self.context["current_graph"] in AVG_SUPPORTED:
                avg_button.show()
            else:
                avg_button.hide()
