<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=GoT%20AI%20Analyser&fontSize=52&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Transformers%20meet%20Westeros&descAlignY=62&descSize=20"/>
</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-0D1117?style=for-the-badge&logo=python&logoColor=3776AB)
![HuggingFace](https://img.shields.io/badge/HuggingFace-0D1117?style=for-the-badge&logo=huggingface&logoColor=FFD21F)
![Gradio](https://img.shields.io/badge/Gradio-0D1117?style=for-the-badge&logo=gradio&logoColor=FF7C00)
![NLP](https://img.shields.io/badge/NLP-0D1117?style=for-the-badge&logo=spacy&logoColor=09A3D5)
![License](https://img.shields.io/badge/License-MIT-0D1117?style=for-the-badge)

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=2"/>

## 🐉 About

An AI/NLP-powered dashboard that analyses Game of Thrones episodes and predicts dominant narrative themes using **Transformers**, **Hugging Face**, and **Gradio**.

Point it at an episode. It tells you what it's really about — Family, Loyalty, Politics, Power, or Death.

Phase 1 of a 3-phase analytical suite:

| Phase | Module | Status |
|-------|--------|--------|
| 1 | 🧠 Theme Classification | ✅ Complete |
| 2 | 🕸️ Character Network Analysis | 🔧 In Progress |
| 3 | 💬 Dialogue Intelligence (Character Chatbot) | 📋 Planned |

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=2"/>

## ✨ Features

- 🧹 **Automated subtitle cleaning** — raw `.json` subtitles → structured episode-level text
- 🧠 **Theme detection** — Transformer-based NLP classifies dominant themes per episode
- 📈 **Interactive Gradio dashboard** — explore and compare themes across all seasons
- 🧩 **Modular architecture** — built for Phase 2 and Phase 3 expansion
- 🗂️ **Full data pipeline** — raw → processed automatically

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=2"/>

## 🛠 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.13 |
| **NLP** | Transformers · Hugging Face Hub · NLTK · SpaCy |
| **Data** | Pandas · NumPy · TQDM |
| **Dashboard** | Gradio · Plotly |
| **Dataset** | Custom GoT subtitle JSONs |

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=2"/>

## 🚀 Getting Started

```bash
git clone https://github.com/derrickrajkumar10/GameOfThrones_AI_Analayser.git
cd GameOfThrones_AI_Analayser

pip install -r requirements.txt

# Launch the Gradio dashboard
python phase1_theme_classifier/app/app.py
```

Open `http://localhost:7860` in your browser.

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=2"/>

## 📁 Project Structure

```
GameOfThrones_AI_Analayser/
├── data/
│   ├── raw/          # Original subtitle JSON files
│   ├── interim/      # Cleaned episode-level text
│   └── processed/    # Final CSVs and model predictions
├── phase1_theme_classifier/
│   ├── scripts/      # Data cleaning, frame construction, theme modelling
│   ├── app/          # Gradio dashboard
│   └── visuals/      # EDA graphs and plots
└── Game_of_Thrones_Script.csv
```

<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>
</div>
