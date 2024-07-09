import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\2022\Python\pandas\pandas_convertSQL\insert_values.csv')
# df['rev'] = 'BASE'
# df['gbn'] = '1RP'
# df.to_csv(r'D:\2022\Python\pandas\pandas_convertSQL\insert_values.csv')

##### merge
## method 1 : apply func
print(df.columns)
df_gbn = df.loc[(df['gbn'] == '2RP') & (df['pgrm_nm'] == 'pg11'), ['location', 'pgrm_nm', 'rev', 'y_val']]
print(df_gbn)
print(df[df['y_val'].isna()])
df_tmp = pd.merge(left = df, right = df_gbn, on = ['location', 'rev'], how = 'left', suffixes= [None, '_pg11'])
def insert_val(val, val_pg11):
    if val == np.nan:
        return val_pg11
    return val_pg11
df_tmp['y_val'] = df_tmp.apply(lambda x : insert_val(x['y_val'], x['y_val_pg11']), axis = 1, result_type='expand' )
print(df_tmp)
# print(df_tmp.isnull().sum())

## method 2 : func
# df_tmp['y_val'] = insert_val(df_tmp['y_val'], df_tmp['y_val_pg11'])
# print(df_tmp.isnull().sum())
