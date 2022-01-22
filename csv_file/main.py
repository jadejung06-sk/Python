import pandas as pd
PATH = "./csv_file/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pd.read_csv(PATH)
print(squirrel_data.columns)
print(squirrel_data["Primary Fur Color"])
print(squirrel_data['Highlight Fur Color'])
print(squirrel_data['Combination of Primary and Highlight Color'])
# print(squirrel_data['Color notes'])