# a script to clean the dataset and keep only the columns we need for our analysis
from pathlib import Path
import pandas as pd
# Directories
input_dir = Path("../data/rawData")
output_dir = Path("../data/cleanedData")

# Columns we want to keep

def clean_dataFile(file_path , wanted_columns):
    season = file_path.stem  # Get the season from the filename
    df = pd.read_csv(file_path)
    df_clean = df[wanted_columns].copy()
    df_clean["Season"]= season
    return df_clean