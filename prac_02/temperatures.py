"""
Convert from °C -> °F or vise versa.
"""

# CONSTANTS
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Main function to get a temperature from user input and convert it."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit):
    """Convert from Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert from Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
