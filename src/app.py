import streamlit as st

home = st.Page("pages/home_page.py", title="Accueil", icon="🏠")
page_evo = st.Page("pages/evolution_page.py", title="Évolution", icon="💾")
page_today = st.Page("pages/today_page.py", title="Aujourd'hui", icon="📺")
page_impact = st.Page("pages/impact_page.py", title="Impact", icon="👩‍⚖️")

pg = st.navigation([home, page_evo, page_today, page_impact], position="hidden")

st.markdown(
    """
    <style>
    .timeline-link {
        text-decoration: none !important;
        color: inherit !important;
        display: block;
        padding: 20px;
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        text-align: center;
        height: 100%;
    }

    .timeline-link:hover {
        background-color: rgba(151, 166, 195, 0.15);
        border-color: #ff4b4b;
        transform: translateY(-3px) scale(1.05);
    }

    .timeline-title {
        font-size: 1.5rem;
        font-weight: bold;
        display: block;
        margin-bottom: 8px;
    }

    .timeline-desc {
        font-size: 0.95rem;
        color: #A3A8B8;
    }
    </style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns([1, 12, 12, 12], gap="small")

with col1:
    st.markdown(
        f"""
        <a href="/" target="_self" class="timeline-link">
            <span>◄</span>
        </a>
    """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"""
        <a href="/evolution_page" target="_self" class="timeline-link">
            <span class="timeline-title">💾 1995 — 2019</span>
            <p class="timeline-desc">Analyse des <b>archives</b> et de l'évolution passée.</p>
        </a>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <a href="/today_page" target="_self" class="timeline-link">
            <span class="timeline-title">📺 Aujourd'hui</span>
            <p class="timeline-desc">Situation <i>actuelle (2019-2020)</i>.</p>
        </a>
    """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
        <a href="/impact_page" target="_self" class="timeline-link">
            <span class="timeline-title">👩‍⚖️ Impact</span>
            <p class="timeline-desc">Conséquences identifiées.</p>
        </a>
    """,
        unsafe_allow_html=True,
    )

st.divider()

pg.run()
