from taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100,
                   1.23)  # Create a new taxi object, my_taxi, with the name "Prius 1", 100 units of fuel, and a price of $1.23
    my_taxi.drive(40)  # Drive 40km
    print(f"Taxi details: {my_taxi};\nCost: ${my_taxi.get_fare()}")  # Print taxi details and current fair
    my_taxi.start_fare()  # Start a new fare
    my_taxi.drive(100)  # Drive 100km
    print(f"Taxi details: {my_taxi};\nCost: ${my_taxi.get_fare()}")  # Print taxi details and current fair


main()
