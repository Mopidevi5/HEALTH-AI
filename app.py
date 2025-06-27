import streamlit as st
from components.analytics_page import display_analytics_page
from components.chat_page import display_chat_page
from components.prediction_page import display_prediction_page
from components.treatment_page import display_treatment_page

st.set_page_config(page_title="HealthAI - Intelligent Assistant", layout="wide")
st.sidebar.title("🩺 HealthAI Navigation")

page = st.sidebar.radio("Choose a section:", [
    "Analytics",
    "Patient Chat",
    "Disease Prediction",
    "Treatment Plans"
])

if page == "Analytics":
    display_analytics_page()
elif page == "Patient Chat":
    display_chat_page()
elif page == "Disease Prediction":
    display_prediction_page()
elif page == "Treatment Plans":
    display_treatment_page()
