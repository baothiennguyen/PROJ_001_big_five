from typing import Literal

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import utils.utils_constants as constants


def generate_distributions_figure(
    total_scores,
    kdes: Literal[True, False] = True,
    means: Literal[True, False] = True,
    stds: Literal[True, False] = True,
    stats: Literal[True, False] = True,
    ylims: Literal[True, False] = True,
):
    """
    Creates Distributions figure
    Parameters:
    - total_scores:     dataframe of total scores to by plotted

    Configuration Parameters
    - kdes:     bool for showing the kernel density estimate (KDE) for each plot
    - means:    bool for showing the distribution's mean for each plot
    - stds:     bool for showing the distribution's standard deviation for each
                plot
    - stats:    bool for showing the distribution's numerical values for mean
                and standard deviation for each plot
    - ylims:    bool for setting each plot to have the same y-axis
    """

    sns.set_theme(
        style="dark",
        rc={
            "text.color": "white",
            "axes.labelcolor": "white",
            "axes.facecolor": "slategrey",
            "patch.edgecolor": "lightgrey",
            "figure.facecolor": "#242424",
            "xtick.color": "white",
            "ytick.color": "white",
        },
    )

    palette = sns.color_palette("bright")

    fig = plt.figure(layout="tight")
    ax_dict = fig.subplot_mosaic(
        [
            [
                constants.AGR_KEY,
                constants.AGR_KEY,
                constants.CSN_KEY,
                constants.CSN_KEY,
                constants.OPN_KEY,
                constants.OPN_KEY,
            ],
            [
                ".",
                constants.EXT_KEY,
                constants.EXT_KEY,
                constants.EST_KEY,
                constants.EST_KEY,
                ".",
            ],
        ],
    )
    for i, trait_key in enumerate(constants.TRAITS_LIST):
        sns.histplot(
            total_scores[trait_key],
            binwidth=constants.NORM_FACTOR,
            kde=kdes,
            kde_kws={"bw_adjust": 2, "clip": (0, 100)},
            ax=ax_dict[trait_key],
            color=palette[i],
        )
        ax_dict[trait_key].set(xlim=(0, 100))
        ax_dict[trait_key].set_title(
            f"Distribution of {trait_key}", fontdict={"fontsize": 18}
        )
        ax_dict[trait_key].set_xlabel(f"Total Scores for {trait_key}")
        ax_dict[trait_key].set_ylabel("Frequency")

        mean = np.mean(total_scores[trait_key])
        std = np.std(total_scores[trait_key])
        max_y = len(total_scores[trait_key]) // 16

        if means:
            ax_dict[trait_key].axvline(
                x=mean, color="black", linestyle="solid", linewidth=3
            )
        if stds:
            ax_dict[trait_key].axvline(
                x=mean - std,
                color="white",
                linestyle="dashed",
                linewidth=1.5,
            )
            ax_dict[trait_key].axvline(
                x=mean + std,
                color="white",
                linestyle="dashed",
                linewidth=1.5,
            )
        if stats:
            x_text = 3.25
            ax_dict[trait_key].text(
                x_text,
                max_y / 50,
                f"Mean Score = {np.round(mean, 2)},   "
                + f"Standard Deviation = {np.round(std, 2)}",
            )
        if ylims:
            ax_dict[trait_key].set(ylim=(0, max_y))

    plt.close()

    return fig


def generate_correlations_figure(
    total_scores, vars_bool: list = [True, True, True, True, True]
):
    """
    Creates Correlations figure
    Parameters:
    - total_scores:     dataframe of total scores to by plotted

    Configuration Parameters
    - vars_bool:        list of bools corresponding to each of the traits to show
    """
    vars_list = [
        trait for (trait, v_bool) in zip(constants.TRAITS_LIST, vars_bool) if v_bool
    ]

    sns.set_theme(
        style="dark",
        rc={
            "text.color": "white",
            "axes.labelcolor": "white",
            "axes.facecolor": "white",
            "patch.edgecolor": "lightgrey",
            "figure.facecolor": "#242424",
            "xtick.color": "white",
            "ytick.color": "white",
        },
    )

    # palette = sns.color_palette("bright")

    # fig = plt.figure(layout="tight")
    # fig, axis = plt.subplots(1, 1)
    grid = sns.pairplot(
        total_scores,
        x_vars=vars_list,
        y_vars=vars_list,
        kind="hist",
        dropna=True,
        plot_kws={"binwidth": constants.NORM_FACTOR},
        diag_kws={"binwidth": constants.NORM_FACTOR},
    )

    # grid.map_offdiag(sns.kdeplot, levels=4, color=".2")
    # grid.map_offdiag(sns.regplot)
    grid.set(xlim=(0, 100), ylim=(0, 100))
    plt.tight_layout()
    plt.close()
    return grid.figure
