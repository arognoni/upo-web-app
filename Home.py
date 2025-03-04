"""Dashboard main file."""

import httpx
import streamlit as st


def healthcheck() -> bool:
    """Check the API health.

    Returns:
        bool: `True` if the check succeeded.
    """
    try:
        response = httpx.get("http://127.0.0.1:8000/health")
        return response.is_success
    except httpx.HTTPError:
        return False


st.set_page_config(page_title="Home", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Home")
if healthcheck():
    st.success("Service up and running")
else:
    st.error("Service unavailable")
