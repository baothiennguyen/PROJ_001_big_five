import os
from gui.gui_app import App
from utils.utils_constants import *
from utils.utils_data import *


def main():
    if not os.path.exists(dataset_path_dict.get(SMALL_KEY)):
        sample_datasets_all()
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
