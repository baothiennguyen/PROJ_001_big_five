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
