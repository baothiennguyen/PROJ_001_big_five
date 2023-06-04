import os
import pandas as pd
from path_utils import get_root_dir
from kaggle.api.kaggle_api_extended import KaggleApi


def get_kaggle_data():
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


def make_sample_dataset(sample_size=100):
    BIG_DATA_PATH = (
        "data/big-five-personality-test/IPIP-FFM-data-8Nov2018/data-final.csv"
    )
    SAMPLE_DATA_PATH = "data/sample_data.csv"

    with open(BIG_DATA_PATH) as data_file:
        data_df = pd.read_csv(data_file)

    sample_df = data_df.sample(n=sample_size)
    sample_df.to_csv(SAMPLE_DATA_PATH, index=False)

    print(f"Sample dataset created successfully! View in {SAMPLE_DATA_PATH}")


make_sample_dataset()
