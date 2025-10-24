import gradio as gr
import pandas as pd
import plotly.express as px
import os

# ====== Load Data ======
EPISODE_PATH = "data/processed/episodes.csv"
THEME_PATH = "data/processed/theme_predictions.csv"

episodes_df = pd.read_csv(EPISODE_PATH)
themes_df = pd.read_csv(THEME_PATH)

# ====== Helper Functions ======
def get_episode_list(season):
    """Return list of episodes (as strings) for the given season."""
    season = int(season)
    episodes = themes_df[themes_df["season"] == season]["episode"].unique()
    return [str(e) for e in sorted(episodes)]

def get_episode_data(season, episode):
    """Return theme info, chart, and preview text for a selected episode."""
    season = int(season)
    episode = int(episode)
    row = themes_df[(themes_df["season"] == season) & (themes_df["episode"] == episode)]

    if row.empty:
        return "No data found.", None, "No dialogue available", None

    row = row.iloc[0]
    theme = row["theme"]
    title = row["title"]
    file = row["file"]

    # Read episode text safely
    episode_path = os.path.join("data", "interim", file)
    if os.path.exists(episode_path):
        with open(episode_path, "r", encoding="utf-8") as f:
            full_text = f.read()
        preview_text = "\n".join(full_text.split("\n")[:15]) + "\n\n[...] (full dialogue truncated)"
    else:
        preview_text = "Dialogue file not found."

    # Generate season-level theme frequency chart
    season_df = themes_df[themes_df["season"] == season]
    chart_df = season_df.groupby("theme").size().reset_index(name="count").nlargest(5, "count")

    fig = px.bar(
        chart_df,
        x="theme",
        y="count",
        color="theme",
        title=f"Top 5 Themes in Season {season}",
        template="plotly_dark"
    )
    fig.update_layout(title_x=0.5)

    info_text = f"🧠 **Predicted Theme:** {theme}\n🎬 **{title}** (Season {season}, Episode {episode})"
    return info_text, fig, preview_text, episode_path

# ====== UI Logic ======
def update_episodes(season):
    """Update episode dropdown choices when a season is selected."""
    return gr.update(choices=get_episode_list(season))

def display_episode(season, episode):
    """Display episode info and charts."""
    return get_episode_data(season, episode)

# ====== Build Gradio Interface ======
with gr.Blocks(theme=gr.themes.Monochrome(), css=".gradio-container {background-color: #0f1117;}") as demo:
    gr.Markdown(
        """
        # ⚔️ Game of Thrones AI Theme Analyzer
        Discover dominant themes across episodes of Game of Thrones — powered by NLP and Hugging Face Transformers.
        """
    )

    with gr.Row():
        season_select = gr.Dropdown(
            label="Select Season",
            choices=[str(s) for s in sorted(themes_df["season"].unique())],
            value=str(sorted(themes_df["season"].unique())[0]),
        )
        episode_select = gr.Dropdown(label="Select Episode")

    info = gr.Markdown(label="Episode Info")
    plot = gr.Plot(label="Theme Chart")

    with gr.Accordion("📜 Episode Dialogue", open=False):
        dialogue = gr.Textbox(label="Dialogue Preview", lines=10)

    view_button = gr.Button("🔗 View Full Episode")

    # --- Functional bindings ---
    season_select.change(update_episodes, inputs=season_select, outputs=episode_select)
    episode_select.change(display_episode, inputs=[season_select, episode_select],
                          outputs=[info, plot, dialogue, view_button])

    # --- Footer ---
    gr.HTML(
        """
        <div style="text-align:center; font-size:14px; margin-top:20px; color:#bbb;">
            | Powered by <b>Transformers</b> + <b>Gradio</b><br>
            <a href="https://github.com/YOUR_GITHUB/GameOfThrones_AI_Analyser" target="_blank" style="color:#a78bfa;">
                View on GitHub
            </a>
        </div>
        """
    )

# ====== Launch App ======
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=8080)
