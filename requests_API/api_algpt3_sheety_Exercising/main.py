import requests
from datetime import datetime
import os

GPT3_APP_ID = ""
GPT3_APP_KEY = ""
SHEET_USERNAME = ""
SHEET_AUTH_ID = ""

GENDER = "male"
AGE = "35"
DATE = datetime.now().strftime("%d/%m/%Y") # 14/04/2022
TIME = datetime.now().strftime("%X") #★ 21:46:50
print(type(DATE), type(TIME), TIME)

##### Excercising Tracking
excercise_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endopoint = f"https://api.sheety.co/{SHEET_USERNAME}/workoutTracking/workouts"

headers = {"x-app-id" : GPT3_APP_ID,
"x-app-key" : GPT3_APP_KEY
}

excercise_params = {
 "query":input("Tell me which excerciese you did: ")
 ,"gender":GENDER
 ,"age": AGE
}
#########################

### gpt3 api
response = requests.post(url = excercise_endpoint, json = excercise_params, headers=headers)
# print(response.text)
exercising = response.json()["exercises"][0]
# print(exercising)
name_exercising = exercising["name"]
duration_min_exercising = exercising["duration_min"]
calories_exercising = exercising["nf_calories"]
# print(name_exercising, duration_min_exercising,calories_exercising) # running 683.65 7816.4
# print(name_exercising, type(duration_min_exercising),type(calories_exercising)) # running <class 'float'> <class 'float'>
#####################################

##### Input some data in the sheet.

sheety_header = { 
"Authorization" : "Basic "
}

sheety_params = {
  "workout": 
    {
      "date": DATE,
      "time": TIME,
      "exercise": name_exercising.title(),
      "duration": duration_min_exercising,
      "calories": calories_exercising
    }
}
# print(sheety_params)
# sheety_get = requests.get(url= sheety_endopoint)
# print(sheety_get.text)
sheety_input = requests.post(url = sheety_endopoint, json = sheety_params, headers=sheety_header)
print(sheety_input.text)
#########################
