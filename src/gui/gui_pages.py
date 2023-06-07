from typing import Callable
import customtkinter
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import Page, HomeMenuButton
from utils.utils_data import generate_figures
from utils.utils_constants import (
    HOME_KEY,
    DATA_ANALYSIS_KEY,
    CLUSTERING_KEY,
    TAKE_TEST_KEY,
    RESULTS_KEY,
    ABOUT_KEY,
)


class HomePage(Page):
    def __init__(self, master: any, menu_items: list[tuple[str, Callable]], **kwargs):
        kwargs.setdefault("page_name", HOME_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_rowconfigure(len(menu_items), weight=2)
        self.page_frame.grid_columnconfigure((0, 3), weight=1)
        self.menu_buttons: dict[str, HomeMenuButton] = {}
        menu_button_map = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]
        for i, (item_str, item_command) in enumerate(menu_items[1:]):
            row_i, col_i = menu_button_map[i]
            menu_button = HomeMenuButton(
                self.page_frame,
                text=item_str,
                command=item_command,
            )
            if item_str == ABOUT_KEY:
                menu_button.grid(
                    row=row_i, column=col_i, columnspan=2, padx=20, pady=20, sticky="ew"
                )
            else:
                menu_button.grid(row=row_i, column=col_i, padx=20, pady=20, sticky="ew")
            self.menu_buttons[item_str] = menu_button


class DataAnalysisPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", DATA_ANALYSIS_KEY)
        super().__init__(master, **kwargs)

        # Add configuration menu
        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(1, weight=1)

        self.config_menu_frame = customtkinter.CTkFrame(
            self.page_frame, corner_radius=0, fg_color="transparent"
        )
        self.config_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.config_menu_frame.grid_rowconfigure(10, weight=1)

        self.config_menu_label = customtkinter.CTkLabel(
            self.config_menu_frame,
            text="Data Configuration",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.config_menu_label.grid(row=0, column=0, padx=20, pady=20, sticky="new")

        # Add config menu options
        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            self.config_menu_frame,
            width=200,
            values=["100", "1,000", "10,000", "100,000", "Full Dataset"],
        )
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.seg_button_1 = customtkinter.CTkSegmentedButton(
            self.config_menu_frame, width=200, values=["Distributions", "Correlations"]
        )
        self.seg_button_1.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="ew")

        self.optionmenu_2 = customtkinter.CTkOptionMenu(
            self.config_menu_frame,
            width=200,
            values=[
                "Agreeableness",
                "Conscientiousness",
                "Extraversion",
                "Neuroticism",
                "Openness",
            ],
        )
        self.optionmenu_2.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.main_button_1 = customtkinter.CTkButton(
            self.config_menu_frame,
            corner_radius=20,
            height=100,
            border_width=2,
            text="Plot",
            text_color=("gray10", "#DCE4EE"),
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.main_button_1.grid(
            row=4, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # set default values
        self.optionmenu_1.set("Select Dataset Size")
        self.seg_button_1.set("Distributions")
        self.optionmenu_2.set("Select Trait")

        # draw figures
        self.canvas = self.draw_figure(self.page_frame)
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")

    def draw_figure(self, master) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_figures()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=master)
        canvas.draw()
        # canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")
        return canvas


class ClusteringPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", CLUSTERING_KEY)
        super().__init__(master, **kwargs)


class TakeTestPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", TAKE_TEST_KEY)
        super().__init__(master, **kwargs)


class ResultsPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", RESULTS_KEY)
        super().__init__(master, **kwargs)


class AboutPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", ABOUT_KEY)
        super().__init__(master, **kwargs)
