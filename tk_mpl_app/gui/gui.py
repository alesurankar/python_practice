from graphs.graphs import get_graph_types
from gui.navigation import make_navigation_buttons
from gui.menus import create_menus
from gui.actions import toggle_avg, next_graph, prev_graph
from gui.graph_widget import GraphWidget


def create_gui(root):
    context = {"root": root}

    # Navigation buttons
    button_config = [
        {"text": "Previous", "command": lambda: prev_graph(context, get_graph_types()), "side": "left"},
        {"text": "Toggle Avg", "command": lambda: toggle_avg(context), "side": "left"},
        {"text": "Next", "command": lambda: next_graph(context, get_graph_types()), "side": "right"},
    ]
    buttons = make_navigation_buttons(root, button_config)
    context["avg_button"] = buttons["Toggle Avg"]

    # Graph widget
    graph_widget = GraphWidget(root, context)

    # Menus
    create_menus(root, context)

    return graph_widget.fig, graph_widget.canvas