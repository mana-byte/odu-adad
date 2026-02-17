# front
import streamlit as st

# Graph
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Fonction pour créer un gradient de couleur
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap


col_container = st.container()
col_container.subheader("Aujourd'hui")

# VARIABLES DE COULEURS GLOBALES
TV_COLOR = "#1F77B4"
RADIO_COLOR = "#FF7F0E"
WOMEN_COLOR = "#E63973"
MEN_COLOR = "#4C72B0"
NOISE_COLOR = "#DADADA"

GRADIENT_CMAP = plt.cm.RdYlGn
GRADIENT_VMIN = 20
GRADIENT_VMAX = 50

def gradient_colors(
    values, vmin=GRADIENT_VMIN, vmax=GRADIENT_VMAX, cmap=GRADIENT_CMAP
):
    norm = Normalize(vmin=vmin, vmax=vmax)
    sm = ScalarMappable(cmap=cmap, norm=norm)
    return [cmap(norm(v)) for v in values], sm

df = pd.read_csv(
    "https://www.data.gouv.fr/api/1/datasets/r/cb2f0bb0-59e3-48ff-9382-0e7f47adaa91"
)
# Nettoyer les noms de colonne et ajout d'une colonne année
base_cols = [
    "nb_declarations",
    "total_declarations_duration",  # vaut : women_speech_duration + men_speech_duration + other_speech_duration
    "women_speech_duration",  # en secondes
    "men_speech_duration",  # en secondes
    "other_duration",  # en secondes (bruits, musiques, silences...)
    "women_expression_rate",  # women_speech_duration / (durée totale de parole sans les bruits, musique, silences...)
    "speech_rate",  # (men_speech_duration + women_speech_duration) / total_declarations_duration
]

records = []
for _, row in df.iterrows():
    for year in (2019, 2020):
        rec = {"genre": row["genre"], "year": year}
        for base in base_cols:
            rec[base] = row[f"{base}_{year}"]
        records.append(rec)

df_long = pd.DataFrame(records)

# Ajout d'une colonne : durée totale de parole (hommes + femmes)
df_long["spoken_duration"] = (
    df_long["women_speech_duration"] + df_long["men_speech_duration"]
)
df_comp = df.dropna(
    subset=["women_expression_rate_2019", "women_expression_rate_2020"]
).sort_values("women_expression_rate_2019")

plt.figure(figsize=(12, 7))

for i, (_, row) in enumerate(df_comp.iterrows()):
    x_2019 = row["women_expression_rate_2019"]
    x_2020 = row["women_expression_rate_2020"]

    # Ligne et points avec couleurs distinctes
    plt.plot(
        [x_2019, x_2020], [i, i], marker="o", color="gray", linewidth=2, zorder=1
    )
    plt.scatter(
        x_2019,
        i,
        s=100,
        color=WOMEN_COLOR,
        zorder=2,
        label="2019" if i == 0 else "",
    )
    plt.scatter(
        x_2020, i, s=100, color=MEN_COLOR, zorder=2, label="2020" if i == 0 else ""
    )

    # Label pour 2019
    plt.text(
        x_2019,
        i - 0.40,
        "2019",
        ha="center",
        fontsize=12,
        color=WOMEN_COLOR,
        fontweight="bold",
    )

    # Label pour 2020
    plt.text(
        x_2020,
        i + 0.25,
        "2020",
        ha="center",
        fontsize=12,
        color=MEN_COLOR,
        fontweight="bold",
    )

    # Pourcentage de changement - placement intelligent
    change_pp = (x_2020 - x_2019) * 100
    label = f"{change_pp:+.2f}%"

    # Si le changement est positif, placer le label à droite
    # Si le changement est négatif, placer le label à gauche
    if change_pp >= 0:
        x_label = max(x_2019, x_2020) + 0.02
        ha_align = "left"
    else:
        x_label = min(x_2019, x_2020) - 0.02
        ha_align = "right"

    plt.text(
        x_label,
        i,
        label,
        ha=ha_align,
        fontsize=13,
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor="white",
            edgecolor="lightgray",
            alpha=0.8,
        ),
        va="center",
    )

plt.yticks(range(len(df_comp)), df_comp["genre"])
plt.xlabel("Taux d'expressivité des femmes", fontsize=11, fontweight="bold")
plt.title(
    "Évolution de la part de parole féminine par genre (2019 → 2020)",
    fontsize=13,
    fontweight="bold",
)

plt.grid(color="lightgray", linestyle="-", alpha=0.7)
plt.tight_layout()
plt.show()
