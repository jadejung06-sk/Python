import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# print(response.status_code)
 
if response.status_code != 200:
    print("Error")
    raise Exception("Bad response from ISS API")

if response.status_code == 404:
    raise Exception("That resource does not exits.")
if response.status_code == 401:
    raise Exception("You are not autorised to access this data.")