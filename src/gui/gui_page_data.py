from typing import Callable
import customtkinter
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import Page
from utils.utils_constants import *
from utils.utils_data import *
from utils.utils_figures import *


class DataPage(Page):
    """
    Data Analysis Page class
    """

    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", DATA_PAGE_KEY)
        super().__init__(master, **kwargs)

        # Configure page
        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        # Add sidebar menu options
        # Datasize Option Menu
        self.datasize_optionmenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            width=200,
            values=[
                "Select Dataset Size",
                SMALL_STR_KEY,
                MEDIUM_STR_KEY,
                LARGE_STR_KEY,
                FULL_STR_KEY,
            ],
        )
        self.datasize_optionmenu.grid(
            row=1, column=0, padx=50, pady=(10, 10), sticky="ew"
        )

        # Create Plot Type Tab View
        self.plottype_tabview = customtkinter.CTkTabview(self.sidebar_frame, width=200)
        # , values=[DISTRIBUTIONS_KEY, CORRELATIONS_KEY]
        self.plottype_tabview.grid(row=2, column=0, padx=50, pady=(10, 10), sticky="ew")

        # Create Tabs
        self.plottype_tabview.add(DISTRIBUTIONS_KEY)
        self.plottype_tabview.tab(DISTRIBUTIONS_KEY).grid_columnconfigure(0, weight=1)
        self.plottype_tabview.add(CORRELATIONS_KEY)
        self.plottype_tabview.tab(CORRELATIONS_KEY).grid_columnconfigure(0, weight=1)
        # self.plottype_tabview.add(CLUSTERS_KEY)
        # self.plottype_tabview.tab(CLUSTERS_KEY).grid_columnconfigure(0, weight=1)

        # Create Distributions tab components

        self.checkbox_kdes = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(DISTRIBUTIONS_KEY), text="Show KDE curves"
        )
        self.checkbox_kdes.grid(row=1, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_means = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(DISTRIBUTIONS_KEY),
            text="Show distribution means",
        )
        self.checkbox_means.grid(row=2, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_stds = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(DISTRIBUTIONS_KEY),
            text="Show standard deviations",
        )
        self.checkbox_stds.grid(row=3, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_stats = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(DISTRIBUTIONS_KEY),
            text="Show distribution statistics",
        )
        self.checkbox_stats.grid(row=4, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_ylims = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(DISTRIBUTIONS_KEY),
            text="Set constant y-axis limits",
        )
        self.checkbox_ylims.grid(row=5, column=0, padx=10, pady=(20, 20), sticky="w")

        # Create Correlations tab components
        # Trait Options Menu
        self.checkbox_1 = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(CORRELATIONS_KEY), text=AGR_KEY
        )
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(CORRELATIONS_KEY), text=CSN_KEY
        )
        self.checkbox_2.grid(row=2, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(CORRELATIONS_KEY), text=OPN_KEY
        )
        self.checkbox_3.grid(row=3, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_4 = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(CORRELATIONS_KEY), text=EXT_KEY
        )
        self.checkbox_4.grid(row=4, column=0, padx=10, pady=(20, 0), sticky="w")
        self.checkbox_5 = customtkinter.CTkCheckBox(
            master=self.plottype_tabview.tab(CORRELATIONS_KEY), text=EST_KEY
        )
        self.checkbox_5.grid(row=5, column=0, padx=10, pady=(20, 20), sticky="w")

        # Re-sample button
        self.resample_button = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=25,
            height=80,
            border_width=2,
            text="Re-sample",
            text_color=("gray10", "#DCE4EE"),
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.resample_dataset,
        )
        self.resample_button.grid(
            row=11, column=0, padx=(50, 50), pady=(0, 50), sticky="sew"
        )

        # Plot button
        self.plot_button = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=25,
            height=80,
            border_width=2,
            text="Plot",
            text_color=("gray10", "#DCE4EE"),
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.draw_figure,
        )
        self.plot_button.grid(
            row=12, column=0, padx=(50, 50), pady=(0, 50), sticky="sew"
        )

        # set default values
        self.datasize_optionmenu.set("Select Dataset Size")
        self.plottype_tabview.set(DISTRIBUTIONS_KEY)
        self.checkbox_kdes.select()
        self.checkbox_1.select()
        self.checkbox_2.select()
        self.checkbox_3.select()
        self.checkbox_4.select()
        self.checkbox_5.select()

    def resample_dataset(self):
        # get relevant parameters from GUI widgets
        data_size_str = self.datasize_optionmenu.get()
        size_key = dataset_str_dict.get(data_size_str)
        print(f"Resample button pressed: Resampling {size_key} dataset.")

        if data_size_str == "Select Dataset Size":
            print("Select Dataset Size to resample.")
            return

        elif size_key == FULL_KEY:
            print("Cannot resample the full dataset.")
            return

        else:
            print(f"{sample_from_map_dict.get(size_key)}")
            dataset_df = get_dataset(sample_from_map_dict.get(size_key))
            sample_dataset(dataset_df, size_key)
            self.draw_figure()

    def draw_figure(self):
        # get relevant parameters from GUI widgets
        data_size_str = self.datasize_optionmenu.get()
        plot_type = self.plottype_tabview.get()
        size_key = dataset_str_dict.get(data_size_str)
        print(f"Plot button pressed: {data_size_str}, {plot_type}")

        if data_size_str == "Select Dataset Size":
            print("Select Dataset Size to plot.")
            return

        total_scores = calculate_scores(size_key)

        if plot_type == DISTRIBUTIONS_KEY:
            plot_figure = generate_distributions_figure(
                total_scores,
                kdes=self.checkbox_kdes.get(),
                means=self.checkbox_means.get(),
                stds=self.checkbox_stds.get(),
                stats=self.checkbox_stats.get(),
                ylims=self.checkbox_ylims.get(),
            )

        elif plot_type == CORRELATIONS_KEY:
            plot_figure = generate_correlations_figure(
                total_scores,
                vars_bool=[
                    self.checkbox_1.get(),
                    self.checkbox_2.get(),
                    self.checkbox_3.get(),
                    self.checkbox_4.get(),
                    self.checkbox_5.get(),
                ],
            )

        self.canvas = tkagg.FigureCanvasTkAgg(plot_figure, master=self.page_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


# def get_distribution_fig():
