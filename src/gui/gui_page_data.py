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
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        # Add sidebar menu options
        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            width=200,
            values=[
                "Select Dataset Size",
                dataset_size_dict.get(SMALL_KEY).get(OPTION_KEY),
                dataset_size_dict.get(MEDIUM_KEY).get(OPTION_KEY),
                dataset_size_dict.get(LARGE_KEY).get(OPTION_KEY),
                dataset_size_dict.get(FULL_KEY).get(OPTION_KEY),
            ],
        )
        self.optionmenu_1.grid(row=1, column=0, padx=50, pady=(10, 10), sticky="ew")

        self.seg_button_1 = customtkinter.CTkSegmentedButton(
            self.sidebar_frame, width=200, values=["Distributions", "Correlations"]
        )
        self.seg_button_1.grid(row=2, column=0, padx=50, pady=(10, 10), sticky="ew")

        self.optionmenu_2 = customtkinter.CTkOptionMenu(
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
        self.optionmenu_2.grid(row=3, column=0, padx=50, pady=(10, 10), sticky="ew")

        self.main_button_1 = customtkinter.CTkButton(
            self.sidebar_frame,
            corner_radius=25,
            height=100,
            border_width=2,
            text="Plot",
            text_color=("gray10", "#DCE4EE"),
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.draw_figure,
        )
        self.main_button_1.grid(
            row=10, column=0, padx=(50, 50), pady=(50, 50), sticky="sew"
        )

        # set default values
        self.optionmenu_1.set("Select Dataset Size")
        self.seg_button_1.set("Distributions")
        self.optionmenu_2.set("Select Trait")

        # draw figures
        self.canvas = self.distribution_figure(self.page_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def distribution_figure(self, master) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_figures()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=master)
        canvas.draw()
        # canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")
        return canvas

    def draw_figure(self):
        print("button pressed")
