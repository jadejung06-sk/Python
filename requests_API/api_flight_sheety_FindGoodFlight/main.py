#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
data_mg = DataManager()
flight_search = FlightSearch()
sheet_name = data_mg.response_get.json()["prices"]
city_list = []
for data in sheet_name:
    city_list.append(data["city"])
# print(city_list)
IATA_list = []
for city in city_list:
    IATA = flight_search.get_IATA_cd(city)
    IATA_list.append(IATA)
# print(IATA_list)
# print(sheet_name)

##### New sheet
### method 1 : put into a dic 
# for row in sheet_name:
#     row['iataCode'] = 'Testing'
# print(sheet_name)
### method 2 : put into a dic
for idx, row in enumerate(sheet_name):
    row['iataCode'] = IATA_list[idx]
print(sheet_name)