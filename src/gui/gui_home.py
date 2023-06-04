import tkinter
import customtkinter

from gui_settings import SettingsPage
from gui_personality_test import PersonalityTestPage


class HomePage(customtkinter.CTkFrame):
    def __init__(self, master, personality_test_callback, settings_callback):
        super().__init__(master)

        # Create a label for the home page
        label = customtkinter.CTkLabel(
            self, text="Welcome to the Home Page", font=("Arial", 24)
        )
        label.pack(pady=20)

        # Create buttons for navigation
        personality_test_button = customtkinter.CTkButton(
            self, text="Go to Personality Test", command=personality_test_callback
        )
        personality_test_button.pack(pady=10)

        settings_button = customtkinter.CTkButton(
            self, text="Go to Settings", command=settings_callback
        )
        settings_button.pack(pady=10)
