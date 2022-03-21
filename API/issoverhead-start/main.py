import requests
from datetime import datetime

MY_LAT = 37.271996 # Your latitude
MY_LONG = 127.434822 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
# 37.271996 127.434822

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
# 8.8897 -103.2459
close_to_lat = abs(iss_latitude - MY_LAT)
close_to_long = abs(iss_longitude-MY_LONG)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
if close_to_lat < 5 and close_to_long <5:
     print(sunrise)
     

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



