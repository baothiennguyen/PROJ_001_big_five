import os


def get_root_dir():
    # Identify a known file or directory in the root directory
    project_root = ".project_root"

    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Traverse upward until the known file or directory is found
    root_dir = None
    while current_dir != "/":
        if project_root in os.listdir(current_dir):
            root_dir = current_dir
            break
        current_dir = os.path.dirname(current_dir)

    if root_dir is None:
        raise Exception("Repo directory not found.")
    else:
        return root_dir
