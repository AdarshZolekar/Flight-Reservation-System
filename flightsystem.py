import uuid

class Flight:
    def __init__(self, flight_id, source, destination, price, seats):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price
        self.seats = seats

    def __repr__(self):
        return f"{self.flight_id} | {self.source} → {self.destination} | ₹{self.price} | Seats: {self.seats}"


class FlightReservationSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Pune", "Delhi", 4500, 5),
            Flight("AI102", "Pune", "Bangalore", 3500, 3),
            Flight("AI103", "Pune", "Chennai", 4000, 4),
            Flight("AI104", "Mumbai", "Delhi", 4200, 2),
            Flight("AI105", "Delhi", "Kolkata", 3800, 6)
        ]
        self.reservations = {}

    def search_flights(self, destination):
        return [f for f in self.flights if f.destination.lower() == destination.lower()]

    def sort_flights_by_price(self):
        n = len(self.flights)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.flights[j].price > self.flights[j + 1].price:
                    self.flights[j], self.flights[j + 1] = self.flights[j + 1], self.flights[j]

    def book_ticket(self, flight_id, passenger_name):
        for f in self.flights:
            if f.flight_id == flight_id:
                if f.seats > 0:
                    f.seats -= 1
                    ticket_id = str(uuid.uuid4())[:8]
                    self.reservations[ticket_id] = {"passenger": passenger_name, "flight": f.flight_id}
                    return f"Booking successful! Ticket ID: {ticket_id}"
                else:
                    return "No seats available."
        return "Invalid flight ID."

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.reservations:
            flight_id = self.reservations[ticket_id]["flight"]
            for f in self.flights:
                if f.flight_id == flight_id:
                    f.seats += 1
                    break
            del self.reservations[ticket_id]
            return "Cancellation successful."
        return "Invalid ticket ID."

    def show_reservations(self):
        if not self.reservations:
            print("No reservations found.")
        else:
            for t_id, details in self.reservations.items():
                print(f"Ticket ID: {t_id} | Passenger: {details['passenger']} | Flight: {details['flight']}")

    def show_all_flights(self):
        for f in self.flights:
            print(f)


def main():
    system = FlightReservationSystem()

    while True:
        print("••• Flight Reservation System •••")
        print("1. View All Flights")
        print("2. Search Flights by Destination")
        print("3. Sort Flights by Price")
        print("4. Book Ticket")
        print("5. Cancel Ticket")
        print("6. Show Reservations")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.show_all_flights()
        elif choice == "2":
            dest = input("Enter destination: ")
            flights = system.search_flights(dest)
            if flights:
                for f in flights:
                    print(f)
            else:
                print("No flights found.")
        elif choice == "3":
            system.sort_flights_by_price()
            print("Flights sorted by price.")
        elif choice == "4":
            fid = input("Enter Flight ID: ")
            name = input("Enter Passenger Name: ")
            print(system.book_ticket(fid, name))
        elif choice == "5":
            tid = input("Enter Ticket ID: ")
            print(system.cancel_ticket(tid))
        elif choice == "6":
            system.show_reservations()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
