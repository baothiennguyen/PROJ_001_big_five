# utils_constants.py
"""
Numerical constants and strings for dictionary keys and paths
"""

# Titles
APP_TITLE = "Big Five Personality Traits"
MENUBAR_TITLE = "Big Five Data Visualisation"

# Dataset size keys
SMALL_KEY = "small"
MEDIUM_KEY = "medium"
LARGE_KEY = "large"
FULL_KEY = "full"

# Dataset sizes
SMALL_N = 100
MEDIUM_N = 2500
LARGE_N = 50000
FULL_N = None

NORM_FACTOR = 100 / 40

SMALL_STR_KEY = f"Small  (n = 100 values)"
MEDIUM_STR_KEY = f"Medium  (n = 2,500 values)"
LARGE_STR_KEY = f"Large  (n = 50,000 values)"
FULL_STR_KEY = f"Full Dataset  (n = 1,015,341 values)"

dataset_size_dict = {
    SMALL_KEY: SMALL_N,
    MEDIUM_KEY: MEDIUM_N,
    LARGE_KEY: LARGE_N,
    FULL_KEY: FULL_N,
}

dataset_str_dict = {
    SMALL_STR_KEY: SMALL_KEY,
    MEDIUM_STR_KEY: MEDIUM_KEY,
    LARGE_STR_KEY: LARGE_KEY,
    FULL_STR_KEY: FULL_KEY,
}


sample_from_map_dict = {
    SMALL_KEY: MEDIUM_KEY,
    MEDIUM_KEY: LARGE_KEY,
    LARGE_KEY: FULL_KEY,
}

# Dataset paths
README_MD = "README.md"
ORIGINAL_DATASET_PATH = "data/IPIP-FFM-data-8Nov2018/data-final.csv"
ORIGINAL_DATASET_URL = (
    "https://www.kaggle.com/datasets/tunguz/big-five-personality-test"
)
DATA_DIR = "data/"
QUESTIONS_JSON_PATH = "data/questions.json"
THEME_JSON_PATH = "src/assets/theme.json"
# DATASET_PATH = "data/sample_data.csv"

dataset_path_dict = {
    SMALL_KEY: DATA_DIR + f"dataset_sample_{SMALL_N}.csv",
    MEDIUM_KEY: DATA_DIR + f"dataset_sample_{MEDIUM_N}.csv",
    LARGE_KEY: DATA_DIR + f"dataset_sample_{LARGE_N}.csv",
    FULL_KEY: DATA_DIR + f"dataset_full.csv",
}

# Keys
PROMPT_KEY = "prompt"
DIMENSION_KEY = "dimension"
ORIENTATION_KEY = "orientation"

# Page Keys
DATA_PAGE_KEY = "Data"
TEST_PAGE_KEY = "Test"
ABOUT_PAGE_KEY = "About"

# Frame Keys
HOME_FRAME_KEY = "Home"
TAKE_TEST_FRAME_KEY = "Take Test"
RESULTS_FRAME_KEY = "Results"
INSTRUCTIONS_FRAME_KEY = "Instructions"


CLUSTERING_PAGE_KEY = "Clustering"

# Trait Keys
AGR_KEY = "Agreeableness"
CSN_KEY = "Conscientiousness"
OPN_KEY = "Openness"
EXT_KEY = "Extraversion"
EST_KEY = "Neuroticism"

TRAITS_LIST = [AGR_KEY, CSN_KEY, OPN_KEY, EXT_KEY, EST_KEY]

# Plot Type Keys
DISTRIBUTIONS_KEY = "Distributions"
CORRELATIONS_KEY = "Correlations"
CLUSTERS_KEY = "Clusters"


# Distributions tab keys
KDE_KEY = "kde"
MEAN_KEY = "mean"
STD_KEY = "std"
SHOW_STATS_KEY = "show_stats"
YLIM_CONSTANT_KEY = "ylim_constant"

# Personality test questions
dimensions_dict = {
    "EXT1": EXT_KEY,
    "EXT2": EXT_KEY,
    "EXT3": EXT_KEY,
    "EXT4": EXT_KEY,
    "EXT5": EXT_KEY,
    "EXT6": EXT_KEY,
    "EXT7": EXT_KEY,
    "EXT8": EXT_KEY,
    "EXT9": EXT_KEY,
    "EXT10": EXT_KEY,
    "EST1": EST_KEY,
    "EST2": EST_KEY,
    "EST3": EST_KEY,
    "EST4": EST_KEY,
    "EST5": EST_KEY,
    "EST6": EST_KEY,
    "EST7": EST_KEY,
    "EST8": EST_KEY,
    "EST9": EST_KEY,
    "EST10": EST_KEY,
    "AGR1": AGR_KEY,
    "AGR2": AGR_KEY,
    "AGR3": AGR_KEY,
    "AGR4": AGR_KEY,
    "AGR5": AGR_KEY,
    "AGR6": AGR_KEY,
    "AGR7": AGR_KEY,
    "AGR8": AGR_KEY,
    "AGR9": AGR_KEY,
    "AGR10": AGR_KEY,
    "CSN1": CSN_KEY,
    "CSN2": CSN_KEY,
    "CSN3": CSN_KEY,
    "CSN4": CSN_KEY,
    "CSN5": CSN_KEY,
    "CSN6": CSN_KEY,
    "CSN7": CSN_KEY,
    "CSN8": CSN_KEY,
    "CSN9": CSN_KEY,
    "CSN10": CSN_KEY,
    "OPN1": OPN_KEY,
    "OPN2": OPN_KEY,
    "OPN3": OPN_KEY,
    "OPN4": OPN_KEY,
    "OPN5": OPN_KEY,
    "OPN6": OPN_KEY,
    "OPN7": OPN_KEY,
    "OPN8": OPN_KEY,
    "OPN9": OPN_KEY,
    "OPN10": OPN_KEY,
}

prompts_dict = {
    "EXT1": "I am the life of the party.",
    "EXT2": "I don't talk a lot.",
    "EXT3": "I feel comfortable around people.",
    "EXT4": "I keep in the background.",
    "EXT5": "I start conversations.",
    "EXT6": "I have little to say.",
    "EXT7": "I talk to a lot of different people at parties.",
    "EXT8": "I don't like to draw attention to myself.",
    "EXT9": "I don't mind being the center of attention.",
    "EXT10": "I am quiet around strangers.",
    "EST1": "I get stressed out easily.",
    "EST2": "I am relaxed most of the time.",
    "EST3": "I worry about things.",
    "EST4": "I seldom feel blue.",
    "EST5": "I am easily disturbed.",
    "EST6": "I get upset easily.",
    "EST7": "I change my mood a lot.",
    "EST8": "I have frequent mood swings.",
    "EST9": "I get irritated easily.",
    "EST10": "I often feel blue.",
    "AGR1": "I feel little concern for others.",
    "AGR2": "I am interested in people.",
    "AGR3": "I insult people.",
    "AGR4": "I sympathize with others' feelings.",
    "AGR5": "I am not interested in other people's problems.",
    "AGR6": "I have a soft heart.",
    "AGR7": "I am not really interested in others.",
    "AGR8": "I take time out for others.",
    "AGR9": "I feel others' emotions.",
    "AGR10": "I make people feel at ease.",
    "CSN1": "I am always prepared.",
    "CSN2": "I leave my belongings around.",
    "CSN3": "I pay attention to details.",
    "CSN4": "I make a mess of things.",
    "CSN5": "I get chores done right away.",
    "CSN6": "I often forget to put things back in their proper place.",
    "CSN7": "I like order.",
    "CSN8": "I shirk my duties.",
    "CSN9": "I follow a schedule.",
    "CSN10": "I am exacting in my work.",
    "OPN1": "I have a rich vocabulary.",
    "OPN2": "I have difficulty understanding abstract ideas.",
    "OPN3": "I have a vivid imagination.",
    "OPN4": "I am not interested in abstract ideas.",
    "OPN5": "I have excellent ideas.",
    "OPN6": "I do not have a good imagination.",
    "OPN7": "I am quick to understand things.",
    "OPN8": "I use difficult words.",
    "OPN9": "I spend time reflecting on things.",
    "OPN10": "I am full of ideas.",
}

# Question orientation
orientations_dict = {
    "EXT1": True,  # Positive
    "EXT2": False,  # Negative
    "EXT3": True,  # Positive
    "EXT4": False,  # Negative
    "EXT5": True,  # Positive
    "EXT6": False,  # Negative
    "EXT7": True,  # Positive
    "EXT8": False,  # Negative
    "EXT9": True,  # Positive
    "EXT10": False,  # Negative
    "EST1": True,  # Positive
    "EST2": False,  # Negative
    "EST3": True,  # Positive
    "EST4": False,  # Negative
    "EST5": True,  # Positive
    "EST6": True,  # Positive
    "EST7": True,  # Positive
    "EST8": True,  # Positive
    "EST9": True,  # Positive
    "EST10": True,  # Positive
    "AGR1": False,  # Negative
    "AGR2": True,  # Positive
    "AGR3": False,  # Negative
    "AGR4": True,  # Positive
    "AGR5": False,  # Negative
    "AGR6": True,  # Positive
    "AGR7": False,  # Negative
    "AGR8": True,  # Positive
    "AGR9": True,  # Positive
    "AGR10": True,  # Positive
    "CSN1": True,  # Positive
    "CSN2": False,  # Negative
    "CSN3": True,  # Positive
    "CSN4": False,  # Negative
    "CSN5": True,  # Positive
    "CSN6": False,  # Negative
    "CSN7": True,  # Positive
    "CSN8": False,  # Negative
    "CSN9": True,  # Positive
    "CSN10": True,  # Positive
    "OPN1": True,  # Positive
    "OPN2": False,  # Negative
    "OPN3": True,  # Positive
    "OPN4": False,  # Negative
    "OPN5": True,  # Positive
    "OPN6": False,  # Negative
    "OPN7": True,  # Positive
    "OPN8": True,  # Positive
    "OPN9": True,  # Positive
    "OPN10": True,  # Positive
}
