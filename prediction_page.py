import streamlit as st

def display_prediction_page():
    st.title("🧠 Disease Prediction")

    symptoms = st.text_input("Enter your symptoms (comma-separated):")

    if symptoms:
        # Simple simulated logic
        st.info(f"Symptoms received: {symptoms}")
        st.success("🩺 Possible condition: Flu (simulated output)")
