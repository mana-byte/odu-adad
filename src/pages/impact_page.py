import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from data.dfs import df_ina

st.set_page_config(
    page_title="Impact de la thématique abordée", page_icon="📺", layout="wide"
)

db = df_ina[::-1]
db_long_genres = []
base_cols = [
    "nb_declarations",
    "total_declarations_duration",
    "women_speech_duration",
    "men_speech_duration",
    "other_duration",
    "women_expression_rate",
    "speech_rate",
]

for _, row in db.iterrows():
    for year in (2019, 2020):
        rec = {"genre": row["genre"], "year": year}
        for base in base_cols:
            rec[base] = row[f"{base}_{year}"]
        db_long_genres.append(rec)

df_long = pd.DataFrame(db_long_genres)

df_2020 = df_long[(df_long["year"] == 2020) & (df_long["genre"] != "Non Renseigné")]
df_2020 = df_2020.sort_values("women_expression_rate", ascending=False)

values_pct = df_2020["women_expression_rate"] * 100
genres = df_2020["genre"].astype(str)

colors = ["#19d2c9", "#66b3ff"] * (len(df_2020) // 2 + 1)

fig = go.Figure(
    data=[
        go.Bar(
            y=genres,
            x=values_pct,
            orientation="h",
            marker=dict(color=colors[: len(df_2020)]),
            text=values_pct.round(1).astype(str) + "%",
            textposition="outside",
            textfont=dict(size=16, color="white"),
            hovertemplate="<b>%{y}</b><br>%{x:.1f}%<extra></extra>",
            hoverlabel=dict(bgcolor="black", font_size=16, font_color="white"),
        )
    ]
)

fig.update_layout(
    title="",
    xaxis_title="Part de parole féminine (%)",
    xaxis=dict(title_font=dict(size=18), tickfont=dict(size=14)),
    yaxis=dict(tickfont=dict(size=14), automargin=True),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    height=700,
    margin=dict(l=220, r=20, t=70, b=50),
)

st.header("Impact des thématiques abordées sur la part de parole féminine")
st.markdown(
    """
    ### <span style='font-size: 20px;'> Part de parole féminine par genre (2020) </span>
    """,
    unsafe_allow_html=True,
)

col_graph, col_card = st.columns([2, 1], gap="large")
with col_graph:
    st.plotly_chart(fig, use_container_width=True)

with col_card:
    with st.container(border=True):
        st.markdown(
            "<h3 style='text-align: center; margin: 0 0 0.5em;'>Chartes et législations</h3>",
            unsafe_allow_html=True,
        )
    col1, col2 = st.columns(2, border=True)
    with col1:
        st.markdown(
            """
            <span style='font-size: 18px; display: block; margin: 0 2em 2em; '>
            <span style='font-size: 20px;'>Loi du 4 août 2014</span>
            <hr style='margin: 0.5em 0;'>
            Égalité femmes-hommes : reporting des données hommes/femmes obligatoire
            </span>
            """,
            unsafe_allow_html=True,
            text_alignment="center",
        )
    with col2:
        st.markdown(
            """
            <span style='font-size: 18px; display: block; margin: 2em 2em 2em; '>
            Absence de législation obligeant l'obtention de résultats
            </span>
        """,
        unsafe_allow_html=True,
        text_alignment="center",
    )
    with st.container(border=True):
        st.markdown(
            "<h3 style='text-align: center; margin: 0 0 0.5em;'>Observations</h3><hr style='margin: 0.5em 0;'>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <span style='font-size: 18px; display: block; margin: 0 2em 2em; '> 
            La part de parole féminine varie considérablement selon les genres, avec des taux atteignant 44% pour la musique et descendant à 13% pour le sport. \
            La plupart des genres sont cependant regroupés autour de 38%, ce qui pourrait s'expliquer par un manque de granularité dans le découpage des genres, certains pouvant être très hétérogènes.
            </span>
            """,
            unsafe_allow_html=True,
        )