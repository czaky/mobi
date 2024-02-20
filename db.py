"""Implementation of passenger flight database."""

import json
from typing import Optional

class Flight:
    """Represents a single flight in the database."""

    def __init__(self, code):
        self.code = code
        self.passengers = {}

    def add_passenger(self, passenger):
        "Add `passenger` to the flight."
        passenger["scanned"] = False
        pnr = passenger["reservation_code"]
        self.passengers[pnr] = passenger

    def scan_passenger(self, pnr: str) -> bool:
        "Scans `pnr` and marks it as scanned."
        pax = self.passengers.get(pnr)
        if pax and not pax["scanned"]:
            pax["scanned"] = True
            return True
        return False

class ReservationDB:
    """Implementation of passenger flight database."""

    def __init__(self):
        self.flights = {}

    def load_data(self, data_file_name: str):
        "Load data from JSON `data_file_name`."
        with open(data_file_name, encoding="utf8") as data_file:
            data = json.load(data_file)
        for pax in data["records"]:
            flight_code = pax["flight_number"]
            flight = self.flights.get(flight_code)
            if not flight:
                flight = self.flights.setdefault(
                    flight_code, Flight(flight_code))
            flight.add_passenger(pax)

    def lookup_flight(self, flight_code: str) -> Optional[Flight]:
        "Lookup the flight by `flight_code` return a dictionary of `pnr` to reservation."
        return self.flights.get(flight_code)
