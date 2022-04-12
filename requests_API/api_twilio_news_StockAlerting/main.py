STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from datetime import datetime, timedelta
import numpy as np
'''
https://www.alphavantage.co/
https://newsapi.org/
https://www.twilio.com/
'''
## STEP 1: Use https://www.alphavantage.co
def check_price(stock_param):
    '''
    When STOCK price increase/decreases by 5%  between yesterday and the day before yesterday then print("Get News").
    '''
    ### convert a today & yesterday date format
    format = '%Y-%m-%d'
    # today = datetime.today().strftime(format)
    yesterday = (datetime.today() - timedelta(days=1)).strftime(format)
    two_days_ago = (datetime.today() - timedelta(days=2)).strftime(format)
    ### get stock data
    STOCK_API = "https://www.alphavantage.co/query?"
    # stock_param = {"function" : "TIME_SERIES_DAILY", 
    # "symbol":"IBM", 
    # "apikey":"demo"}
    if requests.get(STOCK_API).status_code == 200:
        print("\t\t<<Good Connection>>")
        daily_stock_data = requests.get(STOCK_API, params=stock_param).json()['Time Series (Daily)']
        open_time = '1. open'
        close_time = '4. close'
        yesterday_price = float(daily_stock_data[yesterday][close_time])
        two_days_ago_price = float(daily_stock_data[two_days_ago][close_time])
        gap_price = two_days_ago_price - yesterday_price
        percent_gap = gap_price / two_days_ago_price
        if percent_gap > 0.05:
            print("Get Positive News")
            return (np.round(percent_gap * 100,2), True)
        elif percent_gap < -0.05:
            print("Get Negative News")
            return (np.round(percent_gap * 100,2), True)
        else:
            print("Pass")
            return (np.round(percent_gap * 100,2), False)
# daily_stock_data = requests.get(STOCK_API, params=stock_param).json()['Time Series (Daily)']
# data_list = [value for (key, value) in daily_stock_data.items()]

### Get my own API key
### Need to change a symbol of TSLA
percent = check_price(stock_param = {"function" : "TIME_SERIES_DAILY", 
    "symbol":"IBM", 
    "apikey":"demo"})

## STEP 2: Use https://newsapi.org
def get_news(news_param):
    '''
    Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    '''
    NEWS_API = "https://newsapi.org/v2/everything?"
    news_json = requests.get(url = NEWS_API, params= news_param).json()
    top3_news = news_json["articles"][:3]
    news_headline = "title"
    news_brief = "description"
    for news in top3_news:
        print(f"TSLA: {percent[0]}%\nHeadline: {news[news_headline]}\nBrief: {news[news_brief]}\nor\n")

NEWS_API_KEY = "41feb7f101bf466abf8307456c09b49b"
news_param = {
    "q":"tesla",
    "from":"2022-04-06",
    "apiKey":NEWS_API_KEY
}
if percent[1]:
    get_news(news_param=news_param)
else:
    print("End")


## STEP 3: Use       instead of https://www.twilio.com 
# Send a seperate message with the percentage change and each article's title and description to your phone number. 






#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

