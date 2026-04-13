import streamlit as st 
import pandas as pd
import urllib.parse

st.set_page_config(page_title="TCG Portfolio Pro", layout="wide")

st.title("📊 TCG Portfolio AI Client (Verified Mode)")

uploaded_file = st.file_uploader("Upload your Collection CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Inventory Preview")
    st.dataframe(df.head(10))
    
    st.divider()
    
    # Selection for analysis
    st.subheader("Market Verification (Manual Cross-Check)")
    selected_card = st.selectbox("Select a card:", df['Product Name'].unique())
    
    # Generate search queries
    query = urllib.parse.quote(selected_card)
    tcg_url = f"https://www.tcgplayer.com/search/all/product?q={query}"
    ebay_url = f"https://www.ebay.com/sch/i.html?_nkw={query}&LH_Sold=1&LH_Complete=1"

    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("View on TCGPlayer", tcg_url)
        st.caption("Check 'Market Price' for base value.")
        
    with col2:
        st.link_button("View eBay Sold Listings", ebay_url)
        st.caption("Check most recent 'Sold' prices for liquidity.")

    # Data Entry for the AI
    st.divider()
    st.write("Enter the found prices below for AI Portfolio Analysis:")
    tcg_p = st.number_input("Found TCG Market Price ($)", value=0.0)
    ebay_p = st.number_input("Found eBay Sold Average ($)", value=0.0)
    
    if tcg_p > 0 and ebay_p > 0:
        spread = ((tcg_p - ebay_p) / tcg_p) * 100
        st.metric("Price Variance (Spread)", f"{spread:.2f}%")
        
        if spread > 15:
            st.error("High Spread Alert: TCG Market is significantly higher than actual sales. Value may be inflated.")
        else:
            st.success("Stable Value: Market and Sales are closely aligned.")

