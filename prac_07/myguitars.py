"""
A program to add and track your guitars and sort them from oldest to newest.
"""

from guitar import Guitar

FILENAME = "guitars.csv"

MENU = """Menu:
D - Display guitars
A - Add a new guitar
Q - Quit"""


def main():
    """Add and track your guitars and sort them from oldest to newest."""
    guitars = load_guitar_list()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            print_guitar_list(guitars)
        elif choice == "A":
            add_guitar(guitars)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_guitar_list(guitars)


def load_guitar_list():
    """Read guitars from a CSV file."""
    guitars = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as in_file:
            for line in in_file:
                name, year, cost = line.split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
            guitars.sort()
            print(f"{len(guitars)} guitars loaded.")
    except FileNotFoundError:
        print(f"{FILENAME} not found.")
    return guitars


def get_valid_string(prompt):
    """Get a non-empty string from the user."""
    string = input(prompt)
    while not string:
        print("Input can not be blank")
        string = input(prompt)
    return string


def get_valid_number(prompt):
    """Get a number from the user which is greater than zero."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("Input must be > 0")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number


def get_valid_guitar_year(prompt):
    """Get a valid guitar year from the user."""
    is_valid_year = False
    while not is_valid_year:
        try:
            year = int(input(prompt))
            if year < 1500 or year > 2024:
                print("Input must be between 1500 and 2024 inclusive")
            else:
                is_valid_year = True
        except ValueError:
            print("Invalid input - please enter a valid year")
    return year


def add_guitar(guitars):
    """Add a new guitar to the guitar list and sort the list based on year and name."""
    name = get_valid_string("Name: ")
    year = get_valid_guitar_year("Year: ")
    cost = get_valid_number("Cost: ")

    guitars.append(Guitar(name, year, cost))
    guitars.sort()
    print(f"{name} ({year}) : ${cost:,.2f} added.")


def print_guitar_list(guitars):
    """Print the guitar list and information about the guitars in columns."""
    if not guitars:
        print("No guitars in the list.")
    else:
        # Determine the max length of name and cost for formatting
        max_name_length = max(len(guitar.name) for guitar in guitars)
        max_cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

        # Print the header
        print(f"{'Name':<{max_name_length}} {'Year':<6} {'Cost':>{max_cost_length}}")
        print("-" * (max_name_length + max_cost_length + 9))
        for guitar in guitars:
            print(f"{guitar.name:<{max_name_length}} {guitar.year:<6} $ {guitar.cost:>{max_cost_length},.2f}")


def save_guitar_list(guitars):
    """Save the guitar list to a CSV file."""
    with open(FILENAME, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print(f"{len(guitars)} guitars saved to {FILENAME}")


if __name__ == '__main__':
    main()
