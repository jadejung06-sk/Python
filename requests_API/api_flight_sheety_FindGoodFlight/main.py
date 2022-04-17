#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

##### get IATA 
data_mg = DataManager()
flight_search = FlightSearch()
sheet_name = data_mg.response_get.json()["prices"]
city_list = []
original_data = {}
for data in sheet_name:
    print(data)
    city_list.append(data["city"])
    original_data[data["iataCode"]] = (data["lowestPrice"], data['id']) # ★
# print(original_data) 
# >>> {'PAR': (9999999, 2), 'BER': (9999999, 3), 'SYD': (9999999, 4), 'NYC': (9999999, 5), 'SFO': (9999999, 6), 'SEL': (9999999, 7), 'GMP': (9999999, 8), 'ICN': (9999999, 9), 'ROM': (9999999, 10), 'ZRH': (9999999, 11), 'BUH': (9999999, 12)}
# print(city_list)
IATA_list = []
for city in city_list:
    IATA = flight_search.get_IATA_cd(city)
    IATA_list.append(IATA)

##### New sheet
### method 1 : put into a dic 
# for row in sheet_name:
#     row['iataCode'] = 'Testing'
# print(sheet_name)
### method 2 : put into a dic
# for idx, row in enumerate(sheet_name):
#     row['iataCode'] = IATA_list[idx]
# print(sheet_name)

######################## ing
##### get the lowest prices
flight_data = FlightData()
flight_info = {}
for iata in IATA_list:
    try:
        # print(f"{iata} : {flight_data.search_lowest(iata)}")
        flight_info[iata] = flight_data.search_lowest(iata)
        if flight_info[iata] < original_data[iata][0]:
            # print(iata, flight_info[iata], "Lowest")
            data_mg.update_price(obj_id = original_data[iata][1], lowest_price = flight_info[iata]) # ★
    except IndexError:
        # print(f"{iata} : No Flights")
        flight_info[iata] = int(9999999)