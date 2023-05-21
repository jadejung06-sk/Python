import pandas as pd
import yfinance as yf
yf.pdr_override()
from pandas_datareader import data

##### stock data
df1 = data.get_data_yahoo('AAPL', '2020-01-01', '2022-01-01')
print(df1)
print(df1['Close'])
df1['Close'].plot()

df2 = data.get_data_yahoo('005930.KS', '2020-01-01', '2022-01-01')
print(df2)
print(df2['Close'])
# df2['Close'] = df2['Close'].astype(float)
df2['Close'].plot()
#####################

##### rolling mean (removal of daily noise)
df2['rolling5'] = df2['Close'].rolling(5).mean()
df2['rolling20'] = df2['Close'].rolling(20).mean()
df2['rolling60'] = df2['Close'].rolling(60).mean()
print(df2)
df2['rolling5'].plot()
df2['rolling20'].plot()
df2['rolling60'].plot()