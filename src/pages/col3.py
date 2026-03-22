import streamlit as st
import pandas as pd

from data.dfs import df_ina

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

chart_data = pd.DataFrame({
    "Taux (%)": values_pct.values
}, index=df_2020["genre"])
st.header("Impact des thématiques abordées sur la part de parole féminine")
st.subheader("Classement des genres selon la part de parole féminine (2020)")
st.bar_chart(chart_data, horizontal=True, sort="-Taux (%)")
st.header("Chartes et législations")
st.markdown("""
- Loi du 4 août 2014 – Égalité femmes-hommes :  
    Reporting des données hommes/femmes obligatoire
- Pas d'obligation de résultats
""")