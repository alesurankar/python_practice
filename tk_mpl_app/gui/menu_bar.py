import os
import tkinter as tk
from tkinter import messagebox, filedialog
from data.data import Data


class MenuBar:
    """Encapsulates the application menus."""
    def __init__(self, root: tk.Tk, app):
        self.root = root
        self.app = app
        self.menubar = tk.Menu(root)
        self.root.config(menu=self.menubar)

        self._build_menu("File", self._file_menu_items())
        self._build_menu("Help", self._help_menu_items())

    # Internal menu builder
    def _build_menu(self, label: str, items: list[tuple[str, callable]]):
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=label, menu=menu)

        for text, action in items:
            menu.add_command(label=text, command=action)

    # Menu item definitions
    def _file_menu_items(self):
        return [
            ("Load Data...", self._load_new_data),
            ("Export as PNG", self._export_png),
            ("Exit", lambda app: app.root.quit()),
        ]

    def _help_menu_items(self):
        return [
            ("About", self._show_about),
        ]

    # Internal actions
    def _export_png(self, app):
        """Export current graph to PNG"""
        if not app.graph_widget or not hasattr(app.graph_widget, "fig"):
            messagebox.showwarning("Warning", "No graph to export!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")],
            title="Save Graph as PNG"
        )
        if file_path:
            app.graph_widget.fig.savefig(file_path, dpi=300, bbox_inches="tight")
            messagebox.showinfo("Saved", f"Graph saved to:\n{file_path}")

    def _show_about(self):
        messagebox.showinfo("About", "Analysis App\nVersion 1.0")

    def _load_new_data(self, app):
        """Load new CSV data into the App instance."""
        csv_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv")]
        )
        if not csv_path:
            return
        
        meta_path = csv_path.replace(".csv", ".meta.json")
        if not os.path.exists(meta_path):
            meta_path = None
            
        app.data = Data(csv_path, meta_path)

        # Refresh graph
        if hasattr(app, "show_graph") and callable(app.show_graph):
            app.show_graph()
