import tkinter as tk
import customtkinter
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.utils_data import get_distributions, generate_figures
from gui.gui_app import App


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
