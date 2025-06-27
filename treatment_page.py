import streamlit as st

def display_treatment_page():
    st.title("💊 Treatment Recommendations")

    condition = st.selectbox("Choose a condition:", ["Flu", "Diabetes", "Hypertension", "Covid-19"])

    if condition == "Flu":
        st.write("- Rest")
        st.write("- Stay hydrated")
        st.write("- Paracetamol if needed")
    elif condition == "Diabetes":
        st.write("- Monitor blood sugar")
        st.write("- Low-carb diet")
        st.write("- Exercise regularly")
    elif condition == "Hypertension":
        st.write("- Low salt diet")
        st.write("- Regular BP checks")
        st.write("- Medication as prescribed")
    elif condition == "Covid-19":
        st.write("- Isolate")
        st.write("- Consult doctor immediately")
