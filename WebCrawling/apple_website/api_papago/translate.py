from api_papago import translate
import pandas as pd


data = pd.read_excel(r"D:\2022\Python\WebCrawling\apple_website\api_papago\english-1.xlsx", engine= "openpyxl")

##### iterrows
# # print(data['english'][0])
# for i, row in data.iterrows(): # DataFrame.iterows()
#     # print(i) # 0
#     # print(row) # '''english    Life begins at the end of your comfort zone. korean                                              NaN'''
#     # print(row['english'])
#     data.loc[i, 'korean'] = translate(row['english'])
# print(data)

##### itertuples
for tu in data.itertuples():
    data.loc[tu.Index, 'korean']  = translate(tu.english) # Pandas(Index=0, english='Life begins at the end of your comfort zone.', korean=nan)
# for i, a, b in data.itertuples():
    # data.loc[i, 'korean']  = translate(a)
    # print(i, a, b)
#########################

# data.to_excel(r"D:\2022\Python\WebCrawling\apple_website\api_papago\output.xlsx")
# data.to_csv(r"D:\2022\Python\WebCrawling\apple_website\api_papago\out.csv", encoding= 'cp949')