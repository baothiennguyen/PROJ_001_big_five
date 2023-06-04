import os
from utils.path_utils import get_root_dir
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()

# Define the dataset ID
dataset_id = "tunguz/big-five-personality-test"

# Define the target directory to save the downloaded dataset
target_directory = os.path.join(get_root_dir(), "data")

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

print(target_directory)

# Download the dataset
api.dataset_download_files(dataset=dataset_id, path=target_directory, unzip=True)

print("Dataset downloaded successfully!")
