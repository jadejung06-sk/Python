import pandas as pd


df = pd.read_csv(r'D:\2022\Python\pandas_dfs\daily_values.csv')


##### Q1 : datetime adds integer
## >>> pd.to_datetime( Series ) +  Series.apply(lambda x : pd.DateOffset(days = int(x) ))  
df['x_val'] = 2
df.work_dt = pd.to_datetime(df.work_dt)
df['xy_1'] = (df['x_val'] * df['y_val']).round() # .astype(int) 버림 처리가 되므로 .round()함수 사용 필요
df['out_date2'] = df['work_dt'] + df['xy_1'].apply(lambda x : pd.DateOffset(days = x)) ## 필요 부분 확인 종료 (데이터 확인 포함)
########################################

##### Q2 : lead 
## >>> https://statwith.tistory.com/3073
df['xy_2'] = None
df['xy_2'] = df['y_val'].shift(periods= 1) # idx 193 (idx192) 
df['xy_2'] = df['y_val'].shift(periods= -1) # idx 193 (idx194) 
## Oracle Sql
# LEAD(sal, 1, 0) OVER (partition by job ORDER BY hiredate) AS prev_sal
## Python
# withmooc['sal_lag'] = emp.sort_values(by='hiredate').groupby('job')['sal'].shift(-1,fill_value = 0)
### / LEAD(sal, 1, 0) == ['sal'].shift(-1, fill_value = 0)
### / partiton by job == .groupby('job')
### / order by hiredate == .sort_values(by = 'hiredate') 


print(df.info())
print(df.tail(5))




