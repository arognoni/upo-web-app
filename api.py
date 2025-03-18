import sqlite3

import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return "Hello, world!"


@app.get("/health")
def health():
    return {"status": "OK"}


@app.get("/data")
def data():
    with sqlite3.connect("crypto.db") as conn:
        df = pd.read_sql("SELECT * FROM crypto;", conn)
    return df.to_dict(orient="records")
