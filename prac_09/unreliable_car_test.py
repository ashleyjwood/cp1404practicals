from unreliable_car import UnreliableCar


def main():
    """Demo the UnreliableCar class."""
    car = UnreliableCar("Ol' Unreliable", 100, 40)
    car.drive(40)
    print(f"Car details: {car}")


# Run the main function a number of times to test the reliability factor
i = 0
while i < 10:
    main()
    i += 1
