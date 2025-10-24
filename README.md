# 🐉 Game of Thrones AI Theme Analyzer  

> **Built by TM Derrick ⚔️**  
> An AI/NLP-powered dashboard that analyzes Game of Thrones episodes and predicts their dominant themes using **Transformers**, **Hugging Face**, and **Gradio**.

---

## 🚀 Overview  

This project processes *Game of Thrones* subtitle transcripts, cleans and structures the data,  
classifies each episode by its dominant theme (e.g. Family, Loyalty, Power, Politics),  
and presents the results through an interactive **Gradio** dashboard.  

It’s Phase 1 of a 3-part project:
1. 🧠 Theme Classification (**current phase**)  
2. 🕸️ Character Network Analysis (using NER + graph visualization)  
3. 💬 Character Chatbot Module (for interactive dialogue simulation)  

---

## 🧩 Folder Structure  

GameOfThrones_AI_Analayser/
│
├── data/
│ ├── raw/ # Subtitle JSONs (from Kaggle)
│ ├── interim/ # Cleaned .txt episodes
│ └── processed/ # Final CSVs (theme predictions etc.)
│
├── phase1_theme_classifier/
│ ├── scripts/ # Cleaning + NLP scripts
│ ├── app/ # Gradio app UI
│ └── visuals/ # Dashboards/plots
│
├── .gitignore
├── titles.json
└── Game_of_Thrones_Script.csv


---

## ⚙️ Installation  

```bash
git clone https://github.com/derrickrajkumar10-tech/GameOfThrones_AI_Analayser.git
cd GameOfThrones_AI_Analayser

# create virtual env
python -m venv .venv
.\.venv\Scripts\activate   # (Windows)

# install dependencies
pip install -r requirements.txt
'''
---
##Features

🎬 Loads and cleans real GoT subtitle data

🤖 Theme classification via Hugging Face Transformers

📈 Interactive dashboard built with Gradio

🗂 Full data pipeline (raw → processed)

🌗 Ready for Phase 2: Character Network Analysis
