import pandas as pd
import yfinance as yf
yf.pdr_override()
from pandas_datareader import data


df1 = data.get_data_yahoo('AAPL', '2020-01-01', '2022-01-01')
print(df1)

df2 = data.get_data_yahoo('005930.KS', '2020-01-01', '2022-01-01')
print(df2)