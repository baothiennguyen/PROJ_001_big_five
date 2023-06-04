import tkinter
import customtkinter

from gui_home import HomePage


customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "green"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self, root):
        self.root = root
        self.current_page = None

        self.show_home_page()

    def show_home_page(self):
        self.clear_current_page()
        self.current_page = HomePage(
            self.root, self.go_to_personality_test, self.go_to_settings
        )
        self.current_page.pack()

    def go_to_personality_test(self):
        self.clear_current_page()
        # Create and display the personality test page
        from gui_personality_test import PersonalityTestPage

        personality_test_page = PersonalityTestPage(self.root, self.show_home_page)
        personality_test_page.pack()

    def go_to_settings(self):
        self.clear_current_page()
        # Create and display the settings page
        from gui_settings import SettingsPage

        settings_page = SettingsPage(self.root, self.show_home_page)
        settings_page.pack()

    def clear_current_page(self):
        if self.current_page:
            self.current_page.destroy()


# Create the main application window
root = customtkinter.CTk()

# Create an instance of the App class
app = App(root)

# Start the main event loop
root.mainloop()
