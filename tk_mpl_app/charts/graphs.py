import mplfinance as mpf
from charts.graph_defaults import GRAPH_DEFAULTS
from charts.graph_utils import clear_graph, set_labels
import charts.graph_types as gt


GRAPH_FUNCTIONS = {
    'plot': gt.draw_line_graph,
    'bar': gt.draw_bar_graph,
    'barh': gt.draw_barh_graph,
    'scatter': gt.draw_scatter_graph,
    'fill_between': gt.draw_fill_between_graph,
    'step': gt.draw_step_graph,
    'errorbar': gt.draw_errorbar_graph,
    'hist': gt.draw_hist_graph,
    'boxplot': gt.draw_boxplot_graph,
    'violinplot': gt.draw_violinplot_graph,
    'pie': gt.draw_pie_graph,
    'candlestick': gt.draw_candlestick_graph
}

def get_graph_types():
    return list(GRAPH_FUNCTIONS.keys())

def draw_graph(fig, graph_type='plot', data=None, **kwargs):
    if data is None:
        from data.data import Data
        data = Data("data/candles.csv")  # fallback default

    ax = clear_graph(fig)
    options = GRAPH_DEFAULTS.copy()
    options.update(kwargs)
    # dynamic labels from current data
    options['label'] = data.label
    options['tick_label'] = data.x

    func = GRAPH_FUNCTIONS.get(graph_type)
    if func:
        if graph_type in {'plot', 'bar', 'barh', 'scatter', 'fill_between', 'step', 'errorbar', 'pie'}:
            func(ax, data.x, data.y, options)
        elif graph_type in {'hist', 'boxplot', 'violinplot'}:
            func(ax, data.y, options)
        elif graph_type == 'candlestick':
            func(ax, mpf, data)
    else:
        raise ValueError(f"Unknown graph_type: {graph_type}")

    # -----------------------------
    # Average line
    # -----------------------------
    if data.avg and graph_type in {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}:
        ax.axhline(y=data.avg_val, linestyle='--', color='green', label=data.avg_label)
    set_labels(ax, graph_type, data)
