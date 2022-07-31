import pandas as pd
import os
os.getcwd()
data = pd.read_csv('./wedding/wedding_hall.csv', header=None)
name = data[0][data[0].str.startswith("*")].reset_index(drop = True)
link = data[0][data[0].str.startswith("h")].reset_index(drop = True)
time = data[0][data[0].str.startswith("잔여")].reset_index(drop = True)
people = data[0][data[0].str.startswith("최소")].reset_index(drop = True)
hall = data[0][data[0].str.startswith("홀대")].reset_index(drop = True)
lunch = data[0][data[0].str.startswith("식대")].reset_index(drop = True)

hall_excel = pd.DataFrame({"name": name, 'link':link, 'time': time, 'people':people, 'hall':hall, 'lunch':lunch})
hall_excel.to_csv("hall_excel.csv", index = False, encoding = 'cp949')