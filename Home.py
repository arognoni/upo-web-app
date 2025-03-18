import httpx
import streamlit as st


def healthcheck():
    response = httpx.get("http://127.0.0.1:8000/health")
    return response.is_success


st.set_page_config("Home", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Home")

if healthcheck():
    st.success("Service is up and running!")
else:
    st.error("Service unavailable.")
