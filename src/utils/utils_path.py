import os
from utils.utils_constants import README_MD


def get_root_dir():
    # Identify a known file or directory in the root directory

    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Traverse upward until the known file or directory is found
    root_dir = None
    while current_dir != "/":
        if README_MD in os.listdir(current_dir):
            root_dir = current_dir
            break
        current_dir = os.path.dirname(current_dir)

    if root_dir is None:
        raise Exception("Repo root directory not found.")
    else:
        return root_dir
