import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(
    page_title="Worldwide Conflicts Dashboard Analysis",
    layout="wide"
)




overview = st.Page("overview.py", title="Overview", icon="🔎")
detailed_analysis = st.Page("detailed_analysis.py", title="Detailed Analysis", icon="📊")

pg = st.navigation([
    overview,
    detailed_analysis
])

pg.run()


