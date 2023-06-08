from typing import Callable, Optional, Tuple, Union
import tkinter
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import *
from gui.gui_pages import *
from utils.utils_data import generate_figures
from utils.utils_constants import (
    HOME_PAGE_KEY,
    DATA_PAGE_KEY,
    CLUSTERING_PAGE_KEY,
    TEST_PAGE_KEY,
    RESULTS_PAGE_KEY,
    ABOUT_PAGE_KEY,
)


customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        self.current_page: Page = None
        super().__init__()

        # configure window
        self.title("Big Five Personality Traits")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (2x1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create page title

        # create navigation menu
        navigation_menu_items = [
            # (HOME_PAGE_KEY, self.home_button_event),
            (DATA_PAGE_KEY, self.data_analysis_button_event),
            # (CLUSTERING_PAGE_KEY, self.clustering_button_event),
            (TEST_PAGE_KEY, self.take_test_button_event),
            # (RESULTS_PAGE_KEY, self.results_button_event),
            (ABOUT_PAGE_KEY, self.about_button_event),
        ]
        self.navigation_menu = NavigationMenu(self, navigation_menu_items)
        self.navigation_menu.grid(row=0, column=0, sticky="nsew")

        # create pages
        self.pages: dict[str, Page] = {
            HOME_PAGE_KEY: HomePage(self, navigation_menu_items),
            DATA_PAGE_KEY: DataAnalysisPage(self),
            CLUSTERING_PAGE_KEY: ClusteringPage(self),
            TEST_PAGE_KEY: TakeTestPage(self),
            RESULTS_PAGE_KEY: ResultsPage(self),
            ABOUT_PAGE_KEY: AboutPage(self),
        }

        # select default frame
        self.select_page(DATA_PAGE_KEY)
        # self.page = Page(self)
        # self.page.grid(row=0, column=1, sticky="nsew")

    def get_page(self, page_name):
        return self.pages.get(page_name)

    def select_page(self, page_name):
        if self.current_page is not None:
            # clear current button and forget current page
            current_page_name = self.current_page.get_page_name()
            self.navigation_menu.menu_buttons[current_page_name].configure(
                fg_color="transparent", hover_color=("gray70", "gray30")
            )
            self.pages[current_page_name].grid_forget()

        # set new button colour and show new page
        self.navigation_menu.menu_buttons[page_name].configure(
            fg_color=("#3B8ED0", "#1F6AA5"),
            hover_color=("#3B8ED0", "#1F6AA5")
            # fg_color=("gray75", "gray25")
        )
        self.pages[page_name].grid(row=1, column=0, sticky="nsew")
        self.current_page = self.get_page(page_name)

    def home_button_event(self):
        self.select_page(HOME_PAGE_KEY)

    def data_analysis_button_event(self):
        self.select_page(DATA_PAGE_KEY)

    def clustering_button_event(self):
        self.select_page(CLUSTERING_PAGE_KEY)

    def take_test_button_event(self):
        self.select_page(TEST_PAGE_KEY)

    def results_button_event(self):
        self.select_page(RESULTS_PAGE_KEY)

    def about_button_event(self):
        self.select_page(ABOUT_PAGE_KEY)


class NavigationMenu(customtkinter.CTkFrame):
    def __init__(
        self,
        master: any,
        menu_items: list[tuple[str, Callable]],
        menu_title="Big Five by malgra",
        **kwargs,
    ):
        kwargs.setdefault("corner_radius", 0)
        super().__init__(
            master,
            **kwargs,
        )
        self.grid_columnconfigure(1, weight=1)

        # create navigation menu heading
        self.navigation_frame_label = customtkinter.CTkLabel(
            self,
            text=menu_title,
            font=customtkinter.CTkFont(size=50, weight="normal"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # create navigation menu buttons
        self.menu_buttons: dict[str, NavigationMenuButton] = {}
        for i, (item_str, item_command) in enumerate(menu_items, start=2):
            menu_button = NavigationMenuButton(
                self,
                text=item_str,
                command=item_command,
            )
            menu_button.grid(row=0, column=i, padx=20, pady=20, sticky="ew")
            self.menu_buttons[item_str] = menu_button

    """
        # create navigation menu appearance settings
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(
            row=len(menu_items) + 2, column=0, padx=20, pady=20, sticky="s"
        )

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    """
