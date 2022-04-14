from sqlite3 import Date
import requests
from datetime import datetime

GPT3_APP_ID = "79185132"
GPT3_APP_KEY = "7b377a808d7b2c7ce0679090fb8da0bc"
GENDER = "male"
AGE = "35"
DATE = datetime.now().strftime("%d/%m/%Y") # 14/04/2022
TIME = datetime.now().strftime("%H:%M:%S") # 21:46:50


##### Excercising Tracking
excercise_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endopoint = f"https://api.sheety.co/1afdc9861c39d7aea3407072f386921c/workoutTracking/workouts"

headers = {"x-app-id" : GPT3_APP_ID,
"x-app-key" : GPT3_APP_KEY}

excercise_params = {
 "query":input("Tell me which excerciese you did.")
 ,"gender":GENDER
 ,"age": AGE
}

response = requests.post(url = excercise_endpoint, json = excercise_params, headers=headers)
# print(response.text)
exercising = response.json()["exercises"][0]
# print(exercising)
name_exercising = exercising["name"]
duration_min_exercising = exercising["duration_min"]
calories_exercising = exercising["nf_calories"]
# print(name_exercising, duration_min_exercising,calories_exercising) # running 683.65 7816.4

##### Input some data in the sheet.
# sheety_params = {
# "Date":DATE
# ,"Time":TIME
# ,"Exercising":name_exercising
# ,"Duration":duration_min_exercising
# ,"Calories": calories_exercising
# }

# sheety_input = requests.post(url = sheety_endopoint, json = sheety_params)
# print(sheety_input.text)