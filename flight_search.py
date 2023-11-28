import requests
import os

# Loads sensitive data from environment variable
flight_endpoint = "https://api.tequila.kiwi.com/v2"
# API endpoint for Tequila
FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY")


class FlightSearch:
    def get_destination_code(self, city):
        test = "Test"
        return test
