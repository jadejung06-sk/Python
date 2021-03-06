import requests
from datetime import datetime, timedelta
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data_api = ""
        self.flight_data_endpoint = "https://tequila-api.kiwi.com/v2/search?"
        self.dateformat = "%d/%m/%Y"
        self.today = datetime.now()
        self.start_date = datetime(year = 2022, month = 12, day = 5) # need strftime
        self.delay = timedelta(days = 4)
        self.duration = timedelta(days = 12)
        self.start_delay = (self.start_date + self.delay) # need strftime
        self.comeback_date = (self.start_date + self.duration).strftime(self.dateformat) #
        self.comeback_delay = (self.start_delay + self.duration).strftime(self.dateformat) #
        self.flight_data_header = {"apikey" : self.flight_data_api}          
        
    def search_lowest(self, fly_from):
        self.flight_info_dict = {}
        self.flight_data_params = {
            "fly_from":fly_from,
            "fly_to":"SEL",
            "date_from": self.start_date.strftime(self.dateformat),
            "date_to" : self.start_date.strftime(self.dateformat),
            "return_from": self.comeback_date,
            "return_to":self.comeback_delay,
            "flight_type":"round",
            "max_stopovers":0,
            "sort":"price",
            "curr":"KRW"
        }
        self.response_data = requests.get(url = self.flight_data_endpoint, params = self.flight_data_params, headers=self.flight_data_header)
        # self.flight_info_dict[fly_from] = int(self.response_data.json()["data"][0]["price"])
        # return self.flight_info_dict
        # return int(self.response_data.json()["data"][0]["price"])
        self.flight_info_dict["flyFrom"] = self.response_data.json()["data"][0]["flyFrom"]
        self.flight_info_dict["cityFrom"] = self.response_data.json()["data"][0]["cityFrom"]
        self.flight_info_dict["price"] = self.response_data.json()["data"][0]["price"]
        self.flight_info_dict["local_arrival"] = self.response_data.json()["data"][0]["local_arrival"]
        self.flight_info_dict["local_departure"] = self.response_data.json()["data"][0]["local_departure"]
        return self.flight_info_dict
'''
return self.response_data.json()["data"][0]

{'id': '037209934b834b92d9a62140_0|037209934b834b92d9a62140_1', 'flyFrom': 'SYD', 'flyTo': 'ICN', 'cityFrom': 'Sydney', 'cityCodeFrom': 'SYD', 'cityTo': 'Seoul', 'cityCodeTo': 'SEL', 
, 'price': 1935010.0003, 'local_arrival': '2022-12-05T19:00:00.000Z', 'utc_arrival': '2022-12-05T10:00:00.000Z', 'local_departure': '2022-12-05T10:20:00.000Z', 'utc_departure': '2022-12-04T23:20:00.000Z'}

'''



        # curl -X GET "https://tequila-api.kiwi.com/v2/search?fly_from=PAR&fly_to=SEL&date_from=05%2F12%2F2022&date_to=09%2F12%2F2022&return_from=17%2F12%2F2022
        # &return_to=24%2F12%2F2022&flight_type=round&adults=2&selected_cabins=M&adult_hold_bag=1%2C1&adult_hand_bag=1%2C1&curr=KRW&max_stopovers=0&
        # max_sector_stopovers=0&vehicle_type=aircraft&sort=price" -H  "accept: application/json" -H  "apikey: 1GL3D1WH9uJ0PSa6JweEAfbmD9THOv5m"

# if __name__ == "__main__":
#     debug = FlightData()
#     # print(debug.start_date, debug.start_delay)
#     # print("===")
#     # print(debug.comeback_date, debug.comeback_delay)
#     test_list = ['SYD', 'NYC', 'SFO', 'SEL', 'GMP', 'ICN', 'ROM', 'ZRH', 'BUH']
#     for test in test_list:
#         print(debug.search_lowest(fly_from=test))
