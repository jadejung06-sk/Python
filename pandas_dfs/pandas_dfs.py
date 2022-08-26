import pandas as pd
import os

# print(pd.read_csv('./pandas_dfs/apps.csv'))
df = pd.read_csv('./pandas_dfs/apps.csv')
print(df.shape)
print(df.columns)
print(df.head())

# apps_1 = pd.read_csv('./pandas_dfs/apps.csv').loc[:3000,:]
# apps_2 = pd.read_csv('./pandas_dfs/apps.csv').loc[3001:6000,:]
# apps_3 = pd.read_csv('./pandas_dfs/apps.csv').loc[6001:9000,:]

# print(apps_3)
# apps_1.to_csv('./pandas_dfs/apps_1.csv', index= False)
# apps_2.to_csv('./pandas_dfs/apps_2.csv', index= False)
# apps_3.to_csv('./pandas_dfs/apps_3.csv', index= False)

# # print(os.getcwd())
# file_path = './pandas_dfs/'

# # print(os.listdir('./pandas_dfs'))
# df = pd.DataFrame()
# for file in os.listdir('./pandas_dfs'):
#     if file != 'apps.csv' and file != 'pandas_dfs.py':
#         df_tmp = pd.read_csv(file_path + file)
#         df = pd.concat([df, df_tmp])
# df.to_csv('./pandas_dfs/total_apps.csv', index = False)
tmp = pd.read_csv('./pandas_dfs/total_apps.csv')
print(tmp.shape)
print(tmp.columns)
print(tmp.head())