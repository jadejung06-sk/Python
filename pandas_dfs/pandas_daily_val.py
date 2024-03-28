import pandas as pd


df = pd.read_csv(r'D:\2022\Python\pandas_dfs\daily_values.csv')

### pd.to_datetime()
# df.work_dt = pd.to_datetime(df.work_dt)
# df.out_dt = pd.to_datetime(df.out_dt)
# df.bf_out_dt = pd.to_datetime(df.bf_out_dt)
print(df.info())
out_dt = list(df.out_dt)
print(out_dt)

