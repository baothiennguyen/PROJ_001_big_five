from typing import Callable
import customtkinter
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import Page, HomeMenuButton
from utils.utils_data import *
from utils.utils_constants import *

# from utils.utils_constants import (
#     HOME_PAGE_KEY,
#     DATA_PAGE_KEY,
#     CLUSTERING_PAGE_KEY,
#     TEST_PAGE_KEY,
#     RESULTS_PAGE_KEY,
#     ABOUT_PAGE_KEY,
# )


class DataPage(Page):
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

        # Plot Type Segmented Button
        self.plottype_segbutton = customtkinter.CTkSegmentedButton(
            self.sidebar_frame, width=200, values=[DISTRIBUTIONS_KEY, CORRELATIONS_KEY]
        )
        self.plottype_segbutton.grid(
            row=2, column=0, padx=50, pady=(10, 10), sticky="ew"
        )

        # Trait Option Menu
        self.trait_optionmenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            width=200,
            values=[
                "Select Trait",
                EXT_KEY,
                EST_KEY,
                AGR_KEY,
                CSN_KEY,
                OPN_KEY,
            ],
        )
        self.trait_optionmenu.grid(row=3, column=0, padx=50, pady=(10, 10), sticky="ew")

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
            row=11, column=0, padx=(50, 50), pady=25, sticky="sew"
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
            row=12, column=0, padx=(50, 50), pady=(25, 50), sticky="sew"
        )

        # set default values
        self.datasize_optionmenu.set("Select Dataset Size")
        self.plottype_segbutton.set(DISTRIBUTIONS_KEY)
        self.trait_optionmenu.set("Select Trait")

        # self.plot_button.configure(state="disabled")

        # self.select = False
        # while not self.select:
        #     if self.datasize_optionmenu.get() == "Select Dataset Size":
        #         self.plot_button.configure(state="disabled")
        #     else:
        #         self.plot_button.configure(state="normal")
        #         self.select = True

        # draw figures
        # self.canvas = self.distribution_figure(self.page_frame)
        # self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def resample_dataset(self):
        # get relevant parameters from GUI widgets
        data_size_str = self.datasize_optionmenu.get()
        # plot_type = self.plottype_segbutton.get()
        # trait_select = self.trait_optionmenu.get()
        size_key = dataset_str_dict.get(data_size_str)

        if data_size_str == "Select Dataset Size":
            print("Select Dataset Size to resample.")
            return

        dataset_df = load_dataset()
        sample_dataset(dataset_df, size_key)
        self.draw_figure()

    def draw_figure(self):
        # Display loading status
        self.plot_button.configure(text="Loading...", require_redraw=True)
        self.progressbar.start()

        # get relevant parameters from GUI widgets
        data_size_str = self.datasize_optionmenu.get()
        plot_type = self.plottype_segbutton.get()
        trait_select = self.trait_optionmenu.get()
        print(f"button pressed: {data_size_str}, {plot_type}, {trait_select}")

        if data_size_str == "Select Dataset Size":
            print("Select Dataset Size to plot.")
            self.plot_button.configure(text="Plot")
            self.progressbar.stop()
            return

        size_key = dataset_str_dict.get(data_size_str)
        dataset = load_dataset(size_key)

        total_scores = calculate_scores(dataset)

        if plot_type == DISTRIBUTIONS_KEY:
            plot_figure = generate_distributions_figure(total_scores)
        else:
            print("Correlations not yet implemented :(")
            self.plot_button.configure(text="Plot")
            return

        self.canvas = tkagg.FigureCanvasTkAgg(plot_figure, master=self.page_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        self.plot_button.configure(text="Plot")
        self.progressbar.stop()

    def distribution_figure(self, master) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_distributions_figure()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=master)
        canvas.draw()
        # canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")
        return canvas
