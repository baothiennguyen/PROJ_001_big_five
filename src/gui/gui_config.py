from typing import Optional, Tuple, Union
import customtkinter


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


class Page(customtkinter.CTkFrame):
    def __init__(
        self,
        master: any,
        page_title="Page Title",
        **kwargs,
    ):
        kwargs.setdefault("corner_radius", 0)
        kwargs.setdefault("fg_color", "transparent")
        super().__init__(
            master,
            **kwargs,
        )
        self.page_frame_label = customtkinter.CTkLabel(
            self,
            text=page_title,
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.page_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.page_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.page_frame.grid(row=0, column=1, sticky="nsew")
        self.page_frame.grid_rowconfigure(1, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
