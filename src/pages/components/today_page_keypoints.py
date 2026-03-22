import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from data.dfs import df_channels

WOMEN_COLOR = "#ff9999"
MEN_COLOR = "#66b3ff"


def keypoints_channels():
    st.markdown(
        "### <span style='font-size: 24px;'>Temps de parole moyen des femmes à la Radio et Télévision entre 2019 et 2020</span>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <span style='font-size: 18px;'>Sur les deux années et dans les deux types de médias, le temps de parole des hommes domine largement, se situant toujours au-dessus de la barre des 60%. Les femmes n'occupent qu'environ un tiers de l'espace vocal.</span>
    """,
        unsafe_allow_html=True,
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
                labels=["Femme", "Homme"],
                hole=0.4,
                marker_colors=[WOMEN_COLOR, MEN_COLOR],
                textinfo="percent+label",
                textposition="inside",
                textfont=dict(size=24, color="white"),
                hovertemplate="<b>%{label}</b><br>%{value:.2%}<extra></extra>",
                hoverlabel=dict(
                    font_size=18,
                ),
                showlegend=False,
                pull=[0.1, 0],
            ),
            row=row,
            col=col,
        )

    # Update layout
    fig.update_layout(
        title_text="",
        title_x=0.5,
        title_font=dict(size=24),
        height=1000,
        width=1000,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=30, b=20),
    )

    # Display the figure in Streamlit
    st.plotly_chart(fig, use_container_width=True)
