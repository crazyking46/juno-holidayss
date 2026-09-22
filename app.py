import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Juno Holidays — Travel Is For Everyone",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Make Streamlit look like a normal full-screen website.
st.markdown(
    """
    <style>
        #MainMenu { visibility: hidden; }
        header { visibility: hidden; }
        footer { visibility: hidden; }
        [data-testid="stToolbar"] { visibility: hidden; height: 0; }
        [data-testid="stDecoration"] { display: none; }
        [data-testid="stHeader"] { display: none; }
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        .stApp {
            background: #06111F;
        }
        iframe {
            display: block !important;
            width: 100% !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "juno-holidays.html"

if not HTML_FILE.exists():
    st.error("juno-holidays.html is missing. Keep it in the same folder as app.py.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

# The original website is rendered inside Streamlit.
# All HTML/CSS/JavaScript interactions remain inside the component.
components.html(
    html,
    height=6500,
    scrolling=True,
)
