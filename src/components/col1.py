import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

db = pd.read_csv("./data/20190308-radio-years.csv")
db = db[::-1]
db_values = db.iloc[:, 4:].sort_values(by=24, axis=1)
values = db_values.values
years = db["year"].tolist()
stations = db_values.columns.tolist()
cmap = sns.diverging_palette(4, 135, as_cmap=True)
fig, axes = plt.subplots(1, 3, width_ratios=[20, 1, 1], figsize=(15, 10))
cbar_ax = axes[1]
cbar_ax.set_title("Taux", fontsize=12, pad=12)
ax = axes[0]
graph = sns.heatmap(values, ax=ax, xticklabels=stations, yticklabels=years, linewidths=0.5, cmap="Spectral", cbar_ax=cbar_ax)
fig.suptitle("Taux d’expression des femmes moyen par radio entre 95 et 2020", x=0.4, y=0.95, fontsize=20)
for lbl in ax.get_yticklabels():
    lbl.set_size(12)
for lbl in ax.get_xticklabels():
    lbl.set_rotation(45)
    lbl.set_ha('right')
    lbl.set_size(12)

def change(val, db_values=db_values, fig=fig, ax=ax, cbar_ax=cbar_ax, years=years, values=values):
    db_values = db_values.sort_values(by=val-1995, axis=1)
    ax.clear()
    cbar_ax.clear()
    cbar_ax.set_title("Taux", fontsize=12, pad=12)
    sns.heatmap(db_values, ax = ax, xticklabels=db_values.columns.tolist(), yticklabels=years, linewidths=0.5, cmap="Spectral", cbar_ax=cbar_ax)
    for lbl in ax.get_yticklabels():
        lbl.set_size(12) 
    for lbl in ax.get_xticklabels():
        lbl.set_rotation(45)
        lbl.set_ha('right')
        lbl.set_size(12)
    fig.canvas.draw_idle()    

slider = Slider(ax=axes[2], label='Année sur laquelle\nle tri est effectué', valmin=years[-1], valmax=years[0], valinit=years[0], valstep=1, orientation="vertical")
slider.label.set_size(12)
slider.on_changed(change)

col1 = st.container()
with col1:
    st.header("Évolution 1995-2019")
    st.pyplot(fig)
    