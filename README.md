# Python Web Applications
Material for the "Python web applications" seminar.
The project can be downloaded by clicking the "code" button at the top-right corner of the page.

## Contents
- [Python Web Applications](#python-web-applications)
  - [Getting started](#getting-started)
  - [Dependencies](#dependencies)
  - [Project Organization](#project-organization)
  - [The Binance API](#the-binance-api)


## Getting started

To create a virtual environment named `.venv`, simply run:

```bat
python -m venv .venv
```

On Windows, execute the following command to activate it:

```bat
.venv\Scripts\activate
```

Once the environment has been activated, dependencies can be installed with pip:

```bat
pip install -r requirements.txt
```

The complete project can be found in the `complete-project` branch.
A standalone script allows one to generate the SQLite database:

```bat
python create_db.py 
```

To start the back-end API locally, execute:

```bat
fastapi dev api.py
```

Similarly, to launch the Streamlit dashboard run:

```bat
streamlit run Home.py
```

The API and dashboard default ports are `8000` and `5501`, respectively.

## Dependencies

The main dependencies are:
- [FastAPI](https://fastapi.tiangolo.com/): Used to develop the back-end API.
- [Streamlit](https://streamlit.io/): Used to develop the front-end dashboard.
- [SQLite](https://www.sqlite.org/): Built-in SQL database engine.
- [Plotly](https://plotly.com/): Plotting library.
- [HTTPX](https://www.python-httpx.org/): HTTP client.

## Project Organization

```raw
├── README.md          <- README file.
├── requirements.txt   <- Project dependencies.
├── .gitignore         <- git-ignore configuration file.
│
├── create_db.py       <- Standalone script to create the DB.
├── api.py             <- API main file.
├── Home.py            <- Dashboard main file.
├── pages
    ├── Crypto.py      <- Cryptocurrency page.
    └── Data.py        <- Data page.
```

## The Binance API

To get real-time cryptocurrency prices, we will use the
[Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md).
Specifically, will make GET requests to the following endpoint: [https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]](https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]). The data we receive is a JSON having the following shape:

```js
[
    {
        "symbol":"BTCUSDT",
        "price":"29316.60000000"
    },
    {
        "symbol":"ETHUSDT",
        "price":"1969.81000000"
    },
    {
        "symbol":"DOGEUSDT",
        "price":"0.08400000"
    }
]
```

where `symbol` represents the cryptocurrency symbol and `price` is the price in USD(T).
