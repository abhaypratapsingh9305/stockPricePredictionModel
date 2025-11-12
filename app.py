# stock_app.py

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load the trained stock model
with open("Stock_price_model.pkl", "rb") as f:
    rf = pickle.load(f)

# Page settings
st.set_page_config(page_title="📈 Stock Price Predictor", layout="wide")

# Title
st.title("📊 Stock Price Prediction App")
st.markdown("Enter market values below to predict the stock's **adjusted close price**.")

st.markdown("---")

# Input form
with st.form("prediction_form"):
    st.subheader("🔢 Enter Stock Market Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        open_val = st.number_input("🔹 Open", min_value=0.0, value=100.0, step=1.0)
        high_val = st.number_input("🔹 High", min_value=0.0, value=105.0, step=1.0)

    with col2:
        low_val = st.number_input("🔹 Low", min_value=0.0, value=98.0, step=1.0)
        adj_close_val = st.number_input("🔹 Adj Close", min_value=0.0, value=102.0, step=1.0)

    with col3:
        volume_val = st.number_input("🔹 Volume", min_value=0.0, value=1000000.0, step=10000.0)

    submitted = st.form_submit_button("📈 Predict Price")

# Prediction
if submitted:
    input_data = pd.DataFrame({
        'Open': [open_val],
        'High': [high_val],
        'Low': [low_val],
        'Adj Close': [adj_close_val],
        'Volume': [volume_val]
    })

    prediction = rf.predict(input_data)[0]

    st.markdown("---")
    st.success(f"🎯 **Predicted Adjusted Close Price: ₹ {prediction:,.2f}**")
