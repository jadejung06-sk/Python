import requests

class DataManager:
    '''
    https://sheety.co/
    '''
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/1afdc9861c39d7aea3407072f386921c/flightDeals/prices" 
        self.sheety_api = ""
        self.sheety_token = ""

        self.response_get = requests.get(url = self.sheety_endpoint)
        self.response_post = requests.get(url = self.sheety_endpoint, json ="" )