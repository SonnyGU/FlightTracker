# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_stops_data()

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet: \n {sheet_data}")

    data_manager.stops = sheet_data
    data_manager.update_codes()
