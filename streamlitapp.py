import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="INVESMATE",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default chrome
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0; }
    [data-testid="stVerticalBlock"] { gap: 0 !important; }
</style>
""", unsafe_allow_html=True)

# Load the HTML file from the same directory as this script
html_path = os.path.join(os.path.dirname(__file__), "invesmate.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=True)
