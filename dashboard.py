# dashboard.py

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from text_analysis import extract_keywords_and_topics

# -------------------------------
# Simulated dataset (replace with DB or CSV later)
# -------------------------------
sample_reports = [
    {
        "location": "Voinjama",
        "message": "There is no medicine at the clinic and the children are sick.",
        "lat": 8.4218,
        "lon": -9.7476
    },
    {
        "location": "Zorzor",
        "message": "The road is damaged and schools are closed.",
        "lat": 7.7531,
        "lon": -9.2654
    },
    {
        "location": "Kolahun",
        "message": "We need water and food. The hand pump is broken.",
        "lat": 8.3306,
        "lon": -10.1521
    }
]

# -------------------------------
# Streamlit Dashboard UI
# -------------------------------
st.set_page_config(page_title="VoxCiv Dashboard", layout="wide")
st.title("📊 VoxCiv – Civic Voice Dashboard")
st.markdown("**Live insights from community feedback across Liberia**")

# -------------------------------
# Keyword Summary Table
# -------------------------------
st.subheader("🧠 Keyword Extraction")
keywords_data = []

for report in sample_reports:
    keywords = extract_keywords_and_topics(report["message"])
    keywords_data.append({"Location": report["location"], "Keywords": ", ".join(keywords)})

st.dataframe(pd.DataFrame(keywords_data))

# -------------------------------
# Geo Mapping of Reports
# -------------------------------
st.subheader("🗺️ Reports Heatmap")

map_center = [8.0, -9.5]
m = folium.Map(location=map_center, zoom_start=7)

for report in sample_reports:
    folium.Marker(
        location=[report["lat"], report["lon"]],
        popup=report["message"],
        tooltip=report["location"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

st_folium(m, width=700, height=500)

# -------------------------------
# Feedback Log Viewer
# -------------------------------
st.subheader("📄 Raw Report Logs")
for report in sample_reports:
    st.markdown(f"**{report['location']}**: {report['message']}")

