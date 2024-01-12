class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.passengers = []

    def check_availability(self):
        # Method to check the availability of seats on the flight
        return self.capacity - len(self.passengers)

    def book_flight(self, passenger):
        # Method to book a seat for a passenger on the flight
        if self.check_availability() > 0:
            self.passengers.append(passenger)
            print(f"Reservation successful for {passenger.name} on Flight {self.flight_number}.")
        else:
            print("Sorry, the flight is fully booked.")

class Passenger:
    def __init__(self, name, age, passport_number):
        self.name = name
        self.age = age
        self.passport_number = passport_number

class Reservation:
    def __init__(self, flight, passenger):
        self.flight = flight
        self.passenger = passenger

    def display_reservation_details(self):
        # Method to display reservation details
        print("Reservation Details:")
        print(f"Flight Number: {self.flight.flight_number}")
        print(f"Passenger Name: {self.passenger.name}")
        print(f"Origin: {self.flight.origin}")
        print(f"Destination: {self.flight.destination}")
        print(f"Departure Time: {self.flight.departure_time}")

# Example usage:
flight1 = Flight("F123", "New York", "Los Angeles", "2024-02-01 08:00", 100)
passenger1 = Passenger("John Doe", 30, "AB123456")
reservation1 = Reservation(flight1, passenger1)

flight1.book_flight(passenger1)
flight1.book_flight(Passenger("Jane Smith", 25, "CD789012"))

reservation1.display_reservation_details()