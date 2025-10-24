import pandas as pd
from transformers import pipeline
from tqdm import tqdm
import torch
import os

# Paths
DATA_PATH = "data/processed/episodes.csv"
OUT_PATH = "data/processed/theme_predictions.csv"

# Ensure folder exists
os.makedirs("data/processed", exist_ok=True)

# Load episodes data
df = pd.read_csv(DATA_PATH)

# Define possible themes
themes = [
    "War", "Politics", "Loyalty", "Betrayal", "Love", "Revenge",
    "Family", "Power", "Honor", "Death", "Destiny", "Sacrifice"
]

# Load zero-shot classifier
torch.set_num_threads(4)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
print("✅ Model loaded successfully!")

results = []
MAX_CHARS = 2500  # adjust if you want longer text

for _, row in tqdm(df.iterrows(), total=len(df), desc="Classifying episodes"):
    text = row["dialogue"][:MAX_CHARS]
    out = classifier(text, candidate_labels=themes, multi_label=False)
    results.append({
        "season": row["season"],
        "episode": row["episode"],
        "title": row["title"],
        "theme": out["labels"][0],
        "confidence": round(out["scores"][0], 3)
    })

theme_df = pd.DataFrame(results)
theme_df.to_csv(OUT_PATH, index=False)
print(f"\n🎯 Theme classification complete! Saved to {OUT_PATH}")
print(theme_df.head())
