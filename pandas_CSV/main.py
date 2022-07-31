import pandas as pd
PATH = "./csv_file/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
squirrel_data = pd.read_csv(PATH)

### Check Data
# print(squirrel_data.columns)
# print(squirrel_data["Primary Fur Color"])
# print(squirrel_data['Highlight Fur Color'])
# print(squirrel_data['Combination of Primary and Highlight Color'])
# print(squirrel_data['Color notes'])

### Output 
# Fur Color, Count
# grey
# red
# black

### My Code
# new_data = pd.DataFrame()
# col_list = []
# for col in squirrel_data["Primary Fur Color"].value_counts().index:
#     col_list.append(col)
# # print(col_list)
# new_data["Fur Color"] = col_list
# new_data["Fur Color"][new_data["Fur Color"] == "Cinnamon"] = 'red'
# new_data["Fur Color"] = new_data["Fur Color"].str.lower() 

# val_list = []
# for val in squirrel_data["Primary Fur Color"].value_counts():
#     val_list.append(val)
# # print(val_list)
# new_data["Count"] = val_list
# new_data.to_csv('./csv_file/squirrel_count.csv')
#####

### Study
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
data_dict = {
"Fur Color": ["grey", 'cinnamon', 'black'],
"Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
new_data2 = pd.DataFrame(data_dict)
print(new_data2)

# ### study 2
# import pandas as pd
# num_list = [5,5,5,0,0,0,1,1,1,4,4,4,5,5,5]
# data =pd.DataFrame({'num': num_list})
# print(data.drop_duplicates(keep=False))

# x = np.array([5, 5, 5, 0, 0, 0, 1, 1, 1, 4, 4, 4, 5, 5, 5, 4, 4, 4, 0, 0 ])
# result = []
# for i in range(len(x)):
#     if i==0:
#         result += [x[i]]
#         temp = x[i]
#     else:
#         if temp == x[i]:
#             pass
#         else:
#             result += [x[i]]
#             temp = x[i]
# print(result)
# import numpy as np
# import time
# x = np.array([5, 5, 5, 0, 0, 0, 1, 1, 1, 4, 4, 4, 5, 5, 5])
# print(np.insert(x[1:][np.diff(x) != 0], 0, x[0]))
# np.diff(x) the next num - the num 