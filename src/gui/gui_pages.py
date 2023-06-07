import customtkinter
import matplotlib.backends.backend_tkagg as tkagg

from gui.gui_config import Page
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
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", HOME_KEY)
        super().__init__(master, **kwargs)
        # self.grid(row=0, column=1, sticky="nsew")


class DataAnalysisPage(Page):
    def __init__(self, master: any, **kwargs):
        kwargs.setdefault("page_name", DATA_ANALYSIS_KEY)
        super().__init__(master, **kwargs)

        self.canvas = self.draw_figure(self)

    def draw_figure(self, master) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_figures()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=master)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")
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
