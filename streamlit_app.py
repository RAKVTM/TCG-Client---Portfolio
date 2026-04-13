import streamlit as st 
import pandas as pd

st.set_page_config(page_title="TCG Portfolio Pro", layout="wide")

st.title("📊 TCG Portfolio AI Client")
st.info("Direct Upload Mode: Upload your CSV to begin analysis.")

# 1. File Uploader (Accepts your Pokemon/MTG files)
uploaded_file = st.file_uploader("Upload your Collection CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # 2. Display the data
    st.subheader("Inventory Preview")
    st.dataframe(df.head(10))
    
    # 3. The "No Extrapolation" Check
    st.divider()
    st.subheader("Market Verification")
    
    # Selection for analysis
    selected_card = st.selectbox("Select a card to verify against Live Sources:", df['Product Name'].unique())
    
    if st.button("Run Verified Analysis"):
        st.warning(f"Connecting to TCGPlayer & eBay APIs for {selected_card}...")
        # This is where we will plug in the Search logic next
        st.write("Verification Status: [Pending API Key Integration]")
