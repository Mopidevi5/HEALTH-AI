import streamlit as st

def display_chat_page():
    st.title("💬 Patient Chat")
    user_input = st.text_input("Ask your health-related question:")

    if user_input:
        # Simple simulated response
        response = f"🤖 Based on your input '{user_input}', please consult a physician for more detailed advice."
        st.success(response)
