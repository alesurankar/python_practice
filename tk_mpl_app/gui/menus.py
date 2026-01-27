import os
import tkinter as tk
from tkinter import messagebox, filedialog
from data.data import Data


def create_menus(root, context):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    _build_menu(menubar, "File", FILE_MENU_ITEMS, context)
    _build_menu(menubar, "Help", HELP_MENU_ITEMS, context)


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
    csv_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv")]
    )
    if not csv_path:
        return
    meta_path = csv_path.replace(".csv", ".meta.json")
    if not os.path.exists(meta_path):
        meta_path = None
    context["data"] = Data(csv_path, meta_path)
    context["show_graph"]()


# Items
FILE_MENU_ITEMS = [
    ("Load Data...", lambda ctx: _load_new_data(ctx)),
    ("Export as PNG", lambda ctx: _export_png(ctx["fig"])),
    ("Exit", lambda ctx: ctx["root"].quit()),
]

HELP_MENU_ITEMS = [
    ("About", _show_about),
]