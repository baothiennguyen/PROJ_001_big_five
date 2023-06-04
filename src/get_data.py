import os
from utils.path_utils import get_root_dir
from kaggle.api.kaggle_api_extended import KaggleApi

# project_root_dir = os.path.abspath(__file__)
# get_data_script_dir = os.path.dirname(get_data_script_path)

# kaggle_path = os.path.join(get_root_dir(), "kaggle.json")
# print(kaggle_path)
# print(os.listdir(os.path.dirname(kaggle_path)))

"""
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
"""


# Set the environment variable for the Kaggle API credentials
# os.environ["KAGGLE_CONFIG_DIR"] = kaggle_path


# try:
#     with open()


# Initialize the Kaggle API
api = KaggleApi()

# Define the dataset ID
dataset_id = "tunguz/big-five-personality-test"

# Define the target directory to save the downloaded dataset
target_directory = os.path.join(get_root_dir(), "data")

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Download the dataset
api.dataset_download_files(dataset_id, path=target_directory, unzip=True)

print("Dataset downloaded successfully!")
