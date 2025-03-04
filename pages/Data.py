"""Dashboard data page."""

import httpx
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Data", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Data")

response = httpx.get("http://127.0.0.1:8000/data")
data = response.json()
df = pd.DataFrame.from_dict(data)
st.dataframe(df)
