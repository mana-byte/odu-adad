import streamlit as st
import pandas as pd
import plotly.graph_objects as go


db = pd.read_csv("https://www.data.gouv.fr/api/1/datasets/r/4ac77400-054c-4a81-a770-f8e719400c78")
db_tv = pd.read_csv("https://www.data.gouv.fr/api/1/datasets/r/5f4a8e22-7599-4789-bf60-7cf7df9a8e70")

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
    sorted_cols = target.sort_values(ascending=True).index.tolist()
    ordered = db_values[sorted_cols]

    z = ordered.values
    x = ordered.columns.tolist()
    y = years

    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x,
        y=y,
        colorscale='Spectral',
        colorbar=dict(title='Taux'),
        hovertemplate='Station: %{x}<br>Année: %{y}<br>Taux: %{z:.2f}<extra></extra>'
    ))
    fig.update_layout(
        title="Taux d’expression des femmes moyen par radio entre 95 et 2020",
        xaxis_tickangle=-45,
        yaxis=dict(autorange=True),
        height=700,
    )
    return fig

col = st.container()
with col:
    st.header("Évolution 1995-2019")
    subcol1, subcol2 = st.columns([2, 1])
    with subcol1:
        st.subheader("Taux d'expression moyen des femmes à la radio et à la TV")
        radio_avg = db.iloc[:, 4:].mean(axis=1)
        radio_series = pd.Series(radio_avg.values, index=db['year'].astype(int), name='Radio')
        tv_avg = db_tv.iloc[:, 4:].mean(axis=1)
        tv_series = pd.Series(tv_avg.values, index=db_tv['year'].astype(int), name='TV')
        chart_df = pd.concat([radio_series, tv_series], axis=1).sort_index()
        st.line_chart(chart_df)
    with subcol2:
        st.metric("Radio evolution 95-19", "+6%")
        st.metric("TV evolution 95-19", "+4%")

    year = st.slider('Année sur laquelle le tri est effectué', min_value=min(years), max_value=max(years), value=max(years), step=1)
    fig = make_fig(year)
    st.plotly_chart(fig, width='stretch')