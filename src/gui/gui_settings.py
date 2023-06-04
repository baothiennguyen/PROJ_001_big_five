import tkinter
import customtkinter


class SettingsPage(customtkinter.CTkFrame):
    def __init__(self, master, back_callback):
        super().__init__(master)

        # Create a label for the settings page
        label = customtkinter.CTkLabel(self, text="Settings Page", font=("Arial", 24))
        label.pack(pady=20)

        # Create a button to go back to the home page
        back_button = customtkinter.CTkButton(
            self, text="Go Back", command=back_callback
        )
        back_button.pack(pady=10)
