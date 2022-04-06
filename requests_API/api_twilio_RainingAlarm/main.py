import requests
from twilio.rest import Client 
import os

'''
https://openweathermap.org/api/one-call-api
https://www.latlong.net/
parameters exclude : It should be a comma-delimited list (without spaces). # ★
'''
## a city
city_name = "icheon"
# lat = 37.271996
# lon = 127.434822
## rainy city
# lat = 35.689487
# lon = 139.691711
## Pyeongtek
lat = 37.056981
lon = 127.052946

# export OWM_API_KEY="d5cb186b7ada6023a3a24d4b1b6cafa4"
# os.environ['OWM_API_KEY'] = 'd5cb186b7ada6023a3a24d4b1b6cafa4'
API_key = "d5cb186b7ada6023a3a24d4b1b6cafa4" # ★
# API_key =os.getenv("OWM_API_KEY")

## twilio 
account_sid = "AC0bd2928a5eb6edb1e2252288e6ac8369" 
auth_token = "978c044bb35b015f1b9cfa7c52992e57"
# auth_token = os.getenv("OWM_AUTH_TOKEN")

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/onecall"
basic_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
city_api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

weather_params = {
    "lat":lat
    ,"lon":lon
    ,"appid":API_key
    ,"exclude":"current,minutely,daily"
}

response = requests.get(url= OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)
list_weather = []
will_rain = False

if response.status_code == 200:
    # print(response.json())
    hourly_weather = response.json()["hourly"]
    # print(len(hourly_weather))
## next 12 hours
# for weather in hourly_weather[0:11]:
    for hour, data_weather in enumerate(hourly_weather[0:11]):
        weather_id = data_weather["weather"][0]["id"]
        # print(hour, f"id : {weather_id}")
        if weather_id < 700:
            will_rain = True
        else:
            list_weather.append(weather_id)
    # print(list_weather)

## if it rains, print out!
if will_rain:
    print(f"Bring your umbrella!")
    client = Client(account_sid, auth_token) 
    message = client.messages.create(body=f"It's going to rain today. Remember to bring an umbrella", from_ = "+13156591997", to='+821090378136' )
    print(message.sid) 
else:
    print("Happy day! Good weather.")