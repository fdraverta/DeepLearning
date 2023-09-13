# conda install -c conda-forge yfinance
from datetime import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_data_for_ticker(ticker, start_date='1800-01-01', end_date=None):
  end_date = end_date if end_date is not None else datetime.today()
  data_by_day = yf.download([ticker], start_date, end_date)
  data_by_day["net_returns"] = (data_by_day["Close"] - data_by_day["Open"])  / data_by_day["Open"]

  return data_by_day

def create_hist(data, xlabel, title, path_to_save=None, bins=100):
  ax = data.hist(bins=bins)
  ax.set_title(title)
  ax.set_xlabel(xlabel)
  ax.set_ylabel("Frecuency")
  return ax

ticker = 'AAPL'
sp500 = fetch_data_for_ticker(ticker)

create_hist(sp500["net_returns"],
              title=f"{ticker} Daily Net Returns",
              xlabel=f"{ticker} Net Returns",
              bins=100)

plt.show()