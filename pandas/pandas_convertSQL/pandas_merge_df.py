import pandas as pd
from datetime import datetime, timedelta


##### Dataset
start_date = datetime.strptime('2023-02-01', '%Y-%m-%d').date()
numdays = 100
dates = [start_date + timedelta(days=x) for x in range(numdays)]
date_list = []
for date in dates:
    date_list.append(date)
    # print(date)
date = pd.DataFrame(date_list, columns=['day'])
date['yearmonth'] = date['day'].apply(lambda x : str(x)[:4] + str(x)[5:7])
print(date)
df_tmp = pd.read_csv('./pandas/pandas_convertSQL/merge_values.csv')
df_tmp['ym'] = df_tmp['ym'].astype('str')
print(date.dtypes)
print(df_tmp.dtypes)
df = pd.merge(left = df_tmp, right = date, how = 'right', left_on = 'ym', right_on = 'yearmonth')
# df_tmp.drop(columns = ['work_dt', 'out_dt', 'bf_out_dt', 'Unnamed: 0'], inplace = True, axis= 1)
# df_tmp['ym'] = '202302'
# df_tmp.to_csv('./pandas/pandas_convertSQL/merge_values.csv', index = False)
##### 
print(df_tmp.shape)
print(df.shape)
print(df_tmp)
print(df)
df.to_csv('./pandas/pandas_convertSQL/merged_values.csv', index = False)