from typing import Optional, Tuple, Union
import customtkinter


class NavigationMenuButton(customtkinter.CTkButton):
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


class HomeMenuButton(customtkinter.CTkButton):
    def __init__(
        self,
        master: any,
        **kwargs,
    ):
        kwargs.setdefault("height", 40)
        kwargs.setdefault("width", 200)
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


class Page(customtkinter.CTkFrame):
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

    # def page_frame
