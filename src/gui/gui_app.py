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
    HOME_KEY,
    DATA_ANALYSIS_KEY,
    CLUSTERING_KEY,
    TAKE_TEST_KEY,
    RESULTS_KEY,
    ABOUT_KEY,
)


customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("main.py")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create navigation menu
        navigation_menu_items = [
            (HOME_KEY, self.home_button_event),
            (DATA_ANALYSIS_KEY, self.data_analysis_button_event),
            (CLUSTERING_KEY, self.clustering_button_event),
            (TAKE_TEST_KEY, self.take_test_button_event),
            (RESULTS_KEY, self.results_button_event),
            (ABOUT_KEY, self.about_button_event),
        ]
        self.navigation_menu = NavigationMenu(self, navigation_menu_items)
        self.navigation_menu.grid(row=0, column=0, sticky="nsew")

        # create pages
        self.pages = {
            HOME_KEY: HomePage(self),
            DATA_ANALYSIS_KEY: DataAnalysisPage(self),
            CLUSTERING_KEY: ClusteringPage(self),
            TAKE_TEST_KEY: TakeTestPage(self),
            RESULTS_KEY: ResultsPage(self),
            ABOUT_KEY: AboutPage(self),
        }

    def select_page(self, page_key):
        # set button color for selected button
        pass

    def home_button_event(self):
        print("Home button pressed")

    def data_analysis_button_event(self):
        print("Data Analysis button pressed")

    def clustering_button_event(self):
        print("Clustering button pressed")

    def take_test_button_event(self):
        print("Take Test button pressed")

    def results_button_event(self):
        print("Results button pressed")

    def about_button_event(self):
        print("About button pressed")


class NavigationMenu(customtkinter.CTkFrame):
    def __init__(
        self,
        master: any,
        menu_items: list[tuple[str, Callable]],
        menu_title="Navigation Menu",
        **kwargs,
    ):
        kwargs.setdefault("corner_radius", 0)
        super().__init__(
            master,
            **kwargs,
        )
        self.grid_rowconfigure(len(menu_items) + 1, weight=1)

        # create navigation menu heading
        self.navigation_frame_label = customtkinter.CTkLabel(
            self,
            text=menu_title,
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # create navigation menu buttons
        self.menu_buttons = {}
        for i, (item_str, item_command) in enumerate(menu_items):
            menu_button = NavigationMenuButton(
                self,
                text=item_str,
                command=item_command,
            )
            menu_button.grid(row=i + 1, column=0, sticky="ew")
            self.menu_buttons[item_str] = menu_button

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
