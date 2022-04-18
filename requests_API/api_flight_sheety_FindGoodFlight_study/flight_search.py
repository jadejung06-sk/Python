import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    '''https://tequila.kiwi.com/portal/docs/tequila_api/search_api'''
    def __init__(self):
        self.flightsearch_api = "1GL3D1WH9uJ0PSa6JweEAfbmD9THOv5m"
        self.flightsearch_endpoint = "https://tequila-api.kiwi.com/"
        self.dateformat = "%d/%m/%Y"
        self.flightlocation_endpoint = f"{self.flightsearch_endpoint}locations/query?"

    def get_IATA_cd(self, city_name):
        self.loc_headers = {"apikey": self.flightsearch_api}
        self.loc_params = {"term" : city_name, "limit": 1}
        self.location= requests.get(url = self.flightlocation_endpoint, params=self.loc_params, headers=self.loc_headers)
        return self.location.json()["locations"][0]["code"]
        # return self.location.json()["locations"][0]

# if __name__ == "__main__":
    # debug = FlightSearch()
    # print(debug.get_IATA_cd(city_name = "Zurich"))
# 