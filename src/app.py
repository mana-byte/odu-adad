import streamlit as st

pg = st.navigation(
    [
        st.Page("pages/evolution_page.py"),
        st.Page("pages/today_page.py"),
        st.Page(
            "pages/impact_page.py",
        ),
    ]
)
pg.run()

