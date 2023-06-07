from typing import Callable, Optional, Tuple, Union
import tkinter
import customtkinter
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg

from utils.utils_data import generate_figures


customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.pages = {}  # Dictionary to store instances of each page

        # configure window
        self.title("main.py")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (1x2)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0), weight=1)
        # self.grid_rowconfigure((1, 2), weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(9, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="Navigation Menu",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # create page buttons in navigation frame
        self.sidebar_button_1 = NavigationMenuButton(
            self.navigation_frame,
            text="Home",
            command=self.button_callback,
        )
        self.sidebar_button_1.grid(row=1, column=0, sticky="ew")
        self.sidebar_button_2 = NavigationMenuButton(
            self.navigation_frame,
            text="Data Analysis",
            command=self.button_callback,
        )
        self.sidebar_button_2.grid(row=2, column=0, sticky="ew")
        self.sidebar_button_3 = NavigationMenuButton(
            self.navigation_frame,
            text="Clustering",
            command=self.button_callback,
        )
        self.sidebar_button_3.grid(row=3, column=0, sticky="ew")
        self.sidebar_button_4 = NavigationMenuButton(
            self.navigation_frame,
            text="Take Test",
            command=self.button_callback,
        )
        self.sidebar_button_4.grid(row=4, column=0, sticky="ew")
        self.sidebar_button_5 = NavigationMenuButton(
            self.navigation_frame,
            text="Results",
            command=self.button_callback,
        )
        self.sidebar_button_5.grid(row=5, column=0, sticky="ew")
        self.sidebar_button_6 = NavigationMenuButton(
            self.navigation_frame,
            text="About",
            command=self.button_callback,
        )
        self.sidebar_button_6.grid(row=6, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=10, column=0, padx=20, pady=20, sticky="s")

        # Create main display frame
        self.main_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.canvas = self.draw_figure(self.main_frame)
        self.main_frame_label = customtkinter.CTkLabel(
            self.main_frame,
            text="Main Heading",
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.main_frame_label.grid(row=0, column=0, padx=20, pady=20)

        """
        Create Pages

        self.second_frame = secondFrame(self)


        class secondFrame(customtkinter.CTkFrame)
            def __init__(self):
                super().__init__()
                
        """

    def draw_figure(self, root) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_figures()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")
        return canvas

    def button_callback(self):
        print("button pressed")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


class NavigationMenuButton(customtkinter.CTkButton):
    def __init__(
        self,
        master: any,
        **kwargs,
    ):
        kwargs.setdefault("height", 40)
        kwargs.setdefault("corner_radius", 0)
        kwargs.setdefault("border_spacing", 20)
        kwargs.setdefault("fg_color", "transparent")
        kwargs.setdefault("hover_color", ("gray70", "gray30"))
        kwargs.setdefault("text_color", ("gray10", "gray90"))
        kwargs.setdefault("font", customtkinter.CTkFont(size=20, weight="normal"))
        kwargs.setdefault("anchor", "w")
        super().__init__(
            master,
            **kwargs,
        )
