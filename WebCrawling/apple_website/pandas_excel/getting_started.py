##### stock data
## pip install
'''
pip install pandas_datareader
'''

##### yahoo
## TypeError: string indices must be integers
# df1 = data.DataReader('AAPL',  'yahoo', start = '2020-1-1', end = '2023-1-1') 
# print(df1)
'''
pip install yfinance
import yfinance as yf
yf.pdr_override()
'''

## 1 Failed download:
## - AAPL: ValueError("time data 'yahoo' does not match format '%Y-%m-%d'")
## Empty DataFrame
# df1 = data.DataReader('AAPL',  'yahoo',  '2020-1-1')
# >>> https://www.learnpythonwithrune.org/fix-get_data_yahoo-from-pandas-datareader/
'''
df1 = data.get_data_yahoo('AAPL', '2020-01-01', '2022-01-01')
'''


## 1 Failed download:
## - 005930: No timezone found, symbol may be delisted
## Empty DataFrame
# >>> https://wikidocs.net/4370
'''
df2 = data.get_data_yahoo('005930.KS', '2020-01-01', '2022-01-01')
'''