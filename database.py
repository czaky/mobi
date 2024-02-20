"""Implementation of passenger flight database."""

import json
from typing import Optional

class Flight:
    """
Represents a single flight in the database.

Contains all the relevant `pnr` records.
"""

    def __init__(self, code):
        # Flight code (airline + flight_number)
        self.code = code
        # Keyed on pax pnr-code; contains pax records.
        self.passengers = {}

    def add_passenger(self, passenger):
        "Add `passenger` to the flight. Thread unsafe."
        # Create field `scanned` on the pnr-record.
        passenger['scanned'] = False
        pnr = passenger['reservation_code']
        self.passengers[pnr.lower()] = passenger

    def scan_passenger(self, pnr: str) -> bool:
        "Scans `pnr` and marks it as scanned. Thread unsafe."
        pax = self.passengers.get(pnr.lower())
        if pax and not pax['scanned']:
            # Update the `scanned` field.
            pax['scanned'] = True
            return True
        return False

    def count_passengers(self) -> int:
        "How many passengers are on the flight?"
        return len(self.passengers)

    def count_scanned_passengers(self) -> int:
        "How many passengers have been scanned?"
        return sum(
            pnr['scanned'] for pnr in self.passengers.values())

class ReservationDB:
    "Passenger flight database."

    def __init__(self):
        self.flights = {}

    def load_data(self, data_file_name: str):
        "Load data from JSON `data_file_name`."
        records = []
        with open(data_file_name, encoding='utf8') as data_file:
            if data_file_name.lower().endswith(".json"):
                records = json.load(data_file)['records']
            elif data_file_name.lower().endswith(".jsonl"):
                records = list(map(json.loads, data_file))
            else:
                print(f'ERROR: unrecognized file format: {data_file_name}. ')
                print('ERROR: need ".json" or ".jsonl" extension.')

        print(f'Loading {len(records)} passenger records from: "{data_file_name}"')
        for pnr in records:
            flight_code = pnr['flight_number'].lower()
            flight = self.flights.get(flight_code)
            if not flight:
                flight = self.flights.setdefault(
                    flight_code, Flight(flight_code))
            flight.add_passenger(pnr)

    def lookup_flight(self, flight_code: str) -> Optional[Flight]:
        "Lookup the flight by `flight_code`."
        return self.flights.get(flight_code.lower())

    def count_flights(self) -> int:
        "Returns number of flights in the database."
        return len(self.flights)
