# a script to clean the dataset and keep only the columns we need for our analysis
from pathlib import Path

# Directories
input_dir = Path("../data/rawData")
output_dir = Path("../data/cleanedData")

# Columns we want to keep
wanted_columns = [
    "Date", "HomeTeam", "AwayTeam",
    "FTHG", "FTAG", "FTR",
    "AvgH", "AvgD", "AvgA",
    "AvgCH", "AvgCD", "AvgCA",
    "Avg>2.5", "Avg<2.5",
    "AvgC>2.5", "AvgC<2.5",
    "AHh", "AHCh",
    "HS", "AS", "HST", "AST", "HC", "AC"
]
def clean_dataset(df):

# Drop unwanted columns 
    unwanted_columns = [col for col in df.columns if col not in wanted_columns]

    df_clean = df.drop(columns=unwanted_columns)

# Add season
    df_clean["Season"] = "2025-2026"

# Export cleaned dataset
    df_clean.to_csv("../data/cleanedData/matches_clean2025-2026.csv", index=False)
    