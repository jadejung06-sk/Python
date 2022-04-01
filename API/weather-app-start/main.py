import requests
'''
https://openweathermap.org/api/one-call-api
https://www.latlong.net/
parameters exclude : It should be a comma-delimited list (without spaces). # ★
'''
city_name = 'icheon'
lat = 37.271996
lon = 127.434822
API_key = "d5cb186b7ada6023a3a24d4b1b6cafa4" # ★

OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
basic_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
city_api = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

weather_params = {
    "lat":lat
    ,"lon":lon
    ,"appid":API_key
    ,"exclude":"current,minutely,daily"
}

response = requests.get(url= OWN_Endpoint, params=weather_params)
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
    # print(weather)
    for hour, data_weather in enumerate(hourly_weather[0:11]):
        weather_id = data_weather['weather'][0]['id']
        # print(hour, f"id : {weather_id}")
        if weather_id < 700:
            will_rain = True
        else:
            list_weather.append(weather_id)
    # print(list_weather)

## if it rains, print out!
if will_rain:
    print(f"Bring your umbrella!")
else:
    print("Happy day! Good weather.")

