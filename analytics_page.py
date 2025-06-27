import streamlit as st
import pandas as pd
import os

def load_analytics_data():
    try:
        data = pd.read_csv("data/analytics_data.csv")  # ✅ Correct placement
        return data
    except Exception as e:
        st.error(f"Failed to load analytics data: {e}")
        return pd.DataFrame()

def display_analytics_page():
    st.title("📊 Analytics Dashboard")

    data = load_analytics_data()

    st.write("🔍 Columns found:", data.columns.tolist())

    if data.empty:
        st.warning("No analytics data available to display.")
        return

    if "Region" not in data.columns or "Count" not in data.columns:
        st.error("Required columns 'Region' and 'Count' not found.")
        return

    st.subheader("🗺️ Disease Count by Region")
    region_data = data.groupby("Region")["Count"].sum().sort_values(ascending=False)
    st.bar_chart(region_data)

    st.subheader("📄 Full Analytics Data")
    st.dataframe(data)
