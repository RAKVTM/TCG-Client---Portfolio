import streamlit as st 
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="TCG Portfolio AI", layout="wide")
st.title("🎴 TCG Portfolio AI Client")

# 1. Establish Connection
conn = st.connection("gsheets", type=GSheetsConnection)

# 2. Read the Pokémon Raw tab
df = conn.read(worksheet="Pokemon_Raw")

# 3. Display the Data
st.subheader("Current Inventory: Pokémon Raw")
st.dataframe(df)
st.success(f"Successfully loaded {len(df)} cards!")
