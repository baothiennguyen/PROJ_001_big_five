import subprocess

# Set the path to your downloaded Kaggle API credentials JSON file
kaggle_credentials_path = "/path/to/kaggle.json"

# Set the competition or dataset you want to download
competition_name = "competition-name"  # Replace with the actual competition or dataset name

# Run the Kaggle command to download the data
subprocess.call(["kaggle", "competitions", "download", "-c", competition_name, "--path", "."], env={'KAGGLE_CONFIG_PATH': kaggle_credentials_path})