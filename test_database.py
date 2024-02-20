"""Test module for the Mobi DB."""
import unittest
from database import ReservationDB

class TestDB(unittest.TestCase):
    """Test class for the Mobi DB."""

    def test_make(self):
        "Test DB constructor."
        db = ReservationDB()
        self.assertEqual(0, db.count_flights())

    def test_load_data_json(self):
        "Test `load_data` method."
        db = ReservationDB()
        db.load_data("test_reservation_data.json")
        self.assertEqual(2, db.count_flights())

        fl = db.lookup_flight("aa311")
        self.assertIsNotNone(fl)
        self.assertEqual(2, fl.count_passengers())

    def test_load_data_jsonl(self):
        "Test `load_data` method."
        db = ReservationDB()
        db.load_data("test_reservation_data.jsonl")
        self.assertEqual(2, db.count_flights())

        fl = db.lookup_flight("aa311")
        self.assertIsNotNone(fl)
        self.assertEqual(2, fl.count_passengers())

    def test_lookup_flight(self):
        "Test `lookup_flight` method."
        db = ReservationDB()
        db.load_data("test_reservation_data.json")

        fl = db.lookup_flight("aa311")
        self.assertIsNotNone(fl)
        self.assertEqual("aa311", fl.code)

        fl = db.lookup_flight("AA311")
        self.assertIsNotNone(fl)
        self.assertEqual("aa311", fl.code)

        self.assertIsNone(db.lookup_flight("foo9999"))

    def test_scan_passenger(self):
        "Test the `scan_passenger`."

        db = ReservationDB()
        db.load_data("test_reservation_data.json")
        fl = db.lookup_flight('aa311')
        self.assertIsNotNone(fl)
        self.assertEqual(2, fl.count_passengers())
        self.assertEqual(0, fl.count_scanned_passengers())
        self.assertTrue(fl.scan_passenger('WDXDIC'))
        self.assertEqual(2, fl.count_passengers())
        self.assertEqual(1, fl.count_scanned_passengers())

        self.assertFalse(fl.scan_passenger('WDXDIC'))
        self.assertEqual(2, fl.count_passengers())
        self.assertEqual(1, fl.count_scanned_passengers())

        self.assertTrue(fl.scan_passenger('aciwmy'))
        self.assertEqual(2, fl.count_passengers())
        self.assertEqual(2, fl.count_scanned_passengers())
        self.assertFalse(fl.scan_passenger('aciwmy'))

        self.assertFalse(fl.scan_passenger('NAQMBF'))
