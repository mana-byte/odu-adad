import streamlit as st

pg = st.navigation([st.Page("pages/col1.py", title="Évolution 1995-2019"), st.Page("pages/today_page.py", title="Aujourd'hui"), st.Page("pages/col3.py", title="Impact de la thématique abordée")])
pg.run()