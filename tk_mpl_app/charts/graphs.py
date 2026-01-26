import mplfinance as mpf
from data.data import Data
from charts.graph_defaults import GRAPH_DEFAULTS
from charts.graph_utils import ClearGraph, SetLabels
import charts.graph_types as gt


xData=Data.x
yData=Data.y # must be numerical

GRAPH_FUNCTIONS = {
    'plot': gt.DrawLineGraph,
    'bar': gt.DrawBarGraph,
    'barh': gt.DrawBarhGraph,
    'scatter': gt.DrawScatterGraph,
    'fill_between': gt.DrawFillBetweenGraph,
    'step': gt.DrawStepGraph,
    'errorbar': gt.DrawErrorBarGraph,
    'hist': gt.DrawHistGraph,
    'boxplot': gt.DrawBoxPlotGraph,
    'violinplot': gt.DrawViolinPlotGraph,
    'pie': gt.DrawPieGraph,
    'candlestick': gt.DrawCandlestickGraph
}

def GetGraphTypes():
    return list(GRAPH_FUNCTIONS.keys())

def DrawGraph(fig, graphType='plot', **kwargs):
    """Draws a graph of type `graphType` on the given figure.
    kwargs can override defaults in graph_defaults.
    """
    ax = ClearGraph(fig)
    options = GRAPH_DEFAULTS.copy()
    options.update(kwargs)

    func = GRAPH_FUNCTIONS.get(graphType)
    if func:
        if graphType in {'plot', 'bar', 'barh', 'scatter', 'fill_between', 'step', 'errorbar', 'pie'}:
            func(ax, xData, yData, options)
        elif graphType in {'hist', 'boxplot', 'violinplot'}:
            func(ax, yData, options)
        elif graphType == 'candlestick':
            func(ax, mpf)
    else:
        raise ValueError(f"Unknown graphType: {graphType}")

    # -----------------------------
    # Average line
    # -----------------------------
    if Data.avg and graphType in {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}:
        ax.axhline(y=Data.avg_val, linestyle='--', color='green', label=Data.avg_label)
    SetLabels(ax, graphType)
