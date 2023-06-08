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


class TestPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", TEST_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
