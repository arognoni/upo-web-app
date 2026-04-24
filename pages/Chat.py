"""Chat."""

import json
from time import sleep

import httpx
import streamlit as st
from langchain.agents import create_agent
from langchain.messages import AIMessage


def get_crypto_price(coin: str) -> str:
    """Get the real-time price of a cryptocurrency using the Binance API.

    Args:
        coin (str): Cryptocurrency full name (e.g., ethereum).

    Returns:
        str: Cryptocurrency price in USDT. If the request failed,
            'unknown' is returned.
    """
    try:
        print(coin)
        symbols = {
            "bitcoin": "BTC",
            "ethereum": "ETH",
        }
        coin_symbol = symbols[coin.lower()]

        url = "https://api4.binance.com/api/v3/ticker/price"
        res = httpx.get(url, params={"symbol": f"{coin_symbol}USDT"})
        data = res.json()
        output = data["price"]
    except Exception:
        output = "unknown"

    return output


def generate_mock(agent):
    for letter in "hello, how can I help you?":
        yield letter
        sleep(0.1)


def generate_httpx():
    body = {
        "model": "qwen3.5:2b",
        "messages": st.session_state.messages,
        "stream": True,
    }
    with httpx.stream("POST", url="http://127.0.0.1:11434/api/chat", json=body) as r:
        for text in r.iter_text():
            d = json.loads(text)
            content = d["message"]["content"]
            if content:
                yield content


def generate(agent):
    for chunk in agent.stream(
        {"messages": st.session_state.messages},
        stream_mode="messages",
        version="v2",
    ):
        if chunk["type"] == "messages":
            token, _ = chunk["data"]
            content = token.content
            if content and isinstance(token, AIMessage):
                yield content


agent = create_agent(model="ollama:qwen3-vl:2b", tools=[get_crypto_price])

st.set_page_config(page_title="Home", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")
st.title("Home")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


message = st.chat_message("assistant")
message.write("hello human")

if prompt := st.chat_input("What's up?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        response = st.write_stream(generate(agent))

    st.session_state.messages.append({"role": "assistant", "content": response})
