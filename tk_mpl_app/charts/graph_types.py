
def draw_line_graph(ax, x_data, y_data, options):
    ax.plot(
        x_data, y_data,
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

def draw_bar_graph(ax, x_data, y_data, options):
    ax.bar(
        x_data, y_data,
        color=options['color'],
        edgecolor=options['edgecolor'],
        linewidth=options['linewidth'],
        width=options['width'],
        alpha=options['alpha'],
        label=options['label'],
        tick_label=options['tick_label']
    )

def draw_barh_graph(ax, x_data, y_data, options):
    ax.barh(
        y=x_data, width=y_data,
        color=options['color'],
        edgecolor=options['edgecolor'],
        linewidth=options['linewidth'],
        height=options['width'],
        alpha=options['alpha'],
        label=options['label'],
        tick_label=options['tick_label']
    )

def draw_scatter_graph(ax, x_data, y_data, options):
    ax.scatter(
        x_data, y_data,
        color=options['color'],
        marker=options['marker'],
        s=options['markersize']**2,
        edgecolors=options['markeredgecolor'],
        alpha=options['alpha'],
        label=options['label']
    )

def draw_fill_between_graph(ax, x_data, y_data, options):
    ax.fill_between(
        x_data, y_data,
        color=options['color'],
        alpha=options['alpha'],
        label=options['label']
    )

def draw_step_graph(ax, x_data, y_data, options):
    ax.step(
        x_data, y_data,
        color=options['color'],
        linewidth=options['linewidth'],
        label=options['label']
    )

def draw_errorbar_graph(ax, x_data, y_data, options):
    ax.errorbar(
        x_data, y_data,
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

def draw_hist_graph(ax, y_data, options):
    ax.hist(
        y_data,       
        bins=options['bins'],
        color=options['color'],
        edgecolor=options['edgecolor'],
        alpha=options['alpha'],
        label=options['label']
    )

def draw_boxplot_graph(ax, y_data, options):
    ax.boxplot(
        y_data,
        patch_artist=True,
        boxprops=dict(facecolor=options['box_facecolor'], color=options['box_edgecolor']),
        medianprops=dict(color=options['median_color']),
        whiskerprops=dict(color=options['whisker_color']),
        capprops=dict(color=options['cap_color']),
        flierprops=dict(marker=options['flier_marker'], color=options['flier_color'], alpha=options['flier_alpha'])
    )
    ax.set_xticklabels([options['label']])

def draw_violinplot_graph(ax, y_data, options):
    ax.violinplot(
        y_data,
        showmeans=options['violin_showmeans'],
        showmedians=options['violin_showmedians'],
        showextrema=options['violin_showextrema']
    )
    ax.set_xticks([1])
    ax.set_xticklabels([options['label']])

def draw_pie_graph(ax, x_data, y_data, options):
    ax.pie(
        y_data,
        labels=x_data,
        colors=options['colors'],
        autopct=options['autopct'],
        startangle=options['startangle'],
        shadow=options['shadow']
    )

def draw_candlestick_graph(ax, mpf, data):
    mpf.plot(
        data.df,
        type='candle',
        ax=ax,
        style='classic',
        volume=False,
        show_nontrading=False
    )