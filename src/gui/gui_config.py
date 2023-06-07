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
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.page_frame_label = customtkinter.CTkLabel(
            self,
            text=page_name,
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.page_frame_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.page_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.page_frame.grid(row=1, column=0, sticky="nsew")

    def get_page_name(self):
        return self.page_name

    # def page_frame
