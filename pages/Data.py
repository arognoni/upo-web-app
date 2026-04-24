"""Dashboard data page."""

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Data", page_icon="static/favicon-32x32.png", layout="wide"
)
st.logo("static/uniupo-logo.svg", size="large")
st.title("Data")

df = pd.read_csv("static/data.csv")

name = st.sidebar.selectbox(
    "Select cryptocurrency", options=["Bitcoin", "Dogecoin", "Ethereum"]
)

c1, c2 = st.columns(2)

c1.dataframe(df[["Datetime", name]])
figure = px.line(df, x="Datetime", y=name, color_discrete_sequence=["#d92626"])
c2.plotly_chart(figure)
