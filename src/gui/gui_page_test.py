from typing import Callable
import customtkinter
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import *
from utils.utils_constants import *
from utils.utils_data import *
from utils.utils_figures import *


class TestPage(Page):
    """
    Test Page class
    """

    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", TEST_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        menu_items = [
            (TAKE_TEST_FRAME_KEY, self.take_test_button_event),
            (RESULTS_FRAME_KEY, self.see_results_button_event),
        ]

        self.frames: dict[str, Frame] = {
            HOME_FRAME_KEY: HomeFrame(self.page_frame, menu_items=menu_items),
            TAKE_TEST_FRAME_KEY: TestFrame(self.page_frame),
            RESULTS_FRAME_KEY: ResultsFrame(self.page_frame),
        }

        self.select_frame(HOME_FRAME_KEY)

    def get_frame(self, frame_name):
        return self.frames.get(frame_name)

    def select_frame(self, frame_name):
        # if self.current_page is not None:
        # clear current button and forget current page
        # current_page_name = self.current_page.get_page_name()
        # self.menu_bar.menu_buttons[current_page_name].configure(
        #     fg_color="transparent", hover_color=("gray70", "gray30")
        # )
        # self.pages[current_page_name].grid_forget()

        # set new button colour and show new page
        # self.menu_bar.menu_buttons[page_name].configure(
        #     fg_color=("#3B8ED0", "#1F6AA5"), hover_color=("#3B8ED0", "#1F6AA5")
        # )
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
        self.current_frame = self.get_frame(frame_name)

    def take_test_button_event(self):
        self.select_frame(TAKE_TEST_FRAME_KEY)

    def see_results_button_event(self):
        self.select_frame(RESULTS_FRAME_KEY)


class HomeFrame(Frame):
    """
    Home Frame for the Test Page
    """

    def __init__(self, master: any, menu_items: list[tuple[str, Callable]], **kwargs):
        kwargs.setdefault("frame_name", HOME_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 3), weight=1)
        # self.grid_rowconfigure(len(menu_items), weight=2)
        self.grid_columnconfigure((0, 3), weight=1)
        self.menu_buttons: dict[str, MenuButton] = {}
        menu_button_map = [(1, 1), (2, 1)]

        for i, (item_str, item_command) in enumerate(menu_items):
            row_i, col_i = menu_button_map[i]
            menu_button = MenuButton(
                self,
                text=item_str,
                command=item_command,
            )
            # if item_str == ABOUT_PAGE_KEY:
            #     menu_button.grid(
            #         row=row_i, column=col_i, columnspan=2, padx=20, pady=20, sticky="ew"
            #     )
            # else:
            menu_button.grid(row=row_i, column=col_i, padx=20, pady=20, sticky="ew")
            self.menu_buttons[item_str] = menu_button

        self.menu_buttons[RESULTS_FRAME_KEY].configure(
            state="disabled", fg_color="#144870"
        )


class ResultsFrame(Frame):
    """
    Results Frame for the Test Page
    """

    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("frame_name", RESULTS_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = customtkinter.CTkLabel(self, text=self.frame_name)
        self.frame_title.grid(row=0, column=0, sticky="nsew")


class TestFrame(Frame):
    """
    Test Frame for the Test Page
    """

    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("frame_name", TAKE_TEST_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = customtkinter.CTkLabel(self, text=self.frame_name)
        self.frame_title.grid(row=0, column=0, sticky="nsew")

        # Add progress bar
        # Add Question class
        # - prompt
        # - radial buttons
        # - 1,2,3,4,5 labels
        # - agree, neutral, disagree
        # Add back and next buttons


class InstructionsFrame(Frame):
    """
    Instructions Frame for the Test Page
    """

    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("frame_name", INSTRUCTIONS_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = customtkinter.CTkLabel(self, text=self.frame_name)
        self.frame_title.grid(row=0, column=0, sticky="nsew")
