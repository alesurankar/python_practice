from data.data import Data

def clear_graph(fig):
    """Clears the figure and returns a new Axes object."""
    fig.clear()
    return fig.add_subplot(111)

def set_labels(ax, graph_type, data):
    """Sets title and axis labels for the current graph."""
    ax.set_title(f"{data.title} ({graph_type})")
    ax.set_xlabel(data.x_label)
    ax.set_ylabel(data.y_label)
    if graph_type in {'plot', 'bar', 'barh', 'scatter', 'fill_between', 'step', 'errorbar', 'hist', 'pie'}:
        ax.legend()