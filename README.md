# Flight Reservation System

A simple Data Structures based Python project to simulate basic flight booking operations.
It allows users to view flights, search by destination, sort by price, book or cancel tickets and view reservations — all through a console menu. This project was developed as a mini project for the Data Structures subject as part of the Computer Engineering curriculum at Savitribai Phule Pune University (SPPU).

---

## Features

- View all available flights

- Search flights by destination

- Sort flights by ticket price (Bubble Sort implementation)

- Book and cancel tickets

- Display all reservations (passenger name and flight ID)

- Validation for seat availability and valid flight/ticket IDs

- Interactive console-based menu

---

## Concepts Used

- Object-Oriented Programming (Encapsulation, Classes, Objects)

- Python Collections (list, dictionary)

- Looping and Conditional Logic

- UUID generation for unique ticket IDs

- Sorting Algorithm (Bubble Sort)

---

## Data Structures Used

- List (Dynamic Array) – Stores flight objects in an ordered collection.

- Dictionary (Hashing) – Maps unique ticket IDs to reservation details.

- Class & Objects (OOP Structure) – Encapsulate flight and system data.

- Loops & Conditionals – Control logic for searching, sorting and validation.

- UUID – Generates unique ticket identifiers for each booking.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/AdarshZolekar/Flight-Reservation-System.git
cd Flight-Reservation-System
```

2. Run the program:
```
python flightsystem.py

---

## Sample Output

```bash
••• Flight Reservation System •••
1. View All Flights
2. Search Flights by Destination
3. Sort Flights by Price
4. Book Ticket
5. Cancel Ticket
6. Show Reservations
7. Exit
Enter choice: 1
AI101 | Pune → Delhi | ₹4500 | Seats: 5
AI102 | Pune → Bangalore | ₹3500 | Seats: 3
AI103 | Pune → Chennai | ₹4000 | Seats: 4
AI104 | Mumbai → Delhi | ₹4200 | Seats: 2
AI105 | Delhi → Kolkata | ₹3800 | Seats: 6

Enter choice: 4
Enter Flight ID: AI102
Enter Passenger Name: Adarsh
Booking successful! Ticket ID: a1b2c3d4

Enter choice: 6
Ticket ID: a1b2c3d4 | Passenger: Adarsh | Flight: AI102

Enter choice: 7
Exiting system.
```
---

## Requirements

- Python 3.8+

- No external dependencies required

---

## Future Improvements

- Add date and time for flights

- Integrate passenger details (age, ID proof, etc.)

- Store flight and booking data in a CSV or database

- Add GUI using Tkinter or PyQt

- Implement seat selection and cancellation charges

---

## License

This project is open-source under the MIT License.

---

## Contributions

Feel free to open issues or submit pull requests for improvements or bug fixes!


<p align="center">
  <a href="#top">
    <img src="https://img.shields.io/badge/%E2%AC%86-Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top"/>
  </a>
</p>
