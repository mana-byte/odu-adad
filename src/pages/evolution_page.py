import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

from data.dfs import df_radio, df_tv

st.set_page_config(page_title="Évolution 1995-2019", page_icon="📺", layout="wide")

df_radio = df_radio[::-1]
df_values = df_radio.iloc[:, 4:]
years = df_radio["year"].astype(int).tolist()
stations = df_values.columns.tolist()


def make_fig(display, df_values=df_values, years=years):
    fig = go.Figure()
    for idx in range(len(years)):
        target = df_values.iloc[idx]
        sorted_cols = target.sort_values(ascending=True).index.tolist()
        if display:
            ordered = df_values[sorted_cols]
        else:
            ordered = df_values[sorted_cols].iloc[idx:].dropna(axis=1, how="all")
        z = ordered.values
        x = ordered.columns.tolist()
        fig.add_trace(
            go.Heatmap(
                z=z,
                x=x,
                y=years[idx:] if not display else years,
                colorscale="Spectral",
                colorbar=dict(),
                hovertemplate="Station: %{x}<br>Année: %{y}<br>Taux: %{z:.2f}<extra></extra>",
                hoverlabel=dict(bgcolor="black", font_size=16, font_color="white"),
            )
        )

    fig.data[0].visible = True
    for i in range(1, len(years)):
        fig.data[i].visible = False

    steps = []
    for i in range(len(years) - 1, -1, -1):
        step = dict(
            method="update",
            label=years[i],
            args=[{"visible": [False] * len(years)}, {"title": f"Année: {years[i]}"}],
        )
        step["args"][0]["visible"][i] = True
        steps.append(step)

    sliders = [
        dict(
            active=len(years) - 1,
            currentvalue={"prefix": "Année: ", "visible": True, "xanchor": "right"},
            pad={"b": 10, "t": 100},
            steps=steps,
        )
    ]

    fig.update_layout(
        xaxis_tickangle=-45, yaxis=dict(autorange=True), height=600, sliders=sliders
    )
    return fig


col = st.container()
with col:
    st.header("Évolution 1995-2019")
    st.subheader("Tendances globales et progrès sur 25 ans")
    subcol1, subcol2 = st.columns([2, 1], gap="large")
    with subcol1:
        st.markdown(
            "### <span style='font-size: 20px;'>Taux d'expression moyen des femmes à la radio et à la télévision</span>",
            unsafe_allow_html=True,
        )
        radio_avg = df_radio.iloc[:, 4:].mean(axis=1)
        radio_series = pd.Series(
            np.round(radio_avg.values, 2),
            index=df_radio["year"].astype(int),
            name="Radio",
        )
        tv_avg = df_tv.iloc[:, 4:].mean(axis=1)
        tv_series = pd.Series(
            np.round(tv_avg.values, 2), index=df_tv["year"].astype(int), name="TV"
        )
        chart_df = pd.concat([radio_series, tv_series], axis=1).sort_index()

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=chart_df.index,
                y=chart_df["Radio"],
                mode="lines",
                name="Radio",
                hovertemplate="<b>Radio</b><br>Année: %{x}<br>Taux: %{y:.2f}%<extra></extra>",
                hoverlabel=dict(bgcolor="black", font_size=16, font_color="white"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=chart_df.index,
                y=chart_df["TV"],
                mode="lines",
                name="TV",
                hovertemplate="<b>TV</b><br>Année: %{x}<br>Taux: %{y:.2f}%<extra></extra>",
                hoverlabel=dict(bgcolor="black", font_size=16, font_color="white"),
            )
        )
        fig.update_xaxes(tickformat="d")
        st.plotly_chart(fig, width="stretch")

    with subcol2:
        with st.container(border=True):
            st.markdown(
                "<h3 style='text-align: center; margin: 0;'>Variation entre 1995 et 2019</h3>",
                unsafe_allow_html=True,
            )
            st.divider()
            col_r, col_t = st.columns(2)
            with col_r:
                st.markdown(
                    "<p style='text-align: center; font-size: 20px;'>Radio</p>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<p style='text-align: center; font-size: 28px; font-weight: bold; color: rgb(131, 201, 255); margin: 0;'>+6%</p>",
                    unsafe_allow_html=True,
                )
            with col_t:
                st.markdown(
                    "<p style='text-align: center; font-size: 20px;'>TV</p>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<p style='text-align: center; font-size: 28px; font-weight: bold; color: rgb(0, 104, 201); margin: 0;'>+4%</p>",
                    unsafe_allow_html=True,
                )
            st.divider()
            st.markdown(
                """<span style='font-size: 18px; display: block; margin: 0 2em 2em; '>
                    On observe une augmentation du taux d'expression moyen des femmes à la radio et à la télévision, bien que les progrès soient lents et inégaux. \
                    L'absence de données pour la télévision empêche une comparaison antérieure à 2010 mais on peut tout de même constater un retard de plusieurs années \
                    par rapport à la radio, bien que les tendances soient similaires.
                """,
                unsafe_allow_html=True,
            )

    st.subheader("Focus sur les chaînes de radio")
    subcol3, subcol4 = st.columns([1, 2], gap="large")
    with subcol3:
        with st.container(border=True):
            st.markdown(
                "<h3 style='text-align: center; margin: 0;'>Statistiques</h3>",
                unsafe_allow_html=True,
            )
            st.divider()
            subcol3_1, subcol3_2 = st.columns(2)
            with subcol3_1:
                st.markdown(
                    "<p style='text-align: center; font-size: 20px;'>Plus haut taux:</p>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<p style='text-align: center; font-size: 28px; font-weight: bold; margin: 0; color: green'>54%</p>"
                    "<p style='text-align: center; font-size: 18px; margin: 0;'>Chérie FM - 2012</p>",
                    unsafe_allow_html=True,
                )
            with subcol3_2:
                st.markdown(
                    "<p style='text-align: center; font-size: 20px;'>Plus bas taux:</p>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "<p style='text-align: center; font-size: 28px; font-weight: bold;margin: 0;color: red'>14%</p>"
                    "<p style='text-align: center; font-size: 18px; margin: 0;'>Skyrock - 2016</p>",
                    unsafe_allow_html=True,
                )
            st.divider()
            st.markdown(
                """<span style='font-size: 18px; display: block; margin: 0 2em 2em; '>
                    Bien qu'il y ait une tendance générale à l'amélioration, l'évolution n'est ni uniforme selon les chaînes de radio ni selon les années. \
                    Certaines stations comme RTL2 ou Europe 1 ont montré une progression régulière, tandis que d'autres comme France Musique ou Chérie FM ont \
                    connu des fluctuations plus ou moins importantes sans réel progrès sur la période. D'autres encore comme Skyrock ou RMC connu une régression.
                    Il y a également une grande disparité au niveau des plages de taux d'expression, avec des stations ne descendant jamais en dessous de 30% et \
                    atteignant 40% voire 50% alors que d'autres ne dépassent jamais les 20%.
                """,
                unsafe_allow_html=True,
            )

    with subcol4:
        st.markdown(
            "### <span style='font-size: 20px;'>Évolution du taux d'expression des femmes moyen par chaîne de radio entre 95 et 2019</span>",
            unsafe_allow_html=True,
        )
        display = st.checkbox(
            "Afficher les années postérieures à l'année sélectionnée", value=False
        )
        fig = make_fig(display)
        st.plotly_chart(fig, width="stretch")
