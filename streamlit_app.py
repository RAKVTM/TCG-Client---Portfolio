import streamlit as st 
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="TCG Portfolio AI", layout="wide")
st.title("🎴 TCG Portfolio AI Client")

# 1. Establish Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# 2. Read the Data (Notice we put the URL directly here now)
# REPLACE the URL below with your actual Google Sheet URL
url = "https://docs.google.com/spreadsheets/d/1sJviZ9ZkfRsQpONd08qRD4ly_CVXJyayhqx0ecCSTd0/edit#gid=0"

df = conn.read(spreadsheet=url, worksheet="Pokemon_Raw")

# 3. Display the Data
st.subheader("Current Inventory: Pokémon Raw")
st.dataframe(df)
st.success(f"Successfully loaded {len(df)} cards!")
