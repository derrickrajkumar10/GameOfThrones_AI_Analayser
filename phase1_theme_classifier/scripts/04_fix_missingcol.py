import pandas as pd

# Load both files
episodes_df = pd.read_csv("data/processed/episodes.csv")
themes_df = pd.read_csv("data/processed/theme_predictions.csv")

# Match episodes to theme predictions by season + episode
merged = pd.merge(
    themes_df,
    episodes_df[["season", "episode", "file"]],
    on=["season", "episode"],
    how="left"
)

# Save fixed version
merged.to_csv("data/processed/theme_predictions.csv", index=False)
print("✅ Added 'file' column successfully to theme_predictions.csv!")
print(merged.head())