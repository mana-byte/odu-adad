import streamlit as st

from pages.components.today_page_barplot import bar_plots_radio_tv
from pages.components.today_page_keypoints import keypoints_channels

st.title("Aujourd'hui")

keypoints_channels()
bar_plots_radio_tv()


