"""Back-end API."""

import sqlite3
from datetime import datetime
from typing import Any

import httpx
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello() -> str:
    """FastAPI hello world.

    Returns:
        str: API response.
    """
    return "Hello world"


@app.get("/health")
def health() -> dict[str, str]:
    """API healthcheck.

    Returns:
        dict[str, str]: Response dict.
    """
    return {"status": "OK"}


@app.get("/data")
def data() -> list[dict[str, Any]]:
    """Fetch the entire DB crypto table.

    Returns:
        list[dict[str, Any]]: Database rows listing
            datetimes and cryptocurrency prices.
    """
    with sqlite3.connect("crypto.db") as conn:
        df = pd.read_sql("SELECT * FROM crypto;", conn)
    return df.to_dict(orient="records")


@app.get("/crypto/{name}")
def crypto(name: str) -> list[dict[str, Any]]:
    """Fetch the data of a single coin.

    Args:
        name (str): Coin name.

    Returns:
        list[dict[str, Any]]: Datetimes and corresponding prices.
    """
    with sqlite3.connect("crypto.db") as conn:
        df = pd.read_sql(f"SELECT Datetime,{name} FROM crypto;", conn)
    return df.to_dict(orient="records")


@app.get("/update")
def update() -> str:
    """Update prices through the Binance API.

    Returns:
        str: Success.
    """
    url = 'https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]'
    response = httpx.get(url)
    data = response.json()
    row = {coin["symbol"]: coin["price"] for coin in data}

    with sqlite3.connect("crypto.db") as conn:
        conn.execute(
            """
            INSERT INTO crypto (Datetime,Bitcoin,Dogecoin,Ethereum)
            VALUES (:datetime,:bitcoin,:dogecoin,:ethereum);
            """,
            {
                "datetime": datetime.now(),
                "bitcoin": row["BTCUSDT"],
                "dogecoin": row["DOGEUSDT"],
                "ethereum": row["ETHUSDT"],
            },
        )

    return "Success"
