import streamlit as st


st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
    layout="wide",
)
header_container = st.container()

col1, col2, col3 = st.columns(spec=[1, 1.8, 1])

with open("src/assets/report.md", "r") as f:
    with col2:
        report_content = f.read()
        _ = st.markdown("# La place de la femmes dans les médias à travers les années")
        _ = st.markdown(report_content)
