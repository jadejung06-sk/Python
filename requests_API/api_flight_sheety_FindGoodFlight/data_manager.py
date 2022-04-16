import requests
from flight_search import FlightSearch

class DataManager(FlightSearch):
    '''
    https://sheety.co/
    '''
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/1afdc9861c39d7aea3407072f386921c/flightDeals/prices"
        self.sheety_put_endpoint = f"https://api.sheety.co/1afdc9861c39d7aea3407072f386921c/flightDeals/prices/"
        self.sheety_api = ""
        self.sheety_token = ""
        # self.post_params = {"price" : {"city":"Test",
        # "iataCode":"TST", "lowestPrice":0}}
        # self.response_post = requests.post(url = self.sheety_endpoint, json = self.post_params)
        super().__init__()

    def update_sheet(self):
        self.response_get = requests.get(url = self.sheety_endpoint)
        self.sheet_name = self.response_get.json()["prices"]
        self.city_list = []
        for self.data in self.sheet_name:
            self.city_list.append(self.data["city"])
        self.IATA_list = []
        for self.city in self.city_list:
            self.IATA = self.get_IATA_cd(self.city)
            self.IATA_list.append(self.IATA)
        for self.idx, self.row in enumerate(self.sheet_name):
            self.row['iataCode'] = self.IATA_list[self.idx]
        # return self.sheet_name
        ### update iata data
        for obj_id in range(2, len(self.sheet_name)+2): # id 2 ~ 12
           self.put_params = {"price" : self.sheet_name[obj_id -2]}
           self.response_put = requests.put(url = f"{self.sheety_put_endpoint}{obj_id}", json =self.put_params)
        return self.response_put

if __name__=="__main__":
    debug = DataManager()
    # print(debug.response_get.json()["prices"])
    print(debug.update_sheet())
    # print(debug.response_post.json())