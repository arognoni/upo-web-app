# Python Web Applications

Material for the "Python web applications" seminar.
The project can be downloaded by clicking the "code" button at the top-right corner of the page.

## Contents

- [Python Web Applications](#python-web-applications)
  - [Getting started](#getting-started)
  - [Dependencies](#dependencies)
  - [Project Organization](#project-organization)
  - [Ollama](#ollama)
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

```bat
streamlit run Home.py
```

The dashboard will be running at http://localhost:8501.

## Dependencies

The main dependencies are:
- [Streamlit](https://streamlit.io/): Dashboard framework.
- [Plotly](https://plotly.com/): Plotting library.
- [HTTPX](https://www.python-httpx.org/): HTTP client.
- [Langchain](https://www.langchain.com/): Agent library.

## Project Organization

```raw
├── README.md          <- README file.
├── requirements.txt   <- Project dependencies.
├── .gitignore         <- git-ignore configuration file.
├── Home.py            <- Dashboard main file.
├── pages
│    ├── Chat.py       <- Chat page.
│    └── Data.py       <- Data page.
└── static
     ├── data.csv           <- Data source.
     ├── uniupo-logo.svg    <- UPO logo.
     └── favicon-32x32.png  <- UPO favicon.
```

## Ollama

We use [ollama](https://ollama.com/) to run models locally. Execute

```sh
ollama run qwen3.5:2b
```

to download and lanuch Qwen 3.5-2B. If you face OOMs, try with the 0.8B:

```sh
ollama run qwen3.5:0.8b
```

We will send requests to [http://localhost:11434/api/chat](http://localhost:11434/api/chat).


## The Binance API

To get real-time cryptocurrency prices, we will use the
[Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md).
Specifically, will make GET requests to the following endpoint: [https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT](https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT). The response has the following format:

```js
{
    "symbol":"ETHUSDT",
    "price":"2322.54000000"
}
```