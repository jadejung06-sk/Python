import pandas as pd

df = pd.read_csv(r'D:\2022\Python\WebCrawling\apple_website\pandas_excel\credit.csv')
print(df)

print(df['나이'].mean())
print(df['나이'].mode())
print(df['나이'].max())
print(df['나이'].min())
print(df['나이'].describe())