
def next_graph(context, graph_types):
    context["current_graph_index"] = (context["current_graph_index"] + 1) % len(graph_types)
    context["update_frame"]()

def prev_graph(context, graph_types):
    context["current_graph_index"] = (context["current_graph_index"] - 1) % len(graph_types)
    context["update_frame"]()

def toggle_avg(context):
    context["data"].avg = not context["data"].avg
    context["update_frame"]()