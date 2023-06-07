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
        **kwargs,
    ):
        super().__init__(
            master,
            **kwargs,
        )
