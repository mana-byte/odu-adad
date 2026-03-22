import streamlit as st

pg = st.navigation(
    [
        st.Page("pages/evolution_page.py", title="Évolution 1995-2019", icon="📺"),
        st.Page("pages/today_page.py", title="Aujourd'hui", icon="📺"),
        st.Page(
            "pages/impact_page.py", title="Impact de la thématique abordée", icon="📺"
        ),
    ]
)
pg.run()

