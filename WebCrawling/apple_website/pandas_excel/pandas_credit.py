import pandas as pd

df = pd.read_csv(r'D:\2022\Python\WebCrawling\apple_website\pandas_excel\credit.csv')
print(df)

##### statistic
print(df['나이'].mean())
print(df['나이'].mode())
print(df['나이'].max())
print(df['나이'].min())
# print(df['사용금액', '사용횟수'].describe())

##### aggregation
print(df.groupby('성별').mean())
print(df[['나이', '사용금액']].corr())


##### filter, query
print(df[df['나이'] > 50])
# print(df.query(" 나이 > 50 and 기혼 == 'Married' and 성별 == 'M' "))
print(df['기혼'].value_counts())
print(df['성별'].value_counts())
print(df.query(" 기혼 == 'Married' and 성별 == 'M' ").mean()) # higher
print(df.query(" 기혼 == 'Single' and 성별 != 'M' ").mean())


def get_price(x):
    if 'Less' in x:
        return 20000
    elif '$80K - $120K' == x:
        return 80000
    elif '$60K - $80K' == x:
        return 60000
    elif '$40K - $60K' == x:
        return 40000
    elif '$120K + '== x:
        return 120000
    else:
        return 0
df['소득액'] = df['소득'].apply(lambda x: get_price(x))
# print(df.sort_values(by = '소득액', ascending = False))
print(df.groupby('소득액').mean())

'''
Less than $40K    51
$80K - $120K      45
$60K - $80K       37
$40K - $60K       28
$120K +           22
Unknown           17
'''

##### Dict to DataFrame
# years = [15, 20, 25]
# height = [160, 170, 180]

# dic = {'years': years,
#        'height': height}

# df2 = pd.DataFrame(dic)
# print(df2)
#######################

