import streamlit as st
from components.header import header
from components.col1 import col1
from components.col2 import col2
from components.col3 import col3

header()

col1_, col2_, col3_ = st.columns(3)

col1(col1_)
col2(col2_)
col3(col3_)
