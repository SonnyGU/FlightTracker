import requests
from IPython.lib.pretty import pprint

sheety_endpoint = "https://api.sheety.co/7fe796b00789ab35642be56f51df98a0/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.stops = {}

    def get_stops_data(self):
        response = requests.get(url=sheety_endpoint)
        response.raise_for_status()
        sheety_data = response.json()
        self.stops = sheety_data["prices"]
        pprint(self.stops)
        return self.stops

    def update_codes(self):
        for city in self.stops:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}",
                                    json=new_data)
            print(response.text)
