"""
Estimated time for guitars.py: 25 minutes
Actual time: 1h45min
"""

from prac_06.guitar import Guitar
from operator import itemgetter

YEAR_INDEX = 1


def main():
    """Get a list of guitars and related information from the user, sort by release year and print completed list."""
    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name=name, year=year, cost=cost))
        print(f"{name} ({year}) : ${cost:,.2f} added. \n")
        name = input("Name: ")

    guitars_tuples = [(guitar.name, guitar.year, guitar.cost) for guitar in guitars]
    guitars_tuples.sort(key=itemgetter(YEAR_INDEX))
    guitars_sorted = [Guitar(name, year, cost) for name, year, cost in guitars_tuples]

    max_name_length = max(len(guitar.name) for guitar in guitars_sorted)
    max_cost_string_length = max(len(str(f"{guitar.cost},.2f")) for guitar in guitars_sorted)
    print("\nThese are my guitars: ")
    for i, guitar in enumerate(guitars_sorted, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2024) else ""
        print(
            f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), "
            f"worth ${guitar.cost:{max_cost_string_length},.2f}{vintage_string}"
        )


if __name__ == '__main__':
    main()
