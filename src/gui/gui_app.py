from typing import Callable
import tkinter
import customtkinter
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

        # configure grid layout (3x3)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        self.page_title = customtkinter.CTkLabel(
            self,
            text="Main Heading",
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.page_title.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=1, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((0, 2), weight=0)
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        self.sidebar_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Dataset Visualisation",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.sidebar_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.tabview = customtkinter.CTkTabview(
            self.sidebar_frame, width=250, height=600
        )
        self.tabview.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.tabview.add("Data")
        self.tabview.add("Analytics")

        # self.test_button = customtkinter.CTkButton(
        #     self, text="Take Test", command=self.button_callback
        # )
        # self.test_button.grid(row=1, column=2, padx=20, pady=20, sticky="new")

        # Create main display
        self.main_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.main_frame.grid(row=1, column=1, sticky="nsew")
        self.canvas = self.draw_figure(self.main_frame)

    def draw_figure(self, root) -> tkagg.FigureCanvasTkAgg:
        dist_figure = generate_figures()
        canvas = tkagg.FigureCanvasTkAgg(dist_figure, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
        return canvas

    def button_callback(self):
        print("button pressed")

    #     self.show_home_page()

    # def show_home_page(self):
    #     self.hide_current_page()

    #     if "home" not in self.pages:
    #         self.pages["home"] = HomePage(
    #             self.root, self.go_to_personality_test, self.go_to_settings
    #         )

    #     self.current_page = "home"
    #     self.pages["home"].pack()

    # def go_to_personality_test(self):
    #     self.hide_current_page()

    #     if "personality_test" not in self.pages:
    #         self.pages["personality_test"] = PersonalityTestPage(
    #             self.root, self.show_home_page
    #         )

    #     self.current_page = "personality_test"
    #     self.pages["personality_test"].pack()

    # def go_to_settings(self):
    #     self.hide_current_page()

    #     if "settings" not in self.pages:
    #         self.pages["settings"] = SettingsPage(self, self.show_home_page)

    #     self.current_page = "settings"
    #     self.pages["settings"].pack()

    # def hide_current_page(self):
    #     if self.current_page and self.current_page in self.pages:
    #         self.pages[self.current_page].pack_forget()
