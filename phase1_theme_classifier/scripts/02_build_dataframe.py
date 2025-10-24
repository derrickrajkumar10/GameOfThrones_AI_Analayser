import os
import re
import pandas as pd

CLEAN_PATH = "data/interim"
OUT_PATH = "data/processed/episodes.csv"

os.makedirs("data/processed", exist_ok=True)

records = []

for file in os.listdir(CLEAN_PATH):
    if not file.endswith(".txt"):
        continue

    # extract season + episode numbers from filename
    match = re.search(r"S(\d{2})E(\d{2})", file)
    if not match:
        continue
    season, episode = match.groups()

    # extract readable title
    title = re.sub(r"^.*S\d{2}E\d{2}_", "", file)
    title = title.replace(".txt", "").replace("_", " ")

    # read cleaned dialogue text
    with open(os.path.join(CLEAN_PATH, file), "r", encoding="utf-8") as f:
        text = f.read().strip()

    records.append({
        "season": season,
        "episode": episode,
        "title": title,
        "dialogue": text,
        "file": file
    })

df = pd.DataFrame(records).sort_values(["season", "episode"]).reset_index(drop=True)
df.to_csv(OUT_PATH, index=False)

print(f"✅ Saved dataframe to {OUT_PATH} — {len(df)} episodes total.")
print(df.head())
