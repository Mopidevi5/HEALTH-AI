### components/prediction_page.py

import streamlit as st
from utils.prediction_utils import predict_disease

def display_prediction_page():
    st.header("🩺 Disease Prediction")
    symptoms = st.text_input("Enter symptoms separated by commas")
    if symptoms:
        prediction = predict_disease(symptoms)
        st.success(f"Predicted Disease: {prediction}")