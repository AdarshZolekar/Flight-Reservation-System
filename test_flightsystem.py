import unittest
from flightsystem import FlightReservationSystem

class TestFlightReservationSystem(unittest.TestCase):
    def setUp(self):
        self.system = FlightReservationSystem()

    def test_search_flights(self):
        results = self.system.search_flights("Delhi")
        self.assertTrue(len(results) > 0)
        for f in results:
            self.assertEqual(f.destination.lower(), "delhi")

    def test_book_ticket_success(self):
        # AI101 has 5 seats initially
        result = self.system.book_ticket("AI101", "John Doe")
        self.assertIn("Booking successful!", result)
        self.assertEqual(len(self.system.reservations), 1)
        # Check if seat count decreased
        for f in self.system.flights:
            if f.flight_id == "AI101":
                self.assertEqual(f.seats, 4)

    def test_book_ticket_invalid_id(self):
        result = self.system.book_ticket("INVALID", "John Doe")
        self.assertEqual(result, "Invalid flight ID.")

    def test_cancel_ticket_success(self):
        # Book first
        book_result = self.system.book_ticket("AI101", "John Doe")
        ticket_id = book_result.split(": ")[1]
        
        # Cancel
        cancel_result = self.system.cancel_ticket(ticket_id)
        self.assertEqual(cancel_result, "Cancellation successful.")
        self.assertEqual(len(self.system.reservations), 0)
        # Check if seat count restored
        for f in self.system.flights:
            if f.flight_id == "AI101":
                self.assertEqual(f.seats, 5)

    def test_sort_flights_by_price(self):
        self.system.sort_flights_by_price()
        prices = [f.price for f in self.system.flights]
        self.assertEqual(prices, sorted(prices))

if __name__ == "__main__":
    unittest.main()
