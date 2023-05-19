import pandas as pd


raw = pd.read_excel(r'D:\2022\Python\WebCrawling\apple_website\pandas_excel\product.xlsx', engine = "openpyxl")
print(raw)
