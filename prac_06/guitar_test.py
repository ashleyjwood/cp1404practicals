"""
Estimated time for guitar.py and guitar_test.py: 30 minutes
Actual time: ~60 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Main docstring"""
    current_year = int(input("Enter current year: "))

    guitar = Guitar(name="Gibson L-5 CES", year=1951, cost=16035.40)  # Corrected release year
    print(f"{guitar.name} get_age() - Expected 71 (Assuming year is 2022). Got {guitar.get_age(current_year)}.")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage(current_year)}.")
    print("")  # Blank line for readability

    guitar = Guitar(name="Another Guitar", year=2013)
    print(f"{guitar.name} get_age() - Expected 9 (Assuming year is 2022). Got {guitar.get_age(current_year)}.")
    print(f"{guitar.name} is_vintage() - Expected False. Got {guitar.is_vintage(current_year)}.")


if __name__ == '__main__':
    main()
