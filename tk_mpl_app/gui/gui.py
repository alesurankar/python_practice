import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from charts.graphs import DrawGraph


def CreateGui(root):
    # -----------------------------
    # Plot area
    # -----------------------------
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.Figure(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # -----------------------------
    # Graph functions
    # -----------------------------
    GRAPH_TYPES = [
        'plot',          # line plots
        'bar',           # vertical bars
        'barh',          # horizontal bars
        'scatter',       # points
        'fill_between',  # area under curve
        'step',          # step plot
        'errorbar',      # line with error bars
        'hist',          # histogram
        'boxplot',       # box & whisker
        'violinplot',    # violin plot
        'pie',           # pie chart
        'candlestick',
    ]
    def ShowGraph(graphType):
        DrawGraph(fig, graphType)
        canvas.draw()

    current_graph_index = 0
    def ShowNextGraph():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index + 1) % len(GRAPH_TYPES)
        ShowGraph(GRAPH_TYPES[current_graph_index])

    def ShowPrevGraph():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index - 1) % len(GRAPH_TYPES)
        ShowGraph(GRAPH_TYPES[current_graph_index])

    # -----------------------------
    # File menu
    # -----------------------------
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    def ExportPNG():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )
        if file_path:
            fig.savefig(file_path, dpi=300, bbox_inches="tight")

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Export as PNG", command=ExportPNG)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # -----------------------------
    # View menu
    # -----------------------------
    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View", menu=view_menu)

    # -----------------------------
    # Help menu
    # -----------------------------
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    def ShowAbout():
        messagebox.showinfo("About", "Analysis App\nVersion 1.0")

    help_menu.add_command(label="About", command=ShowAbout)

    # -----------------------------
    # Top buttons for navigation
    # -----------------------------
    top_frame = ttk.Frame(root, padding=5)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    next_button = ttk.Button(top_frame, text="Next", command=lambda: ShowNextGraph())
    next_button.pack(side=tk.RIGHT, padx=5)
    prev_button = ttk.Button(top_frame, text="Previous", command=lambda: ShowPrevGraph())
    prev_button.pack(side=tk.RIGHT, padx=5)

    # -----------------------------
    # Show initial graph
    # -----------------------------
    ShowGraph('plot')

    # Return figure and canvas in case app.py wants it
    return fig, canvas