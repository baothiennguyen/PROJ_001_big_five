import os
from gui.gui_app import App
from utils.utils_constants import *
from utils.utils_data import *


def main():
    if any(
        [
            not os.path.exists(dataset_path_dict.get(key))
            for key in [SMALL_KEY, MEDIUM_KEY, LARGE_KEY]
        ]
    ):
        sample_datasets_all()
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
