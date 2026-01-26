import mplfinance as mpf
from data.data import Data
from charts.graph_defaults import graph_defaults
from charts.graph_utils import ClearGraph, SetLabels


xData=Data.x
yData=Data.y # must be numerical


def DrawGraph(fig, graphType='plot', **kwargs):
    """Draws a graph of type `graphType` on the given figure.
    
    kwargs can override defaults in graph_defaults.
    """
    ax = ClearGraph(fig)
    options = graph_defaults.copy()
    options.update(kwargs)

    if graphType == 'plot':
        DrawLineGraph(ax, xData, yData, options)
    elif graphType == 'bar':
        DrawBarGraph(ax, xData, yData, options)
    elif graphType == 'barh':
        DrawBarhGraph(ax, xData, yData, options)
    elif graphType == 'scatter':
        DrawScatterGraph(ax, xData, yData, options)
    elif graphType == 'fill_between':
        DrawFillBetweenGraph(ax, xData, yData, options)
    elif graphType == 'step':
        DrawStepGraph(ax, xData, yData, options)
    elif graphType == 'errorbar':
        DrawErrorBarGraph(ax, xData, yData, options)
    elif graphType == 'hist':
        DrawHistGraph(ax, yData, options)
    elif graphType == 'boxplot':
        DrawBoxPlotGraph(ax, yData, options)
    elif graphType == 'violinplot':
        DrawViolinPlotGraph(ax, yData, options)
    elif graphType == 'pie':
        DrawPieGraph(ax, yData, options)
    elif graphType == 'candlestick':
        DrawCandlestickGraph(ax, mpf)

    # -----------------------------
    # Average line
    # -----------------------------
    if Data.avg and graphType in {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}:
        ax.axhline(y=Data.avg_val, linestyle='--', color='green', label=Data.avg_label)
    SetLabels(ax, graphType)


def DrawLineGraph(ax, xData, yData, options):
    ax.plot(
        xData, yData,
        color=options['color'],
        linestyle=options['linestyle'],
        linewidth=options['linewidth'],
        marker=options['marker'],
        markersize=options['markersize'],
        markerfacecolor=options['markerfacecolor'],
        markeredgecolor=options['markeredgecolor'],
        alpha=options['alpha'],
        label=options['label']
    )

def DrawBarGraph(ax, xData, yData, options):
    ax.bar(
        xData, yData,
        color=options['color'],
        edgecolor=options['edgecolor'],
        linewidth=options['linewidth'],
        width=options['width'],
        alpha=options['alpha'],
        label=options['label'],
        tick_label=options['tick_label']
    )

def DrawBarhGraph(ax, xData, yData, options):
    ax.barh(
        y=xData, width=yData,
        color=options['color'],
        edgecolor=options['edgecolor'],
        linewidth=options['linewidth'],
        height=options['width'],
        alpha=options['alpha'],
        label=options['label'],
        tick_label=options['tick_label']
    )

def DrawScatterGraph(ax, xData, yData, options):
    ax.scatter(
        xData, yData,
        color=options['color'],
        marker=options['marker'],
        s=options['markersize']**2,
        edgecolors=options['markeredgecolor'],
        alpha=options['alpha'],
        label=options['label']
    )

def DrawFillBetweenGraph(ax, xData, yData, options):
    ax.fill_between(
        xData, yData,
        color=options['color'],
        alpha=options['alpha'],
        label=options['label']
    )

def DrawStepGraph(ax, xData, yData, options):
    ax.step(
        xData, yData,
        color=options['color'],
        linewidth=options['linewidth'],
        label=options['label']
    )

def DrawErrorBarGraph(ax, xData, yData, options):
    ax.errorbar(
        xData, yData,
        yerr=options['yerr'],
        xerr=options['xerr'],
        fmt=options['fmt'],
        color=options['color'],
        linewidth=options['linewidth'],
        markersize=options['markersize'],
        markerfacecolor=options['markerfacecolor'],
        markeredgecolor=options['markeredgecolor'],
        alpha=options['alpha'],
        label=options['label']
    )

def DrawHistGraph(ax, yData, options):
    ax.hist(
        yData,       
        bins=options['bins'],
        color=options['color'],
        edgecolor=options['edgecolor'],
        alpha=options['alpha'],
        label=options['label']
    )

def DrawBoxPlotGraph(ax, yData, options):
    ax.boxplot(
        yData,
        patch_artist=True,
        boxprops=dict(facecolor=options['box_facecolor'], color=options['box_edgecolor']),
        medianprops=dict(color=options['median_color']),
        whiskerprops=dict(color=options['whisker_color']),
        capprops=dict(color=options['cap_color']),
        flierprops=dict(marker=options['flier_marker'], color=options['flier_color'], alpha=options['flier_alpha'])
    )
    ax.set_xticklabels([options['label']])

def DrawViolinPlotGraph(ax, yData, options):
    ax.violinplot(
        yData,
        showmeans=options['violin_showmeans'],
        showmedians=options['violin_showmedians'],
        showextrema=options['violin_showextrema']
    )
    ax.set_xticks([1])
    ax.set_xticklabels([options['label']])

def DrawPieGraph(ax, yData, options):
    ax.pie(
        yData,
        labels=xData,
        colors=options['colors'],
        autopct=options['autopct'],
        startangle=options['startangle'],
        shadow=options['shadow']
    )

def DrawCandlestickGraph(ax, mpf):
    mpf.plot(
        Data.candlestick_df,
        type='candle',
        ax=ax,
        style='classic',
        volume=False,
        show_nontrading=False
    )