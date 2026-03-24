import streamlit as st


st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
    layout="wide",
)
header_container = st.container()

col1, col2, col3 = st.columns(spec=[1, 1.8, 1])

with open("src/assets/report.md", "r", encoding="utf-8") as f:
    with col2:
        report_content = f.read()
        st.markdown("# La place de la femme dans les médias à travers les années")
        
        # Define CSS for paragraphs, lists, AND scale up headers so they stand out
        custom_css = """
        <style>
            p, li { 
                font-size: 22px !important; /* Makes normal text and lists bigger */
            }
            h1 { 
                font-size: 42px !important; /* Scales up main titles */
            }
            h2 { 
                font-size: 34px !important; /* Scales up subtitles */
            }
            h3 { 
                font-size: 28px !important; /* Scales up section titles */
            }
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown(report_content)
