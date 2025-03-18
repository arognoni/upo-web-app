import streamlit as st

st.set_page_config("Crypto", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")

name = st.sidebar.selectbox(
    "Select cryptocurrency:", options=["Bitcoin", "Dogecoin", "Ethereum"]
)

st.title(name)
