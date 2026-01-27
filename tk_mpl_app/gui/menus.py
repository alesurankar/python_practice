import os
import tkinter as tk
from tkinter import messagebox, filedialog
from data.data import Data
from charts.graphs import draw_graph


def create_menus(root, fig):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    _build_menu(menubar, "File", FILE_MENU_ITEMS, {"root": root, "fig": fig})
    _build_menu(menubar, "Help", HELP_MENU_ITEMS, {})


# Menu Builder
def _build_menu(menubar, label, items, context=None):
    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=label, menu=menu)

    for text, action in items:
            menu.add_command(
                label=text, 
                command=lambda a=action: a(context)
            )
    return menu

# Internal Menu
def _export_png(fig):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )
    if file_path:
        fig.savefig(file_path, dpi=300, bbox_inches="tight")

def _show_about(context=None):
    messagebox.showinfo("About", "Analysis App\nVersion 1.0")

def _load_new_data(context):
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv")]
    )
    if not file_path:
        return
    
    # Optional: check for metadata JSON with same name
    meta_path = file_path.replace(".csv", ".meta.json")
    if not os.path.exists(meta_path):
        meta_path = None

    try:
        context["data"] = Data(file_path, meta_path)
        # Redraw the current graph with new data
        draw_graph(context["fig"], context["current_graph"], data=context["data"])
        context["canvas"].draw()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data:\n{e}")

# Items
FILE_MENU_ITEMS = [
    {"Load Data...", lambda ctx: _load_new_data(ctx)},
    ("Export as PNG", lambda ctx: _export_png(ctx["fig"])),
    ("Exit", lambda ctx: ctx["root"].quit()),
]

HELP_MENU_ITEMS = [
    ("About", _show_about),
]