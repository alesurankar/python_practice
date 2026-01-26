import mplfinance as mpf
from data.data import Data
from charts.graph_defaults import graph_defaults

# -----------------------------
# Definitions
# -----------------------------
xData=Data.x
yData=Data.y # must be numerical

# -----------------------------
# Graph functions
# -----------------------------
def ClearGraph(fig):
    """Clears the figure and returns a new Axes object."""
    fig.clear()
    return fig.add_subplot(111)

def SetLabels(ax, graphType):
    """Sets title and axis labels for the current graph."""
    ax.set_title(f"{Data.title} ({graphType})")
    ax.set_xlabel(Data.xLabel)
    ax.set_ylabel(Data.yLabel)
    if graphType in {'plot', 'bar', 'barh', 'scatter', 'fill_between', 'step', 'errorbar', 'hist', 'pie'}:
        ax.legend()

def DrawGraph(fig, graphType='plot', **kwargs):
    """Draws a graph of type `graphType` on the given figure.
    
    kwargs can override defaults in graph_defaults.
    """
    ax = ClearGraph(fig)
    options = graph_defaults.copy()
    options.update(kwargs)

    # -----------------------------
    # Graph type handling
    # -----------------------------
    if graphType == 'plot':
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
    elif graphType == 'bar':
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
    elif graphType == 'barh':
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
    elif graphType == 'scatter':
        ax.scatter(
            xData, yData,
            color=options['color'],
            marker=options['marker'],
            s=options['markersize']**2,
            edgecolors=options['markeredgecolor'],
            alpha=options['alpha'],
            label=options['label']
        )
    elif graphType == 'fill_between':
        ax.fill_between(
            xData, yData,
            color=options['color'],
            alpha=options['alpha'],
            label=options['label']
        )
    elif graphType == 'step':
        ax.step(
            xData, yData,
            color=options['color'],
            linewidth=options['linewidth'],
            label=options['label']
        )
    elif graphType == 'errorbar':
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
    elif graphType == 'hist':
        ax.hist(
            yData,       
            bins=options['bins'],
            color=options['color'],
            edgecolor=options['edgecolor'],
            alpha=options['alpha'],
            label=options['label']
        )
    elif graphType == 'boxplot':
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
    elif graphType == 'violinplot':
        ax.violinplot(
            yData,
            showmeans=options['violin_showmeans'],
            showmedians=options['violin_showmedians'],
            showextrema=options['violin_showextrema']
        )
        ax.set_xticks([1])
        ax.set_xticklabels([options['label']])
    elif graphType == 'pie':
        ax.pie(
            yData,
            labels=xData,
            colors=options['colors'],
            autopct=options['autopct'],
            startangle=options['startangle'],
            shadow=options['shadow']
        )
    elif graphType == 'candlestick':
        mpf.plot(
            Data.candlestick_df,
            type='candle',
            ax=ax,
            style='classic',
            volume=False,
            show_nontrading=False
        )

    # -----------------------------
    # Average line
    # -----------------------------
    if Data.avg and graphType in {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}:
        ax.axhline(y=Data.avg_val, linestyle='--', color='green', label=Data.avg_label)
    SetLabels(ax, graphType)