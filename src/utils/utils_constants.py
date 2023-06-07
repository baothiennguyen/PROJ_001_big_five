# utils_constants.py

# Configuration parameters
PROJECT_ROOT = ".project_root"
DATASET_PATH = "data/big-five-personality-test/IPIP-FFM-data-8Nov2018/data-final.csv"
SAMPLE_DATASET_PATH = "data/sample_data.csv"
QUESTIONS_JSON_PATH = "data/questions.json"
# DATASET_PATH = "data/sample_data.csv"

# Keys
PROMPT_KEY = "prompt"
DIMENSION_KEY = "dimension"
ORIENTATION_KEY = "orientation"

# Page Keys
HOME_KEY = "Home"
DATA_ANALYSIS_KEY = "Data Analysis"
CLUSTERING_KEY = "Clustering"
TAKE_TEST_KEY = "Take Test"
RESULTS_KEY = "Results"
ABOUT_KEY = "About"

# Numbers
SAMPLE_SIZE = 100

# Personality test questions
dimensions_dict = {
    "EXT1": "Extraversion",
    "EXT2": "Extraversion",
    "EXT3": "Extraversion",
    "EXT4": "Extraversion",
    "EXT5": "Extraversion",
    "EXT6": "Extraversion",
    "EXT7": "Extraversion",
    "EXT8": "Extraversion",
    "EXT9": "Extraversion",
    "EXT10": "Extraversion",
    "EST1": "Neuroticism",
    "EST2": "Neuroticism",
    "EST3": "Neuroticism",
    "EST4": "Neuroticism",
    "EST5": "Neuroticism",
    "EST6": "Neuroticism",
    "EST7": "Neuroticism",
    "EST8": "Neuroticism",
    "EST9": "Neuroticism",
    "EST10": "Neuroticism",
    "AGR1": "Agreeableness",
    "AGR2": "Agreeableness",
    "AGR3": "Agreeableness",
    "AGR4": "Agreeableness",
    "AGR5": "Agreeableness",
    "AGR6": "Agreeableness",
    "AGR7": "Agreeableness",
    "AGR8": "Agreeableness",
    "AGR9": "Agreeableness",
    "AGR10": "Agreeableness",
    "CSN1": "Conscientiousness",
    "CSN2": "Conscientiousness",
    "CSN3": "Conscientiousness",
    "CSN4": "Conscientiousness",
    "CSN5": "Conscientiousness",
    "CSN6": "Conscientiousness",
    "CSN7": "Conscientiousness",
    "CSN8": "Conscientiousness",
    "CSN9": "Conscientiousness",
    "CSN10": "Conscientiousness",
    "OPN1": "Openness",
    "OPN2": "Openness",
    "OPN3": "Openness",
    "OPN4": "Openness",
    "OPN5": "Openness",
    "OPN6": "Openness",
    "OPN7": "Openness",
    "OPN8": "Openness",
    "OPN9": "Openness",
    "OPN10": "Openness",
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
