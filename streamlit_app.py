import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import json

st.set_page_config(page_title="TCG Portfolio AI", layout="wide")
st.title("🎴 TCG Portfolio AI Client")

# 1. Your Google Sheet URL
# MAKE SURE THIS IS YOUR ACTUAL URL
SHEET_URL = " https://docs.google.com/spreadsheets/d/1sJviZ9ZkfRsQpONd08qRD4ly_CVXJyayhqx0ecCSTd0/edit?pli=1&gid=2142017253#gid=2142017253"

# 2. Setup Connection
# We are going to tell the app to look for the credentials manually
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # We pass the URL directly into the read function
    df = conn.read(spreadsheet=SHEET_URL, worksheet="Pokemon_Raw")

    st.subheader("Current Inventory: Pokémon Raw")
    st.dataframe(df)
    st.success(f"Successfully loaded {len(df)} cards!")

except Exception as e:
    st.error("Connection Failed. Let's check the settings.")
    st.write(e)
