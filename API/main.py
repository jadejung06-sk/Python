import requests
from datetime import datetime


# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# # print(response.status_code)

# data = response.json()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# if response.status_code != 200:
#     print("Error")
#     raise Exception("Bad response from ISS API")

# if response.status_code == 404:
#     raise Exception("That resource does not exits.")
# if response.status_code == 401:
#     raise Exception("You are not autorised to access this data.")

MY_LAT = 51.507351
MY_LONG = -0.127758
SUNRISE_API = "https://api.sunrise-sunset.org/json"
parameters = {'lat': MY_LAT, 
    'lng':MY_LONG,
    'formatted':0 } # ★
# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400 dict

response = requests.get(SUNRISE_API, params=parameters) #?=
response.raise_for_status()
json_data = response.json()
sunrise = json_data['results']["sunrise"].split('T')[1].split(":")[0]
sunset = json_data['results']["sunset"].split('T')[1].split(":")[0]

time_now = datetime.now()
print(time_now.hour)