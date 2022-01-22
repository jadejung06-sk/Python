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
print(data["temp"])
