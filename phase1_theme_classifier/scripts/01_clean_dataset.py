import os
import json
import re

RAW_PATH = "data/raw"
CLEAN_PATH = "data/interim"

os.makedirs(CLEAN_PATH, exist_ok=True)

def clean_text(text):
    """Remove extra whitespace and newlines."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()

for file in os.listdir(RAW_PATH):
    if not file.endswith(".json"):
        continue

    file_path = os.path.join(RAW_PATH, file)
    print(f"\n📘 Processing {file}...")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for episode_key, lines_dict in data.items():
        subtitles = list(lines_dict.values())
        combined_text = " ".join(subtitles)
        cleaned_text = clean_text(combined_text)

        # Create a safe filename
        clean_name = episode_key.replace(".srt", "").replace(" ", "_")
        output_path = os.path.join(CLEAN_PATH, f"{clean_name}.txt")

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(cleaned_text)

        print(f"   ✅ {episode_key} — {len(subtitles)} lines saved")

print(" All seasons processed! Cleaned files are in 'data/interim/'")
