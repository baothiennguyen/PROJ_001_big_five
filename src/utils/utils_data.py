import os
import pandas as pd
from utils_constants import (
    DATASET_PATH,
    SAMPLE_DATASET_PATH,
    SAMPLE_SIZE,
)
from utils_path import get_root_dir
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


def load_dataset():
    dataset_df = pd.read_csv(DATASET_PATH, sep="\t")
    columns_to_drop = [
        col for col in dataset_df.columns if col[-1] not in [str(i) for i in range(10)]
    ]
    dataset_df.drop(columns_to_drop, axis=1, inplace=True)
    return dataset_df


def make_sample_dataset():
    dataset_df = load_dataset()

    sample_dataset_df = dataset_df.sample(n=SAMPLE_SIZE)
    sample_dataset_df.to_csv(SAMPLE_DATASET_PATH, index=False)

    print(f"Sample dataset created successfully! View in {SAMPLE_DATASET_PATH}")


make_sample_dataset()
