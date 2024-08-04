from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").upper()

    while menu_choice != 'Q':
        if menu_choice == 'C':
            # Choose a taxi
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = get_valid_choice(taxis, total_bill)
            current_taxi = taxis[taxi_choice]
        elif menu_choice == 'D':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                total_bill += fare
                # Move the fare reset to before a new drive
                current_taxi.start_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_choice(taxis, total_bill):
    """Get a valid taxi choice from the user."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxi_choice
        else:
            print("Invalid taxi choice")
            print(f"Bill to date: ${total_bill:.2f}")
            return get_valid_choice(taxis, total_bill)
    except ValueError:
        print("Invalid taxi choice")
        print(f"Bill to date: ${total_bill:.2f}")
        return get_valid_choice(taxis, total_bill)


def drive_taxi(taxi):
    """Drive the chosen taxi and calculate fare."""
    try:
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
    except ValueError:
        print("Invalid distance entered.")
        drive_taxi(taxi)


if __name__ == "__main__":
    main()
