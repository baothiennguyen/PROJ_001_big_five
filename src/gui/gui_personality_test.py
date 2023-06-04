import tkinter
import customtkinter


class PersonalityTestPage(customtkinter.CTkFrame):
    def __init__(self, master, back_callback):
        super().__init__(master)

        # Create a label for the personality test page
        label = customtkinter.CTkLabel(
            self, text="Personality Test Page", font=("Arial", 24)
        )
        label.pack(pady=20)

        # Create a button to go back to the home page
        back_button = customtkinter.CTkButton(
            self, text="Go Back", command=back_callback
        )
        back_button.pack(pady=10)
