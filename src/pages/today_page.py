import streamlit as st

from pages.components.today_page_barplot import bar_plots_radio_tv
from pages.components.today_page_keypoints import keypoints_channels

st.title("Récemment")
st.set_page_config(
    page_title="Aujourd'hui",
    page_icon="📺",
    layout="wide",
)

keypoints_channels()
bar_plots_radio_tv()
