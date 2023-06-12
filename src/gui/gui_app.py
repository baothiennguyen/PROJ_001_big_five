from typing import Callable, Optional, Tuple, Union
import tkinter
import customtkinter

# from customtkinter.windows.widgets.font import CTkFont
# from customtkinter.windows.widgets.image import CTkImage
# import matplotlib.pyplot as plt
# import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import *
from gui.gui_page_data import *
from gui.gui_page_test import *
from gui.gui_page_about import *
from utils.utils_path import get_root_dir
from utils.utils_constants import (
    DATA_PAGE_KEY,
    TEST_PAGE_KEY,
    ABOUT_PAGE_KEY,
)

root_dir = get_root_dir()

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")

# Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.set_default_color_theme(root_dir + "/src/assets/theme.json")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        self.current_page: Page = None
        super().__init__()

        # configure window
        self.title(APP_TITLE)
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (2x1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create page title

        # create menu bar
        menu_bar_items = [
            (DATA_PAGE_KEY, self.data_button_event),
            (TEST_PAGE_KEY, self.test_button_event),
            (ABOUT_PAGE_KEY, self.about_button_event),
        ]
        self.menu_bar = MenuBar(self, menu_bar_items, menubar_title=MENUBAR_TITLE)
        self.menu_bar.grid(row=0, column=0, sticky="nsew")

        # create pages
        self.pages: dict[str, Page] = {
            DATA_PAGE_KEY: DataPage(self),
            TEST_PAGE_KEY: TestPage(self),
            ABOUT_PAGE_KEY: AboutPage(self),
        }

        # select default frame
        self.select_page(DATA_PAGE_KEY)

    def get_page(self, page_name):
        return self.pages.get(page_name)

    def select_page(self, page_name):
        if self.current_page is not None:
            # clear current button and forget current page
            current_page_name = self.current_page.get_page_name()
            self.menu_bar.menu_buttons[current_page_name].configure(
                fg_color="transparent", hover_color=("gray70", "gray30")
            )
            self.pages[current_page_name].grid_forget()

        # set new button colour and show new page
        self.menu_bar.menu_buttons[page_name].configure(
            fg_color=("#3B8ED0", "#1F6AA5"), hover_color=("#3B8ED0", "#1F6AA5")
        )
        self.pages[page_name].grid(row=1, column=0, sticky="nsew")
        self.current_page = self.get_page(page_name)

    def data_button_event(self):
        self.select_page(DATA_PAGE_KEY)

    def test_button_event(self):
        self.select_page(TEST_PAGE_KEY)

    def about_button_event(self):
        self.select_page(ABOUT_PAGE_KEY)


class MenuBar(customtkinter.CTkFrame):
    def __init__(
        self,
        master: any,
        menu_items: list[tuple[str, Callable]],
        menubar_title="Menu Bar Title",
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
            text=menubar_title,
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
