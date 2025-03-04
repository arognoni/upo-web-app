"""Dashboard cryptocurrency page."""

import httpx
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Cryptocurrencies", page_icon="static/favicon-32x32.png"
)
st.logo("static/uniupo-logo.svg", size="large")

name = st.sidebar.selectbox(
    "Select cryptocurrency", options=["Bitcoin", "Dogecoin", "Ethereum"]
)

st.title(name)

# Update all prices
if st.button("Update", type="primary"):
    httpx.get("http://127.0.0.1:8000/update")

# Fetch the crypto data
response = httpx.get(f"http://127.0.0.1:8000/crypto/{name}")
data = response.json()
df = pd.DataFrame.from_dict(data)

# Print Crypto information
price = df[name].iloc[-1]
dt = df["Datetime"].iloc[-1]
st.text(f"Current price: {price} USD")
st.text(f"Updated at: {dt}")

# Plot
figure = px.line(df, x="Datetime", y=name, color_discrete_sequence=["#d92626"])
st.plotly_chart(figure)
