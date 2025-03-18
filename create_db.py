import sqlite3

import pandas as pd

df = pd.read_csv("static/data.csv")
print(df.head())

with sqlite3.connect("crypto.db") as conn:
    df.to_sql("crypto", conn, index=False)
