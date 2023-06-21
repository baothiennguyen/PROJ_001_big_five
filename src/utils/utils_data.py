import json
import os
from typing import Union

import numpy as np
import pandas as pd

import utils.utils_constants as constants

# from utils.utils_constants import *


def process_dataset(
    dataset_path=constants.ORIGINAL_DATASET_PATH,
    questions_json_path=constants.QUESTIONS_JSON_PATH,
):
    """
    Process original dataset:
    - Drop irrelevant columns
    - Format missing values
    - Reverse scores for negatively-oriented questions
    - Saves resulting dataframe as csv
    """
    try:
        assert os.path.exists(dataset_path)
    except AssertionError:
        raise Exception(
            f"Original dataset not found in {dataset_path}."
            + f"Download dataset from Kaggle at {constants.ORIGINAL_DATASET_URL}"
            + f"and place extract the contents into {constants.DATA_DIR}."
        )
    dataset_df = pd.read_csv(dataset_path, sep="\t")

    # Drop non-question columns, replace 0 values, convert to
    columns_to_drop = [
        col for col in dataset_df.columns if col[-1] not in [str(i) for i in range(10)]
    ]
    dataset_df.drop(columns_to_drop, axis=1, inplace=True)
    dataset_df.replace(0, np.nan, inplace=True)
    dataset_df = dataset_df.astype("Int8")

    # Reverse scores for negative-oriented questions
    with open(questions_json_path) as f_json:
        questions_dict: dict() = json.load(f_json)

    columns_to_reverse = [
        question_key
        for question_key in dataset_df.columns
        if not questions_dict.get(question_key).get(constants.ORIENTATION_KEY)
    ]
    score_mapping = {1.0: 5.0, 2.0: 4.0, 4.0: 2.0, 5.0: 1.0}
    dataset_df[columns_to_reverse] = dataset_df[columns_to_reverse].replace(
        score_mapping
    )
    dataset_df = dataset_df.sub(1)

    dataset_path = constants.dataset_path_dict.get(constants.FULL_KEY)
    dataset_df.to_csv(dataset_path, index=False)
    print(f"Full dataset with saved successfully! View at {dataset_path}.")


def get_dataset(
    size_key: Union[
        constants.SMALL_KEY,
        constants.MEDIUM_KEY,
        constants.LARGE_KEY,
        constants.FULL_KEY,
    ],
) -> pd.DataFrame:
    """
    Load and return dataset of specified sizes
    """
    dataset_path = constants.dataset_path_dict.get(size_key)
    dataset_df = pd.read_csv(dataset_path)
    return dataset_df


def sample_datasets_all():
    """
    Process original dataset and create sample dataset files
    """
    process_dataset()
    dataset_df = get_dataset(constants.FULL_KEY).astype("Int8")
    for size_key in [constants.SMALL_KEY, constants.MEDIUM_KEY, constants.LARGE_KEY]:
        sample_dataset(dataset_df, size_key)


def sample_dataset(
    dataset_df: pd.DataFrame,
    size_key: Union[constants.SMALL_KEY, constants.MEDIUM_KEY, constants.LARGE_KEY],
):
    """
    Loads the next largest dataset file and re-samples, overwrites the exisitng dataset
    """
    n_samples = constants.dataset_size_dict.get(size_key)
    sample_dataset_df = dataset_df.sample(n=n_samples).astype("Int8")

    dataset_path = constants.dataset_path_dict.get(size_key)
    sample_dataset_df.to_csv(dataset_path, index=False)
    print(
        f"Sample dataset with {n_samples} "
        + f"values created successfully! View at {dataset_path}"
    )


def make_questions_json(outpath=constants.QUESTIONS_JSON_PATH):
    """
    Creates json file to combine all components of questions
    """
    questions_dict = {}
    for prompt_key in constants.prompts_dict:
        questions_dict[prompt_key] = {
            constants.PROMPT_KEY: constants.prompts_dict[prompt_key],
            constants.DIMENSION_KEY: constants.dimensions_dict[prompt_key],
            constants.ORIENTATION_KEY: constants.orientations_dict[prompt_key],
        }
    with open(outpath, "w") as f:
        json.dump(questions_dict, f, indent=4)

    return questions_dict


def calculate_scores(
    size_key: Union[constants.SMALL_KEY, constants.MEDIUM_KEY, constants.LARGE_KEY]
) -> pd.DataFrame:
    """
    Returns normalised scores for datset of input size
    """
    dataset_df = get_dataset(size_key)
    total_scores = (
        dataset_df.groupby(constants.dimensions_dict, axis=1)
        .sum()
        .mul(constants.NORM_FACTOR)
    )
    return total_scores


"""
from kaggle.api.kaggle_api_extended import KaggleApi


def get_kaggle_data():

    # [REDUNDANT] Get original dataset from Kaggle

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
"""
