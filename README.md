# 🐉 Game of Thrones AI Theme Analyzer  

> **Developed by TM Derrick ⚔️**  
> An AI/NLP-powered dashboard that analyzes Game of Thrones episodes and predicts dominant narrative themes using **Transformers**, **Hugging Face**, and **Gradio**.

---

## 🚀 Overview  

This project implements an end-to-end Natural Language Processing (NLP) pipeline designed to analyze dialogues extracted from *Game of Thrones* subtitle data.  
By leveraging modern Transformer-based architectures, the system classifies each episode according to thematic dimensions such as **Family**, **Loyalty**, **Politics**, **Power**, and **Death**.  

The application provides an **interactive Gradio dashboard** that allows users to explore the thematic evolution of the series season by season, supported by dynamic data visualizations and textual summaries.

This initiative forms **Phase 1** of a three-phase analytical suite:
1. 🧠 **Theme Classification** *(current phase)*  
2. 🕸️ **Character Network Analysis** *(relationship mapping using NER and graph theory)*  
3. 💬 **Dialogue Intelligence Module** *(interactive AI-based character simulation)*  

---

## 🧩 Project Structure  

GameOfThrones_AI_Analayser/
│
├── data/
│ ├── raw/ # Original subtitle JSON files
│ ├── interim/ # Intermediate text files (cleaned dialogues)
│ └── processed/ # Final structured CSVs and predictions
│
├── phase1_theme_classifier/
│ ├── scripts/ # Data cleaning, frame construction, and theme modeling
│ ├── app/ # Gradio-based visualization and dashboard logic
│ └── visuals/ # Graphs and plots generated during EDA
│
├── .gitignore
├── Game_of_Thrones_Script.csv
└── titles.json

## 📊 Key Features

🧹 Automated Subtitle Cleaning: Converts raw .json subtitles into structured episode-level text.

🧠 Theme Detection: Utilizes Transformer-based NLP models to infer dominant narrative themes per episode.

📈 Interactive Visualization: Built using Gradio for seamless theme exploration and comparison across seasons.

🧩 Modular Architecture: Designed for scalability, enabling future integration of character-level NLP analysis.

🗂️ Full Data Pipeline: Processes data from raw to processed format automatically.

---

## 🧰 Tech Stack  

| Category | Technologies |
|-----------|---------------|
| **Language** | Python 3.13 |
| **Libraries** | Transformers · Hugging Face Hub · Pandas · NumPy · TQDM |
| **NLP Tools** | NLTK · SpaCy *(for upcoming Character Network)* |
| **Visualization** | Gradio · Plotly |
| **Version Control** | Git · GitHub |
| **Environment** | Virtualenv · VS Code |
| **Dataset Source** | Custom Game of Thrones Subtitle JSONs |

---

## 🧭 Roadmap
Phase 2 — Character Network Analyzer

Extract entity relationships using SpaCy Named Entity Recognition (NER).

Construct a graph-based visualization using NetworkX to reveal alliances, rivalries, and power structures.

Phase 3 — Character Chatbot

Develop an AI-driven conversational interface trained on GoT dialogues.

Deploy as a context-aware chatbot that responds in the tone of specific characters.


