"""
This file contains modular action functions for the GUI. Each function is intended to be
called by buttons or menus via the 'context' dictionary, which holds all shared state 
(e.g., the current graph, figure, data, and UI update functions).

HOW TO USE / EXTEND:

1. Each function receives the `context` object, and optionally other relevant arguments 
   (like `graph_types` for navigation).
2. Functions should **update the relevant state in `context`** and then call 
   `context["update_frame"]()` to redraw the GUI and synchronize the UI.
3. To add new behaviors (e.g., toggling different overlays or settings):
   - Add a new function here following the same pattern.
   - Add a corresponding button/menu item in `gui.py` linking to the new function.

CURRENT FUNCTIONS:

- next_graph(context, graph_types): Move to the next graph in the list.
- prev_graph(context, graph_types): Move to the previous graph in the list.
- toggle_avg(context): Toggle the average line display for graphs that support it.

This pattern keeps `gui.py` clean, making it responsible only for layout, button creation, 
and wiring actions, while all behavior logic lives in this file.
"""


def next_graph(context, graph_types):
    context["current_graph_index"] = (context["current_graph_index"] + 1) % len(graph_types)
    context["update_frame"]()

def prev_graph(context, graph_types):
    context["current_graph_index"] = (context["current_graph_index"] - 1) % len(graph_types)
    context["update_frame"]()

def toggle_avg(context):
    context["data"].avg = not context["data"].avg
    context["update_frame"]()