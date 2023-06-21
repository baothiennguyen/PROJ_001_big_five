import tkinter

import customtkinter


class Page(customtkinter.CTkFrame):
    """
    Page class as template for all pages in the application
    Sets defaults that can easily be adjusted
    """

    def __init__(
        self,
        master: any,
        page_name="Page Name",
        **kwargs,
    ):
        kwargs.setdefault("corner_radius", 0)
        kwargs.setdefault("fg_color", "transparent")
        self.page_name = page_name
        super().__init__(
            master,
            **kwargs,
        )
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create Page Sidebar
        self.sidebar_frame = customtkinter.CTkFrame(
            self,
            width=1000,
            corner_radius=0,
            fg_color="gray20",  # fg_color="transparent"
        )
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # Create Page Title
        self.page_title = customtkinter.CTkLabel(
            self.sidebar_frame,
            width=300,
            text=page_name,
            font=customtkinter.CTkFont(size=40, weight="bold"),
            anchor="center",
        )
        self.page_title.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # Create Page Frame
        self.page_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.page_frame.grid(row=0, column=1, sticky="nsew")
        self.page_frame.grid_rowconfigure(0, weight=1)

        # Create Page Progress Bar
        self.progressbar = customtkinter.CTkProgressBar(
            self.page_frame, mode="indeterminate"
        )
        self.progressbar.grid(
            row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew"
        )

    def get_page_name(self):
        return self.page_name


class Frame(customtkinter.CTkFrame):
    """
    Frame class as template for all frames in a Page
    Sets defaults that can easily be adjusted
    """

    def __init__(
        self,
        master: any,
        frame_name="Frame Name",
        **kwargs,
    ):
        kwargs.setdefault("corner_radius", 0)
        kwargs.setdefault("fg_color", "transparent")
        self.frame_name = frame_name
        super().__init__(
            master,
            **kwargs,
        )

    def get_frame_name(self):
        return self.frame_name


class NavigationMenuButton(customtkinter.CTkButton):
    """
    Navigation button class for the Navigation Bar in the Menu Bar
    Sets defaults that can easily be adjusted
    """

    def __init__(
        self,
        master: any,
        **kwargs,
    ):
        kwargs.setdefault("height", 40)
        kwargs.setdefault("corner_radius", 20)
        kwargs.setdefault("border_spacing", 10)
        kwargs.setdefault("fg_color", "transparent")
        kwargs.setdefault("hover_color", ("gray70", "gray30"))
        kwargs.setdefault("text_color", ("gray10", "gray90"))
        kwargs.setdefault("font", customtkinter.CTkFont(size=20, weight="normal"))
        kwargs.setdefault("anchor", "center")
        super().__init__(
            master,
            **kwargs,
        )


class MenuButton(customtkinter.CTkButton):
    """
    Menu button class for pages with a start page
    Sets defaults that can easily be adjusted
    """

    def __init__(
        self,
        master: any,
        **kwargs,
    ):
        kwargs.setdefault("height", 80)
        kwargs.setdefault("width", 500)
        kwargs.setdefault("corner_radius", 20)
        kwargs.setdefault("border_spacing", 20)
        # kwargs.setdefault("fg_color", "transparent")
        # kwargs.setdefault("hover_color", ("gray70", "gray30"))
        # kwargs.setdefault("text_color", ("gray10", "gray90"))
        kwargs.setdefault("font", customtkinter.CTkFont(size=40, weight="normal"))
        # kwargs.setdefault("anchor", "w")
        super().__init__(
            master,
            **kwargs,
        )


class NavButton(customtkinter.CTkButton):
    """
    Menu button class for pages with a start page
    Sets defaults that can easily be adjusted
    """

    def __init__(
        self,
        master: any,
        **kwargs,
    ):
        kwargs.setdefault("height", 40)
        kwargs.setdefault("width", 100)
        kwargs.setdefault("corner_radius", 20)
        kwargs.setdefault("border_spacing", 20)
        # kwargs.setdefault("fg_color", "transparent")
        # kwargs.setdefault("hover_color", ("gray70", "gray30"))
        # kwargs.setdefault("text_color", ("gray10", "gray90"))
        kwargs.setdefault("font", customtkinter.CTkFont(size=20, weight="normal"))
        # kwargs.setdefault("anchor", "w")
        super().__init__(
            master,
            **kwargs,
        )


class Question(customtkinter.CTkFrame):
    """
    Question class for Test page
    """

    def __init__(
        self,
        master: any,
        prompt: str = "default prompt",
        **kwargs,
    ):
        super().__init__(
            master,
            **kwargs,
        )
        # create radiobutton frame
        self.grid_rowconfigure(8, weight=1)
        self.grid_columnconfigure((0, 2, 4, 6, 8, 10), weight=1)
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(
            row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(
            master=self.radiobutton_frame, text=prompt
        )
        self.label_radio_group.grid(
            row=0, column=0, columnspan=10, padx=10, pady=10, sticky="nsew"
        )
        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=0
        )
        self.radio_button_1.grid(row=1, column=1, pady=10, padx=20, sticky="new")
        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=1
        )
        self.radio_button_2.grid(row=1, column=3, pady=10, padx=20, sticky="new")
        self.radio_button_3 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=2
        )
        self.radio_button_3.grid(row=1, column=5, pady=10, padx=20, sticky="new")
        self.radio_button_4 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=3
        )
        self.radio_button_4.grid(row=1, column=7, pady=10, padx=20, sticky="new")
        self.radio_button_5 = customtkinter.CTkRadioButton(
            master=self.radiobutton_frame, variable=self.radio_var, value=4
        )
        self.radio_button_5.grid(row=1, column=9, pady=10, padx=20, sticky="new")
