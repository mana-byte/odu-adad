import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


db = pd.read_csv("https://www.data.gouv.fr/api/1/datasets/r/4ac77400-054c-4a81-a770-f8e719400c78")
db = db[::-1]
db_values = db.iloc[:, 4:]
years = db["year"].astype(int).tolist()
stations = db_values.columns.tolist()


def make_fig(sort_year, db_values=db_values, years=years):
    try:
        row_idx = years.index(int(sort_year))
    except ValueError:
        row_idx = 0
    target = db_values.iloc[row_idx]
    sorted_cols = target.sort_values(ascending=False).index.tolist()
    ordered = db_values[sorted_cols]

    fig, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(ordered.values, ax=ax, xticklabels=ordered.columns.tolist(), yticklabels=years, linewidths=0.5, cmap="Spectral", cbar_kws={"label": "Taux"})
    fig.suptitle("Taux d’expression des femmes moyen par radio entre 95 et 2020", x=0.4, y=0.95, fontsize=20)
    for lbl in ax.get_yticklabels():
        lbl.set_size(12)
    for lbl in ax.get_xticklabels():
        lbl.set_rotation(45)
        lbl.set_ha('right')
        lbl.set_size(12)
    return fig


def col1(col):
    with col:
        subcol1, subcol2 = st.columns([2, 1])
        with subcol2:
            st.metric("Radio evolution 95-19", "+40%")
            st.metric("TV evolution 95-19", "+43%")
        st.header("Évolution 1995-2019")

        year = st.slider('Année sur laquelle le tri est effectué', min_value=min(years), max_value=max(years), value=max(years), step=1)
        fig = make_fig(year)
        st.pyplot(fig)
        plt.close(fig)