from data.data import Data

graph_defaults = {
    # General
    'color': 'blue',
    'edgecolor': 'black',
    'linewidth': 2,
    'linestyle': '-',
    'alpha': 0.8,
    'label': Data.label,
    # Marker options (line/scatter/errorbar)
    'marker': 'o',
    'markersize': 6,
    'markerfacecolor': 'orange',
    'markeredgecolor': 'black',
    # Bar options
    'width': 0.8,
    'tick_label': Data.x,
    # Errorbar
    'yerr': None,
    'xerr': None,
    'fmt': 'o',
    # Histogram
    'bins': 10,
    # Boxplot
    'box_facecolor': 'lightblue',
    'box_edgecolor': 'black',
    'median_color': 'black',
    'whisker_color': 'black',
    'cap_color': 'black',
    'flier_marker': 'o',
    'flier_color': 'red',
    'flier_alpha': 0.5,
    # Violinplot
    'violin_showmeans': True,
    'violin_showmedians': True,
    'violin_showextrema': True,
    # Pie
    'colors': None,
    'autopct': '%1.1f%%',
    'startangle': 90,
    'shadow': False
}