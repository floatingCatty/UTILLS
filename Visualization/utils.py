import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def show_values_on_bars(axs, h_v="v", space=0.4):
    def _show_on_single_plot(ax):
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif h_v == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height()
                value = int(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)

def barPlot(w, h, data, x1, x2, y1, y2, title, label_x, label_y, invert_x=False, x_rotation=False, style='whitegrid', save=False):
    sns.set(style=style)
    _, ax = plt.subplots(figsize=(w, h))

    if x_rotation:
        plt.xticks(rotation=40)

    ax.set_title(title=title, fontsize=16)

    sns.set_color_codes("pastel")
    sns.barplot(x=x1, y=y1, data=data, color='b', label='Submitted', ax=ax)
    # show_values_on_bars(g, 'v')
    sns.set_color_codes("muted")
    sns.barplot(x=x2, y=y2, data=data, color='b', label='Admitted', ax=ax)

    ax.legend(ncol=2, loc="upper left", fontsize='large', frameon=True)

    if invert_x:
        ax.invert_xaxis()
    ax.set_xlabel(label_x, fontsize=14)
    ax.set_ylabel(label_y, fontsize=14)

    plt.show()

    if save:
        scatter_fig = ax.get_figure()
        scatter_fig.savefig('img', dpi=400)

    return ax