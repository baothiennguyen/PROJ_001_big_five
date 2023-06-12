import os
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Literal, Union
from utils.utils_constants import *

from utils.utils_path import get_root_dir
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


def load_dataset(
    size_key: Union[SMALL_KEY, MEDIUM_KEY, LARGE_KEY, FULL_KEY] = None,
) -> pd.DataFrame:
    """
    Load and process dataset of different sizes
    """
    if (size_key == FULL_KEY) | (size_key is None):
        dataset_df = pd.read_csv(FULL_DATASET_PATH, sep="\t")
        columns_to_drop = [
            col
            for col in dataset_df.columns
            if col[-1] not in [str(i) for i in range(10)]
        ]
        dataset_df.drop(columns_to_drop, axis=1, inplace=True)
        dataset_df = dataset_df.astype(float)

    else:
        dataset_size_path = dataset_path_dict.get(size_key)
        dataset_df = pd.read_csv(dataset_size_path).astype(float)
    return dataset_df


def sample_datasets_all():
    """
    Load full dataset and create sample dataset files
    """
    dataset_df = load_dataset()
    for size_key in [SMALL_KEY, MEDIUM_KEY, LARGE_KEY]:
        sample_dataset(dataset_df, size_key)


def sample_dataset(
    dataset_df: pd.DataFrame,
    size_key: Union[SMALL_KEY, MEDIUM_KEY, LARGE_KEY],
):
    """
    Load full dataset and create sample dataset files
    """
    n_samples = dataset_size_dict.get(size_key)
    sample_dataset_df = dataset_df.sample(n=n_samples)

    dataset_path = dataset_path_dict.get(size_key)
    sample_dataset_df.to_csv(dataset_path, index=False)
    print(
        f"Sample dataset with {n_samples} values created successfully! View in {dataset_path} directory."
    )


def make_questions_json(outpath=QUESTIONS_JSON_PATH):
    questions_dict = {}
    for prompt_key in prompts_dict:
        questions_dict[prompt_key] = {
            PROMPT_KEY: prompts_dict[prompt_key],
            DIMENSION_KEY: dimensions_dict[prompt_key],
            ORIENTATION_KEY: orientations_dict[prompt_key],
        }
    with open(outpath, "w") as f:
        json.dump(questions_dict, f, indent=4)

    return questions_dict


def calculate_scores(
    dataset: pd.DataFrame, questions_json_path=QUESTIONS_JSON_PATH
) -> pd.DataFrame:
    with open(questions_json_path) as f_json:
        questions_dict = json.load(f_json)

    columns_to_reverse = [
        question_key
        for question_key in dataset.columns
        if not questions_dict.get(question_key).get(ORIENTATION_KEY)
    ]
    score_mapping = {1.0: 5.0, 2.0: 4.0, 4.0: 2.0, 5.0: 1.0}
    dataset[columns_to_reverse] = dataset[columns_to_reverse].replace(score_mapping)
    total_scores = dataset.groupby(dimensions_dict, axis=1).sum()
    return total_scores


def generate_distributions_figure(total_scores):
    # dataset = load_dataset(sample=True)
    # total_scores = calculate_scores(dataset)

    # Create subplots for each trait

    sns.set_theme(
        style="dark",
        rc={
            "text.color": "white",
            "axes.labelcolor": "white",
            "axes.facecolor": "slategrey",
            "patch.edgecolor": "lightgrey",
            "figure.facecolor": "#242424",
            "xtick.color": "white",
            "ytick.color": "white",
        },
    )

    palette = sns.color_palette("bright")
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
    fig.delaxes(axes[1, 2])
    subplot_index = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
    # Plot distribution for each trait
    for i, column in enumerate(total_scores.columns):
        row_i, col_i = subplot_index[i]
        sns.histplot(
            total_scores[column],
            binwidth=1,
            kde=True,
            ax=axes[row_i, col_i],
            color=palette[i],
        )
        axes[row_i, col_i].set(xlim=(5, 50))
        axes[row_i, col_i].set_title(f"Distribution of {column}")
        axes[row_i, col_i].set_xlabel("Values")
        axes[row_i, col_i].set_ylabel("Frequency")

    plt.tight_layout()
    plt.close()

    return fig
