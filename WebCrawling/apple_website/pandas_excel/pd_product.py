import pandas as pd
import re


raw = pd.read_excel(r'D:\2022\Python\WebCrawling\apple_website\pandas_excel\product.xlsx', engine = "openpyxl")
print("org_raw", raw)

##### new column
# raw["부가세포함"] = raw["판매가"] * 1.1
# print(raw)
# def multiply(x):
    # return x * 1.1
# raw["부가세포함"] = raw["판매가"].apply(multiply) # each rows are applied into the function 
# print(raw)

##### append new data
def category(x):
    if "Chair" in str(x):
        return "의자"
    elif "Table" in str(x):
        return "테이블"
    elif "Mirror" in str(x):
        return "거울"
    elif "Sofa" in str(x):
        return "소파"
    else:
        return "기타"
raw["카테고리"] = raw["상품목록"].apply(category)
print(raw)