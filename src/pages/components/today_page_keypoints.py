import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

WOMEN_COLOR = "#ff9999"
MEN_COLOR = "#66b3ff"


def keypoints_channels():
    st.write("### Temps de parole moyen par média et par année")

    # Load data
    df_channels = pd.read_csv(
        "https://www.data.gouv.fr/api/1/datasets/r/756365eb-a8ae-42b1-8345-76fda5dde110"
    )

    # Calculate averages
    media_year_avg = {
        ("radio", 2019): df_channels[df_channels["media"] == "radio"][
            "women_expression_rate_2019"
        ].mean(),
        ("radio", 2020): df_channels[df_channels["media"] == "radio"][
            "women_expression_rate_2020"
        ].mean(),
        ("tv", 2019): df_channels[df_channels["media"] == "tv"][
            "women_expression_rate_2019"
        ].mean(),
        ("tv", 2020): df_channels[df_channels["media"] == "tv"][
            "women_expression_rate_2020"
        ].mean(),
    }

    # Create a 2x2 grid for the plots
    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[[{"type": "pie"}, {"type": "pie"}], [{"type": "pie"}, {"type": "pie"}]],
        subplot_titles=["Radio – 2019", "Radio – 2020", "TV – 2019", "TV – 2020"],
    )

    # Order of plots
    plots = [
        (1, 1, "radio", 2019),
        (1, 2, "radio", 2020),
        (2, 1, "tv", 2019),
        (2, 2, "tv", 2020),
    ]

    for row, col, media, year in plots:
        value = media_year_avg[(media, year)]
        fig.add_trace(
            go.Pie(
                values=[value, 1 - value],
                labels=["Women", "Men"],
                hole=0.5,
                marker_colors=[WOMEN_COLOR, MEN_COLOR],
                textinfo="percent",
                textposition="inside",
                showlegend=False,
            ),
            row=row,
            col=col,
        )

    # Update layout
    fig.update_layout(
        title_text="",
        title_x=0.5,
        title_font=dict(size=20),
        height=800,
        width=800,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)
