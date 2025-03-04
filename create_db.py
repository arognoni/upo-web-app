"""Standalone script to generate the SQLite DB."""

import sqlite3

import pandas as pd

with open("static/data.csv") as f:
    df = pd.read_csv(f)

with sqlite3.connect("crypto.db") as conn:
    df.to_sql("crypto", conn, index=False)
