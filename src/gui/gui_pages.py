from typing import Callable
import customtkinter
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import Page, HomeMenuButton
from utils.utils_data import generate_figures
from utils.utils_constants import (
    HOME_PAGE_KEY,
    DATA_PAGE_KEY,
    CLUSTERING_PAGE_KEY,
    TEST_PAGE_KEY,
    RESULTS_PAGE_KEY,
    ABOUT_PAGE_KEY,
)


class HomePage(Page):
    def __init__(self, master: any, menu_items: list[tuple[str, Callable]], **kwargs):
        kwargs.setdefault("page_name", HOME_PAGE_KEY)
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
            if item_str == ABOUT_PAGE_KEY:
                menu_button.grid(
                    row=row_i, column=col_i, columnspan=2, padx=20, pady=20, sticky="ew"
                )
            else:
                menu_button.grid(row=row_i, column=col_i, padx=20, pady=20, sticky="ew")
            self.menu_buttons[item_str] = menu_button


class DataAnalysisPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", DATA_PAGE_KEY)
        super().__init__(master, **kwargs)

        # Add configuration menu
        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
        # self.sidebar_frame.grid_rowconfigure(2, weight=1)
        # self.sidebar_frame.grid_columnconfigure(0, weight=0)

        self.config_menu_frame = customtkinter.CTkFrame(
            self.sidebar_frame, corner_radius=0, fg_color="transparent"
        )
        self.config_menu_frame.grid(row=1, column=0, sticky="nsew")
        self.config_menu_frame.grid_rowconfigure(6, weight=1)
        self.config_menu_frame.grid_columnconfigure(0, weight=1)

        """
        self.config_menu_label = customtkinter.CTkLabel(
            self.config_menu_frame,
            text="Data Configuration",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.config_menu_label.grid(row=0, column=0, padx=20, pady=20, sticky="new")
        """

        # Add config menu options
        self.optionmenu_1 = customtkinter.CTkOptionMenu(
            self.config_menu_frame,
            width=200,
            values=[
                "Select Dataset Size",
                "Small (n = 100 values)",
                "Medium (n = 2,500 values)",
                "Large (n = 50,000 values)",
                "Full Dataset (n = 1,015,341 values)",
            ],
        )
        self.optionmenu_1.grid(row=1, column=0, padx=50, pady=(10, 10), sticky="ew")

        self.seg_button_1 = customtkinter.CTkSegmentedButton(
            self.config_menu_frame, width=200, values=["Distributions", "Correlations"]
        )
        self.seg_button_1.grid(row=2, column=0, padx=50, pady=(10, 10), sticky="ew")

        self.optionmenu_2 = customtkinter.CTkOptionMenu(
            self.config_menu_frame,
            width=200,
            values=[
                "Select Trait",
                "Agreeableness",
                "Conscientiousness",
                "Extraversion",
                "Neuroticism",
                "Openness",
            ],
        )
        self.optionmenu_2.grid(row=3, column=0, padx=50, pady=(10, 10), sticky="ew")

        self.main_button_1 = customtkinter.CTkButton(
            self.config_menu_frame,
            corner_radius=25,
            height=100,
            border_width=2,
            text="Plot",
            text_color=("gray10", "#DCE4EE"),
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.main_button_1.grid(
            row=10, column=0, padx=(50, 50), pady=(20, 20), sticky="sew"
        )

        # set default values
        self.optionmenu_1.set("Select Dataset Size")
        self.seg_button_1.set("Distributions")
        self.optionmenu_2.set("Select Trait")

        # draw figures
        self.canvas = self.draw_figure(self.page_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def draw_figure(self, master) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_figures()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=master)
        canvas.draw()
        # canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")
        return canvas


class ClusteringPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", CLUSTERING_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)


class TakeTestPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", TEST_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)


class ResultsPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", RESULTS_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)


class AboutPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", ABOUT_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
