PATH = './csv_file/weather_data.csv'
### method 1
# with open(PATH) as data_file:
#     data = data_file.readlines()
#     print(data)

### method 2
# import csv
# with open(PATH) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp': # ★
#             temperatures.append(int(row[1]))
#     print(temperatures)

### method 3
import pandas as pd
data = pd.read_csv(PATH)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()

### Func.
# print(len(temp_list))
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean(), data["temp"].max(), data["temp"].min())

### Get data in columns
# print(data["condition"])
# print(data.condition)

### Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = monday.temp 
day_max = data[data.temp == data.temp.max()]
print(monday_temp * 9 / 5 + 32)
print(day_max.temp * 9 / 5 + 32)

## (0°C × 9/5) + 32 = 32°F
