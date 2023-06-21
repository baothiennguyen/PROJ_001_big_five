from typing import Any, Callable

import customtkinter

import utils.utils_constants as constants
from gui.gui_config import Frame, MenuButton, NavButton, Page, Question


class TestPage(Page):
    """
    Test Page class
    """

    def __init__(self, master: Any, **kwargs):
        self.current_frame: Frame = None
        kwargs.setdefault("page_name", constants.TEST_PAGE_KEY)
        super().__init__(master, **kwargs)

        self.page_frame.grid_rowconfigure(0, weight=1)
        self.page_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        menu_items = [
            (constants.QUESTIONS_FRAME_KEY, self.take_test_button_event),
            (constants.RESULTS_FRAME_KEY, self.see_results_button_event),
        ]

        self.frames: dict[str, Frame] = {
            constants.HOME_FRAME_KEY: HomeFrame(self.page_frame, menu_items=menu_items)
        }
        self.frames.update(
            {
                constants.QUESTIONS_FRAME_KEY
                + f"_{i}": QuestionsFrame(
                    self.page_frame,
                    page_num=i,
                    frame_name=constants.QUESTIONS_FRAME_KEY + f"_{i}",
                )
                for i in range(10)
            }
        )

        # {
        #     constants.HOME_FRAME_KEY: HomeFrame(self.page_frame, menu_items=menu_items),
        #     constants.QUESTIONS_FRAME_KEY: QuestionsFrame(self.page_frame),
        #     constants.RESULTS_FRAME_KEY: ResultsFrame(self.page_frame),
        # }
        self.frames[constants.HOME_FRAME_KEY] = HomeFrame(
            self.page_frame, menu_items=menu_items
        )
        self.frames[constants.RESULTS_FRAME_KEY] = ResultsFrame(self.page_frame)

        for frame in self.frames.values():
            if isinstance(frame, QuestionsFrame):
                page_num = frame.get_page_num()
                if page_num + 1 in range(10):
                    nextpage = self.frames.get(
                        constants.QUESTIONS_FRAME_KEY + f"_{page_num + 1}"
                    )
                else:
                    nextpage = self.frames.get(constants.HOME_FRAME_KEY)

                if page_num - 1 in range(10):
                    prevpage = self.frames.get(
                        constants.QUESTIONS_FRAME_KEY + f"_{page_num - 1}"
                    )
                else:
                    prevpage = self.frames.get(constants.HOME_FRAME_KEY)

                print(prevpage.get_frame_name())
                print(frame.get_frame_name())
                print(nextpage.get_frame_name())
                print()
                frame.set_nextpage(nextpage)
                frame.set_prevpage(prevpage)

        self.select_frame(constants.HOME_FRAME_KEY)

    def get_frame(self, frame_name):
        return self.frames.get(frame_name)

    def select_frame(self, frame_name):
        print(frame_name)
        if self.current_frame:
            # clear current button and forget current page
            current_frame_name = self.current_frame.get_frame_name()

            self.frames[current_frame_name].grid_forget()

        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
        self.current_frame = self.get_frame(frame_name)

    def take_test_button_event(self):
        self.select_frame(constants.QUESTIONS_FRAME_KEY + "_0")

    def see_results_button_event(self):
        self.select_frame(constants.RESULTS_FRAME_KEY)


class HomeFrame(Frame):
    """
    Home Frame for the Test Page
    """

    def __init__(self, master: Any, menu_items: list[tuple[str, Callable]], **kwargs):
        kwargs.setdefault("frame_name", constants.HOME_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 3), weight=1)
        # self.grid_rowconfigure(len(menu_items), weight=2)
        self.grid_columnconfigure((0, 3), weight=1)
        self.menu_buttons: dict[str, MenuButton] = {}
        menu_button_map = [(1, 1), (2, 1)]

        for i, (item_str, item_command) in enumerate(menu_items):
            row_i, col_i = menu_button_map[i]
            menu_button = MenuButton(
                self,
                text=item_str,
                command=item_command,
            )
            # if item_str == ABOUT_PAGE_KEY:
            #     menu_button.grid(
            #         row=row_i, column=col_i, columnspan=2, padx=20, pady=20, sticky="ew"
            #     )
            # else:
            menu_button.grid(row=row_i, column=col_i, padx=20, pady=20, sticky="ew")
            self.menu_buttons[item_str] = menu_button

        self.menu_buttons[constants.RESULTS_FRAME_KEY].configure(
            state="disabled", fg_color="#144870"
        )


class ResultsFrame(Frame):
    """
    Results Frame for the Test Page
    """

    def __init__(self, master: Any, **kwargs):
        kwargs.setdefault("frame_name", constants.RESULTS_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = customtkinter.CTkLabel(self, text=self.frame_name)
        self.frame_title.grid(row=0, column=0, sticky="nsew")


class QuestionsFrame(Frame):
    """
    Test Frame for the Test Page
    """

    def __init__(
        self,
        master: TestPage,
        page_num: int,
        questions: dict[str, str] = None,
        nextpage: Frame = None,
        prevpage: Frame = None,
        **kwargs,
    ):
        kwargs.setdefault("frame_name", constants.QUESTIONS_FRAME_KEY)
        super().__init__(master, **kwargs)
        self._page_num = page_num
        self._questions = questions
        self._nextpage = nextpage
        self._prevpage = prevpage

        self.grid_rowconfigure(10, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.frame_title = customtkinter.CTkLabel(self, text=self.frame_name)
        self.frame_title.grid(row=0, column=0, sticky="nsew")

        self.back_button = NavButton(
            self,
            text=constants.BACK_FRAME_KEY,
            command=self.back_button_event,
        )
        self.back_button.grid(row=11, column=0, padx=20, pady=20, sticky="ew")

        self.next_button = NavButton(
            self,
            text=constants.NEXT_FRAME_KEY,
            command=self.next_button_event,
        )
        self.next_button.grid(row=11, column=2, padx=20, pady=20, sticky="ew")

        for i in range(1, 6):
            self.question = Question(self)
            self.question.grid(row=i, column=0, columnspan=10, sticky="nsew")
        # Add progress bar
        # Add Question class
        # - prompt
        # - radial buttons
        # - 1,2,3,4,5 labels
        # - agree, neutral, disagree
        # Add back and next buttons

    def next_button_event(self):
        print("nextpage button")
        print(self._nextpage)
        self.grid_forget()
        self._nextpage.grid(row=0, column=0, sticky="nsew")

    def back_button_event(self):
        print("backpage button")
        self.grid_forget()
        self._prevpage.grid(row=0, column=0, sticky="nsew")

    def get_page_num(self):
        return self._page_num

    def set_page_num(self, page_num):
        self._page_num = page_num

    def get_nextpage(self):
        return self._nextpage

    def set_nextpage(self, nextpage: Frame):
        self._nextpage = nextpage

    def get_prevpage(self):
        return self._prevpage

    def set_prevpage(self, prevpage: Frame):
        self._prevpage = prevpage


class InstructionsFrame(Frame):
    """
    Instructions Frame for the Test Page
    """

    def __init__(self, master: Any, **kwargs):
        kwargs.setdefault("frame_name", constants.INSTRUCTIONS_FRAME_KEY)
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_title = customtkinter.CTkLabel(self, text=self.frame_name)
        self.frame_title.grid(row=0, column=0, sticky="nsew")
