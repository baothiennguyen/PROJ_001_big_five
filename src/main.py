import os

import utils.utils_constants as constants
from gui.gui_app import App
from utils.utils_data import sample_datasets_all


def main():
    if any(
        [
            not os.path.exists(constants.dataset_path_dict.get(key))
            for key in [
                constants.SMALL_KEY,
                constants.MEDIUM_KEY,
                constants.LARGE_KEY,
                constants.FULL_KEY,
            ]
        ]
    ):
        sample_datasets_all()
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
