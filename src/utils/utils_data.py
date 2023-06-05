import os
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
from utils.utils_constants import (
    DATASET_PATH,
    SAMPLE_DATASET_PATH,
    SAMPLE_SIZE,
    QUESTIONS_JSON_PATH,
    PROMPT_KEY,
    DIMENSION_KEY,
    ORIENTATION_KEY,
    dimensions_dict,
    prompts_dict,
    orientations_dict,
)
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


def load_dataset(sample=True):
    if sample:
        dataset_df = pd.read_csv(SAMPLE_DATASET_PATH).astype(float)
    else:
        dataset_df = pd.read_csv(DATASET_PATH, sep="\t")
        columns_to_drop = [
            col
            for col in dataset_df.columns
            if col[-1] not in [str(i) for i in range(10)]
        ]
        dataset_df.drop(columns_to_drop, axis=1, inplace=True)
        dataset_df = dataset_df.astype(float)
    return dataset_df


def make_sample_dataset(sample_size=SAMPLE_SIZE):
    dataset_df = load_dataset(sample=False)

    sample_dataset_df = dataset_df.sample(n=sample_size)
    sample_dataset_df.to_csv(SAMPLE_DATASET_PATH, index=False)

    print(f"Sample dataset created successfully! View in {SAMPLE_DATASET_PATH}")


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


def calculate_scores(dataset: pd.DataFrame, questions_json_path=QUESTIONS_JSON_PATH):
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

    # for group, data in grouped:
    #     print(f"Trait Group: {group}")
    #     print(data)
    #     print()
    # dimension_scores = pd.DataFrame


def get_distributions():
    make_sample_dataset(1000)
    make_questions_json()
    dataset = load_dataset(sample=True)
    total_scores = calculate_scores(dataset)
    return total_scores


def generate_figures():
    dataset = load_dataset(sample=True)
    total_scores = calculate_scores(dataset)

    # Create subplots for each trait
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

    subplot_index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]]

    # Plot distribution for each trait
    for i, column in enumerate(total_scores.columns):
        row_i, col_i = subplot_index[i]
        sns.histplot(total_scores[column], binwidth=1, kde=True, ax=axes[i // 3, i % 3])
        axes[row_i, col_i].set(xlim=(5, 50))
        axes[row_i, col_i].set_title(f"Distribution of {column}")
        axes[row_i, col_i].set_xlabel("Values")
        axes[row_i, col_i].set_ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    return fig


# get_distributions()
